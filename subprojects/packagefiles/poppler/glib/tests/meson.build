if get_option('tests') and gtk3_dep.found()
  # pdfdrawbb
  poppler_glib_pdfdrawbb_executable = executable(
    'pdfdrawbb',
    sources: 'pdfdrawbb.c',
    dependencies: poppler_glib_library_dep,
  )

  # check-text
  poppler_glib_check_text_executable = executable(
    'poppler-check-text',
    sources: 'check_text.c',
    dependencies: [poppler_glib_library_dep, gtk3_dep],
    c_args: ['-DTESTDATADIR="@0@"'.format(poppler_test_directory)],
  )
  test('poppler-check-text', poppler_glib_check_text_executable)

  # check-bb
  poppler_glib_check_bb_executable = executable(
    'poppler-check-bb',
    sources: 'check_bb.c',
    dependencies: [poppler_glib_library_dep, gtk3_dep],
  )

  poppler_glib_check_bb_tests = {
    'shapes+attachments.pdf': ['42.5', '42.5', '557.5', '557.5'],
    'orientation.pdf': [
      '34',
      '34',
      '83.74',
      '49',
      '793',
      '34',
      '808',
      '97.19',
      '488.02',
      '793',
      '561',
      '808',
      '34',
      '503.61',
      '49',
      '561',
    ],
    'xr01.pdf': ['148.71', '126.35', '308.11', '704.57'],
    'xr02.pdf': [
      '133.77',
      '124.81',
      '308.11',
      '704.57',
      '133.77',
      '124.80',
      '308.11',
      '704.57',
    ],
    'russian.pdf': ['71.5', '76.81', '197.69', '131.09'],
    'vis_policy_test.pdf': ['90', '77.93', '312.01', '265.13'],
    'searchAcrossLines.pdf': [
      '107.15',
      '105.23',
      '523.85',
      '691',
      '85.04',
      '94',
      '538.59',
      '762.19',
    ],
    'deseret.pdf': ['56.8', '57.15', '109.5', '72.8'],
    'fieldWithUtf16Names.pdf': ['56.65', '56.65', '264.55', '83.05'],
    'bug7063.pdf': ['56.8', '57.46', '244.29', '118.79'],
    'WithActualText.pdf': ['100', '90.72', '331.01', '102.35'],
    'Issue637.pdf': ['70.87', '53', '293', '105.37'],
    'truetype.pdf': ['17.5', '17.5', '577.5', '225.62'],
    'form_set_icon.pdf': ['0', '0', '362.835', '272.126'],
    'imageretrieve+attachment.pdf': ['0', '0', '610.56', '792'],
    'checkbox_issue_159.pdf': ['2.84', '14.17', '553.18', '840.87'],
    'NestedLayers.pdf': ['0', '191', '612', '792'],
    'A6EmbeddedFiles.pdf': ['18', '18', '558.36', '751.92'],
    'latex-hyperref-checkbox-issue-655.pdf': [
      '148.71',
      '123.81',
      '308.11',
      '704.57',
    ],
    'utf16le-annot.pdf': ['55.47', '54.78', '98.74', '96.12'],
    'type3.pdf': [
      '-p',
      '10',
      '125.80',
      '130',
      '509.30',
      '695',
      '125.80',
      '132',
      '538.03',
      '693',
    ],
  }

  foreach poppler_glib_check_bb_test_name, poppler_glib_check_bb_test_arguments : poppler_glib_check_bb_tests
    test(
      'poppler-check-bb-' + poppler_glib_check_bb_test_name,
      poppler_glib_check_bb_executable,
      args: [
        poppler_test_directory / 'unittestcases' / poppler_glib_check_bb_test_name,
      ] + poppler_glib_check_bb_test_arguments,
    )
  endforeach

  # @todo fuzz tests
endif
