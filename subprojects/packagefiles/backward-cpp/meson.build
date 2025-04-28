project(
  'backward-cpp',
  'cpp',
  version: '1.6',
  meson_version: '>= 0.47',
)

cpp = meson.get_compiler('cpp')

bfd = cpp.find_library(
  'bfd',
  required: get_option('bfd'),
)
dw = cpp.find_library(
  'dw',
  required: get_option('dw'),
)
libunwind = dependency(
  'libunwind',
  required: get_option('libunwind'),
)
dwarf = dependency(
  'libdwarf',
  required: get_option('dwarf'),
)

deps = []
args = []
# stack walking
if libunwind.found()
  deps += libunwind
  args += ['-DBACKWARD_HAS_LIBUNWIND=1']
endif

# stack detail extraction
if dw.found()
  deps += dw
  args += ['-DBACKWARD_HAS_DW=1']
elif dwarf.found()
  deps += dwarf
  args += ['-DBACKWARD_HAS_DWARF=1']
elif bfd.found()
  deps += bfd
  args += ['-DBACKWARD_HAS_BFD=1']
  if host_machine.system() != 'windows'
    if meson.version().version_compare('>= 0.62')
      deps += dependency('dl')
    else
      deps += cpp.find_library('dl')
    endif
  endif
endif

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
    cpp_args: args,
  )
else
  backward = library(
    'backward-cpp',
    'backward.cpp',
    dependencies: deps,
    install: true,
    cpp_args: args,
  )
endif

backward_interface_dep = declare_dependency(
  include_directories: include_directories('.'),
  dependencies: deps,
  compile_args: args,
)

backward_dep = declare_dependency(
  dependencies: backward_interface_dep,
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

# https://github.com/bombela/backward-cpp/pull/242
if meson.project_version() != '1.6' or host_machine.cpu_family() not in [
  'aarch64',
  'mips',
  'mips64',
]
  tests = ['suicide']
  foreach test : tests
    test(
      'test_' + test,
      executable(
        'testexe_' + test,
        'test/' + test + '.cpp',
        'test/_test_main.cpp',
        cpp_args: args,
      ),
    )
  endforeach
endif
