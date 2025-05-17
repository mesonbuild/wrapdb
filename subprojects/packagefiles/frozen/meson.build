project(
  'frozen',
  'cpp',
  version: '1.2.0',
  license: 'Apache-2.0',
)

install_headers(
  'include/frozen/algorithm.h',
  'include/frozen/map.h',
  'include/frozen/random.h',
  'include/frozen/set.h',
  'include/frozen/string.h',
  'include/frozen/unordered_map.h',
  'include/frozen/unordered_set.h',
  subdir: 'frozen',
)

install_headers(
  'include/frozen/bits/algorithms.h',
  'include/frozen/bits/basic_types.h',
  'include/frozen/bits/constexpr_assert.h',
  'include/frozen/bits/defines.h',
  'include/frozen/bits/elsa_std.h',
  'include/frozen/bits/elsa.h',
  'include/frozen/bits/exceptions.h',
  'include/frozen/bits/hash_string.h',
  'include/frozen/bits/pmh.h',
  'include/frozen/bits/version.h',
  subdir: 'frozen/bits',
)

pkgc = import('pkgconfig')
pkgc.generate(
  name: 'frozen',
  version: meson.project_version(),
  description: '0 cost initialization for immutable containers, fixed-size containers, and various algorithms.',
)

frozen_dep = declare_dependency(
  include_directories: include_directories('include'),
)
