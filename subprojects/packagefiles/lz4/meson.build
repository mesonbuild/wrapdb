# #############################################################################
# Copyright (c) 2018-present    lzutao <taolzu(at)gmail.com>
# All rights reserved.
#
# This source code is licensed under both the BSD-style license and the GPLv2.
# #############################################################################

# This is the dummy meson file from upstream, with paths adjusted.

project(
  'lz4',
  'c',
  license: 'BSD-2-Clause-Patent AND GPL-2.0-or-later',
  default_options: ['c_std=c99', 'warning_level=3'],
  version: run_command(
    find_program('build/meson/GetLz4LibraryVersion.py'),
    'lib/lz4.h',
    check: true,
  ).stdout().strip(),
  meson_version: '>=0.58.0',
)

subdir('build/meson/meson')
