subdir('joystick')
subdir('sound')

#the rest are broken
subdir_done()

executable(
  'opengl',
  'opengl/OpenGL.cpp',
  dependencies: [gl_dep, sfml_dep],
)
executable(
  'window',
  'window/Window.cpp',
  dependencies: [gl_dep, sfml_dep],
)
