# #############################################################################
# Copyright (c) 2018-present    lzutao <taolzu(at)gmail.com>
# All rights reserved.
#
# This source code is licensed under both the BSD-style license and the GPLv2.
# #############################################################################

# This is the dummy meson file from upstream, with version and path adjusted.

project(
  'lz4',
  'c',
  license: 'BSD-2-Clause-Patent AND GPL-2.0-or-later',
  default_options: [
    'c_std=c99',
    'buildtype=release',
    'warning_level=3'
  ],
  version: '1.9.4',
  meson_version: '>=0.49.0'
)

# upstream meson.build has this as c_args that get passed to nowhere
if host_machine.system() == 'windows' and get_option('default_library') != 'static'
  add_project_arguments('-DLZ4_DLL_EXPORT=1', language: 'c')
endif

if get_option('unstable')
  add_project_arguments('-DLZ4_STATIC_LINKING_ONLY', language: 'c')
  if get_option('default_library') != 'static'
    add_project_arguments('-DLZ4_PUBLISH_STATIC_FUNCTIONS', language: 'c')
  endif
endif

subdir('contrib/meson/meson')
