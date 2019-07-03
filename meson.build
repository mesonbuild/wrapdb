project(
    'flatbuffers',
    'cpp',
    version : '1.11.0',
    license : 'Apache-2.0'
)

cpp = meson.get_compiler('cpp')

cpp_args = [
    '-Wall',
    '-pedantic',
    '-Werror',
    '-Wextra'
]

# Certain platforms such as ARM do not use signed chars by default
# which causes issues with certain bounds checks.
if cpp.has_argument('-fsigned-char')
   cpp_args += '-fsigned-char'
endif

includes = include_directories(['include', 'grpc'])

install_headers([
    'include/flatbuffers/base.h',
    'include/flatbuffers/code_generators.h',
    'include/flatbuffers/flatbuffers.h',
    'include/flatbuffers/flatc.h',
    'include/flatbuffers/flexbuffers.h',
    'include/flatbuffers/grpc.h',
    'include/flatbuffers/hash.h',
    'include/flatbuffers/idl.h',
    'include/flatbuffers/minireflect.h',
    'include/flatbuffers/reflection_generated.h',
    'include/flatbuffers/reflection.h',
    'include/flatbuffers/registry.h',
    'include/flatbuffers/stl_emulation.h',
    'include/flatbuffers/util.h',
], subdir: 'flatbuffers')

flatbuffers_lib_sources = [
    'src/code_generators.cpp',
    'src/idl_parser.cpp',
    'src/idl_gen_text.cpp',
    'src/reflection.cpp',
    'src/util.cpp'
]

flatbuffers_lib = library(
    'flatbuffers',
    flatbuffers_lib_sources,
    include_directories : includes,
    cpp_args : cpp_args,
    install: true
)

flatc_sources = [
    flatbuffers_lib_sources,
    'src/idl_gen_cpp.cpp',
    'src/idl_gen_dart.cpp',
    'src/idl_gen_general.cpp',
    'src/idl_gen_go.cpp',
    'src/idl_gen_js_ts.cpp',
    'src/idl_gen_php.cpp',
    'src/idl_gen_python.cpp',
    'src/idl_gen_lobster.cpp',
    'src/idl_gen_lua.cpp',
    'src/idl_gen_rust.cpp',
    'src/idl_gen_fbs.cpp',
    'src/idl_gen_grpc.cpp',
    'src/idl_gen_json_schema.cpp',
    'src/flatc.cpp',
    'src/flatc_main.cpp',
    'grpc/src/compiler/cpp_generator.cc',
    'grpc/src/compiler/go_generator.cc',
    'grpc/src/compiler/java_generator.cc'
]

flatc = executable(
    'flatc',
    flatc_sources,
    include_directories : includes,
    cpp_args : cpp_args,
    install: true
)

flathash_sources = [
    'src/flathash.cpp'
]

flathash = executable(
    'flathash',
    flathash_sources,
    include_directories : includes,
    cpp_args : cpp_args
)

flatbuffers_dep = declare_dependency(
    include_directories : includes,
    link_with: flatbuffers_lib
)