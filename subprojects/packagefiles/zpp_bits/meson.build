project(
  'zpp_bits',
  'cpp',
  version: '4.7.7',
  license: 'MIT',
  meson_version: '>=0.64.0',
  default_options: ['cpp_std=c++20'],
)

subdir('include')

zpp_bits_dep = declare_dependency(
  include_directories: incdir,
  sources: copy,
)
meson.override_dependency('zpp_bits', zpp_bits_dep)
