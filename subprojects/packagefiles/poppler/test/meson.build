if get_option('tests')
  perf_test_executable = executable(
    'perf-test',
    sources: 'perf-test.cc',
    dependencies: poppler_library_dependency,
  )

  pdf_fullrewrite_executable = executable(
    'pdf-fullrewrite',
    sources: ['pdf-fullrewrite.cc', utils_parseargs_cc],
    dependencies: poppler_library_dependency,
  )

  if gtk3_dependency.found()
    gtk_test_executable = executable(
      'gtk-test',
      sources: 'gtk-test.cc',
      dependencies: [poppler_glib_library_dependency, gtk3_dependency],
    )
  endif

  if cairo_dependency.found() and gtk3_dependency.found()
    pdf_inspector_executable = executable(
      'pdf-inspector',
      sources: ['pdf-inspector.cc', poppler_cairo_sources],
      dependencies: [poppler_glib_library_dependency, gtk3_dependency],
      cpp_args: '-DSRC_DIR="@0@"'.format(meson.current_source_dir()),
    )
  endif

  threads_dependency = dependency(
    'threads',
    required: cairo_dependency.found(),
  )
  if threads_dependency.found()
    cairo_thread_test_executable = executable(
      'cairo-thread-test',
      sources: ['cairo-thread-test.cc', poppler_cairo_sources],
      dependencies: [
        poppler_library_dependency,
        cairo_dependency,
        threads_dependency,
      ],
    )
  endif

  if enable_nss
    pdf_validate_signature_executable = executable(
      'pdf-validate-signature',
      sources: 'pdf-validate-signature.cc',
      dependencies: poppler_library_dependency,
    )
    # @todo add tests, but they depend on test data, not in this repository
    pdf_signing_nss_executable = executable(
      'pdf-signing-nss',
      sources: 'pdf-signing-nss.cc',
      dependencies: poppler_library_dependency,
    )
    # @todo add tests, but they depend on test data, not in this repository
  endif
endif
