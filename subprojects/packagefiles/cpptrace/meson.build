project(
    'cpptrace',
    ['c', 'cpp'],
    license: 'MIT',
    version: '0.5.1',
    meson_version: '>= 0.62.0',
    default_options: ['cpp_std=c++11', 'warning_level=3'],
)

unwinder = get_option('unwind')
get_symbols = get_option('get-symbols')
demangler = get_option('demangle')

host_sys = host_machine.system()
cxx = meson.get_compiler('cpp')
cxx_id = cxx.get_id()

dbghelp_dep = dependency('dbghelp', required: unwinder == 'dbghelp')
libunwind_dep = dependency('libunwind', required: unwinder == 'libunwind')
libdwarf_dep = dependency('libdwarf', required: get_symbols == 'libdwarf')

cxx_is_cl_like = cxx_id == 'msvc' or cxx_id.endswith('-cl')

if cxx_id == 'msvc'
    has_cxxabi = false
else
    has_cxxabi = cxx.compiles(files('cmake/has_cxxabi.cpp')[0])
endif

compdefs = []

# Best way to work out "Windows, but not MinGW?"
if cxx_is_cl_like
    has_unwind = false
    has_execinfo = false
    has_backtrace = false
    has_stackwalk = cxx.compiles(
        files('cmake/has_stackwalk.cpp')[0],
        dependencies: dbghelp_dep,
    )
else
    has_unwind = cxx.compiles(files('cmake/has_unwind.cpp')[0])
    has_execinfo = cxx.compiles(files('cmake/has_execinfo.cpp')[0])
    bt_dep = dependency('stdc++_backtrace', method: 'system', required: false)
    has_backtrace = (
        bt_dep.found()
        and cxx.compiles(
            files('cmake/has_backtrace.cpp')[0],
            dependencies: bt_dep,
        )
    )
    has_stackwalk = false
endif

if host_sys != 'windows'
    if (
        cxx.compiles(
            files('cmake/has_cxx_exception_type.cpp')[0],
        )
    )
        compdefs += '-DCPPTRACE_HAS_CXX_EXCEPTION_TYPE'
    endif
endif

# Interpretation of `UNIX AND NOT APPLE` based on README.
if host_sys in ['linux', 'cygwin']
    if cxx.compiles(files('cmake/has_dl_find_object.cpp')[0])
        compdefs += '-DCPPTRACE_HAS_DL_FIND_OBJECT'
    endif
endif

if unwinder == 'auto'
    if host_sys != 'windows'
        if has_unwind
            message('unwind=auto : using compiler unwind for unwinding.')
            unwinder = 'unwind'
        elif has_execinfo
            message('unwind=auto : using execinfo.h for unwinding.')
            unwinder = 'execinfo'
        elif libunwind_dep.found()
            message('unwind=auto : using libunwind for unwinding.')
            unwinder = 'libunwind'
        else
            error(
                'unwind=auto : cannot find a supported unwinder. stack tracing will not work. set it to `nothing` to compile anyway.',
            )
        endif
    else
        if has_stackwalk
            message('unwind=auto : using dbghelp for unwinding.')
            unwinder = 'dbghelp'
        else
            message('unwind=auto : using winapi for unwinding.')
            unwinder = 'winapi'
        endif
    endif
endif

if get_symbols == 'auto'
    if host_sys != 'windows'
        if libdwarf_dep.found()
            message('get-symbols=auto : using libdwarf for symbols.')
            get_symbols = 'libdwarf'
        elif has_backtrace
            message('get-symbols=auto : using stdc++_backtrace for symbols.')
            get_symbols = 'libbacktrace'
        else
            message('get-symbols=auto : using addr2line for symbols.')
            get_symbols = 'addr2line'
        endif
    elif not cxx_is_cl_like
        message('get-symbols=auto : using libdwarf + dbghelp for symbols.')
        get_symbols = 'libdwarf+dbghelp'
    else
        message('get-symbols=auto : using dbghelp for symbols.')
        get_symbols = 'dbghelp'
    endif
endif

if demangler == 'auto'
    if has_cxxabi
        message('demangle=auto : using cxxabi for demangling.')
        demangler = 'cxxabi'
    elif cxx_is_cl_like
        message('demangle=auto : using dbghelp for demangling.')
        demangler = 'winapi'
    else
        error(
            'demangle=auto : no supported demangler found. set it to `nothing` to build anyway.',
        )
    endif
endif

if unwinder == 'unwind'
    assert(
        has_unwind,
        'unwind=unwind requires compiler support, which is not present.',
    )
elif unwinder == 'execinfo'
    assert(
        has_execinfo,
        'unwind=execinfo requires system support, which is not present.',
    )
elif unwinder in ['winapi', 'dbghelp']
    assert(host_sys == 'windows', f'unwind=@unwinder@ requires Windows.')
endif

if get_symbols == 'libbacktrace'
    assert(has_backtrace, 'unwind=libbacktrace requires libstdc++_backtrace')
elif get_symbols in ['libdl', 'addr2line', 'libdwarf']
    assert(
        host_sys in ['cygwin', 'darwin', 'linux'],
        f'get-symbols=@get_symbols@ requires Unix-like.',
    )
elif get_symbols == 'dbghelp'
    assert(host_sys == 'windows', 'get-symbols=dbghelp requires Windows.')
elif get_symbols == 'libdwarf+dbghelp'
    assert(
        host_sys == 'windows' and not cxx_is_cl_like,
        'get-symbols=libdwarf+dbghelp requires MinGW.',
    )
endif

if demangler == 'cxxabi'
    assert(
        has_cxxabi,
        'demangle=cxxabi requires compiler support, which is not present.',
    )
elif demangler == 'winapi'
    assert(cxx_is_cl_like, 'demangle=winapi requires a cl.exe-like compiler.')
endif

unwind_dep_name = {
    'unwind': '',
    'libunwind': 'libunwind',
    'execinfo': '',
    'winapi': '',
    'dbghelp': 'dbghelp',
    'nothing': '',
}[unwinder]
if unwind_dep_name == ''
    unwinder_dep = dependency('', required: false)
else
    if unwind_dep_name == 'dbghelp'
        unwinder_dep = dependency(unwind_dep_name, method: 'system')
    else
        unwinder_dep = dependency(unwind_dep_name)
    endif
endif

compdefs += f'-DCPPTRACE_UNWIND_WITH_@unwinder@'.to_upper()

symbol_getter_dep_names = {
    'libbacktrace': ['stdc++_backtrace'],
    'libdl': ['dl'],
    'addr2line': ['dl'],
    'libdwarf': ['libdwarf'],
    'dbghelp': ['dbghelp'],
    'libdwarf+dbghelp': ['libdwarf', 'dbghelp'],
    'nothing': [],
}[get_symbols]

if get_symbols == 'addr2line'
    compdefs += '-DCPPTRACE_ADDR2LINE_SEARCH_SYSTEM_PATH'
endif

symbol_getter_deps = []
foreach dep_name : symbol_getter_dep_names
    if dep_name in ['stdc++_backtrace', 'dbghelp']
        symbol_getter_deps += dependency(dep_name, method: 'system')
    else
        dep = dependency(dep_name)
        if dep_name == 'libdwarf'
            if cxx.has_header('libdwarf/libdwarf.h', dependencies: dep)
                compdefs += '-DCPPTRACE_USE_NESTED_LIBDWARF_HEADER_PATH'
            endif
        endif
        symbol_getter_deps += dep
    endif
endforeach

compdefs += f'-DCPPTRACE_GET_SYMBOLS_WITH_@get_symbols@'.to_upper()

compdefs += f'-DCPPTRACE_DEMANGLE_WITH_@demangler@'.to_upper()

hard_max_frames = get_option('hard-max-frames')

compdefs += f'-DCPPTRACE_HARD_MAX_FRAMES=@hard_max_frames@'

libtype = get_option('default_library')

if libtype == 'static'
    compdefs += '-DCPPTRACE_STATIC_DEFINE'
endif

summary(
    {
        'unwind': unwinder,
        'get-symbols': get_symbols,
        'demangle': demangler,
        'library type': libtype,
    },
    section: 'Configuration',
)

cpptrace_inc = include_directories('include')

cpptrace_lib = library(
    'cpptrace',
    files(
        'src/cpptrace.cpp',
        'src/ctrace.cpp',
        'src/demangle/demangle_with_cxxabi.cpp',
        'src/demangle/demangle_with_nothing.cpp',
        'src/demangle/demangle_with_winapi.cpp',
        'src/snippets/snippet.cpp',
        'src/symbols/symbols_core.cpp',
        'src/symbols/symbols_with_addr2line.cpp',
        'src/symbols/symbols_with_dbghelp.cpp',
        'src/symbols/symbols_with_dl.cpp',
        'src/symbols/symbols_with_libbacktrace.cpp',
        'src/symbols/symbols_with_libdwarf.cpp',
        'src/symbols/symbols_with_nothing.cpp',
        'src/unwind/unwind_with_dbghelp.cpp',
        'src/unwind/unwind_with_execinfo.cpp',
        'src/unwind/unwind_with_libunwind.cpp',
        'src/unwind/unwind_with_nothing.cpp',
        'src/unwind/unwind_with_unwind.cpp',
        'src/unwind/unwind_with_winapi.cpp',
    ),
    cpp_args: compdefs,
    dependencies: [unwinder_dep] + symbol_getter_deps,
    include_directories: cpptrace_inc,
)

cpptrace_dep = declare_dependency(
    link_with: cpptrace_lib,
    include_directories: cpptrace_inc,
)

meson.override_dependency('cpptrace', cpptrace_dep)
