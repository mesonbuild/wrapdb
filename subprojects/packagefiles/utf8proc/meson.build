project('utf8proc', 'c',
    version : '2.6.0',
    license: 'MIT',
    default_options: ['c_std=c99']
)

utf8proc_args = []

if get_option('default_library') == 'static'
    utf8proc_args += '-DUTF8PROC_STATIC'
endif

utf8proc_lib = library('utf8proc',
    sources: [
        'utf8proc.c',
        'utf8proc.h'
    ],
    include_directories: include_directories('.'),
    c_args: ['-DUTF8PROC_EXPORTS']
)

utf8proc_dep = declare_dependency(
    include_directories: include_directories('.'),
    compile_args: utf8proc_args,
    link_with: utf8proc_lib
)
