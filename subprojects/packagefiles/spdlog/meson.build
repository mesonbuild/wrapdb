project('spdlog', 'cpp', version : '1.10.0', license: 'MIT',
        default_options : ['cpp_std=c++14'])

inc = include_directories('include')

thread_dep = dependency('threads')

spdlog_dependencies = [thread_dep] 
spdlog_compile_args = []


fmt_dep = dependency('fmt', version : '>=8.1', required : get_option('external_fmt'))
if fmt_dep.found()
    spdlog_dependencies += fmt_dep
    spdlog_compile_args += '-DSPDLOG_FMT_EXTERNAL'
endif

if get_option('compile_library')
    spdlog_compile_args += '-DSPDLOG_COMPILED_LIB'
    if get_option('buildtype') != 'static'
        spdlog_compile_args += '-DSPDLOG_SHARED_LIB'
        spdlog_compile_args += '-Dspdlog_EXPORTS'
        if not fmt_dep.found()
            spdlog_compile_args += '-DFMT_EXPORT'
            spdlog_compile_args += '-DFMT_SHARED'
        endif
    endif
    subdir('src')
    
    spdlog_dep = declare_dependency(include_directories : inc, dependencies : spdlog_dependencies, link_with : spdlog_lib, compile_args : spdlog_compile_args)
else 
    spdlog_dep = declare_dependency(include_directories : inc, dependencies : spdlog_dependencies, compile_args : spdlog_compile_args)
endif

if get_option('tests')
    subdir('tests')
endif
