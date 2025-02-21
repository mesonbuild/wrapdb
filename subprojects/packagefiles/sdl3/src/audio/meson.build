if host_machine.system() == 'windows'
  cdata.set('SDL_AUDIO_DRIVER_DSOUND', 1)
#  cdata.set('SDL_AUDIO_DRIVER_WASAPI', 1)
  subdir('directsound')
#  subdir('wasapi')
else
  cdata.set('SDL_AUDIO_DRIVER_PIPEWIRE', 1)
  subdir('pipewire')
endif

sources += files(
  'SDL_audiodev.c',
  'SDL_audioresample.c',
  'SDL_audioqueue.c',
  'SDL_audio.c',
  'SDL_audiocvt.c',
  'SDL_wave.c',
  'SDL_audiotypecvt.c',
  'SDL_mixer.c',
)
