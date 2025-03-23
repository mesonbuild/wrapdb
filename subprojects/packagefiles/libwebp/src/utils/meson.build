webputilsdec_lib = static_library(
  'webputilsdec',
  [
    'bit_reader_utils.c',
    'color_cache_utils.c',
    'filters_utils.c',
    'huffman_utils.c',
    'palette.c',
    'quant_levels_dec_utils.c',
    'rescaler_utils.c',
    'random_utils.c',
    'thread_utils.c',
    'utils.c',
  ],
  build_by_default: false,
  pic: get_option('default_library') != 'static',
  dependencies: common_deps,
  gnu_symbol_visibility: 'hidden',
)

webputilsenc_lib = static_library(
  'webputilsenc',
  [
    'bit_writer_utils.c',
    'huffman_encode_utils.c',
    'quant_levels_utils.c',
  ],
  build_by_default: false,
  pic: get_option('default_library') != 'static',
  dependencies: common_deps,
  gnu_symbol_visibility: 'hidden',
)
