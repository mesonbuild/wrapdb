project(
  'minizip-ng',
  'c',
  version: '4.0.4',
  license: 'BSD-3-Clause',
  default_options: ['warning_level=1'],
  meson_version: '>=0.49.0',
)

cc = meson.get_compiler('c')
if host_machine.system() == 'windows'
  add_project_arguments(cc.get_supported_arguments('/D_CRT_SECURE_NO_WARNINGS', '-Wno-deprecated-declarations'), language: 'c')
  if get_option('default_library') != 'static'
    add_project_arguments('-DMZ_EXPORTS', language: 'c')
  endif
  add_project_arguments('-D_WIN32_WINNT=0x600', language: 'c')
endif

margs = []
if cc.has_header('stdint.h')
  margs += '-DHAVE_STDINT_H'
endif

if cc.has_header('inttypes.h')
  margs += '-DHAVE_INTTYPES_H'
endif

if cc.has_function('getrandom')
  margs += '-DHAVE_GETRANDOM'
endif

if not cc.has_function('fseeko')
  margs += '-DNO_FSEEKO'
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

sources += files('mz_compat.c')
margs += '-DHAVE_COMPAT'

bsd_dep = dependency('libbsd', required: get_option('bsd'))
if bsd_dep.found()
  margs += '-DHAVE_LIBBSD'
endif

if cc.has_function('arc4random_buf', dependencies: bsd_dep)
  margs += '-DHAVE_ARC4RANDOM_BUF'
endif

if cc.has_function('arc4random', dependencies: bsd_dep)
  margs += '-DHAVE_ARC4RANDOM'
endif

bcrypt_dep = []
if host_machine.system() == 'windows'
  crypt_dep = cc.find_library('crypt32', required: get_option('wzaes'))
  if crypt_dep.found()
    sources += files('mz_crypt_winvista.c')
  endif
  bcrypt_dep = cc.find_library('bcrypt')
elif host_machine.system() == 'darwin'
  crypt_dep = dependency('appleframeworks', modules: ['CoreFoundation', 'Security'], required: get_option('wzaes'))
  if crypt_dep.found()
    sources += files('mz_crypt_apple.c')
  endif
else
  crypt_dep = dependency('openssl', required: get_option('wzaes'))
  if crypt_dep.found()
    sources += files('mz_crypt_openssl.c')
  endif
endif

if crypt_dep.found()
  sources += files('mz_strm_wzaes.c')
  margs += '-DHAVE_WZAES'
  margs += '-DMZ_ZIP_SIGNING'
else
  margs += '-DMZ_ZIP_NO_ENCRYPTION'
  margs += '-DMZ_ZIP_NO_CRYPTO'
endif

if meson.version().version_compare('>= 0.60')
  iconv_dep = dependency('iconv', required: get_option('iconv'))
else
  iconv_dep = dependency('', required: false)
endif
if iconv_dep.found()
  margs += '-DHAVE_ICONV'
endif

bzip2_dep = dependency('bzip2', required: get_option('bzip2'))
if bzip2_dep.found()
  sources += files('mz_strm_bzip.c')
  margs += '-DHAVE_BZIP2'
endif

lzma_dep = dependency('liblzma', required: get_option('lzma'))
if lzma_dep.found()
  sources += files('mz_strm_lzma.c')
  margs += '-DHAVE_LZMA'
endif

zlib_dep = dependency('zlib-ng', required: get_option('zlib'))
if not zlib_dep.found()
  zlib_dep = dependency('zlib', required: get_option('zlib'))
  if zlib_dep.found()
    margs += '-DZLIB_COMPAT'
  endif
endif
if zlib_dep.found()
  sources += files('mz_strm_zlib.c')
  margs += '-DHAVE_ZLIB'
endif

zstd_dep = dependency('libzstd', required: get_option('zstd'))
if zstd_dep.found()
  sources += files('mz_strm_zstd.c')
  margs += '-DHAVE_ZSTD'
endif

if not zlib_dep.found() and not zstd_dep.found() and not bzip2_dep.found() and not lzma_dep.found()
  margs += '-DMZ_ZIP_NO_DECOMPRESSION'
  margs += '-DMZ_ZIP_NO_COMPRESSION'
endif

minizip_ng = library(
  'minizip',
  sources,
  c_args: margs,
  version: meson.project_version(),
  soversion: host_machine.system() == 'windows' ? '' : '1',
  vs_module_defs: 'mz.def',
  dependencies: [
    bcrypt_dep,
    bsd_dep,
    crypt_dep,
    iconv_dep,
    bzip2_dep,
    lzma_dep,
    zlib_dep,
    zstd_dep,
  ],
  install: true,
)

pconf = import('pkgconfig')
pconf.generate(
  minizip_ng,
  description: 'Minizip zip file manipulation library',
  subdirs: 'minizip',
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

install_headers(
  headers,
)

subdir('include-workaround-meson/minizip')

depinc = include_directories('.', 'include-workaround-meson')
minizip_ng_dep = declare_dependency(
  include_directories: depinc,
  link_with: minizip_ng,
)

gtest_dep = dependency('gtest', required: get_option('tests'))
if gtest_dep.found()
  testdir = meson.current_source_dir()
  subdir('test')
endif
