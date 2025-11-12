headers += files(
  'Callback.h',
  'UpnpActionComplete.h',
  'UpnpActionRequest.h',
  'UpnpDiscovery.h',
  'UpnpEvent.h',
  'UpnpEventSubscribe.h',
  'UpnpExtraHeaders.h',
  'UpnpFileInfo.h',
  'UpnpGlobal.h',
  'UpnpInet.h',
  'UpnpIntTypes.h',
  'UpnpStateVarComplete.h',
  'UpnpStateVarRequest.h',
  'UpnpStdInt.h',
  'UpnpString.h',
  'UpnpSubscriptionRequest.h',
  'UpnpUniStd.h',
  'list.h',
  'upnp.h',
)

ufile = configure_file(
  input: 'upnpconfig.h.cm',
  output: 'upnpconfig.h',
  format: 'cmake',
  configuration: uconf,
)

headers += ufile

if get_option('tools')
  headers += files('upnptools.h')
endif

install_headers(
  headers,
  subdir: 'upnp',
)
