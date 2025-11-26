project(
  's2n-bignum',
  'c',
  version: '1.0.0',
  license: 'Apache-2.0 OR ISC or MIT-0',
  meson_version: '>=1.3.2',
)

pkg = import('pkgconfig')

cpu = host_machine.cpu_family()
cc = meson.get_compiler('c')

inc = include_directories('include')

tests_opt = get_option('tests').disable_auto_if(meson.is_subproject())

c_args = []

# Only 64 bit architectures are supported
if cpu == 'x86_64'
  subdir('x86')
elif cpu == 'aarch64'
  subdir('arm')
else
  error('unsupported architecture @0@'.format(host_machine.cpu_family()))
endif

src = []

tr = find_program('tr')

preprocess_args = ['-xassembler-with-cpp']
preprocess_args += cc.get_supported_arguments(
  '-Wno-unused-command-line-argument',
  '-DWINDOWS_ABI=0',
)

# Source files need to be preprocessed before compiling
foreach asm : unprocessed_src
  # First fed through the preprocessor to expand macros and includes
  name = asm.replace('/', '_').replace('.S', '')
  preprocessed = cc.preprocess(
    asm,
    output: '@PLAINNAME@',
    include_directories: inc,
    compile_args: preprocess_args,
  )
  # Then fed into 'tr' to convert ';' to newlines, some assemblers require this
  finalized = custom_target(
    'finalize_' + name,
    command: [tr, ';', '\n'],
    feed: true,
    capture: true,
    input: preprocessed,
    output: asm.replace('/', '_'),
  )

  src += [finalized]
endforeach

if host_machine.system() == 'darwin' and cc.get_id() == 'clang' and host_machine.cpu_family() == 'aarch64'
  c_args += ['-arch', 'arm64', '-march=armv8.2-a+sha3']
endif

if host_machine.system() == 'windows'
  error('s2n-bignum does not support Windows builds')
endif

s2n_bignum_lib = library(
  's2nbignum',
  src,
  c_args: c_args,
  include_directories: inc,
  install: true,
)

s2n_bignum_dep = declare_dependency(
  include_directories: inc,
  link_with: s2n_bignum_lib,
)

meson.override_dependency('s2n-bignum', s2n_bignum_dep)

install_headers('include/s2n-bignum.h')

pkg.generate(s2n_bignum_lib)

if tests_opt.allowed()
  m_dep = cc.find_library(
    'm',
    required: false,
  )

  test_exe = executable(
    's2n-bignum-tests',
    'tests/test.c',
    dependencies: [s2n_bignum_dep, m_dep],
    build_by_default: false,
  )

  test('s2n-bignum tests', test_exe)
endif
