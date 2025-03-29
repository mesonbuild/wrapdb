_ignore_tests = [
  # Specific to the autotools build system.
  'Bug_-_Install_all_files.test',
]

_tests_dir = meson.current_source_dir()

foreach _test : run_command(
  [sh, '-c', 'cd "$1" && printf \'%s\n\' *.test', '--', _tests_dir],
  check: true,
).stdout().split()
  if _test in _ignore_tests
    continue
  endif
  _suite = ''
  _name = []
  foreach _part : _test.substring(0, -5).split('_-_')
    if _suite == ''
      _suite = _part
    else
      _name += [_part]
    endif
  endforeach
  _name = ' '.join(_name).replace('_', ' ')
  test(
    _name,
    sh,
    args: [
      '-c',
      '. "$1" && "$2"',
      '--',
      _tests_dir / 'test-env.sh',
      _tests_dir / _test,
    ],
    depends: pv,
    env: 'srcdir=' + meson.project_source_root(),
    suite: _suite,
    timeout: 60,
    # Tests use `./pv`.
    workdir: meson.project_build_root(),
  )
endforeach
