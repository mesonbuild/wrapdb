project(
  'gflags',
  'cpp',
  'c',
  version: '2.2.2',
  default_options: ['default_library=static'],
)

incdir = include_directories('src', 'src/gflags')

is_windows = host_machine.system() == 'windows'
cc = meson.get_compiler('cpp')
if get_option('default_library') == 'static'
  gflags_is_a_dll = false
else
  gflags_is_a_dll = true
endif

subdir('src/gflags')

gflags_srcs = files(
  'src/gflags.cc',
  'src/gflags_completions.cc',
  'src/gflags_reporting.cc',
)
if is_windows
  gflags_srcs += files('src/windows_port.cc')
endif

gflags_defines = []
if gflags_is_a_dll
  gflags_defines += ['-DGFLAGS_IS_A_DLL=1']
else
  gflags_defines += ['-DGFLAGS_IS_A_DLL=0']
endif

gflags_lib = library(
  'gflags',
  sources: gflags_srcs,
  include_directories: incdir,
  cpp_args: gflags_defines,
  install: true,
)

gflags_dep = declare_dependency(
  link_with: gflags_lib,
  include_directories: incdir,
  compile_args: gflags_defines,
)
