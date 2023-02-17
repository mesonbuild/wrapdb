project(
  'simdjson',
  'cpp',
  license: 'Apache-2.0',
  version: '3.1.1',
)

simdjson_inc = include_directories('singleheader')

simdjson_lib = library(
  'simdjson',
  sources: files('singleheader/simdjson.cpp'),
  include_directories: simdjson_inc,
)

simdjson_dep = declare_dependency(
  include_directories: simdjson_inc,
  link_with: simdjson_lib,
)
