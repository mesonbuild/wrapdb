project('vorbis', 'c', version : '1.3.5', license : 'bsd-style')

ogg_dep = dependency('ogg')

incdir = include_directories('include')
subdir('lib')
if host_machine.system() != 'windows'
  # These don't seem to build on Windows.
  subdir('vq')
endif
subdir('test')
