import sys
import os
import importlib.util

_DEFAULT_KEYWORDS_CONTENT = """\
# C++ 기본 타입 + 한정자 (변수명으로 오인하지 않도록)
CPP_KEYWORDS = {
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
"""


def _get_base_dir() -> str:
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load() -> object:
    base = _get_base_dir()
    path = os.path.join(base, 'keywords.py')

    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(_DEFAULT_KEYWORDS_CONTENT)

    spec = importlib.util.spec_from_file_location('user_keywords', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_mod = _load()
CPP_KEYWORDS: set[str] = _mod.CPP_KEYWORDS
