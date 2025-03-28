project(
  'exif',
  'c',
  license: 'LGPL-2.1',
  version: '0.6.25',
  meson_version: '>=0.49.0',
)

cc = meson.get_compiler('c')

m_dep = cc.find_library('m', required: false)
if meson.version().version_compare('>= 0.59')
  intl_dep = dependency('intl', required: get_option('nls'))
else
  intl_dep = dependency('', required: false)
endif

#bugfix for msvc builds
if cc.get_argument_syntax() == 'msvc'
  add_project_arguments('-Dssize_t=ptrdiff_t', language: 'c')
endif

cdata = configuration_data()
cdata.set('HAVE_LOCALTIME_R', cc.has_function('localtime_r'))
cdata.set('HAVE_LOCALTIME_S', cc.has_header_symbol('time.h', 'localtime_s'))
cdata.set('ENABLE_NLS', intl_dep.found())
cdata.set_quoted('GETTEXT_PACKAGE', '@0@-@1@'.format(meson.project_name(), meson.project_version()))
cdata.set_quoted('LOCALEDIR', get_option('prefix') / get_option('localedir'))

configure_file(
  output: 'config.h',
  configuration: cdata,
)

sources = files(
  'libexif/canon/exif-mnote-data-canon.c',
  'libexif/canon/mnote-canon-entry.c',
  'libexif/canon/mnote-canon-tag.c',
  'libexif/exif-byte-order.c',
  'libexif/exif-content.c',
  'libexif/exif-data.c',
  'libexif/exif-entry.c',
  'libexif/exif-format.c',
  'libexif/exif-gps-ifd.c',
  'libexif/exif-ifd.c',
  'libexif/exif-loader.c',
  'libexif/exif-log.c',
  'libexif/exif-mem.c',
  'libexif/exif-mnote-data.c',
  'libexif/exif-tag.c',
  'libexif/exif-utils.c',
  'libexif/fuji/exif-mnote-data-fuji.c',
  'libexif/fuji/mnote-fuji-entry.c',
  'libexif/fuji/mnote-fuji-tag.c',
  'libexif/olympus/exif-mnote-data-olympus.c',
  'libexif/olympus/mnote-olympus-entry.c',
  'libexif/olympus/mnote-olympus-tag.c',
  'libexif/pentax/exif-mnote-data-pentax.c',
  'libexif/pentax/mnote-pentax-entry.c',
  'libexif/pentax/mnote-pentax-tag.c',
)

defs = custom_target(
  'defs',
  input: 'libexif/libexif.sym',
  output: 'libexif.def',
  command: ['def.py', '@INPUT@', '@OUTPUT@'],
)

exif = library(
  'exif',
  sources,
  vs_module_defs: defs,
  install: true,
  dependencies: [m_dep, intl_dep],
  version: '12.3.4',
)

install_headers(
  'libexif/exif-byte-order.h',
  'libexif/exif-content.h',
  'libexif/exif-data.h',
  'libexif/exif-data-type.h',
  'libexif/exif-entry.h',
  'libexif/exif-format.h',
  'libexif/exif-ifd.h',
  'libexif/exif-loader.h',
  'libexif/exif-log.h',
  'libexif/exif-mem.h',
  'libexif/exif-mnote-data.h',
  'libexif/exif-tag.h',
  'libexif/exif-utils.h',
  'libexif/_stdint.h',
  subdir: 'libexif',
)

depinc = include_directories('.')
exif_dep = declare_dependency(
  include_directories: depinc,
  link_with: exif,
)

if meson.version().version_compare('>=0.54.0')
  meson.override_dependency('libexif', exif_dep)
endif

subdir('contrib')
subdir('test')
