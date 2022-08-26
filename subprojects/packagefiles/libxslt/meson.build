project('libxslt', 'c',
  version : '1.1.36',
  meson_version: '>=0.54.0')

exslt_version = '0.8.20'
pkg = import('pkgconfig')
cc = meson.get_compiler('c')
config = configuration_data()

headers = [
  'inttypes.h',
  'xlocale.h',
  'sys/types.h',
  'sys/time.h',
  'stdlib.h',
  'unistd.h',
  'string.h',
  'locale.h',
  'xlocale.h',
  'ieeefp.h',
  'nan.h',
  'math.h',
  'fp_class.h',
  'float.h',
  'sys/timeb.h',
  'time.h',
  'sys/stat.h',
  'sys/select.h',
  'stdarg.h',
  'errno.h',
]

foreach h : headers
  if cc.has_header(h)
    config.set10('HAVE_' + h.underscorify().to_upper(), true)
  endif
endforeach

functions = [
  'ftime',
  'gettimeofday',
  'gmtime_r',
  'localtime_r',
  'snprintf',
  'strxfrm_l',
  'stat',
  'vsnprintf',
  '_stat',
]

foreach f : functions
  if cc.has_function(f)
    config.set10('HAVE_' + f.underscorify().to_upper(), true)
  endif
endforeach

threads_dep = dependency('threads', required : false)
if threads_dep.found()
  config.set('HAVE_LIBPTHREAD', true)
  config.set('HAVE_PTHREAD_H', true)
endif

libm = cc.find_library('m', required : false)
librt = cc.find_library('rt', required : false)
config.set('HAVE_CLOCK_GETTIME', cc.has_function('clock_gettime', dependencies : librt))

trio_functions = [
  'printf',
  'sprintf',
  'fprintf',
  'snprintf',
  'vfprintf',
  'vsprintf',
  'vsnprintf',
  'sscanf',
]

with_trio = false
foreach f : trio_functions
  if not cc.has_function(f)
    with_trio = true
    break
  endif
endforeach

libgcrypt_dep = dependency('libgcrypt', version : '>=1.1.42',
  required : get_option('crypto'))

libxml2_dep = dependency('libxml-2.0')
with_modules = libxml2_dep.get_variable(
  pkgconfig : 'modules',
  internal : 'modules',
  default_value : '0').to_int() != 0

configure_file(
  input: 'config.h.cmake.in',
  output : 'config.h',
  format: 'cmake@',
  configuration : config,
)

incdir = include_directories('.')
subdir('libxslt')
subdir('libexslt')
subdir('xsltproc')
