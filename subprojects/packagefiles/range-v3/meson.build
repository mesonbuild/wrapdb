project(
  'range-v3',
  'cpp',
  version: '0.12.0',
  meson_version: '>=0.59.0',
  license: 'BSL-1.0 and NCSA and MIT and Stepanov McJones Elements of Programming and SGI STL',
)

range_inc = include_directories('include')

range_dep = declare_dependency(
  include_directories: range_inc,
)
meson.override_dependency('range-v3', range_dep)

subdir('test')
