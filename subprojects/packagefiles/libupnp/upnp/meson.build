subdir('inc')

upnp_sources = files(
  'src/api/UpnpActionComplete.c',
  'src/api/UpnpActionRequest.c',
  'src/api/UpnpDiscovery.c',
  'src/api/UpnpEvent.c',
  'src/api/UpnpEventSubscribe.c',
  'src/api/UpnpExtraHeaders.c',
  'src/api/UpnpFileInfo.c',
  'src/api/UpnpStateVarComplete.c',
  'src/api/UpnpStateVarRequest.c',
  'src/api/UpnpString.c',
  'src/api/UpnpSubscriptionRequest.c',
  'src/api/upnpapi.c',
  'src/api/upnpdebug.c',
  'src/genlib/client_table/GenlibClientSubscription.c',
  'src/genlib/client_table/client_table.c',
  'src/genlib/miniserver/miniserver.c',
  'src/genlib/net/http/httpparser.c',
  'src/genlib/net/http/httpreadwrite.c',
  'src/genlib/net/http/parsetools.c',
  'src/genlib/net/http/statcodes.c',
  'src/genlib/net/http/webserver.c',
  'src/genlib/net/sock.c',
  'src/genlib/net/uri/uri.c',
  'src/genlib/service_table/service_table.c',
  'src/genlib/util/list.c',
  'src/genlib/util/membuffer.c',
  'src/genlib/util/strintmap.c',
  'src/genlib/util/util.c',
  'src/threadutil/FreeList.c',
  'src/threadutil/LinkedList.c',
  'src/threadutil/ThreadPool.c',
  'src/threadutil/TimerThread.c',
  'src/urlconfig/urlconfig.c',
)

if get_option('gena') or get_option('optssdp')
  upnp_sources += files('src/uuid/md5.c', 'src/uuid/sysdep.c', 'src/uuid/uuid.c')
endif

if get_option('gena')
  upnp_sources += files(
    'src/gena/gena_callback2.c',
    'src/gena/gena_ctrlpt.c',
    'src/gena/gena_device.c',
  )
endif

if get_option('soap')
  upnp_sources += files(
    'src/soap/soap_common.c',
    'src/soap/soap_ctrlpt.c',
    'src/soap/soap_device.c',
  )
endif

if get_option('ssdp')
  upnp_sources += files(
    'src/ssdp/SSDPResultData.c',
    'src/ssdp/SSDPResultDataCallback.c',
    'src/ssdp/ssdp_ctrlpt.c',
    'src/ssdp/ssdp_device.c',
    'src/ssdp/ssdp_server.c',
  )
endif

if get_option('tools')
  upnp_sources += files('src/api/upnptools.c')
endif

libupnp = library(
  'libupnp',
  upnp_sources,
  include_directories: ['src/inc', 'src/threadutil', libupnp_incdir],
  dependencies: [deps, threads_dep],
  name_prefix: '',
  link_with: libixml,
  override_options: cstd,
  install: true,
  version: '17.2.8',
)

libupnp_dep = declare_dependency(
  include_directories: depinc,
  link_with: libupnp,
)

meson.override_dependency('libupnp', libupnp_dep)

pkg = import('pkgconfig')
pkg.generate(
  libupnp,
  subdirs: 'upnp',
)

subdir('sample')
