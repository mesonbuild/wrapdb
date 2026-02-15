network_sources = files(
  'Ftp.cpp',
  'Http.cpp',
  'IpAddress.cpp',
  'Packet.cpp',
  'SocketSelector.cpp',
  'TcpListener.cpp',
  'TcpSocket.cpp',
  'UdpSocket.cpp',
)

network_lib = library(
  'csfml-network',
  network_sources,
  link_with: system_lib,
  include_directories: [public_include, private_include],
  dependencies: deps,
  install: true,
)
