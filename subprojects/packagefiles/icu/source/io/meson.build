sources = files(
  'locbund.cpp',
  'ufile.cpp',
  'ufmt_cmn.cpp',
  'uprintf.cpp',
  'uprntf_p.cpp',
  'uscanf.cpp',
  'uscanf_p.cpp',
  'ustdio.cpp',
  'sprintf.cpp',
  'sscanf.cpp',
  'ustream.cpp',
  'ucln_io.cpp',
)

io_lib = library('icuio',
  sources,
  include_directories : incdir,
  c_args : '-DU_IO_IMPLEMENTATION',
  cpp_args : '-DU_IO_IMPLEMENTATION',
  link_with: [i18n_lib, common_lib],
)

icuio_dep = declare_dependency(link_with: [io_lib, common_lib],
    include_directories: incdir)
meson.override_dependency('icu-io', icuio_dep)
