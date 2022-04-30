project('libkqueue', 'c',
    version : '2.6.1',
    license : 'BSD',
    meson_version : '>=0.48.0',
    default_options : ['c_std=c11'],
)

varr = meson.project_version().split('.')
version_major = varr[0]
version_minor = varr[1]
version_patch = varr[2]

cc = meson.get_compiler('c')

cdata = configuration_data()

cdata.set_quoted('LIBKQUEUE_VERSION_STRING', meson.project_version())
cdata.set('LIBKQUEUE_VERSION_MAJOR', version_major)
cdata.set('LIBKQUEUE_VERSION_MINOR', version_minor)
cdata.set('LIBKQUEUE_VERSION_PATCH', version_patch)
cdata.set_quoted('LIBKQUEUE_VERSION_DATE', '')

check_headers = [
    'sys/signalfd.h',
    'sys/timerfd.h',
    'sys/eventfd.h',
    'sys/types.h',
]

foreach entry : check_headers
    header = entry
    if cc.has_header(header)
        cdata.set('HAVE_@0@'.format(header.underscorify().to_upper()), 1)
    endif
endforeach

check_symbols = [
    ['HAVE_EPOLLRDHUP',     'EPOLLRDHUP',       'sys/epoll.h'],
    ['HAVE_NOTE_TRUNCATE',  'NOTE_TRUNCATE',    'sys/event.h'],
    ['HAVE_DECL_PPOLL',     'ppoll',            'poll.h'],
    ['HAVE_SYS_PIDFD_OPEN', 'pidfd_open',   'sys/syscall.h'],
]

foreach entry : check_symbols
    define = entry[0]
    symbol = entry[1]
    header = entry[2]
    if cc.has_header_symbol(header, symbol)
        cdata.set(define, 1)
    endif
endforeach

kqueue_sources = [
    'src/common/alloc.h',
    'src/common/debug.h',
    'src/common/debug.c',
    'src/common/filter.c',
    'src/common/kevent.c',
    'src/common/knote.c',
    'src/common/kqueue.c',
    'src/common/libkqueue.c',
    'src/common/map.c',
    'src/common/private.h',
    'src/common/queue.h',
    'src/common/tree.h',
]

kqueue_inc = [
    'include',
]

kqueue_args = []

kqueue_deps = [
    dependency('threads')
]

if target_machine.system() == 'windows'
    kqueue_sources += [
        'src/windows/platform.c',
        'src/windows/platform.h',
        'src/windows/read.c',
        'src/windows/stdint.h',
        'src/windows/timer.c',
        'src/windows/user.c',
    ]

    kqueue_args += [
        '-D_USRDLL',
        '-D_WINDLL',
        '-D_CRT_SECURE_NO_WARNINGS',
        '-DWIN32_LEAN_AND_MEAN'
    ]

    kqueue_deps += cc.find_library('ws2_32')
elif target_machine.system() == 'linux'
    kqueue_sources += [
        'src/linux/platform.c',
        'src/linux/platform.h',
        'src/linux/read.c',
        'src/linux/signal.c',
        'src/linux/timer.c',
        'src/linux/user.c',
        'src/linux/vnode.c',
        'src/linux/write.c',
    ]

    if cdata.get('HAVE_SYS_PIDFD_OPEN', 0) == 1
        kqueue_sources += 'src/linux/proc.c'
    else
        kqueue_sources += 'src/posix/proc.c'
    endif

    kqueue_inc += 'src/common'

    kqueue_args += [
        '-D_XOPEN_SOURCE=600',
    ]
elif target_machine.system() == 'sunos'
    kqueue_sources += [
        'src/posix/eventfd.c',
        'src/posix/eventfd.h',
        'src/solaris/platform.c',
        'src/solaris/platform.h',
        'src/solaris/signal.c',
        'src/solaris/socket.c',
        'src/solaris/timer.c',
        'src/solaris/user.c',
    ]

    kqueue_inc += 'src/common'

    kqueue_args += [
        '-D_XOPEN_SOURCE=600',
    ]
else
    error('unsupported host os')
endif

configure_file(
    input : 'config.h.meson',
    output : 'config.h',
    configuration : cdata
)

configure_file(
    input : 'version.h.meson',
    output : 'version.h',
    configuration : cdata
)

libkqueue = library('kqueue',
    kqueue_sources,
    include_directories : kqueue_inc,
    c_args : kqueue_args,
    dependencies : kqueue_deps
)

libkqueue_dep = declare_dependency(
    link_with : libkqueue,
    include_directories : kqueue_inc,
)
