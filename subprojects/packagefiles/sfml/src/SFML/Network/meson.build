network_sources = files(
  'Ftp.cpp',
  'Http.cpp',
  'IpAddress.cpp',
  'Packet.cpp',
  'Socket.cpp',
  'SocketSelector.cpp',
  'TcpListener.cpp',
  'TcpSocket.cpp',
  'UdpSocket.cpp',
  '@0@/SocketImpl.cpp'.format(host_machine.system() == 'windows' ? 'Win32' : 'Unix'),
)

network_lib = library(
  'sfml-network',
  network_sources,
  cpp_args: get_option('default_library') != 'static' ? '-DSFML_NETWORK_EXPORTS' : '-DSFML_STATIC',
  include_directories: [pub_inc, priv_inc],
  link_with: system_lib,
  dependencies: w32_dep,
)

sfml_network_dep = declare_dependency(
  include_directories: pub_inc,
  link_with: network_lib,
  compile_args: get_option('default_library') == 'static' ? '-DSFML_STATIC' : [],
)

meson.override_dependency('sfml-network', sfml_network_dep)
