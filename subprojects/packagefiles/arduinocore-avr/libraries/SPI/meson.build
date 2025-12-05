spi_src = files('src/SPI.cpp')

spi_inc = ['src/']

arduinocore_spi_lib = static_library(
  'arduinocore-spi-' + cross_variant,
  spi_src,
  include_directories: include_directories(spi_inc),
  dependencies: [arduinocore_dep],
  install: do_install,
  install_dir: 'lib/avr/lib',
)
arduinocore_spi_dep = declare_dependency(
  link_with: arduinocore_spi_lib,
  include_directories: include_directories(spi_inc),
  dependencies: [arduinocore_dep],
)
meson.override_dependency('arduinocore-spi', arduinocore_spi_dep)

if do_install
  install_headers(
    ['src/SPI.h'],
    install_dir: 'lib/avr/include/arduino/SPI',
  )
endif
