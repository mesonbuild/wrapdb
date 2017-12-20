project('protobuf-c', 'c', 'cpp', version : '1.3.0', license : 'BSD-2')

c = meson.get_compiler('c')
cc = meson.get_compiler('cpp')

libprotobuf_c_src = [
  'protobuf-c/protobuf-c.c',
]

protobuf_deps = dependency('protobuf',
                           fallback: ['protobuf', 'protobuf_dep'],
                           version: '>= 3.0.0')
libprotobuf_c = library('protobuf-c',
                        libprotobuf_c_src,
                        cpp_args: [],
                        dependencies: protobuf_deps,
                        include_directories: include_directories('protobuf-c'))

protoc_c_src = [
  'protoc-c/c_bytes_field.cc',
  'protoc-c/c_enum.cc',
  'protoc-c/c_enum_field.cc',
  'protoc-c/c_extension.cc',
  'protoc-c/c_field.cc',
  'protoc-c/c_file.cc',
  'protoc-c/c_generator.cc',
  'protoc-c/c_helpers.cc',
  'protoc-c/c_message.cc',
  'protoc-c/c_message_field.cc',
  'protoc-c/c_primitive_field.cc',
  'protoc-c/c_service.cc',
  'protoc-c/c_string_field.cc',
  'protoc-c/main.cc',
]

protoc_deps = dependency('protobuf',
                         fallback: ['protobuf', 'protoc_dep'],
                         version: '>= 3.0.0')

protoc_c = executable('protoc-c',
                      protoc_c_src,
                      cpp_args: '-DPACKAGE_STRING="protobuf-c"',
                      include_directories: include_directories('protoc-c',
                                                               'protobuf-c'),
                      dependencies: protoc_deps)
