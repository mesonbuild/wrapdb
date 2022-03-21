protoc_src = [ 'google/protobuf/compiler/main.cc' ]
protoc = executable(
  'protoc',
  protoc_src,
  cpp_args: flags,
  include_directories: include_directories('.'),
  link_with: libprotoc
)


if meson.is_cross_build()
  protoc_native = executable(
    'protoc-native',
    [libprotobuf_lite_src, libprotobuf_src, libprotoc_src, protoc_src],
    native: true,
    cpp_args: flags,
    include_directories: include_directories('.'),
    dependencies: dependency('threads', native: true),
  )
else
  protoc_native = protoc
endif

protoc_gen = generator(protoc_native,
  output: ['@BASENAME@.pb.cc', '@BASENAME@.pb.h'],
  arguments: ['@EXTRA_ARGS@', '--proto_path=' + meson.current_source_dir(), '--cpp_out=@BUILD_DIR@', '@INPUT@']
)
