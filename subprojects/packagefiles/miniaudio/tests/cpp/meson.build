if add_languages('cpp', native: false, required: false)
  test(
    'deviceio_cpp',
    executable(
      'ma_test_cpp',
      'cpp.cpp',
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
