# Build definition for https://github.com/RoaringBitmap/CRoaring
project(
  'croaring',
  'c',
  'cpp',
  version: '1.3.0',
  license: 'MIT',
)

croaring_sources = files(
  'src/array_util.c',
  'src/bitset.c',
  'src/bitset_util.c',
  'src/containers/array.c',
  'src/containers/bitset.c',
  'src/containers/containers.c',
  'src/containers/convert.c',
  'src/containers/mixed_andnot.c',
  'src/containers/mixed_equal.c',
  'src/containers/mixed_intersection.c',
  'src/containers/mixed_negation.c',
  'src/containers/mixed_subset.c',
  'src/containers/mixed_union.c',
  'src/containers/mixed_xor.c',
  'src/containers/run.c',
  'src/isadetection.c',
  'src/memory.c',
  'src/roaring.c',
  'src/roaring_array.c',
  'src/roaring_priority_queue.c',
)

croaring_headers = [include_directories('cpp'), include_directories('include')]

croaring_lib = library(
  'croaring',
  croaring_sources,
  include_directories: croaring_headers,
)

croaring_dep = declare_dependency(
  include_directories: croaring_headers,
  link_with: croaring_lib,
)
