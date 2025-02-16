project(
    'argparse',
    'cpp',
    version : '3.2',
    license : 'MIT',
    meson_version : '>=0.60.0',
)

includes = include_directories(['include'])

install_headers([
    'include/argparse/argparse.hpp',
], subdir: 'argparse')

argparse_dep = declare_dependency(
    include_directories: includes
)

conf_data = configuration_data()
conf_data.set('CMAKE_INSTALL_PREFIX', get_option('prefix'))
conf_data.set('CMAKE_INSTALL_INCLUDEDIR', get_option('includedir'))
conf_data.set('PROJECT_NAME', meson.project_name())
conf_data.set('PROJECT_DESCRIPTION', 'A single header argument parser for C++17')
conf_data.set('PROJECT_VERSION', meson.project_version())
configure_file(
  input: 'packaging/pkgconfig.pc.in',
  output: 'argparse.pc',
  configuration: conf_data,
  install: true,
  install_tag: 'devel',
  install_dir: get_option('datadir') / 'pkgconfig',
)
