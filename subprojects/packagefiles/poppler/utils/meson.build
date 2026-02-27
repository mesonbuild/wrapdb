utils_parseargs_cc = files('parseargs.cc')

if get_option('tools').allowed()
  tools_dependencies = [poppler_library_dep]

  tools_sources = [utils_parseargs_cc, 'Win32Console.cc']


  # pdftoppm
  pdftoppm_executable = executable(
    'pdftoppm',
    sources: tools_sources + ['pdftoppm.cc', 'sanitychecks.cc'],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdftoppm.1')
  meson.override_find_program('pdftoppm', pdftoppm_executable)


  # pdftocairo
  if cairo_dep.found()
    pdftocairo_executable = executable(
      'pdftocairo',
      sources: [
        tools_sources,
        poppler_cairo_sources,
        'pdftocairo.cc',
        'pdftocairo-win32.cc',
      ],
      dependencies: [
        cairo_dep,
        tools_dependencies,
      ],
      install: true,
    )
    install_man('pdftocairo.1')
    meson.override_find_program('pdftocairo', pdftocairo_executable)
  endif


  # pdfdetach
  pdfdetach_executable = executable(
    'pdfdetach',
    sources: tools_sources + ['pdfdetach.cc'],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdfdetach.1')
  meson.override_find_program('pdfdetach', pdfdetach_executable)


  # pdfattach
  pdfattach_executable = executable(
    'pdfattach',
    sources: tools_sources + ['pdfattach.cc'],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdfattach.1')
  meson.override_find_program('pdfattach', pdfattach_executable)


  # pdffonts
  pdffonts_executable = executable(
    'pdffonts',
    sources: tools_sources + ['pdffonts.cc'],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdffonts.1')
  meson.override_find_program('pdffonts', pdffonts_executable)


  # pdfimages
  pdfimages_executable = executable(
    'pdfimages',
    sources: tools_sources + ['pdfimages.cc', 'ImageOutputDev.cc'],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdfimages.1')
  meson.override_find_program('pdfimages', pdfimages_executable)


  # pdfinfo
  pdfinfo_executable = executable(
    'pdfinfo',
    sources: tools_sources + ['pdfinfo.cc', 'printencodings.cc'],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdfinfo.1')
  meson.override_find_program('pdfinfo', pdfinfo_executable)


  # pdfsig
  if nss_dep.found() or gpgmepp_dep.found()
    pdfsig_executable = executable(
      'pdfsig',
      sources: tools_sources + ['pdfsig.cc'],
      dependencies: tools_dependencies,
      install: true,
    )
    install_man('pdfsig.1')
    meson.override_find_program('pdfsig', pdfsig_executable)
  endif


  # pdftops
  pdftops_executable = executable(
    'pdftops',
    sources: tools_sources + ['pdftops.cc', 'sanitychecks.cc'],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdftops.1')
  meson.override_find_program('pdftops', pdftops_executable)


  # pdftotext
  pdftotext_executable = executable(
    'pdftotext',
    sources: tools_sources + ['pdftotext.cc', 'printencodings.cc'],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdftotext.1')
  meson.override_find_program('pdftotext', pdftotext_executable)


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
  meson.override_find_program('pdftohtml', pdftohtml_executable)


  # pdfseparate
  pdfseparate_executable = executable(
    'pdfseparate',
    sources: tools_sources + ['pdfseparate.cc'],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdfseparate.1')
  meson.override_find_program('pdfseparate', pdfseparate_executable)


  # pdfunite
  pdfunite_executable = executable(
    'pdfunite',
    sources: tools_sources + ['pdfunite.cc'],
    dependencies: tools_dependencies,
    install: true,
  )
  install_man('pdfunite.1')
  meson.override_find_program('pdfunite', pdfunite_executable)

endif

summary('tools', get_option('tools').allowed())
