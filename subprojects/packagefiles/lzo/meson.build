# SPDX-License-Identifier: GPL-2.1-or-later
# Copyright 2021 Eli Schwartz <eschwartz@archlinux.org>

project(
  'lzo',
  'c',
  version: '2.10',
  meson_version: '>=0.48.0',
)

inc = include_directories('include', '.')
subdir('src')
topdir = meson.current_source_dir()

cc = meson.get_compiler('c')

api = '-D__LZO_EXPORT1=__attribute__((visibility("default")))'
if host_machine.system() == 'windows'
  api = get_option('default_library') != 'static' ? '-D__LZO_EXPORT1=__declspec(dllexport)' : []
endif

add_project_arguments(
  '-DLZO_ABI_@0@_ENDIAN=1'.format(host_machine.endian().to_upper()),
  language: 'c',
)

liblzo2 = library(
  'lzo2',
  sources,
  c_args: api,
  gnu_symbol_visibility: 'hidden',
  include_directories: inc,
  version: '2.0.0',
  install: true,
)

install_headers(
  'include/lzo/lzo1.h',
  'include/lzo/lzo1a.h',
  'include/lzo/lzo1b.h',
  'include/lzo/lzo1c.h',
  'include/lzo/lzo1f.h',
  'include/lzo/lzo1x.h',
  'include/lzo/lzo1y.h',
  'include/lzo/lzo1z.h',
  'include/lzo/lzo2a.h',
  'include/lzo/lzo_asm.h',
  'include/lzo/lzoconf.h',
  'include/lzo/lzodefs.h',
  'include/lzo/lzoutil.h',
  subdir: 'lzo',
)

pconf = import('pkgconfig')
pconf.generate(
  liblzo2,
  description: 'LZO - a real-time data compression library',
  url: 'http://www.oberhumer.com/opensource/lzo/',
  subdirs: 'lzo',
)

api = []
if host_machine.system() == 'windows' and get_option('default_library') != 'static'
  api += '-D__LZO_EXPORT1=__declspec(dllimport)'
endif

lzo2_dep = declare_dependency(
  compile_args: api,
  link_with: liblzo2,
  include_directories: inc,
)

subdir('lzotest')
subdir('tests')
subdir('examples')
