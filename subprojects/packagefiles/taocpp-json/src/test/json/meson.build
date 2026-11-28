test_files = [
  'big_list_of_naughty_strings.cpp',
  'binding_array.cpp',
  'binding_factory.cpp',
  'binding_function.cpp',
  'binding_object.cpp',
  'binding_versions.cpp',
  'cbor.cpp',
  'cbor_parts_parser.cpp',
  'contrib_diff.cpp',
  'contrib_get.cpp',
  'contrib_patch_add.cpp',
  'contrib_patch_copy.cpp',
  'contrib_patch_move.cpp',
  'contrib_patch_remove.cpp',
  'contrib_patch_replace.cpp',
  'contrib_patch_test.cpp',
  'contrib_position.cpp',
  'contrib_reference.cpp',
  'contrib_schema.cpp',
  'contrib_traits.cpp',
  'double.cpp',
  'enable_implicit_constructor.cpp',
  'escape.cpp',
  'events_binary_to.cpp',
  'events_compare.cpp',
  'events_debug.cpp',
  'events_hash.cpp',
  'events_to_stream.cpp',
  'events_to_string.cpp',
  'include_json.cpp',
  'integer.cpp',
  'jaxn_ostream.cpp',
  'jaxn_parse.cpp',
  'jaxn_parts_parser.cpp',
  'json_ostream.cpp',
  'json_parse.cpp',
  'json_parts_parser.cpp',
  'json_pointer.cpp',
  'key_camel_case_to_snake_case.cpp',
  'key_snake_case_to_camel_case.cpp',
  'literal.cpp',
  'msgpack.cpp',
  'object_construction.cpp',
  'opaque_pointer.cpp',
  'operators.cpp',
  'optional.cpp',
  'public_base.cpp',
  'self_contained.cpp',
  'sha256.cpp',
  'temporary_parsing.cpp',
  'type.cpp',
  'ubjson.cpp',
  'uri_fragment.cpp',
  'validate_event_interfaces.cpp',
  'validate_utf8.cpp',
  'value_access.cpp',
  'value_basics.cpp',
  'value_create.cpp',
  'value_ptr.cpp',
  'value_subscript.cpp',
  'with_arguments.cpp',
]

args = []
cpp = meson.get_compiler('cpp')

if cpp.get_argument_syntax() == 'msvc'
  args += cpp.get_supported_arguments('/W4', '/WX', '/utf-8')
else
  args += cpp.get_supported_arguments('-pedantic', '-Wall', '-Wextra', '-Wshadow', '-Werror')
endif

fs = import('fs')

foreach file : test_files

  name = fs.replace_suffix(file, '')

  test_exe = executable(
    name,
    files(file),
    dependencies: pegtl_dep,
    cpp_args: args,
  )

  test(name, test_exe, workdir: meson.project_source_root())

endforeach
