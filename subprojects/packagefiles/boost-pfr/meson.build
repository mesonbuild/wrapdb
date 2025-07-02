project(
  'boost-pfr',
  'cpp',
  default_options: ['cpp_std=c++11'],
  license: 'BSL-1.0',
  meson_version: '>=0.63.0',
  version: '1.88.0',
)

boost_pfr_dep = declare_dependency(
  include_directories: 'include',
)

meson.override_dependency('boost-pfr', boost_pfr_dep)
