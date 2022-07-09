project('lame', 'c',
        version : '3.100',
        meson_version : '>=0.49',
        license: 'LGPL-2.1+')

cc = meson.get_compiler('c')
cpu_family = host_machine.cpu_family()

build_tools = get_option('tools')
build_decoder = get_option('decoder')

cdata = configuration_data()
check_headers = [
  'ctype.h',
  'errno.h',
  'fcntl.h',
  'inttypes.h',
  'limits.h',
  # used by misc/*.c which we don't build right now
  #'linux/soundcard.h',
  #'sys/soundcard.h',
  'stdarg.h',
  'stddef.h',
  'stdint.h',
  'stdio.h',
  'stdlib.h',
  'string.h',
]

if cpu_family == 'x86_64' or cpu_family == 'x86'
  check_headers += ['xmmintrin.h']
endif

if build_tools
  check_headers += [
    'ncurses/termcap.h',
    'termcap.h',
    'unistd.h',
  ]
endif

foreach h : check_headers
  if cc.has_header(h)
    cdata.set('HAVE_' + h.underscorify().to_upper(), 1)
  endif
endforeach

# mingw32 does not enable SSE by default
if cc.get_argument_syntax() == 'gcc' and cpu_family == 'x86'
  add_project_arguments('-msse', language: 'c')
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
endif

check_functions = [
# check token HAVE_ICONV
# check token HAVE_NASM
  ['HAVE_MEMCPY', 'memcpy', '#include<string.h>'],
  ['HAVE_STRCHR', 'strchr', '#include<string.h>'],
]

if build_tools
  check_functions += [
    ['HAVE_SOCKET', 'socket', '#include<sys/socket.h>'],
# check token HAVE_TERMCAP
  ]
endif

# HACK
if cc.has_header('stdint.h')
  cdata.set('HAVE_UINT8_T', true)
  cdata.set('HAVE_UINT16_T', true)
  cdata.set('HAVE_UINT32_T', true)
  cdata.set('HAVE_UINT64_T', true)
  cdata.set('HAVE_INT8_T', true)
  cdata.set('HAVE_INT16_T', true)
  cdata.set('HAVE_INT32_T', true)
  cdata.set('HAVE_INT64_T', true)
endif

foreach f : check_functions
  if cc.has_function(f.get(1), prefix : f.get(2))
    cdata.set(f.get(0), 1)
  endif
endforeach

# These functions are used unconditionally
need_functions = [
  ['HAVE_STRTOL', 'strtol', '#include<stdlib.h>'],
]

foreach f : need_functions
  if not cc.has_function(f.get(1), prefix : f.get(2))
    error('Need @0@() from @1@'.format(f.get(1), f.get(2)))
  endif
endforeach

cdata.set('SIZEOF_DOUBLE', cc.sizeof('double'))
cdata.set('SIZEOF_FLOAT', cc.sizeof('float'))
cdata.set('SIZEOF_INT', cc.sizeof('int'))
cdata.set('SIZEOF_LONG', cc.sizeof('long'))
cdata.set('SIZEOF_LONG_DOUBLE', cc.sizeof('long double'))
cdata.set('SIZEOF_LONG_LONG', cc.sizeof('long long'))
cdata.set('SIZEOF_SHORT', cc.sizeof('short'))
cdata.set('SIZEOF_UNSIGNED_INT', cc.sizeof('unsigned int'))
cdata.set('SIZEOF_UNSIGNED_LONG', cc.sizeof('unsigned long'))
cdata.set('SIZEOF_UNSIGNED_LONG_LONG', cc.sizeof('unsigned long long'))
cdata.set('SIZEOF_UNSIGNED_SHORT', cc.sizeof('unsigned short'))
cdata.set('ieee754_float32_t', 'float')
cdata.set('ieee754_float64_t', 'double')

have_visibility_hidden = cc.has_argument('-fvisibility=hidden')
if have_visibility_hidden
  add_project_arguments('-fvisibility=hidden', language: 'c')
endif

if cc.get_id() == 'msvc' and get_option('default_library') != 'static'
  export_define = '__declspec(dllexport) extern'
elif cc.has_argument('-fvisibility=hidden')
  add_project_arguments('-fvisibility=hidden', language: 'c')
  export_define = 'extern __attribute__ ((visibility ("default")))'
else
  export_define = 'extern'
endif

cdata.set('LAME_EXPORT', export_define)

configure_file(output : 'config.h',
  configuration : cdata)

common_args = ['-DHAVE_CONFIG_H']
lameinc = include_directories('include', 'libmp3lame')
confinc = include_directories('.')

m_dep = cc.find_library('m', required : false)

if build_decoder
  subdir('mpglib')
endif
subdir('libmp3lame')
if build_tools
  subdir('frontend')
endif
