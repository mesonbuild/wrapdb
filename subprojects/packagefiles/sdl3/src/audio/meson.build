if 'audio' in enabled_subsystems
  if platform_is_windows
    cdata.set('SDL_AUDIO_DRIVER_DSOUND', 1)
    #  cdata.set('SDL_AUDIO_DRIVER_WASAPI', 1)
    subdir('directsound')
    #  subdir('wasapi')
  elif platform_is_apple
    cdata.set('SDL_AUDIO_DRIVER_COREAUDIO', 1)
    subdir('coreaudio')
  else
    cdata.set('SDL_AUDIO_DRIVER_PIPEWIRE', 1)
    subdir('pipewire')
  endif
else
  subdir('dummy')
endif

sources += files(
  'SDL_audio.c',
  'SDL_audiocvt.c',
  'SDL_audiodev.c',
  'SDL_audioqueue.c',
  'SDL_audioresample.c',
  'SDL_audiotypecvt.c',
  'SDL_mixer.c',
  'SDL_wave.c',
)
