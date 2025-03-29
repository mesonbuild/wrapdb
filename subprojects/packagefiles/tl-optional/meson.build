project(
  'tl-optional',
  'cpp',
  license: 'CC0-1.0',
  version: '1.0.0',
)

tl_optional_dep = declare_dependency(
  include_directories: include_directories('include'),
)

if meson.version().version_compare('>=0.54.0')
  meson.override_dependency('tl-optional', tl_optional_dep)
endif
