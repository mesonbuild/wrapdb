available_audio_drivers = {
  'alsa': {},
  'coreaudio': {},
  'disk': {},
  'dummy': {},
  'dsound': {
    'subdir': 'directsound',
  },
  'jack': {},
  'oss': {
    'subdir': 'dsp',
  },
  'pipewire': {},
  'pulseaudio': {},
  'netbsd': {},
  'sndio': {},
  'wasapi': {},
}
audio_drivers = ''

if sdl_audio
  if opt_audio_disk.allowed()
    audio_drivers += ' disk'
  endif

  if platform_is_netbsd
    audio_drivers += ' netbsd'
  endif

  if opt_audio_oss.enable_auto_if(oss_default).enabled()
    oss_available = cc.compiles(
      '''
      #include <sys/soundcard.h>
      int main(int argc, char **argv) { int arg = SNDCTL_DSP_SETFRAGMENT; return 0; }''',
    )
    if oss_available
      audio_drivers += ' oss'
    endif
  endif

  if opt_audio_alsa.enable_auto_if(platform_is_unixlike).enabled()
    alsa_dep = dependency(
      'alsa',
      required: opt_audio_alsa,
    )
    sdl_deps += alsa_dep
    if alsa_dep.found()
      audio_drivers += ' alsa'
      dlopen_table += {
        'option': opt_audio_alsa_shared,
        'dep_var': 'alsa_dep',
        'lib': 'asound',
        'conf_var': 'SDL_AUDIO_DRIVER_ALSA_DYNAMIC',
      }
    endif
  endif

  if opt_audio_jack.enable_auto_if(platform_is_unixlike).enabled()
    jack_dep = dependency(
      'jack',
      required: opt_audio_jack,
    )
    sdl_deps += jack_dep
    if jack_dep.found()
      audio_drivers += ' jack'
      dlopen_table += {
        'option': opt_audio_jack_shared,
        'dep_var': 'jack_dep',
        'lib': 'jack',
        'conf_var': 'SDL_AUDIO_DRIVER_JACK_DYNAMIC',
      }
    endif
  endif

  if have_pipewire
    audio_drivers += ' pipewire'
    dlopen_table += {
      'option': opt_pipewire_shared,
      'dep_var': 'pipewire_dep',
      'lib': 'pipewire-0.3',
      'conf_var': 'SDL_AUDIO_DRIVER_PIPEWIRE_DYNAMIC',
    }
  endif

  if opt_audio_pulseaudio.enable_auto_if(platform_is_unixlike).enabled()
    pulseaudio_dep = dependency(
      'libpulse-simple',
      required: opt_audio_pulseaudio,
    )
    sdl_deps += pulseaudio_dep
    if pulseaudio_dep.found()
      audio_drivers += ' pulseaudio'
      dlopen_table += {
        'option': opt_audio_pulseaudio_shared,
        'dep_var': 'pulseaudio_dep',
        'lib': 'pulse-simple',
        'conf_var': 'SDL_AUDIO_DRIVER_PULSEAUDIO_DYNAMIC',
      }
    endif
  endif

  if opt_audio_sndio.enable_auto_if(platform_is_unixlike).enabled()
    sndio_dep = dependency(
      'sndio',
      required: opt_audio_sndio,
    )
    sdl_deps += sndio_dep
    if sndio_dep.found()
      audio_drivers += ' sndio'
      dlopen_table += {
        'option': opt_audio_sndio_shared,
        'dep_var': 'sndio_dep',
        'lib': 'sndio',
        'conf_var': 'SDL_AUDIO_DRIVER_SNDIO_DYNAMIC',
      }
    endif
  endif

  if platform_is_windows
    if cdata.get('HAVE_DSOUND_H', 0) != 0
      audio_drivers += ' dsound'
    endif

    if opt_audio_wasapi.allowed()
      audio_drivers += ' wasapi'
    endif
  endif

  if platform_is_apple
    audio_drivers += ' coreaudio'
  endif
endif

if opt_audio_dummy.allowed() or audio_drivers == ''
  audio_drivers += ' dummy'
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

foreach ad : audio_drivers.split()
  dir = available_audio_drivers[ad].get('subdir', ad)
  ad_up = ad.to_upper()
  cdata.set10(f'SDL_AUDIO_DRIVER_@ad_up@', true)
  subdir(dir)
endforeach

enabled_audio = ''
foreach ad : available_audio_drivers.keys()
  ad_up = ad.to_upper()
  if cdata.get(f'SDL_AUDIO_DRIVER_@ad_up@', 0) != 0
    enabled_audio += f'@ad@ '
  endif
endforeach
