project(
  'libmicrohttpd',
  'c',
  version: '0.9.77',
  meson_version: '>=0.49.0',
  default_options: ['warning_level=1'],
)

add_project_arguments(
  '-D_GNU_SOURCE',
  language: 'c',
)

incdirs = include_directories('src/include')

cdata = configuration_data()
cc = meson.get_compiler('c')

headers = [
  'arpa/inet.h',
  'endian.h',
  'errno.h',
  'fcntl.h',
  'inetlib.h',
  'inttypes.h',
  'limits.h',
  'machine/endian.h',
  'machine/param.h',
  'memory.h',
  'net/if.h',
  'netdb.h',
  'netinet/icmp_var.h',
  'netinet/in.h',
  'netinet/ip.h',
  'netinet/ip_icmp.h',
  'netinet/tcp.h',
  'poll.h',
  'pthread.h',
  'pthread_np.h',
  'sdkdkver.h',
  'signal.h',
  'socklib.h',
  'stdalign.h',
  'stdbool.h',
  'stddef.h',
  'stdint.h',
  'stdio.h',
  'stdlib.h',
  'string.h',
  'strings.h',
  'sys/byteorder.h',
  'sys/endian.h',
  'sys/eventfd.h',
  'sys/ioctl.h',
  'sys/isa_defs.h',
  'sys/machine.h',
  'sys/mman.h',
  'sys/msg.h',
  'sys/param.h',
  'sys/select.h',
  'sys/socket.h',
  'sys/stat.h',
  'sys/sysctl.h',
  'sys/time.h',
  'sys/types.h',
  'time.h',
  'unistd.h',
  'windows.h',
  'winsock2.h',
  'ws2tcpip.h',
  'zlib.h',
]

foreach h : headers
  if cc.has_header(h)
    cdata.set('HAVE_@0@'.format(h.underscorify().to_upper()), 1)
  endif
endforeach

cdata.set('HAVE_ASSERT', cc.has_header_symbol('assert.h', 'assert'))
cdata.set10(
  'HAVE_INET6',
  cc.has_header_symbol('netinet/in.h', 'struct in6_addr'),
)

functions = [
  'accept4',
  'calloc',
  'clock_gettime',
  'clock_get_time',
  'epoll_create1',
  'fseeko',
  'fork',
  'getsockname',
  'gettimeofday',
  'lseek64',
  'memmem',
  'nanosleep',
  'poll',
  'pread',
  'pread64',
  'rand',
  'random',
  'sendfile64',
  'sendmsg',
  'snprintf',
  'sysconf',
  'sysctlbybame',
  'timespec_get',
  'tsearch',
  'twalk',
  'usleep',
  'waitpid',
  'writev',
]

foreach f : functions
  if cc.has_function(f)
    cdata.set('HAVE_@0@'.format(f.to_upper()), 1)
  endif
endforeach

foreach s : ['size_t', 'unsigned int', 'unsigned long long']
  cdata.set('SIZEOF_@0@'.format(s.underscorify().to_upper()), cc.sizeof(s))
endforeach

if host_machine.system() == 'windows'
  # `timevale.tv_sec` is `long` on Windows
  # See https://learn.microsoft.com/en-us/windows/win32/api/winsock/ns-winsock-timeval
  cdata.set('SIZEOF_STRUCT_TIMEVAL_TV_SEC', cc.sizeof('long'))
else
  cdata.set(
    'SIZEOF_STRUCT_TIMEVAL_TV_SEC',
    cc.sizeof(
      'time_t',
      prefix: '#include <time.h>',
    ),
  )
endif
cdata.set(
  'SIZEOF_UINT64_T',
  cc.sizeof(
    'uint64_t',
    prefix: '#include <stdint.h>',
  ),
)

cdata.set('HAVE_PIPE2_FUNC', cc.has_function('pipe2'))
cdata.set('MHD_HAVE___BUILTIN_BSWAP32', cc.has_function('__builtin_bswap32'))
cdata.set('MHD_HAVE___BUILTIN_BSWAP64', cc.has_function('__builtin_bswap64'))

if host_machine.system() == 'windows'
  cdata.set('HAVE_W32_GMTIME_S', cc.has_header_symbol('time.h', 'gmtime_s'))
else
  cdata.set('HAVE_GMTIME_R', cc.has_function('gmtime_r'))
endif

if cdata.has('HAVE_TSEARCH')
  cdata.set('HAVE_SEARCH_H', 1)
endif

if cdata.has('HAVE_GETSOCKNAME')
  cdata.set('MHD_USE_GETSOCKNAME', 1)
endif

if cdata.has('HAVE_EPOLL_CREATE1')
  cdata.set('EPOLL_SUPPORT', 1)
endif

cdata.set(host_machine.system().to_upper(), 1)
cdata.set_quoted(
  'MHD_PLUGIN_INSTALL_PREFIX',
  get_option('prefix') / get_option('libdir') / 'libmicrohttpd',
)

if host_machine.system() == 'windows'
  cdata.set('_MHD_ITC_SOCKETPAIR', 1)
elif cdata.has('HAVE_SYS_EVENTFD_H')
  cdata.set('_MHD_ITC_EVENTFD', 1)
else
  cdata.set('_MHD_ITC_PIPE', 1)
endif

if host_machine.system() == 'windows'
  net_dep = cc.find_library('ws2_32')
elif host_machine.system() == 'sunos'
  net_dep = cc.find_library('socket')
else
  net_dep = []
endif

if meson.version().version_compare('>= 0.62')
  dl_dep = dependency(
    'dl',
    required: false,
  )
else
  dl_dep = cc.find_library(
    'dl',
    required: false,
  )
endif
if dl_dep.found()
  cdata.set('HAVE_DLFCN_H', 1)
endif

threads_dep = dependency(
  '',
  required: false,
)
if host_machine.system() == 'windows'
  cdata.set('MHD_USE_W32_THREADS', 1)
else
  threads_dep = dependency(
    'threads',
    required: false,
  )
  if threads_dep.found()
    cdata.set('MHD_USE_POSIX_THREADS', 1)
  endif
endif

curl_dep = dependency(
  'libcurl',
  required: get_option('curl'),
)
if curl_dep.found()
  cdata.set('HAVE_LIBCURL', 1)
endif

gcrypt_dep = dependency(
  'libgcrypt',
  required: get_option('gcrypt'),
)
if gcrypt_dep.found()
  cdata.set('HAVE_GCRYPT_H', 1)
endif

gnutls_dep = dependency(
  'gnutls',
  required: get_option('gnutls'),
)
if gnutls_dep.found()
  cdata.set('HAVE_GNUTLS_GNUTLS_H', 1)
  cdata.set('HTTPS_SUPPORT', 1)
  cdata.set('UPGRADE_SUPPORT', 1)
endif

if cc.has_function_attribute('always_inline')
  cdata.set('_MHD_static_inline', 'static inline __attribute__((always_inline))')
else
  cdata.set('_MHD_static_inline', 'static inline')
endif

if cc.has_function_attribute('noreturn')
  if host_machine.system() == 'windows'
    cdata.set('_MHD_NORETURN', '__declspec(noreturn)')
  else
    cdata.set('_MHD_NORETURN', '__attribute__((noreturn))')
  endif
else
  cdata.set('_MHD_NORETURN', '')
endif

if cc.get_argument_syntax() == 'msvc' and get_option('default_library') != 'static'
  export_define = 'extern __declspec(dllexport)'
elif cc.has_argument('-fvisibility=hidden')
  export_define = 'extern __attribute__ ((visibility ("default")))'
else
  export_define = 'extern'
endif

cdata.set('_MHD_EXTERN', export_define)

cfile = configure_file(
  input: 'MHD_config.h.meson',
  output: 'MHD_config.h',
  configuration: cdata,
)

sources = files(
  'src/microhttpd/connection.c',
  'src/microhttpd/daemon.c',
  'src/microhttpd/internal.c',
  'src/microhttpd/memorypool.c',
  'src/microhttpd/mhd_compat.c',
  'src/microhttpd/mhd_itc.c',
  'src/microhttpd/mhd_mono_clock.c',
  'src/microhttpd/mhd_send.c',
  'src/microhttpd/mhd_sockets.c',
  'src/microhttpd/mhd_str.c',
  'src/microhttpd/reason_phrase.c',
  'src/microhttpd/response.c',
  'src/microhttpd/sysfdsetsize.c',
)

if gnutls_dep.found()
  sources += files('src/microhttpd/connection_https.c')
endif

if not cdata.has('HAVE_SEARCH_H')
  sources += files('src/microhttpd/tsearch.c')
endif

if host_machine.system() == 'windows' or threads_dep.found()
  sources += files('src/microhttpd/mhd_threads.c')
endif

libmicrohttpd = library(
  'microhttpd',
  sources,
  gnu_symbol_visibility: 'hidden',
  dependencies: [dl_dep, gnutls_dep, threads_dep, net_dep],
  include_directories: incdirs,
  install: true,
)

depinc = include_directories('.', 'src/include')
libmicrohttpd_dep = declare_dependency(
  include_directories: depinc,
  link_with: libmicrohttpd,
)
