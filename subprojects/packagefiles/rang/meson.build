project(
  'rang',
  'cpp',
  version: '3.2',
  default_options: ['cpp_std=c++11'],
)

inc = include_directories('include')

rang_dep = declare_dependency(
  include_directories: inc,
)

doctest = dependency(
  'doctest',
  required: false,
)
if doctest.found()
  subdir('test')
endif
