"""PAdES signing and verification of rendered PDFs, and generation of the signing key.

The release pipeline signs every PDF with the ISMS document-control key, a PKCS#12 file stored as
a CI secret (``ISMS_SIGNING_P12``, base64) with its passphrase (``ISMS_SIGNING_PASSPHRASE``). When
no key is configured -- local builds, forks -- an ephemeral key is generated whose common name
says loudly that it is untrusted, so a signed PDF never *looks* more authoritative than it is.
Private keys are never written to the repository.
"""

from __future__ import annotations

import base64
import os
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.x509.oid import NameOID

try:  # pragma: no cover - import guard exercised by environments without the pdf extra
    from pyhanko import keys as pyhanko_keys
    from pyhanko import stamp
    from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
    from pyhanko.pdf_utils.reader import PdfFileReader
    from pyhanko.pdf_utils.text import TextBoxStyle
    from pyhanko.sign import fields, signers
    from pyhanko.sign.validation import validate_pdf_signature
    from pyhanko_certvalidator import ValidationContext
    from pyhanko_certvalidator.registry import SimpleCertificateStore

    SIGNING_AVAILABLE = True
except ImportError:  # pragma: no cover
    SIGNING_AVAILABLE = False

__all__ = [
    "SIGNING_AVAILABLE",
    "P12_ENV",
    "PASSPHRASE_ENV",
    "DEV_COMMON_NAME",
    "KeyMaterial",
    "generate_key_material",
    "to_pkcs12",
    "from_pkcs12",
    "load_key_material",
    "sign_pdf",
    "SignatureReport",
    "verify_pdf",
]

P12_ENV = "ISMS_SIGNING_P12"
PASSPHRASE_ENV = "ISMS_SIGNING_PASSPHRASE"
DEV_COMMON_NAME = "ISMS Document Control - UNTRUSTED DEVELOPMENT KEY"
FIELD_NAME = "ISMSDocumentControl"
# The reserved band at the bottom of the cover page (PDF user units, origin bottom-left).
STAMP_BOX = (318, 28, 544, 122)


@dataclass(frozen=True)
class KeyMaterial:
    """Signing certificate, its private key and the issuing CA that anchors trust."""

    certificate_pem: bytes
    private_key_pem: bytes
    trust_anchor_pem: bytes
    subject: str
    ephemeral: bool


def _name(common_name: str, organisation: str) -> x509.Name:
    return x509.Name(
        [
            x509.NameAttribute(NameOID.COMMON_NAME, common_name),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, organisation),
        ]
    )


def _key_usage(*, ca: bool) -> x509.KeyUsage:
    return x509.KeyUsage(
        digital_signature=not ca,
        content_commitment=not ca,
        key_encipherment=False,
        data_encipherment=False,
        key_agreement=False,
        key_cert_sign=ca,
        crl_sign=ca,
        encipher_only=False,
        decipher_only=False,
    )


def generate_key_material(
    common_name: str, organisation: str, days: int = 3650, ephemeral: bool = False
) -> KeyMaterial:
    """Create an issuing CA (the trust anchor) and a P-256 signing certificate issued by it."""
    now = datetime.now(UTC)
    ca_key = ec.generate_private_key(ec.SECP256R1())
    ca_name = _name(f"{common_name} CA", organisation)
    ca_cert = (
        x509.CertificateBuilder()
        .subject_name(ca_name)
        .issuer_name(ca_name)
        .public_key(ca_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - timedelta(minutes=5))
        .not_valid_after(now + timedelta(days=days + 1))
        .add_extension(x509.BasicConstraints(ca=True, path_length=0), critical=True)
        .add_extension(_key_usage(ca=True), critical=True)
        .add_extension(
            x509.SubjectKeyIdentifier.from_public_key(ca_key.public_key()), critical=False
        )
        .sign(ca_key, hashes.SHA256())
    )
    key = ec.generate_private_key(ec.SECP256R1())
    certificate = (
        x509.CertificateBuilder()
        .subject_name(_name(common_name, organisation))
        .issuer_name(ca_name)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - timedelta(minutes=5))
        .not_valid_after(now + timedelta(days=days))
        .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
        .add_extension(_key_usage(ca=False), critical=True)
        .add_extension(x509.SubjectKeyIdentifier.from_public_key(key.public_key()), critical=False)
        .add_extension(
            x509.AuthorityKeyIdentifier.from_issuer_public_key(ca_key.public_key()), critical=False
        )
        .sign(ca_key, hashes.SHA256())
    )
    return KeyMaterial(
        certificate_pem=certificate.public_bytes(serialization.Encoding.PEM),
        private_key_pem=key.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.PKCS8,
            serialization.NoEncryption(),
        ),
        trust_anchor_pem=ca_cert.public_bytes(serialization.Encoding.PEM),
        subject=certificate.subject.rfc4514_string(),
        ephemeral=ephemeral,
    )


def to_pkcs12(material: KeyMaterial, passphrase: str) -> bytes:
    key = serialization.load_pem_private_key(material.private_key_pem, password=None)
    certificate = x509.load_pem_x509_certificate(material.certificate_pem)
    anchor = x509.load_pem_x509_certificate(material.trust_anchor_pem)
    return pkcs12.serialize_key_and_certificates(
        name=b"isms-document-control",
        key=key,  # type: ignore[arg-type]
        cert=certificate,
        cas=[anchor],
        encryption_algorithm=serialization.BestAvailableEncryption(passphrase.encode("utf-8")),
    )


def from_pkcs12(data: bytes, passphrase: str | None) -> KeyMaterial:
    key, certificate, chain = pkcs12.load_key_and_certificates(
        data, passphrase.encode("utf-8") if passphrase else None
    )
    if key is None or certificate is None:
        raise ValueError("the PKCS#12 file does not contain a private key and a certificate")
    if not chain:
        raise ValueError("the PKCS#12 file must include the issuing CA certificate (trust anchor)")
    return KeyMaterial(
        certificate_pem=certificate.public_bytes(serialization.Encoding.PEM),
        private_key_pem=key.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.PKCS8,
            serialization.NoEncryption(),
        ),
        trust_anchor_pem=b"".join(c.public_bytes(serialization.Encoding.PEM) for c in chain),
        subject=certificate.subject.rfc4514_string(),
        ephemeral=False,
    )


def load_key_material(
    p12_path: Path | None = None,
    passphrase: str | None = None,
    env: Mapping[str, str] | None = None,
) -> KeyMaterial:
    """Resolve the signing key: explicit file -> ``ISMS_SIGNING_P12`` -> ephemeral dev key."""
    environment = os.environ if env is None else env
    secret = passphrase or environment.get(PASSPHRASE_ENV)
    if p12_path is not None:
        return from_pkcs12(p12_path.read_bytes(), secret)
    encoded = environment.get(P12_ENV)
    if encoded:
        return from_pkcs12(base64.b64decode(encoded), secret)
    return generate_key_material(DEV_COMMON_NAME, "isms-as-code local build", ephemeral=True)


def _simple_signer(material: KeyMaterial) -> signers.SimpleSigner:
    certificate = next(iter(pyhanko_keys.load_certs_from_pemder_data(material.certificate_pem)))
    key = pyhanko_keys.load_private_key_from_pemder_data(material.private_key_pem, passphrase=None)
    registry = SimpleCertificateStore()  # type: ignore[no-untyped-call]
    registry.register(certificate)
    for anchor in pyhanko_keys.load_certs_from_pemder_data(material.trust_anchor_pem):
        registry.register(anchor)
    return signers.SimpleSigner(signing_cert=certificate, signing_key=key, cert_registry=registry)


def sign_pdf(
    source: Path,
    destination: Path,
    material: KeyMaterial,
    *,
    reason: str,
    location: str,
    contact: str = "",
) -> None:
    """Apply a PAdES signature with a visible stamp on the cover page."""
    if not SIGNING_AVAILABLE:  # pragma: no cover - guarded by callers
        raise RuntimeError("signing needs the 'pdf' extra: uv sync --extra pdf")
    footer = (
        "UNTRUSTED DEVELOPMENT KEY - not a controlled copy"
        if material.ephemeral
        else "ISMS document control"
    )
    metadata = signers.PdfSignatureMetadata(
        field_name=FIELD_NAME,
        reason=reason,
        location=location,
        contact_info=contact or None,
        subfilter=fields.SigSeedSubFilter.PADES,
        md_algorithm="sha256",
    )
    style = stamp.TextStampStyle(
        stamp_text="Digitally signed by\n%(signer)s\n%(ts)s\n" + footer,
        border_width=1,
        text_box_style=TextBoxStyle(font_size=8),
    )
    spec = fields.SigFieldSpec(sig_field_name=FIELD_NAME, on_page=0, box=STAMP_BOX)
    pdf_signer = signers.PdfSigner(
        metadata, signer=_simple_signer(material), stamp_style=style, new_field_spec=spec
    )
    temporary = destination.with_suffix(destination.suffix + ".signing")
    with source.open("rb") as handle, temporary.open("wb") as output:
        pdf_signer.sign_pdf(IncrementalPdfFileWriter(handle), output=output)
    temporary.replace(destination)


@dataclass(frozen=True)
class SignatureReport:
    path: Path
    signed: bool
    intact: bool = False
    valid: bool = False
    trusted: bool = False
    anchored: bool = False
    signer: str = ""
    signing_time: datetime | None = None
    coverage: str = ""
    reason: str = ""
    detail: str = ""

    @property
    def ok(self) -> bool:
        """Signature present, cryptographically valid over the whole file; trusted if anchored."""
        whole = self.coverage == "ENTIRE_FILE"
        return (
            self.signed
            and self.intact
            and self.valid
            and whole
            and (self.trusted or not self.anchored)
        )

    def summary(self) -> str:
        if not self.signed:
            return f"{self.path.name}: NOT SIGNED"
        trust = "trusted" if self.trusted else ("UNTRUSTED" if self.anchored else "unanchored")
        state = "valid" if self.intact and self.valid else "INVALID"
        when = self.signing_time.isoformat(timespec="seconds") if self.signing_time else "?"
        return (
            f"{self.path.name}: {state}, {trust}, {self.coverage.lower()}, {self.signer} @ {when}"
        )


def verify_pdf(path: Path, trust_pem: bytes | None = None) -> SignatureReport:
    """Validate the newest signature of ``path``; ``trust_pem`` anchors trust to a certificate."""
    if not SIGNING_AVAILABLE:  # pragma: no cover - guarded by callers
        raise RuntimeError("verification needs the 'pdf' extra: uv sync --extra pdf")
    with path.open("rb") as handle:
        reader = PdfFileReader(handle)
        embedded = reader.embedded_signatures
        if not embedded:
            return SignatureReport(path=path, signed=False)
        signature = embedded[-1]
        if trust_pem:
            roots = list(pyhanko_keys.load_certs_from_pemder_data(trust_pem))
        else:
            # No anchor given: trust the issuing certificates embedded in the signature itself,
            # which proves integrity but says nothing about who signed.
            roots = list(signature.other_embedded_certs) or [signature.signer_cert]
        context = ValidationContext(
            trust_roots=roots, allow_fetching=False, revocation_mode="soft-fail"
        )
        try:
            status = validate_pdf_signature(signature, context)
        except Exception as exc:  # pyhanko raises on unresolvable paths and malformed signatures
            return SignatureReport(
                path=path,
                signed=True,
                anchored=trust_pem is not None,
                signer=str(signature.signer_cert.subject.human_friendly),
                signing_time=signature.self_reported_timestamp,
                reason=str(signature.sig_object.get("/Reason", "")),
                detail=f"validation failed: {exc}",
            )
        trusted = bool(getattr(status, "trusted", status.trust_problem_indic is None))
        reported = signature.self_reported_timestamp
        return SignatureReport(
            path=path,
            signed=True,
            intact=bool(status.intact),
            valid=bool(status.valid),
            trusted=trusted,
            anchored=trust_pem is not None,
            signer=str(signature.signer_cert.subject.human_friendly),
            signing_time=reported,
            coverage=status.coverage.name if status.coverage is not None else "",
            reason=str(signature.sig_object.get("/Reason", "")),
            detail=status.summary(),
        )
