project(
  'aws-c-cal',
  'c',
  version: '0.9.13',
  meson_version: '>=0.63.0',
  license: 'Apache-2.0',
)

cc = meson.get_compiler('c')
fs = import('fs')
pkg = import('pkgconfig')

tests_opt = get_option('tests').disable_auto_if(meson.is_subproject())

# aws-c-cal doesn't use openssl on windows or darwin, on those platforms it uses the native crypto libraries
# as it's required for compliance with platform policies. On linux and emscripten openssl is used.
may_have_openssl = host_machine.system() in ['linux', 'emscripten']
is_windows = host_machine.system() == 'windows'
is_darwin = host_machine.system() == 'darwin'

byo_crypto = get_option('byo_crypto')
ed25519_everywhere = get_option('ed25519_everywhere').disable_auto_if(
  not may_have_openssl,
)

c_args = ['-DAWS_CAL_EXPORTS=1']

public_c_args = []
if (
  get_option('default_library') == 'shared'
  and host_machine.system() == 'windows'
) or host_machine.system() != 'windows'
  public_c_args += ['-DAWS_CAL_USE_IMPORT_EXPORT=1']
endif

if host_machine.system() == 'windows' and host_machine.cpu_family() in [
  'x86',
  'aarch64',
]
  error('unsupported architecture: only x86_64 is supported on Windows')
endif

aws_c_common_dep = dependency('aws-c-common')
libcrypto_dep = dependency(
  'openssl',
  version: '>=1.1',
  required: not byo_crypto.allowed(),
)

ncrypt = cc.find_library(
  'ncrypt',
  required: false,
)

foundation = dependency(
  'appleframeworks',
  modules: ['Security', 'CoreFoundation'],
  required: false,
)

if is_windows
  byo_crypto = byo_crypto.disable_auto_if(ncrypt.found())
endif

if is_darwin
  byo_crypto = byo_crypto.disable_auto_if(foundation.found())
endif

src = files(
  'source/cal.c',
  'source/der.c',
  'source/ecc.c',
  'source/ed25519.c',
  'source/hash.c',
  'source/hkdf.c',
  'source/hmac.c',
  'source/rsa.c',
  'source/shared/ref_hkdf.c',
  'source/symmetric_cipher.c',
)

if byo_crypto.allowed()
  c_args += ['-DBYO_CRYPTO=1']
endif

if libcrypto_dep.found()
  src += files('source/shared/ed25519.c', 'source/shared/lccrypto_common.c')
  c_args += ['-DAWS_USE_LIBCRYPTO_TO_SUPPORT_ED25519_EVERYWHERE']
else
  src += files('source/ed25519.c', 'source/shared/ed25519_noop.c')
endif

if not byo_crypto.allowed()
  if host_machine.system() in ['cygwin', 'windows']
    src += files(
      'source/windows/bcrypt_aes.c',
      'source/windows/bcrypt_ecc.c',
      'source/windows/bcrypt_hash.c',
      'source/windows/bcrypt_hmac.c',
      'source/windows/bcrypt_platform_init.c',
      'source/windows/bcrypt_rsa.c',
    )
  elif host_machine.system() == 'darwin'
    src += files(
      'source/darwin/commoncrypto_aes.c',
      'source/darwin/commoncrypto_hmac.c',
      'source/darwin/commoncrypto_md5.c',
      'source/darwin/commoncrypto_platform_init.c',
      'source/darwin/commoncrypto_sha1.c',
      'source/darwin/commoncrypto_sha256.c',
      'source/darwin/commoncrypto_sha512.c',
      'source/darwin/securityframework_ecc.c',
      'source/darwin/securityframework_rsa.c',
    )
  elif host_machine.system() in ['linux', 'emscripten']
    src += files(
      'source/unix/openssl_aes.c',
      'source/unix/openssl_platform_init.c',
      'source/unix/openssl_rsa.c',
      'source/unix/opensslcrypto_ecc.c',
      'source/unix/opensslcrypto_hash.c',
      'source/unix/opensslcrypto_hmac.c',
    )
  endif
endif

inc = include_directories('include')

libaws_c_cal = library(
  'aws-c-cal',
  src,
  c_args: c_args + public_c_args,
  dependencies: [aws_c_common_dep, libcrypto_dep, ncrypt, foundation],
  include_directories: inc,
  install: true,
  version: meson.project_version(),
  gnu_symbol_visibility: 'hidden',
)

aws_c_cal_dep = declare_dependency(
  link_with: libaws_c_cal,
  include_directories: inc,
  dependencies: aws_c_common_dep,
  compile_args: public_c_args,
)

meson.override_dependency('aws-c-cal', aws_c_cal_dep)

pkg.generate(
  libaws_c_cal,
  extra_cflags: public_c_args,
  description: 'Aws Crypto Abstraction Layer: Cross-Platform, C99 wrapper for cryptography primitives.',
)

subdir('include')

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
    'tests/aes256_test.c',
    'tests/der_test.c',
    'tests/ecc_test.c',
    'tests/ed25519_test.c',
    'tests/hkdf_test.c',
    'tests/md5_test.c',
    'tests/rsa_test.c',
    'tests/sha1_test.c',
    'tests/sha256_hmac_test.c',
    'tests/sha256_test.c',
    'tests/sha512_hmac_test.c',
    'tests/sha512_test.c',
  )

  libtestcases = static_library(
    'aws_c_cal_testcases',
    test_src,
    dependencies: [aws_c_cal_dep],
    c_args: ['-DAWS_UNSTABLE_TESTING_API=1'],
    include_directories: inc,
    build_by_default: false,
  )

  # implements an approximation of cmakes create_test_sourcelist
  test_harness_src = custom_target(
    'generate_test_harness',
    input: 'tests.txt',
    output: 'test_harness.c',
    command: [generate_tests, '@INPUT@', '@OUTPUT@'],
  )

  test_harness = executable(
    'aws-c-cal-tests',
    test_harness_src,
    dependencies: [aws_c_cal_dep],
    link_with: [libtestcases],
    c_args: ['-DAWS_UNSTABLE_TESTING_API=1'],
    include_directories: inc,
    build_by_default: false,
  )

  names = fs.read('tests.txt').split('\n')

  foreach name : names
    test(
      name,
      run_test,
      args: [test_harness, name],
      workdir: meson.current_source_dir(),
      timeout: 600,
    )
  endforeach
endif
