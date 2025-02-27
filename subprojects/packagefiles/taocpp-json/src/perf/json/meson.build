perf_files = [
  'benchmark.cpp',
  'parse_file.cpp',
  'pretty_print_file.cpp',
  'print_double.cpp',
  'print_file.cpp',
  'sizes.cpp',
  'syntax_only.cpp',
]

args = []
cpp = meson.get_compiler('cpp')

if cpp.get_argument_syntax() == 'msvc'
  args += cpp.get_supported_arguments('/W4', '/WX', '/utf-8')
else
  args += cpp.get_supported_arguments('-pedantic', '-Wall', '-Wextra', '-Wshadow', '-Werror')
endif

fs = import('fs')

foreach file : perf_files

  name = fs.replace_suffix(file, '')

  perf_exe = executable(
    name,
    files(file),
    dependencies: pegtl_dep,
    cpp_args: args,
  )

endforeach
