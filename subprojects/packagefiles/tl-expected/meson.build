project(
  'tl-expected',
  'cpp',
  license: 'CC0-1.0',
  version: '1.3.1',
)

tl_expected_dep = declare_dependency(
  include_directories: include_directories('include'),
)

if meson.version().version_compare('>=0.54.0')
  meson.override_dependency('tl-expected', tl_expected_dep)
endif
