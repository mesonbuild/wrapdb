test_module_header_files = files(
    'web/ClientServerTestRunner.hpp',
    'Checker.hpp',
    'UnitTest.hpp',
)

test_module_src_files += test_module_header_files

test_module_src_files += files(
    'Checker.cpp',
    'UnitTest.cpp',
)

install_headers(test_module_header_files, subdir: 'oatpp-test')
