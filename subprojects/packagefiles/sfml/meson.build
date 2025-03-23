project(
  'sfml',
  'cpp',
  version: '2.6.2',
  default_options: ['cpp_std=c++17', 'wrap_mode=forcefallback'],
  meson_version: '>=0.49.0',
)

cpp = meson.get_compiler('cpp')

openal_dep = dependency('openal')
thread_dep = dependency('threads')
gl_dep = dependency('gl')
winmm_dep = cpp.find_library(
  'winmm',
  required: host_machine.system() == 'windows',
)
w32_dep = cpp.find_library(
  'ws2_32',
  required: host_machine.system() == 'windows',
)
freetype_dep = dependency('freetype2')
flac_dep = dependency('flac')
ogg_dep = dependency('ogg')
vorbis_dep = dependency('vorbis')
vorbisenc_dep = dependency('vorbisenc')
vorbisfile_dep = dependency('vorbisfile')

stb_inc = include_directories('extlibs/headers/stb_image')
glad_inc = include_directories('extlibs/headers/glad/include')
vulkan_inc = include_directories('extlibs/headers/vulkan')
mp3_inc = include_directories('extlibs/headers/minimp3')
pub_inc = include_directories('include')
priv_inc = include_directories('src')

subdir('src/SFML')

sfml_dep = declare_dependency(
  include_directories: pub_inc,
  link_with: [
    audio_lib,
    graphics_lib,
    network_lib,
    window_lib,
    system_lib,
    host_machine.system() == 'windows' ? main_lib : [],
  ],
  compile_args: get_option('default_library') == 'static' ? '-DSFML_STATIC' : [],
)

subdir('examples')
