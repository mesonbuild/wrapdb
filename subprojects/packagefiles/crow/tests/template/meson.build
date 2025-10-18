mustachetest_exe = executable(
  'mustachetest',
  'mustachetest.cpp',
  dependencies: crow_dep,
  override_options: crow_private_options,
  cpp_args: crow_private_args,
)

# original CMakeLists.txt excludes MSVC only here
# but upstream does not test mingw and it seems to fail on mingw too.
# if meson.get_compiler('cpp').get_argument_syntax() != 'msvc'
if host_machine.system() != 'windows'
  py_prog = find_program('python3')
  json_files = [
    'comments.json',
    'crow_extra_mustache_tests.json',
    'delimiters.json',
    'interpolation.json',
    'inverted.json',
    'partials.json',
    'sections.json',
    '~lambdas.json',
  ]
  foreach f : json_files
    configure_file(
      copy: true,
      input: f,
      output: f,
    )
  endforeach
  configure_file(
    copy: true,
    input: 'test.py',
    output: 'test.py',
  )

  test(
    'template_test',
    py_prog,
    args: ['test.py'],
    workdir: meson.current_build_dir(),
    depends: mustachetest_exe,
  )
endif
