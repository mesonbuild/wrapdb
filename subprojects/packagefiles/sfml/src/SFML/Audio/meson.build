audio_sources = files(
  'ALCheck.cpp',
  'AlResource.cpp',
  'AudioDevice.cpp',
  'InputSoundFile.cpp',
  'Listener.cpp',
  'Music.cpp',
  'OutputSoundFile.cpp',
  'Sound.cpp',
  'SoundBuffer.cpp',
  'SoundBufferRecorder.cpp',
  'SoundFileFactory.cpp',
  'SoundFileReaderFlac.cpp',
  'SoundFileReaderMp3.cpp',
  'SoundFileReaderOgg.cpp',
  'SoundFileReaderWav.cpp',
  'SoundFileWriterFlac.cpp',
  'SoundFileWriterOgg.cpp',
  'SoundFileWriterWav.cpp',
  'SoundRecorder.cpp',
  'SoundSource.cpp',
  'SoundStream.cpp',
)

openal_dep = dependency('openal')
flac_dep = dependency('flac')
vorbis_dep = dependency('vorbis')
vorbisenc_dep = dependency('vorbisenc')
vorbisfile_dep = dependency('vorbisfile')
ogg_dep = dependency('ogg')

audio_lib = library(
  'sfml-audio',
  audio_sources,
  cpp_args: get_option('default_library') != 'static' ? '-DSFML_AUDIO_EXPORTS' : '-DSFML_STATIC',
  link_with: system_lib,
  include_directories: [pub_inc, priv_inc, mp3_inc],
  dependencies: [openal_dep, flac_dep, vorbis_dep, vorbisenc_dep, vorbisfile_dep, ogg_dep],
)

sfml_audio_dep = declare_dependency(
  include_directories: pub_inc,
  link_with: audio_lib,
  compile_args: get_option('default_library') == 'static' ? '-DSFML_STATIC' : [],
)

meson.override_dependency('sfml-audio', sfml_audio_dep)
