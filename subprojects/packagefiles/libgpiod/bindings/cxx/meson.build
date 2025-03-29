# SPDX-License-Identifier: LGPL-2.1-or-later
# Copyright 2021 IBM Corp.

add_languages(
  'cpp',
  native: false,
)

# See version commentary in lib/meson.build
#
# From upstream:
# > ABI_CXX_VERSION=2.2.1
abi_cxx_version = '1.1.2'

gpiodcxx_sources = files('chip.cpp', 'iter.cpp', 'line.cpp', 'line_bulk.cpp')
gpiodcxx_includes = include_directories('.')
gpiodcxx = library(
  'gpiodcxx',
  gpiodcxx_sources,
  include_directories: [gpiodcxx_includes],
  gnu_symbol_visibility: 'hidden',
  version: abi_cxx_version,
  dependencies: gpiod_dep,
  install: true,
)
pkg.generate(
  gpiodcxx,
  name: 'libgpiodcxx',
  description: 'C++ bindings for libgpiod',
)

gpiodcxx_dep = declare_dependency(
  link_with: gpiodcxx,
  include_directories: gpiodcxx_includes,
  dependencies: gpiod_dep,
  version: abi_cxx_version,
)

install_headers('gpiod.hpp')

subdir('examples')

if get_option('tests')
  subdir('tests')
endif
