project(
  'nonstd-expected-lite',
  'cpp',
  version: '0.3.0',
  license: 'BSL-1.0',
)

includes = include_directories('include')

nonstd_expected_lite_dep = declare_dependency(
  include_directories: includes,
)

if meson.version().version_compare('>= 0.54.0')
  meson.override_dependency('expected-lite', nonstd_expected_lite_dep)
endif
