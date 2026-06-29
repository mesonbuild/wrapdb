project(
  'x265',
  'c',
  'cpp',
  version: '4.1',
  meson_version: '>= 1.3.0',
  license: 'GPL-2.0-or-later',
  license_files: 'COPYING',
  default_options: [
    'c_std=gnu11,c11',
    'cpp_std=gnu++14,c++14',
    'warning_level=2',
  ],
)

if get_option('optimization') != '3'
  message(
    'This library expects to be built with -Doptimization=3. If you find any visual artifacts, consider adding this flag.',
  )
endif

subdir('source')

x265_dep = declare_dependency(
  link_with: x265_lib,
  include_directories: include_dirs,
)

meson.override_dependency('x265', x265_dep)
