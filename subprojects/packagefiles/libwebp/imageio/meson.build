imageio_util_lib = static_library(
  'imageioutil',
  'imageio_util.c',
  build_by_default: false,
  dependencies: common_deps,
  gnu_symbol_visibility: 'hidden',
)

imageio_dec_lib = static_library(
  'imageiodec',
  [
    'image_dec.c',
    'jpegdec.c',
    'metadata.c',
    'pngdec.c',
    'pnmdec.c',
    'tiffdec.c',
    'webpdec.c',
    'wicdec.c',
  ],
  build_by_default: false,
  dependencies: common_deps,
  gnu_symbol_visibility: 'hidden',
)

imageio_enc_lib = static_library(
  'imageioenc',
  'image_enc.c',
  build_by_default: false,
  dependencies: common_deps,
  gnu_symbol_visibility: 'hidden',
)
