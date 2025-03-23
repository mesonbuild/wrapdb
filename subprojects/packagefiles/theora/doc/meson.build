static_docs = files(
  'color.html',
  'draft-ietf-avt-rtp-theora-00.txt',
  'draft-ietf-avt-rtp-theora-00.xml',
  'vp3-format.txt',
)

install_data(
  static_docs,
  install_dir: get_option('datadir') / 'theora',
)

if doxygen_exe.found()
  doxygen_conf = configuration_data()

  doxygen_conf.set('PACKAGE', meson.project_name())
  doxygen_conf.set('VERSION', meson.project_version())
  doxygen_conf.set('top_srcdir', doc_root_dir)

  doxyfile_tmp = configure_file(
    input: 'Doxyfile.in',
    configuration: doxygen_conf,
    output: 'Doxyfile.in',
  )

  doxyfile_patcher = find_program('doxyfile-patcher.py')

  doxyfile = custom_target(
    'doxyfile-patcher',
    command: [
      doxyfile_patcher,
      '@INPUT@',
      '@OUTPUT@',
      meson.current_build_dir(),
    ],
    input: doxyfile_tmp,
    output: 'Doxyfile',
  )

  custom_target(
    'libtheora-docs',
    input: doxyfile,
    output: 'html',
    command: [doxygen_exe, doxyfile],
    console: true,
    install: true,
    install_dir: get_option('datadir') / 'doc' / meson.project_name(),
  )
endif
