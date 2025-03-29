soundtouch_headers = files(
  'BPMDetect.h',
  'FIFOSampleBuffer.h',
  'FIFOSamplePipe.h',
  'STTypes.h',
  'SoundTouch.h',
)

soundtouch_config_h = configure_file(
  output: 'soundtouch_config.h',
  configuration: conf,
)

soundtouch_includes = include_directories('.')

install_headers(
  [soundtouch_headers, soundtouch_config_h],
  subdir: 'soundtouch',
)
