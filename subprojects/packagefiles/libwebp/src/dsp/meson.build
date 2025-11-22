webp_dsp_dec_simd_libs = []
foreach _variant, _sources : {
  'neon': [
    'alpha_processing_neon.c',
    'dec_neon.c',
    'filters_neon.c',
    'lossless_neon.c',
    'rescaler_neon.c',
    'upsampling_neon.c',
    'yuv_neon.c',
  ],
  'sse2': [
    'alpha_processing_sse2.c',
    'dec_sse2.c',
    'filters_sse2.c',
    'lossless_sse2.c',
    'rescaler_sse2.c',
    'upsampling_sse2.c',
    'yuv_sse2.c',
  ],
  'sse41': [
    'alpha_processing_sse41.c',
    'dec_sse41.c',
    'lossless_sse41.c',
    'upsampling_sse41.c',
    'yuv_sse41.c',
  ],
  'avx2': ['lossless_avx2.c'],
}
  webp_dsp_dec_simd_libs += static_library(
    'webpdspdec_' + _variant,
    _sources,
    build_by_default: false,
    c_args: simd_cflags[_variant],
    dependencies: common_deps,
    gnu_symbol_visibility: 'hidden',
  )
endforeach

webpdspdec_lib = static_library(
  'webpdspdec',
  [
    'alpha_processing.c',
    'alpha_processing_mips_dsp_r2.c',
    'cpu.c',
    'dec.c',
    'dec_clip_tables.c',
    'dec_mips32.c',
    'dec_mips_dsp_r2.c',
    'dec_msa.c',
    'filters.c',
    'filters_mips_dsp_r2.c',
    'filters_msa.c',
    'lossless.c',
    'lossless_mips_dsp_r2.c',
    'lossless_msa.c',
    'rescaler.c',
    'rescaler_mips32.c',
    'rescaler_mips_dsp_r2.c',
    'rescaler_msa.c',
    'upsampling.c',
    'upsampling_mips_dsp_r2.c',
    'upsampling_msa.c',
    'yuv.c',
    'yuv_mips32.c',
    'yuv_mips_dsp_r2.c',
  ],
  build_by_default: false,
  dependencies: common_deps,
  gnu_symbol_visibility: 'hidden',
  link_whole: webp_dsp_dec_simd_libs,
)

webp_dsp_enc_simd_libs = []
foreach _variant, _sources : {
  'neon': ['cost_neon.c', 'enc_neon.c', 'lossless_enc_neon.c'],
  'sse2': ['cost_sse2.c', 'enc_sse2.c', 'lossless_enc_sse2.c', 'ssim_sse2.c'],
  'sse41': ['enc_sse41.c', 'lossless_enc_sse41.c'],
  'avx2': ['lossless_enc_avx2.c'],
}
  webp_dsp_enc_simd_libs += static_library(
    'webpdspenc_' + _variant,
    _sources,
    build_by_default: false,
    c_args: simd_cflags[_variant],
    dependencies: common_deps,
    gnu_symbol_visibility: 'hidden',
  )
endforeach

webpdspenc_lib = static_library(
  'webpdspenc',
  [
    'cost.c',
    'cost_mips32.c',
    'cost_mips_dsp_r2.c',
    'enc.c',
    'enc_mips32.c',
    'enc_mips_dsp_r2.c',
    'enc_msa.c',
    'lossless_enc.c',
    'lossless_enc_mips32.c',
    'lossless_enc_mips_dsp_r2.c',
    'lossless_enc_msa.c',
    'ssim.c',
  ],
  build_by_default: false,
  dependencies: common_deps,
  gnu_symbol_visibility: 'hidden',
  link_whole: webp_dsp_enc_simd_libs,
)
