# bimg + bimg_decode — image libraries for bgfx

# --- bundled 3rdparty codecs ---

subdir('3rdparty/astc-encoder')
subdir('3rdparty/libsquish')
subdir('3rdparty/nvtt')
subdir('3rdparty/pvrtc')
subdir('3rdparty/etc1')
subdir('3rdparty/etc2')
subdir('3rdparty/edtaa3')
subdir('3rdparty/iqa')

# --- bimg library ---

bimg_sources = files(
  'src/image.cpp',
  'src/image_gnf.cpp',
)

bimg_inc = include_directories('include')

bimg_lib = static_library('bimg',
  bimg_sources,
  astc_encoder_sources,
  include_directories: [bimg_inc, astc_encoder_inc],
  dependencies: bx_dep,
)

bimg_dep = declare_dependency(
  include_directories: bimg_inc,
  link_with: bimg_lib,
)

# --- bimg_decode library ---
# image_decode.cpp #includes lodepng, miniz, tinyexr inline — not compiled separately.

bimg_decode_sources = files(
  'src/image_decode.cpp',
)

bimg_3rdparty_inc = include_directories('3rdparty')
bimg_miniz_inc = include_directories('3rdparty/tinyexr/deps')

bimg_decode_lib = static_library('bimg_decode',
  bimg_decode_sources,
  include_directories: [bimg_inc, bimg_3rdparty_inc, bimg_miniz_inc],
  dependencies: bx_dep,
)

bimg_decode_dep = declare_dependency(
  include_directories: bimg_inc,
  link_with: bimg_decode_lib,
)

# --- bimg_encode library ---
# Compiles image encoding support + 8 bundled 3rdparty codec libraries.
# astc-encoder is already compiled into bimg; we only need its include dir here.

# -- tinyexr is header-only (already used by bimg_decode via #include) --

bimg_encode_sources = files(
  'src/image_encode.cpp',
  'src/image_cubemap_filter.cpp',
)

bimg_encode_3rdparty_inc = include_directories(
  '3rdparty',
  '3rdparty/nvtt',
  '3rdparty/iqa/include',
  '3rdparty/astc-encoder/include',
  '3rdparty/tinyexr/deps',  # miniz
)

bimg_encode_warn_args = []
cpp = meson.get_compiler('cpp')
foreach flag : ['-Wno-implicit-fallthrough', '-Wno-shadow', '-Wno-shift-negative-value', '-Wno-undef',
                '-Wno-class-memaccess', '-Wno-deprecated-copy']
  if cpp.has_argument(flag)
    bimg_encode_warn_args += flag
  endif
endforeach

bimg_encode_lib = static_library('bimg_encode',
  bimg_encode_sources,
  libsquish_sources,
  nvtt_sources,
  pvrtc_sources,
  etc1_sources,
  etc2_sources,
  edtaa3_sources,
  iqa_sources,
  include_directories: [bimg_inc, bimg_encode_3rdparty_inc],
  dependencies: bx_dep,
  cpp_args: bimg_encode_warn_args,
)

bimg_encode_dep = declare_dependency(
  include_directories: bimg_inc,
  link_with: bimg_encode_lib,
)
