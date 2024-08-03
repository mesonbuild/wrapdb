project(
  'sfml',
  'cpp',
  version: '2.6.1',
  default_options: [
    'cpp_std=c++17',
    'wrap_mode=forcefallback',
  ],
  meson_version: '>=0.59.0',
)

cpp = meson.get_compiler('cpp')

graphics_opt = get_option('graphics')
audio_opt = get_option('audio')
window_opt = get_option('window')
network_opt = get_option('network')

gl_dep = dependency('gl')
winmm_dep = cpp.find_library('winmm', required: host_machine.system() == 'windows')
w32_dep = cpp.find_library('ws2_32', required: host_machine.system() == 'windows')

foreach audio_dep : [
    'flac',
    'ogg',
    'openal',
    'vorbis',
    'vorbisenc',
    'vorbisfile',
  ]
  _dep = dependency(audio_dep, required: audio_opt)
  audio_opt = audio_opt.require(_dep.found())
  set_variable(audio_dep + '_dep', _dep)
endforeach

stb_inc = include_directories('extlibs/headers/stb_image')
glad_inc = include_directories('extlibs/headers/glad/include')
vulkan_inc = include_directories('extlibs/headers/vulkan')
mp3_inc = include_directories('extlibs/headers/minimp3')
pub_inc = include_directories('include')
priv_inc = include_directories('src')

summary(
  {
    'audio'   : get_option('audio').allowed(),
    'graphics': get_option('graphics').allowed(),
    'network' : get_option('network').allowed(),
    'window'  : get_option('window').allowed(),
  },
  bool_yn: true,
  section: 'Features',
)

subdir('src/SFML')

if (
  (
  audio_opt.allowed()
  and graphics_opt.allowed()
  and network_opt.allowed()
  and window_opt.allowed()
  ) 
)
  sfml_all_dep = declare_dependency(
    include_directories: pub_inc,
    link_with: [host_machine.system() == 'windows' ? main_lib : []],
    dependencies: [
      sfml_audio_dep,
      sfml_graphics_dep,
      sfml_network_dep,
      sfml_window_dep,
      sfml_system_dep,
    ],
  )
  meson.override_dependency('sfml-all', sfml_all_dep)
endif

if get_option('examples')
  subdir('examples')
endif
