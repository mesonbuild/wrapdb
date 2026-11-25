_bundle = {}
foreach _line : makefile_extractions['server']
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

servers_c = custom_target(
  'servers.c',
  command: [
    bash_exe,
    '-c',
    'cd "$0" && exec perl "$@"',
    meson.current_source_dir(),
    meson.project_source_root() / 'scripts/mk-unity.pl',
    '--include',
  ] + _includes + [
    '--test',
  ] + _tests,
  depend_files: [
    meson.project_source_root() / 'scripts/mk-unity.pl',
  ] + _deps,
  capture: true,
  output: 'servers.c',
)

server_targets += executable(
  'servers',
  servers_c,
  config_h,
  dependencies: [curl_iflags_dep, sys_deps],
  include_directories: include_directories('.', '../../src'),
)
