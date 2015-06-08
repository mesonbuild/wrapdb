project('vorbis', 'c')

ogg_dep = dependency('ogg', required : false)

if not ogg_dep.found()
  ogg_proj = subproject('ogg')
  ogg_inc = ogg_proj.get_variable('incdir')
  ogg_lib = ogg_proj.get_variable('libogg')
else
  ogg_inc = []
  ogg_lib = []
endif

if get_option('shared_lib')
  libtype = 'shared_library'
else
  libtype = 'static_library'
endif

incdir = include_directories('include')
subdir('lib')
subdir('vq')
subdir('test')
