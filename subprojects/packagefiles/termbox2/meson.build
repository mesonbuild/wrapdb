project(
  'termbox2',
  'c',
  license: 'MIT',
  version: '2.5.0',
  default_options: ['c_std=c99', 'warning_level=3'],
  meson_version: '>=0.54.0',
)

if host_machine.system() == 'windows'
  error('termbox2 does not support Windows')
endif

c_args = [
  '-Wno-unused-result',
  '-D_XOPEN_SOURCE',
  '-D_DEFAULT_SOURCE',
  '-DTB_IMPL',
]
src = configure_file(
  copy: true,
  input: 'termbox2.h',
  output: 'termbox2.c',
)
lib = library(
  'termbox2',
  src,
  c_args: c_args,
)

inc = include_directories('.')

termbox2_dep = declare_dependency(
  link_with: lib,
  include_directories: inc,
)
meson.override_dependency('termbox2', termbox2_dep)
