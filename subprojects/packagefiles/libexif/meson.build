project('exif', 'c', license: 'LGPL-2.1', version: '0.6.24')

cc = meson.get_compiler('c')

deps = [meson.get_compiler('c').find_library('m', required: false)]

cdata = configuration_data()

#bugfix for msvc builds
if cc.get_id() == 'msvc'
  add_project_arguments('-Dssize_t=ptrdiff_t', language : 'c')
endif

check_functions = [
  ['HAVE_DCGETTEXT', 'dcgettext', '#include <libintl.h>'],
  ['HAVE_GETTEXT', 'gettext', '#include <libintl.h>'],
  ['HAVE_ICONV', 'iconv', '#include <iconv.h>'],
  ['HAVE_LOCALTIME_R', 'localtime_r', '#include <time.h>'],
]

foreach f : check_functions
  if cc.has_function(f.get(1), prefix : f.get(2))
    cdata.set(f.get(0), 1)
  endif
endforeach

check_headers = [
  'dlfcn.h',
  'inttypes.h',
  'memory.h',
  'stdint.h',
  'stdlib.h',
  'strings.h',
  'string.h',
  'sys/stat.h',
  'sys/types.h',
  'unistd.h',
]

foreach h : check_headers
  if cc.has_header(h)
    cdata.set('HAVE_' + h.underscorify().to_upper(), 1)
  endif
endforeach

configure_file(input : 'meson_config.h.meson',
  output : 'config.h',
  configuration : cdata)

sources = [
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
    'libexif/apple/exif-mnote-data-apple.c',
    'libexif/apple/mnote-apple-entry.c',
    'libexif/apple/mnote-apple-tag.c',
    'libexif/pentax/exif-mnote-data-pentax.c',
    'libexif/pentax/mnote-pentax-entry.c',
    'libexif/pentax/mnote-pentax-tag.c',
    'libexif/canon/exif-mnote-data-canon.c',
    'libexif/canon/mnote-canon-entry.c',
    'libexif/canon/mnote-canon-tag.c',
    'libexif/olympus/exif-mnote-data-olympus.c',
    'libexif/olympus/mnote-olympus-entry.c',
    'libexif/olympus/mnote-olympus-tag.c',
    'libexif/fuji/exif-mnote-data-fuji.c',
    'libexif/fuji/mnote-fuji-entry.c',
    'libexif/fuji/mnote-fuji-tag.c'
]

exif = shared_library(
    'exif', sources,
    install: true,
    dependencies: deps,
    include_directories : '.',
    soversion: 0, version: '0.6.22'
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
  subdir: 'libexif'
)

exif_dep = declare_dependency(
  include_directories : '.',
  link_with: exif,
)
