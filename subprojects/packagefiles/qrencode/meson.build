project(
  'qrencode',
  'c',
  license: 'mit',
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
  'qrencode',
  sources,
  c_args: c_args,
  dependencies: [dependency('threads')],
  vs_module_defs: 'qrencode.def',
  install: true,
  version: meson.project_version(),
)
import('pkgconfig').generate(
  libqrencode,
  name: 'libqrencode',
  description: 'A QR Code encoding library',
  version: meson.project_version(),
)
libqrencode_dep = declare_dependency(
  link_with: libqrencode,
  include_directories: include_directories('.'),
)
meson.override_dependency('libqrencode', libqrencode_dep)
