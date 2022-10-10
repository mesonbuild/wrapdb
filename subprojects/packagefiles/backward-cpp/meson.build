project('backward-cpp', 'cpp', version: '1.6')

install_headers('backward.hpp', subdir : 'backward')
backward = library('backward-cpp', files('backward.cpp'), install: true)
backward_dep = declare_dependency(link_with: backward)

tests = ['test', 'stacktrace', 'rectrace', 'select_signals']

foreach test : tests
    test('test_' + test, executable('testexe_' + test, 'test/' + test + '.cpp', 'test/_test_main.cpp'))
endforeach

tests = ['suicide']
foreach test : tests
    test('test_' + test, executable('testexe_' + test, 'test/' + test + '.cpp', 'test/_test_main.cpp'))
endforeach
