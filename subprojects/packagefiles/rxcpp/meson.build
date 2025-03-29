project(
  'rxcpp',
  'cpp',
  version: '4.1.1',
  license: 'Apache-2.0',
)

thread_dep = dependency('threads')

rxcpp_dep = declare_dependency(
  include_directories: include_directories('Rx/v2/src'),
  dependencies: [thread_dep],
)
