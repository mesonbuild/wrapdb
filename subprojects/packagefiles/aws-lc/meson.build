project(
  'aws-lc',
  'c',
  version: '1.67.0',
  license: 'OpenSSL AND ISC AND SSLeay-standalone AND MIT AND BSD-3-Clause AND Apache-2.0',
  default_options: [
    'warning_level=3',
    'cpp_std=c++17',
    'c_std=c11',
    # Obscure behaviour of the VSCRT is that the version linked against
    # changes the behaviour of abort. If the debug version is linked
    # then abort will popup a dialog which blocks CI.
    'b_vscrt=md',
  ],
  meson_version: '>=1.4.0',
)

fs = import('fs')
cc = meson.get_compiler('c')

b_sanitize = get_option('b_sanitize')
default_library = get_option('default_library')
msan = b_sanitize.contains('memory') or b_sanitize.contains('address')
is_windows_like = host_machine.system() in ['windows', 'cygwin']
is_intel = host_machine.cpu_family() in ['x86', 'x86_64']
is_win_intel = is_windows_like and is_intel

tests_opt = get_option('tests').disable_auto_if(meson.is_subproject())
libssl_opt = get_option('libssl')
fips_opt = get_option('fips').disable_auto_if(
  (
    is_windows_like
    and default_library == 'static'
  ) or (
    cc.get_id() == 'msvc'
    and not is_intel
  ) or (
    cc.get_id() == 'clang-cl'
    and host_machine.cpu_family() == 'aarch64'
  ) or (
    host_machine.system() == 'windows'
    and not is_intel
    and cc.get_id() != 'clang-cl'
  ) or (
    # While this might technically be possible, I don't have access to a msys2 environment
    # with clang installed to test this.
    host_machine.system() == 'windows'
    and cc.get_id() == 'clang'
  ) or (
    # AWS-LC upstream does not support FIPS on Win-x86 builds.
    # They might be possible, but as they're not officially supported
    # best to not leave it on by default.
    host_machine.system() == 'windows'
    and host_machine.cpu_family() == 'x86'
  )
  # upstream has support for FIPS on macOS, but I don't own a macbook so cannot test it.
  # Disabled by default so that CI passes.
or host_machine.system() == 'darwin' or msan,
)

asm_opt = get_option('asm').disable_auto_if(
  (cc.get_id() == 'msvc' and not is_intel) or (
    cc.get_id() == 'clang-cl'
    and host_machine.cpu_family() == 'aarch64'
  ),
).enable_auto_if(
  fips_opt.allowed(),
)
openssl_override_opt = get_option('openssl-override')

fips_opt = fips_opt.require(
  not msan,
  error_message: 'Memory sanitizer and Address sanitizer are not compatible with FIPS mode.',
)

if is_windows_like or host_machine.system() == 'darwin'
  fips_opt = fips_opt.require(
    default_library == 'shared',
    error_message: 'FIPS cannot be delocated on Windows & macOS, so aws-lc must be built as a shared library when FIPS is enabled.',
  )
endif

if host_machine.system() == 'windows'
  asm_opt = asm_opt.disable_auto_if(not is_intel and cc.get_id() != 'clang-cl')
  asm_opt = asm_opt.require(
    is_intel or cc.get_id() == 'clang-cl',
    error_message: 'Assembly is only supported on MSVC + Windows for x86 and x86_64 builds.',
  )
endif

go = find_program(
  'go',
  required: fips_opt,
  native: true,
)
perl = find_program(
  'perl',
  required: fips_opt,
  native: true,
)
jitterentropy = dependency(
  'jitterentropy',
  required: fips_opt,
)

fips_opt = fips_opt.require(
  asm_opt.allowed(),
  error_message: 'Assembly must be enabled to build aws-lc in FIPS mode.',
)
fips_opt = fips_opt.require(
  go.found(),
  error_message: 'Go toolchain is required to build aws-lc in FIPS mode.',
)
fips_opt = fips_opt.require(
  perl.found(),
  error_message: 'Perl is required to build aws-lc in FIPS mode.',
)
fips_opt = fips_opt.require(
  jitterentropy.found(),
  error_message: 'Jitterentropy library is required to build aws-lc in FIPS mode.',
)

inject_hash_src = files('util/fipstools/inject_hash/inject_hash.go')
capture_hash_src = files('util/fipstools/capture_hash/capture_hash.go')
fips_delocate_src = files('util/fipstools/delocate/delocate.go')

if default_library == 'static'
  run_go = find_program(
    'run_go.sh',
    required: fips_opt,
    native: true,
  )
endif

custom_target_sh = find_program(
  'inject_hash_wrapper.sh',
  required: fips_opt,
  native: true,
)

convert_archive_sh = find_program(
  'convert_archive.sh',
  required: fips_opt,
  native: true,
)

capture_hash_wrapper_sh = find_program(
  host_machine.system() == 'windows' ? 'capture_hash_wrapper.bat' : 'capture_hash_wrapper.sh',
  required: fips_opt,
  native: true,
)

# On win-x86 and win-x86_64 always use nasm for assembly files.
needs_nasm = asm_opt.allowed() and is_win_intel

if needs_nasm
  nasm = find_program(
    'nasm',
    native: true,
  )
endif

if tests_opt.allowed() or libssl_opt.allowed()
  add_languages(
    'cpp',
    native: false,
  )
endif

gtest_dep = dependency(
  'gtest',
  required: tests_opt,
  default_options: [
    # Need to line up with aws-lc's b_vscrt option to avoid msvcrt debug mismatches.
    'b_vscrt=md',
  ],
)

wsa2_dep = cc.find_library(
  'ws2_32',
  required: host_machine.system() == 'windows',
)

inc = include_directories('include')

common_args = cc.get_supported_arguments(
  '-fno-common',
  '-Wno-unused-parameter',
  '-Wno-overlength-strings',
  '-Wno-extra-semi',
  '-Wno-pedantic',
  '/wd4100',
  '/wd4244',
  '/wd4267',
  '/wd4702',
  '/wd4152',
  '/wd4146',
  '/wd4996',
  '/wd4127',
  '/wd4834',
)

subdir('include/openssl')

subdir('third_party/s2n-bignum')

# Provides asm_src, fips_asm_src, err_data, test_asm_src, and crypto_test_data
subdir('generated-src')

subdir('crypto')

if libssl_opt.allowed()
  subdir('ssl')
endif

if openssl_override_opt
  meson.override_dependency('libcrypto', libcrypto_dep)

  if libssl_opt.allowed()
    meson.override_dependency('libssl', libssl_dep)
  endif

  if libssl_opt.allowed()
    awslc_dep = declare_dependency(
      dependencies: [libcrypto_dep, libssl_dep],
      include_directories: inc,
      variables: ['OPENSSL_IS_AWS_LC=1'],
    )
  else
    awslc_dep = declare_dependency(
      dependencies: [libcrypto_dep],
      include_directories: inc,
      variables: ['OPENSSL_IS_AWS_LC=1'],
    )
  endif

  meson.override_dependency('openssl', awslc_dep)
endif

summary(
  {
    'Tests': tests_opt,
    'libssl': libssl_opt,
    'FIPS mode': fips_opt,
    'Assembly': asm_opt,
    'OpenSSL override': openssl_override_opt,
    'System': host_machine.system(),
  },
)
