if device_io.enabled() and encoding and decoding and generation
  test(
    'deviceio',
    executable(
      'ma_test_deviceio',
      'deviceio.c',
      dependencies: ma_sys_deps + ma_backend_deps,
      install: false,
      build_by_default: false,
      implicit_include_directories: false,
      include_directories: ma_inc,
    ),
    args: '--auto',
    is_parallel: false,
    workdir: test_workdir,
  )
endif
