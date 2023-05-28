test_module_header_files = files(
    'web/ClientServerTestRunner.hpp',
    'Checker.hpp',
    'UnitTest.hpp',
)

test_module_src_files += files(
    'Checker.cpp',
    'UnitTest.cpp',
    test_module_header_files,
)

install_headers(test_module_header_files, subdir: 'oatpp-test')
