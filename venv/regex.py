import re

EMAIL_REGEX = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
CPF_REGEX = re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b")
DOMAIN_REGEX = re.compile(r"\b[a-zA-Z0-9-]+\.(com|net|org|br|gov|edu)\b")
PASSWORD_REGEX = re.compile(r"(?=.*[a-zA-Z])(?=.*\d).{6,}")  # simples
