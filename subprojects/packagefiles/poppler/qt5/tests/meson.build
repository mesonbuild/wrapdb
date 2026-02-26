if get_option('tests')
  qt5_test_dependency = dependency(
    'qt5',
    version: '>=5.15',
    modules: ['Test'],
  )

  # manual tests
  # test name: [source, run moc, add Qt5Widgets dependency]
  qt5_manual_tests = {
    'test-poppler-qt5': ['test-poppler-qt5.cpp', true, true],
    'test-password-qt5': ['test-password-qt5.cpp', true, true],
    'test-render-to-file-qt5': ['test-render-to-file.cpp', false, false],
    'poppler-qt5-forms': ['poppler-forms.cpp', false, false],
    'poppler-qt5-fonts': ['poppler-fonts.cpp', false, false],
    'poppler-qt5-attachments': ['poppler-attachments.cpp', false, false],
    'stress-poppler-qt5': ['stress-poppler-qt5.cpp', false, true],
    'stress-poppler-dir-qt5': ['stress-poppler-dir.cpp', false, true],
    'stress-poppler-threads-qt5': ['stress-threads-qt5.cpp', true, false],
    'poppler-qt5-texts': ['poppler-texts.cpp', false, false],
    'poppler-qt5-page-labels': ['poppler-page-labels.cpp', false, false],
  }

  qt5_widgets_dependency = dependency(
    'qt5',
    version: '>=5.15',
    modules: ['Widgets'],
  )

  foreach qt5_manual_test_name, qt5_manual_test : qt5_manual_tests
    qt5_manual_test_sources = [qt5_manual_test[0]]
    if qt5_manual_test[1]
      qt5_manual_test_sources += qt5_module.compile_moc(
        sources: qt5_manual_test[0],
      )
    endif
    qt5_manual_test_dependencies = [poppler_qt5_library_dependency]
    if qt5_manual_test[2]
      qt5_manual_test_dependencies += qt5_widgets_dependency
    endif
    executable(
      qt5_manual_test_name,
      sources: qt5_manual_test_sources,
      dependencies: qt5_manual_test_dependencies,
    )
  endforeach

  # unit tests
  qt5_unit_tests = [
    'attachments',
    'dateConversion',
    'fonts',
    'links',
    'annotations',
    'metadata',
    'optcontent',
    'forms',
    'pagelayout',
    'pagemode',
    'password',
    'permissions',
    'search',
    'actualtext',
    'lexer',
    'internal_outline',
    'goostring',
    'object',
    'stroke_opacity',
    'utf_conversion',
    'outline',
    'signature_basics',
    'utf8document',
    'distinguished_name_parser',
    'cidfontswidthsbuilder',
    'overprint',
    'pagelabelinfo',
    'strings',
  ]

  foreach qt5_unit_test : qt5_unit_tests
    qt5_unit_test_name = 'check_qt5_' + qt5_unit_test
    qt5_unit_test_source = 'check_' + qt5_unit_test + '.cpp'
    qt5_unit_test_executable = executable(
      qt5_unit_test_name,
      sources: [
        qt5_unit_test_source,
        qt5_module.compile_moc(
          sources: qt5_unit_test_source,
        ),
      ],
      dependencies: [poppler_qt5_library_dependency, qt5_test_dependency],
      cpp_args: ['-DTESTDATADIR="@0@"'.format(poppler_test_directory)],
    )
    test(qt5_unit_test_name, qt5_unit_test_executable)
  endforeach
endif
