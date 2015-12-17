project('vorbis', 'c', version : '1.3.5', license : 'bsd-style')

ogg_dep = dependency('ogg', required : false)

if not ogg_dep.found()
  ogg_proj = subproject('ogg')
  ogg_inc = ogg_proj.get_variable('incdir')
  ogg_lib = ogg_proj.get_variable('libogg')
else
  ogg_inc = []
  ogg_lib = []
endif

incdir = include_directories('include')
subdir('lib')
subdir('vq')
subdir('test')
