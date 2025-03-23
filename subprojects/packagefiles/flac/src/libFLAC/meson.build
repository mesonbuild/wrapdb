if get_option('default_library') != 'static'
  extra_args = ['-DFLAC_API_EXPORTS', '-DFLAC__USE_VISIBILITY_ATTR']
else
  extra_args = ['-DFLAC__NO_DLL']
endif

avx2_args = []

if cc.get_argument_syntax() == 'msvc' and cdata.get('WITH_AVX')
  avx2_args += '/arch:AVX2'
endif

flac_avx2_lib = static_library(
  'flac_avx2',
  files(
    'fixed_intrin_avx2.c',
    'lpc_intrin_avx2.c',
    'lpc_intrin_fma.c',
    'stream_encoder_intrin_avx2.c',
  ),
  pic: true,
  include_directories: [main_inc, 'include'],
  c_args: [avx2_args, extra_args],
  install: false,
)

flac_lib = library(
  'FLAC',
  'bitmath.c',
  'bitreader.c',
  'bitwriter.c',
  'cpu.c',
  'crc.c',
  'fixed.c',
  'fixed_intrin_sse2.c',
  'fixed_intrin_ssse3.c',
  'fixed_intrin_sse42.c',
  'float.c',
  'format.c',
  'lpc.c',
  'lpc_intrin_neon.c',
  'lpc_intrin_sse2.c',
  'lpc_intrin_sse41.c',
  'md5.c',
  'memory.c',
  'metadata_iterators.c',
  'metadata_object.c',
  'stream_decoder.c',
  'stream_encoder.c',
  'stream_encoder_intrin_sse2.c',
  'stream_encoder_intrin_ssse3.c',
  'stream_encoder_framing.c',
  'window.c',
  'ogg_decoder_aspect.c',
  'ogg_encoder_aspect.c',
  'ogg_helper.c',
  'ogg_mapping.c',
  win32_utf8,
  include_directories: [main_inc, 'include'],
  link_whole: flac_avx2_lib,
  c_args: extra_args,
  version: '14.0.0',
  soversion: '14',
  gnu_symbol_visibility: 'hidden',
  dependencies: [ogg_dep, m_dep],
  install: true,
)

flac_dep = declare_dependency(
  compile_args: get_option('default_library') != 'static' ? [] : '-DFLAC__NO_DLL',
  include_directories: main_inc,
  link_with: flac_lib,
)

pconf.generate(
  flac_lib,
  name: 'flac',
  description: 'Free Lossless Audio Codec Library',
)
