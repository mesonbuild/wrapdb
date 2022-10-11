project(
  'sdl2_net',
  'c',
  version: '2.2.0',
  license: 'zlib',
  default_options: ['c_std=gnu99'],
)

sdl2_net_src = files(
  'SDLnet.c',
  'SDLnetTCP.c',
  'SDLnetUDP.c',
  'SDLnetselect.c',
)

cc = meson.get_compiler('c')

if host_machine.system() == 'windows'
  plat_args = ['-DWIN32']
  plat_libs = [cc.find_library('ws2_32'), cc.find_library('iphlpapi')]
else
  plat_args = []
  plat_libs = []
endif

sdl2_dep = dependency('sdl2')

sdl2_net = library(
  'sdl2_net',
  sdl2_net_src,
  dependencies: [sdl2_dep, plat_libs],
  c_args: plat_args,
)

sdl2_net_dep = declare_dependency(
  link_with: sdl2_net,
  dependencies: plat_libs,
  include_directories: '.',
)
