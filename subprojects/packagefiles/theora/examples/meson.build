theora_libs = [theora_dep]
theoradec_libs = [theoradec_dep]
theoraenc_libs = [theoraenc_dep, theoradec_dep]

compat_dep = dependency(
  'compat',
  required: host_machine.system() == 'openbsd',
)

if cc.has_header_symbol('unistd.h', 'getopt_long')
  getopt_dep = declare_dependency(
    dependencies: config_dep,
  )
else
  if cc.get_argument_syntax() == 'msvc'
    getopt_sources = files('../win32/getopt.c', '../win32/getopt1.c')
    getopt_incdir = include_directories('../win32/')
  else
    getopt_sources = files('getopt.c', 'getopt1.c')
    getopt_incdir = include_directories('.')
  endif

  getopt_dep = declare_dependency(
    sources: getopt_sources,
    dependencies: config_dep,
    include_directories: [getopt_incdir, incdir],
  )
endif

dump_video_sources = files('dump_video.c')

dump_video = executable(
  'dump_video',
  dump_video_sources,
  c_args: compile_args,
  dependencies: [compat_dep, getopt_dep] + theoradec_libs,
)

dump_psnr_sources = files('dump_psnr.c')

dump_psnr = executable(
  'dump_psnr',
  dump_psnr_sources,
  c_args: compile_args,
  dependencies: [m_dep, getopt_dep] + theoradec_libs,
)

player_example_sources = files('player_example.c')

player_example = executable(
  'player_example',
  player_example_sources,
  c_args: compile_args,
  dependencies: [sdl_dep, vorbis_dep, oss_dep, m_dep, getopt_dep, config_dep] + theoradec_libs,
)

# Upstream defines a rint substitute
if host_machine.system() == 'windows' and not cc.has_header_symbol(
  'math.h',
  'rint',
)
  encoder_example_sources = files('encoder_example.c')

  encoder_example = executable(
    'encoder_example',
    encoder_example_sources,
    c_args: compile_args,
    dependencies: [ogg_dep, vorbis_dep, vorbisenc_dep, m_dep, getopt_dep] + theoraenc_libs,
  )
endif

png2theora_sources = files('png2theora.c')

png2theora = executable(
  'png2theora',
  png2theora_sources,
  c_args: compile_args,
  dependencies: [ogg_dep, libpng_dep, unistd_dep, m_dep, getopt_dep, config_dep] + theoraenc_libs,
)
