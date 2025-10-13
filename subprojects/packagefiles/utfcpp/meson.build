project(
  'utfcpp',
  'cpp',
  version: '4.0.8',
  license: 'MIT',
  meson_version: '>=0.54.0',
)

depinc = include_directories('source')
utfcpp_dep = declare_dependency(
  include_directories: depinc,
)

meson.override_dependency('utf8cpp', utfcpp_dep)
