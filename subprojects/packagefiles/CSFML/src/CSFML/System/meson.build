system_sources = files(
  'Alloc.cpp',
  'Buffer.cpp',
  'Clock.cpp',
  'Sleep.cpp',
  'Time.cpp',
)

system_lib = library(
  'csfml-system',
  system_sources,
  cpp_args: get_option('default_library') != 'static' ? '-DCSFML_SYSTEM_EXPORTS' : '-DCSFML_STATIC',
  include_directories: [private_include, public_include],
  dependencies: deps,
  install: true,
)
