sources = files(
  'locbund.cpp',
  'sprintf.cpp',
  'sscanf.cpp',
  'ucln_io.cpp',
  'ufile.cpp',
  'ufmt_cmn.cpp',
  'uprintf.cpp',
  'uprntf_p.cpp',
  'uscanf.cpp',
  'uscanf_p.cpp',
  'ustdio.cpp',
  'ustream.cpp',
)

if host_machine.system() == 'windows'
  sources += windows.compile_resources(
    'io.rc',
    include_directories: incdir
  )
endif

io_lib = library(
  'icuio',
  sources,
  include_directories: incdir,
  c_args: '-DU_IO_IMPLEMENTATION',
  cpp_args: '-DU_IO_IMPLEMENTATION',
  link_with: [i18n_lib, common_lib],
  version: U_ICU_VERSION,
  install: true,
)

icuio_dep = declare_dependency(
  link_with: [io_lib, common_lib],
  include_directories: incdir,
)

if meson.version().version_compare('>=0.54.0')
  meson.override_dependency('icu-io', icuio_dep)
endif
