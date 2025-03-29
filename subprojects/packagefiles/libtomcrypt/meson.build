project(
  'libtomcrypt',
  'c',
  version: '1.18.2',
  license: 'Public Domain',
)

add_project_arguments(
  '-DLTC_NO_ASM',
  '-DLTC_SOURCE',
  language: 'c',
)

core_inc = include_directories('src/headers')
all_sources = []
extra_objects = []

subdir('src')

tomcryptlib = library(
  'tomcrypt',
  all_sources,
  objects: extra_objects,
  include_directories: core_inc,
)

tomcrypt_dep = declare_dependency(
  link_with: tomcryptlib,
  include_directories: core_inc,
)
