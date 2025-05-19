define_cdata = configuration_data()
define_cdata.set('OS_WINDOWS', is_windows)
define_cdata.set10('HAVE_STDINT_H', cc.has_header('stdint.h'))
define_cdata.set10('HAVE_SYS_TYPES_H', cc.has_header('sys/types.h'))
define_cdata.set10('HAVE_INTTYPES_H', cc.has_header('inttypes.h'))
define_cdata.set10('HAVE_SYS_STAT_H', cc.has_header('sys/stat.h'))
define_cdata.set10('HAVE_UNISTD_H', cc.has_header('unistd.h'))
define_cdata.set10('HAVE_FNMATCH_H', cc.has_header('fnmatch.h'))
define_cdata.set10('HAVE_SHLWAPI_H', cc.has_header('shlwapi.h'))
define_cdata.set10('HAVE_STRTOLL', cc.has_function('strtoll'))
define_cdata.set10('HAVE_STRTOQ', cc.has_function('strtoq'))
define_cdata.set10('HAVE_PTHREAD', cc.has_header('pthread.h'))
define_cdata.set10(
  'HAVE_RWLOCK',
  cc.has_type(
    'pthread_rwlock_t',
    prefix: '#include <pthread.h>',
  ),
)

configure_file(
  input: '../defines.h.in',
  output: 'defines.h',
  format: 'cmake',
  configuration: define_cdata,
  install: true,
  install_dir: 'gflags',
)

gflags_completions_data = configuration_data()
gflags_completions_data.set('GFLAGS_NAMESPACE', 'gflags')

configure_file(
  input: '../gflags_completions.h.in',
  output: 'gflags_completions.h',
  configuration: gflags_completions_data,
  install: true,
  install_dir: 'gflags',
)

gflags_declare_data = configuration_data()
gflags_declare_data.set('GFLAGS_NAMESPACE', 'gflags')
gflags_declare_data.set10('GFLAGS_IS_A_DLL', gflags_is_a_dll)
gflags_declare_data.set10('HAVE_STDINT_H', true)
gflags_declare_data.set10('HAVE_SYS_TYPES_H', cc.has_header('sys/types.h'))
gflags_declare_data.set10('HAVE_INTTYPES_H', true)
gflags_declare_data.set10('GFLAGS_INTTYPES_FORMAT_C99', true)
gflags_declare_data.set10('GFLAGS_INTTYPES_FORMAT_BSD', false)
gflags_declare_data.set10('GFLAGS_INTTYPES_FORMAT_VC7', false)

configure_file(
  input: '../gflags_declare.h.in',
  output: 'gflags_declare.h',
  configuration: gflags_declare_data,
  install: true,
  install_dir: 'gflags',
)

gflags_data = configuration_data()
if cc.has_function_attribute('unused')
  gflags_data.set('GFLAGS_ATTRIBUTE_UNUSED', '__attribute((unused))')
else
  gflags_data.set('GFLAGS_ATTRIBUTE_UNUSED', '')
endif
gflags_data.set('INCLUDE_GFLAGS_NS_H', '')
configure_file(
  input: '../gflags.h.in',
  output: 'gflags.h',
  configuration: gflags_data,
  install: true,
  install_dir: 'gflags',
)

gflags_ns_data = configuration_data()
gflags_ns_data.set('NS', 'gflags')
gflags_ns_data.set('ns', 'gflags')
configure_file(
  input: '../gflags_ns.h.in',
  output: 'gflags_ns.h',
  configuration: gflags_ns_data,
  install: true,
  install_dir: 'gflags',
)
