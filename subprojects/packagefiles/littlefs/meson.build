project(
  'littlefs',
  'c',
  license: 'BSD-3-Clause',
  version: '2.11.2',
)

cc = meson.get_compiler('c')

if cc.get_id() == 'msvc'
  add_project_arguments(
    '/Zc:preprocessor',
    language: 'c',
  )
endif

littlefs_inc = include_directories('.')

littlefs_lib = library(
  'lfs',
  files('lfs.c', 'lfs_util.c'),
  include_directories: littlefs_inc,
  override_options: ['c_std=c99'],
)

littlefs_dep = declare_dependency(
  include_directories: littlefs_inc,
  link_with: littlefs_lib,
)
if meson.version().version_compare('>=0.54.0')
  meson.override_dependency('littlefs', littlefs_dep)
endif
