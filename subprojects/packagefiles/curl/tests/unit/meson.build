_bundle = {}
foreach _line : makefile_extractions['unit']
  _kv = _line.split('=')
  _bundle += {
    _kv[0].strip(): _kv[1].strip().split(),
  }
endforeach

_tests = _bundle['TESTS_C']

_deps = ['../libtest/first.c', 'Makefile.inc']
foreach _f : _tests
  _deps += files(_f)
endforeach

units_c = custom_target(
  'units.c',
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
  output: 'units.c',
)

unit_targets += executable(
  'units',
  [units_c, unitprotos_h],
  c_args: curlu_flags + ['-DBUILDING_LIBCURL', debug_args],
  dependencies: [curl_iflags_dep, curlu_dep],
  include_directories: [
    include_directories('../../src', '../libtest'),
    lib_build_inc,
  ],
)
