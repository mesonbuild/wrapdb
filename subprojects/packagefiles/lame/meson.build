project(
  'lame',
  'c',
  version: '3.100',
  meson_version: '>=0.49',
  license: 'LGPL-2.1-or-later',
  default_options: ['warning_level=0'],
)

cc = meson.get_compiler('c')
cpu_family = host_machine.cpu_family()

build_decoder = get_option('decoder')

cdata = configuration_data()
check_headers = [
  'alloca.h',
  'ctype.h',
  'errno.h',
  'fcntl.h',
  'inttypes.h',
  'limits.h',
  'linux/soundcard.h',
  'sys/soundcard.h',
  'memory.h',
  'stdarg.h',
  'stddef.h',
  'stdint.h',
  'stdio.h',
  'stdlib.h',
  'string.h',
  'strings.h',
  'sys/stat.h',
  'sys/time.h',
  'sys/types.h',
  'unistd.h',
]

if cc.check_header('xmmintrin.h')
  cdata.set('HAVE_XMMINTRIN_H', 1)
endif

foreach h : check_headers
  if cc.has_header(h)
    cdata.set('HAVE_' + h.underscorify().to_upper(), 1)
  endif
endforeach

stdtypes = [
  'int8_t',
  'int16_t',
  'int32_t',
  'int64_t',
  'uint8_t',
  'uint16_t',
  'uint32_t',
  'uint64_t',
  'long double',
]

foreach t : stdtypes
  if cc.has_type(
    t,
    prefix: '#include <stdint.h>',
  )
    cdata.set('HAVE_@0@'.format(t.underscorify().to_upper()), 1)
  endif
endforeach

cdata.set('A_INT32_T', 'int')
cdata.set('A_INT64_T', cc.sizeof('long') == 8 ? 'long' : 'long long')
cdata.set('A_UINT32_T', 'unsigned int')
cdata.set(
  'A_UINT64_T',
  cc.sizeof('long') == 8 ? 'unsigned long' : 'unsigned long long',
)

sizes = [
  'double',
  'float',
  'int',
  'long',
  'long long',
  'long double',
  'short',
  'unsigned int',
  'unsigned long',
  'unsigned long long',
  'unsigned short',
]

foreach s : sizes
  cdata.set('SIZEOF_@0@'.format(s.underscorify().to_upper()), cc.sizeof(s))
endforeach

if cc.sizeof('long double') > cc.sizeof('double')
  cdata.set('HAVE_LONG_DOUBLE_WIDER', 1)
endif

# mingw32 does not enable SSE by default
if cc.get_argument_syntax() == 'gcc' and cpu_family == 'x86'
  add_project_arguments(
    '-msse',
    language: 'c',
  )
endif

# Approximate autoconf's STDC_HEADERS define
have_stdc_headers = true
stdc_headers = [
  'HAVE_CTYPE_H',
  'HAVE_STDARG_H',
  'HAVE_STDDEF_H',
  'HAVE_STDIO_H',
  'HAVE_STDINT_H',
  'HAVE_STDLIB_H',
  'HAVE_STRING_H',
]
foreach h : stdc_headers
  if not cdata.has(h)
    have_stdc_headers = false
  endif
endforeach
if have_stdc_headers
  cdata.set('STDC_HEADERS', 1)
endif

# Enable the decoder
if build_decoder
  cdata.set('HAVE_MPGLIB', 1)
  cdata.set('DECODE_ON_THE_FLY', 1)
endif

check_functions = {
  'alloca': 'alloca.h',
  'gettimeofday': 'sys/time.h',
  'memcpy': 'string.h',
  'socket': 'sys/socket.h',
  'strchr': 'string.h',
  'strtol': 'stdlib.h',
}

foreach f, h : check_functions
  if cc.has_function(
    f,
    prefix: '#include <@0@>'.format(h),
  )
    cdata.set('HAVE_@0@'.format(f.underscorify().to_upper()), 1)
  endif
endforeach

# These functions are used unconditionally
need_functions = {
  'strtol': 'stdlib.h',
}

foreach f, h : need_functions
  if not cc.has_function(
    f,
    prefix: '#include <@0@>'.format(h),
  )
    error('Need @0@() from @1@'.format(f, h))
  endif
endforeach

if meson.version().version_compare('>= 0.62')
  dl_dep = dependency(
    'dl',
    required: false,
  )
else
  dl_dep = cc.find_library(
    'dl',
    required: false,
  )
endif

if dl_dep.found() and cc.has_header('dlfcn.h')
  cdata.set('HAVE_DLFCN_H', 1)
endif

if meson.version().version_compare('>= 0.54')
  curses_dep = dependency(
    'curses',
    required: get_option('tools'),
  )
else
  curses_dep = dependency(
    '',
    required: false,
  )
endif

if curses_dep.found()
  if cc.has_header('ncurses/termcap.h')
    cdata.set('HAVE_NCURSES_TERMCAP_H', 1)
  endif
  if cc.has_header('termcap.h')
    cdata.set('HAVE_TERMCAP_H', 1)
  endif
  cdata.set('HAVE_TERMCAP', 1)
endif

if meson.version().version_compare('>= 0.60') and cc.has_header('langinfo.h')
  iconv_dep = dependency(
    'iconv',
    required: get_option('iconv'),
  )
else
  iconv_dep = dependency(
    '',
    required: false,
  )
endif

if iconv_dep.found() and cc.has_header('langinfo.h')
  cdata.set('HAVE_ICONV', 1)

  iconv_const_test = '''
      #include <iconv.h>
      size_t iconv(iconv_t, const char**, size_t*, char**, size_t*);
      int main(){}
      '''
  cdata.set(
    'ICONV_CONST',
    cc.compiles(
      iconv_const_test,
      dependencies: iconv_dep,
    ) ? 'const' : '',
  )
endif

cdata.set_quoted('PACKAGE', meson.project_name())
cdata.set_quoted('PACKAGE_NAME', meson.project_name())
cdata.set_quoted('PACKAGE_TARNAME', meson.project_name())
cdata.set_quoted('PACKAGE_VERSION', meson.project_version())
cdata.set_quoted('VERSION', meson.project_version())
cdata.set_quoted('PACKAGE_BUGREPORT', 'lame-dev@lists.sf.net')
cdata.set_quoted('PACKAGE_URL', '')
cdata.set(
  'PACKAGE_STRING',
  '"@0@ @1@"'.format(meson.project_name(), meson.project_version()),
)

cdata.set('TIME_WITH_SYS_TIME', 1)
cdata.set_quoted('LT_OBJDIR', '.libs/')
cdata.set('LAME_LIBRARY_BUILD', 1)
cdata.set('_POSIX_PTHREAD_SEMANTICS', 1)
cdata.set('_ALL_SOURCE', 1)
cdata.set('_GNU_SOURCE', 1)
cdata.set('_TANDEM_SOURCE', 1)
cdata.set('__EXTENSIONS__', 1)

#hacks
cdata.set('TAKEHIRO_IEEE754_HACK', 1)
cdata.set('USE_FAST_LOG', 1)
cdata.set('HAVE_IEEE854_FLOAT80', 1)

configure_file(
  input: 'config.h.meson',
  output: 'config.h',
  configuration: cdata,
)

common_args = ['-DHAVE_CONFIG_H']
subdir('include/lame')
lameinc = include_directories('include')
confinc = include_directories('.')

m_dep = cc.find_library(
  'm',
  required: false,
)

windows = import('windows')

if build_decoder
  subdir('mpglib')
endif
subdir('libmp3lame')
if curses_dep.found()
  subdir('frontend')
endif
