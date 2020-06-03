project('libwebsockets', 'c', version: '4.0.13', license: 'MIT')

lws_library_version = meson.project_version()
lws_library_version_major  = '4'
lws_library_version_minor  = '0'
lws_library_version_patch  = '13'
lws_library_version_number = 16

lws_incdirs = [ ]
lws_dependencies = [ ]
lws_c_args = []


# ToDo: detect platform properly
esp_platform = false
ios = false
apple = false
mingw = false
win32 = build_machine.system() == 'win32'
unix  = build_machine.system() == 'linux'

# Initialize
lws_max_smp = ''
lws_with_abstract = false
lws_build_hash = ''
lws_builtin_getifaddrs = false
lws_detected_plat_ios = false
lws_no_client = false
lws_plat_unix = false
lws_with_polarssl = false
lws_with_smtp = false
lws_with_stateful_urldecode = false
use_old_cyassl = false
use_wolfssl = false

lws_with_bundled_zlib_default = false
if win32
    lws_with_bundled_zlib_default = true
endif

lws_role_raw = true
lws_with_poll = true

# Select features recommended for PC distro packaging
lws_with_distro_recommended = get_option('LWS_WITH_DISTRO_RECOMMENDED')
lws_for_gitohashi = get_option('LWS_FOR_GITOHASHI')

# Major individual features
lws_with_network = get_option('LWS_WITH_NETWORK')
lws_role_h1 = get_option('LWS_ROLE_H1')
lws_role_ws = get_option('LWS_ROLE_WS')
lws_role_mqtt = get_option('LWS_ROLE_MQTT')
lws_role_dbus = get_option('LWS_ROLE_DBUS')
lws_role_raw_proxy = get_option('LWS_ROLE_RAW_PROXY')
 
lws_role_raw_file = get_option('LWS_ROLE_RAW_FILE')
lws_with_http2 = get_option('LWS_WITH_HTTP2')
lws_with_lwsws = get_option('LWS_WITH_LWSWS')
lws_with_cgi = get_option('LWS_WITH_CGI')
lws_ipv6 = get_option('LWS_IPV6')
lws_unix_sock = get_option('LWS_UNIX_SOCK')
lws_with_plugins = get_option('LWS_WITH_PLUGINS')
lws_with_http_proxy = get_option('LWS_WITH_HTTP_PROXY')
lws_with_zip_fops = get_option('LWS_WITH_ZIP_FOPS')
lws_with_socks5 = get_option('LWS_WITH_SOCKS5')
lws_with_generic_sessions = get_option('LWS_WITH_GENERIC_SESSIONS')
lws_with_peer_limits = get_option('LWS_WITH_PEER_LIMITS')
lws_with_access_log = get_option('LWS_WITH_ACCESS_LOG')
lws_with_ranges = get_option('LWS_WITH_RANGES')
lws_with_server_status = get_option('LWS_WITH_SERVER_STATUS')
lws_with_threadpool = get_option('LWS_WITH_THREADPOOL')
lws_with_http_stream_compression = get_option('LWS_WITH_HTTP_STREAM_COMPRESSION')
lws_with_http_brotli = get_option('LWS_WITH_HTTP_BROTLI')
lws_with_acme = get_option('LWS_WITH_ACME')
lws_with_hubbub = get_option('LWS_WITH_HUBBUB')
lws_with_alsa = get_option('LWS_WITH_ALSA')
lws_with_gtk = get_option('LWS_WITH_GTK')
lws_with_fts = get_option('LWS_WITH_FTS')
lws_with_sys_async_dns = get_option('LWS_WITH_SYS_ASYNC_DNS')
lws_with_sys_ntpclient = get_option('LWS_WITH_SYS_NTPCLIENT')
lws_with_sys_dhcp_client = get_option('LWS_WITH_SYS_DHCP_CLIENT')
 
lws_with_http_basic_auth = get_option('LWS_WITH_HTTP_BASIC_AUTH')
lws_with_http_uncommon_headers = get_option('LWS_WITH_HTTP_UNCOMMON_HEADERS')

# Secure Streams
lws_with_secure_streams = get_option('LWS_WITH_SECURE_STREAMS')
lws_with_secure_streams_proxy_api = get_option('LWS_WITH_SECURE_STREAMS_PROXY_API')
lws_with_secure_streams_sys_auth_api_amazon_com = get_option('LWS_WITH_SECURE_STREAMS_SYS_AUTH_API_AMAZON_COM')
 
# TLS library
lws_with_ssl = get_option('LWS_WITH_SSL')
lws_with_mbedtls = get_option('LWS_WITH_MBEDTLS')
lws_with_boringssl = get_option('LWS_WITH_BORINGSSL')
lws_with_cyassl = get_option('LWS_WITH_CYASSL')
lws_with_wolfssl = get_option('LWS_WITH_WOLFSSL')
lws_ssl_client_use_os_ca_certs = get_option('LWS_SSL_CLIENT_USE_OS_CA_CERTS')
 
# Event library options
lws_with_libev = get_option('LWS_WITH_LIBEV')
lws_with_libuv = get_option('LWS_WITH_LIBUV')
lws_with_libevent = get_option('LWS_WITH_LIBEVENT')
lws_with_glib = get_option('LWS_WITH_GLIB')

# Static / Dynamic build options
lws_with_static = get_option('LWS_WITH_STATIC')
lws_with_shared = get_option('LWS_WITH_SHARED')
lws_link_testapps_dynamic = get_option('LWS_LINK_TESTAPPS_DYNAMIC')
lws_static_pic = get_option('LWS_STATIC_PIC')

# Specific platforms
lws_with_esp32 = get_option('LWS_WITH_ESP32')
lws_with_esp32_helper = get_option('LWS_WITH_ESP32_HELPER')
lws_plat_optee = get_option('LWS_PLAT_OPTEE')
lws_plat_freertos = get_option('LWS_PLAT_FREERTOS')
lws_plat_android = get_option('LWS_PLAT_ANDROID')
 
# Client / Server / Test Apps build control
lws_without_client = get_option('LWS_WITHOUT_CLIENT')
lws_without_server = get_option('LWS_WITHOUT_SERVER')
lws_without_testapps = get_option('LWS_WITHOUT_TESTAPPS')
lws_without_test_server = get_option('LWS_WITHOUT_TEST_SERVER')
lws_without_test_server_extpoll = get_option('LWS_WITHOUT_TEST_SERVER_EXTPOLL')
lws_without_test_ping = get_option('LWS_WITHOUT_TEST_PING')
lws_without_test_client = get_option('LWS_WITHOUT_TEST_CLIENT')
 
# Extensions
lws_without_extensions = get_option('LWS_WITHOUT_EXTENSIONS')

# Helpers + misc
lws_without_builtin_getifaddrs = get_option('LWS_WITHOUT_BUILTIN_GETIFADDRS')
lws_fallback_gethostbyname = get_option('LWS_FALLBACK_GETHOSTBYNAME')
lws_without_builtin_sha1 = get_option('LWS_WITHOUT_BUILTIN_SHA1')
lws_without_daemonize = get_option('LWS_WITHOUT_DAEMONIZE')
lws_ssl_server_with_ecdh_cert = get_option('LWS_SSL_SERVER_WITH_ECDH_CERT')
lws_with_lejp = get_option('LWS_WITH_LEJP')
lws_with_sqlite3 = get_option('LWS_WITH_SQLITE3')
lws_with_struct_json = get_option('LWS_WITH_STRUCT_JSON')
lws_with_struct_sqlite3 = get_option('LWS_WITH_STRUCT_SQLITE3')
lws_with_dir = get_option('LWS_WITH_DIR')
lws_with_lejp_conf = get_option('LWS_WITH_LEJP_CONF')
lws_with_no_logs = get_option('LWS_WITH_NO_LOGS')
lws_logging_bitfield_set = get_option('LWS_LOGGING_BITFIELD_SET')
lws_logging_bitfield_clear = get_option('LWS_LOGGING_BITFIELD_CLEAR')
lws_logs_timestamp = get_option('LWS_LOGS_TIMESTAMP')
lws_avoid_sigpipe_ign = get_option('LWS_AVOID_SIGPIPE_IGN')
lws_with_stats = get_option('LWS_WITH_STATS')
lws_with_jose = get_option('LWS_WITH_JOSE')
lws_with_gencrypto = get_option('LWS_WITH_GENCRYPTO')
lws_with_selftests = get_option('LWS_WITH_SELFTESTS')
lws_with_gcov = get_option('LWS_WITH_GCOV')
lws_with_export_lwstargets = get_option('LWS_WITH_EXPORT_LWSTARGETS')
lws_reproducible = get_option('LWS_REPRODUCIBLE')
lws_with_minimal_examples = get_option('LWS_WITH_MINIMAL_EXAMPLES')
lws_with_lwsac = get_option('LWS_WITH_LWSAC')
lws_with_custom_headers = get_option('LWS_WITH_CUSTOM_HEADERS')
lws_with_diskcache = get_option('LWS_WITH_DISKCACHE')
lws_with_asan = get_option('LWS_WITH_ASAN')
lws_with_dir = get_option('LWS_WITH_DIR')
lws_with_lejp_conf = get_option('LWS_WITH_LEJP_CONF')
lws_with_zlib = get_option('LWS_WITH_ZLIB')
lws_with_bundled_zlib = get_option('LWS_WITH_BUNDLED_ZLIB')
lws_with_miniz = get_option('LWS_WITH_MINIZ')
lws_with_deprecated_lws_dll = get_option('LWS_WITH_DEPRECATED_LWS_DLL')
lws_with_sequencer = get_option('LWS_WITH_SEQUENCER')
lws_with_external_poll = get_option('LWS_WITH_EXTERNAL_POLL')
lws_with_lws_dsh = get_option('LWS_WITH_LWS_DSH')
lws_client_http_proxying = get_option('LWS_CLIENT_HTTP_PROXYING')
lws_with_file_ops = get_option('LWS_WITH_FILE_OPS')
lws_with_detailed_latency = get_option('LWS_WITH_DETAILED_LATENCY')
lws_with_udp = get_option('LWS_WITH_UDP')
lws_with_spawn = get_option('LWS_WITH_SPAWN')
lws_with_fsmount = get_option('LWS_WITH_FSMOUNT')

#
# to use miniz, enable both LWS_WITH_ZLIB and LWS_WITH_MINIZ
#
# End of user settings
#

if ios
    lws_detect_plat_ios = true
endif

if esp_platform
    message('ESP-IDF enabled')
    lws_with_esp32 = true
else
    lws_with_esp32_helper = false
endif

if lws_with_esp32
    lws_plat_freertos = true
endif

if lws_plat_freertos or lws_plat_optee
    lws_with_udp = false
endif

if win32 or lws_plat_freertos
    message('no LWS_WITH_DIR or LWS_WITH_LEJP_CONF')
    lws_with_dir = false
    lws_with_lejp_conf = false
    message('lws_with_dir ${lws_with_dir}')
else
    message('compiled with lws_with_dir and lws_with_lejp_conf')
    lws_with_dir = true
    lws_with_lejp_conf = true
endif

if lws_for_gitohashi
    lws_with_threadpool = true
    lws_with_http2 = true
    lws_with_sock = true
    lws_with_http_proxy = true
    lws_with_fts = true
    lws_with_diskcache = true
    lws_with_lwsac = true
    lws_with_lejp_conf = true
    lws_with_spawn = true
    lws_with_fsmount = true
    lws_with_struct_json = true
    lws_with_struct_sqlite3 = true
endif

if lws_with_distro_recommended
    lws_with_http2 = true
    lws_with_lwsws = true
    lws_with_cgi = true
    lws_ipv6 = true
    lws_with_zip_fops = true
    lws_with_socks5 = true
    lws_with_ranges = true
    lws_with_acme = true
    lws_with_server_status = true
    lws_with_glib = true
    lws_with_libuv = true
    lws_with_libev = true
    # livev + livevent cannot coexist at build-time
    lws_with_libevent = false
    lws_without_extensions = false
    lws_role_dbus = true
    lws_with_fts = true
    lws_with_threadpool = true
    lws_unix_sock = true
    lws_with_http_proxy = true
    lws_with_diskcache = true
    lws_with_lwsac = true
    lws_with_lejp_conf = true
    lws_with_plugins = true
    lws_role_raw_proxy = true
    lws_with_gencrypto = true
    lws_with_jose = true
    lws_with_struct_json = true
    lws_with_struct_sqlite3 = true
    lws_with_spawn = true
    lws_with_fsmount = true
    lws_role_mqtt = true
endif

if lws_with_secure_streams_proxy_api
    lws_with_lws_dsh = true
    lws_with_unix_sock = true
endif

if not lws_with_network
    lws_role_mqtt = false
    lws_role_h1 = false
    lws_role_ws = false
    lws_role_raw = false
    lws_without_extensions = true
    lws_without_server = true
    lws_without_client = true
    lws_with_http2 = false
    lws_with_socks5 = false
    lws_unix_sock = false
    lws_with_http_proxy = false
    lws_with_plugins = false
    lws_with_lwsws = false
    lws_with_cgi = false
    lws_role_raw_proxy = false
    lws_role_peer_limits = false
    lws_with_peer_limits = false
    lws_with_generic_sessions = false
    lws_with_http_stream_compression = false
    lws_with_http_brotli = false
    lws_with_poll = false
    lws_with_sequencer = false
    lws_role_dbus = false
    lws_with_lws_dsh = false
    lws_with_threadpool = false
endif

if lws_with_cgi
    lws_with_spawn = true
endif

if lws_with_struct_sqlite3
    lws_with_sqlite3 = true
endif

if apple
    lws_role_dbus = false
endif

# microsoft... that's why you can't have nice things

if win32 or lws_plat_freertos
    lws_unix_sock = false
endif

if lws_plat_freertos
    lws_with_lwsac = false
    lws_with_fts = false
endif

if win32
    win32_version_data = configuration_data()
    win32_version_data.set('LWS_LIBRARY_VERSION_MAJOR', lws_library_version_major)
    win32_version_data.set('LWS_LIBRARY_VERSION_MINOR', lws_library_version_minor)
    win32_version_data.set('LWS_LIBRARY_VERSION_PATCH', lws_library_version_patch)
    win32_version_data.set('LWS_LIBRARY_PACKAGE', 'libwebsockets')
    configure_file(input: 'win32port/version.rc.in',
        output: 'win32port/version.rc',
        configuration: conf_data,
        format: 'cmake')
endif

# translate old functionality enables to set up ROLE enables so nothing changes
if lws_with_http2 and lws_without_server
    lew_with_http2 = false
    message('HTTP2 disabled due to LWS_WITHOUT_SERVER')
endif

lws_role_h2 = lws_with_http2

lws_role_cgi = false
if lws_with_cgi
    lws_role_cgi = true
endif

if not lws_role_ws
    lws_without_extensions = true
endif

if lws_with_mbedtls
    lws_incdirs += [ 'lib/tls/mbedtls/wrapper/include' ]
endif

lws_incdirs += [
    'include',
    'plugins',
    'lib/core',
    'lib/core-net',
    'lib/event-libs',
    'lib/tls',
    'lib/roles',
    'lib/event-libs/libuv',
    'lib/event-libs/poll',
    'lib/event-libs/libevent',
    'lib/event-libs/glib',
    'lib/event-libs/libev',
    'lib/jose/jwe',
    'lib/jose/jws',
    'lib/jose',
    'lib/misc',
    'lib/roles/http',
    'lib/roles/http/compression',
    'lib/roles/h1',
    'lib/roles/h2',
    'lib/roles/ws',
    'lib/roles/cgi',
    'lib/roles/dbus',
    'lib/roles/raw-proxy',
    'lib/abstract',
    'lib/system/async-dns',
    'lib/roles/mqtt']

if lws_with_secure_streams
    lws_with_secure_streams_sys_auth_api_amazon_com = true
endif

if lws_plat_freertos
    lws_incdirs += ['lib/plat/freertos', 'lib/plat/freertos/esp32']
else
    if win32
        lws_incdirs += ['lib/plat/windows']
    else
        if lws_plat_optee
            lws_incdirs += ['lib/plat/optee']
        else
            lws_incdirs += ['lib/plat/unix']
        endif
    endif
endif

if lws_with_lwsws
    message('LWS_WITH_LWSWS --> Enabling LWS_WITH_PLUGINS and LWS_WITH_LIBUV')
    lws_with_plugins = true
    lws_with_libuv = true
    lws_with_access_log = true
    lws_with_server_status = true
    lws_with_lejp = true
    lws_with_lejp_conf = true
    lws_with_peer_limits = true
    LWS_ROLE_RAW_PROXY = true
endif

# sshd plugin
if lws_with_plugins
    lws_with_gencrypto = true
endif

if lws_role_raw_proxy
    lws_with_client = true
    lws_with_server = true
endif

if lws_with_acme
    lws_with_client = true
    lws_with_server = true
    lws_with_jose = true
endif

if lws_with_jose
    lws_with_lejp = true
    lws_with_gencrypto = true
endif

if lws_with_plugins and not lws_with_libuv
    message('LWS_WITH_PLUGINS --> Enabling LWS_WITH_LIBUV')
    lws_with_libuv = true
endif

if lws_with_plugins or lws_with_cgi
    # sshd plugin
    lws_with_gencrypto = true
endif

if lws_plat_freertos
    lws_with_shared = false
    lws_with_mbedtls = true
    # lws_without_client = true
    lws_without_testapps = true
    lws_without_extensions = true
    lws_with_plugins = false
    lws_with_ranges = true
    # this implies no pthread in the lib
    lws_max_smp = 1
    lws_have_malloc = true
    lws_have_realloc = true
    lws_have_getifaddrs = true
    lws_with_custom_headers = false
endif

if lws_with_esp32
    lws_with_zip_fops = true
endif

if win32
    lws_max_smp = 1
    lws_with_threadpool = true
endif

if lws_without_server
    lws_with_lwsws = false
endif

if lws_with_lejp_conf
    lws_with_dir = true
endif

# confirm H1 relationships

if not lws_role_h1 and lws_role_h2
    error('H2 requires LWS_ROLE_H1')
endif

if not lws_role_h1 and lws_role_ws
    error('WS required LWS_ROLE_H1')
endif

if not lws_role_h1 and lws_role_cgi
    error('CGI required LWS_ROLE_H1')
endif

# confirm HTTP relationships

if not lws_role_h1 and not lws_role_h2 and lws_with_lwsws
    error('LWS_WITH_LWSWS required LWS_ROLE_H1')
endif

if not lws_role_h1 and not lws_role_h2 and lws_with_http_proxy
    error('LWS_WITH_HTTP_PROXY required LWS_ROLE_H1')
endif

if not lws_role_h1 and not lws_role_h2 and lws_with_ranges
    error('LWS_WITH_RANGES requires LWS_ROLE_H1')
endif

if not lws_role_h1 and not lws_role_h2 and lws_with_access_log
    error('LWS_WITH_ACCESS_LOG requires LWS_ROLE_H1')
endif

if lws_with_http_proxy and (lws_without_client or lws_without_server)
    message('You have to enable both client and server for http proxy')
    lws_with_http_proxy = false
endif

# skip override of installation directories

# Alllow the user to override installation directories
#set(LWS_INSTALL_LIB_DIR       lib CACHE PATH "Installation directory for libraries")
#set(LWS_INSTALL_BIN_DIR       bin CACHE PATH "Installation directory for executables")
#set(LWS_INSTALL_INCLUDE_DIR   include CACHE PATH "Installation directory for header files")
#set(LWS_INSTALL_EXAMPLES_DIR  bin CACHE PATH "Installation directory for example files")

# Allow the user to user the old CyaSSL options/library in stead of wolfSSL
if lws_with_cyassl and lws_with_wolfssl
    error('LWS_WITH_CYASSL and LWS_WITH_WOLFSSL are mutually exclusive!')
endif

if lws_with_cyassl
    # Copy CyaSSL options to the wolfSSL options
    lws_with_wolfssl = lws_with_cyassl
    # dependencies are handled below
endif

if not (lws_with_static or lws_with_shared)
    error('Makes no sense to compile with neither static or shared libraries.')
endif

if not lws_without_extensions or lws_with_zip_fops
    lws_with_zlib = true
endif

if lws_with_http_stream_compression
    lws_with_zlib = true
endif


# if you gave LWS_WITH_MINIZ, point to MINIZ here if not found
# automatically

zlib_dep = dependency('zlib', required: false)
lws_dependencies += [zlib_dep]
lws_with_zlib = zlib_dep.found()

if lws_with_ssl
    openssl_dep = dependency('openssl', required: false)
    lws_dependencies += [openssl_dep]
    lws_with_ssl = openssl_dep.found()
endif


if lws_with_wolfssl
    if lws_with_cyassl
        wolfssl_dep = dependency('cyassl', required: false)
        lws_with_wolfssl = wolfssl_dep.found()
    else
        wolfssl_dep = dependency('wolfssl', required: false)
        lws_with_wolfssl = wolfssl_dep.found()
    endif

    lws_dependencies += [wolfssl_dep]
endif

if lws_with_libev
    libev_dep = dependency('libev', required: false)
    lws_dependencies += [libev_dep]
    lws_with_libev = libev_dep.found()
endif

if lws_with_libuv
    libuv_dep = dependency('libuv', required: false)
    lws_dependencies += [libuv_dep]
    lws_with_libuv = libuv_dep.found()
endif

if lws_with_sqlite3
    sqlite3_dep = dependency('sqlite3', required: false)
    lws_dependencies += [sqlite3_dep]
    lws_with_sqlite3 = sqlite3_dep.found()
endif

if lws_with_libevent
    libevent_dep = dependency('libevent', required: false)
    lws_dependencies += [libevent_dep]
    lws_with_libevent = libevent_dep.found()
endif

if lws_with_glib
    glib_dep = dependency('glib', required: false)
    lws_with_glib = glib_dep.found()
    if glib_dep.found()
        lws_dependencies += [glib_dep]
    endif
endif

if lws_with_fsmount
    libmount_dep = dependency('libmount', required: false)
    lws_with_fsmount = libmount_dep.found()
    if libmount_dep.found()
        lws_dependencies += [libmount_dep]
    endif
endif


if not lws_with_ssl
    lws_without_builtin_sha1 = false
endif

if lws_with_boringssl
    # boringssl deprecated EVP_PKEY
    lws_with_genhash = false
endif

# base dir where the test-apps look for SSL certs.
lws_openssl_client_certs = '../share'
if win32
    lws_openssl_client_certs = '.'
    if lws_unix_sock
        lws_unix_sock = false
        warning('Windows does not support UNIX domain sockets')
    endif
else
    lws_openssl_client_certs = '/etc/pki/tls/certs'
endif

# LWS_OPENSSL_SUPPORT deprecated... use LWS_WITH_TLS
if lws_with_ssl or lws_with_mbedtls
    lws_openssl_support = true
    lws_with_tls = true
endif

if lws_without_daemonize or win32
    lws_no_daemonize = true
endif

lws_with_ipv6 = lws_ipv6
lws_with_unix_sock = lws_unix_sock

if '' == lws_max_smp
    lws_max_smp = 1
endif

lws_with_client = not lws_without_client
lws_with_server = not lws_without_server

lws_mingw_support = mingw

lws_sha1_use_openssl_name = lws_without_builtin_sha1


# checking compiler features

c_compiler = meson.get_compiler('c')

lws_have_malloc_trim = c_compiler.compiles('''
    #include <malloc.h>
	int main(int argc, char **argv) { return malloc_trim(0); }
	''')

lws_have_malloc_usable_size = c_compiler.compiles('''
	#include <malloc.h>
	int main(int argc, char **argv) { return (int)malloc_usable_size((void *)0); }
	''')


lws_have_fork = c_compiler.has_function('fork')
lws_have_getenv = c_compiler.has_function('getenv')
lws_have_malloc = c_compiler.has_function('malloc')
lws_have_memset = c_compiler.has_function('memset')
lws_have_realloc = c_compiler.has_function('realloc')
lws_have_socket = c_compiler.has_function('(socket')
lws_have_strerror = c_compiler.has_function('strerror')
lws_have_vfork = c_compiler.has_function('vfork')
lws_have_execvpe = c_compiler.has_function('(execvpe')
lws_have_getifaddrs = c_compiler.has_function('getifaddrs')
lws_have_snprintf = c_compiler.has_function('snprintf')
lws_have__snprintf = c_compiler.has_function('_snprintf')
lws_have__vsnprintf = c_compiler.has_function('_vsnprintf')
lws_have_getloadavg = c_compiler.has_function('(getloadavg')
lws_have_atoll = c_compiler.has_function('(atoll')
lws_have__atoi64 = c_compiler.has_function('_atoi64')
lws_have__stat32i64 = c_compiler.has_function('_stat32i64')
lws_have_clock_gettime = c_compiler.has_function('clock_gettime')
lws_have_eventfd = c_compiler.has_function('eventfd')

if not lws_have_getifaddrs
	if lws_without_builtin_getifaddrs
		error('No getifaddrs was found on the system. Turn off the LWS_WITHOUT_BUILTIN_GETIFADDRS compile option to use the supplied BSD version.')
	endif
	lws_builtin_getifaddrs = true
endif

lws_have_dlfcn_h = c_compiler.has_header('dlfcn.h')
lws_have_fcntl_h = c_compiler.has_header('fcntl.h')
lws_have_in6addr_h = c_compiler.has_header('in6addr.h')
lws_have_memory_h = c_compiler.has_header('memory.h')
lws_have_netinet_in_h = c_compiler.has_header('netinet/in.h')
lws_have_stdint_h = c_compiler.has_header('stdint.h')
lws_have_stdlib_h = c_compiler.has_header('stdlib.h')
lws_have_strings_h = c_compiler.has_header('strings.h')
lws_have_string_h = c_compiler.has_header('string.h')
lws_have_sys_prctl_h = c_compiler.has_header('sys/prctl.h')
lws_have_sys_socket_h = c_compiler.has_header('sys/socket.h')
lws_have_sys_sockio_h = c_compiler.has_header('sys/sockio.h')
lws_have_sys_stat_h = c_compiler.has_header('sys/stat.h')
lws_have_sys_types_h = c_compiler.has_header('sys/types.h')
lws_have_unistd_h = c_compiler.has_header('unistd.h')
lws_have_vfork_h = c_compiler.has_header('vfork.h')
lws_have_sys_capability_h = c_compiler.has_header('sys/capability.h')
lws_have_malloc_h = c_compiler.has_header('malloc.h')
lws_have_pthread_h = c_compiler.has_header('pthread.h')
lws_have_inttypes_h = c_compiler.has_header('inttypes.h')

lws_libcap = c_compiler.find_library('cap', required: false)
lws_dependencies += [lws_libcap]
lws_have_libcap = lws_libcap.found()

lws_have_uv_version_h = false
lws_have_new_uv_version_h = false
if lws_with_libuv
    lws_have_uv_version_h = c_compiler.has_header('uv-version.h', dependencies: [libuv_dep])
    # libuv changed the location in 1.21.0. Retain both
    # checks temporarily to ensure a smooth transition.
    if (not lws_have_uv_version_h)
        lws_have_new_uv_version_h = CHECK_INCLUDE_FILE('uv/version.h', dependencies: [libuv_dep])
    endif
endif

lws_have_evbackend_linuxaio = false
lws_have_evbackend_iouring = false
if lws_with_libev
	lws_have_evbackend_linuxaio = c_compiler.compiles('''
        #include <ev.h>
        int main(int argc, char **argv) { return EVBACKEND_LINUXAIO; }
        ''', dependencies: [libev_dep])

	lws_have_evbackend_iouring = c_compiler.compiles('''(
        #include <ev.h>
	    int main(int argc, char **argv) { return EVBACKEND_IOURING; }
        ''', dependencies: [libev_dep])
endif

if lws_with_zlib and not lws_with_bundled_zlib
    if lws_with_miniz
        lws_have_zlib_h = c_compiler.has_header('miniz.h')
    else
        lws_have_zlib_h = c_compiler.has_header('zlib.h')
    endif
endif

# TODO: These can also be tested to see whether they actually work...
lws_have_working_fork = lws_have_fork
lws_have_working_vfork = lws_have_vfork

lws_has_intptr_t = c_compiler.compiles('''
    #include <stdint.h>
    int main(void) {
        intptr_t test = 1;
        return 0;
    }''')

lws_has_pthread_setname_np = false
if lws_have_pthread_h
    lws_has_pthread_setname_np = c_compiler.compiles('''
        #define _GNU_SOURCE
		#include <pthread.h>
		int main(void) {
			pthread_t th = 0;
			pthread_setname_np(th, NULL);
			return 0;
        }''')
endif

lws_has_getopt_long = c_compiler.compiles('''
    #include <stddef.h>
	#include <getopt.h>
	int main(void) {
		void *p = (void *)getopt_long;
		return p != NULL;
	}''')

varia = ''

lws_have_openssl_ecdh_h = c_compiler.has_header('openssl/ecdh.h', dependencies: [openssl_dep])


lws_have_ssl_ctx_set1_param = c_compiler.has_function(varia + 'SSL_CTX_set1_param', dependencies: [openssl_dep])
lws_have_ssl_set_info_callback = c_compiler.has_function(varia + 'SSL_set_info_callback', dependencies: [openssl_dep])
lws_have_x509_verify_param_set1_host = c_compiler.has_function(varia + 'X509_VERIFY_PARAM_set1_host', dependencies: [openssl_dep])
lws_have_rsa_set0_key = c_compiler.has_function(varia + 'RSA_set0_key', dependencies: [openssl_dep])
lws_have_x509_get_key_usage = c_compiler.has_function(varia + 'X509_get_key_usage', dependencies: [openssl_dep])
lws_have_ssl_ctx_evp_pkey_new_raw_private_key = c_compiler.has_function(varia + 'EVP_PKEY_new_raw_private_key', dependencies: [openssl_dep])
lws_have_ssl_ctx_get0_certificate = c_compiler.has_function(varia + 'SSL_CTX_get0_certificate', dependencies: [openssl_dep])
lws_have_ssl_get0_alpn_selected = c_compiler.has_function(varia + 'SSL_get0_alpn_selected', dependencies: [openssl_dep])
lws_have_ssl_set_alpn_protos = c_compiler.has_function(varia + 'SSL_set_alpn_protos', dependencies: [openssl_dep])
lws_have_evp_aes_128_cfb8 = c_compiler.has_function(varia + 'EVP_aes_128_cfb8', dependencies: [openssl_dep])
lws_have_evp_aes_128_cfb128 = c_compiler.has_function(varia + 'EVP_aes_128_cfb128', dependencies: [openssl_dep])
lws_have_evp_aes_192_cfb8 = c_compiler.has_function(varia + 'EVP_aes_192_cfb8', dependencies: [openssl_dep])
lws_have_evp_aes_192_cfb128 = c_compiler.has_function(varia + 'EVP_aes_192_cfb128', dependencies: [openssl_dep])
lws_have_evp_aes_256_cfb8 = c_compiler.has_function(varia + 'EVP_aes_256_cfb8', dependencies: [openssl_dep])
lws_have_evp_aes_256_cfb128 = c_compiler.has_function(varia + 'EVP_aes_256_cfb128', dependencies: [openssl_dep])
lws_have_evp_aes_128_xts = c_compiler.has_function(varia + 'EVP_aes_128_xts', dependencies: [openssl_dep])
lws_have_rsa_verify_pss_mgf1 = c_compiler.has_function(varia + 'RSA_verify_pss_mgf1', dependencies: [openssl_dep])
lws_have_hmac_ctx_new = c_compiler.has_function(varia + 'HMAC_CTX_new', dependencies: [openssl_dep])
lws_have_ssl_ctx_set_ciphersuites = c_compiler.has_function(varia + 'SSL_CTX_set_ciphersuites', dependencies: [openssl_dep])
if (lws_with_ssl and not lws_with_mbedtls)
    lws_have_ssl_extra_chain_certs = c_compiler.compiles('#include <openssl/ssl.h>\nint main(void) { STACK_OF(X509) *c = NULL; SSL_CTX *ctx = NULL; return (int)SSL_CTX_get_extra_chain_certs_only(ctx, &c); }\n', dependencies: [openssl_dep])
    lws_have_evp_md_ctx_free = c_compiler.compiles('#include <openssl/ssl.h>\nint main(void) { EVP_MD_CTX *md_ctx = NULL; EVP_MD_CTX_free(md_ctx); return 0; }\n', dependencies: [openssl_dep])
    lws_have_ecdsa_sig_set0 = c_compiler.has_function(varia + 'ECDSA_SIG_set0', dependencies: [openssl_dep])
    lws_have_bn_bn2binpad = c_compiler.has_function(varia + 'BN_bn2binpad', dependencies: [openssl_dep])
    lws_have_evp_aes_128_wrap = c_compiler.has_function(varia + 'EVP_aes_128_wrap', dependencies: [openssl_dep])
    lws_have_ec_point_get_affine_coordinates = c_compiler.has_function(varia + 'EC_POINT_get_affine_coordinates', dependencies: [openssl_dep])
endif
if lws_with_mbedtls
	lws_have_tls_client_method = true
	if not lws_plat_freertos
		# not supported in esp-idf openssl wrapper yet, but is in our version
		lws_have_x509_verify_param_set1_host = true
	endif

	lws_have_mbedtls_ssl_conf_alpn_protocols = c_compiler.has_function('mbedtls_ssl_conf_alpn_protocols')
	lws_have_mbedtls_ssl_get_alpn_protocol = c_compiler.has_function('mbedtls_ssl_get_alpn_protocol')
	lws_have_mbedtls_ssl_conf_sni = c_compiler.has_function('mbedtls_ssl_conf_sni')
	lws_have_mbedtls_ssl_set_hs_ca_chain = c_compiler.has_function('mbedtls_ssl_set_hs_ca_chain')
	lws_have_mbedtls_ssl_set_hs_own_cert = c_compiler.has_function('mbedtls_ssl_set_hs_own_cert')
	lws_have_mbedtls_ssl_set_hs_authmode = c_compiler.has_function('mbedtls_ssl_set_hs_authmode')
	lws_have_mbedtls_net_init = c_compiler.has_function('mbedtls_net_init')
    lws_have_tlsv1_2_client_method = false
else
	lws_have_mbedtls_ssl_conf_alpn_protocols = false
	lws_have_mbedtls_ssl_get_alpn_protocol = false
	lws_have_mbedtls_ssl_conf_sni = false
	lws_have_mbedtls_ssl_set_hs_ca_chain = false
	lws_have_mbedtls_ssl_set_hs_own_cert = false
	lws_have_mbedtls_ssl_set_hs_authmode = false
	lws_have_mbedtls_net_init = false

    lws_have_tls_client_method = c_compiler.has_function(varia + 'TLS_client_method')
    lws_have_tlsv1_2_client_method = c_compiler.has_function(varia + 'TLSv1_2_client_method')
endif

# ideally we want to use pipe2()

lws_have_pipe2 = c_compiler.compiles('#define _GNU_SOURCE\n#include <unistd.h>\nint main(void) {int fd[2];\n return pipe2(fd, 0);\n}\n')

# old mbedtls has everything in mbedtls/net.h

lws_have_mbedtls_net_sockets = c_compiler.compiles('#include <mbedtls/net_sockets.h>\nint main(void) { return 0;}\n')

# tcp keepalive needs this on linux to work practically... but it only exists
# after kernel 2.6.37

lws_have_tcp_user_timeout = c_compiler.compiles('#include <netinet/tcp.h>\nint main(void) { return TCP_USER_TIMEOUT; }\n')



lws_includes = include_directories(lws_incdirs)

lws_sources = ['lib/core/alloc.c',
	'lib/core/buflist.c',
	'lib/core/context.c',
	'lib/core/lws_dll2.c',
	'lib/core/libwebsockets.c',
	'lib/core/logs.c',
	'lib/system/system.c',
	'lib/misc/base64-decode.c',
	'lib/misc/lws-ring.c']

if lws_with_spawn
    lws_sources += ['lib/misc/spawn.c']
endif

if lws_with_fsmount and (build_machine.system() == 'linux')
    lws_sources += ['lib/misc/fsmount.c']
endif

if lws_with_file_ops
    lws_sources += ['lib/core/vfs.c']
endif

if lws_with_deprecated_lws_dll
    lws_sources += ['lib/core/lws_dll.c']
endif

if lws_with_network
    lws_sources += [
		'lib/core-net/dummy-callback.c',
		'lib/core-net/output.c',
		'lib/core-net/close.c',
		'lib/core-net/network.c',
		'lib/core-net/vhost.c',
		'lib/core-net/pollfd.c',
		'lib/core-net/service.c',
		'lib/core-net/sorted-usec-list.c',
		'lib/core-net/state.c',
		'lib/core-net/stats.c',
		'lib/core-net/wsi.c',
		'lib/core-net/wsi-timeout.c',
		'lib/core-net/adopt.c',
		'lib/roles/pipe/ops-pipe.c']

    if lws_with_sys_async_dns
        lws_sources += [
            'lib/system/async-dns/async-dns.c',
            'lib/system/async-dns/async-dns-parse.c']
    endif

    if lws_with_sys_ntpclient
        lws_sources += ['lib/system/ntpclient/ntpclient.c']
    endif

    if lws_with_sys_dhcp_client
        lws_sources += ['lib/system/dhcpclient/dhcpclient.c']
    endif

    if lws_with_detailed_latency
        lws_sources += ['lib/core-net/detailed-latency.c']
    endif

    if lws_with_lws_dsh
        lws_sources += ['lib/core-net/lws-dsh.c']
    endif

    if lws_with_sequencer
        lws_sources += ['lib/core-net/sequencer.c']
    endif

    if lws_with_abstract
        lws_sources += ['lib/abstract/abstract.c']

        if lws_with_sequencer
            lws_sources += ['lib/abstract/test-sequencer.c']
        endif
    endif

    if lws_with_secure_streams
        lws_sources += [
            'lib/secure-streams/secure-streams.c',
            'lib/secure-streams/policy.c',
            'lib/secure-streams/system/fetch-policy/fetch-policy.c'
        ]

        if lws_role_h1
            lws_sources += ['lib/secure-streams/protocols/ss-h1.c']
        endif

        if lws_role_h2
            lws_sources += ['lib/secure-streams/protocols/ss-h2.c']
        endif

        if lws_role_ws
            lws_sources += ['lib/secure-streams/protocols/ss-ws.c']
        endif

        if lws_role_mqtt
            lws_sources += ['lib/secure-streams/protocols/ss-mqtt.c']
        endif

        if lws_with_secure_streams_proxy_api
            lws_sources += [
                'lib/secure-streams/secure-streams-serialize.c',
                'lib/secure-streams/secure-streams-client.c']
        endif

        if lws_with_secure_streams_proxy_api
            lws_sources += ['lib/secure-streams/secure-streams-process.c']
        endif

        if lws_with_secure_streams_sys_auth_api_amazon_com
            lws_sources += ['lib/secure-streams/system/auth-api.amazon.com/auth.c']
        endif
    endif

    if lws_with_stats
        lws_sources += ['lib/core-net/stats.c']
    endif
endif

if lws_with_dir
    lws_sources += ['lib/misc/dir.c']
endif

if lws_role_mqtt and lws_with_client
    lws_sources += [
        'lib/roles/mqtt/mqtt.c',
        'lib/roles/mqtt/ops-mqtt.c',
        'lib/roles/mqtt/primitives.c',
        'lib/roles/mqtt/client/client-mqtt.c',
        'lib/roles/mqtt/client/client-mqtt-handshake.c']
endif

if lws_with_threadpool and unix and lws_have_pthread_h
    lws_sources += ['lib/misc/threadpool/threadpool.c']
endif

if lws_role_h1 or lws_role_h2
    lws_sources += [
        'lib/roles/http/header.c',
        'lib/roles/http/parsers.c']

    if lws_with_http_stream_compression
        lws_sources += [
            'lib/roles/http/compression/stream.c',
            'lib/roles/http/compression/deflate/deflate.c']
        if lws_with_http_brotli
            lws_sources += ['lib/roles/http/compression/brotli/brotli.c']
        endif
    endif
endif

if lws_role_h1
    lws_sources += ['lib/roles/h1/ops-h1.c']
endif

if lws_role_ws
    lws_sources += ['lib/roles/ws/ops-ws.c']
    if not lws_without_client
        lws_sources += [
            'lib/roles/ws/client-ws.c',
            'lib/roles/ws/client-parser-ws.c']
    endif
    if not lws_without_server
        lws_sources += ['lib/roles/ws/server-ws.c']
    endif
endif

if lws_role_raw
    lws_sources += ['lib/roles/raw-skt/ops-raw-skt.c']
    if lws_role_raw_file
        lws_sources += ['lib/roles/raw-file/ops-raw-file.c']
    endif
    if lws_with_abstract
        lws_sources += ['lib/abstract/transports/raw-skt.c']
    endif
endif

if lws_role_raw_proxy
    lws_sources += ['lib/roles/raw-proxy/ops-raw-proxy.c']
endif

if lws_role_cgi
    lws_sources += [
        'lib/roles/cgi/cgi-server.c',
        'lib/roles/cgi/ops-cgi.c']
endif

if lws_role_dbus
    lws_sources += ['lib/roles/dbus/dbus.c']
endif

if lws_with_access_log
    lws_sources += ['lib/roles/http/server/access-log.c']
endif

if lws_with_peer_limits
    lws_sources += ['lib/misc/peer-limits.c']
endif

if lws_with_lwsac
    lws_sources += [
        'lib/misc/lwsac/lwsac.c',
        'lib/misc/lwsac/cached-file.c']
endif

if lws_with_fts
    lws_sources += [
        'lib/misc/fts/trie.c',
		'lib/misc/fts/trie-fd.c']
endif

if lws_with_diskcache
    lws_sources += ['lib/misc/diskcache.c']
endif

if lws_with_struct_json
    lws_sources += ['lib/misc/lws-struct-lejp.c']
endif

if lws_with_struct_sqlite3
    lws_sources += ['lib/misc/lws-struct-sqlite.c']
endif

if not lws_without_client
    lws_sources += [
        'lib/core-net/connect.c',
		'lib/core-net/client.c',
		'lib/roles/http/client/client-http.c',
		'lib/roles/http/client/client-handshake.c']
endif

if not lws_without_server
    lws_sources += ['lib/core-net/server.c']
endif

if not lws_without_server or lws_with_secure_streams_proxy_api
    lws_sources += ['lib/roles/listen/ops-listen.c']
endif

if lws_with_mbedtls
    lws_incdirs += [
        'lib/tls/mbedtls/wrapper/include',
        'lib/tls/mbedtls/wrapper/include/platform',
        'lib/tls/mbedtls/wrapper/include/internal',
        'lib/tls/mbedtls/wrapper/include/openssl']
    
    if lws_with_network
        lws_sources += [
            'lib/tls/mbedtls/wrapper/library/ssl_cert.c',
			'lib/tls/mbedtls/wrapper/library/ssl_lib.c',
			'lib/tls/mbedtls/wrapper/library/ssl_methods.c',
			'lib/tls/mbedtls/wrapper/library/ssl_pkey.c',
			'lib/tls/mbedtls/wrapper/library/ssl_stack.c',
			'lib/tls/mbedtls/wrapper/library/ssl_x509.c']

        lws_sources += [
            'lib/tls/mbedtls/wrapper/platform/ssl_pm.c',
			'lib/tls/mbedtls/wrapper/platform/ssl_port.c']
    endif
endif

if lws_with_ssl
    lws_sources += ['lib/tls/tls.c']

    if lws_with_network
        lws_sources += ['lib/tls/tls-network.c']
    endif

    if lws_with_mbedtls
        lws_sources += [
            'lib/tls/mbedtls/mbedtls-tls.c',
			'lib/tls/mbedtls/mbedtls-x509.c']
        
        if lws_with_network
            lws_sources += ['lib/tls/mbedtls/mbedtls-ssl.c']
        endif

        if lws_with_gencrypto
            lws_sources += [
                'lib/tls/mbedtls/lws-genhash.c',
				'lib/tls/mbedtls/lws-genrsa.c',
				'lib/tls/mbedtls/lws-genaes.c',
				'lib/tls/lws-genec-common.c',
				'lib/tls/mbedtls/lws-genec.c',
				'lib/tls/mbedtls/lws-gencrypto.c']
        endif
    else
        lws_sources += [
            'lib/tls/openssl/openssl-tls.c',
			'lib/tls/openssl/openssl-x509.c']
        
        if lws_with_network
            lws_sources += ['lib/tls/openssl/openssl-ssl.c']
        endif

        if lws_with_gencrypto
            lws_sources += [
                'lib/tls/openssl/lws-genhash.c',
				'lib/tls/openssl/lws-genrsa.c',
				'lib/tls/openssl/lws-genaes.c',
				'lib/tls/lws-genec-common.c',
				'lib/tls/openssl/lws-genec.c',
				'lib/tls/openssl/lws-gencrypto.c']
        endif
    endif

    if not lws_without_server
        lws_sources += ['lib/tls/tls-server.c']

        if lws_with_mbedtls
            lws_sources += ['lib/tls/mbedtls/mbedtls-server.c']
        else
            lws_sources += ['lib/tls/openssl/openssl-server.c']
        endif
    endif

    if not lws_without_client
        lws_sources += ['lib/tls/tls-client.c']

        if lws_with_mbedtls
            lws_sources += ['lib/tls/mbedtls/mbedtls-client.c']
        else
            lws_sources += ['lib/tls/openssl/openssl-client.c']
        endif
    endif
endif

if not lws_without_builtin_sha1
    lws_sources += ['lib/misc/sha-1.c']
endif

if lws_with_http2 and not lws_without_server
    lws_sources += [
        'lib/roles/h2/http2.c',
		'lib/roles/h2/hpack.c',
		'lib/roles/h2/ops-h2.c']
endif

# select the active platform files

if win32
    lws_sources += [
        'lib/plat/windows/windows-fds.c',
		'lib/plat/windows/windows-file.c',
		'lib/plat/windows/windows-init.c',
		'lib/plat/windows/windows-misc.c',
		'lib/plat/windows/windows-pipe.c',
		'lib/plat/windows/windows-plugins.c',
		'lib/plat/windows/windows-service.c',
		'lib/plat/windows/windows-sockets.c']

    if lws_with_sys_async_dns
        lws_sources += ['lib/plat/windows/windows-resolv.c']
    endif

elif lws_plat_optee
    lws_sources += ['lib/plat/optee/lws-plat-optee.c']

    if lws_with_network
        lws_sources += ['lib/plat/optee/network.c']
    endif

elif lws_plat_freertos
    lws_sources += [
        'lib/plat/freertos/freertos-fds.c',
		'lib/plat/freertos/freertos-init.c',
		'lib/plat/freertos/freertos-misc.c',
		'lib/plat/freertos/freertos-pipe.c',
		'lib/plat/freertos/freertos-service.c',
		'lib/plat/freertos/freertos-sockets.c',
		'lib/misc/romfs.c']

    if lws_with_esp32_helper
        lws_sources += ['lib/plat/freertos/esp32/esp32-helpers.c']
    endif

    if lws_with_file_ops
        lws_sources += ['lib/plat/freertos/freertos-file.c']
    endif

    if lws_with_sys_async_dns
        lws_sources += ['lib/plat/freertos/freertos-resolv.c']
    endif

else
    lws_plat_unix = true
    lws_sources += [
        'lib/plat/unix/unix-caps.c',
		'lib/plat/unix/unix-misc.c',
		'lib/plat/unix/unix-init.c']

    if lws_with_file_ops
        lws_sources += ['lib/plat/unix/unix-file.c']
    endif

    if lws_with_network
        lws_sources += [
            'lib/plat/unix/unix-pipe.c',
			'lib/plat/unix/unix-service.c',
			'lib/plat/unix/unix-sockets.c',
			'lib/plat/unix/unix-fds.c']

        if lws_with_sys_async_dns
            if lws_plat_android
                lws_sources += ['lib/plat/unix/android/android-resolv.c']
            else
                lws_sources += ['lib/plat/unix/unix-resolv.c']
            endif
        endif
    endif

    if lws_with_plugins and lws_with_libuv
        lws_sources += ['lib/plat/unix/unix-plugins.c']
    endif
endif

if lws_with_socks5 and not lws_without_client
    lws_sources += ['lib/core-net/socks5-client.c']
endif

if (lws_role_h1 or lws_role_h2) and not lws_without_server
    lws_sources += [
        'lib/roles/http/server/server.c',
		'lib/roles/http/server/lws-spa.c']
endif

if lws_role_ws and not lws_without_extensions
    lws_sources += [
        'lib/roles/ws/ext/extension.c',
        'lib/roles/ws/ext/extension-permessage-deflate.c']
endif

if lws_with_http_proxy
    lws_sources += ['lib/roles/http/server/rewrite.c']
endif

if lws_with_poll and lws_with_network
    lws_sources += ['lib/event-libs/poll/poll.c']
endif

if lws_with_libuv and lws_with_network
    lws_sources += ['lib/event-libs/libuv/libuv.c']
endif

if lws_with_libevent and lws_with_network
    lws_sources += ['lib/event-libs/libevent/libevent.c']
endif

if lws_with_glib and lws_with_network
    lws_sources += ['lib/event-libs/glib/glib.c']
endif

if lws_with_libev and lws_with_network
    lws_sources += ['lib/event-libs/libev/libev.c']
	# libev generates a big mess of warnings with gcc, maintainer claims gcc to blame
    # ToDo: How to express this in meson?
	# set_source_files_properties( lib/event-libs/libev/libev.c PROPERTIES COMPILE_FLAGS "-Wno-error" )
endif

if lws_with_lejp
    lws_sources += ['lib/misc/lejp.c']
endif

if lws_with_lejp_conf and lws_with_network and not lws_plat_optee
    lws_sources += ['lib/roles/http/server/lejp-conf.c']
endif

if lws_with_abstract
    lws_sources += ['lib/abstract/transports/unit-test.c']
endif

#if lws_with_smtp
#    lws_sources += [
#        'lib/abstract/protocols/smtp/smtp.c',
#        'lib/abstract/protocols/smtp/smtp-sequencer.c']
#endif

if lws_with_ranges
    lws_sources += ['lib/roles/http/server/ranges.c']
endif

if lws_with_zip_fops
    if lws_with_zlib
        lws_sources += ['lib/roles/http/server/fops-zip.c']
    else
        error('Pre-zipped file support (LWS_WITH_ZIP_FOPS) requires ZLIB (LWS_WITH_ZLIB)')
    endif
endif

if lws_with_jose
    lws_sources += [
        'lib/jose/jwk/jwk.c',
		'lib/jose/jws/jose.c',
		'lib/jose/jws/jws.c',
		'lib/jose/jwe/jwe.c',
		'lib/jose/jwe/enc/aescbc.c',
		'lib/jose/jwe/enc/aesgcm.c',
		'lib/jose/jwe/enc/aeskw.c',
		'lib/jose/jwe/jwe-rsa-aescbc.c',
		'lib/jose/jwe/jwe-rsa-aesgcm.c',
		'lib/jose/jwe/jwe-ecdh-es-aeskw.c']
endif

if lws_with_tls and (lws_with_jose or lws_with_gencrypto)
    lws_sources += ['lib/tls/lws-gencrypto-common.c']
endif

# Add helper files for Windows.
if win32
    win32_helper_path = 'win32port/win32helpers'
    lws_incdirs += [win32_helper_path]
    lws_sources += [win32_helper_path + '/gettimeofday.c']
else
    # Unix.
    if not lws_without_daemonize
        lws_sources += ['lib/misc/daemonize.c']
    endif
endif

if unix
    if not lws_have_getifaddrs
        lws_sources += ['lib/misc/getifaddrs.c']
    endif
endif

lws_have_visibility = c_compiler.has_argument('-fvisibility=hidden')
if lws_have_visibility
    lws_c_args += ['-fvisibility=hidden']
endif

lws_config_private_data = configuration_data()
lws_config_private_data.set('LWS_HAVE_DLFCN_H', lws_have_dlfcn_h)
lws_config_private_data.set('LWS_HAVE_FCNTL_H', lws_have_fcntl_h)
lws_config_private_data.set('LWS_HAVE_FORK', lws_have_fork)
lws_config_private_data.set('LWS_HAVE_GETENV', lws_have_getenv)
lws_config_private_data.set('LWS_HAVE_IN6ADDR_H', lws_have_in6addr_h)
lws_config_private_data.set('LWS_HAVE_MALLOC', lws_have_malloc)
lws_config_private_data.set('LWS_HAVE_MEMORY_H', lws_have_memory_h)
lws_config_private_data.set('LWS_HAVE_MEMSET', lws_have_memset)
lws_config_private_data.set('LWS_HAVE_NETINET_IN_H', lws_have_netinet_in_h)
lws_config_private_data.set('LWS_HAVE_REALLOC', lws_have_realloc)
lws_config_private_data.set('LWS_HAVE_STDINT_H', lws_have_stdint_h)
lws_config_private_data.set('LWS_HAVE_STDLIB_H', lws_have_stdlib_h)
lws_config_private_data.set('LWS_HAVE_STRERROR', lws_have_strerror)
lws_config_private_data.set('LWS_HAVE_STRINGS_H', lws_have_strings_h)
lws_config_private_data.set('LWS_HAVE_STRING_H', lws_have_string_h)
lws_config_private_data.set('LWS_HAVE_SYS_PRCTL_H', lws_have_sys_prctl_h)
lws_config_private_data.set('LWS_HAVE_SYS_SOCKET_H', lws_have_sys_socket_h)
lws_config_private_data.set('LWS_HAVE_SYS_SOCKIO_H', lws_have_sys_sockio_h)
lws_config_private_data.set('LWS_HAVE_SYS_STAT_H', lws_have_sys_stat_h)
lws_config_private_data.set('LWS_HAVE_SYS_TYPES_H', lws_have_sys_types_h)
lws_config_private_data.set('LWS_HAVE_UNISTD_H', lws_have_unistd_h)
lws_config_private_data.set('LWS_HAVE_VFORK', lws_have_vfork)
lws_config_private_data.set('LWS_HAVE_VFORK_H', lws_have_vfork_h)
lws_config_private_data.set('LWS_HAVE_WORKING_FORK', lws_have_working_fork)
lws_config_private_data.set('LWS_HAVE_WORKING_VFORK', lws_have_working_vfork)
lws_config_private_data.set('LWS_HAVE_EXECVPE', lws_have_execvpe)
lws_config_private_data.set('LWS_HAVE_ZLIB_H', lws_have_zlib_h)
lws_config_private_data.set('LWS_WITH_ZLIB', lws_with_zlib)
lws_config_private_data.set('LWS_HAS_PTHREAD_SETNAME_NP', lws_has_pthread_setname_np)
lws_config_private_h = configure_file(input: 'cmake/lws_config_private.h.in',
    output: 'lws_config_private.h',
    configuration: lws_config_private_data,
    format: 'cmake')
lws_sources += [lws_config_private_h]

lws_config_data = configuration_data()
lws_config_data.set('CMAKE_INSTALL_PREFIX', '/usr/local')
lws_config_data.set('LWS_LIBRARY_VERSION_MAJOR', lws_library_version_major)
lws_config_data.set('LWS_LIBRARY_VERSION_MINOR', lws_library_version_minor)
lws_config_data.set('LWS_LIBRARY_VERSION_PATCH', lws_library_version_patch)
lws_config_data.set('LWS_MAX_SMP', lws_max_smp)
#lws_config_data.set('LWS_LIBRARY_VERSION_NUMBER',lws_library_version_number)
lws_config_data.set('LWS_AVOID_SIGPIPE_IGN',lws_avoid_sigpipe_ign)
lws_config_data.set('LWS_BUILD_HASH',lws_build_hash)
lws_config_data.set('LWS_BUILTIN_GETIFADDRS',lws_builtin_getifaddrs)
lws_config_data.set('LWS_CLIENT_HTTP_PROXYING',lws_client_http_proxying)
lws_config_data.set('LWS_DETECTED_PLAT_IOS',lws_detected_plat_ios)
lws_config_data.set('LWS_FALLBACK_GETHOSTBYNAME',lws_fallback_gethostbyname)
lws_config_data.set('LWS_HAS_INTPTR_T',lws_has_intptr_t)
lws_config_data.set('LWS_HAS_GETOPT_LONG',lws_has_getopt_long)
lws_config_data.set('LWS_HAVE__ATOI64',lws_have__atoi64)
lws_config_data.set('LWS_HAVE_ATOLL',lws_have_atoll)
lws_config_data.set('LWS_HAVE_BN_bn2binpad',lws_have_bn_bn2binpad)
lws_config_data.set('LWS_HAVE_CLOCK_GETTIME',lws_have_clock_gettime)
lws_config_data.set('LWS_HAVE_EC_POINT_get_affine_coordinates',lws_have_ec_point_get_affine_coordinates)
lws_config_data.set('LWS_HAVE_ECDSA_SIG_set0',lws_have_ecdsa_sig_set0)
lws_config_data.set('LWS_HAVE_EVP_MD_CTX_free',lws_have_evp_md_ctx_free)
lws_config_data.set('LWS_HAVE_EVP_aes_128_wrap',lws_have_evp_aes_128_wrap)
lws_config_data.set('LWS_HAVE_EVP_aes_128_cfb8',lws_have_evp_aes_128_cfb8)
lws_config_data.set('LWS_HAVE_EVP_aes_128_cfb128',lws_have_evp_aes_128_cfb128)
lws_config_data.set('LWS_HAVE_EVP_aes_192_cfb8',lws_have_evp_aes_192_cfb8)
lws_config_data.set('LWS_HAVE_EVP_aes_192_cfb128',lws_have_evp_aes_192_cfb128)
lws_config_data.set('LWS_HAVE_EVP_aes_256_cfb8',lws_have_evp_aes_256_cfb8)
lws_config_data.set('LWS_HAVE_EVP_aes_256_cfb128',lws_have_evp_aes_256_cfb128)
lws_config_data.set('LWS_HAVE_EVP_aes_128_xts',lws_have_evp_aes_128_xts)
lws_config_data.set('LWS_HAVE_EXECVPE',lws_have_execvpe)
lws_config_data.set('LWS_HAVE_LIBCAP',lws_have_libcap)
lws_config_data.set('LWS_HAVE_HMAC_CTX_new',lws_have_hmac_ctx_new)
lws_config_data.set('LWS_HAVE_MALLOC_H',lws_have_malloc_h)
lws_config_data.set('LWS_HAVE_MALLOC_TRIM',lws_have_malloc_trim)
lws_config_data.set('LWS_HAVE_MALLOC_USABLE_SIZE',lws_have_malloc_usable_size)
lws_config_data.set('LWS_HAVE_mbedtls_net_init',lws_have_mbedtls_net_init)
lws_config_data.set('LWS_HAVE_mbedtls_ssl_conf_alpn_protocols',lws_have_mbedtls_ssl_conf_alpn_protocols)
lws_config_data.set('LWS_HAVE_mbedtls_ssl_get_alpn_protocol',lws_have_mbedtls_ssl_get_alpn_protocol)
lws_config_data.set('LWS_HAVE_mbedtls_ssl_conf_sni',lws_have_mbedtls_ssl_conf_sni)
lws_config_data.set('LWS_HAVE_mbedtls_ssl_set_hs_ca_chain',lws_have_mbedtls_ssl_set_hs_ca_chain)
lws_config_data.set('LWS_HAVE_mbedtls_ssl_set_hs_own_cert',lws_have_mbedtls_ssl_set_hs_own_cert)
lws_config_data.set('LWS_HAVE_mbedtls_ssl_set_hs_authmode',lws_have_mbedtls_ssl_set_hs_authmode)
lws_config_data.set('LWS_HAVE_MBEDTLS_NET_SOCKETS',lws_have_mbedtls_net_sockets)
lws_config_data.set('LWS_HAVE_NEW_UV_VERSION_H',lws_have_new_uv_version_h)
lws_config_data.set('LWS_HAVE_OPENSSL_ECDH_H',lws_have_openssl_ecdh_h)
lws_config_data.set('LWS_HAVE_PIPE2',lws_have_pipe2)
lws_config_data.set('LWS_HAVE_EVENTFD',lws_have_eventfd)
lws_config_data.set('LWS_HAVE_PTHREAD_H',lws_have_pthread_h)
lws_config_data.set('LWS_HAVE_RSA_SET0_KEY',lws_have_rsa_set0_key)
lws_config_data.set('LWS_HAVE_RSA_verify_pss_mgf1',lws_have_rsa_verify_pss_mgf1)
lws_config_data.set('LWS_HAVE_SSL_CTX_get0_certificate',lws_have_ssl_ctx_get0_certificate)
lws_config_data.set('LWS_HAVE_SSL_CTX_set1_param',lws_have_ssl_ctx_set1_param)
lws_config_data.set('LWS_HAVE_SSL_CTX_set_ciphersuites',lws_have_ssl_ctx_set_ciphersuites)
lws_config_data.set('LWS_HAVE_SSL_EXTRA_CHAIN_CERTS',lws_have_ssl_extra_chain_certs)
lws_config_data.set('LWS_HAVE_SSL_get0_alpn_selected',lws_have_ssl_get0_alpn_selected)
lws_config_data.set('LWS_HAVE_SSL_CTX_EVP_PKEY_new_raw_private_key',lws_have_ssl_ctx_evp_pkey_new_raw_private_key)
lws_config_data.set('LWS_HAVE_SSL_set_alpn_protos',lws_have_ssl_set_alpn_protos)
lws_config_data.set('LWS_HAVE_SSL_SET_INFO_CALLBACK',lws_have_ssl_set_info_callback)
lws_config_data.set('LWS_HAVE__STAT32I64',lws_have__stat32i64)
lws_config_data.set('LWS_HAVE_STDINT_H',lws_have_stdint_h)
lws_config_data.set('LWS_HAVE_SYS_CAPABILITY_H',lws_have_sys_capability_h)
lws_config_data.set('LWS_HAVE_TLS_CLIENT_METHOD',lws_have_tls_client_method)
lws_config_data.set('LWS_HAVE_TLSV1_2_CLIENT_METHOD',lws_have_tlsv1_2_client_method)
lws_config_data.set('LWS_HAVE_UV_VERSION_H',lws_have_uv_version_h)
lws_config_data.set('LWS_HAVE_VFORK',lws_have_vfork)
lws_config_data.set('LWS_HAVE_X509_get_key_usage',lws_have_x509_get_key_usage)
lws_config_data.set('LWS_HAVE_X509_VERIFY_PARAM_set1_host',lws_have_x509_verify_param_set1_host)
lws_config_data.set('LWS_LIBRARY_VERSION',lws_library_version)
lws_config_data.set('LWS_LOGGING_BITFIELD_CLEAR',lws_logging_bitfield_clear)
lws_config_data.set('LWS_LOGGING_BITFIELD_SET', lws_logging_bitfield_set)
lws_config_data.set('LWS_MINGW_SUPPORT',lws_mingw_support)
lws_config_data.set('LWS_NO_CLIENT',lws_no_client)
lws_config_data.set('LWS_NO_DAEMONIZE',lws_no_daemonize)
lws_config_data.set('LWS_OPENSSL_CLIENT_CERTS',lws_openssl_client_certs)
lws_config_data.set('LWS_OPENSSL_SUPPORT',lws_openssl_support)
lws_config_data.set('LWS_PLAT_OPTEE',lws_plat_optee)
lws_config_data.set('LWS_PLAT_UNIX',lws_plat_unix)
lws_config_data.set('LWS_PLAT_FREERTOS',lws_plat_freertos)
lws_config_data.set('LWS_ROLE_CGI',lws_role_cgi)
lws_config_data.set('LWS_ROLE_DBUS',lws_role_dbus)
lws_config_data.set('LWS_ROLE_H1',lws_role_h1)
lws_config_data.set('LWS_ROLE_H2',lws_role_h2)
lws_config_data.set('LWS_ROLE_RAW',lws_role_raw)
lws_config_data.set('LWS_ROLE_RAW_FILE',lws_role_raw_file)
lws_config_data.set('LWS_ROLE_RAW_PROXY',lws_role_raw_proxy)
lws_config_data.set('LWS_ROLE_WS',lws_role_ws)
lws_config_data.set('LWS_ROLE_MQTT',lws_role_mqtt)
lws_config_data.set('LWS_SHA1_USE_OPENSSL_NAME',lws_sha1_use_openssl_name)
lws_config_data.set('LWS_SSL_CLIENT_USE_OS_CA_CERTS',lws_ssl_client_use_os_ca_certs)
lws_config_data.set('LWS_SSL_SERVER_WITH_ECDH_CERT',lws_ssl_server_with_ecdh_cert)
lws_config_data.set('LWS_WITH_ABSTRACT',lws_with_abstract)
lws_config_data.set('LWS_WITH_ACCESS_LOG',lws_with_access_log)
lws_config_data.set('LWS_WITH_ACME',lws_with_acme)
lws_config_data.set('LWS_WITH_ALSA',lws_with_alsa)
lws_config_data.set('LWS_WITH_SYS_ASYNC_DNS',lws_with_sys_async_dns)
lws_config_data.set('LWS_WITH_BORINGSSL',lws_with_boringssl)
lws_config_data.set('LWS_WITH_CGI',lws_with_cgi)
lws_config_data.set('LWS_WITH_CUSTOM_HEADERS',lws_with_custom_headers)
lws_config_data.set('LWS_WITH_DEPRECATED_LWS_DLL',lws_with_deprecated_lws_dll)
lws_config_data.set('LWS_WITH_DETAILED_LATENCY',lws_with_detailed_latency)
lws_config_data.set('LWS_WITH_DIR',lws_with_dir)
lws_config_data.set('LWS_WITH_ESP32',lws_with_esp32)
lws_config_data.set('LWS_HAVE_EVBACKEND_LINUXAIO',lws_have_evbackend_linuxaio)
lws_config_data.set('LWS_HAVE_EVBACKEND_IOURING',lws_have_evbackend_iouring)
lws_config_data.set('LWS_WITH_EXTERNAL_POLL',lws_with_external_poll)
lws_config_data.set('LWS_WITH_FILE_OPS',lws_with_file_ops)
lws_config_data.set('LWS_WITH_FSMOUNT',lws_with_fsmount)
lws_config_data.set('LWS_WITH_FTS',lws_with_fts)
lws_config_data.set('LWS_WITH_GENCRYPTO',lws_with_gencrypto)
lws_config_data.set('LWS_WITH_GENERIC_SESSIONS',lws_with_generic_sessions)
lws_config_data.set('LWS_WITH_GLIB',lws_with_glib)
lws_config_data.set('LWS_WITH_GTK',lws_with_gtk)
lws_config_data.set('LWS_WITH_HTTP2',lws_with_http_basic_auth)
lws_config_data.set('LWS_WITH_HTTP_BASIC_AUTH',lws_with_http_basic_auth)
lws_config_data.set('LWS_WITH_HTTP_BROTLI',lws_with_http_brotli)
lws_config_data.set('LWS_WITH_HTTP_PROXY',lws_with_http_proxy)
lws_config_data.set('LWS_WITH_HTTP_STREAM_COMPRESSION',lws_with_http_stream_compression)
lws_config_data.set('LWS_WITH_HTTP_UNCOMMON_HEADERS',lws_with_http_uncommon_headers)
lws_config_data.set('LWS_WITH_IPV6',lws_with_ipv6)
lws_config_data.set('LWS_WITH_JOSE',lws_with_jose)
lws_config_data.set('LWS_WITH_LEJP',lws_with_lejp)
lws_config_data.set('LWS_WITH_LIBEV',lws_with_libev)
lws_config_data.set('LWS_WITH_LIBEVENT',lws_with_libevent)
lws_config_data.set('LWS_WITH_LIBUV',lws_with_libuv)
lws_config_data.set('LWS_WITH_LWSAC',lws_with_lwsac)
lws_config_data.set('LWS_LOGS_TIMESTAMP',lws_logs_timestamp)
lws_config_data.set('LWS_WITH_MBEDTLS',lws_with_mbedtls)
lws_config_data.set('LWS_WITH_MINIZ',lws_with_miniz)
lws_config_data.set('LWS_WITH_NETWORK',lws_with_network)
lws_config_data.set('LWS_WITH_NO_LOGS',lws_with_no_logs)
lws_config_data.set('LWS_WITH_CLIENT',lws_with_client)
lws_config_data.set('LWS_WITHOUT_EXTENSIONS',lws_without_extensions)
lws_config_data.set('LWS_WITH_SERVER',lws_with_server)
lws_config_data.set('LWS_WITH_SPAWN',lws_with_spawn)
lws_config_data.set('LWS_WITH_PEER_LIMITS',lws_with_peer_limits)
lws_config_data.set('LWS_WITH_PLUGINS',lws_with_plugins)
lws_config_data.set('LWS_WITH_POLARSSL',lws_with_polarssl)
lws_config_data.set('LWS_WITH_POLL',lws_with_poll)
lws_config_data.set('LWS_WITH_RANGES',lws_with_ranges)
lws_config_data.set('LWS_WITH_SECURE_STREAMS',lws_with_secure_streams)
lws_config_data.set('LWS_WITH_SECURE_STREAMS_SYS_AUTH_API_AMAZON_COM',lws_with_secure_streams_sys_auth_api_amazon_com)
lws_config_data.set('LWS_WITH_SECURE_STREAMS_PROXY_API',lws_with_secure_streams_proxy_api)
lws_config_data.set('LWS_WITH_SELFTESTS',lws_with_selftests)
lws_config_data.set('LWS_WITH_SEQUENCER',lws_with_sequencer)
lws_config_data.set('LWS_WITH_SERVER_STATUS',lws_with_server_status)
lws_config_data.set('LWS_WITH_SMTP',lws_with_smtp)
lws_config_data.set('LWS_WITH_SOCKS5',lws_with_socks5)
lws_config_data.set('LWS_WITH_STATEFUL_URLDECODE',lws_with_stateful_urldecode)
lws_config_data.set('LWS_WITH_STATS',lws_with_stats)
lws_config_data.set('LWS_WITH_STRUCT_SQLITE3',lws_with_struct_sqlite3)
lws_config_data.set('LWS_WITH_STRUCT_JSON',lws_with_struct_json)
lws_config_data.set('LWS_WITH_SQLITE3',lws_with_sqlite3)
lws_config_data.set('LWS_WITH_SYS_NTPCLIENT',lws_with_sys_ntpclient)
lws_config_data.set('LWS_WITH_SYS_DHCP_CLIENT',lws_with_sys_dhcp_client)
lws_config_data.set('LWS_WITH_THREADPOOL',lws_with_threadpool)
lws_config_data.set('LWS_WITH_TLS',lws_with_tls)
lws_config_data.set('LWS_WITH_UDP',lws_with_udp)
lws_config_data.set('LWS_WITH_UNIX_SOCK',lws_with_unix_sock)
lws_config_data.set('LWS_WITH_ZIP_FOPS',lws_with_zip_fops)
lws_config_data.set('USE_OLD_CYASSL',use_old_cyassl)
lws_config_data.set('USE_WOLFSSL',use_wolfssl)
lws_config_data.set('LWS_SIZEOFPTR_CODE', '')
lws_config_h = configure_file(input: 'cmake/lws_config.h.in',
    output: 'lws_config.h',
    configuration: lws_config_data,
    format: 'cmake')
lws_sources += [lws_config_h]

libwebsockets = library('websockets',
    lws_sources,
    version: meson.project_version(),
    soversion: lws_library_version_number,
    include_directories: lws_includes,
    c_args: lws_c_args,
    dependencies: lws_dependencies)

libwebsockets_dep = declare_dependency(
    include_directories: lws_includes,
    link_with: libwebsockets,
    dependencies: lws_dependencies)
