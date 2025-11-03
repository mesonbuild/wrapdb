protoc_dep = dependency('protoc')

install_headers('protobuf-c.h')

api = []
exp = []
if get_option('default_library') != 'static'
  api += '-DPROTOBUF_C_USE_SHARED_LIB'
  exp += '-DPROTOBUF_C_EXPORT'
endif

libprotobuf_c = library(
  'protobuf-c',
  'protobuf-c.c',
  c_args: [api, exp],
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
  compile_args: api,
  include_directories: [depinc, include_directories('..')],
  link_with: libprotobuf_c,
)
