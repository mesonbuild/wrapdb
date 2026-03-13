poppler_poppler_config_h = configure_file(
  configuration: poppler_configuration,
  format: 'cmake',
  input: 'poppler-config.h.cmake',
  output: 'poppler-config.h',
)

poppler_cairo_sources = files(
  'CairoFontEngine.cc',
  'CairoOutputDev.cc',
  'CairoRescaleBox.cc',
)
