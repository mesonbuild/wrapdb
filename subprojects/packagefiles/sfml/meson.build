project('sfml', 'cpp',
    version: '2.5.1',
    default_options: ['cpp_std=c++17',
                      'wrap_mode=forcefallback',
                     ])

cpp = meson.get_compiler('cpp')

stb_dep = dependency('stb')
openal_dep = dependency('openal')
thread_dep = dependency('threads')
gl_dep = dependency('gl')
winmm_dep = cpp.find_library('winmm', required: false)
w32_dep = cpp.find_library('ws2_32', required: false)
freetype_dep = dependency('freetype2')
flac_dep = dependency('flac')
ogg_dep = dependency('ogg')
vorbis_dep = dependency('vorbis')
vorbisenc_dep = dependency('vorbisenc')
vorbisfile_dep = dependency('vorbisfile')

pub_inc = include_directories('include')
priv_inc = include_directories('src')

subdir('src/SFML')

sfml_dep = declare_dependency(include_directories: 'include',
    link_with: [audio_lib,
                graphics_lib,
                network_lib,
                window_lib,
                system_lib] + (host_machine.system() == 'windows' ? [main_lib] : []),
    compile_args: get_option('default_library') == 'shared' ? [] : ['-DSFML_STATIC'],
)
