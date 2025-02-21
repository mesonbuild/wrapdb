project(
    'quickjs',
    'c',
    version: '0.8.0',
    default_options: [
        'c_std=gnu11',
        'buildtype=release',
        'warning_level=0',
        'werror=false',
    ],
)

cc = meson.get_compiler('c')
libm_dep = cc.find_library('m', required: false)
add_project_arguments('-D_GNU_SOURCE', language: 'c')

# Unicode generator
unicode_gen_sources = files('cutils.c', 'libunicode.c', 'unicode_gen.c')
unicode_gen_exe = executable('unicode_gen', unicode_gen_sources, install: false)

# library: qjs
quickjs_sources = files(
    'cutils.c',
    'libbf.c',
    'libregexp.c',
    'libunicode.c',
    'quickjs.c',
)
quickjs_lib = library(
    'qjs',
    quickjs_sources,
    dependencies: libm_dep,
    install: true,
)
quickjs_dep = declare_dependency(link_with: quickjs_lib)

#library: quickjs-libc
quickjs_libc_sources = files('quickjs-libc.c')
quickjs_libc_lib = library(
    'qjs-libc',
    quickjs_libc_sources,
    dependencies: quickjs_dep,
    install: true,
)
quickjs_libc_dep = declare_dependency(link_with: quickjs_libc_lib)


# headers
qjs_headers = files(
    'cutils.h',
    'dirent_compat.h',
    'getopt_compat.h',
    'libbf.h',
    'libregexp-opcode.h',
    'libregexp.h',
    'libunicode-table.h',
    'libunicode.h',
    'list.h',
    'quickjs-atom.h',
    'quickjs-c-atomics.h',
    'quickjs-libc.h',
    'quickjs-opcode.h',
    'quickjs.h',
    'unicode_gen_def.h',
)
install_headers(qjs_headers, subdir: 'quickjs')

# qjsc
qjsc_exe = executable(
    'qjsc',
    'qjsc.c',
    dependencies: [quickjs_dep, quickjs_libc_dep],
    install: true,
)
qjsc_gen = generator(
    qjsc_exe,
    output: '@BASENAME@.c',
    arguments: ['-o', '@OUTPUT@', '@INPUT@'],
)

# qjs
qjs_gen = qjsc_gen.process('repl.js', 'standalone.js')
qjs_exe = executable(
    'qjs',
    ['qjs.c', qjs_gen],
    dependencies: [quickjs_dep, quickjs_libc_dep],
    install: true,
)

meson.override_find_program('qjs', qjs_exe)
meson.override_find_program('qjsc', qjsc_exe)

