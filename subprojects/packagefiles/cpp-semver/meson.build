project(
  'cpp-semver',
  'cpp',
  version: '0.3.3',
  license: 'MIT',
  meson_version: '>=1.2.0',
  default_options: {
    'cpp_std': ['c++17'],
  },
)

install_subdir(
  'include',
  install_dir: get_option('includedir'),
)

cpp_semver_dep = declare_dependency(
  include_directories: include_directories('include'),
  version: meson.project_version(),
)

meson.override_dependency('cpp-semver', cpp_semver_dep)

if get_option('tests')
  subdir('test')
endif
