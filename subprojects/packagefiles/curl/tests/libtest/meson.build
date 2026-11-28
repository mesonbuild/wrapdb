lib1521_c = custom_target(
  'lib1521.c',
  command: [
    bash_exe,
    '-c',
    'exec perl "$@"',
    '--',
    meson.current_source_dir() / 'mk-lib1521.pl',
    '@OUTPUT@',
  ],
  depend_files: 'mk-lib1521.pl',
  feed: true,
  input: meson.project_source_root() / 'include/curl/curl.h',
  output: 'lib1521.c',
)

_bundle = {}
foreach _line : makefile_extractions['libtest']
  _kv = _line.split('=')
  _bundle += {
    _kv[0].strip(): _kv[1].strip().split(),
  }
endforeach

_includes = _bundle['UTILS_C'] + _bundle['CURLX_C'] + _bundle['TOOLX_C']
_tests = _bundle['TESTS_C']

_deps = ['first.c', 'first.h', 'Makefile.inc']
foreach _f : _includes + _tests
  _deps += files(_f)
endforeach

libtests_c = custom_target(
  'libtests.c',
  command: [
    bash_exe,
    '-c',
    'cd "$0" && exec perl "$@"',
    meson.current_source_dir(),
    meson.project_source_root() / 'scripts/mk-unity.pl',
    '--include',
  ] + _includes + [
    '--test',
  ] + _tests + [
    'lib1521.c',
  ],
  depend_files: [
    meson.project_source_root() / 'scripts/mk-unity.pl',
  ] + _deps,
  depends: lib1521_c,
  capture: true,
  output: 'libtests.c',
)

libtest_targets += executable(
  'libtests',
  libtests_c,
  c_args: ['-DCURL_STATICLIB', debug_args],
  dependencies: [curl_ilib_dep, threads_dep, lib_deps],
  include_directories: include_directories('.', '../../src'),
)
