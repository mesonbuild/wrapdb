project(
  'qrencode',
  'c',
  license: 'MIT',
  version: '4.1.1',
)
cc = meson.get_compiler('c')

sources = files(
  'bitstream.c',
  'mask.c',
  'mmask.c',
  'mqrspec.c',
  'qrencode.c',
  'qrinput.c',
  'qrspec.c',
  'rsecc.c',
  'split.c',
)
c_args = [
  '-DSTATIC_IN_RELEASE=static',
  '-DMAJOR_VERSION=' + meson.project_version().split('.')[0],
  '-DMINOR_VERSION=' + meson.project_version().split('.')[1],
  '-DMICRO_VERSION=' + meson.project_version().split('.')[2],
  '-DVERSION="' + meson.project_version() + '"',
]
if cc.check_header('pthread.h')
  c_args += ['-DHAVE_LIBPTHREAD']
endif
if cc.has_function(
  'strdup',
  prefix: '#include <string.h>',
)
  c_args += ['-DHAVE_STRDUP']
endif

libqrencode = library(
  'libqrencode',
  sources,
  name_prefix: '',
  version: meson.project_version(),
  soversion: host_machine.system() == 'windows' ? '' : '4',
  c_args: c_args,
  dependencies: dependency('threads'),
  vs_module_defs: 'qrencode.def',
  install: true,
)
import('pkgconfig').generate(
  libqrencode,
  description: 'A QR Code encoding library',
)
libqrencode_dep = declare_dependency(
  link_with: libqrencode,
  include_directories: include_directories('.'),
)
meson.override_dependency('libqrencode', libqrencode_dep)
