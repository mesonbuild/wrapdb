project('libxslt', 'c',
  version: '1.1.34',
   meson_version: '>=0.54.0')

configure_file(input: 'config.h.meson',
  output: 'config.h',
  copy: true)

cc = meson.get_compiler('c')

xml_dep = dependency('libxml-2.0')
m_dep = cc.find_library('m', required: false)

subdir('libxslt')
subdir('libexslt')

xslt_lib = library('xslt',
  'libxslt/attributes.c',
  'libxslt/attrvt.c',
  'libxslt/documents.c',
  'libxslt/extensions.c',
  'libxslt/extra.c',
  'libxslt/functions.c',
  'libxslt/imports.c',
  'libxslt/keys.c',
  'libxslt/namespaces.c',
  'libxslt/numbers.c',
  'libxslt/pattern.c',
  'libxslt/preproc.c',
  'libxslt/security.c',
  'libxslt/templates.c',
  'libxslt/transform.c',
  'libxslt/variables.c',
  'libxslt/xslt.c',
  'libxslt/xsltlocale.c',
  'libxslt/xsltutils.c',
  include_directories: 'libxslt',
  dependencies: [m_dep, xml_dep],
)

exslt_lib = library('exslt',
  'libexslt/common.c',
  'libexslt/crypto.c',
  'libexslt/date.c',
  'libexslt/dynamic.c',
  'libexslt/exslt.c',
  'libexslt/functions.c',
  'libexslt/math.c',
  'libexslt/saxon.c',
  'libexslt/sets.c',
  'libexslt/strings.c',
  include_directories: ['libexslt', 'libxslt'],
  link_with: xslt_lib,
  dependencies: [m_dep, xml_dep],
)

libxslt_dep = declare_dependency(include_directories: ['.'],
  link_with: xslt_lib)

libexslt_dep = declare_dependency(include_directories: 'libexslt',
  link_with: exslt_lib)

xsltproc = executable('xsltproc', 'xsltproc/xsltproc.c',
  dependencies: [libexslt_dep, libxslt_dep, xml_dep])

meson.override_find_program('xsltproc', xsltproc)
