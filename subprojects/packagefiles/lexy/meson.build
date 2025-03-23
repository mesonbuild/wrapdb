project(
    'lexy',
    'cpp',
    default_options: {'default_library': 'static'},
    version: '2022.12.1',
    license: 'BSL-1.0',
    meson_version: '>=1.2.0',
)

inc_dirs = []
compile_args = []
override_options = []

install = get_option('install')

cpp = meson.get_compiler('cpp')
is_in_cpp20_mode = cpp.compiles(
    '''
#if defined(__cplusplus) && (__cplusplus >= 202002L || (defined(_MSVC_LANG) && _MSVC_LANG >= 202002L))
#else
#error is not in cpp 20 mode
#endif
''',
)
is_in_cpp17_mode = cpp.compiles(
    '''
#if defined(__cplusplus) && (__cplusplus >= 201703L || (defined(_MSVC_LANG) && _MSVC_LANG >= 201703L))
#else
#error is not in cpp 17 mode
#endif
''',
)

if not is_in_cpp17_mode
    error('at least c++17 is required to build this package')
endif

if get_option('use_cpp17').enabled()

    override_options += 'cpp_std=c++17'

elif get_option('use_cpp17').disabled()

    if not is_in_cpp20_mode
        error(
            'at least c++20 is required to build this package, you explicitely disabled c++17 support',
        )
    endif

    override_options += 'cpp_std=c++20'

else
    if not is_in_cpp20_mode
        override_options += 'cpp_std=c++17'
    else
        override_options += 'cpp_std=c++20'
    endif
endif

subdir('include')
subdir('src')


lexy_dep = declare_dependency(
    include_directories: inc_dirs,
    version: meson.project_version(),
    link_with: lexy_lib,
    compile_args: compile_args,
)

if get_option('build_examples')
    subdir('examples')
endif

if get_option('build_benchmarks')
    subdir('benchmarks')
endif

if get_option('tests')
    subdir('tests')
endif
