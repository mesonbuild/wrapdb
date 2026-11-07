if 'power' in enabled_subsystems
  available_power = {
    'linux': {},
    'macosx': {
      'subdir': 'macos',
    },
    'uikit': {},
    'windows': {},
  }
  power = ''

  if platform_is_windows
    power += ' windows'
  elif platform_is_macos
    power += ' macosx'
  elif platform_is_ios
    power += ' uikit'
  elif platform_is_linux
    power += ' linux'
  endif

  if power != ''
    foreach p : power.split()
      dir = available_power[p].get('subdir', p)
      p_up = p.to_upper()
      cdata.set10(f'SDL_POWER_@p_up@', true)
      subdir(dir)
    endforeach
  else
    cdata.set10('SDL_POWER_HARDWIRED', true)
  endif
endif

sources += files('SDL_power.c')
