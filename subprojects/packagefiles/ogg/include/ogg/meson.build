cc = meson.get_compiler('c')

cdata = configuration_data()
cdata.set10('INCLUDE_INTTYPES_H', cc.has_header('inttypes.h'))
cdata.set10('INCLUDE_STDINT_H', cc.has_header('stdint.h'))
cdata.set10('INCLUDE_SYS_TYPES_H', cc.has_header('sys/types.h'))

# stdint.h is everywhere we care about.

cdata.set('SIZE16', 'int16_t')
cdata.set('USIZE16', 'uint16_t')
cdata.set('SIZE32', 'int32_t')
cdata.set('USIZE32', 'uint32_t')
cdata.set('SIZE64', 'int64_t')
cdata.set('USIZE64', 'uint64_t')

cfile = configure_file(
  input: 'config_types.h.in',
  output: 'config_types.h',
  format: 'cmake@',
  configuration: cdata,
)

headers = files('ogg.h', 'os_types.h')
install_headers(
  cfile,
  headers,
  subdir: 'ogg',
)
