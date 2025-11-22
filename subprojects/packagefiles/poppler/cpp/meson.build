building_cpp_wrapper = iconv_dependency.found()
if building_cpp_wrapper == true
  poppler_cpp_library_version = '3.0.0'
  poppler_cpp_library_so_version = '3'

  poppler_cpp_library_cpp_arguments = []
  if get_option('default_library') == 'static'
    poppler_cpp_library_cpp_arguments += '-DPOPPLER_CPP_STATIC_DEFINE'
  else
    poppler_cpp_library_cpp_arguments += '-Dpoppler_cpp_EXPORTS'
  endif

  poppler_cpp_library_dependencies = [
    iconv_dependency,
    poppler_library_dependency,
  ]

  poppler_cpp_library_include_directories = include_directories('.')

  poppler_cpp_library_sources = [
    'poppler-destination.cpp',
    'poppler-document.cpp',
    'poppler-embedded-file.cpp',
    'poppler-font.cpp',
    'poppler-global.cpp',
    'poppler-image.cpp',
    'poppler-page.cpp',
    'poppler-page-renderer.cpp',
    'poppler-page-transition.cpp',
    'poppler-private.cpp',
    'poppler-rectangle.cpp',
    'poppler-toc.cpp',
    'poppler-version.cpp',
  ]
  poppler_cpp_library_sources += configure_file(
    configuration: poppler_configuration,
    input: 'poppler-version.h.in',
    output: 'poppler-version.h',
    install: true,
    install_dir: get_option('includedir') / meson.project_name() / 'cpp',
  )

  poppler_cpp_library = library(
    'poppler-cpp',
    cpp_args: poppler_cpp_library_cpp_arguments,
    dependencies: poppler_cpp_library_dependencies,
    include_directories: poppler_cpp_library_include_directories,
    install: true,
    sources: poppler_cpp_library_sources,
    soversion: poppler_cpp_library_so_version,
    version: poppler_cpp_library_version,
  )

  pkgconfig_module.generate(
    poppler_cpp_library,
    description: 'C++ wrapper for Poppler PDF rendering library.',
  )

  poppler_cpp_library_dependency = declare_dependency(
    link_with: poppler_cpp_library,
    dependencies: poppler_cpp_library_dependencies,
    include_directories: poppler_cpp_library_include_directories,
  )

  meson.override_dependency('poppler-cpp', poppler_cpp_library_dependency)

  install_headers(
    'poppler_cpp_export.h',
    'poppler-destination.h',
    'poppler-document.h',
    'poppler-embedded-file.h',
    'poppler-font.h',
    'poppler-font-private.h',
    'poppler-global.h',
    'poppler-image.h',
    'poppler-page.h',
    'poppler-page-renderer.h',
    'poppler-page-transition.h',
    'poppler-rectangle.h',
    'poppler-toc.h',
    subdir: meson.project_name() / 'cpp',
  )

  subdir('tests')
endif
