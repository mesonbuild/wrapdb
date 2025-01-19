project('whisper.cpp', ['cpp', 'c'], version: '1.5.2')

cc = meson.get_compiler('c')

math = cc.find_library('m', required: false)
threads = dependency('threads')

if cc.get_argument_syntax() == 'gcc'
    add_project_arguments('-D_GNU_SOURCE', language: 'c')

    if get_option('avx').enabled()
        add_project_arguments('-mavx', language: 'c')
    endif

    if get_option('avx2').enabled()
        add_project_arguments('-mavx2', language: 'c')
    endif

    if get_option('fma').enabled()
        add_project_arguments('-mfma', language: 'c')
    endif

    if get_option('f16C').enabled()
        add_project_arguments('-mf16c', language: 'c')
    endif
elif cc.get_argument_syntax() == 'msvc'
    add_project_arguments('/utf-8', language: 'c')

    if get_option('avx').enabled()
        add_project_arguments('/arch:AVX', language: 'c')
    endif

    if get_option('avx2').enabled()
        add_project_arguments('/arch:AVX2', language: 'c')
    endif

endif

ggml_lib = library(
    'ggml',
    'ggml.c',
    'ggml-alloc.c',
    'ggml-backend.c',
    'ggml-quants.c',
    dependencies: [math, threads],
)
ggml_dep = declare_dependency(
    dependencies: [math, threads],
    include_directories: '.',
    link_with: ggml_lib,
)

whisper_lib = library(
    'whisper',
    'whisper.cpp',
    dependencies: [ggml_dep],
)
whisper_cpp_dep = declare_dependency(
    include_directories: '.',
    dependencies: [ggml_dep],
    link_with: whisper_lib,
)

if get_option('examples')
    subdir('examples')
endif
