project(
  'yaml-cpp',
  'cpp',
  version: '0.8.0',
  meson_version: '>=0.63.0',
  default_options: ['cpp_std=c++11'],
  license: 'MIT',
)

inc = include_directories('include')
subdir('src')
yaml_cpp_private_inc = include_directories('include', 'src')

project_version_split = meson.project_version().split('.')
lib_cpp_args = []
cc = meson.get_compiler('cpp')
if cc.has_multi_arguments('-include', 'cstdint')
  lib_cpp_args += ['-include', 'cstdint']
endif
if not meson.is_subproject()
  lib_cpp_args += cc.get_supported_arguments(
    '-Wall',
    '-Wextra',
    '-Wshadow',
    '-Weffc++',
    '-Wno-long-long',
    '-pedantic',
    '-pedantic-errors',
  )
endif

compile_args = []
if get_option('default_library') == 'static'
  compile_args += ['-DYAML_CPP_STATIC_DEFINE']
else
  lib_cpp_args += ['-Dyaml_cpp_EXPORTS']
endif
yaml_cpp_lib = library(
  'yaml-cpp',
  src,
  include_directories: inc,
  cpp_args: [lib_cpp_args, compile_args],
  soversion: project_version_split[0] + '.' + project_version_split[1],
  pic: true,
)
yaml_cpp_dep = declare_dependency(
  include_directories: inc,
  link_with: yaml_cpp_lib,
  compile_args: compile_args,
)
meson.override_dependency('yaml-cpp', yaml_cpp_dep)

if get_option('tools')
  subdir('util')
endif

tests_feature = get_option('tests').disable_auto_if(meson.is_subproject())
if tests_feature.allowed()
  subdir('test')
endif

if not meson.is_subproject()
  clang_format_prog = find_program(
    'clang-format',
    required: false,
  )
  if clang_format_prog.found()
    run_target(
      'format',
      command: [clang_format_prog, '--style=file', '-i', src],
    )
  endif
endif
