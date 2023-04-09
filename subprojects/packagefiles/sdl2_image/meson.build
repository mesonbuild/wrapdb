project(
  'sdl2-image',
  'c',
  version: '2.6.3',
  meson_version: '>=0.49.0',
)

feature_args = ['-DLOAD_BMP']

options = {
  'avif': 'libavif',
  'jpg': 'libjpeg',
  'jxl': 'libjxl',
  'png': 'libpng',
  'tif': 'libtiff-4',
  'webp': 'libwebp',
}

sources = files(
  'IMG.c',
  'IMG_xxx.c',
)

deps = [dependency('sdl2')]

foreach i, d : options
  sources += files('IMG_@0@.c'.format(i))
  id = dependency(d, required: get_option(i))
  if id.found()
    deps += id
    feature_args += '-DLOAD_@0@'.format(i.to_upper())
  endif
endforeach

if host_machine.system() == 'darwin'
  feature_args += '-DSDL_IMAGE_USE_COMMON_BACKEND'
endif

sdl2_image_lib = library(
  'sdl2image',
  sources,
  'IMG_bmp.c',
  'IMG_gif.c',
  'IMG_lbm.c',
  'IMG_pcx.c',
  'IMG_pnm.c',
  'IMG_qoi.c',
  'IMG_stb.c',
  'IMG_svg.c',
  'IMG_tga.c',
  'IMG_WIC.c',
  'IMG_xcf.c',
  'IMG_xpm.c',
  'IMG_xv.c',
  c_args: feature_args,
  dependencies: deps,
)

depinc = include_directories('.')
sdl2_image_dep = declare_dependency(
  include_directories: depinc,
  link_with: sdl2_image_lib,
)
