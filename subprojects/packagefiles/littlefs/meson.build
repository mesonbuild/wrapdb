project(
  'littlefs',
  'c',
  license: 'BSD-3-Clause',
  version: '2.10.1',
  default_options: [
    'c_std=c99',
  ],
)

cc = meson.get_compiler('c')

if cc.get_id() == 'msvc'
  add_project_arguments('/Zc:preprocessor', language: 'c')
endif

littlefs_inc = include_directories('.')

littlefs_lib = library(
  'lfs',
  files('lfs.c', 'lfs_util.c'),
  include_directories: littlefs_inc,
)

littlefs_dep = declare_dependency(
  include_directories: littlefs_inc,
  link_with: littlefs_lib,
)
