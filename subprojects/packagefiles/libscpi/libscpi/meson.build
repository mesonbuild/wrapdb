subdir('src')

libscpi_inc = include_directories('inc')

libscpi_lib = library('scpi',
  libscpi_srcs,
  include_directories : libscpi_inc,
  install : true,
)

libscpi_dep = declare_dependency(
  link_with : libscpi_lib,
  include_directories : libscpi_inc,
)

# Make this library usable from the system's
# package manager.
subdir('inc/scpi')
install_headers(libscpi_hdrs, subdir : 'scpi')

pkg_mod = import('pkgconfig')
pkg_mod.generate(libscpi_lib,
  description : 'Open Source SCPI device library',
  subdirs : 'scpi',
  libraries : libscpi_lib,
)

subdir('test')
