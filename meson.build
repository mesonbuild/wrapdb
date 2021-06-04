project('exif', 'c', license: 'LGPL-2.1', version: '0.6.22')

cc = meson.get_compiler('c')

deps = [meson.get_compiler('c').find_library('m', required: false)]

cdata = configuration_data()

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
  ['HAVE_DLFCN_H', 'dlfcn.h'],
  ['HAVE_INTTYPES_H', 'inttypes.h'],
  ['HAVE_MEMORY_H', 'memory.h'],
  ['HAVE_STDINT_H', 'stdint.h'],
  ['HAVE_STDLIB_H', 'stdlib.h'],
  ['HAVE_STRINGS_H', 'strings.h'],
  ['HAVE_STRING_H', 'string.h'],
  ['HAVE_SYS_STAT_H', 'sys/stat.h'],
  ['HAVE_SYS_TYPES_H', 'sys/types.h'],
  ['HAVE_UNISTD_H', 'unistd.h'],
]

foreach h : check_headers
  if cc.has_header(h.get(1))
    cdata.set(h.get(0), 1)
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
    'libexif/exif-ifd.c',
    'libexif/exif-loader.c',
    'libexif/exif-log.c',
    'libexif/exif-mem.c',
    'libexif/exif-mnote-data.c',
    'libexif/exif-tag.c',
    'libexif/exif-utils.c',
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

install_headers('libexif/exif-data.h', subdir: 'libexif')

exif_dep = declare_dependency(link_with: exif)
