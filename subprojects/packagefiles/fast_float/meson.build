project(
  'fast_float',
  'cpp',
  license: 'Apache-2.0 or BSL-1.0 or MIT',
  meson_version: '>=0.56.0',
  version: '8.2.4',
)

install_subdir(
  'include/fast_float',
  install_dir: get_option('includedir'),
)

fast_float_dep = declare_dependency(
  include_directories: 'include',
)

meson.override_dependency('FastFloat', fast_float_dep)
