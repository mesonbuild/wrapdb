project('quill', 'cpp', version : '4.2.0', default_options : ['warning_level=3', 'cpp_std=c++17'])

inc_dirs = include_directories('quill/include')

# Conditional compiler arguments for specific compiler
cpp = meson.get_compiler('cpp')
if cpp.get_id() == 'gcc' or cpp.get_id() == 'clang'
    interface_compile_args = ['-Wno-gnu-zero-variadic-macro-arguments']
else
    interface_compile_args = []
endif

quill_dep = declare_dependency(include_directories : inc_dirs,
                               dependencies : [dependency('threads')],
                               compile_args : interface_compile_args)

pkg_mod = import('pkgconfig')
pkg_mod.generate(
    name : 'quill',
    filebase : 'quill',
    description : 'Asynchronous Low Latency C++ Logging Library',
    subdirs : 'quill/include'
)