project('quickjs', 'c')

cc = meson.get_compiler('c')
dep_m = cc.find_library('m', required: false)
dep_threads = dependency('threads')
deps = [
    dep_m,
    dep_threads,
    dependency('dl')
]

lib_src = [
    'quickjs.c',
    'libregexp.c',
    'libunicode.c',
    'cutils.c',
    'quickjs-libc.c',
    'libbf.c'
]
config_version = run_command('cat', 'VERSION', check: true).stdout().strip()
# WARNING: current version (2024-01-23) does not compile without bignum
# TODO: support shared libs
c_defines = [
    '-funsigned-char',
    '-D_GNU_SOURCE',
    '-DCONFIG_VERSION="'+config_version+'"',
    '-DCONFIG_BIGNUM',
]

add_project_arguments(c_defines, language: 'c')

qjsc = executable('qjsc',
    'qjsc.c',
    lib_src,
    dependencies: deps)

repl_c = custom_target('repl_c',
    input: 'repl.js',
    output: 'repl.c',
    command: [qjsc, '-c', '-o', '@OUTPUT@', '-m', '@INPUT@']
)

qjscalc_c = custom_target('qjscalc_c',
    input: 'qjscalc.js',
    output: 'qjscalc.c',
    command: [qjsc, '-fbignum', '-c', '-o', '@OUTPUT@', '@INPUT@']
)

quickjs_lib = static_library('quickjs',
    lib_src,
    qjscalc_c,
    dependencies : deps
)

qjs = executable('qjs',
    'qjs.c',
    repl_c,
    link_with: [quickjs_lib],
    dependencies: deps)

# TODO: add more tests and examples

test_root = join_paths(meson.project_source_root(), 'tests')

test('closure', qjs, args: ['test_closure.js'], workdir: test_root)
test('language', qjs, args: ['test_language.js'], workdir: test_root)
test('builtin', qjs, args: ['test_builtin.js'], workdir: test_root)
test('loop', qjs, args: ['test_loop.js'], workdir: test_root)
test('std', qjs, args: ['test_std.js'], workdir: test_root)
test('worker', qjs, args: ['test_worker.js'], workdir: test_root)

test('op_overloading', qjs, args: ['--bignum', 'test_op_overloading.js'], workdir: test_root)
test('bignum', qjs, args: ['--bignum', 'test_bignum.js'], workdir: test_root)
test('qjscalc', qjs, args: ['--qjscalc', 'test_qjscalc.js'], workdir: test_root)

quickjs_lib_dep = declare_dependency(
    include_directories: include_directories('.'),
    link_with: quickjs_lib,
    dependencies: deps)
