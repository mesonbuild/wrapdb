project(
  'msgpack-cxx',
  'cpp',
  version: '7.0.0',
  meson_version: '>=0.48.0',
)

args = []

boost_dep = dependency(
  'boost',
  required: get_option('boost'),
)
if not boost_dep.found()
  message('Disabling Boost interface, some features might not be available')
  args += ['-DMSGPACK_NO_BOOST']
endif

if get_option('x3_parse')
  if not boost_dep.found()
    error('Boost is required for X3 parse')
  endif
  args += ['-DMSGPACK_USE_X3_PARSE']
endif

if get_option('std_variant')
  args += ['-DMSGPACK_USE_STD_VARIANT_ADAPTOR']
endif

if host_machine.cpu_family() == 'sparc'
  args += ['-DMSGPACK_ZONE_ALIGN=8']
endif

msgpack_cxx_dep = declare_dependency(
  compile_args: args,
  include_directories: include_directories('include'),
  dependencies: boost_dep,
)

install_headers('include/msgpack.hpp')
install_subdir(
  'include/msgpack',
  install_dir: get_option('includedir'),
)

subdir('test')
