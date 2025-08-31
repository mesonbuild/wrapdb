network_sources = files(
  '@0@/SocketImpl.cpp'.format(
    host_machine.system() == 'windows' ? 'Win32' : 'Unix',
  ),
  'Ftp.cpp',
  'Http.cpp',
  'IpAddress.cpp',
  'Packet.cpp',
  'Socket.cpp',
  'SocketSelector.cpp',
  'TcpListener.cpp',
  'TcpSocket.cpp',
  'UdpSocket.cpp',
)

network_lib = library(
  'sfml-network',
  network_sources,
  cpp_args: get_option('default_library') != 'static' ? '-DSFML_NETWORK_EXPORTS' : '-DSFML_STATIC',
  include_directories: [pub_inc, priv_inc],
  link_with: system_lib,
  dependencies: w32_dep,
  override_options: override_opts,
)
