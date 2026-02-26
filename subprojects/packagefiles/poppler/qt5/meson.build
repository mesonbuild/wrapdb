qt5_module = import('qt5')
qt5_dependency = dependency(
  'qt5',
  version: '>=5.15',
  modules: ['Core', 'Gui', 'Xml'],
  required: get_option('qt5'),
)

building_qt5_wrapper = qt5_dependency.found()
building_qt5_wrapper_demo = false
if building_qt5_wrapper == true
  poppler_qt5_library_cpp_arguments = [
    '-DQT_STRICT_ITERATORS',
    '-DQT_DISABLE_DEPRECATED_BEFORE=0x050E00',
    '-DQT_NO_DEPRECATED_WARNINGS',
    '-DQT_NO_SIGNALS_SLOTS_KEYWORDS',
    '-DQT_NO_CAST_FROM_ASCII',
    '-DQT_NO_CAST_FROM_BYTEARRAY',
    '-DQT_NO_KEYWORDS',
  ]

  if get_option('default_library') == 'static'
    poppler_qt5_library_cpp_arguments += '-DPOPPLER_QT5_STATIC_DEFINE'
  else
    poppler_qt5_library_cpp_arguments += '-DPOPPLER_QT5_EXPORTS'
  endif

  poppler_qt5_library_include_directories = include_directories('src')

  poppler_qt5_library_dependencies = [
    poppler_library_dependency,
    qt5_dependency,
  ]

  subdir('src')

  poppler_qt5_library = library(
    'poppler-qt5',
    cpp_args: poppler_qt5_library_cpp_arguments,
    dependencies: poppler_qt5_library_dependencies,
    include_directories: poppler_qt5_library_include_directories,
    install: true,
    sources: poppler_qt5_library_sources,
    soversion: '1',
    version: '1.40.0',
  )

  pkgconfig_module.generate(
    poppler_qt5_library,
    description: 'Qt5 wrapper for Poppler PDF rendering library.',
  )

  poppler_qt5_library_dependency = declare_dependency(
    link_with: poppler_qt5_library,
    dependencies: poppler_qt5_library_dependencies,
    include_directories: poppler_qt5_library_include_directories,
  )

  meson.override_dependency('poppler-qt5', poppler_qt5_library_dependency)

  subdir('demos')
  subdir('tests')
endif
