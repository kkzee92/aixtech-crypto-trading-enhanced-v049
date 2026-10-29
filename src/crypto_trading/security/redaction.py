"""Secret redaction and synthetic data helpers."""

import re

SECRET_PATTERNS = [
    re.compile(r"sk-[a-zA-Z0-9]{20,}"),  # API keys
    re.compile(r"[0-9a-fA-F]{64}"),  # private keys style
    re.compile(r"\b\d{9}\b"),  # NRIC-like
]

def redact(text: str) -> str:
    for pat in SECRET_PATTERNS:
        text = pat.sub("[REDACTED]", text)
    return text
