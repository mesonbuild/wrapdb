conf = configuration_data()
if get_option('rdrand')
  conf.set('ENABLE_RDRAND', 1)
endif

check_headers = [
  'dlfcn.h',
  'endian.h',
  'fcntl.h',
  'inttypes.h',
  'limits.h',
  'locale.h',
  'memory.h',
  'stdarg.h',
  'stdint.h',
  'stdlib.h',
  'string.h',
  'strings.h',
  'syslog.h',
  'sys/cdefs.h',
  'sys/param.h',
  'sys/random.h',
  'sys/resource.h',
  'sys/stat.h',
  'sys/types.h',
  'unistd.h',
  'xlocale.h',
]

foreach header : check_headers
  if cc.has_header(header)
    conf.set('HAVE_@0@'.format(header.underscorify().to_upper()), 1)
  endif
endforeach

have_stdc = true
foreach header : ['stdlib.h', 'stdarg.h', 'string.h', 'float.h']
  if not conf.has('HAVE_@0@'.format(header.underscorify().to_upper()))
    have_stdc = false
  endif
endforeach
conf.set10('STDC_HEADERS', have_stdc)

foreach symbol : ['_isnan', '_finite']
  if cc.has_header_symbol('float.h', symbol)
    conf.set('HAVE_DECL_@0@'.format(symbol.to_upper()), 1)
  endif
endforeach

foreach symbol : ['INFINITY', 'isinf', 'isnan', 'nan']
  if cc.has_header_symbol('math.h', symbol)
    conf.set('HAVE_DECL_@0@'.format(symbol.to_upper()), 1)
  endif
endforeach

check_function = [
  'vasprintf',
  'realloc',
  'setlocale',
  'uselocale',
  'strcasecmp',
  'strdup',
  'strerror',
  'vsyslog',
  'open',
  'strtoll',
  'arc4random',
]

if conf.has('HAVE_STRINGS_H')
  check_function += 'strncasecmp'
endif

foreach function : check_function
  if cc.has_function(function)
    conf.set('HAVE_@0@'.format(function.to_upper()), 1)
  endif
endforeach
conf.set10('HAVE_DOPRNT', cc.has_function('_doprnt'))

foreach f : ['snprintf', 'vsnprintf', 'vprintf']
  if cc.has_header_symbol('stdio.h', f)
    conf.set('HAVE_@0@'.format(f.to_upper()), 1)
  endif
endforeach

size = cc.sizeof(
  'size_t',
  prefix: '#include <stddef.h>',
)
conf.set('SIZEOF_SIZE_T', size)

if cc.get_argument_syntax() == 'msvc'
  size = cc.sizeof(
    'SSIZE_T',
    prefix: '#include <BaseTsd.h>',
  )
else
  size = cc.sizeof(
    'ssize_t',
    prefix: '#include <sys/types.h>',
  )
endif
conf.set('SIZEOF_SSIZE_T', size)

foreach type : ['int', 'int64_t', 'long', 'long long']
  size = cc.sizeof(
    type,
    prefix: '#include <stdint.h>',
  )
  conf.set('SIZEOF_@0@'.format(type.underscorify().to_upper()), size)
endforeach

if cc.links(
  'int main(){__sync_synchronize();}',
  name: 'atomic builtins',
)
  conf.set('HAVE_ATOMIC_BUILTINS', 1)
  conf.set('ENABLE_THREADING', 1)
endif

if cc.compiles(
  'static __thread int x = 0;',
  name: '__thread',
)
  conf.set('HAVE___THREAD', 1)
endif

if conf.has('HAVE___THREAD')
  conf.set('SPEC___THREAD', '__thread')
elif cc.get_argument_syntax() == 'msvc'
  conf.set('SPEC___THREAD', '__declspec(thread)')
endif

conf.set_quoted('VERSION', meson.project_version())

config_h = configure_file(
  configuration: conf,
  output: 'config.h',
)
