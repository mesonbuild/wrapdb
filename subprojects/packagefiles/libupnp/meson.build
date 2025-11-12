project(
  'pupnp',
  'c',
  license: 'BSD-3-Clause',
  version: '1.14.25',
  meson_version: '>=0.54.1',
)

cstd = 'c_std=gnu99'

cc = meson.get_compiler('c')
if cc.get_argument_syntax() == 'msvc'
  error('MSVC is unsupported. Requires custom pthread library')
endif

ver = meson.project_version().split('.')
uconf = configuration_data()
uconf.set('IXML_HAVE_SCRIPTSUPPORT', true)
uconf.set('UPNP_VERSION_MAJOR', ver[0])
uconf.set('UPNP_VERSION_MINOR', ver[1])
uconf.set('UPNP_VERSION_PATCH', ver[2])

foreach h : [
  'client',
  'device',
  'gena',
  'tools',
  'optssdp',
  'soap',
  'ssdp',
  'webserver',
]
  if get_option(h)
    uconf.set('UPNP_HAVE_@0@'.format(h.to_upper()), 1)
  endif
endforeach

foreach e : [
  'blocking_tcp_connectionsr',
  'ipv6',
  'open_ssl',
  'unspecified_server',
]
  if get_option(e)
    uconf.set('UPNP_ENABLE_@0@'.format(e.to_upper()), 1)
  endif
endforeach

uconf.set10('UPNP_MINISERVER_REUSEADDR', get_option('reuseaddr'))

aconf = configuration_data()
aconf.merge_from(uconf)

uconf.set('UPNP_VERSION_STRING', meson.project_version())
aconf.set_quoted('UPNP_VERSION_STRING', meson.project_version())
aconf.set10('UPNP_HAVE_DEBUG', get_option('debug'))
aconf.set10(
  'UPNP_USE_RWLOCK',
  cc.has_header_symbol(
    'pthread.h',
    'pthread_rwlock_t',
    args: '-D_XOPEN_SOURCE=500',
  ),
)
aconf.set10('HAVE_STRNDUP', cc.has_function('strndup'))
aconf.set10('HAVE_STRNLEN', cc.has_function('strnlen'))

afile = configure_file(
  output: 'autoconfig.h',
  configuration: aconf,
)

deps = []
if host_machine.system() == 'windows'
  deps += cc.find_library('ws2_32')
  deps += cc.find_library('iphlpapi')
elif host_machine.system() == 'sunos'
  deps += cc.find_library('nsl')
  deps += cc.find_library('socket')
endif
deps += dependency(
  'libcrypto',
  required: get_option('open_ssl'),
)

libupnp_incdir = include_directories('.', 'ixml/inc', 'upnp/inc')
depinc = include_directories('ixml/inc', 'upnp/inc')
threads_dep = dependency('threads')

subdir('ixml')
subdir('upnp')
