project(
  'libusb',
  'c',
  version: '1.0.26',
  meson_version: '>=0.60.0',
)

add_project_arguments('-D_GNU_SOURCE', language: 'c')

cc = meson.get_compiler('c')
pconf = import('pkgconfig')

thread_dep = dependency('threads')
udev_dep = dependency('', required: false)
macos_dep = dependency('', required: false)

if host_machine.system() == 'windows'
  add_project_arguments(
    '-D_WIN32_WINNT=0x0600',
    '-D_CRT_SECURE_NO_WARNINGS',
    cc.get_supported_arguments('-Wno-deprecated-declarations'),
    language: 'c',
  )
endif

cdata = configuration_data()
cdata.set('HAVE_SYSLOG', cc.has_function('syslog'))

if not cdata.get('HAVE_SYSLOG') and get_option('system-log')
  error('system logging requires syslog to be present')
endif

cdata.set('HAVE_CLOCK_GETTIME', cc.has_function('clock_gettime') and host_machine.system() != 'windows')
cdata.set('HAVE_EVENTFD', cc.has_function('eventfd'))
cdata.set('HAVE_TIMERFD', cc.has_function('timerfd_create'))
cdata.set('HAVE_PIPE2', cc.has_function('pipe2'))
cdata.set('HAVE_PTHREAD_CONDATTR_SETCLOCK', cc.has_function('pthread_condattr_setclock', dependencies: thread_dep))
cdata.set('HAVE_PTHREAD_SETNAME_NP', cc.has_function('pthread_setname_np', dependencies: thread_dep))
cdata.set('HAVE_PTHREAD_THREADID_NP', cc.has_function('pthread_threadid_np', dependencies: thread_dep))

cdata.set('HAVE_ASM_TYPES_H', cc.has_header('asm/types.h'))
cdata.set('HAVE_NFDS_T', cc.has_header('nfds.h'))
cdata.set('HAVE_STRING_H', cc.has_header('string.h'))
cdata.set('HAVE_SYS_TIME_H', cc.has_header('sys/time.h'))

cdata.set('HAVE_STRUCT_TIMESPEC', cc.has_header_symbol('time.h', 'struct timespec'))

if cc.has_function_attribute('format')
  cdata.set('PRINTF_FORMAT(a, b)', '__attribute__ ((__format__ (__printf__, a, b)))')
else
  cdata.set('PRINTF_FORMAT(a, b)', '')
endif

cdata.set('ENABLE_LOGGING', get_option('logging'))
cdata.set('ENABLE_DEBUG_LOGGING', get_option('debug-logging'))
cdata.set('USE_SYSTEM_LOGGING_FACILITY', get_option('system-log'))

incdirs = include_directories('libusb', 'libusb/os')
install_headers('libusb/libusb.h', subdir: 'libusb-1.0')

sources = files(
  'libusb/core.c',
  'libusb/descriptor.c',
  'libusb/hotplug.c',
  'libusb/io.c',
  'libusb/strerror.c',
  'libusb/sync.c',
)

if host_machine.system() == 'windows'
  cdata.set('PLATFORM_WINDOWS', true)
  cdata.set('DEFAULT_VISIBILITY', '')
  sources += files('libusb/os/events_windows.c', 'libusb/os/threads_windows.c')
else
  cdata.set('PLATFORM_POSIX', true)
  cdata.set('DEFAULT_VISIBILITY', '__attribute__ ((visibility ("default")))')
  sources += files('libusb/os/events_posix.c', 'libusb/os/threads_posix.c')
endif

if host_machine.system() == 'linux'
  sources += 'libusb/os/linux_usbfs.c'
  udev_dep = dependency('libudev', 'libudev-zero', required: get_option('udev'))
  if udev_dep.found()
    cdata.set('HAVE_LIBUDEV', true)
    sources += 'libusb/os/linux_udev.c'
  else
    sources += 'libusb/os/linux_netlink.c'
  endif
elif host_machine.system() == 'haiku'
  sources += files('libusb/os/haiku_pollfs.cpp', 'libusb/os/haiku_usb_backend.cpp', 'libusb/os/haiku_usb_raw.cpp')
elif host_machine.system() == 'windows'
  sources += files('libusb/os/windows_common.c', 'libusb/os/windows_usbdk.c', 'libusb/os/windows_winusb.c')
elif host_machine.system() in ['darwin', 'netbsd', 'openbsd', 'sunos']
  sources += files('libusb/os/@0@_usb.c'.format(host_machine.system()))
else
  sources += files('libusb/os/null_usb.c')
endif

if host_machine.system() == 'darwin'
  macos_dep = dependency('appleframeworks', modules: ['CoreFoundation', 'IOKit', 'Security'])
endif

configure_file(
  output: 'config.h',
  configuration: cdata,
)

config_inc = include_directories('.')

libusb = library(
  'libusb-1.0',
  sources,
  dependencies: [thread_dep, macos_dep, udev_dep],
  include_directories: incdirs,
  version: '0.3.0',
  soversion: host_machine.system() == 'windows' ? '' : '0',
  name_prefix: '',
  gnu_symbol_visibility: 'hidden',
  vs_module_defs: 'libusb/libusb-1.0.def',
  install: true,
)

pconf.generate(
  libusb,
  name: 'libusb-1.0',
  description: 'C API for USB device access from Linux, Mac OS X, Windows, OpenBSD/NetBSD and Solaris userspace',
  subdirs: 'libusb-1.0',
)

libusb_dep = declare_dependency(
  include_directories: incdirs,
  link_with: libusb,
)

subdir('examples')
subdir('tests')
