sharpyuv_simd_libs = []
foreach _variant, _sources : {
  'neon': 'sharpyuv_neon.c',
  'sse2': 'sharpyuv_sse2.c',
}
  sharpyuv_simd_libs += static_library(
    'sharpyuv_' + _variant,
    _sources,
    build_by_default: false,
    c_args: simd_cflags[_variant],
    dependencies: common_deps,
    gnu_symbol_visibility: 'hidden',
  )
endforeach

sharpyuv_lib = library(
  'sharpyuv',
  [
    'sharpyuv.c',
    'sharpyuv_cpu.c',
    'sharpyuv_csp.c',
    'sharpyuv_dsp.c',
    'sharpyuv_gamma.c',
  ],
  dependencies: [build_libsharpyuv, common_deps],
  gnu_symbol_visibility: 'hidden',
  install: true,
  link_whole: sharpyuv_simd_libs,
  version: '0.1.2',
)

sharpyuv_dep = declare_dependency(
  include_directories: top_includes,
  link_with: sharpyuv_lib,
)

meson.override_dependency('libsharyuv', sharpyuv_dep)

pkg.generate(
  sharpyuv_lib,
  description: 'Library for sharp RGB to YUV conversion',
  name: 'libsharpyuv',
)

if build_libsharpyuv.found()
  install_headers(
    ['sharpyuv.h', 'sharpyuv_csp.h'],
    subdir: 'webp/sharpyuv',
  )
endif
