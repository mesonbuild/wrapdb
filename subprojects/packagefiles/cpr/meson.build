project(
  'cpr',
  'cpp',
  version: '1.9.6',
  license: 'MIT',
  default_options: 'cpp_std=c++14',
)

curl_dep = dependency('libcurl')
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
)

gtest_dep = dependency('gtest', required: get_option('tests'))
if gtest_dep.found()
  subdir('test')
endif
