project('sdl2-image', 'c', version: '2.6.2')

feature_args = ['-DLOAD_BMP', '-DLOAD_PNG', '-DLOAD_JPG']

sdl2_dep = dependency('sdl2')
png_dep = dependency('libpng')
jpeg_dep = dependency('libjpeg')
tif_dep = dependency('libtiff-4', required: false)

if tif_dep.found()
  feature_args += '-DLOAD_TIF'
endif

if host_machine.system() == 'darwin'
  feature_args += '-DSDL_IMAGE_USE_COMMON_BACKEND'
endif

sdl2_image_lib = library(
  'sdl2image',
  'IMG.c',
  'IMG_avif.c',
  'IMG_bmp.c',
  'IMG_gif.c',
  'IMG_jpg.c',
  'IMG_jxl.c',
  'IMG_lbm.c',
  'IMG_pcx.c',
  'IMG_png.c',
  'IMG_pnm.c',
  'IMG_qoi.c',
  'IMG_stb.c',
  'IMG_svg.c',
  'IMG_tga.c',
  'IMG_tif.c',
  'IMG_webp.c',
  'IMG_WIC.c',
  'IMG_xcf.c',
  'IMG_xpm.c',
  'IMG_xv.c',
  'IMG_xxx.c',
  c_args: feature_args,
  dependencies: [png_dep, jpeg_dep, tif_dep, sdl2_dep],
)

sdl2_image_dep = declare_dependency(
  include_directories: '.',
  link_with: sdl2_image_lib,
)
