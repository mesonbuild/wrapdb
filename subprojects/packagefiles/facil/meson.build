project(
  'facil',
  'c',
  version: '0.7.6',
  license: 'MIT',
  default_options: 'c_std=c11',
  meson_version: '>=0.49.0',
)

cc = meson.get_compiler('c')

if cc.get_argument_syntax() == 'msvc'
  error('MSVC is unsupported. Only MinGW')
endif

m_dep = cc.find_library('m', required: false)
thread_dep = dependency('threads')
ws_dep = cc.find_library('ws2_32', required: host_machine.system() == 'windows')

if host_machine.system() == 'windows'
  add_project_arguments('-D_WIN32_WINNT=0x0600', language: 'c')
elif host_machine.system() == 'linux'
  add_project_arguments('-D_LARGEFILE64_SOURCE', language: 'c')
endif

facil_src = files(
  'lib/facil/cli/fio_cli.c',
  'lib/facil/fio.c',
  'lib/facil/fiobj/fio_siphash.c',
  'lib/facil/fiobj/fiobj_ary.c',
  'lib/facil/fiobj/fiobj_data.c',
  'lib/facil/fiobj/fiobj_hash.c',
  'lib/facil/fiobj/fiobj_json.c',
  'lib/facil/fiobj/fiobj_mustache.c',
  'lib/facil/fiobj/fiobj_numbers.c',
  'lib/facil/fiobj/fiobj_str.c',
  'lib/facil/fiobj/fiobject.c',
  'lib/facil/http/http.c',
  'lib/facil/http/http1.c',
  'lib/facil/http/http_internal.c',
  'lib/facil/http/websockets.c',
  'lib/facil/redis/redis_engine.c',
  'lib/facil/tls/fio_tls_missing.c',
  'lib/facil/tls/fio_tls_openssl.c',
)

facil_inc = include_directories(
  'lib',
  'lib/facil',
  'lib/facil/tls',
  'lib/facil/fiobj',
  'lib/facil/cli',
  'lib/facil/http',
  'lib/facil/http/parsers',
  'lib/facil/redis',
)

facil_lib = library(
  'facil',
  sources: facil_src,
  include_directories: facil_inc,
  dependencies: [m_dep, thread_dep, ws_dep],
)

facil_dep = declare_dependency(
  include_directories: facil_inc,
  link_with: facil_lib,
)
