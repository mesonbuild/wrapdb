project(
  'dragonbox',
  'cpp',
  version: '1.1.2',
  license: 'Boost',
  default_options: ['cpp_std=c++17'],
)

dragonbox_lib = library(
  'dragonbox',
  'source/dragonbox_to_chars.cpp',
  include_directories: include_directories('include'),
)

dragonbox_dep = declare_dependency(
  include_directories: include_directories('include'),
  link_with: dragonbox_lib,
)
