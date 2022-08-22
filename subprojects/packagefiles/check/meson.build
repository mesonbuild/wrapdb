project('check', 'c',
  default_options : ['warning_level=0', 'default_library=static'],
  version : '0.15.2',
  license : 'LGPL2.1',
)

check_version = meson.project_version()
cdata = configuration_data({
  'CHECK_MAJOR_VERSION' : check_version.split('.')[0],
  'CHECK_MINOR_VERSION' : check_version.split('.')[1],
  'CHECK_MICRO_VERSION' : check_version.split('.')[2],
})

cc = meson.get_compiler('c')
cdata.set10('HAVE_PTHREAD', cc.has_header('pthread.h'))

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
# 'sys/time.h',
  'sys/types.h',
  'sys/wait.h',
  'time.h',
  'unistd.h',
  'varargs.h',
]

foreach h : check_headers
  cdata.set10('HAVE_@0@'.format(h.underscorify().to_upper()), cc.has_header(h))
endforeach

###############################################################################
check_functions = [
  'clock_gettime',
  'fork',
  'getline',
  'getpid',
  'gettimeofday',
  'malloc',
  'mkstemp',
  'realloc',
  'regcomp',
  'regexec',
  'sigaction',
  'snprintf',
  'vasprintf',
  'va-copy',
  'vsnprintf',
]

foreach f : check_functions
  cdata.set10('HAVE_@0@'.format(f.underscorify().to_upper()), cc.has_function(f))
endforeach

foreach d : [ 'alarm', 'localtime_r', 'setenv', 'strdup', 'strsignal']
  cdata.set10('HAVE_DECL_@0@'.format(d.underscorify().to_upper()), cc.has_function(d))
endforeach

###############################################################################
# Check for integer types

foreach t : [ 'short', 'int', 'long', 'long long', 'unsigned short', 'unsigned', 'unsigned long', 'unsigned long long' ]
  u = t.underscorify().to_upper()
  cdata.set('SIZE_OF_@0@_CODE'.format(u), '#define SIZE_OF_@0@ @1@'.format(u, cc.sizeof(t)))
endforeach

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
endif

if not cc.has_type('clockid_t', prefix : '#include <time.h>')
  cdata.set('clockid_t', 'int')
endif

if not cc.has_type('timer_t', prefix : '#include <time.h>\n#include <sys/time.h>')
  cdata.set('timer_t', 'int')
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
else
  if not cc.has_member('struct itimerspec', 'it_value', prefix : '#include <sys/time.h>')
      add_project_arguments(
        '-DSTRUCT_ITIMERSPEC_DEFINITION_MISSING=1',
        language : 'c'
      )
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
configure_file(input: 'cmake/config.h.in',
  output: 'config.h',
  format: 'cmake@',
  configuration: cdata,
)

confinc = include_directories('.')

subdir('lib')
subdir('src')

if not meson.is_subproject()
  subdir('tests')
endif
