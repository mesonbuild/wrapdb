# SPDX-License-Identifier: LGPL-2.1-or-later
# Copyright 2021 IBM Corp.

kmod_dep = dependency(
  'libkmod',
  version: '>=18',
  required: true,
)
udev_dep = dependency(
  'libudev',
  version: '>=215',
  required: true,
)

# See version commentary in lib/meson.build
# From upstream:
# > ABI_MOCKUP_VERSION=0.1.0
abi_mockup_version = '0.0.1'

gpiomockup_includes = include_directories('.')
gpiomockup_deps = [gpiod_dep, kmod_dep, udev_dep]
gpiomockup = library(
  'gpiomockup',
  'gpio-mockup.c',
  gnu_symbol_visibility: 'hidden',
  version: abi_mockup_version,
  include_directories: [gpiomockup_includes],
  dependencies: gpiomockup_deps,
  install: true,
)

gpiomockup_dep = declare_dependency(
  link_with: gpiomockup,
  include_directories: gpiomockup_includes,
  dependencies: gpiomockup_deps,
  version: abi_mockup_version,
)
