if get_option('default_library') == 'static'
  quazip_args = ['-DQUAZIP_STATIC']
  quazip_dep_args = ['-DQUAZIP_STATIC']
else
  quazip_args = ['-DQUAZIP_BUILD']
  quazip_dep_args = []
endif

quazip_moc_headers = ['quagzipfile.h', 'quaziodevice.h', 'quazipfile.h']

quazip_src = [
  'qioapi.cpp',
  'JlCompress.cpp',
  'quaadler32.cpp',
  'quachecksum32.cpp',
  'quacrc32.cpp',
  'quagzipfile.cpp',
  'quaziodevice.cpp',
  'quazip.cpp',
  'quazipdir.cpp',
  'quazipfile.cpp',
  'quazipfileinfo.cpp',
  'quazipnewinfo.cpp',
  'unzip.c',
  'zip.c',
]

quazip_pp = qt.preprocess(
  moc_headers: quazip_moc_headers,
)

quazip_lib = library(
  'quazip',
  quazip_src,
  quazip_pp,
  dependencies: [qt_dep, zlib_dep],
  cpp_args: quazip_args,
)

quazip_incdir = include_directories('.')

quazip_dep = declare_dependency(
  version: meson.project_version(),
  include_directories: quazip_incdir,
  compile_args: quazip_dep_args,
  link_with: quazip_lib,
)
