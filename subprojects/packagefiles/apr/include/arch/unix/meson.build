private_cdata = configuration_data()

private_cdata.set('HAVE_DIRENT_H', cc.has_header('dirent.h'))
private_cdata.set('APR_OFF_T_STRFN', 'apr_strtoi64')
private_cdata.set('HAVE_NET_IF_H', cc.has_header('net/if.h'))
private_cdata.set('HAVE_SYS_STAT_H', cc.has_header('sys/stat.h'))
private_cdata.set('HAVE_PWD_H', cc.has_header('pwd.h'))
private_cdata.set('HAVE_GRP_H', cc.has_header('grp.h'))
private_cdata.set('HAVE_FCNTL_H', cc.has_header('fcntl.h'))
private_cdata.set('HAVE_SYS_MMAN_H', cc.has_header('sys/mman.h'))
private_cdata.set('HAVE_SYS_IPC_H', cc.has_header('sys/ipc.h'))
private_cdata.set('HAVE_SYS_SHM_H', cc.has_header('sys/shm.h'))
private_cdata.set('HAVE_SYS_MUTEX_H', cc.has_header('sys/mutex.h'))
private_cdata.set('HAVE_SEM_H', cc.has_header('sem.h'))
private_cdata.set('HAVE_SYS_SEM_H', cc.has_header('sys/sem.h'))
private_cdata.set('HAVE_SYS_FILE_H', cc.has_header('sys/file.h'))
private_cdata.set('HAVE_STDLIB_H', cc.has_header('stdlib.h'))
private_cdata.set(
  'HAVE_WRITEV',
  cc.has_function(
    'writev',
    prefix: '#include <sys/uio.h>',
  ),
)
private_cdata.set('HAVE_STDDEF_H', cc.has_header('stddef.h'))
private_cdata.set(
  'HAVE_PTHREAD_MUTEX_RECURSIVE',
  cc.sizeof(
    'PTHREAD_MUTEX_RECURSIVE',
    prefix: '#include <pthread.h>',
  ) != -1,
)
private_cdata.set(
  'HAVE_PTHREAD_RWLOCKS',
  cc.sizeof(
    'pthread_rwlock_t',
    prefix: '#include <sys/types.h>\n#include <pthread.h>',
  ) != -1,
)

have_dlfcn = cc.has_function(
  'dlopen',
  prefix: '#include <dlfcn.h>',
)
have_shl = cc.has_function(
  'shl_load',
  prefix: '#include <shl.h>',
)
have_dyld = cc.has_header('<mach-o/dyld.h>')

private_cdata.set('DSO_USE_DLFCN', have_dlfcn)
private_cdata.set('HAVE_DLFCN_H', have_dlfcn)

private_cdata.set('DSO_USE_SHL', have_shl)
private_cdata.set('HAVE_SHL_H', have_shl)

private_cdata.set('DSO_USE_DYLD', have_dyld)
private_cdata.set('HAVE_MACH_O_DYLD_H', have_dyld)

private_cdata.set('HAVE_UUID_H', cc.has_header('uuid.h'))
private_cdata.set('HAVE_UUID_UUID_H', cc.has_header('uuid/uuid.h'))
private_cdata.set('HAVE_SYS_UUID_H', cc.has_header('sys/uuid.h'))
private_cdata.set('HAVE_SYS_RANDOM_H', cc.has_header('sys/random.h'))
private_cdata.set(
  'HAVE_ARC4RANDOM',
  cc.has_function(
    'arc4random',
    prefix: '#include <stdlib.h>',
  ),
)
private_cdata.set(
  'HAVE_ARC4RANDOM_BUF',
  cc.has_function(
    'arc4random_buf',
    prefix: '#include <stdlib.h>',
  ),
)
private_cdata.set(
  'HAVE_GETRANDOM',
  cc.has_function(
    'getrandom',
    prefix: '#include <sys/random.h>',
  ),
)
private_cdata.set('SYS_RANDOM', true)
private_cdata.set(
  'HAVE_UTIMES',
  cc.has_function(
    'utimes',
    prefix: '#include <sys/time.h>\n#include <sys/types.h>\n#include <unistd.h>',
  ),
)
private_cdata.set(
  'HAVE_UTIME',
  cc.has_function(
    'utime',
    prefix: '#include <utime.h>\n#include <sys/types.h>\n#include <unistd.h>',
  ),
)
private_cdata.set(
  'HAVE_STRUCT_IPMREQ',
  cc.has_type(
    'struct ip_mreq',
    prefix: '#include <netinet/in.h>\n#include <sys/types.h>',
  ),
)
private_cdata.set(
  'HAVE_GETIFADDRS',
  cc.has_function(
    'getifaddrs',
    prefix: '#include <ifaddrs.h>\n#include <sys/types.h>',
  ),
)
private_cdata.set10(
  'HAVE_WAITPID',
  cc.has_function(
    'waitpid',
    prefix: '#include <sys/types.h>\n#include <sys/wait.h>\n#include <unistd.h>',
  ),
)
private_cdata.set('HAVE_SYS_STAT_H', cc.has_header('sys/stat.h'))
private_cdata.set('HAVE_SYS_FCNTL_H', cc.has_header('sys/fcntl.h'))
private_cdata.set('HAVE_TIME_H', cc.has_header('time.h'))
private_cdata.set('HAVE_MALLOC_H', cc.has_header('malloc.h'))
private_cdata.set10('HAVE_POLL_H', cc.has_header('poll.h'))
private_cdata.set(
  'HAVE_POLL',
  cc.has_function(
    'poll',
    prefix: '#include <poll.h>\n#include <sys/types.h>',
  ),
)
private_cdata.set('HAVE_EPOLL', cc.has_header('sys/epoll.h'))
private_cdata.set(
  'HAVE_SENDFILE',
  cc.has_function(
    'sendfile',
    prefix: '#include <sys/sendfile.h>\n#include <sys/types.h>',
  ),
)
private_cdata.set(
  'HAVE_SENDFILE64',
  cc.has_function(
    'sendfile64',
    prefix: '#include <sys/sendfile.h>\n#include <sys/types.h>',
  ),
)

private_cdata.set(
  'HAVE_IF_INDEXTONAME',
  cc.has_function(
    'if_indextoname',
    prefix: '#include <net/if.h>\n#include <sys/types.h>',
  ),
)
private_cdata.set(
  'HAVE_IF_NAMETOINDEX',
  cc.has_function(
    'if_nametoindex',
    prefix: '#include <net/if.h>\n#include <sys/types.h>',
  ),
)
private_cdata.set(
  'HAVE_GAI_STRERROR',
  cc.has_function(
    'gai_strerror',
    prefix: '#include <netdb.h>\n#include <sys/types.h>',
  ),
)
private_cdata.set(
  'HAVE_GETADDRINFO',
  cc.has_function(
    'getaddrinfo',
    prefix: '#include <netdb.h>\n#include <sys/types.h>',
  ),
)

private_cdata.set(
  'HAVE_GETHOSTBYNAME_R',
  cc.has_function(
    'gethostbyname_r',
    prefix: '#include <netdb.h>\n#include <sys/types.h>',
  ),
)
private_cdata.set(
  'HAVE_GETHOSTBYADDR_R',
  cc.has_function(
    'gethostbyaddr_r',
    prefix: '#include <netdb.h>\n#include <sys/types.h>',
  ),
)
private_cdata.set(
  'HAVE_GETSERVBYNAME_R',
  cc.has_function(
    'getservbyname_r',
    prefix: '#include <netdb.h>\n#include <sys/types.h>',
  ),
)

private_cdata.set(
  'GETHOSTBYNAME_R_GLIBC2',
  cc.compiles(
    '''
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <stdlib.h>

int main() {
int tmp = gethostbyname_r((const char *) 0, (struct hostent *) 0,
                          (char *) 0, 0, (struct hostent **) 0, &tmp);
/* use tmp to suppress the warning */
tmp=0;
}
''',
  ),
)

private_cdata.set10('USE_ATOMICS_GENERIC', true)
private_cdata.set10('USE_ATOMICS_GENERIC64', true)

configure_file(
  output: 'apr_private_meson.h',
  configuration: private_cdata,
)
