project(
    'libcap',
    'c',
    version: '2.75',
    license: 'BSD',
    default_options: ['c_std=gnu11'],
)

incdir = include_directories('libcap', '.', 'libcap/include')

cap_names_list_h = custom_target(
    'cap_names.list.h',
    output: 'cap_names.list.h',
    input: 'libcap/cap_names.list',
    command: ['cp', '@INPUT@', '@OUTPUT@'],
    install: false,
    build_by_default: true,
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
    build_by_default: true,
    depends: [_makenames, cap_names_list_h],
)

libcap_sources = files(
    'libcap/cap_alloc.c',
    'libcap/cap_extint.c',
    'libcap/cap_file.c',
    'libcap/cap_flag.c',
    'libcap/cap_proc.c',
    'libcap/cap_text.c',
    'libcap/cap_test.c',
    'libcap/cap_syscalls.c',
)

libcap = library(
    'libcap',
    sources: [libcap_sources, cap_names_h],
    include_directories: incdir,
    install: true,
)

libcap_dep = declare_dependency(
    include_directories: incdir,
    link_with: libcap,
)
