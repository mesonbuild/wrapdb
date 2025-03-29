project(
  'nowide',
  'cpp',
  version: '11.3.0',
  license: 'BSL-1.0',
  default_options: ['cpp_std=c++14'],
  meson_version: '>=0.53.0',
)

compile_args = []

if get_option('default_library') != 'static'
  add_project_arguments(
    '-DNOWIDE_DYN_LINK',
    language: 'cpp',
  )
  compile_args += ['-DNOWIDE_DYN_LINK']
endif

sources = []

subdir('src')  # fills in 'sources'

includes = include_directories('include')

install_subdir(
  'include/nowide',
  install_dir: get_option('includedir'),
)

nowide_lib = library(
  'nowide',
  sources,
  include_directories: includes,
  version: meson.project_version(),
  install: true,
)

nowide_dep = declare_dependency(
  compile_args: compile_args,
  include_directories: includes,
  link_with: nowide_lib,
)

if get_option('tests')
  subdir('test')
endif
