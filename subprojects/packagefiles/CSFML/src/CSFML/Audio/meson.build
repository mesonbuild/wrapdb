audio_sources = files(
  'Listener.cpp',
  'Music.cpp',
  'Sound.cpp',
  'SoundBuffer.cpp',
  'SoundBufferRecorder.cpp',
  'SoundRecorder.cpp',
  'SoundStream.cpp',
)

audio_lib = library(
  'csfml-audio',
  audio_sources,
  link_with: system_lib,
  include_directories: [public_include, private_include],
  dependencies: deps,
  install: true,
)
