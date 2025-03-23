wire_src = files('src/Wire.cpp', 'src/utility/twi.c')

wire_inc = ['src/']

arduinocore_wire_lib = static_library(
  'arduinocore-wire-' + cross_variant,
  wire_src,
  include_directories: include_directories(wire_inc),
  dependencies: [arduinocore_dep],
  install: do_install,
  install_dir: 'lib/avr/lib',
)
arduinocore_wire_dep = declare_dependency(
  link_with: arduinocore_wire_lib,
  include_directories: include_directories(wire_inc),
  dependencies: [arduinocore_dep],
)

if do_install
  install_headers(
    ['src/Wire.h'],
    install_dir: 'lib/avr/include/arduino/Wire',
  )
endif
