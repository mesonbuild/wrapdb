cc = meson.get_compiler('c')

cdata = configuration_data()

cdata.set10('INCLUDE_INTTYPES_H', cc.has_header('inttypes.h'))
cdata.set10('INCLUDE_SYS_TYPES_H', cc.has_header('sys/types.h'))

cc.has_header(
  'stdint.h',
  required: true,
)
cdata.set('SIZE16', 'int16_t')
cdata.set('USIZE16', 'uint16_t')
cdata.set('SIZE32', 'int32_t')
cdata.set('USIZE32', 'uint32_t')

configure_file(
  input: 'speexdsp_config_types.h.meson',
  output: 'speexdsp_config_types.h',
  install_dir: join_paths(get_option('includedir'), 'speex'),
  configuration: cdata,
)

headers = [
  'speex_buffer.h',
  'speexdsp_types.h',
  'speex_echo.h',
  'speex_jitter.h',
  'speex_preprocess.h',
  'speex_resampler.h',
]

install_headers(
  headers,
  subdir: 'speex',
)
