qt6_widgets_dependency = dependency(
  'qt6',
  modules: 'Widgets',
  required: get_option('qt6_demo'),
)

building_qt6_wrapper_demo = qt6_widgets_dependency.found()
if building_qt6_wrapper_demo
  poppler_qt6_viewer_sources = files(
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
  poppler_qt6_viewer_sources += qt6_module.compile_moc(
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

  poppler_qt6_viewer_executable = executable(
    'poppler_qt6viewer',
    sources: poppler_qt6_viewer_sources,
    dependencies: [poppler_qt6_library_dependency, qt6_widgets_dependency],
  )
endif
