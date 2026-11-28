_bundle = {}
foreach _line : makefile_extractions['tunit']
  _kv = _line.split('=')
  _bundle += {
    _kv[0].strip(): _kv[1].strip().split(),
  }
endforeach

_tests = _bundle['TESTS_C']

_deps = ['../libtest/first.c', '../libtest/first.h', 'Makefile.inc']
foreach _f : _tests
  _deps += files(_f)
endforeach

tunits_c = custom_target(
  'tunits.c',
  command: [
    bash_exe,
    '-c',
    'cd "$0" && exec perl "$@"',
    meson.current_source_dir(),
    meson.project_source_root() / 'scripts/mk-unity.pl',
    '--test',
  ] + _tests,
  depend_files: [
    meson.project_source_root() / 'scripts/mk-unity.pl',
  ] + _deps,
  capture: true,
  output: 'tunits.c',
)

tunit_targets += executable(
  'tunits',
  tunits_c,
  c_args: curlu_flags + debug_args,
  dependencies: [curltool_dep, curl_ilib_dep, libuv_dep],
  include_directories: include_directories('.', '../../src', '../libtest'),
)
