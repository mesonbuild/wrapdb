if host_machine.system() == 'windows'
  cdata.set('SDL_AUDIO_DRIVER_DSOUND', 1)
  #  cdata.set('SDL_AUDIO_DRIVER_WASAPI', 1)
  subdir('directsound')
  #  subdir('wasapi')
elif host_machine.system() == 'darwin'
  subdir('coreaudio')
else
  cdata.set('SDL_AUDIO_DRIVER_PIPEWIRE', 1)
  subdir('pipewire')
endif

# Always include dummy audio driver as fallback
cdata.set('SDL_AUDIO_DRIVER_DUMMY', 1)
subdir('dummy')

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
