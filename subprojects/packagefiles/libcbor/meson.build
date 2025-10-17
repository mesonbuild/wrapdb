project(
  'libcbor',
  'c',
  version: '0.13.0',
  meson_version: '>=0.59.0',
  default_options: ['warning_level=3'],
  license: 'MIT',
)

cc = meson.get_compiler('c')

tests_opt = get_option('tests').disable_auto_if(meson.is_subproject())

subdir('src/cbor')

src = [
  'src/cbor.c',
  'src/allocators.c',
  'src/cbor/streaming.c',
  'src/cbor/internal/encoders.c',
  'src/cbor/internal/builder_callbacks.c',
  'src/cbor/internal/loaders.c',
  'src/cbor/internal/memory_utils.c',
  'src/cbor/internal/stack.c',
  'src/cbor/internal/unicode.c',
  'src/cbor/encoding.c',
  'src/cbor/serialization.c',
  'src/cbor/arrays.c',
  'src/cbor/common.c',
  'src/cbor/floats_ctrls.c',
  'src/cbor/bytestrings.c',
  'src/cbor/callbacks.c',
  'src/cbor/strings.c',
  'src/cbor/maps.c',
  'src/cbor/tags.c',
  'src/cbor/ints.c',
]

inc = include_directories('src')

c_args = ['-DCBOR_BUILD=1']

if get_option('default_library') == 'static'
  c_args += ['-DCBOR_BUILD_STATIC=1']
endif

libcbor = library(
  'cbor',
  src,
  config_file,
  c_args: c_args,
  include_directories: inc,
  install: true,
  version: meson.project_version(),
  override_options: ['c_std=c11'],
)

libcbor_dep = declare_dependency(
  link_with: libcbor,
  include_directories: inc,
)

meson.override_dependency('libcbor', libcbor_dep)

headers = [
  config_file,
  'src/cbor/streaming.h',
  'src/cbor/cbor_export.h',
  'src/cbor/data.h',
  'src/cbor/encoding.h',
  'src/cbor/serialization.h',
  'src/cbor/arrays.h',
  'src/cbor/common.h',
  'src/cbor/floats_ctrls.h',
  'src/cbor/bytestrings.h',
  'src/cbor/callbacks.h',
  'src/cbor/strings.h',
  'src/cbor/maps.h',
  'src/cbor/tags.h',
  'src/cbor/ints.h',
]

install_headers('src/cbor.h')
install_headers(
  headers,
  subdir: 'cbor',
)

tests = [
  'test/array_encoders_test.c',
  'test/array_test.c',
  'test/bad_inputs_test.c',
  'test/bytestring_encoders_test.c',
  'test/bytestring_test.c',
  'test/cbor_serialize_test.c',
  'test/cbor_stream_decode_test.c',
  'test/copy_test.c',
  'test/fuzz_test.c',
  'test/map_encoders_test.c',
  'test/map_test.c',
  'test/negint_encoders_test.c',
  'test/negint_test.c',
  'test/pretty_printer_test.c',
  'test/stack_over_limit_test.c',
  'test/string_encoders_test.c',
  'test/string_test.c',
  'test/tag_encoders_test.c',
  'test/tag_test.c',
  'test/uint_encoders_test.c',
  'test/uint_test.c',
]

if host_machine.system() != 'windows'
  tests += [
    'test/callbacks_test.c',
    'test/memory_utils_test.c',
    'test/unicode_test.c',
  ]
endif

if cc.get_id() != 'clang-cl'
  tests += ['test/float_ctrl_encoders_test.c', 'test/float_ctrl_test.c']
endif

cmocka = dependency(
  'cmocka',
  required: tests_opt,
)
m = cc.find_library(
  'm',
  required: false,
)

if cmocka.found()
  libcbor_test = static_library(
    'cbor_test',
    ['test/assertions.c', 'test/stream_expectations.c', 'test/test_allocator.c'],
    include_directories: inc,
    dependencies: [libcbor_dep, cmocka, m],
    c_args: c_args,
    build_by_default: false,
  )

  foreach path : tests
    name = path.split('/')[1].replace('.c', '')
    test_exe = executable(
      name,
      path,
      include_directories: inc,
      link_with: libcbor_test,
      dependencies: [libcbor_dep, cmocka, m],
      override_options: ['c_std=c11'],
      build_by_default: false,
    )

    test(
      name,
      test_exe,
      suite: 'libcbor',
    )
  endforeach
endif
