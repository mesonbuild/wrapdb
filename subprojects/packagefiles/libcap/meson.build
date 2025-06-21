project(
    'libcap',
    'c',
    version: '2.76',
    license: 'BSD-3-Clause OR GPL-2.0-only',
    default_options: ['c_std=gnu11', 'buildtype=release'],
)

if host_machine.system() != 'linux'
    error('libcap is not supported on this platform.')
endif

incdir = include_directories('libcap/include')

cap_names_list_h = custom_target(
    'cap_names.list.h',
    output: 'cap_names.list.h',
    input: 'libcap/include/uapi/linux/capability.h',
    command: [find_program('gen_cap_names.py'), '@INPUT@', '@OUTPUT@'],
    install: false,
)

_makenames = executable(
    '_makenames',
    sources: ['libcap/_makenames.c', cap_names_list_h],
    include_directories: incdir,
    native: true,
)

cap_names_h = custom_target(
    'cap_names.h',
    output: 'cap_names.h',
    input: 'libcap/cap_names.header',
    command: [_makenames, '@INPUT@'],
    capture: true,
    install: false,
)

libcap = library(
    'cap',
    sources: [
        'libcap/cap_alloc.c',
        'libcap/cap_extint.c',
        'libcap/cap_file.c',
        'libcap/cap_flag.c',
        'libcap/cap_proc.c',
        'libcap/cap_text.c',
        'libcap/cap_syscalls.c',
        cap_names_h,
    ],
    include_directories: incdir,
    install: true,
)

libcap_dep = declare_dependency(include_directories: incdir, link_with: libcap)
