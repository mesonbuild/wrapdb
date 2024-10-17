project(
  'hwy',
  'cpp',
  version: '1.2.0',
  meson_version: '>= 1.3.0',
  license: 'Apache-2.0 OR BSD-3-Clause',
)

hwy_sources = files(
    'hwy/abort.cc',
    'hwy/aligned_allocator.cc',
    'hwy/nanobenchmark.cc',
    'hwy/per_target.cc',
    'hwy/print.cc',
    'hwy/targets.cc',
    'hwy/timer.cc',
)

if host_machine.system() == 'windows'
  add_project_arguments('-DNOMINMAX', language: 'cpp')
endif

hwy_lib = library(
    'hwy',
    hwy_sources,
    cpp_static_args: ['-DHWY_STATIC_DEFINE'],
    cpp_shared_args: ['-DHWY_SHARED_DEFINE', '-Dhwy_EXPORTS'],
    gnu_symbol_visibility: 'hidden',
)

inc = include_directories('.')

hwy_dep = declare_dependency(
    link_with: hwy_lib,
    include_directories: inc,
)
meson.override_dependency('hwy', hwy_dep)

if not get_option('tests').disabled()
  hwy_test_sources = [
      'hwy/tests/test_util.cc',
  ]

  hwy_test_lib = library(
      'hwy-test',
      hwy_test_sources,
      cpp_static_args: ['-DHWY_STATIC_DEFINE'],
      cpp_shared_args: ['-DHWY_SHARED_DEFINE', '-Dhwy_test_EXPORTS'],
      dependencies: [hwy_dep],
      gnu_symbol_visibility: 'hidden',
  )

  hwy_tests = [
    'hwy/contrib/algo/copy_test.cc',
    'hwy/contrib/algo/find_test.cc',
    'hwy/contrib/algo/transform_test.cc',
    'hwy/abort_test.cc',
    'hwy/aligned_allocator_test.cc',
    'hwy/base_test.cc',
    'hwy/bit_set_test.cc',
    'hwy/highway_test.cc',
    'hwy/nanobenchmark_test.cc',
    'hwy/targets_test.cc',
    'hwy/examples/skeleton_test.cc',
    'hwy/tests/arithmetic_test.cc',
    'hwy/tests/bit_permute_test.cc',
    'hwy/tests/blockwise_shift_test.cc',
    'hwy/tests/blockwise_test.cc',
    'hwy/tests/cast_test.cc',
    'hwy/tests/combine_test.cc',
    'hwy/tests/compare_test.cc',
    'hwy/tests/compress_test.cc',
    'hwy/tests/convert_test.cc',
    'hwy/tests/count_test.cc',
    'hwy/tests/crypto_test.cc',
    'hwy/tests/demote_test.cc',
    'hwy/tests/div_test.cc',
    'hwy/tests/dup128_vec_test.cc',
    'hwy/tests/expand_test.cc',
    'hwy/tests/float_test.cc',
    'hwy/tests/foreach_vec_test.cc',
    'hwy/tests/if_test.cc',
    'hwy/tests/in_range_float_to_int_conv_test.cc',
    'hwy/tests/interleaved_test.cc',
    'hwy/tests/logical_test.cc',
    'hwy/tests/mask_combine_test.cc',
    'hwy/tests/mask_convert_test.cc',
    'hwy/tests/mask_mem_test.cc',
    'hwy/tests/mask_slide_test.cc',
    'hwy/tests/mask_test.cc',
    'hwy/tests/masked_arithmetic_test.cc',
    'hwy/tests/masked_minmax_test.cc',
    'hwy/tests/memory_test.cc',
    'hwy/tests/minmax_test.cc',
    'hwy/tests/mul_test.cc',
    'hwy/tests/reduction_test.cc',
    'hwy/tests/resize_test.cc',
    'hwy/tests/reverse_test.cc',
    'hwy/tests/saturated_test.cc',
    'hwy/tests/shift_test.cc',
    'hwy/tests/shuffle4_test.cc',
    'hwy/tests/slide_up_down_test.cc',
    'hwy/tests/sums_abs_diff_test.cc',
    'hwy/tests/swizzle_block_test.cc',
    'hwy/tests/swizzle_test.cc',
    'hwy/tests/table_test.cc',
    'hwy/tests/test_util_test.cc',
    'hwy/tests/truncate_test.cc',
    'hwy/tests/tuple_test.cc',
    'hwy/tests/widen_mul_test.cc',
  ]

  benchmarks_no_main = [
    'hwy/contrib/algo/copy_test.cc',
    'hwy/contrib/algo/find_test.cc',
    'hwy/contrib/algo/transform_test.cc',
    'hwy/abort_test.cc',
    'hwy/aligned_allocator_test.cc',
    'hwy/base_test.cc',
    'hwy/bit_set_test.cc',
    'hwy/highway_test.cc',
    'hwy/tests/bit_permute_test.cc',
    'hwy/nanobenchmark_test.cc',
    'hwy/targets_test.cc',
    'hwy/examples/skeleton_test.cc',
    'hwy/tests/arithmetic_test.cc',
    'hwy/tests/blockwise_shift_test.cc',
  ]

  fs = import('fs')

  cpp = meson.get_compiler('cpp')
  if cpp.get_id() == 'msvc'
    gtest_dep = dependency('gtest')
  else
    gtest_dep = dependency('gtest_main')
  endif

  foreach t : hwy_tests
    stem = fs.stem(t)
    sources = hwy_test_sources + t
    if stem == 'skeleton_test'
      sources += 'hwy/examples/skeleton.cc'
    endif

    cpp_args = []
    if stem in ['cast_test', 'mask_test', 'shuffle4_test']
      cpp_args += cpp.get_supported_arguments(['-Wa,-mbig-obj'])
    endif

    test(stem,
      executable(stem, sources,
        link_with: [hwy_test_lib],
        dependencies: [hwy_dep, gtest_dep],
        cpp_args: cpp_args,
      )
    )
  endforeach
endif
