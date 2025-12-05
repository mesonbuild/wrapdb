eeprom_inc = ['src/']

arduinocore_eeprom_dep = declare_dependency(
  include_directories: include_directories(eeprom_inc),
)
meson.override_dependency('arduinocore-eeprom', arduinocore_eeprom_dep)

if do_install
  install_headers(
    ['src/EEPROM.h'],
    install_dir: 'lib/avr/include/arduino/EEPROM',
  )
endif
