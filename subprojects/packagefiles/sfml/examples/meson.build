examples_inc = include_directories('include')

subdir('ftp')
subdir('http')
subdir('sftp')
subdir('sockets')
subdir('voip')
subdir('sound')
subdir('sound_capture')
subdir('sound_device')

subdir('window')
subdir('event_handling')
subdir('opengl')
subdir('stencil')
subdir('text')

subdir('joystick')
subdir('shader')
subdir('island')
subdir('vulkan')

if host_machine.system() == 'windows'
  subdir('win32')
  subdir('raw_input')
elif host_machine.system() in ['linux', 'freebsd', 'openbsd']
  subdir('X11')
  subdir('raw_input')
elif host_machine.system() == 'darwin'
  # Not implemented
  # subdir('cocoa')
endif

subdir('tennis')
subdir('keyboard')
subdir('sound_effects')
