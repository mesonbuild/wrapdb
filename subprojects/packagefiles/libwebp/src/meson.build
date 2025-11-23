webp_lib = library(
  'webp',
  dependencies: [build_libwebp, sharpyuv_dep],
  gnu_symbol_visibility: 'hidden',
  install: true,
  link_whole: [
    webpdec_lib,
    webpdspdec_lib,
    webpdspenc_lib,
    webpenc_lib,
    webputilsdec_lib,
    webputilsenc_lib,
  ],
  version: '7.2.0',
)

webp_dep = declare_dependency(
  dependencies: sharpyuv_dep,
  include_directories: include_directories('.'),
  link_with: webp_lib,
)

meson.override_dependency('libwebp', webp_dep)

pkg.generate(
  webp_lib,
  description: 'Library for the WebP graphics format',
  name: 'libwebp',
)

webpdecoder_lib = library(
  'webpdecoder',
  dependencies: build_libwebpdecoder,
  gnu_symbol_visibility: 'hidden',
  install: true,
  link_whole: [webpdec_lib, webpdspdec_lib, webputilsdec_lib],
  version: '3.2.0',
)

webpdecoder_dep = declare_dependency(
  include_directories: include_directories('.'),
  link_with: webpdecoder_lib,
)

meson.override_dependency('libwebpdecoder', webpdecoder_dep)

pkg.generate(
  webpdecoder_lib,
  description: 'Library for the WebP graphics format (decode only)',
  name: 'libwebpdecoder',
)

if build_libwebp.found()
  webp_dec_dep = webp_dep
elif build_libwebpdecoder.found()
  webp_dec_dep = webpdecoder_dep
else
  webp_dec_dep = disabler()
endif
