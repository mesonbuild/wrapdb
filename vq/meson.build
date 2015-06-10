latticebuild = executable('latticebuild',
  'latticebuild.c',
  'vqgen.c',
  'bookutil.c',
  include_directories : [ogg_inc],
  link_with : [vorbis_lib, ogg_lib],
  dependencies : ogg_dep,
)

latticetune = executable('latticetune',
  'latticetune.c',
  'vqgen.c',
  'bookutil.c',
  include_directories : [ogg_inc],
  link_with : [vorbis_lib, ogg_lib],
  dependencies : ogg_dep,
)

huffbuild = executable('huffbuild',
  'huffbuild.c',
  'vqgen.c',
  'bookutil.c',
  include_directories : [ogg_inc],
  link_with : [vorbis_lib, ogg_lib],
  dependencies : ogg_dep,
)
