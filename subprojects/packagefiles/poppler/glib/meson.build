if building_glib_wrapper
  poppler_glib_library_version = '8.31.0'
  poppler_glib_library_so_version = '8'

  poppler_glib_library_include_directories = include_directories('.')

  poppler_glib_library_sources = [
    poppler_cairo_sources,
    'poppler-action.cc',
    'poppler-date.cc',
    'poppler-document.cc',
    'poppler-page.cc',
    'poppler-attachment.cc',
    'poppler-form-field.cc',
    'poppler-annot.cc',
    'poppler-layer.cc',
    'poppler-movie.cc',
    'poppler-media.cc',
    'poppler.cc',
    'poppler-cached-file-loader.cc',
    'poppler-input-stream.cc',
    'poppler-structure-element.cc',
  ]
  poppler_glib_library_sources += configure_file(
    configuration: poppler_configuration,
    input: 'poppler-features.h.cmake',
    output: 'poppler-features.h',
    format: 'cmake',
    install: true,
    install_dir: get_option('includedir') / meson.project_name() / 'glib',
  )
  poppler_glib_library_sources += configure_file(
    input: poppler_exports_h_in,
    output: 'poppler-macros.h',
    configuration: {
      'NAME': 'GLIB',
      'PUBLIC_DEFINE': 'POPPLER_PUBLIC'
    },
    install: true,
    install_dir: get_option('includedir') / meson.project_name() / 'blib',
  )

  poppler_glib_library_headers = files(
    'poppler-action.h',
    'poppler-annot.h',
    'poppler-attachment.h',
    'poppler-date.h',
    'poppler-document.h',
    'poppler-form-field.h',
    'poppler-layer.h',
    'poppler-media.h',
    'poppler-movie.h',
    'poppler-page.h',
    'poppler-structure-element.h',
    'poppler.h',
  )

  gnome_module = import('gnome')
  poppler_glib_library_sources += gnome_module.mkenums(
    'bogus',
    c_template: 'poppler-enums.c.template',
    h_template: 'poppler-enums.h.template',
    install_header: true,
    install_dir: get_option('includedir') / meson.project_name() / 'glib',
    sources: poppler_glib_library_headers,
  )

  poppler_glib_library_cpp_arguments = []
  if get_option('default_library') == 'static'
    poppler_glib_library_cpp_arguments += '-DPOPPLER_GLIB_STATIC_DEFINE'
  else
    poppler_glib_library_cpp_arguments += '-DPOPPLER_GLIB_EXPORTS'
  endif

  poppler_glib_library_dependencies = [
    cairo_dep,
    gio_dep,
    glib_dep,
    gobject_dep,
    poppler_library_dep,
  ]

  poppler_glib_library = library(
    'poppler-glib',
    cpp_args: poppler_glib_library_cpp_arguments,
    dependencies: poppler_glib_library_dependencies,
    include_directories: poppler_glib_library_include_directories,
    install: true,
    sources: poppler_glib_library_sources,
    soversion: poppler_glib_library_so_version,
    version: poppler_glib_library_version,
  )

  pkgconfig_module.generate(
    poppler_glib_library,
    description: 'GLib wrapper for Poppler PDF rendering library.',
  )

  poppler_glib_library_dep = declare_dependency(
    link_with: poppler_glib_library,
    dependencies: poppler_glib_library_dependencies,
    include_directories: poppler_glib_library_include_directories,
  )

  meson.override_dependency('poppler-glib', poppler_glib_library_dep)

  install_headers(
    poppler_glib_library_headers,
    subdir: meson.project_name() / 'glib',
  )

  if get_option('gobject_introspection').allowed() and get_option(
    'default_library',
  ) == 'shared'
    summary('  GObject introspection', true)
    gnome_module.generate_gir(
      poppler_glib_library,
      namespace: 'Poppler',
      nsversion: '0.18',
      includes: ['GObject-2.0', 'Gio-2.0', 'cairo-1.0'],
      sources: poppler_glib_library_sources + poppler_glib_library_headers,
      header: 'poppler.h',
      install: true,
    )
  else
    summary('  GObject introspection', false)
  endif

  # @todo Gtk docs

  subdir('tests')
  subdir('demo')
endif

summary('GLib wrapper', building_glib_wrapper)
