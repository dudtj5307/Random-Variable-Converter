from utils.anonymizer import anonymize_code, restore_code, generate_alias
from utils.extractor import extract_declared_variables
from utils.keywords import CPP_KEYWORDS, IDENTIFIER_RE

__all__ = [
    "anonymize_code",
    "restore_code",
    "generate_alias",
    "extract_declared_variables",
    "CPP_KEYWORDS",
    "IDENTIFIER_RE",
]