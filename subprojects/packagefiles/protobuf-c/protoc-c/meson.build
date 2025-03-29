protobuf_dep = dependency(
  'protobuf',
  version: '>= 3.0.0',
)

protoc_c_src = files(
  'c_bytes_field.cc',
  'c_enum.cc',
  'c_enum_field.cc',
  'c_extension.cc',
  'c_field.cc',
  'c_file.cc',
  'c_generator.cc',
  'c_helpers.cc',
  'c_message.cc',
  'c_message_field.cc',
  'c_primitive_field.cc',
  'c_service.cc',
  'c_string_field.cc',
  'main.cc',
)

protoc_c = executable(
  'protoc-c',
  protoc_c_src,
  pbgen,
  cpp_args: '-DPACKAGE_STRING="protobuf-c"',
  include_directories: incdir,
  dependencies: [libprotobuf_c_dep, protoc_dep, protobuf_dep],
)
