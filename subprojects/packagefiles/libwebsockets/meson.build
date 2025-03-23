project(
  'libwebsockets',
  'c',
  version: '4.3.3',
  meson_version: '>=0.54.1',
)

cdata = configuration_data()
cdata.set('CMAKE_INSTALL_PREFIX', get_option('prefix'))
cdata.set('LWS_INSTALL_LIB_DIR', get_option('libdir'))
cdata.set('LIB_SUFFIX', '')

vers = meson.project_version().split('.')

cdata.set('LWS_LIBRARY_VERSION_MAJOR', vers[0])
cdata.set('LWS_LIBRARY_VERSION_MINOR', vers[1])
cdata.set('LWS_LIBRARY_VERSION_PATCH', vers[2])
cdata.set(
  'LWS_LIBRARY_VERSION_PATCH_ELABORATED',
  '@0@-@1@'.format(vers[2], 'unknown'),
)
cdata.set(
  'LWS_LIBRARY_VERSION',
  '@0@-@1@'.format(meson.project_version(), 'unknown'),
)

cdata.set('LWS_PLAT_UNIX', host_machine.system() != 'windows')

cdata.set('LWS_MAX_SMP', 1)
cdata.set('LWS_BUILD_HASH', 'unknown')

cdata.set('LWS_LOGGING_BITFIELD_SET', 0)
cdata.set('LWS_LOGGING_BITFIELD_CLEAR', 0)
cdata.set('LWS_CLIENT_HTTP_PROXYING', true)

cdata.set('LWS_WITH_NETWORK', true)
cdata.set('LWS_ROLE_H1', true)
cdata.set('LWS_ROLE_H2', true)
cdata.set('LWS_ROLE_WS', true)
cdata.set('LWS_ROLE_MQTT', false)
cdata.set('LWS_ROLE_RAW_PROXY', false)
cdata.set('LWS_ROLE_RAW_FILE', true)
cdata.set('LWS_WITH_HTTP2', true)
cdata.set('LWS_WITH_LWSWS', false)
cdata.set('LWS_WITH_CGI', false)
cdata.set('LWS_IPV6', false)
cdata.set('LWS_UNIX_SOCK', true)
cdata.set('LWS_WITH_PLUGINS_BUILTIN', false)
cdata.set('LWS_WITH_HTTP_PROXY', false)
cdata.set('LWS_WITH_ZIP_FOPS', false)
cdata.set('LWS_WITH_SOCKS5', false)
cdata.set('LWS_WITH_PEER_LIMITS', false)
cdata.set('LWS_WITH_ACCESS_LOG', true)
cdata.set('LWS_WITH_RANGES', false)
cdata.set('LWS_WITH_ACME', false)
cdata.set('LWS_WITH_HUBBUB', false)
cdata.set('LWS_WITH_ALSA', false)
cdata.set('LWS_WITH_GTK', false)
cdata.set('LWS_WITH_FTS', false)
cdata.set('LWS_WITH_SYS_ASYNC_DNS', false)
cdata.set('LWS_WITH_SYS_NTPCLIENT', false)
cdata.set('LWS_WITH_SYS_DHCP_CLIENT', false)
cdata.set('LWS_WITH_HTTP_BASIC_AUTH', true)
cdata.set('LWS_WITH_HTTP_UNCOMMON_HEADERS', true)
cdata.set('LWS_WITH_SYS_STATE', true)
cdata.set('LWS_WITH_SYS_FAULT_INJECTION', false)
cdata.set('LWS_WITH_SYS_METRICS', false)

cdata.set('LWS_WITH_SECURE_STREAMS', false)
cdata.set('LWS_WITH_SECURE_STREAMS_CPP', false)
cdata.set('LWS_WITH_SECURE_STREAMS_PROXY_API', false)
cdata.set('LWS_WITH_SECURE_STREAMS_SYS_AUTH_API_AMAZON_COM', false)
cdata.set('LWS_WITH_SECURE_STREAMS_STATIC_POLICY_ONLY', false)
cdata.set('LWS_WITH_SECURE_STREAMS_AUTH_SIGV4', false)
cdata.set('LWS_WITH_SECURE_STREAMS_BUFFER_DUMP', false)
cdata.set('LWS_WITH_SS_DIRECT_PROTOCOL_STR', false)

cdata.set('LWS_WITH_SYS_SMD', cdata.get('LWS_WITH_SECURE_STREAMS_PROXY_API'))
cdata.set('LWS_WITH_LWSAC', true)
cdata.set('LWS_LOGS_TIMESTAMP', true)
cdata.set('LWS_LOG_TAG_LIFECYCLE', true)
cdata.set('LWS_ROLE_RAW', true)
cdata.set('LWS_WITH_SPAWN', false)
cdata.set('LWS_WITH_ABSTRACT', false)
cdata.set('LWS_WITH_COSE', false)
cdata.set('LWS_WITH_JOSE', false)
cdata.set('LWS_WITH_DRIVERS', false)
cdata.set('LWS_WITH_FILE_OPS', true)
cdata.set('LWS_WITH_ESP32', true)
cdata.set('LWS_WITH_DIR', true)
cdata.set('LWS_WITH_LEJP_CONF', not cdata.get('LWS_WITH_ESP32'))
cdata.set('LWS_PLAT_OPTEE', false)
cdata.set('LWS_WITH_PEER_LIMITS', false)
cdata.set('LWS_WITH_CLIENT', false)
cdata.set('LWS_WITH_CACHE_NSCOOKIEJAR', true)
cdata.set('LWS_WITH_ACCESS_LOG', true)
cdata.set('LWS_WITH_UDP', true)
cdata.set('LWS_WITH_SERVER', true)
cdata.set('LWS_WITHOUT_SERVER', not cdata.get('LWS_WITH_SERVER'))
cdata.set('LWS_WITH_NETLINK', host_machine.system() == 'linux')
cdata.set('LWS_WITH_LWS_DSH', false)
cdata.set('LWS_WITH_SEQUENCER', false)
cdata.set('LWS_WITH_CONMON', false)
cdata.set('LWS_WITH_POLL', true)
cdata.set('LWS_WITHOUT_CLIENT', not cdata.get('LWS_WITH_CLIENT'))
cdata.set('LWS_ESP_PLATFORM', false)
cdata.set('LWS_NO_DAEMONIZE', host_machine.system() == 'windows')
cdata.set('LWS_WITH_DISKCACHE', host_machine.system() != 'windows')

cc = meson.get_compiler('c')
cdata.set(
  'LWS_HAS_INTPTR_T',
  cc.has_type(
    'intptr_t',
    prefix: '#include <stdint.h>',
  ),
)
cdata.set(
  'LWS_HAVE_SUSECONDS_T',
  cc.has_type(
    'suseconds_t',
    prefix: '#include <sys/types.h>',
  ),
)
cdata.set(
  'LWS_HAVE_RTA_PREF',
  cc.has_header_symbol('linux/rtnetlink.h', 'RTA_PREF'),
)
cdata.set('LWS_WITH_UNIX_SOCK', not cc.has_header('afunix.h'))

functions = [
  'atoll',
  'clock_gettime',
  'ctime_r',
  'eventfd',
  'execvpe',
  'getgrgid_r',
  'getgrnam_r',
  'getifaddrs',
  'getpwnam_r',
  'getpwuid_r',
  'gmtime_r',
  'localtime_r',
  'pipe2',
  'timegm',
  'vfork',
]

foreach f : functions
  cdata.set('LWS_HAVE_@0@'.format(f.to_upper()), cc.has_function(f))
endforeach

foreach h : ['malloc.h', 'pthread.h', 'stdint.h']
  cdata.set('LWS_HAVE_@0@'.format(h.underscorify().to_upper()), cc.has_header(h))
endforeach

cdata.set('LWS_HAS_GETOPT_LONG', cc.has_function('getopt_long'))

windows_dep = []
foreach d : ['ws2_32', 'userenv', 'psapi', 'iphlpapi', 'crypt32']
  windows_dep += cc.find_library(
    d,
    required: host_machine.system() == 'windows',
  )
endforeach

if meson.version().version_compare('>= 0.62')
  dl_dep = dependency(
    'dl',
    required: get_option('plugins'),
  )
else
  dl_dep = cc.find_library(
    'dl',
    required: get_option('plugins'),
  )
endif
cdata.set('LWS_WITH_PLUGINS', dl_dep.found())
cdata.set('LWS_WITH_PLUGINS_API', cdata.get('LWS_WITH_PLUGINS'))

zlib_dep = dependency(
  'zlib',
  required: get_option('compression'),
)
cdata.set('LWS_WITH_HTTP_STREAM_COMPRESSION', zlib_dep.found())
cdata.set('LWS_WITHOUT_EXTENSIONS', not zlib_dep.found())

brotlienc_dep = dependency(
  'libbrotlienc',
  required: get_option('brotli'),
)
brotlidec_dep = dependency(
  'libbrotlidec',
  required: get_option('brotli'),
)
brotli_dep = [brotlienc_dep, brotlidec_dep]
cdata.set(
  'LWS_WITH_HTTP_BROTLI',
  brotlienc_dep.found() and brotlidec_dep.found(),
)

glib_dep = dependency(
  'glib-2.0',
  required: get_option('glib'),
)
cdata.set(
  'LWS_WITH_GLIB',
  glib_dep.found() and host_machine.system() != 'windows',
)

uv_dep = dependency(
  'libuv',
  required: get_option('uv'),
)
cdata.set('LWS_WITH_LIBUV', uv_dep.found())

ev_dep = cc.find_library(
  'libev',
  required: get_option('ev'),
)
cdata.set('LWS_WITH_LIBEV', ev_dep.found())

event_dep = dependency(
  'libevent',
  required: get_option('event'),
)
cdata.set('LWS_WITH_LIBEVENT', event_dep.found())

cdata.set(
  'LWS_WITH_EVENT_LIBS',
  glib_dep.found() or uv_dep.found() or ev_dep.found() or event_dep.found(),
)
cdata.set(
  'LWS_WITH_EVLIB_PLUGINS',
  host_machine.system() != 'windows' and cdata.get('LWS_WITH_EVENT_LIBS'),
)

sqlite_dep = dependency(
  'sqlite3',
  required: get_option('sqlite3'),
)
cdata.set('LWS_WITH_STRUCT_SQLITE3', sqlite_dep.found())

sdevent_dep = cc.find_library(
  'libsdevent',
  required: get_option('sdevent'),
)
cdata.set('LWS_WITH_SDEVENT', sdevent_dep.found())

ubox_dep = cc.find_library(
  'libubox',
  required: get_option('ubox'),
)
cdata.set('LWS_WITH_ULOOP', ubox_dep.found())

mount_dep = dependency(
  'mount',
  required: get_option('mount'),
)
cdata.set('LWS_WITH_FSMOUNT', mount_dep.found())

dbus_dep = dependency(
  'dbus-1',
  required: get_option('dbus'),
)
cdata.set('LWS_ROLE_DBUS', dbus_dep.found())

thread_dep = dependency(
  'threads',
  required: false,
)
cdata.set(
  'LWS_WITH_THREADPOOL',
  thread_dep.found() and cc.has_header('pthread.h'),
)

cfile = configure_file(
  input: 'cmake/lws_config.h.in',
  output: 'lws_config.h',
  format: 'cmake',
  configuration: cdata,
)

privcdata = configuration_data()

privheaders = [
  'inttypes.h',
  'netinet/in.h',
  'string.h',
  'unistd.h',
  'sys/types.h',
  'strings.h',
  'sys/prctl.h',
  'stdlib.h',
  'stdint.h',
  'memory.h',
  'sys/socket.h',
  'sys/stat.h',
  'sys/resource.h',
]

foreach h : privheaders
  privcdata.set(
    'LWS_HAVE_@0@'.format(h.underscorify().to_upper()),
    cc.has_header(h),
  )
endforeach

privfunctions = [
  'fork',
  'getenv',
  'malloc',
  'strerror',
  'vfork',
  'execvpe',
  'getloadavg',
  'getifaddrs',
]

foreach f : privfunctions
  privcdata.set('LWS_HAVE_@0@'.format(f.to_upper()), cc.has_function(f))
endforeach
privcdata.set(
  'LWS_HAS_PTHREAD_SETNAME_NP',
  host_machine.system() != 'darwin' and cc.has_function('pthread_setname_np'),
)

privcdata.set(
  'LWS_HAVE_TCP_USER_TIMEOUT',
  cc.has_header_symbol('netinet/tcp.h', 'TCP_USER_TIMEOUT'),
)

privcfile = configure_file(
  input: 'cmake/lws_config_private.h.in',
  output: 'lws_config_private.h',
  format: 'cmake',
  configuration: privcdata,
)

incdirs = []
incdirs += include_directories(
  'include',
  'lib',
  'lib/core',
  'lib/event-libs',
  'lib/system/metrics',
)

sources = files(
  'lib/core/alloc.c',
  'lib/core/buflist.c',
  'lib/core/context.c',
  'lib/core/libwebsockets.c',
  'lib/core/logs.c',
  'lib/core/lws_dll2.c',
  'lib/core/lws_map.c',
  'lib/event-libs/poll/poll.c',
  'lib/misc/base64-decode.c',
  'lib/misc/cache-ttl/file.c',
  'lib/misc/ieeehalfprecision.c',
  'lib/misc/lecp.c',
  'lib/misc/lejp.c',
  'lib/misc/lws-ring.c',
  'lib/misc/lws-struct-lejp.c',
  'lib/misc/lwsac/cached-file.c',
  'lib/misc/lwsac/lwsac.c',
  'lib/misc/prng.c',
  'lib/misc/sha-1.c',
  'lib/system/system.c',
  #  'lib/secure-streams/plugins/ssp-h1url/h1url.c',
  #  'lib/tls/lws-gencrypto-common.c',
  #  'lib/tls/lws-genec-common.c',
  #  'lib/tls/mbedtls/lws-genaes.c',
  #  'lib/tls/mbedtls/lws-gencrypto.c',
  #  'lib/tls/mbedtls/lws-genec.c',
  #  'lib/tls/mbedtls/lws-genhash.c',
  #  'lib/tls/mbedtls/lws-genrsa.c',
  #  'lib/tls/mbedtls/mbedtls-client.c',
  #  'lib/tls/mbedtls/mbedtls-extensions.c',
  #  'lib/tls/mbedtls/mbedtls-server.c',
  #  'lib/tls/mbedtls/mbedtls-session.c',
  #  'lib/tls/mbedtls/mbedtls-ssl.c',
  #  'lib/tls/mbedtls/mbedtls-tls.c',
  #  'lib/tls/mbedtls/mbedtls-x509.c',
  #  'lib/tls/mbedtls/wrapper/library/ssl_cert.c',
  #  'lib/tls/mbedtls/wrapper/library/ssl_lib.c',
  #  'lib/tls/mbedtls/wrapper/library/ssl_methods.c',
  #  'lib/tls/mbedtls/wrapper/library/ssl_pkey.c',
  #  'lib/tls/mbedtls/wrapper/library/ssl_stack.c',
  #  'lib/tls/mbedtls/wrapper/library/ssl_x509.c',
  #  'lib/tls/mbedtls/wrapper/platform/ssl_pm.c',
  #  'lib/tls/mbedtls/wrapper/platform/ssl_port.c',
  #  'lib/tls/openssl/lws-genaes.c',
  #  'lib/tls/openssl/lws-gencrypto.c',
  #  'lib/tls/openssl/lws-genec.c',
  #  'lib/tls/openssl/lws-genhash.c',
  #  'lib/tls/openssl/lws-genrsa.c',
  #  'lib/tls/openssl/openssl-client.c',
  #  'lib/tls/openssl/openssl-server.c',
  #  'lib/tls/openssl/openssl-session.c',
  #  'lib/tls/openssl/openssl-ssl.c',
  #  'lib/tls/openssl/openssl-tls.c',
  #  'lib/tls/openssl/openssl-x509.c',
  #  'lib/tls/tls-client.c',
  #  'lib/tls/tls-jit-trust.c',
  #  'lib/tls/tls-network.c',
  #  'lib/tls/tls-server.c',
  #  'lib/tls/tls-sessions.c',
  #  'lib/tls/tls.c',
)

if cdata.get('LWS_WITH_DRIVERS')
  incdirs += include_directories(
    'lib/drivers',
    'lib/drivers/devices/display',
    'lib/drivers/led',
  )
  sources += files(
    'lib/drivers/button/lws-button.c',
    'lib/drivers/display/ili9341-spi.c',
    'lib/drivers/display/lws-display.c',
    'lib/drivers/display/ssd1306-i2c.c',
    'lib/drivers/i2c/bitbang/lws-bb-i2c.c',
    'lib/drivers/i2c/lws-i2c.c',
    'lib/drivers/led/led-gpio.c',
    'lib/drivers/led/led-seq.c',
    'lib/drivers/pwm/pwm.c',
    'lib/drivers/settings/settings.c',
    'lib/drivers/spi/bitbang/lws-bb-spi.c',
    'lib/drivers/spi/lws-spi.c',
  )

  if cdata.get('LWS_ESP_PLATFORM')
    sources += files(
      'lib/plat/freertos/esp32/drivers/gpio-esp32.c',
      'lib/plat/freertos/esp32/drivers/pwm-esp32.c',
    )

    if cdata.get('LWS_WITH_NETWORK')
      sources += files(
        'lib/drivers/netdev/netdev.c',
        'lib/drivers/netdev/wifi.c',
      )
    endif
  endif
endif

if cdata.get('LWS_WITH_NETWORK')
  incdirs += include_directories('lib/core-net', 'lib/misc', 'lib/roles')
  sources += files(
    'lib/core-net/adopt.c',
    'lib/core-net/close.c',
    'lib/core-net/dummy-callback.c',
    'lib/core-net/network.c',
    'lib/core-net/output.c',
    'lib/core-net/pollfd.c',
    'lib/core-net/service.c',
    'lib/core-net/sorted-usec-list.c',
    'lib/core-net/vhost.c',
    'lib/core-net/wsi-timeout.c',
    'lib/core-net/wsi.c',
    'lib/misc/cache-ttl/heap.c',
    'lib/misc/cache-ttl/lws-cache-ttl.c',
    'lib/roles/pipe/ops-pipe.c',
  )

  if cdata.get('LWS_WITH_SYS_STATE')
    sources += files('lib/core-net/state.c')
  endif

  if cdata.get('LWS_WITH_NETLINK')
    sources += files('lib/core-net/route.c')
  endif

  if cdata.get('LWS_WITH_LWS_DSH')
    sources += files('lib/core-net/lws-dsh.c')
  endif

  if cdata.get('LWS_WITH_SEQUENCER')
    sources += files('lib/core-net/sequencer.c')
  endif

  if cdata.get('LWS_WITH_CLIENT')
    sources += files(
      'lib/core-net/client/client.c',
      'lib/core-net/client/connect.c',
      'lib/core-net/client/connect2.c',
      'lib/core-net/client/connect3.c',
      'lib/core-net/client/connect4.c',
      'lib/core-net/client/sort-dns.c',
    )

    if cdata.get('LWS_WITH_CONMON')
      sources += files('lib/core-net/client/conmon.c')
    endif

    if cdata.get('LWS_WITH_SOCKS5')
      sources += files('lib/core-net/socks5-client.c')
    endif
  endif

  if cdata.get('LWS_ROLE_MQTT') and cdata.get('LWS_WITH_CLIENT')
    sources += files(
      'lib/roles/mqtt/client/client-mqtt-handshake.c',
      'lib/roles/mqtt/client/client-mqtt.c',
      'lib/roles/mqtt/mqtt.c',
      'lib/roles/mqtt/ops-mqtt.c',
      'lib/roles/mqtt/primitives.c',
    )
  endif

  if cdata.get('LWS_ROLE_DBUS')
    incdirs += include_directories('lib/roles/dbus')
    sources += files('lib/roles/dbus/dbus.c')
  endif

  if cdata.get('LWS_ROLE_H1') or cdata.get('LWS_ROLE_H2')
    incdirs += include_directories('lib/roles/http')
    sources += files(
      'lib/roles/http/date.c',
      'lib/roles/http/header.c',
      'lib/roles/http/parsers.c',
    )

    if cdata.get('LWS_WITH_SERVER')
      sources += files(
        'lib/roles/http/server/lws-spa.c',
        'lib/roles/http/server/server.c',
      )
    endif

    if cdata.get('LWS_WITH_CACHE_NSCOOKIEJAR') and cdata.get('LWS_WITH_CLIENT')
      sources += files('lib/roles/http/cookie.c')
    endif

    if cdata.get('LWS_WITH_HTTP_PROXY') and cdata.get('LWS_WITH_HUBBUB')
      sources += files('lib/roles/http/server/rewrite.c')
    endif

    if cdata.get('LWS_WITH_ACCESS_LOG')
      sources += files('lib/roles/http/server/access-log.c')
    endif

    if cdata.get('LWS_WITH_HTTP_STREAM_COMPRESSION')
      incdirs += include_directories('lib/roles/http/compression')
      sources += files(
        'lib/roles/http/compression/deflate/deflate.c',
        'lib/roles/http/compression/stream.c',
      )

      if cdata.get('LWS_WITH_HTTP_BROTLI')
        sources += files('lib/roles/http/compression/brotli/brotli.c')
      endif
    endif

    if cdata.get('LWS_WITH_LEJP_CONF') and cdata.get('LWS_WITH_NETWORK') and not cdata.get(
      'LWS_PLAT_OPTEE',
    )
      sources += files('lib/roles/http/server/lejp-conf.c')
    endif

    if cdata.get('LWS_WITH_RANGES')
      sources += files('lib/roles/http/server/ranges.c')
    endif

    if cdata.get('LWS_WITH_ZIP_FOPS') and cdata.get('LWS_WITH_ZLIB')
      sources += files('lib/roles/http/server/fops-zip.c')
    endif

    if cdata.get('LWS_WITH_CLIENT')
      sources += files('lib/roles/http/client/client-http.c')
    endif
  endif

  if cdata.get('LWS_ROLE_H1')
    incdirs += include_directories('lib/roles/h1')
    sources += files('lib/roles/h1/ops-h1.c')
  endif

  if cdata.get('LWS_ROLE_H2')
    incdirs += include_directories('lib/roles/h2')
    sources += files(
      'lib/roles/h2/hpack.c',
      'lib/roles/h2/http2.c',
      'lib/roles/h2/ops-h2.c',
    )
  endif

  if cdata.get('LWS_ROLE_WS')
    incdirs += include_directories('lib/roles/ws')
    sources += files('lib/roles/ws/ops-ws.c')

    if cdata.get('LWS_WITH_CLIENT')
      sources += files(
        'lib/roles/ws/client-parser-ws.c',
        'lib/roles/ws/client-ws.c',
      )
    endif

    if cdata.get('LWS_WITH_SERVER')
      sources += files('lib/roles/ws/server-ws.c')
    endif

    if not cdata.get('LWS_WITHOUT_EXTENSIONS')
      sources += files(
        'lib/roles/ws/ext/extension-permessage-deflate.c',
        'lib/roles/ws/ext/extension.c',
      )
    endif
  endif

  if cdata.get('LWS_ROLE_RAW')
    incdirs += include_directories('lib/roles/raw-skt')
    sources += files('lib/roles/raw-skt/ops-raw-skt.c')

    if cdata.get('LWS_WITH_ABSTRACT')
      sources += files('lib/abstract/transports/raw-skt.c')
    endif
  endif

  if cdata.get('LWS_ROLE_RAW_FILE')
    incdirs += include_directories('lib/roles/raw-file')
    sources += files('lib/roles/raw-file/ops-raw-file.c')
  endif

  if cdata.get('LWS_WITH_CGI')
    incdirs += include_directories('lib/roles/cgi')
    sources += files('lib/roles/cgi/cgi-server.c', 'lib/roles/cgi/ops-cgi.c')
  endif

  if cdata.get('LWS_ROLE_RAW_PROXY')
    incdirs += include_directories('lib/roles/raw-proxy')
    sources += files('lib/roles/raw-proxy/ops-raw-proxy.c')
  endif

  if cdata.get('LWS_WITH_SERVER') or cdata.get(
    'LWS_WITH_SECURE_STREAMS_PROCESS_API',
  )
    sources += files('lib/roles/listen/ops-listen.c')
  endif

  if cdata.get('LWS_WITH_NETLINK')
    sources += files('lib/roles/netlink/ops-netlink.c')
  endif

  if cdata.get('LWS_WITH_SYS_ASYNC_DNS')
    sources += files(
      'lib/system/async-dns/async-dns-parse.c',
      'lib/system/async-dns/async-dns.c',
    )
  endif

  if cdata.get('LWS_WITH_SYS_NTPCLIENT')
    sources += files('lib/system/ntpclient/ntpclient.c')
  endif

  if cdata.get('LWS_WITH_SYS_DHCP_CLIENT')
    sources += files(
      'lib/system/dhcpclient/dhcpc4.c',
      'lib/system/dhcpclient/dhcpclient.c',
    )
  endif

  if cdata.get('LWS_WITH_SYS_SMD')
    incdirs += include_directories('lib/system/smd')
    sources += files('lib/system/smd/smd.c')
  endif

  if cdata.get('LWS_WITH_SYS_FAULT_INJECTION')
    incdirs += include_directories('lib/system/fault-injection')
    sources += files('lib/system/fault-injection/fault-injection.c')
  endif

  if cdata.get('LWS_WITH_SYS_METRICS')
    sources += files('lib/system/metrics/metrics.c')
  endif

  if cdata.get('LWS_WITH_ABSTRACT')
    incdirs += include_directories('lib/abstract')
    sources += files(
      'lib/abstract/abstract.c',
      'lib/abstract/protocols/smtp/smtp-sequencer.c',
      'lib/abstract/protocols/smtp/smtp.c',
      'lib/abstract/test-sequencer.c',
      'lib/abstract/transports/unit-test.c',
    )
  endif
endif

if host_machine.system() == 'windows'
  incdirs += include_directories('lib/plat/windows', 'win32port/win32helpers')
  sources += files(
    'lib/plat/windows/windows-fds.c',
    'lib/plat/windows/windows-file.c',
    'lib/plat/windows/windows-init.c',
    'lib/plat/windows/windows-misc.c',
    'lib/plat/windows/windows-pipe.c',
    'lib/plat/windows/windows-plugins.c',
    'lib/plat/windows/windows-service.c',
    'lib/plat/windows/windows-sockets.c',
    'win32port/win32helpers/gettimeofday.c',
  )

  if cdata.get('LWS_WITH_SYS_ASYNC_DNS')
    sources += files('lib/plat/windows/windows-resolv.c')
  endif

  if cdata.get('LWS_WITH_SPAWN')
    sources += files('lib/plat/windows/windows-spawn.c')
  endif
else
  incdirs += include_directories('lib/plat/unix')
  sources += files(
    'lib/plat/unix/unix-caps.c',
    'lib/plat/unix/unix-init.c',
    'lib/plat/unix/unix-misc.c',
  )

  if cdata.get('LWS_WITH_FILE_OPS')
    sources += files('lib/plat/unix/unix-file.c')
  endif

  if cdata.get('LWS_WITH_NETWORK')
    sources += files(
      'lib/plat/unix/unix-fds.c',
      'lib/plat/unix/unix-pipe.c',
      'lib/plat/unix/unix-service.c',
      'lib/plat/unix/unix-sockets.c',
    )

    if cdata.get('LWS_WITH_SYS_ASYNC_DNS')
      sources += files('lib/plat/unix/unix-resolv.c')
    endif
  endif

  if cdata.get('LWS_WITH_PLUGINS_API')
    sources += files('lib/plat/unix/unix-plugins.c')
  endif

  if cdata.get('LWS_WITH_SPAWN')
    sources += files('lib/plat/unix/unix-spawn.c')
  endif
endif

if cdata.get('LWS_WITH_FILE_OPS')
  sources += files('lib/core/vfs.c')
endif

if cdata.get('LWS_WITH_FTS')
  sources += files('lib/misc/fts/trie-fd.c', 'lib/misc/fts/trie.c')
endif

if cdata.get('LWS_WITH_SECURE_STREAMS')
  if cdata.get('LWS_WITH_CLIENT')
    incdirs += include_directories('lib/secure-streams')
    sources += files(
      'lib/secure-streams/policy-common.c',
      'lib/secure-streams/protocols/ss-raw.c',
      'lib/secure-streams/secure-streams.c',
      'lib/secure-streams/system/captive-portal-detect/captive-portal-detect.c',
    )

    if not cdata.get('LWS_WITH_SECURE_STREAMS_STATIC_POLICY_ONLY')
      sources += files(
        'lib/secure-streams/policy-json.c',
        'lib/secure-streams/system/fetch-policy/fetch-policy.c',
      )
    endif

    if cdata.get('LWS_ROLE_H1')
      sources += files('lib/secure-streams/protocols/ss-h1.c')
    endif

    if cdata.get('LWS_ROLE_H2')
      sources += files('lib/secure-streams/protocols/ss-h2.c')
    endif

    if cdata.get('LWS_ROLE_WS')
      sources += files('lib/secure-streams/protocols/ss-ws.c')
    endif

    if cdata.get('LWS_ROLE_MQTT')
      sources += files('lib/secure-streams/protocols/ss-mqtt.c')
    endif

    if cdata.get('LWS_WITH_SECURE_STREAMS_PROXY_API')
      sources += files(
        'lib/secure-streams/secure-streams-client.c',
        'lib/secure-streams/secure-streams-process.c',
        'lib/secure-streams/secure-streams-serialize.c',
      )
    endif

    if cdata.get('LWS_WITH_SECURE_STREAMS_SYS_AUTH_API_AMAZON_COM') and cdata.get(
      'LWS_WITH_SYS_STATE',
    )
      sources += files('lib/secure-streams/system/auth-api.amazon.com/auth.c')
    endif

    if cdata.get('LWS_WITH_SECURE_STREAMS_AUTH_SIGV4')
      sources += files('lib/secure-streams/system/auth-sigv4/sign.c')
    endif
  endif
endif

if cdata.get('LWS_WITH_COSE')
  incdirs += include_directories('lib/cose')
  sources += files(
    'lib/cose/cose_key.c',
    'lib/cose/cose_sign.c',
    'lib/cose/cose_sign_alg.c',
    'lib/cose/cose_validate.c',
    'lib/cose/cose_validate_alg.c',
  )
endif

if cdata.get('LWS_WITH_JOSE')
  incdirs += include_directories('lib/jose')
  sources += files(
    'lib/jose/jwe/enc/aescbc.c',
    'lib/jose/jwe/enc/aesgcm.c',
    'lib/jose/jwe/enc/aeskw.c',
    'lib/jose/jwe/jwe-ecdh-es-aeskw.c',
    'lib/jose/jwe/jwe-rsa-aescbc.c',
    'lib/jose/jwe/jwe-rsa-aesgcm.c',
    'lib/jose/jwe/jwe.c',
    'lib/jose/jwk/jose_key.c',
    'lib/jose/jwk/jwk.c',
    'lib/jose/jws/jose.c',
    'lib/jose/jws/jws.c',
  )
endif

if cdata.get('LWS_WITH_GLIB')
  sources += files('lib/event-libs/glib/glib.c')
endif

if cdata.get('LWS_WITH_LIBUV')
  sources += files('lib/event-libs/libuv/libuv.c')
endif

if cdata.get('LWS_WITH_LIBEV')
  sources += files('lib/event-libs/libev/libev.c')
endif

if cdata.get('LWS_WITH_LIBEVENT')
  sources += files('lib/event-libs/libevent/libevent.c')
endif

if cdata.get('LWS_WITH_STRUCT_SQLITE3')
  sources += files('lib/misc/lws-struct-sqlite.c')
endif

if cdata.get('LWS_WITH_SDEVENT')
  sources += files('lib/event-libs/sdevent/sdevent.c')
endif

if cdata.get('LWS_WITH_ULOOP')
  sources += files('lib/event-libs/uloop/uloop.c')
endif

if cdata.get('LWS_WITH_DIR')
  sources += files('lib/misc/dir.c')
endif

if cdata.get('LWS_WITH_FSMOUNT')
  sources += files('lib/misc/fsmount.c')
endif

if cdata.get('LWS_WITH_PEER_LIMITS')
  sources += files('lib/misc/peer-limits.c')
endif

if not cdata.get('LWS_HAVE_GETIFADDRS') and host_machine.system() != 'windows'
  sources += files('lib/misc/getifaddrs.c')
endif

if cdata.get('LWS_WITH_THREADPOOL')
  sources += files('lib/misc/threadpool/threadpool.c')
endif

if cdata.get('LWS_WITH_DISKCACHE')
  sources += files('lib/misc/diskcache.c')
endif

if not cdata.get('LWS_NO_DAEMONIZE') and host_machine.system() != 'windows'
  sources += files('lib/misc/daemonize.c')
endif

libwebsockets = library(
  'websockets',
  sources,
  include_directories: incdirs,
  dependencies: [
    brotli_dep,
    zlib_dep,
    event_dep,
    ev_dep,
    uv_dep,
    glib_dep,
    mount_dep,
    sqlite_dep,
    dbus_dep,
    thread_dep,
    dl_dep,
    windows_dep,
  ],
)

depinc = include_directories('include')
libwebsockets_dep = declare_dependency(
  include_directories: depinc,
  link_with: libwebsockets,
)
