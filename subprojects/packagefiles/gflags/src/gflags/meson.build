define_cdata = configuration_data()
define_cdata.set('OS_WINDOWS', is_windows)
define_cdata.set('HAVE_STDINT_H', cc.has_header('stdint.h').to_int())
define_cdata.set('HAVE_SYS_TYPES_H', cc.has_header('sys/types.h').to_int())
define_cdata.set('HAVE_INTTYPES_H', cc.has_header('inttypes.h').to_int())
define_cdata.set('HAVE_SYS_STAT_H', cc.has_header('sys/stat.h').to_int())
define_cdata.set('HAVE_UNISTD_H', cc.has_header('unistd.h').to_int())
define_cdata.set('HAVE_FNMATCH_H', cc.has_header('fnmatch.h').to_int())
define_cdata.set('HAVE_SHLWAPI_H', cc.has_header('shlwapi.h').to_int())
define_cdata.set('HAVE_STROLL', cc.has_function('stroll').to_int())
define_cdata.set('HAVE_STRTOQ', cc.has_function('strtoq').to_int())
define_cdata.set('HAVE_PTHREAD', cc.has_header('pthread.h').to_int())
define_cdata.set(
  'HAVE_RWLOCK',
  cc.has_function(
    'pthread_rwlock_t',
    prefix: '#include <pthread.h>',
  ).to_int(),
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
gflags_declare_data.set('GFLAGS_IS_A_DLL', gflags_is_a_dll.to_int())
gflags_declare_data.set('HAVE_STDINT_H', cc.has_header('stdint.h').to_int())
gflags_declare_data.set(
  'HAVE_SYS_TYPES_H',
  cc.has_header('sys/types.h').to_int(),
)
gflags_declare_data.set('HAVE_INTTYPES_H', cc.has_header('inttypes.h').to_int())

# gflag's CMake configuration tries to fallback to support BSD and VC7
# compilers that may not support uint32_t. To make the configuration
# simpler we are just raising when C99 types are not available
if cc.sizeof(
  'uint32_t',
  prefix: '#include <inttypes.h>',
) == -1
  error(
    'The gflags Meson config only implements support for C99 compatible compilers',
  )
endif
gflags_declare_data.set('GFLAGS_INTTYPES_FORMAT_C99', 1)
gflags_declare_data.set('GFLAGS_INTTYPES_FORMAT_BSD', 0)
gflags_declare_data.set('GFLAGS_INTTYPES_FORMAT_VC7', 0)

configure_file(
  input: '../gflags_declare.h.in',
  output: 'gflags_declare.h',
  configuration: gflags_declare_data,
  install: true,
  install_dir: 'gflags',
)

gflags_data = configuration_data()
if cc.get_argument_syntax() == 'gcc'
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
