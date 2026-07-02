project(
  'geo-utils-cpp',
  'cpp',
  version: '1.2.0',
  license: 'Apache-2.0',
  meson_version: '>=0.56.0',
  default_options: ['cpp_std=c++17'],
)

geo_utils_cpp_dep = declare_dependency(
  include_directories: include_directories('include'),
)

meson.override_dependency('geo-utils-cpp', geo_utils_cpp_dep)

install_subdir(
  'include/geo',
  install_dir: get_option('includedir'),
)

# Upstream's self-verifying end-to-end example doubles as a smoke test.
geo_utils_cpp_smoke = executable(
  'geo_utils_cpp_smoke',
  'examples/gps_track.cpp',
  dependencies: geo_utils_cpp_dep,
)
test('smoke', geo_utils_cpp_smoke)
