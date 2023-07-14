protoc_src = ['google/protobuf/compiler/main.cc']
protoc = executable(
  'protoc',
  protoc_src,
  include_directories: incdir,
  link_with: libprotoc,
  dependencies: dependency('threads'),
  install: true,
)

if meson.is_cross_build()
  protoc_native = executable(
    'protoc-native',
    [libprotobuf_lite_src, libprotobuf_src, libprotoc_src, protoc_src],
    native: true,
    include_directories: incdir,
    dependencies: dependency('threads', native: true),
  )
else
  protoc_native = protoc
endif

meson.override_find_program('protoc', protoc_native)

protoc_gen = generator(
  protoc_native,
  output: ['@BASENAME@.pb.cc', '@BASENAME@.pb.h'],
  arguments: ['@EXTRA_ARGS@', '--proto_path=' + meson.current_source_dir(), '--cpp_out=@BUILD_DIR@', '@INPUT@'],
)

install_headers(
  'google/protobuf/any.h',
  'google/protobuf/any.pb.h',
  'google/protobuf/api.pb.h',
  'google/protobuf/arena.h',
  'google/protobuf/arena_impl.h',
  'google/protobuf/arenastring.h',
  'google/protobuf/arenaz_sampler.h',
  'google/protobuf/descriptor.h',
  'google/protobuf/descriptor.pb.h',
  'google/protobuf/descriptor_database.h',
  'google/protobuf/duration.pb.h',
  'google/protobuf/dynamic_message.h',
  'google/protobuf/empty.pb.h',
  'google/protobuf/endian.h',
  'google/protobuf/explicitly_constructed.h',
  'google/protobuf/extension_set.h',
  'google/protobuf/extension_set_inl.h',
  'google/protobuf/field_access_listener.h',
  'google/protobuf/field_mask.pb.h',
  'google/protobuf/generated_enum_reflection.h',
  'google/protobuf/generated_enum_util.h',
  'google/protobuf/generated_message_bases.h',
  'google/protobuf/generated_message_reflection.h',
  'google/protobuf/generated_message_tctable_decl.h',
  'google/protobuf/generated_message_tctable_impl.h',
  'google/protobuf/generated_message_util.h',
  'google/protobuf/has_bits.h',
  'google/protobuf/implicit_weak_message.h',
  'google/protobuf/inlined_string_field.h',
  'google/protobuf/map.h',
  'google/protobuf/map_entry.h',
  'google/protobuf/map_entry_lite.h',
  'google/protobuf/map_field.h',
  'google/protobuf/map_field_inl.h',
  'google/protobuf/map_field_lite.h',
  'google/protobuf/map_type_handler.h',
  'google/protobuf/message.h',
  'google/protobuf/message_lite.h',
  'google/protobuf/metadata.h',
  'google/protobuf/metadata_lite.h',
  'google/protobuf/parse_context.h',
  'google/protobuf/port.h',
  'google/protobuf/port_def.inc',
  'google/protobuf/port_undef.inc',
  'google/protobuf/reflection.h',
  'google/protobuf/reflection_ops.h',
  'google/protobuf/repeated_field.h',
  'google/protobuf/repeated_ptr_field.h',
  'google/protobuf/service.h',
  'google/protobuf/source_context.pb.h',
  'google/protobuf/struct.pb.h',
  'google/protobuf/text_format.h',
  'google/protobuf/timestamp.pb.h',
  'google/protobuf/type.pb.h',
  'google/protobuf/unknown_field_set.h',
  'google/protobuf/wire_format.h',
  'google/protobuf/wire_format_lite.h',
  'google/protobuf/wrappers.pb.h',
  'google/protobuf/any.proto',
  'google/protobuf/api.proto',
  'google/protobuf/descriptor.proto',
  'google/protobuf/duration.proto',
  'google/protobuf/empty.proto',
  'google/protobuf/field_mask.proto',
  'google/protobuf/source_context.proto',
  'google/protobuf/struct.proto',
  'google/protobuf/timestamp.proto',
  'google/protobuf/type.proto',
  'google/protobuf/wrappers.proto',
  subdir: 'google/protobuf',
)

install_headers(
  'google/protobuf/compiler/code_generator.h',
  'google/protobuf/compiler/command_line_interface.h',
  'google/protobuf/compiler/importer.h',
  'google/protobuf/compiler/parser.h',
  'google/protobuf/compiler/plugin.h',
  'google/protobuf/compiler/plugin.pb.h',
  'google/protobuf/compiler/plugin.proto',
  subdir: 'google/protobuf/compiler',
)

install_headers(
  'google/protobuf/compiler/cpp/file.h',
  'google/protobuf/compiler/cpp/generator.h',
  'google/protobuf/compiler/cpp/helpers.h',
  'google/protobuf/compiler/cpp/names.h',
  subdir: 'google/protobuf/compiler/cpp',
)

install_headers(
  'google/protobuf/compiler/csharp/csharp_doc_comment.h',
  'google/protobuf/compiler/csharp/csharp_generator.h',
  'google/protobuf/compiler/csharp/csharp_names.h',
  'google/protobuf/compiler/csharp/csharp_options.h',
  subdir: 'google/protobuf/compiler/csharp',
)

install_headers(
  'google/protobuf/compiler/java/java_generator.h',
  'google/protobuf/compiler/java/names.h',
  subdir: 'google/protobuf/compiler/java',
)

install_headers(
  'google/protobuf/compiler/objectivec/objectivec_generator.h',
  'google/protobuf/compiler/objectivec/objectivec_helpers.h',
  subdir: 'google/protobuf/compiler/objectivec',
)

install_headers(
  'google/protobuf/compiler/php/php_generator.h',
  subdir: 'google/protobuf/compiler/php',
)

install_headers(
  'google/protobuf/compiler/python/generator.h',
  'google/protobuf/compiler/python/pyi_generator.h',
  'google/protobuf/compiler/python/helpers.h',
  subdir: 'google/protobuf/compiler/python',
)

install_headers(
  'google/protobuf/compiler/ruby/ruby_generator.h',
  subdir: 'google/protobuf/compiler/ruby',
)

install_headers(
  'google/protobuf/io/coded_stream.h',
  'google/protobuf/io/gzip_stream.h',
  'google/protobuf/io/io_win32.h',
  'google/protobuf/io/printer.h',
  'google/protobuf/io/strtod.h',
  'google/protobuf/io/tokenizer.h',
  'google/protobuf/io/zero_copy_stream.h',
  'google/protobuf/io/zero_copy_stream_impl.h',
  'google/protobuf/io/zero_copy_stream_impl_lite.h',
  subdir: 'google/protobuf/io',
)

install_headers(
  'google/protobuf/stubs/bytestream.h',
  'google/protobuf/stubs/callback.h',
  'google/protobuf/stubs/casts.h',
  'google/protobuf/stubs/common.h',
  'google/protobuf/stubs/hash.h',
  'google/protobuf/stubs/logging.h',
  'google/protobuf/stubs/macros.h',
  'google/protobuf/stubs/map_util.h',
  'google/protobuf/stubs/mutex.h',
  'google/protobuf/stubs/once.h',
  'google/protobuf/stubs/platform_macros.h',
  'google/protobuf/stubs/port.h',
  'google/protobuf/stubs/status.h',
  'google/protobuf/stubs/stl_util.h',
  'google/protobuf/stubs/stringpiece.h',
  'google/protobuf/stubs/strutil.h',
  'google/protobuf/stubs/template_util.h',
  subdir: 'google/protobuf/stubs',
)

install_headers(
  'google/protobuf/util/delimited_message_util.h',
  'google/protobuf/util/field_comparator.h',
  'google/protobuf/util/field_mask_util.h',
  'google/protobuf/util/json_util.h',
  'google/protobuf/util/message_differencer.h',
  'google/protobuf/util/time_util.h',
  'google/protobuf/util/type_resolver.h',
  'google/protobuf/util/type_resolver_util.h',
  subdir: 'google/protobuf/util',
)
