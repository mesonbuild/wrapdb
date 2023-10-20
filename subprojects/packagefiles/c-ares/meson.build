
project('c-ares', 'c', version: '1.20.1', license: 'MIT')
libtool_version = '2.7.1'
libtool_soversion = '2'

cc = meson.get_compiler('c')
winsock_deps = target_machine.system() == 'windows' ? [
  cc.find_library('iphlpapi'),
  cc.find_library('wininet'),
  cc.find_library('ws2_32'),
] : []

cares_dependencies = [
  winsock_deps,
]

cares_sources = files(
  'src/lib/ares__addrinfo2hostent.c',
  'src/lib/ares__addrinfo_localhost.c',
  'src/lib/ares__close_sockets.c',
  'src/lib/ares__get_hostent.c',
  'src/lib/ares__htable.c',
  'src/lib/ares__htable_asvp.c',
  'src/lib/ares__htable_stvp.c',
  'src/lib/ares__llist.c',
  'src/lib/ares__parse_into_addrinfo.c',
  'src/lib/ares__buf.c',
  'src/lib/ares__readaddrinfo.c',
  'src/lib/ares__slist.c',
  'src/lib/ares__sortaddrinfo.c',
  'src/lib/ares__read_line.c',
  'src/lib/ares__timeval.c',
  'src/lib/ares_android.c',
  'src/lib/ares_cancel.c',
  'src/lib/ares_data.c',
  'src/lib/ares_destroy.c',
  'src/lib/ares_expand_name.c',
  'src/lib/ares_expand_string.c',
  'src/lib/ares_fds.c',
  'src/lib/ares_free_hostent.c',
  'src/lib/ares_free_string.c',
  'src/lib/ares_freeaddrinfo.c',
  'src/lib/ares_getaddrinfo.c',
  'src/lib/ares_getenv.c',
  'src/lib/ares_gethostbyaddr.c',
  'src/lib/ares_gethostbyname.c',
  'src/lib/ares_getnameinfo.c',
  'src/lib/ares_getsock.c',
  'src/lib/ares_init.c',
  'src/lib/ares_library_init.c',
  'src/lib/ares_mkquery.c',
  'src/lib/ares_create_query.c',
  'src/lib/ares_nowarn.c',
  'src/lib/ares_options.c',
  'src/lib/ares_parse_a_reply.c',
  'src/lib/ares_parse_aaaa_reply.c',
  'src/lib/ares_parse_caa_reply.c',
  'src/lib/ares_parse_mx_reply.c',
  'src/lib/ares_parse_naptr_reply.c',
  'src/lib/ares_parse_ns_reply.c',
  'src/lib/ares_parse_ptr_reply.c',
  'src/lib/ares_parse_soa_reply.c',
  'src/lib/ares_parse_srv_reply.c',
  'src/lib/ares_parse_txt_reply.c',
  'src/lib/ares_parse_uri_reply.c',
  'src/lib/ares_platform.c',
  'src/lib/ares_process.c',
  'src/lib/ares_query.c',
  'src/lib/ares_rand.c',
  'src/lib/ares_search.c',
  'src/lib/ares_send.c',
  'src/lib/ares_strcasecmp.c',
  'src/lib/ares_strdup.c',
  'src/lib/ares_strerror.c',
  'src/lib/ares_strsplit.c',
  'src/lib/ares_timeout.c',
  'src/lib/ares_version.c',
  'src/lib/bitncmp.c',
  'src/lib/inet_net_pton.c',
  'src/lib/inet_ntop.c',
  'src/lib/windows_port.c')

cares_headers = files(
  'src/lib/ares__htable.h',
  'src/lib/ares__htable_asvp.h',
  'src/lib/ares__htable_stvp.h',
  'src/lib/ares__llist.h',
  'src/lib/ares__buf.h',
  'src/lib/ares__slist.h',
  'src/lib/ares_android.h',
  'src/lib/ares_data.h',
  'src/lib/ares_getenv.h',
  'src/lib/ares_inet_net_pton.h',
  'src/lib/ares_iphlpapi.h',
  'src/lib/ares_ipv6.h',
  'src/lib/ares_nowarn.h',
  'src/lib/ares_platform.h',
  'src/lib/ares_private.h',
  'src/lib/ares_strcasecmp.h',
  'src/lib/ares_strdup.h',
  'src/lib/ares_strsplit.h',
  'src/lib/bitncmp.h',
  'src/lib/ares_setup.h',
  'src/lib/setup_once.h')

cares_include_dirs = include_directories('include', 'src/lib')

cc = meson.get_compiler('c')
cares_args_map = {
'common': [
  '-DCARES_BUILDING_LIBRARY',

  cc.has_header('arpa/inet.h') ? '-DHAVE_ARPA_INET_H' : [],
  cc.has_header('errno.h') ? '-DHAVE_ERRNO_H' : [],
  cc.has_header('limits.h') ? '-DHAVE_LIMITS_H' : [],
  cc.has_header('netdb.h') ? '-DHAVE_NETDB_H' : [],
  cc.has_header('netinet/in.h') ? '-DHAVE_NETINET_IN_H' : [],
  cc.has_header('netinet/tcp.h') ? '-DHAVE_NETINET_TCP_H' : [],
  cc.has_header('stdint.h') ? '-DHAVE_STDINT_H' : [],
  cc.has_header('strings.h') ? '-DHAVE_STRINGS_H' : [],
  cc.has_header('sys/ioctl.h') ? '-DHAVE_SYS_IOCTL_H' : [],
  cc.has_header('sys/random.h') ? '-DHAVE_SYS_RANDOM_H' : [],
  cc.has_header('sys/socket.h') ? '-DHAVE_SYS_SOCKET_H' : [],
  cc.has_header('sys/stat.h') ? '-DHAVE_SYS_STAT_H' : [],
  cc.has_header('sys/time.h') ? '-DHAVE_SYS_TIME_H' : [],
  (cc.has_header('sys/time.h') and cc.has_header('time.h')) ? '-DTIME_WITH_SYS_TIME' : [],
  cc.has_header('sys/types.h') ? '-DHAVE_SYS_TYPES_H' : [],
  cc.has_header('sys/uio.h') ? '-DHAVE_SYS_UIO_H' : [],

  cc.has_type('struct timeval', prefix: '#include <sys/time.h>') ? '-DHAVE_STRUCT_TIMEVAL' : [],
  cc.has_type('struct sockaddr_in6', prefix: '#include <sys/socket.h>\n#include <netinet/in.h>') ? '-DHAVE_STRUCT_SOCKADDR_IN6' : [],
  cc.has_type('struct addrinfo', prefix: '#include <sys/types.h>\n#include <sys/socket.h>\n#include <netdb.h>') ? '-DHAVE_STRUCT_ADDRINFO' : [],

  ## Wants meson 1.3.0
  # cc.has_define('AF_INET6', prefix: '#include <sys/socket.h>\n#include <netinet/in.h>') ? '-DHAVE_AF_INET6' : [],
  # cc.has_define('PF_INET6', prefix: '#include <sys/socket.h>\n#include <netinet/in.h>') ? '-DHAVE_PF_INET6' : [],
  # cc.has_define('O_NONBLOCK', prefix: '#include <fcntl.h>') ? '-DHAVE_FCNTL_O_NONBLOCK' : [],

  cc.has_function('recvfrom', prefix: '#include <sys/types.h>\n#include <sys/socket.h>') ? '-DHAVE_RECVFROM' : [],
  cc.has_function('writev', prefix: '#include <sys/uio.h>') ? '-DHAVE_WRITEV' : [],
],
'linux': [
  '-DHAVE_RECV',
    '-DRECV_TYPE_ARG1=int',
    '-DRECV_TYPE_ARG2=void*',
    '-DRECV_TYPE_ARG3=size_t',
    '-DRECV_TYPE_ARG4=int',
    '-DRECV_TYPE_RETV=ssize_t',
  '-DHAVE_SEND',
    '-DSEND_TYPE_ARG1=int',
    '-DSEND_QUAL_ARG2=const',
    '-DSEND_TYPE_ARG2=void*',
    '-DSEND_TYPE_ARG3=size_t',
    '-DSEND_TYPE_ARG4=int',
    '-DSEND_TYPE_RETV=ssize_t',
  '-DHAVE_AF_INET6',
  '-DHAVE_PF_INET6',
  '-DHAVE_FCNTL_O_NONBLOCK',
],
}
cares_args_map += {'darwin': cares_args_map['linux']}

cares_args = [cares_args_map['common'], cares_args_map.get(target_machine.system(), [])]

cares_config = {
'common': {
  'CARES_HAVE_SYS_TYPES_H': cc.has_header('sys/types.h'),
  'CARES_HAVE_SYS_RANDOM_H': cc.has_header('sys/random.h'),
  'CARES_HAVE_SYS_SOCKET_H': cc.has_header('sys/socket.h'),
  'CARES_HAVE_WINDOWS_H': cc.has_header('windows.h'),
  'CARES_HAVE_WS2TCPIP_H': cc.has_header('ws2tcpip.h'),
  'CARES_HAVE_WINSOCK2_H': cc.has_header('winsock2.h'),
  'CARES_HAVE_ARPA_NAMESER_H': cc.has_header('arpa/nameser.h'),
  'CARES_HAVE_ARPA_NAMESER_COMPAT_H': cc.has_header('arpa/nameser_compat.h'),
  'CARES_TYPEOF_ARES_SSIZE_T': 'ssize_t',
  'CARES_TYPEOF_ARES_SOCKLEN_T': 'socklen_t',
},
'windows': {
  'CARES_TYPEOF_ARES_SSIZE_T': '__int64',
  'CARES_TYPEOF_ARES_SOCKLEN_T': 'int',
},
}

ares_build_h = configure_file(
  input: 'include/ares_build.h.cmake',
  output: 'ares_build.h',
  configuration: cares_config['common'] + cares_config.get(target_machine.system(), {}),
  format: 'cmake@')

libcares = library('cares',
  sources: [cares_sources, cares_headers, ares_build_h],
  include_directories: cares_include_dirs,
  c_args: cares_args,
  dependencies: cares_dependencies,
  install: true,
  version: libtool_version,
  soversion: libtool_soversion)

cares_dep = declare_dependency(
  include_directories: cares_include_dirs,
  link_with: libcares)
meson.override_dependency('libcares', cares_dep)

cares_tools_include_dirs = include_directories('src/tools')

adig = executable('adig',
  sources: files('src/tools/adig.c', 'src/tools/ares_getopt.c', 'src/tools/ares_getopt.h'),
  include_directories: cares_tools_include_dirs,
  c_args: cares_args,
  dependencies: cares_dep,
  build_by_default: false)
if get_option('export_adig')
  meson.override_find_program('adig', adig)
endif

ahost = executable('ahost',
  sources: files('src/tools/ahost.c', 'src/tools/ares_getopt.c', 'src/tools/ares_getopt.h'),
  include_directories: cares_tools_include_dirs,
  c_args: cares_args,
  dependencies: cares_dep,
  build_by_default: false)
if get_option('export_ahost')
  meson.override_find_program('ahost')
endif
