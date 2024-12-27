project(
  'cpr',
  'cpp',
  version: '1.11.1',
  license: 'MIT',
  default_options: 'cpp_std=c++17',
)

curl_dep = dependency('libcurl', version: '>=7.64.0')
thread_dep = dependency('threads')

includes = include_directories('.', 'include')
subdir('cpr')

cpr_lib = library(
  'cpr',
  include_directories: includes,
  sources: cpr_src,
  dependencies: [curl_dep, thread_dep],
)

cpr_dep = declare_dependency(
  include_directories: includes,
  link_with: cpr_lib,
  dependencies: [curl_dep, thread_dep],
)

subdir('test')
