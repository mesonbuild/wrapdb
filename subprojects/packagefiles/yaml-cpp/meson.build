project(
  'yaml-cpp',
  'cpp',
  version: '0.8.0',
  meson_version: '>=0.54.0',
  license: 'MIT',
)

inc = include_directories('include')
private_inc = include_directories('include', 'src')

private_args = []
public_args = []

if meson.get_compiler('cpp').has_multi_arguments('-include', 'cstdint')
  private_args += ['-include', 'cstdint']
endif

if get_option('default_library') == 'static'
  public_args += ['-DYAML_CPP_STATIC_DEFINE']
else
  private_args += ['-Dyaml_cpp_EXPORTS']
endif

project_version_split = meson.project_version().split('.')

subdir('src')

yaml_cpp_lib = library(
  'yaml-cpp',
  src,
  include_directories: inc,
  cpp_args: [private_args, public_args],
  soversion: project_version_split[0] + '.' + project_version_split[1],
  pic: true,
)
yaml_cpp_dep = declare_dependency(
  include_directories: inc,
  link_with: yaml_cpp_lib,
  compile_args: public_args,
)
meson.override_dependency('yaml-cpp', yaml_cpp_dep)

subdir('util')

subdir('test')
