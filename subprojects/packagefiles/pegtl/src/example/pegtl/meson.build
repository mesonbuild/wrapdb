example_files = [
  'abnf2pegtl.cpp',
  'analyze.cpp',
  'calculator.cpp',
  'chomsky_hierarchy.cpp',
  'csv1.cpp',
  'csv2.cpp',
  'dynamic_match.cpp',
  'expression.cpp',
  'hello_world.cpp',
  'indent_aware.cpp',
  'iri.cpp',
  'json_analyze.cpp',
  'json_ast.cpp',
  'json_build.cpp',
  'json_count.cpp',
  'json_coverage.cpp',
  'json_parse.cpp',
  'json_print_debug.cpp',
  'json_print_names.cpp',
  'json_trace.cpp',
  'lua53_analyze.cpp',
  'lua53_parse.cpp',
  'modulus_match.cpp',
  'parse_tree.cpp',
  'parse_tree_user_state.cpp',
  'peg2pegtl.cpp',
  'proto3.cpp',
  'recover.cpp',
  's_expression.cpp',
  'sum.cpp',
  'symbol_table.cpp',
  'token_input.cpp',
  'unescape.cpp',
  'uri.cpp',
  'uri_print_debug.cpp',
  'uri_print_names.cpp',
  'uri_trace.cpp',
]

args = []
cpp = meson.get_compiler('cpp')

if cpp.get_argument_syntax() == 'msvc'
  args += cpp.get_supported_arguments('/W4', '/WX', '/utf-8')
else
  args += cpp.get_supported_arguments(
    '-pedantic',
    '-Wall',
    '-Wextra',
    '-Wshadow',
    '-Werror',
  )
endif

fs = import('fs')

foreach file : example_files

  name = fs.replace_suffix(file, '')

  example_exe = executable(
    name,
    files(file),
    dependencies: pegtl_dep,
    cpp_args: args,
  )

endforeach
