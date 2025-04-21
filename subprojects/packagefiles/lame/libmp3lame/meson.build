lame_sources = files(
  cdata.has('HAVE_XMMINTRIN_H') ? 'vector/xmm_quantize_sub.c' : [],
  'VbrTag.c',
  'bitstream.c',
  'encoder.c',
  'fft.c',
  'gain_analysis.c',
  'id3tag.c',
  'lame.c',
  'mpglib_interface.c',
  'newmdct.c',
  'presets.c',
  'psymodel.c',
  'quantize.c',
  'quantize_pvt.c',
  'reservoir.c',
  'set_get.c',
  'tables.c',
  'takehiro.c',
  'util.c',
  'vbrquantize.c',
  'version.c',
)

mp3lame_includes = [include_directories('.'), lameinc, confinc]

if host_machine.system() == 'windows'
  lame_sources += windows.compile_resources(
    'lame.rc',
    include_directories: mp3lame_includes,
  )
endif

lame_deps = [m_dep]
if build_decoder
  lame_deps += [mpglib_dep]
endif

lame_def = configure_file(
  input: '../include/lame.def',
  output: 'lame.def',
  command: [find_program('fix_def.py'), '@INPUT@', '@OUTPUT@'],
)

lame_ver = configure_file(
  input: '../include/libmp3lame.sym',
  output: 'libmp3lame.ver',
  command: [find_program('sym2ver.py'), '@INPUT@', '@OUTPUT@'],
)
lame_ver_arg = cc.get_supported_link_arguments(
  '-Wl,--version-script=' + meson.current_build_dir() / 'libmp3lame.ver',
)

lamelib = library(
  'mp3lame',
  lame_sources,
  version: '0.0.0',
  include_directories: mp3lame_includes,
  c_args: common_args,
  link_args: lame_ver_arg,
  vs_module_defs: lame_def,
  dependencies: lame_deps,
  install: true,
)

lame_dep = declare_dependency(
  include_directories: lameinc,
  link_with: lamelib,
  dependencies: lame_deps,
)
