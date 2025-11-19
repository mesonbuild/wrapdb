project(
  'uthash',
  'c',
  version: '2.3.0',
  license: 'BSD-1-Clause',
)

uthash_dep = declare_dependency(
  include_directories: include_directories('src'),
)

if meson.version().version_compare('>=0.54')
  meson.override_dependency('uthash', uthash_dep)
endif
