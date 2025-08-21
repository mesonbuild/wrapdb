project(
  'asio',
  'cpp',
  version: '1.36.0',
  license: 'BSL-1.0',
  meson_version: '>=0.49.0',
)

asio_deps = []

# For windows builds, ASIO depends on ws2_32
if target_machine.system() == 'windows'
  compiler = meson.get_compiler('cpp')
  ws2_32_dep = compiler.find_library('ws2_32')
  asio_deps += ws2_32_dep
endif

asio_dep = declare_dependency(
  include_directories: include_directories('include'),
  dependencies: asio_deps,
)

install_headers('include/asio.hpp')
install_subdir(
  'include/asio',
  install_dir: get_option('includedir'),
)
import('pkgconfig').generate(
  name: meson.project_name(),
  description: 'A cross-platform C++ library for network and low-level I/O programming that provides developers with a consistent asynchronous model using a modern C++ approach.',
  install_dir: get_option('datadir') / 'pkgconfig',
)
