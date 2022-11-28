protoc_dep = dependency('protoc')

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

depinc = include_directories('.')
libprotobuf_c_dep = declare_dependency(
  include_directories: depinc,
  link_with: libprotobuf_c,
)
