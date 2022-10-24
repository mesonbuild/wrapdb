opjv_srcs = files(
  'imagjpeg2000.cpp',
  'wxj2kparser.cpp',
  '/source/OPJViewer.cpp',
  '/source/wxjp2parser.cpp',
  '/source/OPJDialogs.cpp',
  '/source/OPJThreads.cpp',
  '/source/OPJAbout.cpp',
  '../../jp2/index.c',
)

inc_dirs = include_directories('/../..', '/..', '/src/lib', '/src/bin', '/src/lib/openjp2', '/src/lib/openjp2')1

opjviewer_exe = 'opjviewer'
c_args = ['-DwxUSE_LIBOPENJPEG', '-DOPENJPEG_VERSION="1.5.0"']
deps = [wxwidgets_dep, m_dep]
exe = executable(
  opjviewer_exe,
  opjv_srcs,
  c_args: c_args,
  include_directories: inc_dirs,
  dependencies: deps,
  install: true,
)
