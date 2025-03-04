if 'webaudio' in backends
  executable(
    'ma_test_emscripten',
    'emscripten.c',
    name_suffix: host_system == 'emscripten' ? 'html' : [],
    dependencies: ma_sys_deps + ma_backend_deps,
    install: false,
    implicit_include_directories: false,
    include_directories: ma_inc,
  )
endif
