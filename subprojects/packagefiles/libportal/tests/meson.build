if 'qt5' in enabled_backends
  subdir('qt5')
endif
if 'qt6' in enabled_backends
  subdir('qt6')
endif

if meson.version().version_compare('>= 0.56.0')
  pytest = find_program(
    'pytest-3',
    'pytest',
    required: false,
  )
  pymod = import('python')
  python = pymod.find_installation(
    'python3',
    modules: ['dbus', 'dbusmock'],
    required: false,
  )

  if pytest.found() and python.found()
    test_env = environment()
    test_env.set('LD_LIBRARY_PATH', meson.project_build_root() / 'libportal')
    test_env.set('GI_TYPELIB_PATH', meson.project_build_root() / 'libportal')

    test(
      'pytest',
      pytest,
      args: ['--verbose', '--verbose', '--log-level=DEBUG'],
      env: test_env,
      workdir: meson.current_source_dir(),
      timeout: 180,
    )
  endif
endif
