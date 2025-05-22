project(
  'backward-cpp',
  'cpp',
  version: '1.6',
)

cpp = meson.get_compiler('cpp')

bfd = cpp.find_library(
  'bfd',
  required: false,
)
dw = cpp.find_library(
  'dw',
  required: false,
)
unwind = dependency(
  'libunwind',
  required: false,
)
dwarf = dependency(
  'libdwarf',
  required: false,
)

deps = [bfd, dw, dwarf, unwind]

backward_project_args = []

if bfd.found()
  backward_project_args += ['-DBACKWARD_HAS_BFD=1']
  if meson.version().version_compare('>= 0.62')
    deps += dependency('dl')
  else
    deps += cpp.find_library('dl')
  endif
endif

if dw.found()
  backward_project_args += ['-DBACKWARD_HAS_DW=1']
endif

if dwarf.found()
  backward_project_args += ['-DBACKWARD_HAS_DWARF=1']
endif

has_backtrace = cpp.has_header('execinfo.h') and cpp.has_header_symbol(
  'execinfo.h',
  'backtrace',
)
backward_project_args += [
  '-DBACKWARD_HAS_BACKTRACE=@0@'.format(has_backtrace.to_int()),
  '-DBACKWARD_HAS_BACKTRACE_SYMBOL=@0@'.format(has_backtrace.to_int()),
]

add_project_arguments(
  backward_project_args,
  language: 'cpp',
)

install_headers(
  'backward.hpp',
  subdir: 'backward',
)

if host_machine.system() == 'windows'
  deps += cpp.find_library('dbghelp')
  backward = static_library(
    'backward-cpp',
    'backward.cpp',
    dependencies: deps,
    install: true,
  )
else
  backward = library(
    'backward-cpp',
    'backward.cpp',
    dependencies: deps,
    install: true,
  )
endif

backward_cpp_interface_dep = declare_dependency(
  include_directories: '.',
  dependencies: deps,
)

backward_dep = declare_dependency(
  dependencies: backward_cpp_interface_dep,
  link_with: backward,
)

tests = ['test', 'stacktrace', 'rectrace', 'select_signals']

foreach test : tests
  test(
    'test_' + test,
    executable(
      'testexe_' + test,
      'test/' + test + '.cpp',
      'test/_test_main.cpp',
      dependencies: backward_dep,
    ),
  )
endforeach

tests = ['suicide']
foreach test : tests
  test(
    'test_' + test,
    executable('testexe_' + test, 'test/' + test + '.cpp', 'test/_test_main.cpp'),
  )
endforeach
