project(
  'sdl3_image',
  'c',
  license: 'zlib',
  version: '3.2.4',
  meson_version: '>=0.54.0',
)

sdl_dep = dependency(
  'sdl3',
  version: '>=3.2.4',
)

png_dep = dependency('libpng')
jpg_dep = dependency(
  'libjpeg',
  required: false,
)

img_args = []

# These are enabled by default it seems.
#img_args = ['-DWANT_LIBPNG']
#if jpg_dep.found()
#  img_args += '-DWANT_JPEGLIB'
#endif

subdir('src')
img_lib = library(
  'sdl3_image',
  img_src,
  c_args: img_args,
  include_directories: 'include',
  gnu_symbol_visibility: 'hidden',
  dependencies: [png_dep, sdl_dep],
)

sdl3_image_dep = declare_dependency(
  include_directories: 'include',
  link_with: img_lib,
)

meson.override_dependency('sdl3_image', sdl3_image_dep)
