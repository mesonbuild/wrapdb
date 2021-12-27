cdata = configuration_data()

check_headers = [
  'bits/type/traits.h',
  'bzlib.h',
  'dirent.h',
  'dlfcn.h',
  'editline/readline.h',
  'edit/readline/readline.h',
  'inttypes.h',
  'limits.h',
  'memory.h',
  'readline/history.h',
  'readline/readline.h',
  'stdint.h',
  'stdlib.h',
  'strings.h',
  'string.h',
  'sys/stat.h',
  'sys/types.h',
  'type/traits.h',
  'unistd.h',
  'windows.h',
  'zlib.h',
]

foreach h : check_headers
  if cc.has_header(h)
    cdata.set('HAVE_' + h.underscorify().to_upper(), 1)
  endif
endforeach

check_functions = [
  ['HAVE_BCOPY', 'bcopy', '#include<strings.h>'],
# check token HAVE_LONG_LONG
  ['HAVE_MEMMOVE', 'memmove', '#include<string.h>'],
# check token HAVE_PTHREAD
# check token HAVE_PTHREAD_PRIO_INHERIT
  ['HAVE_STRERROR', 'strerror', '#include<string.h>'],
# check token HAVE_STRING
  ['HAVE_STRTOIMAX', 'strtoimax', '#include<inttypes.h>'],
  ['HAVE_STRTOLL', 'strtoll', '#include<stdlib.h>'],
  ['HAVE_STRTOQ', 'strtoq', '#include<stdlib.h>'],
# check token HAVE_UNSIGNED_LONG_LONG
# check token HAVE_VISIBILITY
# check token HAVE__STRTOI64
]

foreach f : check_functions
  if cc.has_function(f.get(1), prefix : f.get(2))
    cdata.set(f.get(0), 1)
  endif
endforeach

if get_option('shared_lib')
  libtype = 'shared_library'
else
  libtype = 'static_library'
  cdata.set('PCRE_STATIC', 1)
endif

cdata.set('SUPPORT_PCRE8', 1)
cdata.set('LINK_SIZE', 2)
cdata.set('MATCH_LIMIT', 1000000)
cdata.set('MATCH_LIMIT_RECURSION', 1000000)
cdata.set('MAX_NAME_COUNT', 10000)
cdata.set('MAX_NAME_SIZE', 32)
cdata.set('PARENS_NEST_LIMIT', 100)
cdata.set('NEWLINE', 10) # Currently unix only.
cdata.set('POSIX_MALLOC_THRESHOLD', 100)
cdata.set('SUPPORT_UCP', 1)
cdata.set('SUPPORT_UTF', 1)

configure_file(input : 'config.h.meson',
  output : 'config.h',
  configuration : cdata)
