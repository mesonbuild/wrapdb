project(
  'utfcpp',
  'cpp',
  version: '3.2.2',
  license: 'MIT',
  meson_version: '>=0.49.0',
)

depinc = include_directories('source')
utfcpp_dep = declare_dependency(
  include_directories: depinc,
)

executable(
  'docsample',
  'samples/docsample.cpp',
  dependencies: utfcpp_dep,
)
