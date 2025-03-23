project(
  'enet',
  'c',
  version: '1.3.17',
  license: 'mit',
)

cc = meson.get_compiler('c')
c_args = []
deps = []
if host_machine.system() == 'windows'
  deps += cc.find_library('winmm')
  deps += cc.find_library('ws2_32')
  deps += cc.find_library('iphlpapi')
endif

if cc.has_function(
  'gethostbyaddr_r',
  prefix: '#include <netdb.h>',
)
  c_args = c_args + ['-DHAS_GETHOSTBYADDR_R']
endif
if cc.has_function(
  'gethostbyname_r',
  prefix: '#include <netdb.h>',
)
  c_args = c_args + ['-DHAS_GETHOSTBYNAME_R']
endif
if cc.has_function(
  'poll',
  prefix: '#include <sys/poll.h>',
)
  c_args = c_args + ['-DHAS_POLL']
endif
if cc.has_function(
  'fcntl',
  prefix: '#include <fcntl.h>',
)
  c_args = c_args + ['-DHAS_FCNTL']
endif
if cc.has_function(
  'inet_pton',
  prefix: '#include <arpa/inet.h>',
)
  c_args = c_args + ['-DHAS_INET_PTON']
endif
if cc.has_function(
  'inet_ntop',
  prefix: '#include <arpa/inet.h>',
)
  c_args = c_args + ['-DHAS_INET_NTOP']
endif
if cc.has_member(
  'struct msghdr',
  'msg_flags',
  prefix: '#include <sys/socket.h>',
)
  c_args = c_args + ['-DHAS_MSGHDR_FLAGS']
endif
if cc.has_type(
  'socklen_t',
  prefix: '#include <sys/types.h>\n#include <sys/socket.h>',
)
  c_args = c_args + ['-DHAS_SOCKLEN_T']
endif

src = [
  'callbacks.c',
  'compress.c',
  'host.c',
  'list.c',
  'packet.c',
  'peer.c',
  'protocol.c',
  'unix.c',
  'win32.c',
]

incdir = include_directories('include')
enetlib = library(
  'enet',
  sources: src,
  include_directories: incdir,
  dependencies: deps,
  c_args: c_args,
)

enet_dep = declare_dependency(
  include_directories: incdir,
  link_with: enetlib,
)
