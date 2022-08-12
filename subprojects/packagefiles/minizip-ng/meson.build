project('minizip-ng', 'c',
  version: '3.0.6',
  default_options: ['warning_level=1'],
)

if host_machine.system() == 'windows' and get_option('buildtype') != 'static'
  add_project_arguments('-DMZ_EXPORTS', language: 'c')
endif

cc = meson.get_compiler('c')
if cc.has_header('stdint.h')
  add_project_arguments('-DHAVE_STDINT_H', language: 'c')
endif

if cc.has_header('inttypes.h')
  add_project_arguments('-DHAVE_INTTYPES_H', language: 'c')
endif

if cc.has_function('getrandom')
  add_project_arguments('-DHAVE_GETRANDOM', language: 'c')
endif

if not cc.has_function('fseeko')
  add_project_arguments('-DNO_FSEEKO', language: 'c')
endif

sources = files(
  'mz_crypt.c',
  'mz_os.c',
  'mz_strm.c',
  'mz_strm_buf.c',
  'mz_strm_mem.c',
  'mz_strm_split.c',
  'mz_zip.c',
  'mz_zip_rw.c',
)

if host_machine.system() == 'windows'
  sources += files('mz_os_win32.c', 'mz_strm_os_win32.c')
else
  sources += files('mz_os_posix.c', 'mz_strm_os_posix.c')
endif

compat = get_option('compat')
if compat
  sources += files('mz_compat.c')
  add_project_arguments('-DHAVE_COMPAT', language: 'c')
endif

bsd_dep = dependency('libbsd', required: get_option('bsd'))
if bsd_dep.found()
  add_project_arguments('-DHAVE_LIBBSD', language: 'c')
endif

if cc.has_function('arc4random_buf', dependencies: bsd_dep)
  add_project_arguments('-DHAVE_ARC4RANDOM_BUF', language: 'c')
endif

if cc.has_function('arc4random', dependencies: bsd_dep)
  add_project_arguments('-DHAVE_ARC4RANDOM', language: 'c')
endif

crypt_dep = dependency('openssl', required: get_option('wzaes'))
if crypt_dep.found()
  sources += files('mz_crypt_openssl.c')
elif host_machine.system() == 'windows'
  crypt_dep = cc.find_library('crypt32', required: get_option('wzaes'))
  if crypt_dep.found()
    sources += files('mz_crypt_win32.c')
  endif
elif host_machine.system() == 'darwin'
  crypt_dep = dependency('appleframeworks', modules : [ 'CoreFoundation', 'Security' ], required: get_option('wzaes'))
  if crypt_dep.found()
    sources += files('mz_crypt_apple.c')
  endif
endif

if crypt_dep.found()
  sources += files('mz_strm_wzaes.c')
  add_project_arguments('-DHAVE_WZAES', language: 'c')
  add_project_arguments('-DMZ_ZIP_SIGNING', language: 'c')
else
  add_project_arguments('-DMZ_ZIP_NO_ENCRYPTION', language: 'c')
  add_project_arguments('-DMZ_ZIP_NO_CRYPTO', language: 'c')
endif

iconv_dep = dependency('iconv', required: get_option('iconv'))
if iconv_dep.found()
  add_project_arguments('-DHAVE_ICONV', language: 'c')
endif

bzip2_dep = dependency('bzip2', required: get_option('bzip2'))
if bzip2_dep.found()
  sources += files('mz_strm_bzip.c')
  add_project_arguments('-DHAVE_BZIP2', language: 'c')
endif

lzma_dep = dependency('liblzma', required: get_option('lzma'))
if lzma_dep.found()
  sources += files('mz_strm_lzma.c')
  add_project_arguments('-DHAVE_LZMA', language: 'c')
endif

zlib_dep = dependency('zlib-ng', required: get_option('zlib'))
if not zlib_dep.found()
  zlib_dep = dependency('zlib', required: get_option('zlib'))
  if zlib_dep.found()
    add_project_arguments('-DZLIB_COMPAT', language: 'c')
  endif
endif
if zlib_dep.found()
  sources += files('mz_strm_zlib.c')
  add_project_arguments('-DHAVE_ZLIB', language: 'c')
endif

zstd_dep = dependency('libzstd', required: get_option('zstd'))
if zstd_dep.found()
  sources += files('mz_strm_zstd.c')
  add_project_arguments('-DHAVE_ZSTD', language: 'c')
endif

if not zlib_dep.found() and not zstd_dep.found() and not bzip2_dep.found() and not lzma_dep.found()
  add_project_arguments('-DMZ_ZIP_NO_DECOMPRESSION', language: 'c')
  add_project_arguments('-DMZ_ZIP_NO_COMPRESSION', language: 'c')
endif

minizip_ng = library(compat ? 'minizip' : 'minizip-ng',
  sources,
  version: meson.project_version(),
  soversion: host_machine.system() == 'windows' ? '' : '3',
  vs_module_defs: 'mz.def',
  dependencies: [ bsd_dep, crypt_dep, iconv_dep, bzip2_dep, lzma_dep, zlib_dep, zstd_dep, ],
  install: true,
)

minizip_ng_dep = declare_dependency(
  include_directories: '.',
  link_with: minizip_ng,
)

pconf = import('pkgconfig')
pconf.generate(minizip_ng,
  description: 'Minizip zip file manipulation library',
)

headers = files(
  'mz.h',
  'mz_crypt.h',
  'mz_os.h',
  'mz_strm.h',
  'mz_strm_buf.h',
  'mz_strm_bzip.h',
  'mz_strm_lzma.h',
  'mz_strm_mem.h',
  'mz_strm_os.h',
  'mz_strm_pkcrypt.h',
  'mz_strm_split.h',
  'mz_strm_wzaes.h',
  'mz_strm_zlib.h',
  'mz_strm_zstd.h',
  'mz_zip.h',
  'mz_zip_rw.h',
)

if compat
  zip_h = configure_file(
    input: 'mz_compat_shim.h.in',
    output: 'zip.h',
    format: 'cmake@',
    configuration: {'MZ_COMPAT_FILE': 'MZ_COMPAT_ZIP', 'FILE_H': 'zip.h'},
  )

  unzip_h = configure_file(
    input: 'mz_compat_shim.h.in',
    output: 'unzip.h',
    format: 'cmake@',
    configuration: {'MZ_COMPAT_FILE': 'MZ_COMPAT_UNZIP', 'FILE_H': 'unzip.h'},
  )

  headers += files('mz_compat.h')
  headers += zip_h
  headers += unzip_h
endif

install_headers(
  headers,
)
