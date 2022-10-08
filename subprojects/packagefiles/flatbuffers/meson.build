project(
    'flatbuffers',
    'cpp',
    version : '2.0.8',
    license : 'Apache-2.0'
)

cpp = meson.get_compiler('cpp')

cpp_args = []

if host_machine.system() == 'windows'
    cpp_args += '-D_CRT_SECURE_NO_WARNINGS'
endif

if cpp.get_argument_syntax() == 'gcc'
    cpp_args += [
        '-Wall',
        '-pedantic',
        '-Werror',
        '-Wextra'
    ]
endif

if not cpp.has_function('strtoull_l')
  cpp_args += '-DFLATBUFFERS_LOCALE_INDEPENDENT=0'
endif

# Certain platforms such as ARM do not use signed chars by default
# which causes issues with certain bounds checks.
if cpp.has_argument('-fsigned-char')
   cpp_args += '-fsigned-char'
endif


includes = include_directories('include', 'grpc')

# flatbuffers
install_headers(
    'include/flatbuffers/base.h',
    'include/flatbuffers/code_generators.h',
    'include/flatbuffers/flatbuffers.h',
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
subdir: 'flatbuffers')

flatbuffers_lib_sources = [
    'src/bfbs_gen_lua.cpp',
    'src/code_generators.cpp',
    'src/idl_gen_fbs.cpp',
    'src/idl_gen_text.cpp',
    'src/idl_parser.cpp',
    'src/reflection.cpp',
    'src/util.cpp'
]

#shared libraries not supported with msvc
flatbuffers_lib = build_target(
  'flatbuffers',
  flatbuffers_lib_sources,
  target_type: cpp.get_argument_syntax() == 'msvc' ? 'static_library' : 'library',
  include_directories: includes,
  cpp_args: cpp_args,
  install: true,
)

flatbuffers_dep = declare_dependency(
    include_directories : includes,
    link_with: flatbuffers_lib,
)

# grpc libraries
cpp_gen_lib =  static_library(
    'cpp_generator',
    [
        'grpc/src/compiler/cpp_generator.cc'
    ],
    include_directories: includes,
    cpp_args : cpp_args
)

# grpc libraries
go_gen_lib =  static_library(
    'go_generator',
    [
        'grpc/src/compiler/go_generator.cc'
    ],
    include_directories: includes,
    cpp_args : cpp_args
)

java_gen_lib =  static_library(
    'java_generator',
    [
        'grpc/src/compiler/java_generator.cc'
    ],
    include_directories: includes,
    cpp_args : cpp_args
)

python_gen_lib =  static_library(
    'python_generator',
    [
        'grpc/src/compiler/python_generator.cc'
    ],
    include_directories: includes,
    cpp_args : cpp_args
)

swift_gen_lib =  static_library(
    'swift_generator',
    [
        'grpc/src/compiler/swift_generator.cc'
    ],
    include_directories: includes,
    cpp_args : cpp_args
)

ts_gen_lib =  static_library(
    'ts_generator',
    [
        'grpc/src/compiler/ts_generator.cc'
    ],
    include_directories: includes,
    cpp_args : cpp_args
)

# flatc_library
install_headers([
    'include/flatbuffers/flatc.h'
], subdir: 'flatbuffers')

flatc_lib_sources = [
    'src/flatc.cpp'
]

flatc_lib = static_library(
    'flatc_library',
    flatc_lib_sources,
    include_directories: includes,
    cpp_args: cpp_args,
    install: true,
    link_with: flatbuffers_lib
)

flatc_lib_dep = declare_dependency(
    include_directories : includes,
    link_with: flatc_lib,
)

flatc_sources = [
    'src/annotated_binary_text_gen.cpp',
    'src/binary_annotator.cpp',
    'src/flatc_main.cpp',
    'src/idl_gen_cpp.cpp',
    'src/idl_gen_csharp.cpp',
    'src/idl_gen_dart.cpp',
    'src/idl_gen_go.cpp',
    'src/idl_gen_grpc.cpp',
    'src/idl_gen_java.cpp',
    'src/idl_gen_json_schema.cpp',
    'src/idl_gen_kotlin.cpp',
    'src/idl_gen_lobster.cpp',
    'src/idl_gen_lua.cpp',
    'src/idl_gen_php.cpp',
    'src/idl_gen_python.cpp',
    'src/idl_gen_rust.cpp',
    'src/idl_gen_swift.cpp',
    'src/idl_gen_text.cpp',
    'src/idl_gen_ts.cpp',
    'src/util.cpp',
]

flatc = executable(
    'flatc',
    flatc_sources,
    include_directories : includes,
    cpp_args : cpp_args,
    install: true,
    link_with: [
        flatc_lib,
        cpp_gen_lib,
        go_gen_lib,
        java_gen_lib,
        python_gen_lib,
        swift_gen_lib,
        ts_gen_lib
    ]
)

meson.override_find_program('flatc', flatc)

flathash_sources = [
    'src/flathash.cpp'
]

flathash = executable(
    'flathash',
    flathash_sources,
    include_directories : includes,
    cpp_args : cpp_args
)

meson.override_find_program('flathash', flathash)
