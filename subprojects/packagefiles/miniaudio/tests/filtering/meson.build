if encoding and decoding
  test(
    'filtering',
    executable(
      'ma_test_filtering',
      'filtering.c',
      dependencies: ma_sys_deps,
      install: false,
      build_by_default: false,
      implicit_include_directories: false,
      include_directories: ma_inc,
    ),
    args: files(test_workdir / 'res/sine_s16_mono_48000.wav'),
    workdir: test_workdir,
  )
endif
