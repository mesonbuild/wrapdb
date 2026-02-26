building_glib_wrapper_demo = gtk3_dependency.found()
if building_glib_wrapper_demo
  poppler_glib_demo_sources = files(
    'annots.c',
    'attachments.c',
    'find.c',
    'fonts.c',
    'forms.c',
    'images.c',
    'info.cc',
    'layers.c',
    'links.c',
    'main.c',
    'outline.c',
    'page.c',
    'print.c',
    'render.c',
    'selections.c',
    'signature.c',
    'taggedstruct.c',
    'text.c',
    'transitions.c',
    'utils.c',
  )

  poppler_glib_demo_executable = executable(
    'poppler-glib-demo',
    sources: poppler_glib_demo_sources,
    dependencies: [poppler_glib_library_dependency, gtk3_dependency],
  )
endif
