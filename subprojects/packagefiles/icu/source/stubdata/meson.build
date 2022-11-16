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
  include_directories: incdir,
)
