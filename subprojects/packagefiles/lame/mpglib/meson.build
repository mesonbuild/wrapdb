mpglib_sources = files(
  'common.c',
  'dct64_i386.c',
  'decode_i386.c',
  'interface.c',
  'layer1.c',
  'layer2.c',
  'layer3.c',
  'tabinit.c',
)

mpglib_includes = [
  include_directories('.'),
  include_directories('../libmp3lame'),
  lameinc,
  confinc,
]

mpglib = static_library(
  'mpgdecoder',
  mpglib_sources,
  include_directories: mpglib_includes,
  c_args: common_args,
  pic: true,
  install: false,
)

mpglib_dep = declare_dependency(
  link_with: mpglib,
  include_directories: include_directories('.'),
)
