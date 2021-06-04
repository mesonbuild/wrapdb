project('sdl2 mixer', 'c')

sdl2_dep = dependency('sdl2')
ogg_dep = dependency('ogg')
vorbis_dep = dependency('vorbis')
vorbisfile_dep = dependency('vorbisfile')

feature_args = ['-DMUSIC_WAV', '-DMUSIC_OGG']

sdl2_mixer_lib = library('sdl2mixer',
  'effect_position.c',
  'effect_stereoreverse.c',
  'effects_internal.c',
  'load_aiff.c',
  'load_voc.c',
  'mixer.c',
  'music_cmd.c',
  'music_flac.c',
  'music_fluidsynth.c',
  'music_mad.c',
  'music_mikmod.c',
  'music_modplug.c',
  'music_mpg123.c',
  'music_nativemidi.c',
  'music_ogg.c',
  'music_opus.c',
  'music_timidity.c',
  'music_wav.c',
  'music.c',
  c_args: [feature_args],
  dependencies: [vorbisfile_dep, vorbis_dep, ogg_dep, sdl2_dep],
)

executable('playmus', 'playmus.c',
  dependencies: sdl2_dep,
  link_with: sdl2_mixer_lib)

sdl2_mixer_dep = declare_dependency(include_directories: '.',
  link_with: sdl2_mixer_lib)
