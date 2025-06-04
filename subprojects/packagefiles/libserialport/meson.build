project(
  'libserialport',
  'c',
  version: '0.1.2',
  license: 'LGPL-3.0-or-later',
  meson_version: '>= 0.49.0',
)

libserialport_includes = include_directories(['.'])

libserialport_headers = files('libserialport.h')

libserialport_sources = files('serialport.c', 'timing.c')

libserialport_cflags = []
libserialport_ldflags = []

if host_machine.system() == 'linux'
  libserialport_sources += files('linux.c', 'linux_termios.c')
  libserialport_cflags += '-DLIBSERIALPORT_ATBUILD'
elif host_machine.system() == 'windows'
  libserialport_sources += files('windows.c')
  libserialport_cflags += '-DLIBSERIALPORT_MSBUILD'
  libserialport_ldflags += '-lsetupapi'
elif host_machine.system() == 'darwin'
  libserialport_sources += files('macosx.c')
  libserialport_cflags += '-DLIBSERIALPORT_ATBUILD'
elif host_machine.system() == 'freebsd'
  libserialport_sources += files('freebsd.c')
  libserialport_cflags += '-DLIBSERIALPORT_ATBUILD'
endif

cdata = configuration_data(
  {
    'SP_API': '__attribute__((visibility("default")))',
    'SP_PRIV': '__attribute__((visibility("hidden")))',
  },
)

configure_file(
  input: 'config.h.in',
  output: 'config.h',
  configuration: cdata,
)

libserialport_lib = library(
  'libserialport',
  libserialport_sources,
  c_args: libserialport_cflags,
  link_args: libserialport_ldflags,
  include_directories: libserialport_includes,
  version: '0.1.0',
  install: true,
)

install_headers(libserialport_headers)

libserialport_dep = declare_dependency(
  include_directories: libserialport_includes,
  link_with: libserialport_lib,
)
