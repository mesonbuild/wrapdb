if get_option('tests')
  qt6_test_dependency = dependency(
    'qt6',
    version: '>=6.2',
    modules: ['Test'],
  )

  # manual tests
  # test name: [sources, run moc, add Qt6Widgets dependency]
  qt6_build_only_tests = {
    'test-poppler-qt6': ['test-poppler-qt6.cpp', true, true],
    'test-password-qt6': ['test-password-qt6.cpp', true, true],
    'test-render-to-file-qt6': ['test-render-to-file.cpp', false, false],
    'poppler-qt6-forms': ['poppler-forms.cpp', false, false],
    'poppler-qt6-fonts': ['poppler-fonts.cpp', false, false],
    'poppler-qt6-attachments': ['poppler-attachments.cpp', false, false],
    'stress-poppler-qt6': ['stress-poppler-qt6.cpp', false, true],
    'stress-poppler-dir-qt6': ['stress-poppler-dir.cpp', false, true],
    'stress-poppler-threads-qt6': ['stress-threads-qt6.cpp', true, false],
    'poppler-qt6-texts': ['poppler-texts.cpp', false, false],
    'poppler-qt6-page-labels': ['poppler-page-labels.cpp', false, false],
  }

  qt6_widgets_dependency = dependency(
    'qt6',
    version: '>=6.2',
    modules: ['Widgets'],
  )

  foreach qt6_build_only_test_name, qt6_build_only_test : qt6_build_only_tests
    qt6_build_only_test_sources = [qt6_build_only_test[0]]
    if qt6_build_only_test[1]
      qt6_build_only_test_sources += qt6_module.compile_moc(
        sources: qt6_build_only_test[0],
      )
    endif
    qt6_build_only_test_dependencies = [poppler_qt6_library_dependency]
    if qt6_build_only_test[2]
      qt6_build_only_test_dependencies += qt6_widgets_dependency
    endif
    executable(
      qt6_build_only_test_name,
      sources: qt6_build_only_test_sources,
      dependencies: qt6_build_only_test_dependencies,
    )
  endforeach

  # unit tests
  qt6_unit_tests = [
    'actualtext',
    'annotations',
    'attachments',
    'cidfontswidthsbuilder',
    'dateConversion',
    'distinguished_name_parser',
    'endoflines',
    'fonts',
    'forms',
    'goostring',
    'internal_outline',
    'lexer',
    'links',
    'metadata',
    'object',
    'optcontent',
    'outline',
    'overprint',
    'pagelabelinfo',
    'pagelayout',
    'pagemode',
    'password',
    'permissions',
    'search',
    'signature_basics',
    # @todo disabled because test fails
    # @sa https://gitlab.freedesktop.org/poppler/poppler/-/issues/1678
    # 'signature_basics_pgp',
    'strings',
    'stroke_opacity',
    'utf_conversion',
    'utf8document',
  ]

  foreach qt6_unit_test : qt6_unit_tests
    qt6_unit_test_name = 'check_qt6_' + qt6_unit_test
    qt6_unit_test_source = 'check_' + qt6_unit_test + '.cpp'
    qt6_unit_test_executable = executable(
      qt6_unit_test_name,
      sources: [
        qt6_unit_test_source,
        qt6_module.compile_moc(
          sources: qt6_unit_test_source,
        ),
      ],
      dependencies: [poppler_qt6_library_dependency, qt6_test_dependency],
      cpp_args: ['-DTESTDATADIR="@0@"'.format(poppler_test_directory)],
    )
    test(qt6_unit_test_name, qt6_unit_test_executable)
  endforeach

  # @todo disabled beacuse test fails
  # @sa https://gitlab.freedesktop.org/poppler/poppler/-/issues/1678
  # if enable_gpgmepp
  #     qt6_check_create_pgp_signature1_executable = executable(
  #     'check_create_pgp_signature1',
  #     sources: [
  #       'check_create_pgp_signature1.cpp',
  #       qt6_module.compile_moc(sources: 'check_create_pgp_signature1.cpp')
  #     ],
  #     dependencies: [
  #       poppler_qt6_library_dependency,
  #       qt6_test_dependency
  #     ],
  #     cpp_args: [
  #       '-DTESTDATADIR="@0@"'.format(poppler_test_directory)
  #     ]
  #   )
  #   test('check_create_pgp_signature1', qt6_check_create_pgp_signature1_executable)
  # endif

  # @todo fuzz tests
endif
