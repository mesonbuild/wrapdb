qt6_module = import('qt6')
qt6_dependency = dependency(
  'qt6',
  version: '>=6.2',
  modules: ['Core', 'Gui'],
  required: get_option('qt6'),
)

building_qt6_wrapper = qt6_dependency.found()
building_qt6_wrapper_demo = false
if building_qt6_wrapper == true
  poppler_qt6_library_cpp_arguments = [
    '-DQT_STRICT_ITERATORS',
    '-DQT_NO_SIGNALS_SLOTS_KEYWORDS',
    '-DQT_NO_CAST_FROM_ASCII',
    '-DQT_NO_CAST_FROM_BYTEARRAY',
    '-DQT_NO_KEYWORDS',
  ]

  if get_option('default_library') == 'static'
    poppler_qt6_library_cpp_arguments += '-DPOPPLER_QT6_STATIC_DEFINE'
  else
    poppler_qt6_library_cpp_arguments += '-Dpoppler_qt6_EXPORTS'
  endif

  # MSVC complains about dll-interface for embedded members of the internal API library
  if cpp_compiler.get_id() == 'msvc'
    poppler_qt6_library_cpp_arguments += '/wd4251'
  endif

  poppler_qt6_library_include_directories = include_directories('src')

  poppler_qt6_library_dependencies = [
    poppler_library_dependency,
    qt6_dependency,
  ]

  subdir('src')

  poppler_qt6_library = library(
    'poppler-qt6',
    cpp_args: poppler_qt6_library_cpp_arguments,
    dependencies: poppler_qt6_library_dependencies,
    include_directories: poppler_qt6_library_include_directories,
    install: true,
    sources: poppler_qt6_library_sources,
    soversion: '3',
    version: '3.12.0',
  )

  pkgconfig_module.generate(
    poppler_qt6_library,
    description: 'Qt6 wrapper for Poppler PDF rendering library.',
  )

  poppler_qt6_library_dependency = declare_dependency(
    link_with: poppler_qt6_library,
    dependencies: poppler_qt6_library_dependencies,
    include_directories: poppler_qt6_library_include_directories,
  )

  meson.override_dependency('poppler-qt6', poppler_qt6_library_dependency)

  subdir('demos')
  subdir('tests')
endif
