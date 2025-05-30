project(
  'gflags',
  'cpp',
  'c',
  version: '2.2.2',
  license: 'BSD-3-Clause',
  meson_version: '>= 0.50',
  default_options: ['c_std=c99', 'default_library=static'],
)

project_version = meson.project_version()
project_components = project_version.split('.')
project_major_version = project_components[0]
project_minor_version = project_components[1]
project_soversion = '@0@.@1@'.format(
  project_major_version,
  project_minor_version,
)

incdir = include_directories('src', 'src/gflags')

is_windows = host_machine.system() == 'windows'
cc = meson.get_compiler('cpp')
if get_option('default_library') == 'static'
  gflags_is_a_dll = false
else
  gflags_is_a_dll = true
endif

subdir('src/gflags')
subdir('src')
