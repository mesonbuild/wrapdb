hid_src = files('src/HID.cpp')

hid_inc = ['src/']

arduinocore_hid_lib = static_library(
  'arduinocore-hid-' + cross_variant,
  hid_src,
  include_directories: include_directories(hid_inc),
  dependencies: [arduinocore_dep],
  install: do_install,
  install_dir: 'lib/avr/lib',
)
arduinocore_hid_dep = declare_dependency(
  link_with: arduinocore_hid_lib,
  include_directories: include_directories(hid_inc),
  dependencies: [arduinocore_dep],
)

if do_install
  install_headers(
    ['src/HID.h'],
    install_dir: 'lib/avr/include/arduino/HID',
  )
endif
