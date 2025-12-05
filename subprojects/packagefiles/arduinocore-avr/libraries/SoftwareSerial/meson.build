softwareserial_src = files('src/SoftwareSerial.cpp')

softwareserial_inc = ['src/']

arduinocore_softwareserial_lib = static_library(
  'arduinocore-softwareserial-' + cross_variant,
  softwareserial_src,
  include_directories: include_directories(softwareserial_inc),
  dependencies: [arduinocore_dep],
  install: do_install,
  install_dir: 'lib/avr/lib',
)
arduinocore_softwareserial_dep = declare_dependency(
  link_with: arduinocore_softwareserial_lib,
  include_directories: include_directories(softwareserial_inc),
  dependencies: [arduinocore_dep],
)
meson.override_dependency(
  'arduinocore-softwareserial',
  arduinocore_softwareserial_dep,
)

if do_install
  install_headers(
    ['src/SoftwareSerial.h'],
    install_dir: 'lib/avr/include/arduino/SoftwareSerial',
  )
endif
