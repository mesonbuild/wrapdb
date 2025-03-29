file_test_helpers_lib = static_library(
  'file_test_helpers',
  'file_test_helpers.cpp',
  dependencies: nowide_dep,
  include_directories: includes,
)

tests_kwargs = {
  'codecvt': {},
  'convert': {},
  'env': {},
  'env windows': {
    'sources': 'test_env.cpp',
    'cpp_args': '-DNOWIDE_TEST_INCLUDE_WINDOWS',
  },
  # we skip test_fs.cpp which would have tested intergation with boost::filesystem
  'filebuf': {
    'link_with': file_test_helpers_lib,
  },
  'fstream': {
    'link_with': file_test_helpers_lib,
  },
  'fstream_special': {
    'link_with': file_test_helpers_lib,
  },
  'ifstream': {
    'link_with': file_test_helpers_lib,
  },
  'iostream': {
    'link_with': file_test_helpers_lib,
  },
  'ofstream': {
    'link_with': file_test_helpers_lib,
  },
  'stackstring': {},
  'stat': {},
  'stdio': {},
  'system_narrow': {
    'sources': 'test_system.cpp',
    'cpp_args': '-DNOWIDE_TEST_USE_NARROW=1',
  },
  'traits': {},
}

if host_machine.system() == 'windows'
  tests_kwargs += {
    'system_wide': {
      'sources': 'test_system.cpp',
      'cpp_args': '-DNOWIDE_TEST_USE_NARROW=0',
    },
  }
else
  foreach name : [
    'filebuf',
    'ifstream',
    'ofstream',
    'fstream',
    'fstream_special',
  ]
    tests_kwargs += {
      name + '_with_internal_filebuf_replacement': {
        'sources': 'test_' + name + '.cpp',
        'cpp_args': '-DNOWIDE_USE_FILEBUF_REPLACEMENT=1',
        'link_with': file_test_helpers_lib,
      },
    }
  endforeach
endif

foreach name, kwargs : tests_kwargs
  if 'sources' not in kwargs
    kwargs += {
      'sources': 'test_' + name + '.cpp',
    }
  endif
  test_executable = executable(
    'test_' + name,
    dependencies: nowide_dep,
    include_directories: includes,
    kwargs: kwargs,
  )
  test('test_' + name, test_executable)
endforeach


iostream_interactive = executable(
  'iostream_interactive',
  'test_iostream.cpp',
  dependencies: nowide_dep,
  include_directories: includes,
  cpp_args: '-DNOWIDE_TEST_INTERACTIVE',
  link_with: file_test_helpers_lib,
)

test(
  'iostream_interactive',
  find_program('python3'),
  args: [files('test_iostream_interactive.py'), iostream_interactive],
)

fstream_benchmark = executable(
  'fstream_benchmark',
  'benchmark_fstream.cpp',
  dependencies: nowide_dep,
  include_directories: includes,
  cpp_args: '-DNOWIDE_USE_FILEBUF_REPLACEMENT=1',
)
