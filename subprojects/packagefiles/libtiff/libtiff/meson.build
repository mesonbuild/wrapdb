tiffconf_h = configure_file(
  input: 'tiffconf.h.cmake.in',
  output: 'tiffconf.h',
  format: 'cmake@',
  configuration: cdata,
)

configure_file(
  input: 'tif_config.h.cmake.in',
  output: 'tif_config.h',
  format: 'cmake@',
  configuration: cdata,
)

tiffvers_h = configure_file(
  input: 'tiffvers.h.cmake.in',
  output: 'tiffvers.h',
  format: 'cmake@',
  configuration: cdata,
)

sources = files(
  'tif_aux.c',
  'tif_close.c',
  'tif_codec.c',
  'tif_color.c',
  'tif_compress.c',
  'tif_dir.c',
  'tif_dirinfo.c',
  'tif_dirread.c',
  'tif_dirwrite.c',
  'tif_dumpmode.c',
  'tif_error.c',
  'tif_extension.c',
  'tif_fax3.c',
  'tif_fax3sm.c',
  'tif_flush.c',
  'tif_getimage.c',
  'tif_hash_set.c',
  'tif_jbig.c',
  'tif_jpeg.c',
  'tif_jpeg_12.c',
  'tif_luv.c',
  'tif_lzma.c',
  'tif_lzw.c',
  'tif_next.c',
  'tif_ojpeg.c',
  'tif_open.c',
  'tif_packbits.c',
  'tif_pixarlog.c',
  'tif_predict.c',
  'tif_print.c',
  'tif_read.c',
  'tif_strip.c',
  'tif_swab.c',
  'tif_thunder.c',
  'tif_tile.c',
  'tif_version.c',
  'tif_warning.c',
  'tif_webp.c',
  'tif_write.c',
  'tif_zip.c',
  'tif_zstd.c',
  'tif_@0@.c'.format(host_machine.system() == 'windows' ? 'win32' : 'unix'),
)

if host_machine.system() == 'windows'
  sources += import('windows').compile_resources(
    'tif_win32_versioninfo.rc',
    include_directories : meson.current_build_dir(),
  )
endif

tiff4_lib = library(
  'tiff',
  sources,
  install: true,
  dependencies: [m_dep, jbig_dep, jpeg_dep, lerc_dep, lzma_dep, webp_dep, zlib_dep, zstd_dep],
  vs_module_defs: 'libtiff.def',
  version: library_version,
)

install_headers(
  'tiff.h',
  'tiffio.h',
  tiffconf_h,
  tiffvers_h,
)
