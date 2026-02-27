poppler_qt6_library_sources = files(
  'QPainterOutputDev.cc',
  'poppler-annotation.cc',
  'poppler-base-converter.cc',
  'poppler-document.cc',
  'poppler-embeddedfile.cc',
  'poppler-fontinfo.cc',
  'poppler-form.cc',
  'poppler-link-extractor.cc',
  'poppler-link.cc',
  'poppler-media.cc',
  'poppler-movie.cc',
  'poppler-optcontent.cc',
  'poppler-outline.cc',
  'poppler-page-transition.cc',
  'poppler-page.cc',
  'poppler-pdf-converter.cc',
  'poppler-private.cc',
  'poppler-ps-converter.cc',
  'poppler-qiodeviceinstream.cc',
  'poppler-qiodeviceoutstream.cc',
  'poppler-sound.cc',
  'poppler-textbox.cc',
  'poppler-version.cpp',
)
poppler_qt6_library_sources += configure_file(
  input: 'poppler-version.h.in',
  output: 'poppler-version.h',
  configuration: poppler_configuration,
  install: true,
  install_dir: get_option('includedir') / meson.project_name() / 'qt6',
)
poppler_qt6_library_sources += configure_file(
  input: poppler_exports_h_in,
  output: 'poppler-export.h',
  configuration: {
    'NAME': 'QT6',
    'PUBLIC_DEFINE': 'POPPLER_QT6_EXPORT',
  },
  install: true,
  install_dir: get_option('includedir') / meson.project_name() / 'qt6',
)
poppler_qt6_library_sources += qt6_module.compile_moc(
  headers: files('poppler-form.h', 'poppler-optcontent.h'),
)

install_headers(
  'poppler-qt6.h',
  'poppler-link.h',
  'poppler-annotation.h',
  'poppler-form.h',
  'poppler-optcontent.h',
  'poppler-page-transition.h',
  'poppler-media.h',
  'poppler-converter.h',
  subdir: meson.project_name() / 'qt6',
)
