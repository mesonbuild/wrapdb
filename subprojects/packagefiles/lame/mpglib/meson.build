mpglib_sources = [
  'common.c',
  'dct64_i386.c',
  'decode_i386.c',
  'interface.c',
  'layer1.c',
  'layer2.c',
  'layer3.c',
  'tabinit.c',
]

mpglib = static_library('mpgdecoder',
  mpglib_sources,
  include_directories : [confinc, lameinc],
  c_args : common_args,
  install : false)
mpglib_dep = declare_dependency(
  link_with : mpglib,
  include_directories: include_directories('.'))
