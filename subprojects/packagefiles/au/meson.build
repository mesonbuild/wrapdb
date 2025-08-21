project(
  'au',
  'cpp',
  version: '0.5.0',
  license: 'Apache-2.0',
  default_options: ['cpp_std=c++14'],
  meson_version: '>=0.54.0',
)

au_dep = declare_dependency(
  include_directories: '.',
)

meson.override_dependency('au', au_dep)
