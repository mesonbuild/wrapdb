project(
  'Crow',
  'cpp',
  version: '1.3.0',
  license: 'BSD-3-Clause',
  meson_version: '>=0.54.0',
)

# equvalent to add_warnings_optimizations macro in compiler_options.cmake
crow_private_options = ['cpp_std=c++17', 'warning_level=3', 'werror=false']
crow_private_args = meson.get_compiler('cpp').get_supported_arguments(
  '-Wsuggest-override',
  '-Wshadow',
  '/bigobj',
  '-Wa,-mbig-obj',
  '/permissive-',
  get_option('debug') ? ['/Ob0', '/RTC1'] : [],
)

crow_public_args = []
crow_deps = []

if get_option('return_ok_on_http_options')
  crow_public_args += 'CROW_RETURNS_OK_ON_HTTP_OPTIONS_REQUEST'
endif

boost_dep = dependency(
  'boost',
  modules: ['date_time'],
  required: get_option('boost'),
)
if boost_dep.found()
  crow_deps += boost_dep
  crow_public_args += '-DCROW_USE_BOOST'
  summary('asio', 'Boost.Asio')
else
  asio_dep = dependency(
    'asio',
    required: true,
  )
  crow_deps += asio_dep
  crow_public_args += '-DASIO_NO_DEPRECATED'
  summary('asio', 'Standalone Asio')
endif

if host_machine.system() == 'windows' and meson.get_compiler('cpp').get_argument_syntax() != 'msvc'
  # actually this is a dependency of asio and boost.asio rather than crow specific.
  crow_deps += [
    meson.get_compiler('cpp').find_library('ws2_32'),
    meson.get_compiler('cpp').find_library('mswsock'),
  ]
endif

openssl_dep = dependency(
  'openssl',
  required: get_option('ssl'),
)
if openssl_dep.found()
  crow_deps += openssl_dep
  crow_public_args += '-DCROW_ENABLE_SSL'
endif
summary(
  'ssl',
  openssl_dep.found(),
  bool_yn: true,
)

zlib_dep = dependency(
  'zlib',
  required: get_option('compression'),
)
if zlib_dep.found()
  crow_deps += zlib_dep
  crow_public_args += '-DCROW_ENABLE_COMPRESSION'
endif
summary(
  'compression',
  zlib_dep.found(),
  bool_yn: true,
)

crow_inc = include_directories('include')

crow_dep = declare_dependency(
  include_directories: crow_inc,
  dependencies: crow_deps,
  compile_args: crow_public_args,
)
meson.override_dependency('Crow', crow_dep)

subdir('examples')
subdir('tests')
