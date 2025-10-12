project(
  'base64',
  'c',
  version: '0.5.2',
  license: 'BSD-2-Clause',
  meson_version: '>=0.59.0',
  default_options: ['warning_level=3'],
)

cc = meson.get_compiler('c')
tests_opt = get_option('tests').disable_auto_if(meson.is_subproject())

c_args = []
config = configuration_data()

if host_machine.cpu_family() in ['x86', 'x86_64']
  features = {
    'SSSE3': 'ssse3',
    'SSE41': 'sse4.1',
    'SSE42': 'sse4.2',
    'AVX': 'avx',
    'AVX2': 'avx2',
  }
  foreach feature, flag : features
    if cc.has_argument('-m' + flag)
      config.set('HAVE_' + feature, 1)
      c_args += ['-DHAVE_' + feature, '-m' + flag]
    endif
  endforeach
elif host_machine.cpu_family() == 'arm'
  config.set('HAVE_NEON32', 1)
  c_args += ['-DHAVE_NEON32']
elif host_machine.cpu_family() == 'aarch64'
  config.set('HAVE_NEON64', 1)
  c_args += ['-DHAVE_NEON64']
endif

cfg = configure_file(
  output: 'config.h',
  configuration: config,
)

src = [
  cfg,
  'lib/lib.c',
  'lib/codec_choose.c',
  'lib/tables/tables.c',
  'lib/arch/generic/codec.c',
  'lib/arch/ssse3/codec.c',
  'lib/arch/sse41/codec.c',
  'lib/arch/sse42/codec.c',
  'lib/arch/avx/codec.c',
  'lib/arch/avx2/codec.c',
  'lib/arch/avx512/codec.c',
  'lib/arch/neon32/codec.c',
  'lib/arch/neon64/codec.c',
]

inc = include_directories('include')

libbase64 = library(
  'base64',
  src,
  c_args: c_args,
  include_directories: inc,
  install: true,
  version: meson.project_version(),
  override_options: ['c_std=c99'],
)

base64_dep = declare_dependency(
  include_directories: inc,
  link_with: libbase64,
)

meson.override_dependency('base64', base64_dep)

if tests_opt.allowed()
  test_src = ['test/codec_supported.c', 'test/test_base64.c']

  test_exe = executable(
    'base64-test',
    test_src,
    include_directories: inc,
    link_with: libbase64,
    override_options: ['c_std=c99'],
    build_by_default: false,
  )
  test('base64', test_exe)
endif
