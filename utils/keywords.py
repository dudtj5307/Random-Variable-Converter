import re

# C++ 기본 타입 + 한정자 (변수명으로 오인하지 않도록)
CPP_KEYWORDS: set[str] = {
    'auto', 'bool', 'break', 'case', 'catch', 'char', 'class', 'const', 'constexpr',
    'continue', 'default', 'delete', 'do', 'double', 'else', 'enum', 'explicit',
    'extern', 'false', 'float', 'for', 'friend', 'goto', 'if', 'inline', 'int',
    'long', 'mutable', 'namespace', 'new', 'noexcept', 'nullptr', 'operator',
    'private', 'protected', 'public', 'register', 'return', 'short', 'signed',
    'sizeof', 'static', 'struct', 'switch', 'template', 'this', 'throw', 'true',
    'try', 'typedef', 'typeid', 'typename', 'union', 'unsigned', 'using',
    'virtual', 'void', 'volatile', 'while', 'override', 'final',
    # 공통 매크로 / 리터럴
    'NULL', 'TRUE', 'FALSE', 'EOF',
    # std 타입들
    'string', 'vector', 'map', 'set', 'list', 'pair', 'tuple', 'array',
    'unique_ptr', 'shared_ptr', 'weak_ptr', 'function', 'thread', 'mutex',
    'size_t', 'uint8_t', 'uint16_t', 'uint32_t', 'uint64_t',
    'int8_t', 'int16_t', 'int32_t', 'int64_t',
    'std', 'cout', 'cin', 'endl',
}

# 일반 식별자 패턴
IDENTIFIER_RE: re.Pattern = re.compile(r'\b([A-Za-z_][A-Za-z0-9_]*)\b')
