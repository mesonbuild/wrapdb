project('jansson', 'c', version : '2.14', license : 'MIT')

cc = meson.get_compiler('c')
pdata = configuration_data()
check_headers = [
  'endian.h',
  'fcntl.h',
  'locale.h',
  'sched.h',
  'sys/param.h',
  'sys/stat.h',
  'sys/time.h',
  'sys/types.h',
  'unistd.h',
]

foreach h : check_headers
  pdata.set('HAVE_@0@'.format(h.underscorify().to_upper()), cc.has_header(h))
endforeach

pdata.set10('HAVE_STDINT_H', cc.has_header('stdint.h'))

foreach f : [ 'close', 'getpid', 'gettimeofday', 'open', 'read', 'sched_yield', 'setlocale', 'strtoll' ]
  pdata.set('HAVE_@0@'.format(f.underscorify().to_upper()), cc.has_function(f))
endforeach

foreach t : [ 'int32', 'uint32', 'uint16', 'uint8' ]
  pdata.set('HAVE_@0@_T'.format(t.underscorify().to_upper()), cc.has_type(t + '_t', prefix: '#include <stdint.h>'))
endforeach

pdata.set('HAVE_SSIZE_T', cc.has_type('ssize_t', prefix: '#include <sys/types.h>'))

pdata.set('JANSSON_INITIAL_HASHTABLE_ORDER', 3)
pdata.set('JSON_INT32', 'int32_t')
pdata.set('JSON_UINT32', 'uint32_t')
pdata.set('JSON_UINT16', 'uint16_t')
pdata.set('JSON_UINT8', 'uint8_t')
pdata.set('JSON_SSIZE', 'long')

pdata.set('USE_URANDOM', host_machine.system() != 'windows')
pdata.set('USE_WINDOWS_CRYPTOAPI', host_machine.system() == 'windows')

cdata = configuration_data()

foreach h : [ 'stdint.h', 'inttypes.h', 'sys/types.h' ]
  cdata.set('HAVE_@0@'.format(h.underscorify().to_upper()), cc.has_header(h))
endforeach

foreach f : ['inline', '__inline', '']
  if cc.compiles(f + ' void func() {}')
    cdata.set('JSON_INLINE', f)
    break
  endif
endforeach

cdata.set('JSON_INT_T', 'int64_t')
cdata.set('JSON_STRTOINT', 'strtoll')
if cc.sizeof('long') == 4
cdata.set_quoted('JSON_INTEGER_FORMAT', 'lld')
else
cdata.set_quoted('JSON_INTEGER_FORMAT', 'ld')
endif

# FIXME: These variables set features to be explicitly disabled. The tests for
# these are missing from the check_functions block above and are also prefixed
# by 'json_'. Also these are used by an extra 'src/jansson_config.h.in' file.
# This means we may miss out on some platform specific performance improvemnts.
cdata.set('var', 'var') # avoid warning; bogus variable found in comment.
cdata.set('JSON_HAVE_LOCALECONV', 0)
cdata.set('JSON_HAVE_ATOMIC_BUILTINS', 0)
cdata.set('JSON_HAVE_SYNC_BUILTINS', 0)

configure_file(
  input: 'cmake/jansson_private_config.h.cmake',
  output: 'jansson_private_config.h',
  format: 'cmake@',
  configuration: pdata,
)

configure_file(
  input: 'cmake/jansson_config.h.cmake',
  output: 'jansson_config.h',
  format: 'cmake@',
  configuration: cdata,
  install: true,
  install_dir: get_option('includedir'),
  install_tag: 'devel'
)

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
  'src/version.c',
  c_args : '-DHAVE_CONFIG_H',
  vs_module_defs : 'src/jansson.def',
  install : true
)

install_headers('src/jansson.h')

pkg = import('pkgconfig')

pkg.generate(
  jansson_lib,
  name: 'jansson',
  description: 'Library for encoding, decoding and manipulating JSON data'
)

jansson_dep = declare_dependency(
  link_with : jansson_lib,
  include_directories : [include_directories('src'), include_directories('.')]
)
