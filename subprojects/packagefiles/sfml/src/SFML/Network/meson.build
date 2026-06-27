network_sources = files(
  '@0@/SocketImpl.cpp'.format(
    host_machine.system() == 'windows' ? 'Win32' : 'Unix',
  ),
  'Dns.cpp',
  'Ftp.cpp',
  'Http.cpp',
  'IpAddress.cpp',
  'Packet.cpp',
  'Sftp.cpp',
  'Socket.cpp',
  'SocketSelector.cpp',
  'TcpListener.cpp',
  'TcpSocket.cpp',
  'UdpSocket.cpp',
)

network_deps = []

if host_machine.system() == 'windows'
  foreach lib : ['ws2_32', 'Crypt32', 'Dnsapi']
    network_win_deps += cpp.find_library(lib, required: true)
  endforeach
endif

if host_machine.system() in ['linux', 'darwin']
  network_deps += cpp.find_library('resolv', required: true)
endif

network_deps += [
  dependency('mbedtls'),
  dependency('mbedcrypto'),
  dependency('mbedx509'),
  dependency(
    'libssh2',
    default_options: [
      'crypto_backend=mbedtls',
      'examples=false',
    ],
  )
]

network_inc = [pub_inc, priv_inc]

if host_machine.system() == 'windows'
  network_inc += wepoll_inc
endif

network_link_args = []

if host_machine.system() == 'darwin'
  network_link_args = [
    '-framework Security',
    '-framework CoreFoundation',
  ]
endif

network_lib = library(
  'sfml-network',
  network_sources,
  cpp_args: get_option('default_library') != 'static' ? '-DSFML_NETWORK_EXPORTS' : '-DSFML_STATIC',
  include_directories: network_inc,
  link_with: system_lib,
  link_args: network_link_args,
  dependencies: network_deps,
  override_options: override_opts,
  install: true,
)
