project(
  'leveldb',
  'c',
  'cpp',
  version: '1.23',
  default_options: ['cpp_std=c++17'],
  meson_version: '>= 0.56.0',
  license: 'BSD-3-Clause',
)

build_tests = get_option('leveldb_build_tests')
build_benchmarks = get_option('leveldb_build_benchmarks')
do_install = get_option('leveldb_install')

c_comp = meson.get_compiler('c')
cpp_comp = meson.get_compiler('cpp')

if host_machine.system() == 'windows'
  platform_define = 'LEVELDB_PLATFORM_WINDOWS=1'
  platform_sources = files(
    'util/env_windows.cc',
    'util/windows_logger.h',
  )
  cpp_project_args = [
    '/EHs-c-',
    '/GR-',
    '/D_HAS_EXCEPTIONS=0',
    '/D_UNICODE',
    '/DUNICODE',
  ]
else
  platform_define = 'LEVELDB_PLATFORM_POSIX=1'
  platform_sources = files(
    'util/env_posix.cc',
    'util/posix_logger.h',
  )
  cpp_project_args = ['-fno-exceptions', '-fno-rtti']
endif

c_project_args = []
if c_comp.get_id() != 'msvc' and c_comp.has_argument('-Wstrict-prototypes')
  c_project_args += ['-Wstrict-prototypes']
endif

if cpp_comp.has_argument('-Wthread-safety')
  cpp_project_args += ['-Wthread-safety']
endif

have_cxx17_has_include = cpp_comp.compiles(
  '''
#if defined(__has_include) && __has_include(<string>)
#include <string>
#endif
int main() { std::string str; return 0; }
''',
  name: 'cxx17_has_include',
)

cpp_project_args += ['-D' + platform_define]
if not have_cxx17_has_include
  cpp_project_args += ['-DLEVELDB_HAS_PORT_CONFIG_H=1']
endif

add_project_arguments(
  c_project_args,
  language: 'c',
)
add_project_arguments(
  cpp_project_args,
  language: 'cpp',
)

have_fdatasync = cpp_comp.has_function(
  'fdatasync',
  prefix: '#include <unistd.h>',
)
have_fullfsync = cpp_comp.has_header_symbol('fcntl.h', 'F_FULLFSYNC')
have_o_cloexec = cpp_comp.has_header_symbol('fcntl.h', 'O_CLOEXEC')

crc32c_dep = dependency(
  'crc32c',
  required: false,
)
if not crc32c_dep.found()
  crc32c_dep = cpp_comp.find_library(
    'crc32c',
    required: false,
  )
endif
snappy_dep = dependency(
  'snappy',
  required: false,
)
if not snappy_dep.found()
  snappy_dep = cpp_comp.find_library(
    'snappy',
    required: false,
  )
endif
zstd_dep = dependency(
  'libzstd',
  required: false,
)
if not zstd_dep.found()
  zstd_dep = cpp_comp.find_library(
    'zstd',
    required: false,
  )
endif
tcmalloc_dep = dependency(
  'tcmalloc',
  required: false,
)
if not tcmalloc_dep.found()
  tcmalloc_dep = cpp_comp.find_library(
    'tcmalloc',
    required: false,
  )
endif

conf_data = configuration_data()
conf_data.set10('HAVE_FDATASYNC', have_fdatasync)
conf_data.set10('HAVE_FULLFSYNC', have_fullfsync)
conf_data.set10('HAVE_O_CLOEXEC', have_o_cloexec)
conf_data.set10('HAVE_CRC32C', crc32c_dep.found())
conf_data.set10('HAVE_SNAPPY', snappy_dep.found())
conf_data.set10('HAVE_ZSTD', zstd_dep.found())

subdir('port')

inc = include_directories('./include')

leveldb_sources = files(
  'db/builder.cc',
  'db/builder.h',
  'db/c.cc',
  'db/db_impl.cc',
  'db/db_impl.h',
  'db/db_iter.cc',
  'db/db_iter.h',
  'db/dbformat.cc',
  'db/dbformat.h',
  'db/dumpfile.cc',
  'db/filename.cc',
  'db/filename.h',
  'db/log_format.h',
  'db/log_reader.cc',
  'db/log_reader.h',
  'db/log_writer.cc',
  'db/log_writer.h',
  'db/memtable.cc',
  'db/memtable.h',
  'db/repair.cc',
  'db/skiplist.h',
  'db/snapshot.h',
  'db/table_cache.cc',
  'db/table_cache.h',
  'db/version_edit.cc',
  'db/version_edit.h',
  'db/version_set.cc',
  'db/version_set.h',
  'db/write_batch.cc',
  'db/write_batch_internal.h',
  'helpers/memenv/memenv.cc',
  'helpers/memenv/memenv.h',
  'port/port.h',
  'port/port_stdcxx.h',
  'port/thread_annotations.h',
  'table/block.cc',
  'table/block.h',
  'table/block_builder.cc',
  'table/block_builder.h',
  'table/filter_block.cc',
  'table/filter_block.h',
  'table/format.cc',
  'table/format.h',
  'table/iterator.cc',
  'table/iterator_wrapper.h',
  'table/merger.cc',
  'table/merger.h',
  'table/table.cc',
  'table/table_builder.cc',
  'table/two_level_iterator.cc',
  'table/two_level_iterator.h',
  'util/arena.cc',
  'util/arena.h',
  'util/bloom.cc',
  'util/cache.cc',
  'util/coding.cc',
  'util/coding.h',
  'util/comparator.cc',
  'util/crc32c.cc',
  'util/crc32c.h',
  'util/env.cc',
  'util/filter_policy.cc',
  'util/hash.cc',
  'util/hash.h',
  'util/logging.cc',
  'util/logging.h',
  'util/mutexlock.h',
  'util/no_destructor.h',
  'util/options.cc',
  'util/random.h',
  'util/status.cc',
)

leveldb_deps = [dependency('threads')]
if crc32c_dep.found()
  leveldb_deps += crc32c_dep
endif
if snappy_dep.found()
  leveldb_deps += snappy_dep
endif
if zstd_dep.found()
  leveldb_deps += zstd_dep
endif
if tcmalloc_dep.found()
  leveldb_deps += tcmalloc_dep
endif

build_shared = get_option('default_library') != 'static'
lib_cpp_args = ['-DLEVELDB_COMPILE_LIBRARY']
if build_shared
  lib_cpp_args += ['-DLEVELDB_SHARED_LIBRARY']
endif

leveldb_lib = library(
  'leveldb',
  leveldb_sources,
  platform_sources,
  include_directories: inc,
  dependencies: leveldb_deps,
  cpp_args: lib_cpp_args,
  install: do_install,
  version: meson.project_version(),
  soversion: meson.project_version().split('.')[0],
)
leveldb_dep = declare_dependency(
  include_directories: inc,
  link_with: leveldb_lib,
  dependencies: leveldb_deps,
  compile_args: ['-DLEVELDB_HAS_PORT_CONFIG_H=1'],  # 仅当你需要强制定义,
)

if meson.version().version_compare('>=0.54.0')
  meson.override_dependency('leveldb', leveldb_dep)
endif

leveldb_util = executable(
  'leveldbutil',
  'db/leveldbutil.cc',
  include_directories: inc,
  link_with: leveldb_lib,
  install: do_install,
)
meson.override_find_program('leveldbutil', leveldb_util)

if do_install
  install_headers(
    'include/leveldb/c.h',
    'include/leveldb/cache.h',
    'include/leveldb/comparator.h',
    'include/leveldb/db.h',
    'include/leveldb/dumpfile.h',
    'include/leveldb/env.h',
    'include/leveldb/export.h',
    'include/leveldb/filter_policy.h',
    'include/leveldb/iterator.h',
    'include/leveldb/options.h',
    'include/leveldb/slice.h',
    'include/leveldb/status.h',
    'include/leveldb/table_builder.h',
    'include/leveldb/table.h',
    'include/leveldb/write_batch.h',
    subdir: 'leveldb',
  )
endif

if build_tests
  gtest_dep = dependency(
    'gtest',
    required: false,
  )
  gmock_dep = dependency(
    'gmock',
    required: false,
  )
  gtest_main_dep = dependency(
    'gtest_main',
    required: false,
  )
  if not gtest_dep.found() or not gmock_dep.found()
    error('LEVELDB_BUILD_TESTS requires gtest and gmock dependencies.')
  endif
  if not gtest_main_dep.found()
    error(
      'LEVELDB_BUILD_TESTS requires gtest_main for the aggregated test binary.',
    )
  endif

  leveldb_tests_sources = files(
    'util/no_destructor_test.cc',
    'util/status_test.cc',
    'util/testutil.cc',
    'util/testutil.h',
  )
  if not build_shared
    leveldb_tests_sources += files(
      'db/autocompact_test.cc',
      'db/corruption_test.cc',
      'db/db_test.cc',
      'db/dbformat_test.cc',
      'db/filename_test.cc',
      'db/log_test.cc',
      'db/recovery_test.cc',
      'db/skiplist_test.cc',
      'db/version_edit_test.cc',
      'db/version_set_test.cc',
      'db/write_batch_test.cc',
      'helpers/memenv/memenv_test.cc',
      'table/filter_block_test.cc',
      'table/table_test.cc',
      'util/arena_test.cc',
      'util/bloom_test.cc',
      'util/cache_test.cc',
      'util/coding_test.cc',
      'util/crc32c_test.cc',
      'util/hash_test.cc',
      'util/logging_test.cc',
    )
  endif

  leveldb_tests_deps = [gtest_dep, gmock_dep, gtest_main_dep]

  leveldb_tests_exe = executable(
    'leveldb_tests',
    leveldb_tests_sources,
    include_directories: inc,
    link_with: leveldb_lib,
    dependencies: leveldb_tests_deps,
  )
  test('leveldb_tests', leveldb_tests_exe)

  per_test_sources = files(
    'util/testutil.cc',
    'util/testutil.h',
  )

  c_test_exe = executable(
    'c_test',
    per_test_sources + files('db/c_test.c'),
    include_directories: inc,
    link_with: leveldb_lib,
    dependencies: [gtest_dep, gmock_dep],
  )
  test('c_test', c_test_exe)

  if not build_shared
    if host_machine.system() == 'windows'
      env_test_source = files('util/env_windows_test.cc')
    else
      env_test_source = files('util/env_posix_test.cc')
    endif

    env_test_exe = executable(
      'env_test',
      per_test_sources + env_test_source,
      include_directories: inc,
      link_with: leveldb_lib,
      dependencies: [gtest_dep, gmock_dep],
    )
    test('env_test', env_test_exe)
  endif
endif

if build_benchmarks
  benchmark_dep = dependency(
    'benchmark',
    required: false,
  )
  gtest_dep = dependency(
    'gtest',
    required: false,
  )
  gmock_dep = dependency(
    'gmock',
    required: false,
  )
  if not benchmark_dep.found() or not gtest_dep.found() or not gmock_dep.found()
    error('LEVELDB_BUILD_BENCHMARKS requires benchmark, gtest, and gmock.')
  endif

  bench_common = files(
    'util/histogram.cc',
    'util/histogram.h',
    'util/testutil.cc',
    'util/testutil.h',
  )

  if not build_shared
    bench_exe = executable(
      'db_bench',
      bench_common + files('benchmarks/db_bench.cc'),
      include_directories: inc,
      link_with: leveldb_lib,
      dependencies: [benchmark_dep, gtest_dep, gmock_dep],
    )
  endif

  sqlite3_dep = dependency(
    'sqlite3',
    required: false,
  )
  if sqlite3_dep.found()
    bench_sqlite = executable(
      'db_bench_sqlite3',
      bench_common + files('benchmarks/db_bench_sqlite3.cc'),
      include_directories: inc,
      link_with: leveldb_lib,
      dependencies: [benchmark_dep, gtest_dep, gmock_dep, sqlite3_dep],
    )
  endif

  kyoto_lib = cpp_comp.find_library(
    'kyotocabinet',
    required: false,
  )
  if kyoto_lib.found() and cpp_comp.has_header('kcpolydb.h')
    bench_kyoto = executable(
      'db_bench_tree_db',
      bench_common + files('benchmarks/db_bench_tree_db.cc'),
      include_directories: inc,
      link_with: leveldb_lib,
      dependencies: [benchmark_dep, gtest_dep, gmock_dep, kyoto_lib],
    )
  endif
endif
