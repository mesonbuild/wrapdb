project('sdl2_net', 'c',
    version : '2.0.1',
    license : 'zlib',
    default_options: ['c_std=gnu99'])

sdl2_net_src = files(
    'SDLnet.c',
    'SDLnetselect.c',
    'SDLnetTCP.c',
    'SDLnetUDP.c'
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

sdl2_net = library('sdl2_net',
    sdl2_net_src,
    dependencies : sdl2_dep,
    c_args: plat_args,
    include_directories : '.')

sdl2_net_dep = declare_dependency(
    link_with : [sdl2_net],
    dependencies: plat_libs,
    version : meson.project_version(),
    include_directories : '.')
