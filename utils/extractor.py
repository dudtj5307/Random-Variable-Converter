import re
from utils.keywords import CPP_KEYWORDS, CSHARP_KEYWORDS


# ── 문자열·주석 제거용 패턴 ─────────────────────────────────────────────────
_STRIP_PATTERN = re.compile(
    r'//[^\n]*'               # 한 줄 주석
    r'|/\*.*?\*/'             # 블록 주석
    r'|"(?:[^"\\]|\\.)*"'     # 문자열 리터럴
    r"|'(?:[^'\\]|\\.)*'",    # 문자 리터럴
    re.DOTALL,
)

_PREPROCESSOR_PATTERN = re.compile(r'^\s*#[^\n]*', re.MULTILINE)
_NUMBER_PATTERN = re.compile(r'\b\d[\dA-Fa-fxXbBoOuUlL.eE_]*\b')
_IDENT_RE = re.compile(r'\b([A-Za-z_][A-Za-z0-9_]*)\b')


def _strip_literals_and_comments(code: str) -> str:
    code = _STRIP_PATTERN.sub(' ', code)
    code = _PREPROCESSOR_PATTERN.sub(' ', code)
    code = _NUMBER_PATTERN.sub(' ', code)
    code = code.replace('::', ' ')
    return code


def extract_declared_variables(code: str) -> set[str]:
    """
    C++ 코드에 등장하는 모든 사용자 정의 식별자를 반환
    """
    cleaned = _strip_literals_and_comments(code)\

    identifiers: set[str] = set()
    for m in _IDENT_RE.finditer(cleaned):
        name = m.group(1)
        if name not in CPP_KEYWORDS and len(name) >= 1:
            identifiers.add(name)

    return identifiers
