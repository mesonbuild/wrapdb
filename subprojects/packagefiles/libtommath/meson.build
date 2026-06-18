project(
  'libtommath',
  'c',
  version: '1.3.0',
  license: 'Unlicense',
  default_options: [
    'c_std=c99',
  ],
  meson_version: '>=0.63.0',
)

cc = meson.get_compiler('c')

# Override optimization for debug builds to use -Og instead of -O0 to work
# around an issue with clang not optimizing away references to some
# conditionally defined functions with forward references
if get_option('debug') and get_option('optimization') == '0' and cc.get_id() in [
  'clang',
  'clang-cl',
]
  add_project_arguments(
    '-Og',
    language: 'c',
  )
endif

if cc.get_id() in ['msvc', 'clang-cl']
  add_project_arguments(
    '/wd4146',
    '/wd4127',
    '/wd4668',
    '/wd4710',
    '/wd4711',
    '/wd4820',
    '/wd5045',
    '/wd4305',
    '/Ox',
    language: 'c',
  )
endif

if host_machine.system() == 'windows'
  add_project_arguments(
    '-D_CRT_SECURE_NO_WARNINGS',
    '-D_CRT_NONSTDC_NO_DEPRECATE',
    '-D__STDC_WANT_SECURE_LIB__=1',
    '-D_CRT_HAS_CXX17=0',
    language: 'c',
  )
endif

add_project_arguments(
  cc.get_supported_arguments('-Wno-unused-but-set-variable'),
  language: 'c',
)

# Library sources
sources = files(
  'bn_cutoffs.c',
  'bn_deprecated.c',
  'bn_mp_2expt.c',
  'bn_mp_abs.c',
  'bn_mp_add.c',
  'bn_mp_add_d.c',
  'bn_mp_addmod.c',
  'bn_mp_and.c',
  'bn_mp_clamp.c',
  'bn_mp_clear.c',
  'bn_mp_clear_multi.c',
  'bn_mp_cmp.c',
  'bn_mp_cmp_d.c',
  'bn_mp_cmp_mag.c',
  'bn_mp_cnt_lsb.c',
  'bn_mp_complement.c',
  'bn_mp_copy.c',
  'bn_mp_count_bits.c',
  'bn_mp_decr.c',
  'bn_mp_div.c',
  'bn_mp_div_2.c',
  'bn_mp_div_2d.c',
  'bn_mp_div_d.c',
  'bn_mp_dr_is_modulus.c',
  'bn_mp_dr_reduce.c',
  'bn_mp_dr_setup.c',
  'bn_mp_error_to_string.c',
  'bn_mp_exch.c',
  'bn_mp_expt_n.c',
  'bn_mp_exptmod.c',
  'bn_mp_exteuclid.c',
  'bn_mp_fread.c',
  'bn_mp_from_sbin.c',
  'bn_mp_from_ubin.c',
  'bn_mp_fwrite.c',
  'bn_mp_gcd.c',
  'bn_mp_get_double.c',
  'bn_mp_get_i32.c',
  'bn_mp_get_i64.c',
  'bn_mp_get_l.c',
  'bn_mp_get_mag_u32.c',
  'bn_mp_get_mag_u64.c',
  'bn_mp_get_mag_ul.c',
  'bn_mp_grow.c',
  'bn_mp_incr.c',
  'bn_mp_init.c',
  'bn_mp_init_copy.c',
  'bn_mp_init_i32.c',
  'bn_mp_init_i64.c',
  'bn_mp_init_l.c',
  'bn_mp_init_multi.c',
  'bn_mp_init_set.c',
  'bn_mp_init_size.c',
  'bn_mp_init_u32.c',
  'bn_mp_init_u64.c',
  'bn_mp_init_ul.c',
  'bn_mp_invmod.c',
  'bn_mp_is_square.c',
  'bn_mp_iseven.c',
  'bn_mp_isodd.c',
  'bn_mp_kronecker.c',
  'bn_mp_lcm.c',
  'bn_mp_log_n.c',
  'bn_mp_lshd.c',
  'bn_mp_mod.c',
  'bn_mp_mod_2d.c',
  'bn_mp_mod_d.c',
  'bn_mp_montgomery_calc_normalization.c',
  'bn_mp_montgomery_reduce.c',
  'bn_mp_montgomery_setup.c',
  'bn_mp_mul.c',
  'bn_mp_mul_2.c',
  'bn_mp_mul_2d.c',
  'bn_mp_mul_d.c',
  'bn_mp_mulmod.c',
  'bn_mp_neg.c',
  'bn_mp_or.c',
  'bn_mp_pack.c',
  'bn_mp_pack_count.c',
  'bn_mp_prime_fermat.c',
  'bn_mp_prime_frobenius_underwood.c',
  'bn_mp_prime_is_prime.c',
  'bn_mp_prime_miller_rabin.c',
  'bn_mp_prime_next_prime.c',
  'bn_mp_prime_rabin_miller_trials.c',
  'bn_mp_prime_rand.c',
  'bn_mp_prime_strong_lucas_selfridge.c',
  'bn_mp_radix_size.c',
  'bn_mp_radix_smap.c',
  'bn_mp_rand.c',
  'bn_mp_read_radix.c',
  'bn_mp_reduce.c',
  'bn_mp_reduce_2k.c',
  'bn_mp_reduce_2k_l.c',
  'bn_mp_reduce_2k_setup.c',
  'bn_mp_reduce_2k_setup_l.c',
  'bn_mp_reduce_is_2k.c',
  'bn_mp_reduce_is_2k_l.c',
  'bn_mp_reduce_setup.c',
  'bn_mp_root_n.c',
  'bn_mp_rshd.c',
  'bn_mp_sbin_size.c',
  'bn_mp_set.c',
  'bn_mp_set_double.c',
  'bn_mp_set_i32.c',
  'bn_mp_set_i64.c',
  'bn_mp_set_l.c',
  'bn_mp_set_u32.c',
  'bn_mp_set_u64.c',
  'bn_mp_set_ul.c',
  'bn_mp_shrink.c',
  'bn_mp_signed_rsh.c',
  'bn_mp_sqr.c',
  'bn_mp_sqrmod.c',
  'bn_mp_sqrt.c',
  'bn_mp_sqrtmod_prime.c',
  'bn_mp_sub.c',
  'bn_mp_sub_d.c',
  'bn_mp_submod.c',
  'bn_mp_to_radix.c',
  'bn_mp_to_sbin.c',
  'bn_mp_to_ubin.c',
  'bn_mp_ubin_size.c',
  'bn_mp_unpack.c',
  'bn_mp_xor.c',
  'bn_mp_zero.c',
  'bn_prime_tab.c',
  'bn_s_mp_add.c',
  'bn_s_mp_balance_mul.c',
  'bn_s_mp_div_3.c',
  'bn_s_mp_exptmod.c',
  'bn_s_mp_exptmod_fast.c',
  'bn_s_mp_get_bit.c',
  'bn_s_mp_invmod_fast.c',
  'bn_s_mp_invmod_slow.c',
  'bn_s_mp_karatsuba_mul.c',
  'bn_s_mp_karatsuba_sqr.c',
  'bn_s_mp_log.c',
  'bn_s_mp_log_2expt.c',
  'bn_s_mp_log_d.c',
  'bn_s_mp_montgomery_reduce_fast.c',
  'bn_s_mp_mul_digs.c',
  'bn_s_mp_mul_digs_fast.c',
  'bn_s_mp_mul_high_digs.c',
  'bn_s_mp_mul_high_digs_fast.c',
  'bn_s_mp_prime_is_divisible.c',
  'bn_s_mp_rand_jenkins.c',
  'bn_s_mp_rand_platform.c',
  'bn_s_mp_reverse.c',
  'bn_s_mp_sqr.c',
  'bn_s_mp_sqr_fast.c',
  'bn_s_mp_sub.c',
  'bn_s_mp_toom_mul.c',
  'bn_s_mp_toom_sqr.c',
)

inc = include_directories('.')

# Add extra optimization flags to match Makefile and CMake builds
# Note: Meson already adds -O3 when optimization=3 (from buildtype=release)
# We only need to add the flags Meson doesn't add by default
if not get_option('debug')
  add_project_arguments(
    cc.get_supported_arguments('-funroll-loops', '-fomit-frame-pointer'),
    language: 'c',
  )
endif

# Build both static and shared libraries by default
# Users can override with -Ddefault_library=static or -Ddefault_library=shared
libtommath = library(
  'tommath',
  sources,
  install: true,
  include_directories: inc,
  version: meson.project_version(),
  link_args: cc.get_id() in ['msvc', 'clang-cl'] ? [
    # MSVC by default exports no symbols, leading to no .LIB file being generated
    '/DEF:@0@'.format(meson.current_source_dir() / 'libtommath.def'),
  ] : [],
  c_args: cc.get_id() in ['msvc', 'clang-cl'] ? [
    # MSVC defaults to IEEE754 since VS 2010, but doesn't set the macro.
    # Can't use add_project_arguments here because that enables tests that contain
    # literal division by zero, which breaks compilation.
    '/fp:precise',
    '-D__STDC_IEC_559__',
  ] : [],
)

# Install headers
install_headers(files('tommath.h'))

# Generate pkg-config file
pkg = import('pkgconfig')
pkg.generate(
  libtommath,
  name: meson.project_name(),
  description: 'public domain library for manipulating large integer numbers',
  url: 'https://www.libtom.net/LibTomMath/',
)

# Create a dependency object for use by other projects
# This makes the library usable as a Meson subproject
libtommath_dep = declare_dependency(
  link_with: libtommath,
  include_directories: inc,
)

# Make the dependency available to parent projects
meson.override_dependency('libtommath', libtommath_dep)

# Build and run unit tests if requested
if get_option('tests')
  if not meson.can_run_host_binaries()
    error(
      'Cannot run tests: cross-compilating and no host binary helper available',
    )
  endif

  libtommath_for_tests = libtommath
  if cc.get_id() in ['msvc', 'clang-cl']
    if get_option('default_library') == 'shared'
      error('Static library build is required to run tests with MSVC/clang-cl')
    endif
    libtommath_for_tests = libtommath.get_static_lib()
  endif

  tommath_test_exe = executable(
    'tommath_test',
    ['demo/test.c', 'demo/shared.c'],
    link_with: libtommath_for_tests,
    include_directories: inc,
    build_by_default: false,
  )

  mtest_opponent_exe = executable(
    'mtest_opponent',
    ['demo/mtest_opponent.c', 'demo/shared.c'],
    link_with: libtommath_for_tests,
    include_directories: inc,
    build_by_default: false,
  )

  # Build mtest - reference implementation for differential testing
  # Note: mtest.c includes mpi.c directly, so we only compile mtest.c
  # Have to disable optimization when building mpi.c or the test fails
  # due to bugs in mpi.c
  mtest_exe = executable(
    'mtest',
    'mtest/mtest.c',
    include_directories: include_directories('mtest'),
    override_options: ['optimization=0'],
    c_args: cc.get_id() == 'clang-cl' ? [
      # For some reason the optimization=0 override doesn't work properly with clang-cl
      '/Od',
    ] : [],
    build_by_default: false,
  )

  test('tommath_test', tommath_test_exe)

  # Differential test: mtest generates test cases, mtest_opponent validates them
  # Usage: mtest <iterations> | mtest_opponent
  test(
    'mtest_opponent',
    find_program(
      'run_mtest.py',
      native: true,
    ),
    args: [
      mtest_exe.full_path(),
      mtest_opponent_exe.full_path(),
          # Iteration count can be added using --test-args, default is 1000
    ],
    depends: [mtest_exe, mtest_opponent_exe],
    timeout: 30,
    suite: 'differential',
  )
endif

if get_option('benchmarks')
  if not meson.can_run_host_binaries()
    error(
      'Cannot run benchmarks: cross-compilating and no host binary helper available',
    )
  endif

  timing_exe = executable(
    'timing',
    'demo/timing.c',
    link_with: libtommath,
    c_args: ['-DTIMER'],
    include_directories: inc,
    build_by_default: false,
  )

  # Create logs directory in build root for benchmark output (timings binary segfaults without it)
  python_mkdir = [
    find_program(
      'python3',
      native: true,
    ),
    '-c',
    'import os, sys; os.makedirs(sys.argv[1]) if not os.path.exists(sys.argv[1]) else None',
  ]
  run_command(
    python_mkdir,
    meson.project_build_root() / 'logs',
    check: true,
  )
  benchmark(
    'benchmarks',
    timing_exe,
    timeout: 30,
  )
endif

# Documentation target - build PDF manual from LaTeX sources
if get_option('docs')
  # Find LaTeX tools (these may not be installed)
  latex = find_program(
    'latex',
    required: true,
  )
  pdflatex = find_program(
    'pdflatex',
    required: true,
  )
  makeindex = find_program(
    'makeindex',
    required: true,
  )

  custom_target(
    'docs',
    input: 'doc/bn.tex',
    output: '@0@-@1@.pdf'.format(meson.project_name(), meson.project_version()),
    command: [
      find_program(
        'doc/build-manual.py',
        native: true,
      ),
      '@INPUT@',
      '@OUTDIR@',
      '@OUTPUT@',
    ],
    env: environment(
      {
        'LATEX': latex.full_path(),
        'PDFLATEX': pdflatex.full_path(),
        'MAKEINDEX': makeindex.full_path(),
      },
    ),
    console: true,
    install: true,
    install_dir: get_option('datadir') / 'doc' / 'libtommath',
  )
endif
