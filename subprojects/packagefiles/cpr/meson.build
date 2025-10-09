project(
  'cpr',
  'cpp',
  version: '1.12.0',
  license: 'MIT',
  default_options: 'cpp_std=c++17',
)

curl_dep = dependency(
  'libcurl',
  version: '>=7.64.0',
)
thread_dep = dependency('threads')

includes = include_directories('.', 'include')
subdir('cpr')

includes = include_directories('include')
install_subdir(
  'include/cpr',
  install_dir: get_option('includedir'),
)

cpr_lib = library(
  'cpr',
  include_directories: includes,
  sources: cpr_src,
  dependencies: [curl_dep, thread_dep],
  version: meson.project_version(),
  install: true,
)

cpr_dep = declare_dependency(
  include_directories: includes,
  link_with: cpr_lib,
  dependencies: [curl_dep, thread_dep],
)
meson.override_dependency('cpr', cpr_dep)

subdir('test')
