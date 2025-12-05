project(
  'libarduinocore-avr',
  'c',
  'cpp',
  version: '1.8.2',
  license: 'LGPL-2.1-or-later',
  default_options: [
    'b_lto=true',
    'c_std=gnu11',
    'cpp_std=gnu++11',
    'b_staticpic=false',
  ],
  meson_version: '>=0.54.0',
)
assert(
  meson.is_cross_build(),
  'Arduino projects can only be built in a cross build environment.',
)
# variant has to be defined in a cross file depending on your board
# It must be set to one of the following values:
#   circuitplay32u4
#   eightanaloginputs
#   ethernet
#   gemma
#   leonardo
#   mega
#   micro
#   robot_control
#   robot_motor
#   standard
#   yun
cross_variant = meson.get_external_property('variant')
# whether install definitions are added (not when compiling as subproject)
do_install = not meson.is_subproject()


arduinocore_src = files(
  'cores/arduino/CDC.cpp',
  'cores/arduino/HardwareSerial.cpp',
  'cores/arduino/HardwareSerial0.cpp',
  'cores/arduino/HardwareSerial1.cpp',
  'cores/arduino/HardwareSerial2.cpp',
  'cores/arduino/HardwareSerial3.cpp',
  'cores/arduino/IPAddress.cpp',
  'cores/arduino/PluggableUSB.cpp',
  'cores/arduino/Print.cpp',
  'cores/arduino/Stream.cpp',
  'cores/arduino/Tone.cpp',
  'cores/arduino/USBCore.cpp',
  'cores/arduino/WInterrupts.c',
  'cores/arduino/WMath.cpp',
  'cores/arduino/WString.cpp',
  'cores/arduino/abi.cpp',
  'cores/arduino/hooks.c',
  'cores/arduino/new.cpp',
  'cores/arduino/wiring.c',
  'cores/arduino/wiring_analog.c',
  'cores/arduino/wiring_digital.c',
  'cores/arduino/wiring_pulse.c',
  'cores/arduino/wiring_shift.c',
)
arduinocore_inc = ['cores/arduino', 'variants/' + cross_variant]

arduinocore_main_src = files('cores/arduino/main.cpp')


includes = include_directories([arduinocore_inc])

# Dependencies will use this include_directories to suppress warnings in the Arduino headers
includes_sys = include_directories(
  [arduinocore_inc],
  is_system: true,
)

arduinocore_lib = static_library(
  'arduinocore-' + cross_variant,
  arduinocore_src,
  include_directories: [includes],
  install: do_install,
  install_dir: 'lib/avr/lib',
  # Only build in a subproject if the dependency is used
  build_by_default: meson.is_subproject() == false,
)
arduinocore_dep = declare_dependency(
  include_directories: [includes_sys],
  link_with: arduinocore_lib,
)
meson.override_dependency('arduinocore', arduinocore_dep)

arduinocore_main_lib = static_library(
  'arduinocore-main-' + cross_variant,
  arduinocore_main_src,
  include_directories: [includes],
  install: do_install,
  install_dir: 'lib/avr/lib',
  # Only build in a subproject if the dependency is used
  build_by_default: meson.is_subproject() == false,
)
arduinocore_main_dep = declare_dependency(
  link_with: arduinocore_main_lib,
  dependencies: [arduinocore_dep],
)
meson.override_dependency('arduinocore-main', arduinocore_main_dep)


subdir('libraries/')


if do_install
  arduinocore_header = files(
    'cores/arduino/Arduino.h',
    'cores/arduino/Client.h',
    'cores/arduino/HardwareSerial.h',
    'cores/arduino/HardwareSerial_private.h',
    'cores/arduino/IPAddress.h',
    'cores/arduino/PluggableUSB.h',
    'cores/arduino/Print.h',
    'cores/arduino/Printable.h',
    'cores/arduino/Server.h',
    'cores/arduino/Stream.h',
    'cores/arduino/USBAPI.h',
    'cores/arduino/USBCore.h',
    'cores/arduino/USBDesc.h',
    'cores/arduino/Udp.h',
    'cores/arduino/WCharacter.h',
    'cores/arduino/WString.h',
    'cores/arduino/binary.h',
    'cores/arduino/new.h',
    'cores/arduino/wiring_private.h',
  )
  install_headers(
    arduinocore_header,
    install_dir: 'lib/avr/include/arduino',
  )
  install_headers(
    ['variants/' + cross_variant + '/pins_arduino.h'],
    install_dir: 'lib/avr/include/arduino/variants/' + cross_variant,
  )
endif

