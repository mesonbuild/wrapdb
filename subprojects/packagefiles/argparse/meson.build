project(
  'argparse',
  'cpp',
  version: '3.2',
  license: 'MIT',
  meson_version: '>=0.49.0',
)

includes = include_directories(['include'])

install_headers(
  ['include/argparse/argparse.hpp'],
  subdir: 'argparse',
)

argparse_dep = declare_dependency(
  include_directories: includes,
)

import('pkgconfig').generate(
  name: meson.project_name(),
  description: 'A single header argument parser for C++17',
  install_dir: get_option('datadir') / 'pkgconfig',
)
