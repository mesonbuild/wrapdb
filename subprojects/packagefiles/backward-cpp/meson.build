project('backward-cpp', 'cpp', version: '1.6')

cpp = meson.get_compiler('cpp')

bfd = cpp.find_library('bfd', required: false)
dw = cpp.find_library('dw', required: false)
unwind = dependency('libunwind', required: false)
dwarf = dependency('libdwarf', required: false)

deps = [bfd, dw, dwarf, unwind]

if bfd.found()
    add_project_arguments('-DBACKWARD_HAS_BFD=1', language: 'cpp')
    if meson.version().version_compare('>= 0.62')
        deps += dependency('dl')
    else
        deps += cpp.find_library('dl')
    endif
endif

if dw.found()
    add_project_arguments('-DBACKWARD_HAS_DW=1', language: 'cpp')
endif

if dwarf.found()
    add_project_arguments('-DBACKWARD_HAS_DWARF=1', language: 'cpp')
endif

install_headers('backward.hpp', subdir : 'backward')

if host_machine.system() == 'windows'
    deps += cpp.find_library('dbghelp')
    backward = static_library('backward-cpp', 'backward.cpp', dependencies: deps, install: true)
else
    backward = library('backward-cpp', 'backward.cpp', dependencies: deps, install: true)
endif

backward_dep = declare_dependency(dependencies: deps, link_with: backward)

if get_option('tests')
    tests = ['test', 'stacktrace', 'rectrace', 'select_signals']

    foreach test : tests
        test('test_' + test, executable('testexe_' + test, 'test/' + test + '.cpp', 'test/_test_main.cpp', dependencies: backward_dep))
    endforeach

    tests = ['suicide']
    foreach test : tests
        test('test_' + test, executable('testexe_' + test, 'test/' + test + '.cpp', 'test/_test_main.cpp'))
    endforeach
endif
