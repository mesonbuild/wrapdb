# To check if the compiler support c++20
if meson.get_compiler('cpp').has_header(
  'bit',
  required: get_option('examples'),
)
  subdir('component')
  subdir('dom')
endif
