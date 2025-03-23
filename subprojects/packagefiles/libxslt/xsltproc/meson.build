sources = ['xsltproc.c']

xsltproc = executable(
  'xsltproc',
  sources,
  dependencies: [libxslt_dep, libexslt_dep, libm, librt],
  install: true,
)

meson.override_find_program('xsltproc', xsltproc)
