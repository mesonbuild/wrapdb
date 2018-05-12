cdata = configuration_data()

check_headers = [
  ['HAVE_BITS_TYPE_TRAITS_H', 'bits/type/traits.h'],
  ['HAVE_BZLIB_H', 'bzlib.h'],
  ['HAVE_DIRENT_H', 'dirent.h'],
  ['HAVE_DLFCN_H', 'dlfcn.h'],
  ['HAVE_EDITLINE_READLINE_H', 'editline/readline.h'],
  ['HAVE_EDIT_READLINE_READLINE_H', 'edit/readline/readline.h'],
  ['HAVE_INTTYPES_H', 'inttypes.h'],
  ['HAVE_LIMITS_H', 'limits.h'],
  ['HAVE_MEMORY_H', 'memory.h'],
  ['HAVE_READLINE_HISTORY_H', 'readline/history.h'],
  ['HAVE_READLINE_READLINE_H', 'readline/readline.h'],
  ['HAVE_STDINT_H', 'stdint.h'],
  ['HAVE_STDLIB_H', 'stdlib.h'],
  ['HAVE_STRINGS_H', 'strings.h'],
  ['HAVE_STRING_H', 'string.h'],
  ['HAVE_SYS_STAT_H', 'sys/stat.h'],
  ['HAVE_SYS_TYPES_H', 'sys/types.h'],
  ['HAVE_TYPE_TRAITS_H', 'type/traits.h'],
  ['HAVE_UNISTD_H', 'unistd.h'],
  ['HAVE_WINDOWS_H', 'windows.h'],
  ['HAVE_ZLIB_H', 'zlib.h'],
]

foreach h : check_headers
  if cc.has_header(h.get(1))
    cdata.set(h.get(0), 1)
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

configure_file(input : 'config.h.meson',
  output : 'config.h',
  configuration : cdata)

