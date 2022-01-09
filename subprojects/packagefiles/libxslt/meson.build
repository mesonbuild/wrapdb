project('libxslt', 'c',
  version : '1.1.34')

exslt_version = '0.8.20'
pkg = import('pkgconfig')
cc = meson.get_compiler('c')
config = configuration_data()

headers = [
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
  'strxfrm_l',
  'stat',
  '_stat',
  'gettimeofday',
  'localtime',
  'localtime_r',
  'time',
  'gmtime',
  'gmtime_r',
  'ftime',
]

foreach f : functions
  if cc.has_function(f)
    config.set10('HAVE_' + h.underscorify().to_upper(), true)
  endif
endforeach

threads_dep = dependency('threads', required : false)
if threads_dep.found()
  config.set('HAVE_LIBPTHREAD', true)
  config.set('HAVE_PTHREAD_H', true)
endif

libm = cc.find_library('m', required : false)
config.set('HAVE_POW', cc.has_function('pow', dependencies : libm))
config.set('HAVE_FLOOR', cc.has_function('floor', dependencies : libm))
config.set('HAVE_FABS', cc.has_function('fabs', dependencies : libm))

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
with_crypto = libgcrypt_dep.found()

libxml2_dep = dependency('libxml-2.0')
with_modules = libxml2_dep.get_variable(
  pkgconfig : 'modules',
  internal : 'modules',
  default_value : '0').to_int()

with_debugger = get_option('debugger')
with_mem_debug = get_option('mem_debug')
with_profiler = get_option('profiler')
with_xslt_debug = get_option('xslt_debug')

configure_file(output : 'config.h',
  configuration : config,
)

incdir = include_directories('.')
subdir('libxslt')
subdir('libexslt')
subdir('xsltproc')
