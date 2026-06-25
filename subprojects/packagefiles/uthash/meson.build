project(
  'uthash',
  'c',
  version: '2.4.0',
  license: 'BSD-1-Clause',
  meson_version: '>=0.56.0',
)

uthash_dep = declare_dependency(
  include_directories: include_directories('src'),
)
meson.override_dependency('uthash', uthash_dep)
