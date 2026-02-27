qt5_widgets_dep = dependency(
  'qt5',
  modules: 'Widgets',
  required: get_option('qt5_demo'),
)

if qt5_widgets_dep.found()
  poppler_qt5_viewer_sources = files(
    'abstractinfodock.cpp',
    'documentobserver.cpp',
    'embeddedfiles.cpp',
    'fonts.cpp',
    'info.cpp',
    'main_viewer.cpp',
    'metadata.cpp',
    'navigationtoolbar.cpp',
    'optcontent.cpp',
    'pageview.cpp',
    'permissions.cpp',
    'thumbnails.cpp',
    'toc.cpp',
    'viewer.cpp',
  )
  poppler_qt5_viewer_sources += qt5_module.compile_moc(
    headers: [
      'abstractinfodock.h',
      'embeddedfiles.h',
      'fonts.h',
      'info.h',
      'metadata.h',
      'navigationtoolbar.h',
      'optcontent.h',
      'pageview.h',
      'permissions.h',
      'thumbnails.h',
      'toc.h',
      'viewer.h',
    ],
    sources: ['toc.cpp'],
  )

  poppler_qt5_viewer_executable = executable(
    'poppler_qt5viewer',
    sources: poppler_qt5_viewer_sources,
    dependencies: [poppler_qt5_library_dep, qt5_widgets_dep],
  )
endif

summary('  Qt5 demo', qt5_widgets_dep.found())
