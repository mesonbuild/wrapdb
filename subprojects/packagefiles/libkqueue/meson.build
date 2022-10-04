project(
  'libkqueue',
  'c',
  version: '2.6.1',
  license: 'BSD',
  meson_version: '>=0.48.0',
  default_options: ['c_std=c11'],
)

varr = meson.project_version().split('.')
version_major = varr[0]
version_minor = varr[1]
version_patch = varr[2]

cc = meson.get_compiler('c')

cdata = configuration_data()
vdata = configuration_data()

vdata.set('PROJECT_VERSION', meson.project_version())
vdata.set('PROJECT_VERSION_MAJOR', version_major)
vdata.set('PROJECT_VERSION_MINOR', version_minor)
vdata.set('PROJECT_VERSION_PATCH', version_patch)
vdata.set('PROJECT_VERSION_DATE', '')

check_headers = [
  'sys/signalfd.h',
  'sys/timerfd.h',
  'sys/eventfd.h',
  'sys/types.h',
]

foreach header : check_headers
  cdata.set10('HAVE_@0@'.format(header.underscorify().to_upper()), cc.has_header(header))
endforeach

cdata.set10('HAVE_NOTE_TRUNCATE', cc.has_header_symbol('sys/event.h', 'NOTE_TRUNCATE'))
cdata.set10('HAVE_EPOLLRDHUP', cc.has_header_symbol('sys/epoll.h', 'HAVE_EPOLLRDHUP'))
cdata.set10('HAVE_DECL_PPOLL', cc.has_function('ppoll'))
cdata.set10('HAVE_SYS_PIDFD_OPEN', cc.has_function('pidfd_open'))

kqueue_sources = [
  'src/common/alloc.h',
  'src/common/debug.h',
  'src/common/debug.c',
  'src/common/filter.c',
  'src/common/kevent.c',
  'src/common/knote.c',
  'src/common/kqueue.c',
  'src/common/libkqueue.c',
  'src/common/map.c',
  'src/common/private.h',
  'src/common/queue.h',
  'src/common/tree.h',
]

kqueue_inc = [
  'include',
]

kqueue_args = []

kqueue_deps = [dependency('threads')]

if target_machine.system() == 'windows'
  kqueue_sources += [
    'src/windows/platform.c',
    'src/windows/platform.h',
    'src/windows/read.c',
    'src/windows/stdint.h',
    'src/windows/timer.c',
    'src/windows/user.c',
  ]

  kqueue_args += ['-D_USRDLL', '-D_WINDLL', '-D_CRT_SECURE_NO_WARNINGS', '-DWIN32_LEAN_AND_MEAN']

  kqueue_deps += cc.find_library('ws2_32')
elif target_machine.system() == 'linux'
  kqueue_sources += [
    'src/linux/platform.c',
    'src/linux/platform.h',
    'src/linux/read.c',
    'src/linux/signal.c',
    'src/linux/timer.c',
    'src/linux/user.c',
    'src/linux/vnode.c',
    'src/linux/write.c',
  ]

  if cdata.get('HAVE_SYS_PIDFD_OPEN', 0) == 1
    kqueue_sources += 'src/linux/proc.c'
  else
    kqueue_sources += 'src/posix/proc.c'
  endif

  kqueue_inc += 'src/common'

  kqueue_args += [
    '-D_XOPEN_SOURCE=600',
  ]
elif target_machine.system() == 'sunos'
  kqueue_sources += [
    'src/posix/eventfd.c',
    'src/posix/eventfd.h',
    'src/solaris/platform.c',
    'src/solaris/platform.h',
    'src/solaris/signal.c',
    'src/solaris/socket.c',
    'src/solaris/timer.c',
    'src/solaris/user.c',
  ]

  kqueue_inc += 'src/common'

  kqueue_args += [
    '-D_XOPEN_SOURCE=600',
  ]
else
  error('unsupported host os')
endif

configure_file(
  input: 'config.h.in',
  output: 'config.h',
  format: 'cmake',
  configuration: cdata,
)

configure_file(
  input: 'version.h.in',
  output: 'version.h',
  format: 'cmake@',
  configuration: vdata,
)

libkqueue = library(
  'kqueue',
  kqueue_sources,
  include_directories: kqueue_inc,
  c_args: kqueue_args,
  dependencies: kqueue_deps,
)

libkqueue_dep = declare_dependency(
  link_with: libkqueue,
  include_directories: kqueue_inc,
)
