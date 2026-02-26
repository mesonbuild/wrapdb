building_tools = false
utils_parseargs_cc = files('parseargs.cc')

if get_option('tools').allowed() == true
  building_tools = true

  tools_dependencies = [poppler_library_dependency]

  tools_sources = [utils_parseargs_cc, 'Win32Console.cc']


  # pdftoppm
  pdftoppm_executable = executable(
    'pdftoppm',
    sources: tools_sources + ['pdftoppm.cc', 'sanitychecks.cc'],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdftoppm.1')


  # pdftocairo
  if cairo_dependency.found() == true
    pdftocairo_executable = executable(
      'pdftocairo',
      sources: [
        tools_sources,
        poppler_cairo_sources,
        'pdftocairo.cc',
        'pdftocairo-win32.cc',
      ],
      dependencies: [
        cairo_dependency,
        tools_dependencies,
      ],
      install: true,
    )
    install_man('pdftocairo.1')
  endif


  # pdfdetach
  pdfdetach_executable = executable(
    'pdfdetach',
    sources: tools_sources + ['pdfdetach.cc'],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdfdetach.1')


  # pdfattach
  pdfattach_executable = executable(
    'pdfattach',
    sources: tools_sources + ['pdfattach.cc'],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdfattach.1')


  # pdffonts
  pdffonts_executable = executable(
    'pdffonts',
    sources: tools_sources + ['pdffonts.cc'],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdffonts.1')


  # pdfimages
  pdfimages_executable = executable(
    'pdfimages',
    sources: tools_sources + ['pdfimages.cc', 'ImageOutputDev.cc'],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdfimages.1')


  # pdfinfo
  pdfinfo_executable = executable(
    'pdfinfo',
    sources: tools_sources + ['pdfinfo.cc', 'printencodings.cc'],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdfinfo.1')


  # pdfsig
  if enable_signatures == true
    pdfsig_executable = executable(
      'pdfsig',
      sources: tools_sources + ['pdfsig.cc'],
      dependencies: tools_dependencies,
      install: true,
    )
    install_man('pdfsig.1')
  endif


  # pdftops
  pdftops_executable = executable(
    'pdftops',
    sources: tools_sources + ['pdftops.cc', 'sanitychecks.cc'],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdftops.1')


  # pdftotext
  pdftotext_executable = executable(
    'pdftotext',
    sources: tools_sources + ['pdftotext.cc', 'printencodings.cc'],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdftotext.1')


  # pdftohtml
  pdftohtml_executable = executable(
    'pdftohtml',
    sources: tools_sources + [
      'pdftohtml.cc',
      'HtmlFonts.cc',
      'HtmlLinks.cc',
      'HtmlOutputDev.cc',
      'InMemoryFile.cc',
    ],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdftohtml.1')


  # pdfseparate
  pdfseparate_executable = executable(
    'pdfseparate',
    sources: tools_sources + ['pdfseparate.cc'],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdfseparate.1')


  # pdfunite
  pdfunite_executable = executable(
    'pdfunite',
    sources: tools_sources + ['pdfunite.cc'],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdfunite.1')


endif
