project(
  'avro-cpp',
  'cpp',
  version: '1.12.1',
  license: 'Apache-2.0',
  meson_version: '>=0.60.0',
)

override_cpp = 'cpp_std=c++17'

avro_flags = []
avro_deps = []
avro_public_flags = []
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
  required: get_option('snappy'),
)
if snappy_dep.found()
  avro_flags += '-DSNAPPY_CODEC_AVAILABLE'
  avro_deps += snappy_dep
endif

zstd_dep = dependency(
  'libzstd',
  required: get_option('zstd'),
)
if zstd_dep.found()
  avro_flags += '-DZSTD_CODEC_AVAILABLE'
  avro_deps += zstd_dep
endif

# Set static and shared flags manually since Meson 1.3.0 is still too new
avro_flags += '-DAVRO_SOURCE'
if get_option('default_library') == 'shared'
  avro_flags += '-DAVRO_DYN_LINK'
  avro_public_flags += '-DAVRO_DYN_LINK'
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
  override_options: override_cpp,
  gnu_symbol_visibility: 'hidden',  # TODO: requires a release with https://github.com/apache/avro/pull/3600
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
  compile_args: avro_public_flags,
  dependencies: avro_public_deps,
)
meson.override_dependency('avro-cpp', avro_dep)

avro_requires = []
foreach dep : avro_public_deps
  avro_requires += dep.name()
endforeach
import('pkgconfig').generate(
  avro_lib,
  name: meson.project_name(),
  description: 'C++ library for parsing Avro data',
  url: 'https://avro.apache.org/',
  extra_cflags: avro_public_flags,
  requires: avro_requires,
)

# Check first if tests should be built
boost_dep = dependency(
  'boost',
  modules: ['test'],
  required: get_option('tests'),
)
tests_enabled = boost_dep.found()

# Emulate enabled_if since Meson 1.1.0 is still too new
avrogencpp_enabled = get_option('avrogencpp').enabled() or (
  tests_enabled
  and get_option(
  'avrogencpp',
  ).auto()
)
if tests_enabled and not avrogencpp_enabled
  error('Tests require avrogencpp')
endif

if avrogencpp_enabled
  avrogencpp_exe = executable(
    'avrogencpp',
    sources: ['impl/avrogencpp.cc'],
    cpp_args: ['-DAVRO_VERSION="@0@"'.format(meson.project_version())],
    dependencies: avro_dep,
    override_options: override_cpp,
    install: true,
    install_tag: 'devel',
  )
  meson.override_find_program('avrogencpp', avrogencpp_exe)
endif

if tests_enabled
  js_ns = {
    'big_union': 'big_union',
    'bigrecord': 'testgen',
    'bigrecord_r': 'testgen_r',
    'cpp_reserved_words': 'cppres',
    'cpp_reserved_words_union_typedef': 'cppres_union',
    'tweet': 'testgen3',
    'union_array_union': 'uau',
    'union_map_union': 'umu',
    'union_conflict': 'uc',
    'union_empty_record': 'uer',
    'union_redundant_types': 'redundant_types',
  }
  js_hh = {}
  foreach file, ns : js_ns
    file_hh = custom_target(
      file + '_hh',
      output: file + '.hh',
      command: [
        avrogencpp_exe,
        '-p',
        '-',
        '-i',
        '@CURRENT_SOURCE_DIR@' / 'jsonschemas' / file,
        '-o',
        '@OUTPUT@',
        '-n',
        ns,
      ],
    )
    js_hh += {
      file: file_hh,
    }
  endforeach

  unittests = {
    'AvrogencppTestReservedWords': [
      js_hh['cpp_reserved_words'],
      js_hh['cpp_reserved_words_union_typedef'],
    ],
    'AvrogencppTests': [
      js_hh['big_union'],
      js_hh['bigrecord'],
      js_hh['bigrecord_r'],
      js_hh['tweet'],
      js_hh['union_array_union'],
      js_hh['union_map_union'],
      js_hh['union_conflict'],
      js_hh['union_empty_record'],
      js_hh['union_redundant_types'],
    ],
    'buffertest': [],
    'CodecTests': [],
    'CommonsSchemasTests': [],
    'CompilerTests': [],
    'DataFileTests': [],
    'JsonTests': [],
    'LargeSchemaTests': [],
    'SchemaTests': [],
    'SpecificTests': [],
    'StreamTests': [],
    'unittest': [],
  }
  foreach unittest, js_hh_deps : unittests
    test_exe = executable(
      unittest,
      sources: ['test/@0@.cc'.format(unittest)] + js_hh_deps,
      dependencies: [avro_dep, boost_dep],
      override_options: override_cpp,
      build_by_default: false,
    )
    test(
      unittest,
      test_exe,
      workdir: meson.current_source_dir(),
    )
  endforeach
endif
