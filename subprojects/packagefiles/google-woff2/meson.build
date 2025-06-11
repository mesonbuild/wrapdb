# Copyright (c) 2021 Benjamin A. Beasley
# Copyright (c) 2019-2020 Intel Corporation

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# This wrap is based closely on the google-brotli wrap.

project(
  'google-woff2',
  'cpp',
  license: 'MIT',
  version: '1.0.2',
  meson_version: '>= 0.55',
  default_options: ['cpp_std=c++11'],
)

cpp = meson.get_compiler('cpp')
# no dllexport support upstream
library_tgt = host_machine.system() == 'windows' ? 'static_library' : 'library'

inc = include_directories('include')

if not get_option('canonical_prefixes')
  add_project_arguments(
    '-no-canonical-prefixes',
    language: 'cpp',
  )
endif
if not get_option('noisy_logging')
  add_project_arguments(
    '-DFONT_COMPRESSION_BIN',
    language: 'cpp',
  )
endif
add_project_arguments(
  '-D__STDC_FORMAT_MACROS',
  language: 'cpp',
)
add_project_arguments(
  cpp.get_supported_arguments('-fno-omit-frame-pointer'),
  language: 'cpp',
)
if host_machine.system() == 'darwin'
  add_project_arguments(
    '-DOS_MACOSX',
    language: 'cpp',
  )
endif
# https://github.com/google/woff2/pull/176
if cpp.has_multi_arguments('-include', 'cstdint')
  add_project_arguments(
    '-include',
    'cstdint',
    language: 'cpp',
  )
endif

# From https://github.com/khaledhosny/ots/:
if 'undefined' in get_option('b_sanitize').split(',')
  # woff2 depends on undefined behavior otherwise.
  add_project_arguments(
    '-U__BYTE_ORDER__',
    language: 'cpp',
  )
endif

libwoff2_common = build_target(
  'woff2_common',
  files('src/table_tags.cc', 'src/variable_length.cc', 'src/woff2_common.cc'),
  target_type: library_tgt,
  include_directories: inc,
  version: meson.project_version(),
)

woff2_common_dep = declare_dependency(
  link_with: libwoff2_common,
  include_directories: inc,
  version: meson.project_version(),
)

woff2_info = executable(
  'woff2_info',
  files('src/woff2_info.cc'),
  include_directories: inc,
  link_with: libwoff2_common,
)
if meson.version().version_compare('>=0.46.0')
  meson.override_find_program('woff2_info', woff2_info)
endif

libwoff2_decoder = build_target(
  'woff2_decoder',
  files('src/woff2_dec.cc', 'src/woff2_out.cc'),
  target_type: library_tgt,
  include_directories: inc,
  link_with: libwoff2_common,
  dependencies: dependency('libbrotlidec'),
  version: meson.project_version(),
)

woff2_decoder_dep = declare_dependency(
  link_with: [libwoff2_common, libwoff2_decoder],
  include_directories: inc,
  version: meson.project_version(),
)

woff2_decompress = executable(
  'woff2_decompress',
  files('src/woff2_decompress.cc'),
  include_directories: inc,
  link_with: [libwoff2_common, libwoff2_decoder],
)
if meson.version().version_compare('>=0.46.0')
  meson.override_find_program('woff2_decompress', woff2_decompress)
endif

libwoff2_encoder = build_target(
  'woff2_encoder',
  files(
    'src/font.cc',
    'src/glyph.cc',
    'src/normalize.cc',
    'src/transform.cc',
    'src/woff2_enc.cc',
  ),
  target_type: library_tgt,
  include_directories: inc,
  link_with: libwoff2_common,
  dependencies: dependency('libbrotlienc'),
  version: meson.project_version(),
)

woff2_encoder_dep = declare_dependency(
  link_with: [libwoff2_common, libwoff2_encoder],
  include_directories: inc,
  version: meson.project_version(),
)

woff2_compress = executable(
  'woff2_compress',
  files('src/woff2_compress.cc'),
  include_directories: inc,
  link_with: [libwoff2_common, libwoff2_encoder],
)
if meson.version().version_compare('>=0.46.0')
  meson.override_find_program('woff2_compress', woff2_compress)
endif
