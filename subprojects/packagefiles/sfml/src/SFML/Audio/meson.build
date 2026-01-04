audio_sources = files(
  'AudioDevice.cpp',
  'AudioResource.cpp',
  'InputSoundFile.cpp',
  'Listener.cpp',
  'Miniaudio.cpp',
  'MiniaudioUtils.cpp',
  'Music.cpp',
  'OutputSoundFile.cpp',
  'PlaybackDevice.cpp',
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

audio_cpp_args = []

audio_cpp_args += get_option('default_library') != 'static' ? '-DSFML_AUDIO_EXPORTS' : '-DSFML_STATIC'

# avoids warnings in vorbisfile.h
audio_cpp_args += ['-DPRIVATE OV_EXCLUDE_STATIC_CALLBACKS', '-DFLAC__NO_DLL']

# disable miniaudio features we do not use
audio_cpp_args += [
  '-DMA_NO_MP3',
  '-DMA_NO_FLAC',
  '-DMA_NO_ENCODING',
  '-DMA_NO_RESOURCE_MANAGER',
  '-DMA_NO_GENERATION',
]

# use standard fixed-width integer types
audio_cpp_args += '-DMA_USE_STDINT'

miniaudio_dep = dependency('miniaudio')
flac_dep = dependency('flac')
vorbis_dep = dependency('vorbis')
vorbisenc_dep = dependency('vorbisenc')
vorbisfile_dep = dependency('vorbisfile')
ogg_dep = dependency('ogg')

audio_lib = library(
  'sfml-audio',
  audio_sources,
  cpp_args: audio_cpp_args,
  link_with: system_lib,
  include_directories: [pub_inc, priv_inc, mp3_inc],
  override_options: override_opts,
  dependencies: [
    miniaudio_dep,
    flac_dep,
    vorbis_dep,
    vorbisenc_dep,
    vorbisfile_dep,
    ogg_dep,
  ],
)
