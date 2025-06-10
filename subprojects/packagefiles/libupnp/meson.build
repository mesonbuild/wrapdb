project(
  'pupnp',
  'c',
  license: 'BSD-3-Clause',
  version: '1.14.23',
  meson_version: '>=0.54.1',
)

cc = meson.get_compiler('c')
if cc.get_argument_syntax() == 'msvc'
  error('MSVC is unsupported. Requires custom pthread library')
endif

if meson.project_version() == '1.14.23'
  # https://github.com/pupnp/pupnp/pull/487
  add_project_arguments(
    cc.get_supported_arguments('-Wno-incompatible-pointer-types'),
    language: 'c',
  )
endif

libupnp_incdir = include_directories(
  '.',
  'upnp/inc',
  'upnp/src/inc',
  'upnp/src/threadutil',
)
libixml_incdir = include_directories('ixml/inc', 'ixml/src/inc')

libixml = static_library(
  'ixml',
  'ixml/src/attr.c',
  'ixml/src/document.c',
  'ixml/src/element.c',
  'ixml/src/ixml.c',
  'ixml/src/ixmldebug.c',
  'ixml/src/ixmlmembuf.c',
  'ixml/src/ixmlparser.c',
  'ixml/src/namedNodeMap.c',
  'ixml/src/node.c',
  'ixml/src/nodeList.c',
  include_directories: [libixml_incdir, libupnp_incdir],
  pic: true,
)

upnp_sources = files(
  'upnp/src/api/UpnpActionComplete.c',
  'upnp/src/api/UpnpActionRequest.c',
  'upnp/src/api/UpnpDiscovery.c',
  'upnp/src/api/UpnpEvent.c',
  'upnp/src/api/UpnpEventSubscribe.c',
  'upnp/src/api/UpnpExtraHeaders.c',
  'upnp/src/api/UpnpFileInfo.c',
  'upnp/src/api/UpnpStateVarComplete.c',
  'upnp/src/api/UpnpStateVarRequest.c',
  'upnp/src/api/UpnpString.c',
  'upnp/src/api/UpnpSubscriptionRequest.c',
  'upnp/src/api/upnpapi.c',
  'upnp/src/api/upnpdebug.c',
  'upnp/src/genlib/client_table/GenlibClientSubscription.c',
  'upnp/src/genlib/client_table/client_table.c',
  'upnp/src/genlib/miniserver/miniserver.c',
  'upnp/src/genlib/net/http/httpparser.c',
  'upnp/src/genlib/net/http/httpreadwrite.c',
  'upnp/src/genlib/net/http/parsetools.c',
  'upnp/src/genlib/net/http/statcodes.c',
  'upnp/src/genlib/net/http/webserver.c',
  'upnp/src/genlib/net/sock.c',
  'upnp/src/genlib/net/uri/uri.c',
  'upnp/src/genlib/service_table/service_table.c',
  'upnp/src/genlib/util/list.c',
  'upnp/src/genlib/util/membuffer.c',
  'upnp/src/genlib/util/strintmap.c',
  'upnp/src/genlib/util/util.c',
  'upnp/src/threadutil/FreeList.c',
  'upnp/src/threadutil/LinkedList.c',
  'upnp/src/threadutil/ThreadPool.c',
  'upnp/src/threadutil/TimerThread.c',
  'upnp/src/urlconfig/urlconfig.c',
)

if get_option('gena') or get_option('optssdp')
  upnp_sources += files(
    'upnp/src/uuid/md5.c',
    'upnp/src/uuid/sysdep.c',
    'upnp/src/uuid/uuid.c',
  )
endif

if get_option('gena')
  upnp_sources += files(
    'upnp/src/gena/gena_callback2.c',
    'upnp/src/gena/gena_ctrlpt.c',
    'upnp/src/gena/gena_device.c',
  )
endif

if get_option('soap')
  upnp_sources += files(
    'upnp/src/soap/soap_common.c',
    'upnp/src/soap/soap_ctrlpt.c',
    'upnp/src/soap/soap_device.c',
  )
endif

if get_option('ssdp')
  upnp_sources += files(
    'upnp/src/ssdp/SSDPResultData.c',
    'upnp/src/ssdp/SSDPResultDataCallback.c',
    'upnp/src/ssdp/ssdp_ctrlpt.c',
    'upnp/src/ssdp/ssdp_device.c',
    'upnp/src/ssdp/ssdp_server.c',
  )
endif

if get_option('tools')
  upnp_sources += files('upnp/src/api/upnptools.c')
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

ufile = configure_file(
  input: 'upnp/inc/upnpconfig.h.cm',
  output: 'upnpconfig.h',
  format: 'cmake',
  configuration: uconf,
)
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
threads_dep = dependency('threads')

libupnp = library(
  'upnp',
  upnp_sources,
  include_directories: [libixml_incdir, libupnp_incdir],
  dependencies: [deps, threads_dep],
  link_with: libixml,
  install: true,
  version: '17.2.3',
)

pkg = import('pkgconfig')
pkg.generate(
  libupnp,
  name: 'libupnp',
  subdirs: 'upnp',
)

headers = files(
  'ixml/inc/ixml.h',
  'ixml/inc/ixmldebug.h',
  'upnp/inc/Callback.h',
  'upnp/inc/UpnpActionComplete.h',
  'upnp/inc/UpnpActionRequest.h',
  'upnp/inc/UpnpDiscovery.h',
  'upnp/inc/UpnpEvent.h',
  'upnp/inc/UpnpEventSubscribe.h',
  'upnp/inc/UpnpExtraHeaders.h',
  'upnp/inc/UpnpFileInfo.h',
  'upnp/inc/UpnpGlobal.h',
  'upnp/inc/UpnpInet.h',
  'upnp/inc/UpnpIntTypes.h',
  'upnp/inc/UpnpStateVarComplete.h',
  'upnp/inc/UpnpStateVarRequest.h',
  'upnp/inc/UpnpStdInt.h',
  'upnp/inc/UpnpString.h',
  'upnp/inc/UpnpSubscriptionRequest.h',
  'upnp/inc/UpnpUniStd.h',
  'upnp/inc/list.h',
  'upnp/inc/upnp.h',
)

headers += ufile

if get_option('tools')
  headers += files('upnp/inc/upnptools.h')
endif

install_headers(
  headers,
  subdir: 'upnp',
)

libupnp_dep = declare_dependency(
  include_directories: [libixml_incdir, libupnp_incdir],
  link_with: libupnp,
)

if get_option('samples') and get_option('tools')
  sample_conf = configuration_data()
  sample_file = configure_file(
    output: 'config_sample.h',
    configuration: sample_conf,
  )

  toolinc = include_directories('upnp/sample/common')

  if get_option('client')
    executable(
      'tv_ctrlpt',
      'upnp/sample/common/sample_util.c',
      'upnp/sample/common/tv_ctrlpt.c',
      'upnp/sample/linux/tv_ctrlpt_main.c',
      include_directories: toolinc,
      dependencies: [libupnp_dep, threads_dep],
      install: true,
    )
  endif

  if get_option('client') and get_option('device')
    executable(
      'tv_combo',
      'upnp/sample/common/sample_util.c',
      'upnp/sample/common/tv_ctrlpt.c',
      'upnp/sample/common/tv_device.c',
      'upnp/sample/linux/tv_combo_main.c',
      include_directories: toolinc,
      dependencies: [libupnp_dep, threads_dep],
      install: true,
    )
  endif

  if get_option('device')
    executable(
      'tv_device',
      'upnp/sample/common/sample_util.c',
      'upnp/sample/common/tv_device.c',
      'upnp/sample/linux/tv_device_main.c',
      include_directories: toolinc,
      dependencies: [libupnp_dep, threads_dep],
      install: true,
    )

    install_subdir(
      'upnp/sample/web',
      install_dir: 'share/upnp',
      strip_directory: true,
    )
  endif
endif
