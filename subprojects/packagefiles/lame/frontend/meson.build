common_sources = files(
  'brhist.c',
  'console.c',
  'get_audio.c',
  'lametime.c',
  'main.c',
  'parse.c',
  'timestatus.c',
)

frontend_includes = mp3lame_includes + [include_directories('.')]

tools_deps = [lame_dep, m_dep, iconv_dep, curses_dep]
if host_machine.system() == 'windows'
  tools_deps += [cc.find_library('ws2_32')]
endif

executable(
  'lame',
  common_sources,
  'lame_main.c',
  c_args: common_args,
  include_directories: frontend_includes,
  dependencies: tools_deps,
)

executable(
  'mp3rpt',
  common_sources,
  'mp3rtp.c',
  'rtp.c',
  c_args: common_args,
  include_directories: frontend_includes,
  dependencies: tools_deps,
)

# Do not build as it requires GTK+.
# If someone wants to add this, feel free.
#mp3x = executable('mp3x',
#  'mp3x.c', 'gtkanal.c', 'gpkplotting.c',
#  include_directories : [lameinc, confinc],
#  c_args : common_args,
#  link_with : lamelib,
#  )
