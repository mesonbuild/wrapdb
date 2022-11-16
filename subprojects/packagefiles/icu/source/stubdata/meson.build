sources = files(
  'stubdata.cpp',
)

if host_machine.system() == 'windows'
  sources += windows.compile_resources(
    '../data/misc/icudata.rc',
    include_directories: incdir
  )
endif

stubdata_lib = library(
  'stubdata',
  sources,
  c_args: '-DSTUBDATA_BUILD',
  cpp_args: '-DSTUBDATA_BUILD',
  include_directories: incdir,
  version: U_ICU_VERSION,
  install: true,
)
