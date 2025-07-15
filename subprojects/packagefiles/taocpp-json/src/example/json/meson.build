example_files = [
  'cbor_to_jaxn.cpp',
  'cbor_to_json.cpp',
  'cbor_to_msgpack.cpp',
  'cbor_to_pretty_jaxn.cpp',
  'cbor_to_pretty_json.cpp',
  'cbor_to_ubjson.cpp',
  'jaxn_to_cbor.cpp',
  'jaxn_to_cplusplus.cpp',
  'jaxn_to_jaxn.cpp',
  'jaxn_to_msgpack.cpp',
  'jaxn_to_pretty_jaxn.cpp',
  'jaxn_to_ubjson.cpp',
  'json_to_cbor.cpp',
  'json_to_json.cpp',
  'json_to_msgpack.cpp',
  'json_to_pretty_json.cpp',
  'json_to_ubjson.cpp',
  'msgpack_to_cbor.cpp',
  'msgpack_to_jaxn.cpp',
  'msgpack_to_json.cpp',
  'msgpack_to_pretty_jaxn.cpp',
  'msgpack_to_pretty_json.cpp',
  'msgpack_to_ubjson.cpp',
  'printf_doubles.cpp',
  'ubjson_to_cbor.cpp',
  'ubjson_to_jaxn.cpp',
  'ubjson_to_json.cpp',
  'ubjson_to_msgpack.cpp',
  'ubjson_to_pretty_jaxn.cpp',
  'ubjson_to_pretty_json.cpp',
  'validate_event_order.cpp',
  'validate_integer.cpp',
]

args = []
cpp = meson.get_compiler('cpp')

if cpp.get_argument_syntax() == 'msvc'
  args += cpp.get_supported_arguments('/W4', '/WX', '/utf-8')
else
  args += cpp.get_supported_arguments('-pedantic', '-Wall', '-Wextra', '-Wshadow', '-Werror')
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
