# SPDX-License-Identifier: LGPL-2.1-or-later
# Copyright 2021 IBM Corp.

# Upstream's ABI_VERSION is defined in terms of libtool versioning.
#
# From upstream configure.ac:
# > ABI_VERSION=4.3.2
#
# From upstream lib/Makefile.am:
# > libgpiod_la_LDFLAGS = -version-info $(subst .,:,$(ABI_VERSION))
#
# So libtool is invoked with:
# > -version-info 4:3:2
#
# Libtool documentation defines the argument for -version-info as[1]:
# > This flag accepts an argument of the form 'current[:revision[:age]]'
#
# In accordance with the libtool script, targetting Linux:
# > version=$(($current - $age)).${age}.${revision}
#
# Solving for upstream ABI_VERSION:
# version=2.2.3
#
# [1] https://www.gnu.org/software/libtool/manual/html_node/Updating-version-info.html
abi_version = '2.2.3'

gpiod_sources = ['core.c', 'ctxless.c', 'helpers.c', 'iter.c', 'misc.c']
gpiod = library(
  'gpiod',
  gpiod_sources,
  include_directories: gpiod_includes,
  gnu_symbol_visibility: 'hidden',
  c_args: ['-include', meson.project_build_root() / 'config.h'],
  version: abi_version,
  install: true,
)

pkg.generate(
  gpiod,
  name: 'libgpiod',
  description: 'Library and tools for the Linux GPIO chardev',
)

gpiod_dep = declare_dependency(
  link_with: gpiod,
  include_directories: gpiod_includes,
  version: abi_version,
)
