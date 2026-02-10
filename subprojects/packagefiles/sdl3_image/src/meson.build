sdl3_image_src = files(
  'IMG.c',
  'IMG_WIC.c',
  'IMG_ani.c',
  'IMG_anim_decoder.c',
  'IMG_anim_encoder.c',
  'IMG_avif.c',
  'IMG_bmp.c',
  'IMG_gif.c',
  'IMG_gpu.c',
  'IMG_jpg.c',
  'IMG_jxl.c',
  'IMG_lbm.c',
  'IMG_libpng.c',
  'IMG_pcx.c',
  'IMG_png.c',
  'IMG_pnm.c',
  'IMG_qoi.c',
  'IMG_stb.c',
  'IMG_svg.c',
  'IMG_tga.c',
  'IMG_tif.c',
  'IMG_webp.c',
  'IMG_xcf.c',
  'IMG_xpm.c',
  'IMG_xv.c',
  'IMG_xxx.c',
)

if target_machine.system() == 'windows' and get_option('default_library') == 'shared'
  import('windows').compile_resources('version.rc')
endif

if target_machine.system() == 'darwin'
  sdl3_image_src += 'IMG_ImageIO.m'
endif
