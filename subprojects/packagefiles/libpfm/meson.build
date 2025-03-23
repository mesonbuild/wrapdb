project(
  'libpfm',
  'c',
  version: '4.13.0',
  meson_version: '>=1.0.0',
)

cc = meson.get_compiler('c')

if host_machine.system() != 'linux'
  error(
    'Due to upstream bugs, this libpfm wrap does not support building for any platform other than Linux',
  )
endif

if not cc.has_header('unistd.h')
  error('libpfm does not support building without POSIX headers')
endif
if host_machine.system() == 'linux' and not cc.has_header('sys/prctl.h')
  error('libpfm does not support building for Linux without Linux headers')
endif

m_dep = cc.find_library(
  'm',
  required: false,
)
rt_dep = cc.find_library(
  'rt',
  required: false,
)
threads_dep = dependency('threads')
curses_dep = dependency(
  'curses',
  required: false,
  disabler: true,
)

add_project_arguments(
  cc.get_supported_arguments('-Wno-unused-parameter'),
  language: 'c',
)

if get_option('buildtype').contains('debug')
  add_project_arguments(
    '-DCONFIG_PFMLIB_DEBUG',
    language: 'c',
  )
endif

if host_machine.system() == 'linux'
  add_project_arguments(
    '-DCONFIG_PFMLIB_OS_LINUX',
    language: 'c',
  )
elif host_machine.system() == 'windows'
  add_project_arguments(
    '-DPFMLIB_WINDOWS',
    language: 'c',
  )
endif

# Define __WORDSIZE on platforms that don't always #define it, like Musl libc.
# This isn't completely accurate but is close enough for practical purposes.
if not cc.compiles('#include <unistd.h>\nstatic int x = __WORDSIZE;')
  add_project_arguments(
    '-D__WORDSIZE=@0@'.format(cc.sizeof('void*') * 8),
    language: 'c',
  )
endif

subdir('include')
subdir('lib')
subdir('tests')
subdir('examples')
if host_machine.system() == 'linux'
  subdir('perf_examples')
endif
