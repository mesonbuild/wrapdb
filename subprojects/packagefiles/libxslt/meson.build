project(
  'libxslt',
  'c',
  license: 'MIT',
  version: '1.1.43',
  meson_version: '>=0.54.1',
)

exslt_version = '0.8.20'
pkg = import('pkgconfig')
cc = meson.get_compiler('c')
config = configuration_data()

headers = [
  'inttypes.h',
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
    config.set('HAVE_@0@'.format(h.underscorify().to_upper()), 1)
  endif
endforeach

threads_dep = dependency('threads', required: false)
if threads_dep.found()
  config.set('HAVE_LIBPTHREAD', true)
  config.set('HAVE_PTHREAD_H', cc.has_header('pthread.h'))
endif

libm = cc.find_library('m', required: false)
librt = cc.find_library('rt', required: false)

functions = {
  'clock_gettime': [librt, threads_dep],
  'ftime': [],
  'gettimeofday': [],
  'gmtime_r': [],
  'localtime_r': [],
  'strxfrm_l': [],
  'stat': [],
  '_stat': [],
}

foreach f, d : functions
  if cc.has_function(f, dependencies: d)
    config.set('HAVE_@0@'.format(f.to_upper()), 1)
  endif
endforeach

foreach m : ['snprintf', 'vsnprintf']
  if cc.has_header_symbol('stdio.h', m)
    config.set('HAVE_@0@'.format(m.to_upper()), 1)
  endif
endforeach

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
  if not cc.has_header_symbol('stdio.h', f)
    with_trio = true
    break
  endif
endforeach

libgcrypt_dep = dependency('libgcrypt', version: '>=1.1.42', required: get_option('crypto'))
if libgcrypt_dep.found()
  config.set('HAVE_GCRYPT', 1)
endif

libxml2_dep = dependency('libxml-2.0', version: '>=2.9.10')
with_modules = libxml2_dep.get_variable(pkgconfig: 'modules', internal: 'modules', default_value: '0').to_int() != 0
if host_machine.system() in ['cygwin', 'windows']
  config.set('MODULE_EXTENSION', '.dll')
else
  config.set('MODULE_EXTENSION', '.so')
endif

configure_file(
  input: 'config.h.cmake.in',
  output: 'config.h',
  format: 'cmake@',
  configuration: config,
)

incdir = include_directories('.')
subdir('libxslt')
subdir('libexslt')
subdir('xsltproc')
