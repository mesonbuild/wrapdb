encoder_sources = files(
  'analyze.c',
  'apiwrapper.c',
  'bitpack.c',
  'dequant.c',
  'encapiwrapper.c',
  'encfrag.c',
  'encinfo.c',
  'encode.c',
  'enquant.c',
  'fdct.c',
  'fragment.c',
  'huffenc.c',
  'idct.c',
  'info.c',  # not in SConstruct or Makefile.am
  'internal.c',
  'mathops.c',
  'mcenc.c',
  'quant.c',
  'rate.c',
  'state.c',
  'tokenize.c',
)

decoder_sources = files(
  'apiwrapper.c',
  'bitpack.c',
  'decapiwrapper.c',
  'decinfo.c',
  'decode.c',
  'dequant.c',
  'fragment.c',
  'huffdec.c',
  'idct.c',
  'info.c',
  'internal.c',
  'quant.c',
  'state.c',
)

if conf.get('CPU_x86_64', false)
  if cc.get_argument_syntax() != 'msvc'
    encoder_sources += files(
      'x86/mmxencfrag.c',
      'x86/mmxfdct.c',
      'x86/mmxfrag.c',
      'x86/mmxidct.c',
      'x86/mmxstate.c',
      'x86/sse2encfrag.c',
      'x86/sse2fdct.c',
      'x86/sse2idct.c',
      'x86/x86cpu.c',
      'x86/x86enc.c',
      'x86/x86enquant.c',
      'x86/x86state.c',
    )
    decoder_sources += files(
      'x86/mmxfrag.c',
      'x86/mmxidct.c',
      'x86/mmxstate.c',
      'x86/sse2idct.c',
      'x86/x86cpu.c',
      'x86/x86state.c',
    )
  endif
elif conf.get('CPU_x86_32', false)
  if cc.get_argument_syntax() != 'msvc'
    decoder_sources += files(
      'x86/mmxfrag.c',
      'x86/mmxidct.c',
      'x86/mmxstate.c',
      'x86/sse2idct.c',
      'x86/x86cpu.c',
      'x86/x86state.c',
    )
    encoder_sources += files(
      'x86/mmxencfrag.c',
      'x86/mmxfdct.c',
      'x86/mmxfrag.c',
      'x86/mmxidct.c',
      'x86/mmxstate.c',
      'x86/sse2encfrag.c',
      'x86/sse2idct.c',
      'x86/x86cpu.c',
      'x86/x86enc.c',
      'x86/x86enquant.c',
      'x86/x86state.c',
    )
  else
    encoder_sources += files(
      'x86_vc/mmxencfrag.c',
      'x86_vc/mmxfdct.c',
      'x86_vc/mmxfrag.c',
      'x86_vc/mmxidct.c',
      'x86_vc/mmxstate.c',
      'x86_vc/x86cpu.c',
      'x86_vc/x86enc.c',
      'x86_vc/x86state.c',
    )
    decoder_sources += files(
      'x86_vc/mmxfrag.c',
      'x86_vc/mmxidct.c',
      'x86_vc/mmxstate.c',
      'x86_vc/x86cpu.c',
      'x86_vc/x86state.c',
    )
  endif
endif

decoder_res = files()
encoder_res = files()

if host_machine.system() == 'windows'
  if get_option('debug')
    decoder_rc = '../win32/xmingw32/libtheoradecd.rc'
    encoder_rc = '../win32/xmingw32/libtheoraencd.rc'
  else
    decoder_rc = '../win32/xmingw32/libtheoradec.rc'
    encoder_rc = '../win32/xmingw32/libtheoraenc.rc'
  endif

  patcher_py = find_program(
    '../win32/xmingw32/generate_windows_rc.py',
    required: true,
    native: true,
  )

  libtheoradec_rc = custom_target(
    'libtheoradec.rc',
    command: [patcher_py, '@INPUT@', '@OUTPUT@', meson.project_version()],
    input: [decoder_rc, '../win32/xmingw32/libtheoradec-all.rc'],
    output: ['libtheoradec.rc'],
  )

  decoder_res += windows.compile_resources(libtheoradec_rc)

  libtheoraenc_rc = custom_target(
    'libtheoraenc.rc',
    command: [patcher_py, '@INPUT@', '@OUTPUT@', meson.project_version()],
    input: [encoder_rc, '../win32/xmingw32/libtheoraenc-all.rc'],
    output: ['libtheoraenc.rc'],
  )

  encoder_res += windows.compile_resources(libtheoraenc_rc)
endif

if host_machine.system() == 'darwin'
  version_flag = '-Wl,-exported_symbols_list,@0@'
  theoradec_version_arg = meson.current_source_dir() / 'theoradec.exp'
  theoraenc_version_arg = meson.current_source_dir() / 'theoraenc.exp'
  theora_version_arg = meson.current_source_dir() / 'theora.exp'

  # macOS Clang requires exported_symbols_list to have all symbols already
  # compiled, so the test will fail. We will use it directly.
  theoradec_version_flag = version_flag.format(theoradec_version_arg)
  theoraenc_version_flag = version_flag.format(theoraenc_version_arg)
  theora_version_flag = version_flag.format(theora_version_arg)
else
  version_flag = '-Wl,--version-script,@0@'
  theoradec_version_arg = meson.current_source_dir() / 'Version_script-dec'
  theoraenc_version_arg = meson.current_source_dir() / 'Version_script-enc'
  theora_version_arg = meson.current_source_dir() / 'Version_script'

  theoradec_version_flag = cc.get_supported_link_arguments(
    version_flag.format(theoradec_version_arg),
  )

  theoraenc_version_flag = cc.get_supported_link_arguments(
    version_flag.format(theoraenc_version_arg),
  )

  theora_version_flag = cc.get_supported_link_arguments(
    version_flag.format(theora_version_arg),
  )
endif

libtheoradec = library(
  'theoradec',
  decoder_sources + decoder_res,
  dependencies: [m_dep, libpng_dep, ogg_dep, cairo_dep, config_dep],
  include_directories: incdir,
  vs_module_defs: '../win32/xmingw32/libtheoradec-all.def',
  c_args: compile_args,
  link_args: theoradec_version_flag,
  version: theoradec_libversion,
  darwin_versions: theoradec_darwin_version,
  install: true,
)

pkg.generate(
  libtheoradec,
  description: 'Theora video codec (decoder)',
  version: meson.project_version(),
)

theoradec_dep = declare_dependency(
  link_with: libtheoradec,
  dependencies: [m_dep, libpng_dep, ogg_dep, cairo_dep, config_dep],
  include_directories: incdir,
)

libtheoraenc = library(
  'theoraenc',
  encoder_sources + encoder_res,
  dependencies: [m_dep, libpng_dep, ogg_dep, config_dep],
  include_directories: incdir,
  vs_module_defs: '../win32/xmingw32/libtheoraenc-all.def',
  c_args: compile_args,
  link_args: theoraenc_version_flag,
  version: theoraenc_libversion,
  darwin_versions: theoraenc_darwin_version,
  install: true,
)

# In 1.1.1 the source pkg-config specifies an incorrect
# dependency on theoradec which is relied on by GStreamer.
# Otherwise th_version_string is invisible according to the
# version scripts/.def files.
pkg.generate(
  libtheoraenc,
  requires: libtheoradec,
  description: 'Theora video codec (encoder)',
  version: meson.project_version(),
)

theoraenc_dep = declare_dependency(
  link_with: [libtheoraenc, libtheoradec],
  dependencies: [m_dep, libpng_dep, ogg_dep, config_dep],
  include_directories: incdir,
)

libtheora = library(
  'theora',
  encoder_sources + decoder_sources,
  dependencies: [m_dep, libpng_dep, ogg_dep, config_dep],
  include_directories: incdir,
  c_args: compile_args,
  link_args: theora_version_flag,
  vs_module_defs: 'theora.def',  # Missing in the official tarballs
  version: theora_libversion,
  darwin_versions: theora_darwin_version,
  install: true,
)

pkg.generate(
  libtheora,
  description: 'Theora video codec',
  version: meson.project_version(),
)

theora_dep = declare_dependency(
  link_with: libtheora,
  dependencies: [m_dep, libpng_dep, ogg_dep, config_dep],
  include_directories: incdir,
)

if meson.version().version_compare('>=0.54.0')
  meson.override_dependency('theora', theora_dep)
  meson.override_dependency('theoradec', theoradec_dep)
  meson.override_dependency('theoraenc', theoraenc_dep)
endif
