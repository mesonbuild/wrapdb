project('UnitTest++', 'cpp',
    version : '2.0.0',
    license : 'MIT')

unittest_cpp_src = []

subdir('UnitTest++')

unittest_cpp_lib = static_library('unittest-cpp', 
    unittest_cpp_src,
    include_directories : '.')

unittest_cpp_dep = declare_dependency(
    version : meson.project_version(),
    link_with : unittest_cpp_lib,
    include_directories : '.')

subdir('tests')
