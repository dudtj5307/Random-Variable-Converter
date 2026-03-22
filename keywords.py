# 익명화 금지할 키워드 등록 (대/소문자 구분)
CPP_KEYWORDS = {
    # C++ 기본 키워드
    'auto', 'bool', 'break', 'case', 'catch', 'char', 'class', 'const', 'constexpr',
    'continue', 'default', 'delete', 'do', 'double', 'else', 'enum', 'explicit',
    'extern', 'false', 'float', 'for', 'friend', 'goto', 'if', 'inline', 'int',
    'long', 'mutable', 'namespace', 'new', 'noexcept', 'nullptr', 'operator',
    'private', 'protected', 'public', 'register', 'return', 'short', 'signed',
    'sizeof', 'static', 'struct', 'switch', 'template', 'this', 'throw', 'true',
    'try', 'typedef', 'typeid', 'typename', 'union', 'unsigned', 'using',
    'virtual', 'void', 'volatile', 'while', 'override', 'final',
    'NULL', 'TRUE', 'EOF', 'BOOL', 'FALSE',

    # Type 키워드
    'string', 'wstring', 'vector', 'map', 'set', 'list', 'pair', 'tuple', 'array',
    'unique_ptr', 'shared_ptr', 'weak_ptr', 'function', 'thread', 'mutex',
    'size_t', 'ptrdiff_t', 'intptr_t', 'uintptr_t',
    'uint8_t', 'uint16_t', 'uint32_t', 'uint64_t',
    'int8_t', 'int16_t', 'int32_t', 'int64_t',
    'std', 'cout', 'cin', 'cerr', 'clog', 'endl',

    # Standard/Library 컨테이너
    'deque', 'queue', 'stack', 'multimap', 'multiset',
    'unordered_map', 'unordered_set', 'unordered_multimap', 'unordered_multiset',
    'bitset', 'valarray', 'forward_list', 'priority_queue',
    'optional', 'variant', 'any', 'span',

    # 스트림 / IO
    'fstream', 'ifstream', 'ofstream', 'stringstream', 'istringstream', 'ostringstream',
    'ios', 'iostream', 'iomanip', 'streampos', 'streamsize', 'streambuf',

    # 스마트 포인터 / 메모리
    'make_unique', 'make_shared', 'allocator', 'memory_order',
    'enable_shared_from_this', 'owner_less',

    # Algorithm/Utility 키워드
    'sort', 'stable_sort', 'partial_sort', 'nth_element',
    'find', 'find_if', 'find_if_not', 'find_end', 'find_first_of', 'adjacent_find',
    'count', 'count_if', 'copy', 'copy_if', 'copy_n', 'copy_backward',
    'move', 'move_backward', 'swap', 'swap_ranges', 'iter_swap',
    'begin', 'end', 'cbegin', 'cend', 'rbegin', 'rend', 'crbegin', 'crend',
    'advance', 'next', 'prev', 'distance',
    'min', 'max', 'min_element', 'max_element', 'minmax', 'minmax_element', 'clamp',
    'abs', 'accumulate', 'transform', 'remove', 'remove_if', 'remove_copy', 'remove_copy_if',
    'replace', 'replace_if', 'replace_copy', 'replace_copy_if',
    'fill', 'fill_n', 'generate', 'generate_n',
    'reverse', 'reverse_copy', 'rotate', 'rotate_copy',
    'unique', 'unique_copy', 'shuffle', 'random_shuffle',
    'lower_bound', 'upper_bound', 'equal_range', 'binary_search',
    'merge', 'inplace_merge', 'includes',
    'set_union', 'set_intersection', 'set_difference', 'set_symmetric_difference',
    'make_heap', 'push_heap', 'pop_heap', 'sort_heap', 'is_heap',
    'all_of', 'any_of', 'none_of', 'for_each',
    'equal', 'mismatch', 'search', 'search_n',
    'iota', 'inner_product', 'adjacent_difference', 'partial_sum',
    'make_pair', 'make_tuple', 'get', 'tie', 'forward', 'move',

    # 수학 / 숫자
    'numeric_limits', 'complex', 'ratio',
    'INT_MAX', 'INT_MIN', 'UINT_MAX', 'LONG_MAX', 'LONG_MIN', 'LLONG_MAX', 'LLONG_MIN',
    'FLT_MAX', 'FLT_MIN', 'DBL_MAX', 'DBL_MIN', 'LDBL_MAX',
    'SIZE_MAX', 'CHAR_BIT', 'CHAR_MAX', 'CHAR_MIN',
    'M_PI', 'M_E', 'M_SQRT2', 'INFINITY', 'NAN',

    # C++11/14/17/20 키워드
    'decltype', 'alignas', 'alignof', 'static_assert', 'thread_local',
    'char16_t', 'char32_t', 'char8_t',
    'concept', 'requires', 'co_await', 'co_return', 'co_yield',
    'export', 'import', 'module', 'consteval', 'constinit',

    # 멀티스레딩 / 동기화
    'atomic', 'atomic_flag', 'atomic_int', 'atomic_bool',
    'condition_variable', 'condition_variable_any',
    'lock_guard', 'unique_lock', 'shared_lock', 'scoped_lock',
    'recursive_mutex', 'shared_mutex', 'timed_mutex', 'recursive_timed_mutex',
    'future', 'shared_future', 'promise', 'async', 'launch', 'packaged_task',

    # 예외
    'exception', 'bad_alloc', 'bad_cast', 'bad_typeid', 'bad_exception',
    'logic_error', 'runtime_error', 'range_error', 'overflow_error', 'underflow_error',
    'invalid_argument', 'length_error', 'out_of_range', 'domain_error',
    'bad_optional_access', 'bad_variant_access',

    # 타입 특성 / 메타프로그래밍
    'type_traits', 'is_same', 'is_base_of', 'is_convertible', 'is_integral',
    'is_floating_point', 'is_pointer', 'is_reference', 'is_const', 'is_volatile',
    'enable_if', 'conditional', 'remove_const', 'remove_reference', 'decay',
    'result_of', 'invoke_result', 'void_t', 'conjunction', 'disjunction', 'negation',

    # 정규식
    'regex', 'smatch', 'cmatch', 'wsmatch', 'wcmatch',
    'regex_match', 'regex_search', 'regex_replace',

    # 파일시스템 (C++17)
    'filesystem', 'path', 'directory_entry', 'directory_iterator',
    'recursive_directory_iterator', 'file_status',

    # 기타 유틸리티
    'chrono', 'duration', 'time_point', 'system_clock', 'steady_clock', 'high_resolution_clock',
    'ratio', 'hash', 'reference_wrapper', 'ref', 'cref',
    'initializer_list', 'type_index', 'type_info',
    'random_device', 'mt19937', 'mt19937_64',
    'uniform_int_distribution', 'uniform_real_distribution', 'normal_distribution',
    'bernoulli_distribution', 'poisson_distribution',

    # Windows API / MFC
    'HWND', 'HDC', 'UINT', 'DWORD', 'WPARAM', 'LPARAM', 'LRESULT', 'WINAPI',
    'CALLBACK', 'HANDLE', 'HINSTANCE',
    'LONG', 'WORD', 'BYTE', 'LPSTR', 'LPCSTR', 'LPWSTR', 'LPCWSTR', 'LPTSTR', 'LPCTSTR',
    'LPVOID', 'LPCVOID', 'HRESULT', 'HKEY', 'HFILE', 'HMODULE', 'HICON', 'HCURSOR',
    'HBITMAP', 'HBRUSH', 'HFONT', 'HPEN', 'HMENU', 'HGDIOBJ',
    'RECT', 'POINT', 'SIZE', 'LARGE_INTEGER', 'ULARGE_INTEGER', 'FILETIME', 'SYSTEMTIME',
    'MSG', 'WNDCLASS', 'WNDCLASSEX', 'PAINTSTRUCT', 'CREATESTRUCT', 'NMHDR',
    'VARIANT', 'BSTR', 'SAFEARRAY', 'DECIMAL', 'CURRENCY',
    'COLORREF', 'LOGFONT', 'TEXTMETRIC', 'BITMAP', 'BITMAPINFO', 'BITMAPINFOHEADER',
    'WM_CREATE', 'WM_DESTROY', 'WM_PAINT', 'WM_SIZE', 'WM_CLOSE', 'WM_COMMAND',
    'WM_TIMER', 'WM_MOVE', 'WM_KEYDOWN', 'WM_KEYUP', 'WM_CHAR',
    'WM_LBUTTONDOWN', 'WM_LBUTTONUP', 'WM_RBUTTONDOWN', 'WM_RBUTTONUP', 'WM_MOUSEMOVE',
    'WM_SETFOCUS', 'WM_KILLFOCUS', 'WM_ENABLE', 'WM_SETTEXT', 'WM_GETTEXT',
    'WM_HSCROLL', 'WM_VSCROLL', 'WM_NOTIFY', 'WM_INITDIALOG', 'WM_USER',
    'SW_SHOW', 'SW_HIDE', 'SW_SHOWMAXIMIZED', 'SW_SHOWMINIMIZED', 'SW_RESTORE', 'SW_SHOWNORMAL',
    'MB_OK', 'MB_OKCANCEL', 'MB_YESNO', 'MB_YESNOCANCEL', 'MB_ICONWARNING', 'MB_ICONERROR',
    'MB_ICONINFORMATION', 'MB_ICONQUESTION', 'MB_DEFBUTTON1', 'MB_DEFBUTTON2',
    'IDOK', 'IDCANCEL', 'IDYES', 'IDNO', 'IDABORT', 'IDRETRY', 'IDIGNORE',
    'GWL_STYLE', 'GWL_EXSTYLE', 'GWL_WNDPROC', 'GWL_USERDATA',
    'WS_VISIBLE', 'WS_CHILD', 'WS_BORDER', 'WS_CAPTION', 'WS_POPUP', 'WS_OVERLAPPEDWINDOW',
    'ES_AUTOHSCROLL', 'ES_AUTOVSCROLL', 'ES_MULTILINE', 'ES_READONLY', 'ES_NUMBER',
    'BS_PUSHBUTTON', 'BS_CHECKBOX', 'BS_RADIOBUTTON', 'BS_GROUPBOX', 'BS_AUTOCHECKBOX',
    'SS_LEFT', 'SS_CENTER', 'SS_RIGHT',
    'S_OK', 'S_FALSE', 'E_FAIL', 'E_INVALIDARG', 'E_NOTIMPL', 'E_NOINTERFACE',
    'E_POINTER', 'E_OUTOFMEMORY', 'E_UNEXPECTED', 'E_ACCESSDENIED',
    'SUCCEEDED', 'FAILED', 'MAKERESULT', 'HRESULT_FROM_WIN32',
    'MAX_PATH', 'INVALID_HANDLE_VALUE', 'INVALID_SOCKET',
    'CString', 'CWnd', 'CDialog', 'CView', 'CDocument', 'CFrameWnd', 'CWinApp',
    'CDC', 'CBitmap', 'CFont', 'CPen', 'CBrush', 'CMenu', 'CPoint', 'CRect', 'CSize',
    'CList', 'CArray', 'CMap', 'CTypedPtrList', 'CTypedPtrArray', 'CTypedPtrMap',
    'CFile', 'CStdioFile', 'CMemFile', 'CArchive',
    'CException', 'CFileException', 'CMemoryException', 'COleException',
    'CScrollView', 'CFormView', 'CListView', 'CTreeView', 'CSplitterWnd',
    'CStatusBar', 'CToolBar', 'CDialogBar', 'CTabCtrl',
    'CListCtrl', 'CTreeCtrl', 'CEditCtrl', 'CButton', 'CComboBox', 'CEdit',
    'CSliderCtrl', 'CSpinButtonCtrl', 'CProgressCtrl', 'CDateTimeCtrl',
    'CImageList', 'CToolTipCtrl', 'CHeaderCtrl', 'CRichEditCtrl',
    'AfxMessageBox', 'AfxGetApp', 'AfxGetMainWnd', 'AfxGetInstanceHandle',
    'AfxBeginThread', 'AfxEndThread', 'AfxGetThread',
    'TRACE', 'TRACE0', 'TRACE1', 'TRACE2', 'ASSERT', 'ASSERT_VALID', 'VERIFY',
    'DEBUG_NEW', 'THIS_FILE',
    'BEGIN_MESSAGE_MAP', 'END_MESSAGE_MAP',
    'ON_COMMAND', 'ON_MESSAGE', 'ON_NOTIFY', 'ON_UPDATE_COMMAND_UI',
    'ON_BN_CLICKED', 'ON_EN_CHANGE', 'ON_CBN_SELCHANGE', 'ON_LBN_SELCHANGE',
    'ON_WM_CREATE', 'ON_WM_DESTROY', 'ON_WM_PAINT', 'ON_WM_SIZE', 'ON_WM_TIMER',
    'ON_WM_LBUTTONDOWN', 'ON_WM_LBUTTONUP', 'ON_WM_MOUSEMOVE', 'ON_WM_KEYDOWN',
    'DECLARE_MESSAGE_MAP', 'DECLARE_DYNAMIC', 'DECLARE_DYNCREATE', 'DECLARE_SERIAL',
    'IMPLEMENT_DYNAMIC', 'IMPLEMENT_DYNCREATE', 'IMPLEMENT_SERIAL',
    
    # 사용자 정의 키워드 (아래 추가)

}

CSHARP_KEYWORDS = {
    # C# 기본 키워드
    'abstract', 'as', 'base', 'break', 'byte', 'case', 'catch', 'char', 'checked',
    'class', 'const', 'continue', 'decimal', 'default', 'delegate', 'do', 'double',
    'else', 'enum', 'event', 'explicit', 'extern', 'false', 'finally', 'fixed',
    'float', 'for', 'foreach', 'goto', 'if', 'implicit', 'in', 'int', 'interface',
    'internal', 'is', 'lock', 'long', 'namespace', 'new', 'null', 'object', 'operator',
    'out', 'override', 'params', 'private', 'protected', 'public', 'readonly',
    'ref', 'return', 'sbyte', 'sealed', 'short', 'sizeof', 'stackalloc', 'static',
    'string', 'struct', 'switch', 'this', 'throw', 'true', 'try', 'typeof',
    'uint', 'ulong', 'unchecked', 'unsafe', 'ushort', 'using', 'virtual', 'void',
    'volatile', 'while',

    # C# 컨텍스트 키워드
    'add', 'alias', 'ascending', 'async', 'await', 'by', 'descending', 'dynamic',
    'equals', 'from', 'get', 'global', 'group', 'into', 'join', 'let', 'nameof',
    'notnull', 'on', 'orderby', 'partial', 'remove', 'select', 'set', 'unmanaged',
    'value', 'var', 'when', 'where', 'with', 'yield', 'nint', 'nuint',
    'record', 'init', 'required', 'file', 'scoped',

    # C# 기본 타입 / BCL
    'Boolean', 'Byte', 'SByte', 'Int16', 'Int32', 'Int64', 'UInt16', 'UInt32', 'UInt64',
    'Single', 'Double', 'Decimal', 'Char', 'String', 'Object', 'IntPtr', 'UIntPtr',
    'DateTime', 'DateOnly', 'TimeOnly', 'TimeSpan', 'Guid', 'Uri', 'Version',
    'Nullable', 'Enum', 'ValueType', 'Array', 'Delegate', 'MulticastDelegate',
    'Exception', 'SystemException', 'ApplicationException',
    'Math', 'Random', 'Convert', 'BitConverter', 'Buffer',
    'Console', 'Environment', 'GC', 'Marshal', 'Activator',
    'StringBuilder', 'String',
    'Encoding', 'Decoder', 'Encoder', 'UTF8Encoding', 'UnicodeEncoding',
    'Path', 'File', 'Directory', 'FileInfo', 'DirectoryInfo', 'DriveInfo',
    'Stream', 'FileStream', 'MemoryStream', 'BufferedStream', 'NetworkStream',
    'StreamReader', 'StreamWriter', 'BinaryReader', 'BinaryWriter', 'TextReader', 'TextWriter',

    # C# 컬렉션
    'List', 'Dictionary', 'HashSet', 'SortedDictionary', 'SortedList', 'SortedSet',
    'Queue', 'Stack', 'LinkedList', 'ObservableCollection', 'ReadOnlyCollection',
    'ConcurrentDictionary', 'ConcurrentQueue', 'ConcurrentStack', 'ConcurrentBag',
    'IEnumerable', 'IEnumerator', 'ICollection', 'IList', 'IDictionary',
    'IReadOnlyList', 'IReadOnlyDictionary', 'IReadOnlyCollection',
    'IQueryable', 'IOrderedQueryable', 'ILookup', 'IGrouping',
    'KeyValuePair', 'Tuple', 'ValueTuple', 'ReadOnlySpan', 'Span', 'Memory',
    'ArraySegment', 'ImmutableList', 'ImmutableDictionary', 'ImmutableHashSet',
    'ImmutableArray', 'ImmutableQueue', 'ImmutableStack', 'ImmutableSortedDictionary',

    # C# 비동기 / 태스크
    'Task', 'ValueTask', 'CancellationToken', 'CancellationTokenSource',
    'TaskCompletionSource', 'TaskFactory', 'TaskScheduler', 'SynchronizationContext',
    'Func', 'Action', 'Predicate', 'Comparison', 'Converter',
    'EventHandler', 'EventArgs', 'PropertyChangedEventArgs', 'NotifyCollectionChangedEventArgs',

    # C# 멀티스레딩 / 동기화
    'Thread', 'ThreadPool', 'Interlocked', 'Monitor', 'Mutex', 'Semaphore',
    'SemaphoreSlim', 'ReaderWriterLock', 'ReaderWriterLockSlim',
    'ManualResetEvent', 'ManualResetEventSlim', 'AutoResetEvent',
    'CountdownEvent', 'Barrier', 'SpinLock', 'SpinWait',
    'Lazy', 'ThreadLocal', 'AsyncLocal',

    # C# 리플렉션 / 특성
    'Attribute', 'Type', 'Assembly', 'Module', 'MethodInfo', 'PropertyInfo',
    'FieldInfo', 'ParameterInfo', 'ConstructorInfo', 'EventInfo', 'MemberInfo',
    'BindingFlags', 'TypeCode',
    'Obsolete', 'Serializable', 'NonSerialized', 'DllImport', 'StructLayout',
    'CallerMemberName', 'CallerFilePath', 'CallerLineNumber', 'CallerArgumentExpression',
    'MethodImpl', 'MarshalAs', 'FieldOffset',
    'Flags', 'AttributeUsage', 'Conditional', 'DebuggerDisplay', 'DebuggerStepThrough',
    'DataContract', 'DataMember', 'XmlSerializable', 'XmlElement', 'XmlAttribute',
    'JsonProperty', 'JsonIgnore', 'JsonConverter',

    # C# 예외
    'ArgumentException', 'ArgumentNullException', 'ArgumentOutOfRangeException',
    'InvalidOperationException', 'NotImplementedException', 'NotSupportedException',
    'NullReferenceException', 'IndexOutOfRangeException', 'OverflowException',
    'DivideByZeroException', 'ArithmeticException', 'FormatException',
    'IOException', 'FileNotFoundException', 'DirectoryNotFoundException',
    'UnauthorizedAccessException', 'PathTooLongException', 'EndOfStreamException',
    'OutOfMemoryException', 'StackOverflowException', 'TimeoutException',
    'InvalidCastException', 'TypeInitializationException', 'MissingMethodException',
    'AggregateException', 'OperationCanceledException', 'ObjectDisposedException',
    'KeyNotFoundException', 'AccessViolationException', 'PlatformNotSupportedException',

    # C# LINQ
    'Enumerable', 'Queryable', 'ParallelEnumerable', 'ParallelQuery',
    'Where', 'Select', 'SelectMany', 'Join', 'GroupJoin', 'GroupBy',
    'OrderBy', 'OrderByDescending', 'ThenBy', 'ThenByDescending',
    'Take', 'TakeWhile', 'Skip', 'SkipWhile',
    'First', 'FirstOrDefault', 'Last', 'LastOrDefault', 'Single', 'SingleOrDefault',
    'Any', 'All', 'Count', 'LongCount', 'Contains',
    'Sum', 'Min', 'Max', 'Average', 'Aggregate',
    'Distinct', 'Union', 'Intersect', 'Except', 'Concat', 'Zip',
    'ToList', 'ToArray', 'ToDictionary', 'ToHashSet', 'ToLookup', 'AsEnumerable',

    # C# 네트워크 / 소켓
    'HttpClient', 'HttpClientHandler', 'HttpRequestMessage', 'HttpResponseMessage',
    'HttpContent', 'StringContent', 'ByteArrayContent', 'MultipartFormDataContent',
    'WebClient', 'WebRequest', 'WebResponse', 'HttpWebRequest', 'HttpWebResponse',
    'Socket', 'TcpClient', 'TcpListener', 'UdpClient', 'NetworkStream',
    'IPAddress', 'IPEndPoint', 'DnsEndPoint',
    'Uri', 'UriBuilder', 'UriKind',

    # C# 직렬화
    'JsonSerializer', 'JsonDocument', 'JsonElement', 'JsonNode',
    'XmlSerializer', 'XmlDocument', 'XDocument', 'XElement', 'XAttribute',
    'BinaryFormatter', 'DataContractSerializer',
    'MemoryPack', 'MessagePack',

    # C# 인터페이스 (자주 쓰는 것)
    'IDisposable', 'IComparable', 'IEquatable', 'ICloneable',
    'IConvertible', 'IFormattable', 'IFormatProvider',
    'INotifyPropertyChanged', 'INotifyCollectionChanged',
    'ISerializable', 'IDeserializationCallback',
    'IAsyncDisposable', 'IAsyncEnumerable', 'IAsyncEnumerator',
    'IProgress', 'IObservable', 'IObserver',

    # 사용자 정의 키워드 (아래 추가)

}
