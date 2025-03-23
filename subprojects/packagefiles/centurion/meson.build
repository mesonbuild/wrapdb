project(
  'centurion',
  'cpp',
  version: '7.3.0',
  license: 'MIT',
  meson_version: '>=0.60.0',
  default_options: ['cpp_std=c++17'],
)

centurion_args = []
centurion_deps = [dependency('sdl2')]

# Uppercase is used by pkg-config, (built-in) cmake finders and wraps are lowercase

sdl2_image_dep = dependency(
  'SDL2_image',
  'sdl2_image',
  required: get_option('with_sdl2_image'),
)

if sdl2_image_dep.found()
  centurion_deps += [sdl2_image_dep]
else
  centurion_args += ['-DCENTURION_NO_SDL_IMAGE']
endif

sdl2_mixer_dep = dependency(
  'SDL2_mixer',
  'sdl2_mixer',
  required: get_option('with_sdl2_mixer'),
)

if sdl2_mixer_dep.found()
  centurion_deps += [sdl2_mixer_dep]
else
  centurion_args += ['-DCENTURION_NO_SDL_MIXER']
endif

sdl2_ttf_dep = dependency(
  'SDL2_ttf',
  'sdl2_ttf',
  required: get_option('with_sdl2_ttf'),
)

if sdl2_ttf_dep.found()
  centurion_deps += [sdl2_ttf_dep]
else
  centurion_args += ['-DCENTURION_NO_SDL_TTF']
endif

centurion_dep = declare_dependency(
  include_directories: 'src',
  dependencies: centurion_deps,
  compile_args: centurion_args,
)

meson.override_dependency('centurion', centurion_dep)
