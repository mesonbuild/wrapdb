project(
  'boost-mp11',
  'cpp',
  version: '1.88.0',
  license: 'BSL-1.0',
  default_options: ['cpp_std=c++11'],
)

boost_mp11_dep = declare_dependency(
  include_directories: 'include',
)

meson.override_dependency('boost-mp11', boost_mp11_dep)
