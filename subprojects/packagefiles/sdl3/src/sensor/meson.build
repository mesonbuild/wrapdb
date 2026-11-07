available_sensors = {
  'coremotion': {},
  'dummy': {},
  'windows': {},
}
sensors = ''

if 'sensor' in enabled_subsystems
  if cdata.get('HAVE_SENSORSAPI_H', 0) != 0
    sensors += ' windows'
  endif

  if platform_is_ios
    sensors += ' coremotion'
  endif
endif

if sensors == ''
  sensors += ' dummy'
endif

sources += files('SDL_sensor.c')

foreach s : sensors.split()
  dir = available_sensors[s].get('subdir', s)
  s_up = s.to_upper()
  cdata.set10(f'SDL_SENSOR_@s_up@', true)
  subdir(dir)
endforeach
