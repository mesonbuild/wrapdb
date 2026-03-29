# bx tests — unit tests + benchmarks
# cmake: cmake/bx/CMakeLists.txt

bx_test_src = files(
  'allocator_test.cpp',
  'atomic_test.cpp',
  'cast_test.cpp',
  'crt_test.cpp',
  'easing_test.cpp',
  'filepath_test.cpp',
  'handle_test.cpp',
  'hash_test.cpp',
  'macros_test.cpp',
  'main_test.cpp',
  'math_test.cpp',
  'os_test.cpp',
  'pixelformat_test.cpp',
  'queue_test.cpp',
  'readerwriter_test.cpp',
  'ringbuffer_test.cpp',
  'rng_test.cpp',
  'run_test.cpp',
  'settings_test.cpp',
  'simd_test.cpp',
  'sort_test.cpp',
  'string_test.cpp',
  'thread_test.cpp',
  'tokenizecmd_test.cpp',
  'typetraits_test.cpp',
  'uint32_test.cpp',
  'unordered_map_nonpod_test.cpp',
  'unordered_map_test.cpp',
  'unordered_set_copyctor_test.cpp',
  'unordered_set_pod_test.cpp',
  'unordered_set_test.cpp',
  'url_test.cpp',
  'vector_complex_test.cpp',
  'vector_header_test.cpp',
  'vector_nocopy_test.cpp',
  'vector_nodefault_test.cpp',
  'vector_primitive_test.cpp',
  'vector_shrinktofit_test.cpp',
  'vsnprintf_test.cpp',
)

bx_catch_src = files('../3rdparty/catch/catch_amalgamated.cpp')

bx_test_inc = include_directories('.', '../3rdparty')

bx_test = executable('bx_test',
  bx_test_src,
  bx_catch_src,
  include_directories: bx_test_inc,
  dependencies: bx_dep,
  cpp_args: '-DCATCH_AMALGAMATED_CUSTOM_MAIN',
)

test('bx.test', bx_test)

# bx benchmarks
bx_bench_src = files(
  'handle_bench.cpp',
  'math_bench.cpp',
  'simd_bench.cpp',
)

bx_bench = executable('bx_bench',
  bx_bench_src,
  bx_catch_src,
  include_directories: bx_test_inc,
  dependencies: bx_dep,
)

test('bx.bench', bx_bench)
