protoc_dep = dependency('protoc')

proto = configure_file(input: 'protobuf-c.proto', output: 'protobuf-c.proto', copy: true)
protoc = find_program('protoc')
pbgen = custom_target(
  'pb-gen',
  input: proto,
  output: ['protobuf-c.pb.h', 'protobuf-c.pb.cc'],
  command: [
    protoc,
    '--cpp_out', '@BUILD_ROOT@/subprojects/protobuf-c-1.4.1',
    '@INPUT@',
  ],
)

install_headers('protobuf-c.h')

libprotobuf_c = library(
  'protobuf-c',
  'protobuf-c.c',
  c_args: get_option('default_library') != 'static' ? '-DPROTOBUF_C_USE_SHARED_LIB' : '',
  dependencies: protoc_dep,
  install: true,
)

pkgconfig = import('pkgconfig')
pkgconfig.generate(
  libprotobuf_c,
  name: 'protobuf-c',
  description: 'Protocol Buffers implementation in C',
  url: 'https://github.com/protobuf-c/protobuf-c',
)

libprotobuf_c_dep = declare_dependency(
  include_directories: '.',
  link_with: libprotobuf_c,
)
