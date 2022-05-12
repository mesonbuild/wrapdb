project('libnpupnp', 'cpp',
  version : '4.2.2',
  default_options : [ 'cpp_std=c++14' ],
  meson_version : '>=0.48',
)

cpp = meson.get_compiler('cpp')

deps = []
if host_machine.system() == 'windows'
    deps += cpp.find_library('ws2_32')
    deps += cpp.find_library('iphlpapi')
elif host_machine.system() == 'sunos'
    deps += cpp.find_library('nsl')
    deps += cpp.find_library('socket')
endif

deps += dependency('threads')
deps += dependency('libmicrohttpd')
deps += dependency('libcurl')
expat_dep = dependency('expat', required : get_option('expat'))
deps += expat_dep

if (host_machine.system() == 'windows')
  add_project_arguments('-DDLL_EXPORT', language : 'cpp')
endif

add_project_arguments('-DSMALLUT_NO_REGEX', language : 'cpp')
add_project_arguments('-DSMALLUT_EXTERNAL_INSTANTIATIONS', language : 'cpp')

libnpupnp_incdir = include_directories([ '.', 'inc', 'src/inc' ])

npupnp_sources = [
  'src/api/upnpapi.cpp',
  'src/dispatcher/miniserver.cpp',
  'src/threadutil/ThreadPool.cpp',
  'src/threadutil/TimerThread.cpp',
  'src/utils/description.cpp',
  'src/utils/genut.cpp',
  'src/utils/httputils.cpp',
  'src/utils/inet_pton.cpp',
  'src/utils/md5.cpp',
  'src/utils/netif.cpp',
  'src/utils/smallut.cpp',
  'src/utils/statcodes.cpp',
  'src/utils/uri.cpp',
  'src/utils/utf8iter.cpp',
  'src/webserver/webserver.cpp',
]

if get_option('debug')
  npupnp_sources += [
    'src/api/upnpdebug.cpp',
  ]
endif

if get_option('gena')
  npupnp_sources += [
    'src/gena/gena_callback2.cpp',
    'src/gena/gena_ctrlpt.cpp',
    'src/gena/gena_device.cpp',
    'src/gena/gena_sids.cpp',
    'src/gena/service_table.cpp',
  ]
endif

if get_option('soap')
  npupnp_sources += [
    'src/soap/soap_ctrlpt.cpp',
    'src/soap/soap_device.cpp',
  ]
endif

if get_option('ssdp')
  npupnp_sources += [
    'src/ssdp/ssdp_ctrlpt.cpp',
    'src/ssdp/ssdp_device.cpp',
    'src/ssdp/ssdpparser.cpp',
    'src/ssdp/ssdp_server.cpp',
  ]
endif

if get_option('tools')
  npupnp_sources += [
    'src/api/upnptools.cpp',
  ]
endif

libnpupnp = library('npupnp',
  npupnp_sources,
  include_directories : libnpupnp_incdir,
  gnu_symbol_visibility : 'hidden',
  version : '4.2.2',
  dependencies : deps,
  install : true,
)

auto = configuration_data()
auto.set_quoted('PACKAGE_VERSION', meson.project_version())
auto.set_quoted('NPUPNP_VERSION_STRING', meson.project_version())
ver = meson.project_version().split('.')
auto.set('NPUPNP_VERSION_MAJOR', ver[0])
auto.set('NPUPNP_VERSION_MINOR', ver[1])
auto.set('NPUPNP_VERSION_PATCH', ver[2])
auto.set('LIBUPNP_EXPORTS', 1)

if get_option('debug')
  auto.set('UPNP_HAVE_DEBUG', 1)
endif

if get_option('device')
  auto.set('UPNP_HAVE_DEVICE', 1)
endif

if expat_dep.found()
  auto.set('USE_EXPAT', 1)
endif

if get_option('gena')
  auto.set('UPNP_HAVE_GENA', 1)
endif

if get_option('optssdp')
  auto.set('UPNP_HAVE_OPTSSDP', 1)
endif

if get_option('soap')
  auto.set('UPNP_HAVE_SOAP', 1)
endif

if get_option('ssdp')
  auto.set('UPNP_HAVE_SSDP', 1)
endif

if get_option('tools')
  auto.set('UPNP_HAVE_TOOLS', 1)
endif

if get_option('unspecified_server')
  auto.set('UPNP_ENABLE_UNSPECIFIED_SERVER', 1)
endif

if get_option('webserver')
  auto.set('UPNP_HAVE_TOOLS', 1)
endif

if get_option('ipv6')
  auto.set('UPNP_ENABLE_IPV6', 1)
endif

if get_option('client')
  auto.set('UPNP_HAVE_CLIENT', 1)
endif

if get_option('webserver')
  auto.set('UPNP_HAVE_WEBSERVER', 1)
endif

if get_option('blocking_tcp_connectionsr')
  auto.set('UPNP_ENABLE_BLOCKING_TCP_CONNECTIONS', 1)
endif

if get_option('reuseaddr')
  auto.set('UPNP_MINISERVER_REUSEADDR', 1)
endif

#every platform has this
auto.set('HAVE_INET_PTON', 1)

if (host_machine.system() == 'windows')
  inet_pton_include = '#include <ws2tcpip.h>'
else
  inet_pton_include = '#include <arpa/inet.h>'
endif

ufile = configure_file(
  output : 'upnpconfig.h',
  configuration : auto
)

cfile = configure_file(
  output : 'autoconfig.h',
  configuration : auto
)

pkg = import('pkgconfig')
pkg.generate(libnpupnp)

install_headers(
  'inc/upnpdebug.h',
  'inc/UpnpGlobal.h',
  'inc/upnp.h',
  'inc/UpnpInet.h',
  'inc/upnptools.h',
  'src/inc/config.h',
  'src/inc/expatmm.hxx',
  'src/inc/gena_ctrlpt.h',
  'src/inc/gena_device.h',
  'src/inc/gena.h',
  'src/inc/gena_sids.h',
  'src/inc/genut.h',
  'src/inc/httputils.h',
  'src/inc/md5.h',
  'src/inc/miniserver.h',
  'src/inc/netif.h',
  'src/inc/picoxml.h',
  'src/inc/service_table.h',
  ufile,
)

libnpupnp_dep = declare_dependency(
  include_directories : libnpupnp_incdir,
  link_with : libnpupnp,
)
