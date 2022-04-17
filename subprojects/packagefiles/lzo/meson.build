# SPDX-License-Identifier: GPL-2.1-or-later
# Copyright 2021 Eli Schwartz <eschwartz@archlinux.org>

project('lzo', 'c', version: '2.10',
  meson_version: '>=0.46.0')

inc = include_directories('include', '.')
subdir('src')
topdir = meson.current_source_dir()

cc = meson.get_compiler('c')
if cc.get_id() == 'msvc' and get_option('default_library') != 'static'
  add_project_arguments('-D__LZO_EXPORT1=__declspec(dllexport)', language: 'c')
endif

if host_machine.endian() == 'big'
  add_project_arguments('-DLZO_ABI_BIG_ENDIAN=1', language: 'c')
else
  add_project_arguments('-DLZO_ABI_LITTLE_ENDIAN=1', language: 'c')
endif

liblzo2 = library('lzo2', sources,
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
  subdir: 'lzo'
)

import('pkgconfig').generate(
  liblzo2,
  description: 'LZO - a real-time data compression library',
  url: 'http://www.oberhumer.com/opensource/lzo/',
  subdirs: 'lzo'
)

lzo2_dep = declare_dependency(
  link_with: liblzo2,
  include_directories: inc
)

if get_option('tests')
  subdir('lzotest')
  subdir('tests')
endif
subdir('examples')

