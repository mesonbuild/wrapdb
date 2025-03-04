if generation
  test(
    'generation',
    executable(
      'ma_test_generation',
      'generation.c',
      dependencies: ma_sys_deps,
      install: false,
      build_by_default: false,
      implicit_include_directories: false,
      include_directories: ma_inc,
    ),
    workdir: test_workdir,
  )
endif
