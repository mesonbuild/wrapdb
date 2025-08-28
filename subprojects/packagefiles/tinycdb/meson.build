# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileCopyrightText: 2025 GNOME Foundation, Inc.
project(
  'tinycdb',
  'c',
  version: '0.81',
  license: 'MIT',
  meson_version: '>= 0.54.0',
)

if host_machine.system() in ['windows', 'cygwin']
  error('tinycdb is not supported on non-POSIX platforms.')
endif

lib_srcs = files(
  'cdb_find.c',
  'cdb_findnext.c',
  'cdb_hash.c',
  'cdb_init.c',
  'cdb_make.c',
  'cdb_make_add.c',
  'cdb_make_put.c',
  'cdb_pack.c',
  'cdb_seek.c',
  'cdb_seq.c',
  'cdb_unpack.c',
)

tinycdb = static_library(
  'cdb',
  lib_srcs,
  cpp_args: ['-D_FILE_OFFSET_BITS=64'],
)

tinycdb_dep = declare_dependency(
  include_directories: include_directories('.'),
  link_with: tinycdb,
)

meson.override_dependency('libcdb', tinycdb_dep)
