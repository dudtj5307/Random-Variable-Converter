# C++ 타입 및 한정자 (익명화 대상 X)
CPP_KEYWORDS = {
    'auto', 'bool', 'break', 'case', 'catch', 'char', 'class', 'const', 'constexpr',
    'continue', 'default', 'delete', 'do', 'double', 'else', 'enum', 'explicit',
    'extern', 'false', 'float', 'for', 'friend', 'goto', 'if', 'inline', 'int',
    'long', 'mutable', 'namespace', 'new', 'noexcept', 'nullptr', 'operator',
    'private', 'protected', 'public', 'register', 'return', 'short', 'signed',
    'sizeof', 'static', 'struct', 'switch', 'template', 'this', 'throw', 'true',
    'try', 'typedef', 'typeid', 'typename', 'union', 'unsigned', 'using',
    'virtual', 'void', 'volatile', 'while', 'override', 'final',
    'NULL', 'TRUE', 'EOF', 'BOOL', 'FALSE',
    
    # Type
    'string', 'vector', 'map', 'set', 'list', 'pair', 'tuple', 'array',
    'unique_ptr', 'shared_ptr', 'weak_ptr', 'function', 'thread', 'mutex',
    'size_t', 'uint8_t', 'uint16_t', 'uint32_t', 'uint64_t',
    'int8_t', 'int16_t', 'int32_t', 'int64_t',
    'std', 'cout', 'cin', 'endl',
    
    # MFC
    'HWND', 'HDC', 'UINT', 'DWORD', 'WPARAM', 'LPARAM', 'LRESULT', 'WINAPI', 
    'CALLBACK', 'HANDLE', 'HINSTANCE',
    
    # User Defined (익명화 금지 키워드 아래 추가)
    'COpenGL',
}
