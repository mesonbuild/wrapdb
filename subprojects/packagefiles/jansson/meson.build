project('jansson', 'c', version : '2.11', license : 'MIT')

cc = meson.get_compiler('c')
cdata = configuration_data()
check_headers = [
  'dlfcn.h',
  'endian.h',
  'fcntl.h',
  'inttypes.h',
  'locale.h',
  'memory.h',
  'sched.h',
  'stdint.h',
  'stdlib.h',
  'strings.h',
  'string.h',
  'sys/param.h',
  'sys/stat.h',
  'sys/time.h',
  'sys/types.h',
  'unistd.h',
]

foreach h : check_headers
  if cc.has_header(h)
    cdata.set('HAVE_' + h.underscorify().to_upper(), 1)
  endif
endforeach

check_functions = [
# check token ('HAVE_ATOMIC_BUILTINS',)
# check token ('HAVE_CLOSE',)
  ['HAVE_GETPID', 'getpid', '#include<unistd.h>'],
  ['HAVE_GETTIMEOFDAY', 'gettimeofday', '#include<sys/time.h>'],
# check token ('HAVE_LOCALECONV',)
# check token ('HAVE_LONG_LONG_INT',)
# check token ('HAVE_OPEN',)
# check token ('HAVE_READ',)
# check token ('HAVE_SCHED_YIELD',)
  ['HAVE_STRTOLL', 'strtoll', '#include<stdlib.h>'],
# check token ('HAVE_SYNC_BUILTINS',)
# check token ('HAVE_UNSIGNED_LONG_LONG_INT',)
]

foreach f : check_functions
  if cc.has_function(f.get(1), prefix : f.get(2))
    cdata.set(f.get(0), 1)
  endif
endforeach

foreach f : ['inline', '__inline', '']
  if cc.compiles(f + ' void func() {}')
    cdata.set('json_inline', f)
    break
  endif
endforeach

if cc.sizeof('long long int') > 0
  cdata.set('json_have_long_long', 1)
  cdata.set('HAVE_LONG_LONG_INT', 1)
else
  cdata.set('json_have_long_long', 0)
endif

# FIXME: These variables set features to be explicitly disabled. The tests for
# these are missing from the check_functions block above and are also prefixed
# by 'json_'. Also these are used by an extra 'src/jansson_config.h.in' file.
# This means we may miss out on some platform specific performance improvemnts.
cdata.set('var', 'var') # avoid warning; bogus variable found in comment.
cdata.set('json_have_localeconv', 0)
cdata.set('json_have_atomic_builtins', 0)
cdata.set('json_have_sync_builtins', 0)

configure_file(input : 'config.h.meson',
  output : 'jansson_private_config.h',
  configuration : cdata)

configure_file(input : 'src/jansson_config.h.in',
  output : 'jansson_config.h',
  configuration : cdata)

jansson_lib = library('jansson',
  'src/dump.c',
  'src/error.c',
  'src/hashtable.c',
  'src/hashtable_seed.c',
  'src/load.c',
  'src/memory.c',
  'src/pack_unpack.c',
  'src/strbuffer.c',
  'src/strconv.c',
  'src/utf.c',
  'src/value.c',
  c_args : '-DHAVE_CONFIG_H'
)

jansson_dep = declare_dependency(
  link_with : jansson_lib,
  include_directories : [include_directories('src'), include_directories('.')]
)
