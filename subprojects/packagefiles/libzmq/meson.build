project('libzmq', ['cpp', 'c'],
    version: '4.3.5',
    license: 'LGPL-3.0-or-later',
)

cc = meson.get_compiler('c')
thread_dep = dependency('threads')

libzmq_inc_private = include_directories('src', 'external/wepoll')
libzmq_inc_public = include_directories('include')

libzmq_deps_private = [thread_dep]
libzmq_deps_public = []

libzmq_flags_private = ['-D_REENTRANT', '-D_THREAD_SAFE', '-DZMQ_CUSTOM_PLATFORM_HPP']
libzmq_flags_public = []

libzmq_src = files(
    'src/precompiled.cpp',
    'src/address.cpp',
    'src/channel.cpp',
    'src/client.cpp',
    'src/clock.cpp',
    'src/ctx.cpp',
    'src/curve_mechanism_base.cpp',
    'src/curve_client.cpp',
    'src/curve_server.cpp',
    'src/dealer.cpp',
    'src/devpoll.cpp',
    'src/dgram.cpp',
    'src/dist.cpp',
    'src/endpoint.cpp',
    'src/epoll.cpp',
    'src/err.cpp',
    'src/fq.cpp',
    'src/io_object.cpp',
    'src/io_thread.cpp',
    'src/ip.cpp',
    'src/ipc_address.cpp',
    'src/ipc_connecter.cpp',
    'src/ipc_listener.cpp',
    'src/kqueue.cpp',
    'src/lb.cpp',
    'src/mailbox.cpp',
    'src/mailbox_safe.cpp',
    'src/mechanism.cpp',
    'src/mechanism_base.cpp',
    'src/metadata.cpp',
    'src/msg.cpp',
    'src/mtrie.cpp',
    'src/norm_engine.cpp',
    'src/object.cpp',
    'src/options.cpp',
    'src/own.cpp',
    'src/null_mechanism.cpp',
    'src/pair.cpp',
    'src/peer.cpp',
    'src/pgm_receiver.cpp',
    'src/pgm_sender.cpp',
    'src/pgm_socket.cpp',
    'src/pipe.cpp',
    'src/plain_client.cpp',
    'src/plain_server.cpp',
    'src/poll.cpp',
    'src/poller_base.cpp',
    'src/polling_util.cpp',
    'src/pollset.cpp',
    'src/proxy.cpp',
    'src/pub.cpp',
    'src/pull.cpp',
    'src/push.cpp',
    'src/random.cpp',
    'src/raw_encoder.cpp',
    'src/raw_decoder.cpp',
    'src/raw_engine.cpp',
    'src/reaper.cpp',
    'src/rep.cpp',
    'src/req.cpp',
    'src/router.cpp',
    'src/select.cpp',
    'src/server.cpp',
    'src/session_base.cpp',
    'src/signaler.cpp',
    'src/socket_base.cpp',
    'src/socks.cpp',
    'src/socks_connecter.cpp',
    'src/stream.cpp',
    'src/stream_connecter_base.cpp',
    'src/stream_engine_base.cpp',
    'src/stream_listener_base.cpp',
    'src/sub.cpp',
    'src/tcp.cpp',
    'src/tcp_address.cpp',
    'src/tcp_connecter.cpp',
    'src/tcp_listener.cpp',
    'src/thread.cpp',
    'src/trie.cpp',
    'src/radix_tree.cpp',
    'src/v1_decoder.cpp',
    'src/v1_encoder.cpp',
    'src/v2_decoder.cpp',
    'src/v2_encoder.cpp',
    'src/v3_1_encoder.cpp',
    'src/xpub.cpp',
    'src/xsub.cpp',
    'src/zmq.cpp',
    'src/zmq_utils.cpp',
    'src/decoder_allocators.cpp',
    'src/socket_poller.cpp',
    'src/timers.cpp',
    'src/radio.cpp',
    'src/dish.cpp',
    'src/udp_engine.cpp',
    'src/udp_address.cpp',
    'src/scatter.cpp',
    'src/gather.cpp',
    'src/ip_resolver.cpp',
    'src/zap_client.cpp',
    'src/zmtp_engine.cpp',
)

libzmq_src_ws = files(
    'src/ws_address.cpp',
    'src/ws_connecter.cpp',
    'src/ws_decoder.cpp',
    'src/ws_encoder.cpp',
    'src/ws_engine.cpp',
    'src/ws_listener.cpp',
)

libzmq_src_wss = files(
    'src/wss_address.cpp',
    'src/wss_engine.cpp',
)

libzmq_src_tipc = files(
    'src/tipc_address.cpp',
    'src/tipc_connecter.cpp',
    'src/tipc_listener.cpp',
)

# for platform.hpp.in
conf_data = configuration_data()

# ZMQ_BUILD_DRAFT_API
drafts = get_option('drafts')
if drafts
    conf_data.set('ZMQ_BUILD_DRAFT_API', true)
    libzmq_flags_public += '-DZMQ_BUILD_DRAFT_API'
endif

# ZMQ_USE_RADIX_TREE
radix_tree = get_option('radix_tree').enabled()
if drafts and get_option('radix_tree').auto()
    radix_tree = true
endif
conf_data.set('ZMQ_USE_RADIX_TREE', radix_tree)

# ZMQ_HAVE_WS
websockets = get_option('websockets').enabled()
if drafts and get_option('websockets').auto()
    websockets = true
endif
if websockets
    libzmq_src += libzmq_src_ws
endif
conf_data.set('ZMQ_HAVE_WS', websockets)

# ZMQ_USE_GNUTLS and ZMQ_HAVE_WSS
gnutls_dep = dependency('gnutls', required: get_option('tls'))
if websockets and gnutls_dep.found()
    libzmq_src += libzmq_src_wss
    libzmq_deps_private += gnutls_dep
    conf_data.set('ZMQ_USE_GNUTLS', true)
    conf_data.set('ZMQ_HAVE_WSS', true)
endif

# ZMQ_USE_NSS and ZMQ_USE_BUILTIN_SHA1
if not gnutls_dep.found()
    nss_dep = dependency('nss', required: get_option('nss'))
    if nss_dep.found()
        libzmq_deps_private += nss_dep
        conf_data.set('ZMQ_USE_NSS', true)
    else
        libzmq_src += files('external/sha1/sha1.c')
        conf_data.set('ZMQ_USE_BUILTIN_SHA1', true)
    endif
endif

# ZMQ_HAVE_LIBBSD
libbsd_dep = dependency('libbsd', required: get_option('libbsd'))
if libbsd_dep.found()
    libzmq_deps_private += libbsd_dep
    conf_data.set('ZMQ_HAVE_LIBBSD', true)
endif

# ZMQ_HAVE_STRLCPY
conf_data.set('ZMQ_HAVE_STRLCPY', cc.has_header_symbol('string.h', 'strlcpy'))

# ZMQ_HAVE_CURVE
curve = get_option('curve')

# ZMQ_USE_LIBSODIUM and ZMQ_LIBSODIUM_RANDOMBYTES_CLOSE
if curve
    libsodium_dep = dependency('libsodium', required: get_option('libsodium'))
    if libsodium_dep.found()
        libzmq_deps_private += libsodium_dep
        conf_data.set('ZMQ_USE_LIBSODIUM', true)
        conf_data.set('ZMQ_HAVE_CURVE', curve)
        if get_option('libsodium_randombytes_close')
            conf_data.set('ZMQ_LIBSODIUM_RANDOMBYTES_CLOSE', true)
        endif
    endif
endif

# Check for poller options
have_kqueue = cc.has_header_symbol('sys/event.h', 'kqueue')
have_epoll = cc.has_header_symbol('sys/epoll.h', 'epoll_create')
have_epoll_cloexec = cc.has_header_symbol('sys/epoll.h', 'epoll_create1')
have_devpoll = cc.has_header('sys/devpoll.h')
have_pollset = cc.has_header_symbol('sys/pollset.h', 'pollset_create')
have_poll = cc.has_header_symbol('poll.h', 'poll')
have_select = cc.has_header_symbol('sys/select.h', 'select')
have_ppoll = cc.has_header_symbol('sys/select.h', 'pselect')

# On Windows: epoll and select are available
if build_machine.system() == 'windows'
    have_epoll = true
    have_select = true
endif

# Auto deduce / set poller
poller = get_option('poller')
# kqueue
if (poller == 'auto' or poller == 'kqueue') and have_kqueue
    poller = 'kqueue'
    conf_data.set('ZMQ_IOTHREAD_POLLER_USE_KQUEUE', true)
endif
# epoll
if (poller == 'auto' or poller == 'epoll') and have_epoll
    poller = 'epoll'
    conf_data.set('ZMQ_IOTHREAD_POLLER_USE_EPOLL', true)
    if have_epoll_cloexec
        conf_data.set('ZMQ_IOTHREAD_POLLER_USE_EPOLL_CLOEXEC', true)
    endif
endif
# devpoll
if (poller == 'auto' or poller == 'devpoll') and have_devpoll
    poller = 'devpoll'
    conf_data.set('ZMQ_IOTHREAD_POLLER_USE_DEVPOLL', true)
endif
# pollset
if (poller == 'auto' or poller == 'pollset') and have_pollset
    poller = 'pollset'
    conf_data.set('ZMQ_IOTHREAD_POLLER_USE_POLLSET', true)
endif
# poll
if (poller == 'auto' or poller == 'poll') and have_poll
    poller = 'poll'
    conf_data.set('ZMQ_IOTHREAD_POLLER_USE_POLL', true)
endif
# select
if (poller == 'auto' or poller == 'select') and have_select
    poller = 'select'
    conf_data.set('ZMQ_IOTHREAD_POLLER_USE_SELECT', true)
endif

# On Windows: if epoll then add wepoll.c
if build_machine.system() == 'windows' and poller == 'epoll'
    libzmq_src += files('external/wepoll/wepoll.c')
endif

# Auto deduce / set api_poller
api_poller = get_option('api_poller')
if api_poller == 'auto'
    if poller == 'select'
        api_poller = 'select'
    else
        api_poller = 'poll'
    endif
endif
if api_poller == 'select'
    conf_data.set('ZMQ_POLL_BASED_ON_SELECT', true)
else
    conf_data.set('ZMQ_POLL_BASED_ON_POLL', true)
endif

# ZMQ_HAVE_PPOLL
if have_ppoll
    conf_data.set('ZMQ_HAVE_PPOLL', true)
endif

# ZMQ_CACHELINE_SIZE
cachline_size = 64
getconf = find_program('getconf', required: false)
if getconf.found()
    cachline_size_r = run_command(getconf, 'LEVEL1_DCACHE_LINESIZE', check: false)
    if cachline_size_r.returncode() == 0
        cachline_size = cachline_size_r.stdout().to_int()
    endif
endif
conf_data.set('ZMQ_CACHELINE_SIZE', cachline_size)

# HAVE_POSIX_MEMALIGN
have_posix_memalign = cc.has_header_symbol('stdlib.h', 'posix_memalign')
if have_posix_memalign
    conf_data.set('HAVE_POSIX_MEMALIGN', true)
endif

# ZMQ_HAVE_WINDOWS
conf_data.set('ZMQ_HAVE_WINDOWS', cc.has_header('windows.h'))

# some windows specific flags
if build_machine.system() == 'windows'
    libzmq_flags_private += ['-DFD_SETSIZE=16384', '-D_CRT_SECURE_NO_WARNINGS', '-D_WINSOCK_DEPRECATED_NO_WARNINGS']
endif

# ZMQ_HAVE_IPC
zmq_have_ipc = true
if build_machine.system() == 'windows'
    zmq_have_ipc = cc.has_header('winsock2.h') and cc.has_header('afunix.h') and poller == 'epoll'
endif
conf_data.set('ZMQ_HAVE_IPC', zmq_have_ipc)
conf_data.set('ZMQ_HAVE_STRUCT_SOCKADDR_UN', zmq_have_ipc)

# ZMQ_USE_CV_IMPL
# We don't check, C++11 compiler support is good enough these days
conf_data.set('ZMQ_USE_CV_IMPL_STL11', true)

# Misc
conf_data.set('ZMQ_HAVE_IFADDRS', cc.has_header('ifaddrs.h'))
conf_data.set('ZMQ_HAVE_UIO', cc.has_header('sys/uio.h'))
conf_data.set('ZMQ_HAVE_EVENTFD', cc.has_header('sys/eventfd.h'))
conf_data.set('ZMQ_HAVE_EVENTFD_CLOEXEC', cc.has_header_symbol('sys/eventfd.h', 'EFD_CLOEXEC'))
conf_data.set('HAVE_IF_NAMETOINDEX', cc.has_header_symbol('net/if.h', 'if_nametoindex'))
conf_data.set('ZMQ_HAVE_SO_PEERCRED', cc.has_header_symbol('sys/socket.h', 'SO_PEERCRED'))
conf_data.set('ZMQ_HAVE_LOCAL_PEERCRED', cc.has_header_symbol('sys/socket.h', 'LOCAL_PEERCRED'))
conf_data.set('ZMQ_HAVE_BUSY_POLL', cc.has_header_symbol('sys/socket.h', 'SO_BUSY_POLL'))
conf_data.set('HAVE_CLOCK_GETTIME', cc.has_header_symbol('time.h', 'clock_gettime'))
conf_data.set('HAVE_FORK', cc.has_header_symbol('unistd.h', 'fork'))
conf_data.set('HAVE_GETHRTIME', cc.has_header_symbol('sys/time.h', 'gethrtime'))
conf_data.set('HAVE_MKDTEMP', cc.has_header_symbol('stdlib.h', 'mkdtemp'))
conf_data.set('HAVE_ACCEPT4', cc.has_header_symbol('sys/socket.h', 'accept4'))
conf_data.set('HAVE_STRNLEN', cc.has_header_symbol('string.h', 'strnlen'))

# TODO: always required?
rt_dep = cc.find_library('rt', required: false)
if rt_dep.found()
    libzmq_deps_private += rt_dep
endif

# FIXME: BSD etc
libzmq_flags_private += '-D_GNU_SOURCE'

# Checking whether noexcept is supported
zmq_check_noexcept = cc.compiles('''
struct X {
    X(int i) noexcept {}
};
int main(int argc, char *argv []) {
    X x(5);
    return 0;
}
''')
conf_data.set('ZMQ_HAVE_NOEXCEPT', zmq_check_noexcept)
# Checking pthread_setname signature
zmq_check_pthread_setname_1  = cc.compiles('''
#include <pthread.h>
int main(int argc, char *argv []) {
    pthread_setname_np ("foo");
    return 0;
}
''', args: ['-D_GNU_SOURCE', '-pthread'])
conf_data.set('ZMQ_HAVE_PTHREAD_SETNAME_1', zmq_check_pthread_setname_1)
zmq_check_pthread_setname_2  = cc.compiles('''
#include <pthread.h>
int main(int argc, char *argv []) {
    pthread_setname_np (pthread_self(), "foo");
    return 0;
}
''', args: ['-D_GNU_SOURCE', '-pthread'])
conf_data.set('ZMQ_HAVE_PTHREAD_SETNAME_2', zmq_check_pthread_setname_2)
zmq_check_pthread_setname_3  = cc.compiles('''
#include <pthread.h>
int main(int argc, char *argv []) {
    pthread_setname_np (pthread_self(), "foo", (void *)0);
    return 0;
}
''', args: ['-D_GNU_SOURCE', '-pthread'])
conf_data.set('ZMQ_HAVE_PTHREAD_SETNAME_3', zmq_check_pthread_setname_3)
zmq_check_pthread_set_name  = cc.compiles('''
#include <pthread.h>
int main(int argc, char *argv []) {
    pthread_set_name_np (pthread_self(), "foo");
    return 0;
}
''', args: ['-D_GNU_SOURCE', '-pthread'])
conf_data.set('ZMQ_HAVE_PTHREAD_SET_NAME', zmq_check_pthread_set_name)
# Checking pthread_setaffinity signature
zmq_check_pthread_setaffinity  = cc.compiles('''
#include <pthread.h>
int main(int argc, char *argv []) {
    cpu_set_t test;
    pthread_setaffinity_np (pthread_self(), sizeof(cpu_set_t), &test);
    return 0;
}
''', args: ['-D_GNU_SOURCE', '-pthread'])
conf_data.set('ZMQ_HAVE_PTHREAD_SET_AFFINITY', zmq_check_pthread_setaffinity)
# Checking whether SOCK_CLOEXEC is supported
conf_data.set('ZMQ_HAVE_SOCK_CLOEXEC', cc.has_header_symbol('sys/socket.h', 'SOCK_CLOEXEC'))
# Checking whether O_CLOEXEC is supported
conf_data.set('ZMQ_HAVE_O_CLOEXEC', cc.has_header_symbol('fcntl.h', 'O_CLOEXEC'))
# Checking whether SO_BINDTODEVICE is supported
conf_data.set('ZMQ_HAVE_SO_BINDTODEVICE', cc.has_header_symbol('sys/socket.h', 'SO_BINDTODEVICE'))
# Checking whether SO_KEEPALIVE is supported
conf_data.set('ZMQ_HAVE_SO_KEEPALIVE', cc.has_header_symbol('sys/socket.h', 'SO_KEEPALIVE'))
# Checking whether SO_PRIORITY is supported
conf_data.set('ZMQ_HAVE_SO_PRIORITY', cc.has_header_symbol('sys/socket.h', 'SO_PRIORITY'))
# Checking whether TCP_KEEPCNT is supported
conf_data.set('ZMQ_HAVE_TCP_KEEPCNT', cc.has_header_symbol('netinet/tcp.h', 'TCP_KEEPCNT'))
# Checking whether TCP_KEEPIDLE is supported
conf_data.set('ZMQ_HAVE_TCP_KEEPIDLE', cc.has_header_symbol('netinet/tcp.h', 'TCP_KEEPIDLE'))
# Checking whether TCP_KEEPINTVL is supported
conf_data.set('ZMQ_HAVE_TCP_KEEPINTVL', cc.has_header_symbol('netinet/tcp.h', 'TCP_KEEPINTVL'))
# Checking whether TCP_KEEPALIVE is supported
conf_data.set('ZMQ_HAVE_TCP_KEEPALIVE', cc.has_header_symbol('netinet/tcp.h', 'TCP_KEEPALIVE'))
# Checking whether TIPC is supported
zmq_check_tcp_tipc  = cc.compiles('''
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <errno.h>
#include <sys/socket.h>
#include <linux/tipc.h>
int main(int argc, char *argv []) {
    struct sockaddr_tipc topsrv;
    int sd = socket(AF_TIPC, SOCK_SEQPACKET, 0);
    memset(&topsrv, 0, sizeof(topsrv));
    topsrv.family = AF_TIPC;
    topsrv.addrtype = TIPC_ADDR_NAME;
    topsrv.addr.name.name.type = TIPC_TOP_SRV;
    topsrv.addr.name.name.instance = TIPC_TOP_SRV;
    fcntl(sd, F_SETFL, O_NONBLOCK);
}
''')
conf_data.set('ZMQ_HAVE_TIPC', zmq_check_tcp_tipc)
if zmq_check_tcp_tipc
    libzmq_src += libzmq_src_tipc
endif
# Checking whether getrandom is supported
zmq_check_getrandom = cc.compiles('''
#include <sys/random.h>
int main (int argc, char *argv []) {
    char buf[4];
    int rc = getrandom(buf, 4, 0);
    return rc == -1 ? 1 : 0;
}
''')
conf_data.set('ZMQ_HAVE_GETRANDOM', zmq_check_getrandom)

# ZMQ_HAVE_OPENPGM
pgm_dep = dependency('openpgm-5.3', required: get_option('openpgm'))
pgm = pgm_dep.found()
if pgm
    libzmq_deps_private += pgm_dep
    conf_data.set('ZMQ_HAVE_OPENPGM', true)
endif
# ZMQ_HAVE_NORM
norm_dep = dependency('norm', required: get_option('norm'))
norm = norm_dep.found()
if norm
    libzmq_deps_private += norm_dep
    conf_data.set('ZMQ_HAVE_NORM', true)
endif
# ZMQ_HAVE_VMCI
vmci_dep = dependency('vmci', required: get_option('vmci'))
vmci = vmci_dep.found()
if vmci
    libzmq_deps_private += vmci_dep
    conf_data.set('ZMQ_HAVE_VMCI', true)
endif


configure_file(
    input: 'builds/cmake/platform.hpp.in',
    configuration: conf_data,
    output: 'platform.hpp',
    format: 'cmake@',
)

libzmq_lib = library('libzmq',
    sources: libzmq_src,
    include_directories: [libzmq_inc_private, libzmq_inc_public],
    dependencies: [libzmq_deps_private, libzmq_deps_public],
    cpp_args: libzmq_flags_private,
    version: '5.2.5',
    soversion: 5,
    install: true,
)

libzmq_dep = declare_dependency(
    include_directories: libzmq_inc_public,
    link_with: libzmq_lib,
    compile_args: libzmq_flags_public,
    dependencies: libzmq_deps_public
)

summary({
    'drafts': drafts,
    'radix_tree': radix_tree,
    'websockets': websockets,
    'curve': curve,
    'poller': poller,
    'api_poller': api_poller,
    'cachline_size': cachline_size,
    'pgm': pgm,
    'norm': norm,
    'vmci': vmci,
    }, section: 'Build options')
