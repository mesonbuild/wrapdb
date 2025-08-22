avro_flags = []
avro_deps = []
avro_public_deps = []

fmt_dep = dependency(
  'fmt',
  required: true,
)
avro_deps += fmt_dep
avro_public_deps += fmt_dep

zlib_dep = dependency(
  'zlib',
  required: true,
)
avro_deps += zlib_dep

snappy_dep = dependency(
  'snappy',
  required: false,
)
if snappy_dep.found()
  avro_flags += '-DSNAPPY_CODEC_AVAILABLE'
  avro_deps += snappy_dep
endif

zstd_dep = dependency(
  'zstd',
  required: false,
)
if zstd_dep.found()
  avro_flags += '-DZSTD_CODEC_AVAILABLE'
  avro_deps += zstd_dep
endif

# Set static and shared flags manually since Meson 1.3.0 is still too new
avro_flags += '-DAVRO_SOURCE'
if get_option('default_library') == 'shared'
  avro_flags += '-DAVRO_DYN_LINK'
elif get_option('default_library') == 'both'
  error('Building both static and shared libraries is not possible')
endif

avro_inc = include_directories('include/avro')

avro_src = files(
  'impl/BinaryDecoder.cc',
  'impl/BinaryEncoder.cc',
  'impl/Compiler.cc',
  'impl/CustomAttributes.cc',
  'impl/DataFile.cc',
  'impl/FileStream.cc',
  'impl/Generic.cc',
  'impl/GenericDatum.cc',
  'impl/LogicalType.cc',
  'impl/Node.cc',
  'impl/NodeImpl.cc',
  'impl/Resolver.cc',
  'impl/ResolverSchema.cc',
  'impl/Schema.cc',
  'impl/Stream.cc',
  'impl/Types.cc',
  'impl/ValidSchema.cc',
  'impl/Validator.cc',
  'impl/Zigzag.cc',
  'impl/json/JsonDom.cc',
  'impl/json/JsonIO.cc',
  'impl/parsing/JsonCodec.cc',
  'impl/parsing/ResolvingDecoder.cc',
  'impl/parsing/Symbol.cc',
  'impl/parsing/ValidatingCodec.cc',
)

avro_lib = library(
  'avrocpp',
  sources: avro_src,
  include_directories: avro_inc,
  cpp_args: avro_flags,
  dependencies: avro_deps,
  version: meson.project_version(),
  install: true,
)

install_subdir(
  'include/avro',
  install_dir: get_option('includedir'),
  install_tag: 'devel',
)

avro_dep = declare_dependency(
  include_directories: avro_inc,
  link_with: avro_lib,
  dependencies: avro_public_deps,
)

if get_option('build_executable')
  avrogencpp_exe = executable(
    'avrogencpp',
    sources: ['impl/avrogencpp.cc'],
    cpp_args: ['-DAVRO_VERSION="@0@"'.format(meson.project_version())],
    dependencies: avro_dep,
    install: true,
    install_tag: 'devel',
  )
  meson.override_find_program('avrogencpp', avrogencpp_exe)
endif
