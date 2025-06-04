project(
  'libserialport',
  'c',
  version: '0.1.2',
  license: 'LGPL-3.0-or-later',
  meson_version: '>= 0.54.0',
)

libserialport_includes = include_directories(['.'])

libserialport_headers = files('libserialport.h')

libserialport_sources = files('serialport.c', 'timing.c')

libserialport_cflags = []
libserialport_ldflags = []

cc = meson.get_compiler('c')

# Check for visibility control
if cc.compiles(
  'void foo(void) __attribute__((visibility("hidden")));',
  name: 'visibility attribute check',
)
  sp_api = '__attribute__((visibility("default")))'
  sp_priv = '__attribute__((visibility("hidden")))'
elif cc.get_id() == 'msvc' or cc.compiles(
  '__declspec(dllexport) void foo(void);',
  name: 'declspec check',
)
  sp_api = '__declspec(dllexport)'
  sp_priv = ''
else
  sp_api = ''
  sp_priv = ''
endif

cdata = configuration_data(
  {
    'SP_API': sp_api,
    'SP_PRIV': sp_priv,
  },
)

# Function checks
cdata.set('HAVE_REALPATH', cc.has_function('realpath'))
cdata.set('HAVE_FLOCK', cc.has_function('flock'))
cdata.set('HAVE_CLOCK_GETTIME', cc.has_function('clock_gettime'))

# Header checks
cdata.set('HAVE_SYS_FILE_H', cc.has_header('sys/file.h'))

# Type checks
cdata.set(
  'HAVE_STRUCT_TERMIOS2',
  cc.has_type(
    'struct termios2',
    prefix: '#include <linux/termios.h>',
  ),
)
cdata.set(
  'HAVE_STRUCT_SERIAL_STRUCT',
  cc.has_type(
    'struct serial_struct',
    prefix: '#include <linux/serial.h>',
  ),
)
cdata.set(
  'HAVE_STRUCT_TERMIOX',
  cc.has_type(
    'struct termiox',
    prefix: '#include <linux/termios.h>',
  ),
)

# Member checks
cdata.set(
  'HAVE_STRUCT_TERMIOS_C_ISPEED',
  cc.has_member(
    'struct termios',
    'c_ispeed',
    prefix: '#include <linux/termios.h>',
  ),
)
cdata.set(
  'HAVE_STRUCT_TERMIOS_C_OSPEED',
  cc.has_member(
    'struct termios',
    'c_ospeed',
    prefix: '#include <linux/termios.h>',
  ),
)
cdata.set(
  'HAVE_STRUCT_TERMIOS2_C_ISPEED',
  cc.has_member(
    'struct termios2',
    'c_ispeed',
    prefix: '#include <linux/termios.h>',
  ),
)
cdata.set(
  'HAVE_STRUCT_TERMIOS2_C_OSPEED',
  cc.has_member(
    'struct termios2',
    'c_ospeed',
    prefix: '#include <linux/termios.h>',
  ),
)

# Header symbol check
cdata.set10(
  'HAVE_DECL_BOTHER',
  cc.has_header_symbol('linux/termios.h', 'BOTHER'),
)

# Derived defines
if cdata.get('HAVE_STRUCT_TERMIOS_C_ISPEED') and cdata.get(
  'HAVE_STRUCT_TERMIOS_C_OSPEED',
)
  cdata.set('HAVE_TERMIOS_SPEED', 1)
endif
if cdata.get('HAVE_STRUCT_TERMIOS2_C_ISPEED') and cdata.get(
  'HAVE_STRUCT_TERMIOS2_C_OSPEED',
)
  cdata.set('HAVE_TERMIOS2_SPEED', 1)
endif

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
  libserialport_ldflags += [
    '-framework',
    'IOKit',
    '-framework',
    'CoreFoundation',
  ]
elif host_machine.system() == 'freebsd'
  libserialport_sources += files('freebsd.c')
  libserialport_cflags += '-DLIBSERIALPORT_ATBUILD'
endif

configure_file(
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

pkg = import('pkgconfig')
pkg.generate(libserialport_lib)

install_headers(libserialport_headers)

libserialport_dep = declare_dependency(
  include_directories: libserialport_includes,
  link_with: libserialport_lib,
)

meson.override_dependency('libserialport', libserialport_dep)
