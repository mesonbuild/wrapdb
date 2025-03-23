if sdl2_dep.type_name() == 'internal'
  sdl2_test_dep = dependency('sdl2_test')
  sdl2main_dep = dependency('sdl2main')
else
  sdl2_test_dep = cc.find_library('SDL2_test')
  sdl2main_dep = cc.find_library('SDL2main')
endif

testimage_exe = executable(
  'testimage',
  'main.c',
  dependencies: [sdl2_dep, sdl2_image_dep, sdl2_test_dep, sdl2main_dep],
  c_args: feature_args,  # required by test suite
)

test(
  'testimage',
  testimage_exe,
  env: {
    'SDL_TEST_SRCDIR': meson.current_source_dir(),
    'SDL_TEST_BUILDDIR': meson.current_build_dir(),
    'SDL_VIDEODRIVER': 'dummy',
  },
)
