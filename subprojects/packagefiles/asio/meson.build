project('asio',
    'cpp',
    version : '1.30.2',
    license : 'BSL-1.0',
    meson_version: '>=0.60.0',
)

asio_deps = []

# For windows builds, ASIO depends on ws2_32
if target_machine.system() == 'windows'
    compiler = meson.get_compiler('cpp')
    ws2_32_dep = compiler.find_library('ws2_32')
    asio_deps += ws2_32_dep
endif

asio_dep = declare_dependency(
    include_directories : include_directories('include'),
    dependencies: asio_deps,
)

install_headers('include/asio.hpp')
install_subdir('include/asio', install_dir: get_option('includedir'))
conf_data = configuration_data()
conf_data.set('prefix', get_option('prefix'))
conf_data.set('exec_prefix', '${prefix}')
conf_data.set('includedir', '${prefix}/' + get_option('includedir'))
conf_data.set('PACKAGE_NAME', meson.project_name())
conf_data.set('PACKAGE_VERSION', meson.project_version())
configure_file(
  input: 'asio.pc.in',
  output: 'asio.pc',
  configuration: conf_data,
  install: true,
  install_tag: 'devel',
  install_dir: get_option('datadir') / 'pkgconfig',
)
