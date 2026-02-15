window_sources = files(
  'Clipboard.cpp',
  'Context.cpp',
  'Cursor.cpp',
  'Joystick.cpp',
  'Keyboard.cpp',
  'Mouse.cpp',
  'Sensor.cpp',
  'Touch.cpp',
  'VideoMode.cpp',
  'Vulkan.cpp',
  'Window.cpp',
  'WindowBase.cpp',
)

window_lib = library(
  'csfml-window',
  window_sources,
  link_with: system_lib,
  cpp_args: get_option('default_library') != 'static' ? '-DCSFML_WINDOW_EXPORTS' : '-DCSFML_STATIC',
  include_directories: [public_include, private_include],
  dependencies: deps,
  install: true,
)
