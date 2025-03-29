# skip tests if disabled
if get_option('tests').disabled()
  subdir_done()
endif

# skip tests if boost interface was disabled
if not boost_dep.found()
  if get_option('tests').enabled()
    error('Boost interface is required for tests')
  endif
  message('Skipping tests as Boost interface is disabled')
  subdir_done()
endif

test_deps = [
  msgpack_cxx_dep,
  dependency(
    'threads',
    required: get_option('tests'),
  ),
  dependency(
    'zlib',
    required: get_option('tests'),
  ),
  dependency(
    'boost',
    modules: ['unit_test_framework', 'system'],
    required: get_option('tests'),
  ),
]

# skip tests if test dependencies not found
foreach dep : test_deps
  if not dep.found()
    message('Skipping tests as test dependency ' + dep.name() + ' not found')
    subdir_done()
  endif
endforeach

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
  'iterator_cpp11',
  'json',
  'limit',
  'msgpack_basic',
  'msgpack_container',
  'msgpack_cpp11',
  'msgpack_cpp17',
  'msgpack_cpp20',
  'msgpack_stream',
  'msgpack_tuple',
  'msgpack_vref',
  'msgpack_x3_parse',
  'object',
  'object_with_zone',
  'pack_unpack',
  'raw',
  'reference',
  'reference_cpp11',
  'reference_wrapper_cpp11',
  'shared_ptr_cpp11',
  'size_equal_only',
  'streaming',
  'unique_ptr_cpp11',
  'user_class',
  'version',
  'visitor',
  'zone',
]

foreach t : progs
  exe = executable(
    t,
    t + '.cpp',
    implicit_include_directories: false,
    dependencies: test_deps,
  )
  test(t, exe)
endforeach

exe = executable(
  'multi_file',
  'multi_file1.cpp',
  'multi_file2.cpp',
  implicit_include_directories: false,
  dependencies: msgpack_cxx_dep,
)
test('multi_file', exe)
