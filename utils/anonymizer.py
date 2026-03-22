import re
from utils.keywords import CPP_KEYWORDS, CSHARP_KEYWORDS

IDENTIFIER_RE: re.Pattern = re.compile(r'\b([A-Za-z_][A-Za-z0-9_]*)\b')
from utils.extractor import extract_declared_variables

def generate_alias(index: int) -> str:
    """순번 기반 익명 변수명 생성: randomVariable1, randomVariable2, ..."""
    return f"anonymousName{index + 1}"


def anonymize_code(original_code: str) -> tuple[str, dict[str, str]]:
    """
    C++ 코드의 변수명을 익명화합니다.

    Args:
        original_code: 원본 C++ 소스 코드 문자열

    Returns:
        (anonymized_code, mapping)
        - anonymized_code : 변수명이 치환된 코드
        - mapping         : {원본 변수명: 익명 변수명} 순서 보존 dict
    """
    declared = extract_declared_variables(original_code)

    # 1글자 이하·키워드는 제외
    declared = {v for v in declared if v not in CPP_KEYWORDS and len(v) >= 1}

    # 코드에서 처음 등장하는 순서대로 번호 부여
    order: list[str] = []
    seen: set[str] = set()
    for m in IDENTIFIER_RE.finditer(original_code):
        name = m.group(1)
        if name in declared and name not in seen:
            order.append(name)
            seen.add(name)

    mapping: dict[str, str] = {orig: generate_alias(i) for i, orig in enumerate(order)}

    # 단어 경계(\b) 기준으로 정확하게 치환
    anonymized = original_code
    for orig, alias in mapping.items():
        anonymized = re.sub(r'\b' + re.escape(orig) + r'\b', alias, anonymized)

    return anonymized, mapping


def restore_code(anonymized_code: str, mapping: dict[str, str]) -> str:
    """
    익명화된 코드를 매핑 테이블을 이용해 원본 변수명으로 복원합니다.

    Args:
        anonymized_code: 익명화된 C++ 소스 코드 (LLM 출력 포함)
        mapping        : anonymize_code() 가 반환한 {원본: 익명} dict

    Returns:
        원본 변수명으로 복원된 코드 문자열
    """
    restored = anonymized_code
    reverse: dict[str, str] = {alias: orig for orig, alias in mapping.items()}
    for alias, orig in reverse.items():
        restored = re.sub(r'\b' + re.escape(alias) + r'\b', orig, restored)
    return restored
