project(
  'mldsa-native',
  'c',
  version: '1.0.0',
  meson_version: '>=1.1.0',
  license: 'ISC OR MIT',
  default_options: [
    'warning_level=3',
    'c_std=c99',
    'default_library=static',
  ],
)

cc = meson.get_compiler('c')

has_asm = host_machine.cpu_family() in ['x86_64', 'aarch64'] and cc.get_id() != 'msvc'

tests_opt = get_option('tests').disable_auto_if(meson.is_subproject())
rand_opt = get_option('byo_rand')
security_level_opt = get_option('security_level')
asm_opt = get_option('asm').enable_auto_if(has_asm).require(
  has_asm,
  error_message: 'Assembly implementations are only available for x86_64 and aarch64 architectures.',
)

if host_machine.system() == 'windows' and get_option('default_library') == 'shared'
  error('Building mldsa-native as a shared library on Windows is not supported.')
endif

private_c_args = []
rand_c_args = []

private_c_args += cc.get_supported_arguments('-Wno-unused-function')

if not rand_opt
  rand_c_args += ['-DMLD_CONFIG_NO_RANDOMIZED_API=1']
endif

if security_level_opt == 'ML-DSA-44'
  private_c_args += ['-DMLD_CONFIG_PARAMETER_SET=44']
elif security_level_opt == 'ML-DSA-65'
  private_c_args += ['-DMLD_CONFIG_PARAMETER_SET=65']
elif security_level_opt == 'ML-DSA-87'
  private_c_args += ['-DMLD_CONFIG_PARAMETER_SET=87']
endif

if asm_opt.disabled()
  private_c_args += ['-DMLD_CONFIG_NO_ASM=1']
else
  private_c_args += [
    '-DMLD_CONFIG_USE_NATIVE_BACKEND_ARITH=1',
    '-DMLD_CONFIG_USE_NATIVE_BACKEND_FIPS202=1',
  ]
endif

if cc.get_id() in ['gcc', 'clang'] and asm_opt.disabled()
  private_c_args += ['-DMLD_HAVE_INLINE_ASM=1']
endif

install_headers(
  'mldsa/mldsa_native.h',
  install_dir: get_option('includedir') / 'mldsa',
)

aarch64_asm = files(
  'mldsa/src/fips202/native/aarch64/src/keccak_f1600_x1_scalar_asm.S',
  'mldsa/src/fips202/native/aarch64/src/keccak_f1600_x1_v84a_asm.S',
  'mldsa/src/fips202/native/aarch64/src/keccak_f1600_x2_v84a_asm.S',
  'mldsa/src/fips202/native/aarch64/src/keccak_f1600_x4_v8a_scalar_hybrid_asm.S',
  'mldsa/src/fips202/native/aarch64/src/keccak_f1600_x4_v8a_v84a_scalar_hybrid_asm.S',
  'mldsa/src/native/aarch64/src/intt.S',
  'mldsa/src/native/aarch64/src/mld_polyvecl_pointwise_acc_montgomery_l4.S',
  'mldsa/src/native/aarch64/src/mld_polyvecl_pointwise_acc_montgomery_l5.S',
  'mldsa/src/native/aarch64/src/mld_polyvecl_pointwise_acc_montgomery_l7.S',
  'mldsa/src/native/aarch64/src/ntt.S',
  'mldsa/src/native/aarch64/src/pointwise_montgomery.S',
  'mldsa/src/native/aarch64/src/poly_caddq_asm.S',
  'mldsa/src/native/aarch64/src/poly_chknorm_asm.S',
  'mldsa/src/native/aarch64/src/poly_decompose_32_asm.S',
  'mldsa/src/native/aarch64/src/poly_decompose_88_asm.S',
  'mldsa/src/native/aarch64/src/poly_use_hint_32_asm.S',
  'mldsa/src/native/aarch64/src/poly_use_hint_88_asm.S',
  'mldsa/src/native/aarch64/src/polyz_unpack_17_asm.S',
  'mldsa/src/native/aarch64/src/polyz_unpack_19_asm.S',
  'mldsa/src/native/aarch64/src/rej_uniform_asm.S',
  'mldsa/src/native/aarch64/src/rej_uniform_eta2_asm.S',
  'mldsa/src/native/aarch64/src/rej_uniform_eta4_asm.S',
)

x86_asm = files(
  'mldsa/src/native/x86_64/src/intt.S',
  'mldsa/src/native/x86_64/src/ntt.S',
  'mldsa/src/native/x86_64/src/nttunpack.S',
  'mldsa/src/native/x86_64/src/pointwise.S',
  'mldsa/src/native/x86_64/src/pointwise_acc_l4.S',
  'mldsa/src/native/x86_64/src/pointwise_acc_l5.S',
  'mldsa/src/native/x86_64/src/pointwise_acc_l7.S',
)

aarch64_src = files(
  'mldsa/src/fips202/native/aarch64/src/keccakf1600_round_constants.c',
  'mldsa/src/native/aarch64/src/aarch64_zetas.c',
  'mldsa/src/native/aarch64/src/polyz_unpack_table.c',
  'mldsa/src/native/aarch64/src/rej_uniform_eta_table.c',
  'mldsa/src/native/aarch64/src/rej_uniform_table.c',
)

x86_src = files(
  'mldsa/src/fips202/native/x86_64/src/KeccakP_1600_times4_SIMD256.c',
  'mldsa/src/native/x86_64/src/consts.c',
  'mldsa/src/native/x86_64/src/poly_caddq_avx2.c',
  'mldsa/src/native/x86_64/src/poly_chknorm_avx2.c',
  'mldsa/src/native/x86_64/src/poly_decompose_32_avx2.c',
  'mldsa/src/native/x86_64/src/poly_decompose_88_avx2.c',
  'mldsa/src/native/x86_64/src/poly_use_hint_32_avx2.c',
  'mldsa/src/native/x86_64/src/poly_use_hint_88_avx2.c',
  'mldsa/src/native/x86_64/src/polyz_unpack_17_avx2.c',
  'mldsa/src/native/x86_64/src/polyz_unpack_19_avx2.c',
  'mldsa/src/native/x86_64/src/rej_uniform_avx2.c',
  'mldsa/src/native/x86_64/src/rej_uniform_eta2_avx2.c',
  'mldsa/src/native/x86_64/src/rej_uniform_eta4_avx2.c',
  'mldsa/src/native/x86_64/src/rej_uniform_table.c',
)

src = files(
  'mldsa/src/ct.c',
  'mldsa/src/debug.c',
  'mldsa/src/fips202/fips202.c',
  'mldsa/src/fips202/fips202x4.c',
  'mldsa/src/fips202/keccakf1600.c',
  'mldsa/src/ntt.c',
  'mldsa/src/packing.c',
  'mldsa/src/poly.c',
  'mldsa/src/poly_kl.c',
  'mldsa/src/polyvec.c',
  'mldsa/src/prehash.c',
  'mldsa/src/sign.c',
)

arch_src = []
if host_machine.cpu_family() == 'aarch64'
  arch_src += aarch64_src
elif host_machine.cpu_family() == 'x86_64'
  arch_src += x86_src
endif

arch_asm = []
if host_machine.cpu_family() == 'aarch64'
  arch_asm += aarch64_asm
elif host_machine.cpu_family() == 'x86_64'
  arch_asm += x86_asm
endif

mldsa_src = src + arch_src
if asm_opt.allowed()
  mldsa_src += arch_asm
endif

inc = include_directories('mldsa')

libmldsa_native = library(
  'mldsa-native',
  mldsa_src,
  c_args: [private_c_args, rand_c_args],
  install: true,
  include_directories: inc,
  version: meson.project_version(),
)

mldsa_native_dep = declare_dependency(
  link_with: libmldsa_native,
  include_directories: inc,
)

meson.override_dependency(
  'mldsa-native',
  mldsa_native_dep,
)

testcases = {
  'test_mldsa': {
    'sources': files('test/test_mldsa.c'),
  },
}

notrandombytes_src = files('test/notrandombytes/notrandombytes.c')

if tests_opt.enabled()
  # Tests provide their own randombytes implementation that returns
  # deterministic data for testing purposes.
  libmldsa_native_test = library(
    'mldsa-native-test',
    mldsa_src,
    notrandombytes_src,
    c_args: private_c_args,
    include_directories: inc,
  )

  foreach testname, kwargs : testcases
    exe = executable(
      testname,
      kwargs: kwargs,
      link_with: libmldsa_native_test,
      include_directories: inc,
    )
    test(testname, exe)
  endforeach
endif
