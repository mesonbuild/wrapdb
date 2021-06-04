project('facil', 'c',
    version : '0.7.5',
    license: 'MIT',
    default_options: ['c_std=c11']
)

cc = meson.get_compiler('c')
m_dep = cc.find_library('m', required : false)

thread_dep = dependency('threads')

facil_src = [
    'lib/facil/fio.c',
    'lib/facil/tls/fio_tls_missing.c',
    'lib/facil/tls/fio_tls_openssl.c',
    'lib/facil/fiobj/fio_siphash.c',
    'lib/facil/fiobj/fiobj_ary.c',
    'lib/facil/fiobj/fiobj_data.c',
    'lib/facil/fiobj/fiobj_hash.c',
    'lib/facil/fiobj/fiobj_json.c',
    'lib/facil/fiobj/fiobj_mustache.c',
    'lib/facil/fiobj/fiobj_numbers.c',
    'lib/facil/fiobj/fiobj_str.c',
    'lib/facil/fiobj/fiobject.c',
    'lib/facil/cli/fio_cli.c',
    'lib/facil/http/http.c',
    'lib/facil/http/http1.c',
    'lib/facil/http/http_internal.c',
    'lib/facil/http/websockets.c',
    'lib/facil/redis/redis_engine.c'
]

facil_inc = [
    'lib',
    'lib/facil',
    'lib/facil/tls',
    'lib/facil/fiobj',
    'lib/facil/cli',
    'lib/facil/http',
    'lib/facil/http/parsers',
    'lib/facil/redis'
]

facil_lib = library('facil',
    sources: facil_src,
    include_directories: facil_inc,
    dependencies: [m_dep, thread_dep]
)

facil_dep = declare_dependency(
    include_directories : facil_inc,
    link_with : facil_lib
)
