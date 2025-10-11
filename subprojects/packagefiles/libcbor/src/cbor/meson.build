version = meson.project_version().split('.')
config = configuration_data()
config.set('CBOR_VERSION_MAJOR', version[0])
config.set('CBOR_VERSION_MINOR', version[1])
config.set('CBOR_VERSION_PATCH', version[2])
config.set('CBOR_BUFFER_GROWTH', get_option('buffer_growth'))
config.set('CBOR_MAX_STACK_SIZE', get_option('max_stack_size'))
config.set('CBOR_PRETTY_PRINTER', get_option('pretty_printer'))
config.set('CBOR_RESTRICT_SPECIFIER', cc.get_id() == 'msvc' ? '' : 'restrict')
config.set('CBOR_INLINE_SPECIFIER', '')

config_file = configure_file(
  input: 'configuration.h.in',
  output: 'configuration.h',
  format: 'cmake',
  configuration: config,
  install: true,
  install_dir: get_option('includedir') / 'cbor',
)
