project('flatbuffers', 'cpp', version: '24.3.25', license: 'Apache-2.0', meson_version: '>=0.49.0')

cpp = meson.get_compiler('cpp')

if host_machine.system() == 'windows'
  add_project_arguments('-D_CRT_SECURE_NO_WARNINGS', language: 'cpp')
endif

add_project_arguments('-DFLATBUFFERS_LOCALE_INDEPENDENT=@0@'.format(cpp.has_function('strtoull_l')), language: 'cpp')

# Certain platforms such as ARM do not use signed chars by default
# which causes issues with certain bounds checks.
add_project_arguments(cpp.get_supported_arguments('-fsigned-char'), language: 'cpp')

includes = include_directories('include', 'grpc')

headers = files(
  'include/flatbuffers/allocator.h',
  'include/flatbuffers/array.h',
  'include/flatbuffers/base.h',
  'include/flatbuffers/buffer.h',
  'include/flatbuffers/buffer_ref.h',
  'include/flatbuffers/code_generators.h',
  'include/flatbuffers/default_allocator.h',
  'include/flatbuffers/detached_buffer.h',
  'include/flatbuffers/file_manager.h',
  'include/flatbuffers/flatbuffer_builder.h',
  'include/flatbuffers/flatbuffers.h',
  'include/flatbuffers/flatc.h',
  'include/flatbuffers/flex_flat_util.h',
  'include/flatbuffers/flexbuffers.h',
  'include/flatbuffers/grpc.h',
  'include/flatbuffers/hash.h',
  'include/flatbuffers/idl.h',
  'include/flatbuffers/minireflect.h',
  'include/flatbuffers/reflection.h',
  'include/flatbuffers/reflection_generated.h',
  'include/flatbuffers/registry.h',
  'include/flatbuffers/stl_emulation.h',
  'include/flatbuffers/string.h',
  'include/flatbuffers/struct.h',
  'include/flatbuffers/table.h',
  'include/flatbuffers/util.h',
  'include/flatbuffers/vector.h',
  'include/flatbuffers/vector_downward.h',
  'include/flatbuffers/verifier.h',
)

# flatbuffers
install_headers(
  headers,
  subdir: 'flatbuffers',
)

flatbuffers_lib_sources = files(
  'src/code_generators.cpp',
  'src/idl_gen_binary.cpp',
  'src/idl_gen_text.cpp',
  'src/idl_parser.cpp',
  'src/reflection.cpp',
  'src/util.cpp',
)

#shared libraries not supported with msvc
flatbuffers_lib = build_target(
  'flatbuffers',
  flatbuffers_lib_sources,
  target_type: cpp.get_argument_syntax() == 'msvc' ? 'static_library' : 'library',
  include_directories: includes,
  install: true,
)

flatbuffers_dep = declare_dependency(
  include_directories: includes,
  link_with: flatbuffers_lib,
)

# grpc libraries
cpp_gen_lib = static_library(
  'cpp_generator',
  'grpc/src/compiler/cpp_generator.cc',
  include_directories: includes,
)

# grpc libraries
go_gen_lib = static_library(
  'go_generator',
  'grpc/src/compiler/go_generator.cc',
  include_directories: includes,
)

java_gen_lib = static_library(
  'java_generator',
  'grpc/src/compiler/java_generator.cc',
  include_directories: includes,
)

python_gen_lib = static_library(
  'python_generator',
  'grpc/src/compiler/python_generator.cc',
  include_directories: includes,
)

swift_gen_lib = static_library(
  'swift_generator',
  'grpc/src/compiler/swift_generator.cc',
  include_directories: includes,
)

ts_gen_lib = static_library(
  'ts_generator',
  'grpc/src/compiler/ts_generator.cc',
  include_directories: includes,
)

# flatc_library
flatc_lib = static_library(
  'flatc_library',
  'src/flatc.cpp',
  include_directories: includes,
  install: true,
  link_with: flatbuffers_lib,
)

flatc_lib_dep = declare_dependency(
  include_directories: includes,
  link_with: flatc_lib,
)

flatc_sources = files(
  'src/annotated_binary_text_gen.cpp',
  'src/bfbs_gen_lua.cpp',
  'src/bfbs_gen_nim.cpp',
  'src/binary_annotator.cpp',
  'src/file_binary_writer.cpp',
  'src/file_name_saving_file_manager.cpp',
  'src/file_writer.cpp',
  'src/flatc_main.cpp',
  'src/idl_gen_cpp.cpp',
  'src/idl_gen_csharp.cpp',
  'src/idl_gen_dart.cpp',
  'src/idl_gen_fbs.cpp',
  'src/idl_gen_go.cpp',
  'src/idl_gen_grpc.cpp',
  'src/idl_gen_java.cpp',
  'src/idl_gen_json_schema.cpp',
  'src/idl_gen_kotlin.cpp',
  'src/idl_gen_kotlin_kmp.cpp',
  'src/idl_gen_lobster.cpp',
  'src/idl_gen_php.cpp',
  'src/idl_gen_python.cpp',
  'src/idl_gen_rust.cpp',
  'src/idl_gen_swift.cpp',
  'src/idl_gen_text.cpp',
  'src/idl_gen_ts.cpp',
  'src/util.cpp',
)

flatc = executable(
  'flatc',
  flatc_sources,
  include_directories: includes,
  install: true,
  link_with: [flatc_lib, cpp_gen_lib, go_gen_lib, java_gen_lib, python_gen_lib, swift_gen_lib, ts_gen_lib],
)

meson.override_find_program('flatc', flatc)

flathash = executable(
  'flathash',
  'src/flathash.cpp',
  include_directories: includes,
)

meson.override_find_program('flathash', flathash)
