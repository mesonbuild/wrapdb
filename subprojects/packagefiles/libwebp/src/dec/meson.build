webpdec_lib = static_library(
  'webpdec',
  [
    'alpha_dec.c',
    'buffer_dec.c',
    'frame_dec.c',
    'idec_dec.c',
    'io_dec.c',
    'quant_dec.c',
    'tree_dec.c',
    'vp8_dec.c',
    'vp8l_dec.c',
    'webp_dec.c',
  ],
  build_by_default: false,
  dependencies: common_deps,
  gnu_symbol_visibility: 'hidden',
)
