project('check', 'c',
  default_options : ['warning_level=0', 'default_library=static'],
  version : '0.14.0',
  license : 'LGPL2.1',
)

check_version = meson.project_version()
cdata = configuration_data({
  'PROJECT_NAME' : meson.project_name(),
  'PROJECT_VERSION' : meson.project_version(),
  'MESON_VERSION' : meson.version(),
  'CHECK_MAJOR_VERSION' : check_version.split('.')[0],
  'CHECK_MINOR_VERSION' : check_version.split('.')[1],
  'CHECK_MICRO_VERSION' : check_version.split('.')[2],
})

cc = meson.get_compiler('c')

###############################################################################
# Per-compiler/platform additional flags
if host_machine.system() == 'windows'
  add_project_arguments([
    '-D_CRT_SECURE_NO_DEPRECATE',
    '-D_CRT_SECURE_NO_WARNINGS',
    '-D_CRT_NONSTDC_NO_WARNINGS',
    ], language : 'c')
  if cc.get_id() == 'clang-cl'
    add_project_arguments([
        '-fcolor-diagnostics',
        '-fansi-escape-codes',
      ], language : 'c')
  endif
endif

###############################################################################
check_headers = [
  'dlfcn.h',
  'errno.h',
  'fcntl.h',
  'inttypes.h',
  'limits.h',
  'locale.h',
  'memory.h',
  'regex.h',
  'signal.h',
  'stdarg.h',
  'stddef.h',
  'stdint.h',
  'stdlib.h',
  'strings.h',
  'string.h',
  'sys/stat.h',
  'sys/time.h',
  'sys/types.h',
  'sys/wait.h',
  'time.h',
  'unistd.h',
  'varargs.h',
]

foreach h : check_headers
  if cc.has_header(h)
    cdata.set('HAVE_' + h.underscorify().to_upper(), 1)
  endif
endforeach

###############################################################################
check_functions = [
  ['HAVE_CLOCK_GETTIME', 'clock_gettime', '#include <time.h>'],
  ['HAVE_DECL_ALARM', 'alarm', '#include <unistd.h>'],
  ['HAVE_DECL_LOCALTIME_R', 'localtime_r', '#include <time.h>'],
  ['HAVE_DECL_SETENV', 'setenv', '#include <stdlib.h>'],
  ['HAVE_DECL_STRDUP', 'strdup', '#include <string.h>'],
  ['HAVE_DECL_STRSIGNAL', 'strsignal', '#include <signal.h>'],
  ['HAVE_FORK', 'fork', '#include <unistd.h>'],
  ['HAVE_GETLINE', 'getline', '#include <stdio.h>'],
  ['HAVE_GETPID', 'getpid', '#include <unistd.h>'],
  ['HAVE_GETTIMEOFDAY', 'gettimeofday', '#include <sys/time.h>'],
  ['HAVE_MALLOC', 'malloc', '#include <stdlib.h>'],
  ['HAVE_MKSTEMP', 'mkstemp', '#include <stdlib.h>'],
  ['HAVE_REALLOC', 'realloc', '#include <stdlib.h>'],
  ['HAVE_REGCOMP', 'regcomp', '#include <regex.h>'],
  ['HAVE_REGEXEC', 'regexec', '#include <regex.h>'],
  ['HAVE_SIGACTION', 'sigaction', '#include <signal.h>'],
  ['HAVE_SNPRINTF', 'snprintf', '#include <stdio.h>'],
  ['HAVE_VASPRINTF', 'vasprintf', '#include <stdio.h>'],
  ['HAVE_VA_COPY', 'va-copy', '#include <stdarg.h>'],
  ['HAVE_VSNPRINTF', 'vsnprintf', '#include <stdio.h>'],
]

foreach f : check_functions
  variable = f[0]
  function = f[1]
  header = f[2]
  if cc.has_function(function, prefix : header)
    cdata.set(variable, 1)
  endif
endforeach


# Some check-specific definitions
if not cdata.has('HAVE_VSNPRINTF') and not cdata.has('HAVE_SNPRINTF')
  cdata.set('snprintf', 'rpl_snprintf')
  add_project_arguments('-Dsnprintf=rpl_snprintf', language : 'c')
  cdata.set('vsnprintf', 'rpl_vsnprintf')
  add_project_arguments('-Dvsnprintf=rpl_vsnprintf', language : 'c')
else
  cdata.set('HAVE_SNPRINTF', 1)
  add_project_arguments('-DHAVE_SNPRINTF=1', language : 'c')
  cdata.set('HAVE_VSNPRINTF', 1)
  add_project_arguments('-DHAVE_VSNPRINTF=1', language : 'c')
endif

if cdata.has('HAVE_FORK')
  cdata.set('HAVE_FORK', 1)
  add_project_arguments('-DHAVE_FORK=1', language : 'c')
else
  cdata.set('HAVE_FORK', 0)
  add_project_arguments('-DHAVE_FORK=0', language : 'c')
endif

if cdata.has('HAVE_MKSTEMP')
  cdata.set('HAVE_MKSTEMP', 1)
  add_project_arguments('-DHAVE_MKSTEMP=1', language : 'c')
else
  cdata.set('HAVE_MKSTEMP', 0)
  add_project_arguments('-DHAVE_MKSTEMP=0', language : 'c')
endif

if cdata.has('HAVE_DECL_ALARM')
  cdata.set('HAVE_DECL_ALARM', 1)
  add_project_arguments('-DHAVE_DECL_ALARM=1', language : 'c')
else
  cdata.set('HAVE_DECL_ALARM', 0)
  add_project_arguments('-DHAVE_DECL_ALARM=0', language : 'c')
endif

if cdata.has('HAVE_REGCOMP') and cdata.has('HAVE_REGEXEC')
  cdata.set('HAVE_REGEX', 1)
  add_project_arguments('-DHAVE_REGEX=1', language : 'c')
  cdata.set('ENABLE_REGEX', 1)
  add_project_arguments('-DENABLE_REGEX=1', language : 'c')
endif
# /Some check-specific definitions

###############################################################################
# Check for integer types

cdata.set('SIZEOF_CHAR', cc.sizeof('char'))
cdata.set('SIZEOF_INT', cc.sizeof('int'))
cdata.set('SIZEOF_LONG', cc.sizeof('long'))
cdata.set('SIZEOF_SHORT', cc.sizeof('short'))
cdata.set('SIZEOF_VOIDP', cc.sizeof('void*'))
cdata.set('SIZE_OF_SHORT', cc.sizeof('short'))
cdata.set('SIZE_OF_INT', cc.sizeof('int'))
cdata.set('SIZE_OF_LONG', cc.sizeof('long'))
cdata.set('SIZE_OF_LONG_LONG', cc.sizeof('long long'))
cdata.set('SIZE_OF_UNSIGNED_SHORT', cc.sizeof('unsigned short'))
cdata.set('SIZE_OF_UNSIGNED', cc.sizeof('unsigned'))
cdata.set('SIZE_OF_UNSIGNED_LONG', cc.sizeof('unsigned long'))
cdata.set('SIZE_OF_UNSIGNED_LONG_LONG', cc.sizeof('unsigned long long'))

cdata.set('__INT64', cc.sizeof('__int64'))
cdata.set('UNSIGNED__INT64', cc.sizeof('unsigned __int64'))

cdata.set('INT16_T', cc.sizeof('int16_t', prefix: '#include <stdint.h>'))
cdata.set('INT32_T', cc.sizeof('int32_t', prefix: '#include <stdint.h>'))
cdata.set('INT64_T', cc.sizeof('int64_t', prefix: '#include <stdint.h>'))
cdata.set('INTMAX_T', cc.sizeof('intmax_t', prefix: '#include <stdint.h>'))
cdata.set('UINT8_T', cc.sizeof('uint8_t', prefix: '#include <stdint.h>'))
cdata.set('UINT16_T', cc.sizeof('uint16_t', prefix: '#include <stdint.h>'))
cdata.set('UINT32_T', cc.sizeof('uint32_t', prefix: '#include <stdint.h>'))
cdata.set('UINT64_T', cc.sizeof('uint64_t', prefix: '#include <stdint.h>'))
cdata.set('UINTMAX_T', cc.sizeof('uintmax_t', prefix: '#include <stdint.h>'))

if not cc.has_type('clock_t', prefix : '#include <time.h>')
  cdata.set('clock_t', 'int')
  cdata.set('CLOCK_T', cc.sizeof('int'))
else
  cdata.set('CLOCK_T', cc.sizeof('clock_t', prefix : '#include <time.h>'))
endif

if not cc.has_type('clockid_t', prefix : '#include <time.h>')
  cdata.set('clockid_t', 'int')
  cdata.set('CLOCKID_T', cc.sizeof('int'))
else
  cdata.set('CLOCKID_T', cc.sizeof('clock_t', prefix : '#include <time.h>'))
endif

if cc.has_type('size_t', prefix: '#include <stddef.h>')
  cdata.set('SIZE_T', cc.sizeof('size_t', prefix: '#include <stddef.h>'))
elif cc.has_type('size_t', prefix: '#include <stdio.h>')
  cdata.set('SIZE_T', cc.sizeof('size_t', prefix: '#include <stdio.h>'))
elif cc.has_type('size_t', prefix: '#include <stdlib.h>')
  cdata.set('SIZE_T', cc.sizeof('size_t', prefix: '#include <stdlib.h>'))
elif cc.has_type('size_t', prefix: '#include <string.h>')
  cdata.set('SIZE_T', cc.sizeof('size_t', prefix: '#include <string.h>'))
elif cc.has_type('size_t', prefix: '#include <time.h>')
  cdata.set('SIZE_T', cc.sizeof('size_t', prefix: '#include <time.h>'))
elif cc.sizeof('void*') == 8
  cdata.set('size_t', 'uint64_t')
  cdata.set('SIZE_T', cc.sizeof('uint64_t', prefix: '#include <stdint.h>'))
else
  cdata.set('size_t', 'uint32_t')
  cdata.set('SIZE_T', cc.sizeof('uint32_t', prefix: '#include <stdint.h>'))
endif

if cc.has_type('ssize_t', prefix : '#include <unistd.h>')
  cdata.set('SSIZE_T', cc.sizeof('ssize_t', prefix : '#include <unistd.h>'))
elif cc.has_type('ssize_t', prefix : '#include <sys/types.h>')
  cdata.set('SSIZE_T', cc.sizeof('ssize_t', prefix : '#include <sys/types.h>'))
elif cc.sizeof('void*') == 8
  cdata.set('ssize_t', 'int64_t')
  cdata.set('SSIZE_T', cc.sizeof('int64_t', prefix: '#include <stdint.h>'))
else
  cdata.set('ssize_t', 'long')
  cdata.set('SSIZE_T', cc.sizeof('long'))
endif

if cc.has_type('pid_t', prefix : '#include <unistd.h>')
  cdata.set('PID_T', cc.sizeof('pid_t', prefix : '#include <unistd.h>'))
elif cc.has_type('pid_t', prefix : '#include <sys/types.h>')
  cdata.set('PID_T', cc.sizeof('pid_t', prefix : '#include <sys/types.h>'))
elif host_machine.system() == 'windows'
  cdata.set('pid_t', 'int')
  cdata.set('PID_T', cc.sizeof('int'))
else
  error('pid_t doesn\'t exist on this platform?')
endif

if cc.has_type('timer_t', prefix : '#include <time.h>')
  cdata.set('TIMER_T', cc.sizeof('timer_t', prefix : '#include <time.h>'))
elif cc.has_type('timer_t', prefix : '#include <sys/time.h>')
  cdata.set('TIMER_T', cc.sizeof('timer_t', prefix : '#include <sys/time.h>'))
else
  cdata.set('timer_t', 'int')
  cdata.set('TIMER_T', cc.sizeof('int'))
endif

###############################################################################
# Check libraries
int_types_check = [
  'int16_t',
  'int32_t',
  'int64_t',
  'intmax_t',

  'uint8_t',
  'uint16_t',
  'uint32_t',
  'uint64_t',
  'uintmax_t',
]

foreach type : int_types_check
  if cc.has_type(type, prefix : '#include <stdint.h>')
    type_upper = type.to_upper()
    cdata.set(type_upper, type)
    cdata.set('HAVE_@0@'.format(type_upper), true)
  endif
endforeach

int_max_min_check = [
  'INT64_MAX',
  'INT64_MIN',
  'UINT32_MAX',
  'UINT64_MAX',
  'SIZE_MAX',
  'SSIZE_MAX',
]

foreach type : int_max_min_check
  if (cc.has_header_symbol('stdint.h', type)
      or cc.has_header_symbol('limits.h', type)
      or cc.has_header_symbol('inttypes.h', type))
    cdata.set('HAVE_@0@'.format(type), true)
  endif
endforeach

if not cdata.has('HAVE_SYS_TIME_H')
  if host_machine.system() == 'windows'
    if cc.has_member('struct timeval', 'tv_sec', prefix : '#include <winsock2.h>')
      cdata.set('HAVE_STRUCT_TIMEVAL_TV_SEC', true)
    endif
    if cc.has_member('struct timeval', 'tv_usec', prefix : '#include <winsock2.h>')
      cdata.set('HAVE_STRUCT_TIMEVAL_TV_USEC', true)
    endif
    if cc.has_member('struct timespec', 'tv_sec', prefix : '#include <winsock2.h>')
      cdata.set('HAVE_WINSOCK2_H_STRUCT_TIMESPEC_TV_SEC', true)
    endif
    if cc.has_member('struct timespec', 'tv_sec', prefix : '#include <time.h>')
      cdata.set('HAVE_TIME_H_STRUCT_TIMESPEC_TV_SEC', true)
    endif
    if cc.has_member('struct itimerspec', 'it_value', prefix : '#include <winsock2.h>')
      cdata.set('HAVE_STRUCT_ITIMERSPEC_IT_VALUE', true)
    endif

    if (not cdata.has('HAVE_WINSOCK2_H_STRUCT_TIMESPEC_TV_SEC')
        and not cdata.has('HAVE_TIME_H_STRUCT_TIMESPEC_TV_SEC'))
      cdata.set('STRUCT_TIMESPEC_DEFINITION_MISSING', 1)
      add_project_arguments(
        '-DSTRUCT_TIMESPEC_DEFINITION_MISSING=1',
        language : 'c'
      )
    endif

    if not cdata.has('HAVE_STRUCT_ITIMERSPEC_IT_VALUE')
      cdata.set('STRUCT_ITIMERSPEC_DEFINITION_MISSING', 1)
      add_project_arguments(
        '-DSTRUCT_ITIMERSPEC_DEFINITION_MISSING=1',
        language : 'c'
      )
    endif
  endif
endif

###############################################################################
# Check libraries
libm = cc.find_library('m', required : false)
if libm.found() and cc.has_header_symbol('math.h', 'floor')
  cdata.set('LIBM', 'm')
  cdata.set('HAVE_LIBM', true)
endif

librt = cc.find_library('rt', required : false)
if librt.found() and cc.has_header_symbol('time.h', 'clock_gettime')
  cdata.set('LIBRT', 'rt')
  cdata.set('HAVE_LIBRT', 1)
  add_project_arguments('-DHAVE_LIBRT=1', language : 'c')
endif

libsubunit = cc.find_library('subunit', required: false)
if libsubunit.found() and cc.has_header_symbol('subunit/child.h', 'subunit_test_start')
  cdata.set('SUBUNIT', 'subunit')
  cdata.set('ENABLE_SUBUNIT', 1)
  add_project_arguments('-DENABLE_SUBUNIT=1', language : 'c')
else
  cdata.set('ENABLE_SUBUNIT', 0)
  add_project_arguments('-DENABLE_SUBUNIT=0', language : 'c')
endif

###############################################################################
# Generate "config.h" from "cmake/config.h.in"
subdir('internal')

subdir('lib')
subdir('src')

if not meson.is_subproject()
  subdir('tests')
endif
