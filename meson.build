project('nng', 'c',
    version : '1.3.2',
    license : 'MIT',
    default_options : [])

cc = meson.get_compiler('c')

nng_src = files(
    'src/nng.c',

    'src/core/aio.c',
    'src/core/clock.c',
    'src/core/device.c',
    'src/core/dialer.c',
    'src/core/file.c',
    'src/core/idhash.c',
    'src/core/init.c',
    'src/core/list.c',
    'src/core/listener.c',
    'src/core/lmq.c',
    'src/core/message.c',
    'src/core/msgqueue.c',
    'src/core/options.c',
    'src/core/pollable.c',
    'src/core/panic.c',
    'src/core/pipe.c',
    'src/core/protocol.c',
    'src/core/reap.c',
    'src/core/socket.c',
    'src/core/stats.c',
    'src/core/stream.c',
    'src/core/strs.c',
    'src/core/taskq.c',
    'src/core/thread.c',
    'src/core/timer.c',
    'src/core/transport.c',
    'src/core/url.c',

    'src/compat/nanomsg/nn.c',
    'src/protocol/bus0/bus.c',
    'src/protocol/pair0/pair.c',
    'src/protocol/pair1/pair.c',
    'src/protocol/pair1/pair1_poly.c',
    'src/protocol/pipeline0/pull.c',
    'src/protocol/pipeline0/push.c',
    'src/protocol/pubsub0/pub.c',
    'src/protocol/pubsub0/sub.c',
    'src/protocol/pubsub0/xsub.c',
    'src/protocol/reqrep0/rep.c',
    'src/protocol/reqrep0/req.c',
    'src/protocol/reqrep0/xrep.c',
    'src/protocol/reqrep0/xreq.c',
    'src/protocol/survey0/respond.c',
    'src/protocol/survey0/survey.c',
    'src/protocol/survey0/xrespond.c',
    'src/protocol/survey0/xsurvey.c',
    'src/supplemental/base64/base64.c',
    'src/supplemental/http/http_chunk.c',
    'src/supplemental/http/http_client.c',
    'src/supplemental/http/http_conn.c',
    'src/supplemental/http/http_msg.c',
    'src/supplemental/http/http_public.c',
    'src/supplemental/http/http_server.c',
    'src/supplemental/sha1/sha1.c',
    'src/supplemental/tcp/tcp.c',
    # Do not build with TLS support (using mbedtls)
    #'src/supplemental/tls/mbedtls/tls.c',
    'src/supplemental/tls/tls_common.c',
    'src/supplemental/util/options.c',
    'src/supplemental/util/platform.c',
    # Not needed
    #'src/supplemental/websocket/stub.c',
    'src/supplemental/websocket/websocket.c',
    'src/transport/inproc/inproc.c',
    'src/transport/ipc/ipc.c',
    'src/transport/tcp/tcp.c',
    'src/transport/tls/tls.c',
    'src/transport/ws/websocket.c',

    # Do not build zerotier
    #'src/transport/zerotier/zerotier.c',
    #'src/transport/zerotier/zthash.c',
)

include_dirs = ['include', 'src']

if target_machine.system() == 'windows'
    nng_src += files(
        'src/platform/windows/win_clock.c',
        'src/platform/windows/win_debug.c',
        'src/platform/windows/win_file.c',
        'src/platform/windows/win_io.c',
        'src/platform/windows/win_ipcconn.c',
        'src/platform/windows/win_ipcdial.c',
        'src/platform/windows/win_ipclisten.c',
        'src/platform/windows/win_pipe.c',
        'src/platform/windows/win_rand.c',
        'src/platform/windows/win_resolv.c',
        'src/platform/windows/win_sockaddr.c',
        'src/platform/windows/win_tcp.c',
        'src/platform/windows/win_tcpconn.c',
        'src/platform/windows/win_tcpdial.c',
        'src/platform/windows/win_tcplisten.c',
        'src/platform/windows/win_thread.c',
        'src/platform/windows/win_udp.c',
    )

    include_dirs += 'src/platform/windows/'
    # Probably missing some other link arguments
    link_args = ''

    add_project_arguments('-DNNG_PLATFORM_WINDOWS', language: 'c')
else
    nng_src += files(
        'src/platform/posix/posix_alloc.c',
        'src/platform/posix/posix_atomic.c',
        'src/platform/posix/posix_clock.c',
        'src/platform/posix/posix_debug.c',
        'src/platform/posix/posix_file.c',
        'src/platform/posix/posix_ipcconn.c',
        'src/platform/posix/posix_ipcdial.c',
        'src/platform/posix/posix_ipclisten.c',
        'src/platform/posix/posix_pipe.c',
        'src/platform/posix/posix_resolv_gai.c',
        'src/platform/posix/posix_sockaddr.c',
        'src/platform/posix/posix_tcpconn.c',
        'src/platform/posix/posix_tcpdial.c',
        'src/platform/posix/posix_tcplisten.c',
        'src/platform/posix/posix_thread.c',
        'src/platform/posix/posix_udp.c',

        'src/platform/posix/posix_pollq_poll.c',
        'src/platform/posix/posix_rand_urandom.c',
    )

    include_dirs += 'src/platform/posix'
    link_args = '-lpthread'

    add_project_arguments('-DNNG_PLATFORM_POSIX', language: 'c')
    add_project_link_arguments('-lpthread', language: 'c')
endif

nng_args = [
    '-DNNG_HAVE_BUS0',
    '-DNNG_HAVE_PAIR0',
    '-DNNG_HAVE_PAIR1',
    '-DNNG_HAVE_PUB0',
    '-DNNG_HAVE_PULL0',
    '-DNNG_HAVE_PUSH0',
    '-DNNG_HAVE_REP0',
    '-DNNG_HAVE_REQ0',
    '-DNNG_HAVE_RESPONDENT0',
    '-DNNG_HAVE_SUB0',
    '-DNNG_HAVE_SURVEYOR0',
    '-DNNG_TRANSPORT_INPROC',
    '-DNNG_TRANSPORT_IPC',
    '-DNNG_TRANSPORT_TCP',
    '-DNNG_TRANSPORT_TLS',
]

add_project_arguments(nng_args, language: 'c')

nng = library('nng',
    nng_src,
    include_directories : include_dirs
)

nng_dep = declare_dependency(
    compile_args: nng_args,
    link_with : nng,
    version : meson.project_version(),
    include_directories : include_dirs,
    link_args : link_args
)
