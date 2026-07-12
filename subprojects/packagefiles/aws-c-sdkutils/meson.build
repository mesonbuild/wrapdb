project(
  'aws-c-sdkutils',
  'c',
  version: '0.2.4',
  license: 'Apache-2.0',
  meson_version: '>=0.64.0',
)

tests_opt = get_option('tests').disable_auto_if(meson.is_subproject())

pkg = import('pkgconfig')
fs = import('fs')

aws_c_common_dep = dependency('aws-c-common')

deps = [aws_c_common_dep]

src = files(
  'source/aws_profile.c',
  'source/endpoints_regex.c',
  'source/endpoints_rule_engine.c',
  'source/endpoints_ruleset.c',
  'source/endpoints_standard_lib.c',
  'source/endpoints_types_impl.c',
  'source/endpoints_util.c',
  'source/partitions.c',
  'source/resource_name.c',
  'source/sdkutils.c',
)

subdir('include')

inc = include_directories('include')

c_args = ['-DAWS_SDKUTILS_EXPORTS=1']
public_c_args = []
if (
  get_option('default_library') == 'shared'
  and host_machine.system() == 'windows'
) or host_machine.system() != 'windows'
  public_c_args += ['-DAWS_SDKUTILS_USE_IMPORT_EXPORT=1']
endif

libaws_c_sdkutils = library(
  'aws-c-sdkutils',
  src,
  c_args: c_args + public_c_args,
  include_directories: inc,
  dependencies: deps,
  install: true,
  version: meson.project_version(),
  gnu_symbol_visibility: 'hidden',
)

aws_c_sdkutils_dep = declare_dependency(
  include_directories: inc,
  link_with: libaws_c_sdkutils,
  dependencies: deps,
  compile_args: public_c_args,
)

meson.override_dependency('aws-c-sdkutils', aws_c_sdkutils_dep)

pkg.generate(
  libaws_c_sdkutils,
  extra_cflags: public_c_args,
  description: 'C99 library implementing AWS SDK specific utilities. Includes utilities for ARN parsing, reading AWS profiles, etc...',
)

generate_tests = find_program(
  'generate_tests.py',
  required: tests_opt,
)
run_test = find_program(
  'run_test.py',
  required: tests_opt,
)

if generate_tests.found() and run_test.found()
  # aws-c-sdkutils uses an obscure cmake feature `create_test_sourcelist` to generate test harnesses
  # this is a best effort approximation of that behavior
  test_harness_src = custom_target(
    'generate_test_harness',
    input: 'tests.txt',
    output: 'test_harness.c',
    command: [generate_tests, '@INPUT@', '@OUTPUT@'],
  )

  names = fs.read('tests.txt').split('\n')

  subdir('tests')
endif
