test_deps = [
    msgpackc_cxx_dep,
    dependency('threads'),
    dependency('zlib'),
    dependency('boost', modules: ['unit_test_framework', 'system'])
]

progs = [
    'array_ref',
    'boost_fusion',
    'boost_optional',
    'boost_string_ref',
    'boost_string_view',
    'boost_variant',
    'buffer',
    'carray',
    'cases',
    'convert',
    'fixint',
    'inc_adaptor_define',
    'json',
    'limit',
    'msgpack_basic',
    'msgpack_container',
    'msgpack_stream',
    'msgpack_tuple',
    'msgpack_vref',
    'object',
    'object_with_zone',
    'pack_unpack',
    'raw',
    'reference',
    'size_equal_only',
    'streaming',
    'user_class',
    'version',
    'visitor',
    'zone',
]
if get_option('x3_parse')
    progs += ['msgpack_x3_parse']
endif

foreach t: progs
    exe = executable(
        t, t+'.cpp',
        implicit_include_directories: false,
        dependencies: test_deps
    )
    test(t, exe)
endforeach

exe = executable(
    'multi_file',
    'multi_file1.cpp', 'multi_file2.cpp',
    implicit_include_directories: false,
    dependencies: msgpackc_cxx_dep
)
test('multi_file', exe)
