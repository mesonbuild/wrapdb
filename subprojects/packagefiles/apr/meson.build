project(
  'apr',
  'c',
  license: 'Apache-2.0',
  meson_version: '>=1.3.0',
  version: '1.7.6',
)

tests_opt = get_option('tests').disable_auto_if(meson.is_subproject())
is_windows = host_machine.system() == 'windows'

cc = meson.get_compiler('c')

pkg = import('pkgconfig')

subdir('include')

cdata = configuration_data()
cdata.set('apr_name', 'apr-1')
cdata.set('apr_libname', 'libapr-1')
cdata.set('win32_winnt_str', '0x0600')
cdata.set('eolstr', '\\n')
cdata.set('proc_mutex_is_global', '0')
check_headers = [
  'pwd.h',
  'arpa/inet.h',
  'conio.h',
  'crypt.h',
  'ctype.h',
  'dirent.h',
  'errno.h',
  'fcntl.h',
  'io.h',
  'limits.h',
  'netdb.h',
  'net/if.h',
  'netinet/in.h',
  'netinet/sctp.h',
  'netinet/sctp_uio.h',
  'netinet/tcp.h',
  'netinet/sctp.h',
  'sys/sockio.h',
  'sys/select.h',
  'process.h',
  'pthread.h',
  'semaphore.h',
  'signal.h',
  'stdarg.h',
  'stddef.h',
  'stdio.h',
  'stdlib.h',
  'string.h',
  'strings.h',
  'inttypes.h',
  'sys/ioctl.h',
  'sys/sendfile.h',
  'sys/signal.h',
  'sys/socket.h',
  'sys/sockio.h',
  'sys/syslimits.h',
  'sys/stat.h',
  'sys/time.h',
  'sys/types.h',
  'sys/uio.h',
  'sys/un.h',
  'sys/wait.h',
  'time.h',
  'unistd.h',
  'windows.h',
  'winsock2.h',
  'sys/file.h',
]

foreach header : check_headers
  key = header.replace('/', '_').replace('.', '')
  cdata.set10(key, cc.has_header(header))
endforeach

cdata.set10('stdint', cc.has_header('stdint.h'))

is_darwin = host_machine.system() == 'darwin'

cdata.set10('havemmaptmp', not is_darwin)
cdata.set10('havemmapshm', not is_darwin)
cdata.set10('havemmapzero', not is_darwin)
cdata.set10('haveshmgetanon', false)
cdata.set10('haveshmget', is_darwin)
cdata.set10('havemmapanon', true)

cdata.set10('usemmaptmp', not is_darwin)
cdata.set10('usemmapshm', false)
cdata.set10('usemmapzero', not is_darwin)
cdata.set10('useshmgetanon', false)
cdata.set10('useshmget', is_darwin)
cdata.set10('usemmapanon', true)

cdata.set10('havebeosarea', false)
cdata.set10('usebeosarea', false)

cdata.set10('sysvser', false)
cdata.set10('procpthreadser', false)
cdata.set10('hasprocpthreadser', false)

hasflockser = cc.has_header('sys/file.h') and cc.has_define(
  'LOCK_EX',
  prefix: '#include <sys/file.h>',
)
cdata.set10('hasflockser', hasflockser)
cdata.set10('flockser', hasflockser)
cdata.set10('hassysvser', false)

posixser = cc.has_function(
  'sem_open',
  prefix: '#include <semaphore.h>',
)
cdata.set10('hasposixser', posixser)
cdata.set10('posixser', posixser)

fcntlser = cc.has_define(
  'F_SETLK',
  prefix: '#include <fcntl.h>',
)
cdata.set10('hasfcntlser', fcntlser)
cdata.set10('fcntlser', fcntlser)

pthreadser = cc.has_function(
  'pthread_mutexattr_settype',
  prefix: '#include <pthread.h>',
)
cdata.set10('haspthreadser', pthreadser)
cdata.set10('pthreadser', pthreadser)

have_sockaddr_un = cc.has_type(
  'struct sockaddr_un',
  prefix: '#include <sys/types.h>\n#include <sys/un.h>',
)

cdata.set10('proclockglobal', false)
cdata.set10('have_corkable_tcp', false)
cdata.set10('have_getrlimit', false)
cdata.set10('have_in_addr', true)
cdata.set10('have_inet_addr', true)
cdata.set10('have_inet_network', true)
cdata.set10('have_sockaddr_un', have_sockaddr_un)
cdata.set10('have_memmove', true)
cdata.set10('have_setrlimit', true)
cdata.set10('have_sigaction', true)
cdata.set10('have_sigsuspend', true)
cdata.set10('have_sigwait', false)
cdata.set10('have_sa_storage', false)
cdata.set10('have_strcasecmp', true)
cdata.set10('have_strdup', true)
cdata.set10('have_stricmp', true)
cdata.set10('have_strncasecmp', true)
cdata.set10('have_strnicmp', true)
cdata.set10('have_strstr', true)
cdata.set10('have_memchr', true)
cdata.set10('struct_rlimit', false)
cdata.set10('have_sctp', false)
cdata.set10('sharedmem', true)
cdata.set10('threads', true)
cdata.set10('sendfile', true)
cdata.set10('mmap', true)
cdata.set10('fork', true)
cdata.set10('rand', true)
cdata.set10('oc', true)
cdata.set10('aprdso', true)
cdata.set10('acceptfilter', false)
cdata.set10('have_unicode_fs', false)
cdata.set10('have_proc_invoked', false)
cdata.set10('apr_has_user', true)
cdata.set10('aprlfs', false)
cdata.set10('apr_has_xthread_files', false)
cdata.set10('osuuid', true)
cdata.set10('apr_has_timedlocks', true)
cdata.set10('file_as_socket', true)
cdata.set10(
  'have_union_semun',
  cc.has_type(
    'union semun',
    prefix: '#include <sys/types.h>\n#include <sys/sem.h>',
  ),
)
cdata.set10(
  'have_iovec',
  cc.has_type(
    'struct iovec',
    prefix: '#include <sys/types.h>\n#include <sys/uio.h>',
  ),
)

cdata.set10('apr_charset_ebcdic', false)
cdata.set10('apr_procattr_user_set_requires_password', false)

cdata.set('apr_tcp_nopush_flag', 'TCP_CORK')
cdata.set('apr_thread_func', '')
cdata.set10('bigendian', host_machine.endian() == 'big')
cdata.set('ino_t_value', 'unsigned int')
cdata.set('int64_literal', '#define APR_INT64_C(val) INT64_C(val)')
cdata.set('int64_t_fmt', '#define APR_INT64_T_FMT PRId64')
cdata.set('int64_value', 'int64_t')
cdata.set('int_value', 'int')
cdata.set10('o_nonblock_inherited', false)
cdata.set('off_t_fmt', '#define APR_OFF_T_FMT APR_INT64_T_FMT')
cdata.set('off_t_value', 'off_t')
cdata.set('pid_t_fmt', '#define APR_PID_T_FMT "ld"')
cdata.set('shlibpath_var', '')
cdata.set('short_value', 'short')
cdata.set('size_t_fmt', '#define APR_SIZE_T_FMT "lu"')
cdata.set('size_t_value', 'size_t')
cdata.set('socklen_t_value', 'socklen_t')
cdata.set('ssize_t_fmt', '#define APR_SSIZE_T_FMT "ld"')
cdata.set('ssize_t_value', is_windows ? 'SSIZE_T' : 'ssize_t')
cdata.set10('tcp_nodelay_inherited', false)
cdata.set('uint64_literal', '#define APR_UINT64_C(val) UINT64_C(val)')
cdata.set('uint64_t_fmt', '#define APR_UINT64_T_FMT PRIu64')
cdata.set('uint64_t_hex_fmt', '#define APR_UINT64_T_HEX_FMT PRIx64')
cdata.set('uint64_value', 'uint64_t')
cdata.set('voidp_size', cc.sizeof('void*'))

cdata.set10('apr_have_ipv6_10', not is_windows)
cdata.set10('have_ipv6', not is_windows)

config = configure_file(
  input: is_windows ? 'include/apr.hwc' : 'include/apr.h.in',
  output: 'apr.h',
  configuration: cdata,
)

gen_test_char = executable(
  'gen_test_char',
  'tools/gen_test_char.c',
  native: true,
)

gen_char_table = custom_target(
  'gen_char_table',
  output: ['apr_escape_test_char.h'],
  command: [gen_test_char],
  capture: true,
)

apr_include_directories = include_directories(
  'include',
  'include/private',
)

apr_system_libs = [
  cc.find_library(
    'ws2_32',
    required: is_windows,
  ),
  cc.find_library(
    'rpcrt4',
    required: is_windows,
  ),
]

apr_sources = files(
  'encoding/apr_encode.c',
  'encoding/apr_escape.c',
  'strings/apr_cpystrn.c',
  'strings/apr_cstr.c',
  'strings/apr_fnmatch.c',
  'strings/apr_snprintf.c',
  'strings/apr_strings.c',
  'strings/apr_strnatcmp.c',
  'strings/apr_strtok.c',
  'tables/apr_hash.c',
  'tables/apr_skiplist.c',
  'tables/apr_tables.c',
)

apr_unix_sources = files(
  'atomic/unix/builtins.c',
  'atomic/unix/builtins64.c',
  'atomic/unix/mutex.c',
  'atomic/unix/mutex64.c',
  'dso/unix/dso.c',
  'file_io/unix/buffer.c',
  'file_io/unix/copy.c',
  'file_io/unix/dir.c',
  'file_io/unix/fileacc.c',
  'file_io/unix/filedup.c',
  'file_io/unix/filepath.c',
  'file_io/unix/filepath_util.c',
  'file_io/unix/filestat.c',
  'file_io/unix/flock.c',
  'file_io/unix/fullrw.c',
  'file_io/unix/mktemp.c',
  'file_io/unix/open.c',
  'file_io/unix/pipe.c',
  'file_io/unix/readwrite.c',
  'file_io/unix/seek.c',
  'file_io/unix/tempdir.c',
  'locks/unix/global_mutex.c',
  'locks/unix/proc_mutex.c',
  'locks/unix/thread_cond.c',
  'locks/unix/thread_mutex.c',
  'locks/unix/thread_rwlock.c',
  'memory/unix/apr_pools.c',
  'misc/unix/env.c',
  'misc/unix/errorcodes.c',
  'misc/unix/getopt.c',
  'misc/unix/otherchild.c',
  'misc/unix/rand.c',
  'misc/unix/start.c',
  'misc/unix/version.c',
  'mmap/unix/common.c',
  'mmap/unix/mmap.c',
  'network_io/unix/inet_ntop.c',
  'network_io/unix/inet_pton.c',
  'network_io/unix/multicast.c',
  'network_io/unix/sendrecv.c',
  'network_io/unix/sockaddr.c',
  'network_io/unix/socket_util.c',
  'network_io/unix/sockets.c',
  'network_io/unix/sockopt.c',
  'passwd/apr_getpass.c',
  'poll/unix/epoll.c',
  'poll/unix/poll.c',
  'poll/unix/pollcb.c',
  'poll/unix/pollcb.c',
  'poll/unix/pollset.c',
  'poll/unix/pollset.c',
  'poll/unix/select.c',
  'poll/unix/wakeup.c',
  'random/unix/apr_random.c',
  'random/unix/sha2.c',
  'random/unix/sha2_glue.c',
  'shmem/unix/shm.c',
  'support/unix/waitio.c',
  'threadproc/unix/proc.c',
  'threadproc/unix/procsup.c',
  'threadproc/unix/signals.c',
  'threadproc/unix/thread.c',
  'threadproc/unix/threadpriv.c',
  'time/unix/time.c',
  'time/unix/timestr.c',
  'user/unix/groupinfo.c',
  'user/unix/userinfo.c',
)

apr_win32_sources = files(
  'atomic/win32/apr_atomic.c',
  'atomic/win32/apr_atomic64.c',
  'dso/win32/dso.c',
  'file_io/unix/copy.c',
  'file_io/unix/fileacc.c',
  'file_io/unix/filepath_util.c',
  'file_io/unix/fullrw.c',
  'file_io/unix/mktemp.c',
  'file_io/unix/tempdir.c',
  'file_io/win32/buffer.c',
  'file_io/win32/dir.c',
  'file_io/win32/filedup.c',
  'file_io/win32/filepath.c',
  'file_io/win32/filestat.c',
  'file_io/win32/filesys.c',
  'file_io/win32/flock.c',
  'file_io/win32/open.c',
  'file_io/win32/pipe.c',
  'file_io/win32/readwrite.c',
  'file_io/win32/seek.c',
  'locks/win32/proc_mutex.c',
  'locks/win32/thread_cond.c',
  'locks/win32/thread_mutex.c',
  'locks/win32/thread_rwlock.c',
  'memory/unix/apr_pools.c',
  'misc/unix/errorcodes.c',
  'misc/unix/getopt.c',
  'misc/unix/otherchild.c',
  'misc/unix/version.c',
  'misc/win32/charset.c',
  'misc/win32/env.c',
  'misc/win32/internal.c',
  'misc/win32/misc.c',
  'misc/win32/rand.c',
  'misc/win32/rand.c',
  'misc/win32/start.c',
  'misc/win32/utf8.c',
  'mmap/unix/common.c',
  'mmap/win32/mmap.c',
  'network_io/unix/inet_ntop.c',
  'network_io/unix/inet_pton.c',
  'network_io/unix/multicast.c',
  'network_io/unix/sockaddr.c',
  'network_io/unix/sockaddr.c',
  'network_io/unix/socket_util.c',
  'network_io/win32/sendrecv.c',
  'network_io/win32/sockets.c',
  'network_io/win32/sockopt.c',
  'poll/unix/poll.c',
  'poll/unix/pollcb.c',
  'poll/unix/pollset.c',
  'poll/unix/select.c',
  'poll/unix/wakeup.c',
  'random/unix/apr_random.c',
  'random/unix/sha2.c',
  'random/unix/sha2_glue.c',
  'shmem/win32/shm.c',
  'threadproc/win32/proc.c',
  'threadproc/win32/signals.c',
  'threadproc/win32/thread.c',
  'threadproc/win32/threadpriv.c',
  'time/win32/time.c',
  'time/win32/timestr.c',
  'user/win32/groupinfo.c',
  'user/win32/userinfo.c',
)

inc = [apr_include_directories]

if host_machine.system() == 'windows'
  arch_sources = apr_win32_sources
  inc_private = include_directories('include/arch/win32', 'include/arch/unix')
else
  # Assume everything else is unix-like for now
  arch_sources = apr_unix_sources
  inc_private = include_directories('include/arch/unix')
endif

apr_c_args = []
if host_machine.system() == 'windows'
  apr_c_args += ['-DWIN32']
endif

libapr = library(
  'apr-1',
  apr_sources + arch_sources,
  gen_char_table,
  c_args: apr_c_args + ['-DAPR_DECLARE_EXPORT'],
  include_directories: [inc, inc_private],
  dependencies: apr_system_libs,
  version: meson.project_version(),
  install: true,
)

apr_dep = declare_dependency(
  include_directories: include_directories('include'),
  link_with: libapr,
  compile_args: ['-DAPR_DECLARE_IMPORT'],
)

meson.override_dependency('apr', apr_dep)

pkg.generate(
  libapr,
  name: 'apr',
  url: 'https://apr.apache.org',
)

if tests_opt.allowed()
  testsuites = [
    'testutil',
    'testargs',
    'testatomic',
    'testcond',
    'testdir',
    'testdup',
    'testencode',
    'testenv',
    'testescape',
    'testfile',
    'testfilecopy',
    'testfileinfo',
    'testfmt',
    'testfnmatch',
    'testglobalmutex',
    'testhash',
    'testipsub',
    'testlfs',
    'testlock',
    'testmmap',
    'testnames',
    'testpath',
    'testpoll',
    'testpools',
    'testprocmutex',
    'testrand',
    'testskiplist',
    'testsleep',
    'testsockets',
    'testsockopt',
    'teststr',
    'teststrnatcmp',
    'testtable',
    'testtemp',
    'testthread',
    'testtime',
    'testud',
    'testutil',
    'testvsn',
  ]

  if not is_windows
    # newer versions of windows return user SIDs from TokenPrimaryGroup which
    # apr doesn't know how to handle
    testsuites += ['testuser']
  endif

  abts_src = files(
    'test/testflock.c',
    'test/testoc.c',
    'test/testpipe.c',
    'test/testproc.c',
    'test/testshm.c',
    'test/testsock.c',
    'test/testuser.c',
  )
  foreach suite : testsuites
    abts_src += files('test' / (suite + '.c'))
  endforeach

  # Slightly silly workaround for this test, it expects mod_test.so to be in a folder called .libs
  # relative to itself. meson doesn't really give control over file layout like that, so pretend to
  # be BeOS which they hardcoded a better path for :^)
  dso_c_args = []
  if host_machine.system() == 'linux'
    dso_c_args += ['-DBEOS', '-DLIB_NAME="libmod_test.so"']
  endif
  dso_test = static_library(
    'abts_dsotest',
    'test/testdso.c',
    dependencies: apr_dep,
    include_directories: inc_private,
    build_by_default: false,
    c_args: dso_c_args,
  )

  mod_test = shared_module(
    'libmod_test',
    'test/mod_test.c',
    include_directories: apr_include_directories,
    dependencies: [apr_dep],
    build_by_default: false,
    name_prefix: '',
  )

  # the test expects this to have a .so suffix even on macos
  mod_test_lib = shared_module(
    'mod_test',
    'test/mod_test.c',
    include_directories: apr_include_directories,
    dependencies: [apr_dep],
    build_by_default: false,
    name_prefix: '',
    name_suffix: host_machine.system() == 'windows' ? 'dll' : 'so',
  )

  testshmproducer = executable(
    'testshmproducer',
    'test/testshmproducer.c',
    include_directories: apr_include_directories,
    dependencies: [apr_dep],
    build_by_default: false,
  )

  testshmconsumer = executable(
    'testshmconsumer',
    'test/testshmconsumer.c',
    include_directories: apr_include_directories,
    dependencies: [apr_dep],
    build_by_default: false,
  )

  proc_child = executable(
    'proc_child',
    'test/proc_child.c',
    include_directories: apr_include_directories,
    dependencies: [apr_dep],
    build_by_default: false,
  )

  tryread = executable(
    'tryread',
    'test/tryread.c',
    include_directories: apr_include_directories,
    dependencies: [apr_dep],
    build_by_default: false,
  )

  sockchild = executable(
    'sockchild',
    'test/sockchild.c',
    include_directories: apr_include_directories,
    dependencies: [apr_dep],
    build_by_default: false,
  )

  readchild = executable(
    'readchild',
    'test/readchild.c',
    include_directories: apr_include_directories,
    dependencies: [apr_dep],
    build_by_default: false,
  )

  abts = executable(
    'abts',
    'test/abts.c',
    abts_src,
    link_with: dso_test,
    dependencies: [apr_dep, apr_system_libs],
    include_directories: inc_private,
    c_args: apr_c_args,
    build_by_default: false,
  )

  subdir('data')

  is_glibc = cc.has_header('features.h') and cc.has_define(
    '__GLIBC__',
    prefix: '#include <features.h>',
  )

  # musl doesn't perform strict unloading of symbols, so skip this test
  if is_glibc
    test(
      'testdso',
      abts,
      args: ['testdso', '-v'],
      workdir: meson.current_build_dir(),
      depends: [mod_test, mod_test_lib],
    )
  endif

  if not is_windows
    test(
      'testshm',
      abts,
      args: ['testshm', '-v'],
      workdir: meson.current_build_dir(),
      timeout: 3000,
      depends: [testshmproducer, testshmconsumer],
    )
  endif

  test(
    'testproc',
    abts,
    args: ['testproc', '-v'],
    workdir: meson.current_build_dir(),
    timeout: 3000,
    depends: [proc_child],
  )

  test(
    'testsock',
    abts,
    args: ['testsock', '-v'],
    workdir: meson.current_build_dir(),
    timeout: 3000,
    depends: [sockchild],
  )

  test(
    'testflock',
    abts,
    args: ['testflock', '-v'],
    workdir: meson.current_build_dir(),
    timeout: 3000,
    depends: [tryread],
  )

  test(
    'testpipe',
    abts,
    args: ['testpipe', '-v'],
    workdir: meson.current_build_dir(),
    timeout: 3000,
    depends: [readchild],
  )

  # Tests the whole kitchen sink, takes a while to run
  foreach suite : testsuites
    test(
      suite,
      abts,
      args: [suite, '-v'],
      workdir: meson.current_source_dir() / 'test',
      timeout: 3000,
    )
  endforeach

  globalmutexchild = executable(
    'globalmutexchild',
    'test/globalmutexchild.c',
    include_directories: apr_include_directories,
    dependencies: [apr_dep],
    build_by_default: false,
  )

  occhild = executable(
    'occhild',
    'test/occhild.c',
    include_directories: apr_include_directories,
    dependencies: [apr_dep],
    build_by_default: false,
  )

  test(
    'testoc',
    abts,
    args: ['testoc', '-v'],
    workdir: meson.current_build_dir(),
    timeout: 3000,
    depends: [occhild],
  )

  testcases = [
    'test/testlockperf.c',
    'test/testapp.c',
    'test/testmutexscope.c',
  ]

  foreach src : testcases
    parts = src.split('/')
    test_name = parts[1].replace('.c', '')
    exe = executable(
      test_name,
      src,
      include_directories: apr_include_directories,
      dependencies: [apr_dep],
      build_by_default: false,
    )
    test(
      test_name,
      exe,
      workdir: meson.current_source_dir() / 'test',
      timeout: 3000,
    )
  endforeach

  sendfile_exe = executable(
    'sendfile',
    'test/sendfile.c',
    include_directories: apr_include_directories,
    dependencies: [apr_dep],
    build_by_default: false,
  )

  # These tests all use the same file names, so cannot be run in parallel
  test(
    'sendfile-blocking',
    sendfile_exe,
    args: ['client', 'blocking', 'startserver'],
    workdir: meson.current_build_dir(),
    is_parallel: false,
  )
  test(
    'sendfile-nonblocking',
    sendfile_exe,
    args: ['client', 'nonblocking', 'startserver'],
    workdir: meson.current_build_dir(),
    is_parallel: false,
  )
  test(
    'sendfile-timeout',
    sendfile_exe,
    args: ['client', 'timeout', 'startserver'],
    workdir: meson.current_build_dir(),
    is_parallel: false,
  )
endif
