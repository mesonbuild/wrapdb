install_headers(
  'Config.h',
  subdir: 'CSFML',
)
install_headers(
  'GPUPreference.h',
  subdir: 'CSFML',
)
install_headers(
  'OpenGL.h',
  subdir: 'CSFML',
)

install_headers(
  'System.h',
  subdir: 'CSFML',
)
install_subdir(
  'System',
  install_dir: 'include/CSFML',
)

if host_machine.system() == 'windows'
  install_subdir(
    'Main',
    install_dir: 'include/CSFML',
  )
endif

if get_option('window') or get_option('graphics')
  install_headers(
    'Window.h',
    subdir: 'CSFML',
  )
  install_subdir(
    'Window',
    install_dir: 'include/CSFML',
  )
endif

if get_option('network')
  install_headers(
    'Network.h',
    subdir: 'CSFML',
  )
  install_subdir(
    'Network',
    install_dir: 'include/CSFML',
  )
endif

if get_option('graphics')
  install_headers(
    'Graphics.h',
    subdir: 'CSFML',
  )
  install_subdir(
    'Graphics',
    install_dir: 'include/CSFML',
  )
endif

if get_option('audio')
  install_headers(
    'Audio.h',
    subdir: 'CSFML',
  )
  install_subdir(
    'Audio',
    install_dir: 'include/CSFML',
  )
endif
