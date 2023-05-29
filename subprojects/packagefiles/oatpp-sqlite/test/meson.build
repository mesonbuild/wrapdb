
test_src_files = files(
    'oatpp-sqlite/ql_template/ParserTest.cpp',
    'oatpp-sqlite/ql_template/ParserTest.hpp',
    'oatpp-sqlite/tests.cpp',
    'oatpp-sqlite/types/BlobTest.cpp',
    'oatpp-sqlite/types/BlobTest.hpp',
    'oatpp-sqlite/types/IntTest.cpp',
    'oatpp-sqlite/types/IntTest.hpp',
    'oatpp-sqlite/types/InterpretationTest.cpp',
    'oatpp-sqlite/types/InterpretationTest.hpp',
    'oatpp-sqlite/types/NumericTest.cpp',
    'oatpp-sqlite/types/NumericTest.hpp',
)


test_flags = flags
test_flags += [
    '-DTEST_DB_FILE="' + (meson.project_source_root() / 'test_db.sqlite') + '"',
]
test_flags += (
    '-DTEST_DB_MIGRATION="' + (
        meson.project_source_root() / 'test' / 'oatpp-sqlite/migration/'
    ) + '"'
)



test_deps = deps
test_deps += dependency('oatpp-test', version: '1.3.0')
test_deps += oatpp_sqlite_dep

test_inc_dirs = inc_dirs
test_inc_dirs += include_directories('.')

sqlite_tests = executable(
    'oatpp_sqlite_tests',
    test_src_files,
    cpp_args: test_flags,
    include_directories: test_inc_dirs,
    dependencies: test_deps,
)

test('oatpp sqlite module tests', sqlite_tests)
