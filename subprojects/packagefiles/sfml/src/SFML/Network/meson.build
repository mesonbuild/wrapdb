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
)

if host_machine.system() == 'windows'
    network_sources += files('Win32/SocketImpl.cpp')
else
    network_sources += files('Unix/SocketImpl.cpp')
endif

network_lib = library('sfml-network',
    network_sources,
    cpp_args: get_option('default_library') == 'shared' ? ['-DSFML_NETWORK_EXPORTS'] : ['-DSFML_STATIC'],
    include_directories: [pub_inc, priv_inc],
    link_with: [system_lib],
    dependencies: [w32_dep],
)
