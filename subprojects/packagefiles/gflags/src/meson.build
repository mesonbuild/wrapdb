gflags_srcs = files('gflags.cc', 'gflags_completions.cc', 'gflags_reporting.cc')
if is_windows
  gflags_srcs += files('windows_port.cc')
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
  version: project_version,
  soversion: project_soversion,
)

gflags_dep = declare_dependency(
  link_with: gflags_lib,
  include_directories: incdir,
  compile_args: gflags_defines,
)
