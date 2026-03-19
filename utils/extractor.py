import re
from utils.keywords import CPP_KEYWORDS


def extract_declared_variables(code: str) -> set[str]:
    """
    C++ 코드에서 선언된 변수명을 추출합니다.

    지원 패턴:
      1) 기본 타입 키워드 선언:  int x;  float* ptr;  const std::string& name;
      2) 함수 파라미터:          void foo(int a, float b)
      3) for 루프 변수:          for (int i = 0; ...)
      4) 사용자 정의 타입 선언:  MyClass aff;  Node* p = ...;  Vector3 pos, dir;
      5) 타입 없는 대입문 좌변:  aff = 10;  result += func();  (단독 식별자 = 패턴)
    """
    declared: set[str] = set()

    # ── 1) 기본 타입 키워드 변수 선언 ─────────────────────────────────────────
    kw_alt = '|'.join(re.escape(k) for k in CPP_KEYWORDS)
    decl_pattern = re.compile(
        r'\b(?:' + kw_alt + r')\b'
        r'(?:[\s\*&<>\[\]:]+(?:' + kw_alt + r'\b)?)*'   # 포인터·참조·추가 한정자
        r'\s+\*{0,2}&?'                                   # 선택적 포인터/참조
        r'([A-Za-z_][A-Za-z0-9_]*)'                      # 변수명
        r'(?:\s*,\s*[\*&\s]*([A-Za-z_][A-Za-z0-9_]*))*' # 복수 선언
    )
    for m in decl_pattern.finditer(code):
        for group in m.groups():
            if group and group not in CPP_KEYWORDS:
                declared.add(group)

    # ── 2) 함수 파라미터 ───────────────────────────────────────────────────────
    param_pattern = re.compile(
        r'\(\s*(?:(?:' + kw_alt + r')'
        r'[\s\*&<>\[\]:\w]*\s+([A-Za-z_][A-Za-z0-9_]*)'
        r'(?:\s*,\s*(?:[\w\s\*&<>\[\]:]+)\s+([A-Za-z_][A-Za-z0-9_]*))*'
        r')\s*\)'
    )
    for m in param_pattern.finditer(code):
        for group in m.groups():
            if group and group not in CPP_KEYWORDS:
                declared.add(group)

    # ── 3) for 루프 변수 ───────────────────────────────────────────────────────
    for_pattern = re.compile(r'\bfor\s*\(\s*\w+\s+([A-Za-z_]\w*)')
    for m in for_pattern.finditer(code):
        if m.group(1) not in CPP_KEYWORDS:
            declared.add(m.group(1))

    # ── 4) 사용자 정의 타입 선언 ──────────────────────────────────────────────
    # "TypeName [*&]* varName [, varName2, ...]  뒤에 = ; ) [ ( 가 오는 경우"
    # - SomeClass obj("str");  처럼 생성자 초기화 → ( 도 허용
    # - (?<!\.)  으로 메서드 호출(obj.method() 등)은 제외
    user_type_pattern = re.compile(
        r'(?<!\.)'                                              # 메서드 호출 제외
        r'\b([A-Za-z_][A-Za-z0-9_]*)'                         # 타입명
        r'(?:<[^>]*>)?'                                        # 선택적 템플릿 인자 <T>
        r'[\s\*&]+'                                            # 공백 또는 포인터/참조
        r'([A-Za-z_][A-Za-z0-9_]*)'                           # 첫 번째 변수명
        r'((?:\s*,\s*[\*&]?\s*[A-Za-z_][A-Za-z0-9_]*)*)'     # 추가 변수명들 (, var2, var3)
        r'\s*(?=[=;)\[(])'                                     # 뒤에 = ; ) [ ( 중 하나
    )
    for m in user_type_pattern.finditer(code):
        type_name = m.group(1)
        var_name  = m.group(2)
        rest      = m.group(3)   # ", var2, var3" 부분

        if type_name in CPP_KEYWORDS:
            continue
        if var_name not in CPP_KEYWORDS:
            declared.add(var_name)

        # 복수 선언 나머지 변수들
        for extra in re.findall(r'[A-Za-z_][A-Za-z0-9_]*', rest):
            if extra not in CPP_KEYWORDS:
                declared.add(extra)

    # ── 5) 타입 없는 대입문 좌변 ─────────────────────────────────────────────
    #  aff = 10;  result += func();  등 문장 맨 앞에 단독으로 오는 식별자
    #  obj.field = ... 처럼 '.' 멤버 접근이 있는 경우는 제외
    assign_pattern = re.compile(
        r'(?:^|(?<=[;{}\n]))'            # 문장/블록 시작
        r'\s*'
        r'([A-Za-z_][A-Za-z0-9_]*)'      # 식별자
        r'\s*(?:[+\-\*/%&|^]?=)'         # 대입 연산자 (+=, -= 등 복합 대입 포함)
        r'(?!=)',                          # == 비교 연산자는 제외
        re.MULTILINE
    )
    for m in assign_pattern.finditer(code):
        name = m.group(1)
        # 대입 직전에 '.' 이 있으면 멤버 접근이므로 건너뜀
        preceding = code[max(0, m.start(1) - 2):m.start(1)]
        if '.' in preceding:
            continue
        if name not in CPP_KEYWORDS:
            declared.add(name)

    return declared