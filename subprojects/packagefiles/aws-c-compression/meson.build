project(
  'aws-c-compression',
  'c',
  version: '0.3.1',
  meson_version: '>=0.63.0',
  license: 'Apache-2.0',
)

pkg = import('pkgconfig')
fs = import('fs')

tests_opt = get_option('tests').disable_auto_if(meson.is_subproject())

public_c_args = ['-DAWS_COMPRESSION_USE_IMPORT_EXPORT=1']
c_args = ['-DAWS_COMPRESSION_EXPORTS=1']

if host_machine.system() == 'windows'
  public_c_args += ['-DUSE_WINDOWS_DLL_SEMANTICS=1']
endif

aws_c_common_dep = dependency('aws-c-common')

src = files('source/compression.c', 'source/huffman.c')

inc = include_directories('include')

libaws_c_compression = library(
  'aws-c-compression',
  src,
  c_args: c_args + public_c_args,
  dependencies: aws_c_common_dep,
  include_directories: inc,
  install: true,
  gnu_symbol_visibility: 'hidden',
)

aws_c_compression_dep = declare_dependency(
  link_with: libaws_c_compression,
  dependencies: aws_c_common_dep,
  include_directories: inc,
  compile_args: public_c_args,
)

meson.override_dependency('aws-c-compression', aws_c_compression_dep)

pkg.generate(
  libaws_c_compression,
  extra_cflags: public_c_args,
  description: 'C99 implementation of huffman encoding/decoding',
)

subdir('include')

huffman_generator_src = files('source/huffman_generator/generator.c')

huffman_generator = executable(
  'aws-c-common-huffman-generator',
  huffman_generator_src,
  install: true,
)

meson.override_find_program('aws-c-common-huffman-generator', huffman_generator)

generate_tests = find_program(
  'generate_tests.py',
  required: tests_opt,
)
run_test = find_program(
  'run_test.py',
  required: tests_opt,
)
if generate_tests.found() and run_test.found()
  test_src = files(
    'source/huffman_testing.c',
    'tests/huffman_test.c',
    'tests/library_test.c',
    'tests/test_huffman_static.c',
  )

  libtestcases = static_library(
    'aws_c_compression_testcases',
    test_src,
    dependencies: [aws_c_compression_dep],
    include_directories: inc,
    build_by_default: false,
  )

  test_harness_src = custom_target(
    'generate_test_harness',
    input: 'tests.txt',
    output: 'test_harness.c',
    command: [generate_tests, '@INPUT@', '@OUTPUT@'],
  )

  test_harness = executable(
    'aws-c-compression-tests',
    test_harness_src,
    dependencies: [aws_c_compression_dep],
    link_with: [libtestcases],
    include_directories: inc,
    build_by_default: false,
  )

  names = fs.read('tests.txt').split('\n')

  foreach name : names
    test(
      name,
      run_test,
      args: [test_harness, name],
      timeout: 600,
    )
  endforeach
endif
