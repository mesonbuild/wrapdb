project(
  'lwip',
  'c',
  'cpp',
  license: 'BSD-3-Clause',
  meson_version: '>=0.63.0',
  version: '2.2.1',
)

lwip_debug = get_option('lwip_debug')
if lwip_debug.enabled() or (lwip_debug.auto() and get_option('debug'))
  add_project_arguments(
    '-DLWIP_DEBUG',
    language: ['c', 'cpp'],
  )
endif

ndebug = get_option('b_ndebug')
if ndebug == 'true' or (ndebug == 'if-release' and not get_option('debug'))
  add_project_arguments(
    '-DLWIP_NOASSERT',
    language: ['c', 'cpp'],
  )
endif

# lwipopts.h must be specified as dependency like that:
#
# lwipopts_dep = declare_dependency(
#   sources: 'configs/lwipopts.h',
#   include_directories: 'configs',
# )
# meson.override_dependency('lwip-opts', lwipopts_dep)
#
# If not specified then we use config from examples as fallback.
lwipopts_dep = dependency(
  'lwip-opts',
  required: false,
)
if not lwipopts_dep.found()
  lwipopts_dep = declare_dependency(
    sources: 'contrib/ports/unix/lib/lwipopts.h',
    include_directories: 'contrib/ports/unix/lib/',
  )
endif

lwipport_dep = dependency(
  'lwip-port',
  required: false,
)
if not lwipport_dep.found()
  lwipport_dep = declare_dependency(
    sources: files(
      'contrib/ports/unix/port/netif/fifo.c',
      'contrib/ports/unix/port/netif/list.c',
      'contrib/ports/unix/port/netif/sio.c',
      'contrib/ports/unix/port/netif/tapif.c',
      'contrib/ports/unix/port/perf.c',
      'contrib/ports/unix/port/sys_arch.c',
    ),
    include_directories: 'contrib/ports/unix/port/include',
  )
endif

subdir('src')
