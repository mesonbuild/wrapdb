if get_option('tests')
  perf_test_executable = executable(
    'perf-test',
    sources: 'perf-test.cc',
    dependencies: poppler_library_dep,
  )

  pdf_fullrewrite_executable = executable(
    'pdf-fullrewrite',
    sources: ['pdf-fullrewrite.cc', utils_parseargs_cc],
    dependencies: poppler_library_dep,
  )

  if gtk3_dep.found()
    gtk_test_executable = executable(
      'gtk-test',
      sources: 'gtk-test.cc',
      dependencies: [poppler_glib_library_dep, gtk3_dep],
    )
  endif

  if cairo_dep.found() and gtk3_dep.found()
    pdf_inspector_executable = executable(
      'pdf-inspector',
      sources: ['pdf-inspector.cc', poppler_cairo_sources],
      dependencies: [poppler_glib_library_dep, gtk3_dep],
      cpp_args: '-DSRC_DIR="@0@"'.format(meson.current_source_dir()),
    )
  endif

  threads_dep = dependency(
    'threads',
    required: cairo_dep.found(),
  )
  if threads_dep.found()
    cairo_thread_test_executable = executable(
      'cairo-thread-test',
      sources: ['cairo-thread-test.cc', poppler_cairo_sources],
      dependencies: [
        poppler_library_dep,
        cairo_dep,
        threads_dep,
      ],
    )
  endif

  if nss_dep.found()
    pdf_validate_signature_executable = executable(
      'pdf-validate-signature',
      sources: 'pdf-validate-signature.cc',
      dependencies: poppler_library_dep,
    )
    # @todo add tests, but they depend on test data, not in this repository
    pdf_signing_nss_executable = executable(
      'pdf-signing-nss',
      sources: 'pdf-signing-nss.cc',
      dependencies: poppler_library_dep,
    )
    # @todo add tests, but they depend on test data, not in this repository
  endif
endif

summary('tests', get_option('tests'))
