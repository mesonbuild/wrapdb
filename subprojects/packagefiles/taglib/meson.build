project(
  'taglib',
  'cpp',
  license: 'LGPL-2.1-or-later OR MPL-1.1',
  version: '2.0.2',
  meson_version: '>=0.55',
  default_options: ['cpp_std=c++17', 'warning_level=1'],
)

cpp = meson.get_compiler('cpp')

add_project_arguments(
  cpp.get_supported_arguments('/wd4244', '/wd4251', '/wd4910'),
  language: 'cpp',
)

if get_option('default_library') != 'static'
  add_project_arguments(
    '-DMAKE_TAGLIB_LIB',
    language: 'cpp',
  )
else
  add_project_arguments(
    '-DTAGLIB_STATIC',
    language: 'cpp',
  )
endif

cdata = configuration_data()
cdata.set('HAVE_GCC_BYTESWAP', cpp.has_function('__builtin_bswap64'))
cdata.set(
  'HAVE_GLIBC_BYTESWAP',
  cpp.has_function(
    '__bswap_64',
    prefix: '#include <byteswap.h>',
  ),
)
cdata.set(
  'HAVE_MSC_BYTESWAP',
  cpp.has_function(
    '_byteswap_uint64',
    prefix: '#include <stdlib.h>',
  ),
)
cdata.set(
  'HAVE_MAC_BYTESWAP',
  cpp.has_function(
    'OSSwapInt64',
    prefix: '#include <libkern/OSByteOrder.h>',
  ),
)
cdata.set(
  'HAVE_OPENBSD_BYTESWAP',
  cpp.has_function(
    'swap64',
    prefix: '#include <sys/endian.h>',
  ),
)

zlib_dep = dependency(
  'zlib',
  required: get_option('zlib'),
)
if zlib_dep.found()
  cdata.set('HAVE_ZLIB', true)
endif

configure_file(
  input: 'config.h.cmake',
  output: 'config.h',
  format: 'cmake@',
  configuration: cdata,
)

subdir('taglib')
subdir('tests')
