project(
  'gumbo',
  'c',
  version: '0.12.1',
  default_options: 'c_std=c99',
)

cc = meson.get_compiler('c')

cpp_available = add_languages(
  'cpp',
  required: false,
)
if cpp_available
  cpp = meson.get_compiler('cpp')
endif

subdir('src')
subdir('examples')
subdir('tests')
