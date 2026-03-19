import re
from utils.keywords import CPP_KEYWORDS


def extract_declared_variables(code: str) -> set[str]:
    """
    C++ 코드에서 선언된 변수명을 추출합니다.
    간단한 휴리스틱: 타입 키워드 뒤에 오는 식별자들을 수집합니다.
    (완전한 파서가 아니므로 복잡한 매크로/템플릿에서 일부 누락·오탐 가능)

    지원 패턴:
      1) 일반 변수 선언:  int x;  float* ptr;  const std::string& name;
      2) 함수 파라미터:  void foo(int a, float b)
      3) for 루프 변수:  for (int i = 0; ...)
    """
    declared: set[str] = set()

    # ── 1) 일반 변수 선언 ──────────────────────────────────────────────────────
    #  `keyword [수식어]* varname [, varname2]*`
    decl_pattern = re.compile(
        r'\b(?:' + '|'.join(re.escape(k) for k in CPP_KEYWORDS) + r')\b'
        r'[\s\*&<>\[\]:\w]*'              # 포인터·참조·템플릿 수식어
        r'\s+([A-Za-z_][A-Za-z0-9_]*)'   # 첫 번째 변수명
        r'(?:\s*,\s*[\*&\s]*([A-Za-z_][A-Za-z0-9_]*))*'  # 추가 변수명 (복수 선언)
    )
    for m in decl_pattern.finditer(code):
        for group in m.groups():
            if group and group not in CPP_KEYWORDS:
                declared.add(group)

    # ── 2) 함수 파라미터 ───────────────────────────────────────────────────────
    #  `(keyword varname, keyword varname, ...)`
    param_pattern = re.compile(
        r'\(\s*(?:(?:' + '|'.join(re.escape(k) for k in CPP_KEYWORDS) + r')'
        r'[\s\*&<>\[\]:\w]*\s+([A-Za-z_][A-Za-z0-9_]*)'
        r'(?:\s*,\s*(?:[\w\s\*&<>\[\]:]+)\s+([A-Za-z_][A-Za-z0-9_]*))*'
        r')\s*\)'
    )
    for m in param_pattern.finditer(code):
        for group in m.groups():
            if group and group not in CPP_KEYWORDS:
                declared.add(group)

    # ── 3) for 루프 변수 ───────────────────────────────────────────────────────
    #  `for (type varname = ...)`
    for_pattern = re.compile(r'\bfor\s*\(\s*\w+\s+([A-Za-z_]\w*)')
    for m in for_pattern.finditer(code):
        if m.group(1) not in CPP_KEYWORDS:
            declared.add(m.group(1))

    return declared
