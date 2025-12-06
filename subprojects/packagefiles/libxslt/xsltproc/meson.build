sources = ['xsltproc.c']

xsltproc = executable(
  'xsltproc',
  sources,
  include_directories: incdir,
  dependencies: [libxslt_dep, libexslt_dep, libm, librt],
  install: true,
)

meson.override_find_program('xsltproc', xsltproc)
