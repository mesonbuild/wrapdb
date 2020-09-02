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

sdl2_dep = dependency('sdl2', fallback : ['sdl2', 'sdl2_dep'], required: true)

sdl2_net = library('sdl2_net',
    sdl2_net_src,
    dependencies : sdl2_dep,
    include_directories : '.')

sdl2_net_dep = declare_dependency(
    link_with : sdl2_net,
    version : meson.project_version(),
    include_directories : '.')
