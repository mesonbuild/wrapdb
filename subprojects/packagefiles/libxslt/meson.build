project('libxslt', 'c', license: 'MIT', version: '1.1.37', meson_version: '>=0.54.0')

#time_r functions under MinGW
if host_machine.system() == 'windows'
  add_project_arguments('-D_POSIX_C_SOURCE', language: 'c')
endif

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
    config.set10('HAVE_' + h.underscorify().to_upper(), true)
  endif
endforeach

functions = {
  'ftime': 'sys/timeb.h',
  'gettimeofday': 'sys/time.h',
  'gmtime_r': 'time.h',
  'localtime_r': 'time.h',
  'snprintf': 'stdio.h',
  'strxfrm_l': 'string.h',
  'stat': 'sys/stat.h',
  'vsnprintf': 'stdio.h',
  '_stat': 'sys/stat.h',
}

foreach f, h : functions
  if cc.has_header_symbol(h, f, args: '-D_POSIX_C_SOURCE')
    config.set10('HAVE_' + f.underscorify().to_upper(), true)
  endif
endforeach

threads_dep = dependency('threads', required: false)
if threads_dep.found()
  config.set('HAVE_LIBPTHREAD', true)
  config.set('HAVE_PTHREAD_H', cc.has_header('pthread.h'))
endif

libm = cc.find_library('m', required: false)
librt = cc.find_library('rt', required: false)
config.set('HAVE_CLOCK_GETTIME', cc.has_function('clock_gettime', dependencies: [librt, threads_dep]))

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

libxml2_dep = dependency('libxml-2.0')
with_modules = libxml2_dep.get_variable(pkgconfig: 'modules', internal: 'modules', default_value: '0').to_int() != 0

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
