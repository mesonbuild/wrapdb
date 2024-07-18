project(
    'nghttp2',
    'c',
    license: 'mit',
    version: '1.62.1',
)
cc = meson.get_compiler('c')

hex = '0123456789abcdef'
project_version_num = '0x' \
    + hex[meson.project_version().split('.')[0].to_int() / 16] \
    + hex[meson.project_version().split('.')[0].to_int() % 16] \
    + hex[meson.project_version().split('.')[1].to_int() / 16] \
    + hex[meson.project_version().split('.')[1].to_int() % 16] \
    + hex[meson.project_version().split('.')[2].to_int() / 16] \
    + hex[meson.project_version().split('.')[2].to_int() % 16]
configuration = configuration_data()
configuration.set('PACKAGE_VERSION', meson.project_version())
configuration.set('PACKAGE_VERSION_NUM', project_version_num)
configuration.set('PROJECT_VERSION', meson.project_version())
configuration.set('PROJECT_VERSION_MAJOR', meson.project_version().split('.')[0])
configuration.set('PROJECT_VERSION_MINOR', meson.project_version().split('.')[1])
configuration.set('PROJECT_VERSION_PATCH', meson.project_version().split('.')[2])
configuration.set('VERSION', meson.project_version())

if cc.has_function_attribute('noreturn')
    configuration.set('HINT_NORETURN', '__attribute__((noreturn))')
else
    configuration.set('HINT_NORETURN', '')
endif
if not cc.has_header_symbol('sys/types.h', 'ssize_t')
    configuration.set('ssize_t', 'int')
endif
configuration.set('HAVE_STD_MAP_EMPLACE', true)
configuration.set('HAVE_JANNSON', false)
configuration.set('HAVE_LIBXML2', false)
configuration.set('HAVE_MRUBY', false)
configuration.set('HAVE_NEVERBLEED', false)
configuration.set('SIZEOF_INT_P', cc.sizeof('int *'))
configuration.set('SIZEOF_TIME_T', cc.sizeof('time_t', prefix: '#include <time.h>'))
configuration.set('HAVE__EXIT', cc.has_header_symbol('stdlib.h', '_Exit'))
configuration.set('HAVE_ACCEPT4', cc.has_header_symbol('sys/socket.h', 'accept4'))
configuration.set('HAVE_CLOCK_GETTIME', cc.has_header_symbol('time.h', 'clock_gettime'))
configuration.set('HAVE_MKOSTEMP', cc.has_header_symbol('stdlib.h', 'mkostemp'))
configuration.set('HAVE_GETTICKCOUNT64', cc.has_header_symbol('sysinfoapi.h', 'GetTickCount64'))
configuration.set('HAVE_DECL_INITGROUPS', cc.has_header_symbol('grp.h', 'initgroups'))
configuration.set('DEBUGBUILD', false)
configuration.set('NOTHREADS', false)
configuration.set('HAVE_ARPA_INET_H', cc.has_header('arpa/inet.h'))
configuration.set('HAVE_FCNTL_H', cc.has_header('fcntl.h'))
configuration.set('HAVE_INTTYPES_H', cc.has_header('inttypes.h'))
configuration.set('HAVE_LIMITS_H', cc.has_header('limits.h'))
configuration.set('HAVE_NETDB_H', cc.has_header('netdb.h'))
configuration.set('HAVE_NETINET_IN_H', cc.has_header('netinet/in.h'))
configuration.set('HAVE_NETINET_IP_H', cc.has_header('netinet/ip.h'))
configuration.set('HAVE_PWD_H', cc.has_header('pwd.h'))
configuration.set('HAVE_SYS_SOCKET_H', cc.has_header('sys/socket.h'))
configuration.set('HAVE_SYS_TIME_H', cc.has_header('sys/time.h'))
configuration.set('HAVE_UNISTD_H', cc.has_header('unistd.h'))
configuration.set('HAVE_WINDOWS_H', cc.has_header('windows.h'))
configuration.set('ENABLE_HTTP3', false)
configuration.set('HAVE_LIBBPF', false)
configuration.set('HAVE_BPF_STATS_TYPE', cc.has_header_symbol('linux/bpf.h', 'enum bpf_stats_type'))
configuration.set('HAVE_LIBNGTCP2_CRYPTO_QUICTLS', false)
configuration.set('HAVE_LIBEV', false)

configure_file(
    input: 'cmakeconfig.h.in',
    output: 'config.h',
    format: 'cmake@',
    configuration: configuration,
)

subdir('lib')
