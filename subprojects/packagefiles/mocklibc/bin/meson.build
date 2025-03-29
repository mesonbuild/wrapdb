mocklibc_conf = configuration_data()
mocklibc_conf.set('libpath', libmocklibc.full_path())

configure_file(
  input: meson.project_name() + '.in',
  output: '@BASENAME@',
  configuration: mocklibc_conf,
)

if find_program(
  'innetgr',
  required: false,
).found()
  # FIXME: workaround due to zip format not storing file permissions
  #        mocklibc.in and mocklibc-test.in need execution permission
  bash = find_program('bash')

  test_conf = configuration_data()
  # FIXME: workaround to execute mocklibc properly
  test_conf.set(
    'bindir',
    '@0@ @1@'.format(bash.path(), meson.current_build_dir()),
  )
  test_conf.set('etcdir', example_dir)

  test_unit = meson.project_name() + '-test'

  mocklibc_test = configure_file(
    input: test_unit + '.in',
    output: '@BASENAME@',
    configuration: test_conf,
  )

  test(
    test_unit,
    bash,
    args: mocklibc_test,
  )
endif
