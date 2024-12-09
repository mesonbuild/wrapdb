# Conventions:
# _ implies that the variables are not meant to be used outside here
# Optionals are applied from the top-level meson_options.txt
# They are declared at the top
# Typically derived from (in order) the CMakeLists.txt and Makefiles
#
# Installation:
# meson setup build --buildtype release
# meson compile -C build
# meson install --prefix=$HOME/.local/lapack
#
# NOTE: This is still a work in progress, the Makefiles are canonical
project('OpenBLAS', ['c', 'fortran'],
        default_options: ['c_std=gnu11'],
        meson_version: '>=1.0.0',
        version: '0.3.28')

openblas_major_version = 0 # soversion
openblas_minor_version = 3
openblas_patch_version = '28'
openblas_version = f'@openblas_major_version@.@openblas_minor_version@.@openblas_patch_version@'

supported_architectures = ['x86_64', 'aarch64']
if host_machine.cpu_family() not in supported_architectures
  cpu_family = host_machine.cpu_family()
  error(f'Building OpenBLAS with Meson is currently not supported on @cpu_family@.')
endif

as_subproject = get_option('as_subproject')

# Skip the check for valid CC
cc = meson.get_compiler('c')
fc = meson.get_compiler('fortran')
cc_id = cc.get_id()
fc_id = fc.get_id()
_mbproot = meson.project_build_root()
_msproot = meson.project_source_root()

pkg = import('pkgconfig')
pkg_ver = meson.project_version()
pkg_install_dir = '../../pkgconfig'

# Common args
_args = []
# TODO(rg): Max parallel number should be conditional
_cargs = ['-DMAX_PARALLEL_NUMBER=1', f'-DVERSION=@openblas_version@']
_fargs = []

# System configuration
build_single = get_option('build_single')
build_double = get_option('build_double')
build_complex = get_option('build_complex')
build_complex16 = get_option('build_complex16')

# TODO: Be conditional
_cargs = [
 '-DBUILD_SINGLE=1',
 '-DBUILD_DOUBLE=1',
 '-DBUILD_COMPLEX=1',
 '-DBUILD_COMPLEX16=1',
]

# Options from CMakelists
build_without_lapack = get_option('build_without_lapack')
build_lapack_deprecated = get_option('build_lapack_deprecated')
build_testing = get_option('build_testing')
use_c_lapack = get_option('use_c_lapack')
build_without_cblas = get_option('build_without_cblas')
dynamic_arch = get_option('dynamic_arch')
dynamic_older = get_option('dynamic_older')
build_relapack = get_option('build_relapack')
use_locking = get_option('use_locking')
use_perl = get_option('use_perl')
no_warmup = get_option('no_warmup')
no_affinity = get_option('no_affinity')
build_cpp_thread_safety_test = get_option('build_cpp_thread_safety_test')
build_cpp_thread_safety_gemv = get_option('build_cpp_thread_safety_gemv')
build_static_libs = get_option('build_static_libs')
max_stack_alloc = get_option('max_stack_alloc')
quad_prec = get_option('quad_precision')
exprecision = get_option('exprecision')

is_linux = host_machine.system() == 'linux'
is_darwin = host_machine.system() == 'darwin'

no_affinity = true
# TODO(mtsokol): Find out in which cases affinity should be on
# if is_linux or is_darwin
#     no_affinity = true
# else
#     no_affinity = false
# endif

if cc_id == 'clang'
    asm_name_prefix = '_'
else
    asm_name_prefix = ''
endif

_check_prefix = []
conf_data = configuration_data()
is_win = host_machine.system() == 'windows' or host_machine.system() == 'cygwin'
conf_data.set('OS_WINDOWS', is_win)
hostcpu = host_machine.cpu_family()
conf_data.set('ARCH', hostcpu.to_upper())

if is_win
    blas_server_src = 'blas_server_win32.c'
else
    blas_server_src = 'blas_server.c'
endif

defarch_array = [
 # {'system': ['windows', 'cygwin'], 'def': ['OS_WINDOWS']},
 {'cpu': ['aarch64'], 'def': ['ARCH_ARGM64']},
 {'cpu': ['alpha'], 'def': ['ARCH_ALPHA']},
 {'cpu': ['arm'], 'def': ['ARCH_ARM', 'USE_TRMM']},
 {'cpu': ['x86_64'], 'def': ['INTEL_AMD', 'USE_GEMM3M', 'USE_DIRECT_SGEMM']},
 {'cpu': ['s390x'], 'def': ['ARCH_ZARCH', 'ZARCH']},
 {'cpu': ['ia64'], 'def': ['ARCH_IA64', 'USE_GEMM3M']},
 {'cpu': ['sparc'], 'def': ['ARCH_SPARC']},
 {'cpu': ['mips'], 'def': ['ARCH_MIPS']},
 {'cpu': ['mips64'], 'def': ['ARCH_MIPS64', 'USE_TRMM']},
 {'cpu': ['loongarch64'], 'def': ['ARCH_LOONGARCH64']},
 {'cpu': ['riscv64'], 'def': ['ARCH_RISCV64', 'USE_TRMM']},
 {'cpu': ['ppc64', 'ppc'], 'def': ['ARCH_POWER', 'POWER']},
 {'cpu': ['generic'], 'def': ['USE_TRMM']},
]

# TODO(rg): Handle the kenel architectures later

foreach arch : defarch_array
  is_cpu = hostcpu in arch['cpu']
  foreach def : arch['def']
    conf_data.set(def, is_cpu)
  endforeach
endforeach

configure_file(output : 'getarch_conf.h',
               configuration : conf_data)

# Makefile.system
cpu_fam = target_machine.cpu_family()

if cpu_fam in ['x86_64', 'ppc64', 'ppc']
  add_project_arguments([
   '-DSMALL_MATRIX_OPT',
   f'-DMAX_STACK_ALLOC=@max_stack_alloc@',
  ], language:'c')
endif

if cpu_fam == 'x86_64'
  _cargs += ['-m64']
endif

quadmath_dep = fc.find_library('quadmath', required: false)

if fc_id == 'gcc'
    add_project_arguments('-DF_INTERFACE_GFORT', language: 'c')
else
  upper_fcid = fc_id.to_upper()
  add_project_arguments(f'-DF_INTERFACE_@upper_fcid@', language: 'c')
endif

# Warnings from LAPACK that we're not interested in seeing:
add_project_arguments(
  fc.get_supported_arguments(
    '-Wno-conversion',
    '-Wno-maybe-uninitialized',
    '-Wno-unused-dummy-argument',
    '-Wno-unused-variable',
  ),
  language: 'fortran'
)
add_project_arguments(
  cc.get_supported_arguments(
    '-Wno-maybe-uninitialized',
    '-Wno-unused-function',
    '-Wno-unused-variable',
  ),
  language: 'c'
)

py3 = find_program('python')

# TODO: these checks are not very robust, copy from NumPy instead
simd_extensions = []
if host_machine.cpu_family() == 'x86_64'
  simd_extensions += [
    {'flag': '-mmmx', 'define': 'HAVE_MMX'},
    {'flag': '-msse', 'define': 'HAVE_SSE'},
    {'flag': '-msse2', 'define': 'HAVE_SSE2'},
    {'flag': '-msse3', 'define': 'HAVE_SSE3'},
    {'flag': '-mssse3', 'define': 'HAVE_SSSE3'},
    {'flag': '-msse4.1', 'define': 'HAVE_SSE4_1'},
    {'flag': '-msse4.2', 'define': 'HAVE_SSE4_2'},
    {'flag': '-mfma', 'define': 'HAVE_FMA3'},
    {'flag': '-mavx', 'define': 'HAVE_AVX'},
    {'flag': '-mavx2', 'define': 'HAVE_AVX2'},
    {'flag': '-mavx512f', 'define': 'HAVE_AVX512F'},
    {'flag': '-mavx512vl', 'define': 'HAVE_AVX512VL'},
    {'flag': '-mavx512dq', 'define': 'HAVE_AVX512DQ'},
    {'flag': '-mavx512cd', 'define': 'HAVE_AVX512CD'},
    {'flag': '-march=skylake-avx512', 'define': 'HAVE_AVX512'},
  ]
endif

simd_cargs = []
simd_conf_data = configuration_data()

foreach ext : simd_extensions
  if cc.has_argument(ext['flag'])
    simd_cargs += ext['flag']
    simd_conf_data.set(ext['define'], true)
  else
    simd_conf_data.set(ext['define'], false)
  endif
endforeach

# Generate configuration header
configure_file(output : 'simd_conf.h',
               configuration : simd_conf_data)

# Header is named simd_conf.h only in this Meson build (TODO: fix that up),
# so adding a project-global include for it here.
if cc.has_multi_arguments('-include', f'@_mbproot@/simd_conf.h')
  add_project_arguments(['-include', f'@_mbproot@/simd_conf.h'], language: 'c')
endif
add_project_arguments(simd_cargs, language: 'c')

# Common symbol related options
symnames = ['ASMNAME', 'ASMFNAME', 'NAME', 'CNAME', 'CHAR_NAME', 'CHAR_CNAME']

# TODO(rg): Maybe make these conditional..
_cargs += [
 '-DSMP_SERVER', # This is evidently necessary for the driver/level2
 '-DBUILD_SINGLE=1',
 '-DBUILD_DOUBLE=1',
 '-DBUILD_COMPLEX=1',
 '-DBUILD_COMPLEX16=1',
]

# Other common options, move later
# Undefine to help prevent clashes
foreach symb : symnames
  _cargs += f'-U@symb@'
endforeach
# Based on options
if no_affinity
  _cargs += '-DNO_AFFINITY'
endif
if no_warmup
  _cargs += '-DNO_WARMUP'
endif
# Parallel builds
# TODO: This can be cleaned up significantly
# Also use multiprocessing.cpu_count()
# TODO: Handle SMP_SERVER
num_parallel = get_option('num_parallel')
if num_parallel > 1
  _cargs += f'-DMAX_PARALLEL_NUMBER=@num_parallel@'
endif
num_cores = get_option('num_cores')
if num_cores > 0
  num_threads = num_cores
else
  num_threads = 0
endif
use_thread = false
if num_threads > 2
  use_thread = true
endif
if use_thread
  message('Multi-threading enabled with ' + num_threads.to_string() + ' threads.')
  _cargs += f'-DMAX_CPU_NUMBER=@num_threads@'
  _cargs += f'-DSMP_SERVER'
else
  if get_option('use_locking')
    _cargs += '-DUSE_LOCKING'
  endif
endif

# Common maps
# Naming conventions: https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-c/2024-1/naming-conventions-for-blas-routines.html
# Also see:
# L1: https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-c/2024-1/blas-level-1-routines-and-functions.html
precision_mappings = {
    's': {'undef': ['COMPLEX', 'DOUBLE']},
    'd': {'undef': ['COMPLEX'], 'def': ['DOUBLE']},
    'q': {'undef': ['COMPLEX'], 'def': ['XDOUBLE']},
    'c': {'undef': ['DOUBLE'], 'def': ['COMPLEX']},
    'z': {'def': ['COMPLEX', 'DOUBLE']},
    'x': {'def': ['COMPLEX', 'XDOUBLE']},
    'cs': {'undef': ['DOUBLE'], 'def': ['COMPLEX']},
    'sc': {'undef': ['DOUBLE'], 'def': ['COMPLEX']},
    'dz': {'def': ['COMPLEX', 'DOUBLE']},
    'zd': {'def': ['COMPLEX', 'DOUBLE']},
    'qx': {'def': ['COMPLEX', 'XDOUBLE']},
    'xq': {'def': ['COMPLEX', 'XDOUBLE']},
    '': {}, # special case, for cblas_?dot*_sub
    # NOTE: Anything with XDOUBLE aka longdouble has no cblas_
    # xq / qx == x
    # sc / cs == c
    # zd / dz is the same as z
    # 'zd': {'undef': [], 'def': ['COMPLEX', 'DOUBLE']},
}

ext_mappings = {
    # TRANSA is only in drivers level2, kernel uses TRANS
    # LOWER is not there for only for ?ger_thread_U in drivers level2
    # TODO(rg): Does that, i.e. having (un)used symbols (un)defined matter?
    '': {}, # special case
    '_k': {},
    '_U': {
      'undef': ['LOWER', 'CONJ', 'XCONJ'],
      'except': [
        '?hemv', '?hemv_thread', '?hpmv', '?hpmv_thread', '?her', '?her_thread',
        '?her2', '?her2_thread', '?hpr2', '?hpr2_thread',
      ],
    },
    '_C': {'def': ['CONJ'], 'undef': ['XCONJ']},
    '_D': {'def': ['CONJ', 'XCONJ']},
    '_L': {
      'def': ['LOWER'],
      'except': [
        '?hemv', '?hemv_thread', '?hpmv', '?hpmv_thread', '?her', '?her_thread',
        '?her2', '?her2_thread', '?hpr2', '?hpr2_thread',
      ],
    },
    '_LN': {'def': ['LEFT'], 'undef': ['TRANSA'],
            'except': ['?syrk', '?syrk_thread',
                       '?syr2k', '?herk', '?herk_kernel',
                       '?trsm_kernel', '?her2k', '?her2k_kernel']},
    # Handle HEMV and HEMVREV better
    '_V': {
      'def': ['HEMV', 'HEMVREV', 'XCONJ'],
      'undef': ['LOWER', 'CONJ'],
      'except': [
        '?hemv', '?hemv_thread', '?hpmv', '?hpmv_thread', '?her', '?her_thread',
        '?her2', '?her2_thread', '?hpr2', '?hpr2_thread',
      ],
    },
    '_M': {
      'def': ['HEMV', 'HEMVREV', 'LOWER'],
      'except': [
        '?hemv', '?hemv_thread', '?hpmv', '?hpmv_thread', '?her', '?her_thread',
        '?her2', '?her2_thread', '?hpr2', '?hpr2_thread',
      ],
    },
    '_n': {'undef': ['TRANS', 'TRANSA', 'CONJ', 'XCONJ']},
    '_t': {'def': ['TRANS', 'TRANSA'], 'undef': ['CONJ', 'XCONJ']},
    '_r': {'def': ['CONJ'], 'undef': ['TRANS', 'TRANSA', 'XCONJ']},
    '_c': {'def': ['TRANS', 'TRANSA', 'CONJ'], 'undef': ['XCONJ']},
    '_o': {'def': ['XCONJ'], 'undef': ['TRANS', 'TRANSA', 'CONJ']},
    '_u': {'def': ['TRANS', 'TRANSA', 'XCONJ'], 'undef': ['CONJ']},
    '_s': {'def': ['CONJ', 'XCONJ'], 'undef': ['TRANS', 'TRANSA']},
    '_d': {'def': ['TRANS', 'TRANSA', 'CONJ', 'XCONJ']},
    '_nn': {'def': ['NN']},
    '_nt': {'def': ['NT']},
    '_nr': {'def': ['NR']},
    '_nc': {'def': ['NC']},
    '_tn': {'def': ['TN']},
    '_tt': {'def': ['TT']},
    '_tr': {'def': ['TR']},
    '_tc': {'def': ['TC']},
    '_rn': {'def': ['RN']},
    '_rt': {'def': ['RT']},
    '_rr': {'def': ['RR']},
    '_rc': {'def': ['RC=RC']},
    '_cn': {'def': ['CN']},
    '_ct': {'def': ['CT']},
    '_cr': {'def': ['CR=CR']},
    '_cc': {'def': ['CC']},
    # Level 3 symbols
    '_LU': {'def': ['NN'], 'undef': ['LOWER', 'RSIDE']},
    '_LL': {'def': ['LOWER', 'NN'], 'undef': ['RSIDE']},
    '_RU': {'def': ['RSIDE', 'NN'], 'undef': ['LOWER'], 'except': ['?hemm', '?hemm_thread']},
    '_RL': {'def': ['RSIDE', 'NN', 'LOWER'], 'except': ['?hemm', '?hemm_thread']},
    '_RN': {'undef': ['LEFT', 'TRANSA']},
    '_RR': {'undef': ['LEFT', 'TRANSA']},
    '_RT': {'def': ['TRANSA'], 'undef': ['LEFT']},
    '_RC': {'def': ['TRANSA'], 'undef': ['LEFT']},
    # TODO(rg): is CONJ OK for interface symbols?
    '_UN': {'undef': ['TRANS', 'LOWER', 'CONJ'], 'except': ['?syrk']},
    '_UT': {'def': ['TRANS'], 'undef': ['LOWER'], 'except': ['?syrk']},
    '_UC': {'def': ['TRANS', 'CONJ'], 'undef': ['LOWER']},
    '_LC': {'def': ['LOWER', 'TRANS', 'CONJ']},
}

ext_mappings_l2 = [
    {'ext': '_NUU', 'def': ['UNIT'], 'undef': ['TRANSA', 'LOWER'], 'for': ['s', 'd']},
    {'ext': '_NUN', 'undef': ['TRANSA', 'UNIT', 'LOWER'], 'for': ['s', 'd']},
    {'ext': '_TLU', 'def': ['UNIT', 'TRANSA', 'LOWER'], 'for': ['s', 'd']},
    {'ext': '_TLN', 'def': ['TRANSA', 'LOWER'], 'undef': ['UNIT'], 'for': ['s', 'd']},
    {'ext': '_NLU', 'def': ['UNIT', 'LOWER'], 'undef': ['TRANSA'], 'for': ['s', 'd']},
    {'ext': '_NLN', 'def': ['LOWER'], 'undef': ['TRANSA', 'UNIT'], 'for': ['s', 'd']},
    {'ext': '_TUU', 'def': ['UNIT', 'TRANSA'], 'undef': ['LOWER'], 'for': ['s', 'd']},
    {'ext': '_TUN', 'def': ['TRANSA'], 'undef': ['UNIT', 'LOWER'], 'for': ['s', 'd']},
    {'ext': '_NUU', 'def': ['UNIT', 'TRANSA=1'], 'undef': ['LOWER'], 'for': ['c', 'x', 'z']},
    {'ext': '_NUN', 'def': ['TRANSA=1'], 'undef': ['UNIT', 'LOWER'], 'for': ['c', 'x', 'z']},
    {'ext': '_TLU', 'def': ['UNIT', 'TRANSA=2', 'LOWER'], 'for': ['c', 'x', 'z']},
    {'ext': '_TLN', 'def': ['TRANSA=2', 'LOWER'], 'undef': ['UNIT'], 'for': ['c', 'x', 'z']},
    {'ext': '_RLU', 'def': ['UNIT', 'TRANSA=3', 'LOWER'], 'for': ['c', 'x', 'z']},
    {'ext': '_RLN', 'def': ['TRANSA=3', 'LOWER'], 'undef': ['UNIT'], 'for': ['c', 'x', 'z']},
    {'ext': '_CLU', 'def': ['UNIT', 'TRANSA=4', 'LOWER'], 'for': ['c', 'x', 'z']},
    {'ext': '_CLN', 'def': ['TRANSA=4', 'LOWER'], 'undef': ['UNIT'], 'for': ['c', 'x', 'z']},
    {'ext': '_NLU', 'def': ['UNIT', 'TRANSA=1', 'LOWER'], 'for': ['c', 'x', 'z']},
    {'ext': '_NLN', 'def': ['TRANSA=1', 'LOWER'], 'undef': ['UNIT'], 'for': ['c', 'x', 'z']},
    {'ext': '_TUU', 'def': ['UNIT', 'TRANSA=2'], 'undef': ['LOWER'], 'for': ['c', 'x', 'z']},
    {'ext': '_TUN', 'def': ['TRANSA=2'], 'undef': ['UNIT', 'LOWER'], 'for': ['c', 'x', 'z']},
    {'ext': '_RUU', 'def': ['UNIT', 'TRANSA=3'], 'undef': ['LOWER'], 'for': ['c', 'x', 'z']},
    {'ext': '_RUN', 'def': ['TRANSA=3'], 'undef': ['UNIT', 'LOWER'], 'for': ['c', 'x', 'z']},
    {'ext': '_CUU', 'def': ['UNIT', 'TRANSA=4'], 'undef': ['LOWER'], 'for': ['c', 'x', 'z']},
    {'ext': '_CUN', 'def': ['TRANSA=4'], 'undef': ['UNIT', 'LOWER'], 'for': ['c', 'x', 'z']}
]

ext_mappings_l3 = [
 {'ext': '_LNUU', 'def': ['UPPER', 'UNIT'], 'undef': ['TRANSA'], 'for': ['s', 'd']},
 {'ext': '_LNUN', 'def': ['UPPER'], 'undef': ['TRANSA', 'UNIT'], 'for': ['s', 'd']},
 {'ext': '_LNLU', 'def': ['UNIT'], 'undef': ['TRANSA', 'UPPER'], 'for': ['s', 'd']},
 {'ext': '_LNLN', 'undef': ['TRANSA', 'UPPER', 'UNIT'], 'for': ['s', 'd', 'q']},
 {'ext': '_LTUU', 'def': ['TRANSA', 'UPPER', 'UNIT'], 'for': ['s', 'd']},
 {'ext': '_LTUN', 'def': ['TRANSA', 'UPPER'], 'undef': ['UNIT'], 'for': ['s', 'd']},
 {'ext': '_LTLU', 'def': ['TRANSA', 'UNIT'], 'undef': ['UPPER'], 'for': ['s', 'd', 'q']},
 {'ext': '_LTLN', 'def': ['TRANSA'], 'undef': ['UPPER', 'UNIT'], 'for': ['s', 'd']},
 {'ext': '_RNUU', 'def': ['UPPER', 'UNIT'], 'undef': ['TRANSA'], 'for': ['s', 'd']},
 {'ext': '_RNUN', 'def': ['UPPER'], 'undef': ['TRANSA', 'UNIT'], 'for': ['s', 'd']},
 {'ext': '_RNLU', 'def': ['UNIT'], 'undef': ['TRANSA', 'UPPER'], 'for': ['s', 'd']},
 {'ext': '_RNLN', 'undef': ['TRANSA', 'UPPER', 'UNIT'], 'for': ['s', 'd']},
 {'ext': '_RTUU', 'def': ['TRANSA', 'UPPER', 'UNIT'], 'for': ['s', 'd']},
 {'ext': '_RTUN', 'def': ['TRANSA', 'UPPER'], 'undef': ['UNIT'], 'for': ['s', 'd', 'q']},
 {'ext': '_RTLU', 'def': ['TRANSA', 'UNIT'], 'undef': ['UPPER'], 'for': ['s', 'd', 'q']},
 {'ext': '_RTLN', 'def': ['TRANSA'], 'undef': ['UPPER', 'UNIT'], 'for': ['s', 'd']},

 # For trmm
 {'ext': '_LNUU', 'def': ['UPPER', 'UNIT'], 'undef': ['TRANSA', 'CONJ'], 'for': ['c', 'z', 'x']},
 {'ext': '_LNUN', 'def': ['UPPER'], 'undef': ['TRANSA', 'UNIT', 'CONJ'], 'for': ['c', 'z', 'x']},
 {'ext': '_LNLU', 'def': ['UNIT'], 'undef': ['TRANSA', 'UPPER', 'CONJ'], 'for': ['c', 'z', 'x']},
 {'ext': '_LNLN', 'def': [], 'undef': ['TRANSA', 'UPPER', 'UNIT', 'CONJ'], 'for': ['c', 'z', 'x']},
 {'ext': '_LTUU', 'def': ['TRANSA', 'UPPER', 'UNIT'], 'undef': ['CONJ'], 'for': ['c', 'z', 'x']},
 {'ext': '_LTUN', 'def': ['TRANSA', 'UPPER'], 'undef': ['UNIT', 'CONJ'], 'for': ['c', 'z', 'x']},
 {'ext': '_LTLU', 'def': ['TRANSA', 'UNIT'], 'undef': ['UPPER', 'CONJ'], 'for': ['c', 'z', 'x']},
 {'ext': '_LTLN', 'def': ['TRANSA'], 'undef': ['UPPER', 'UNIT', 'CONJ'], 'for': ['c', 'z', 'x']},
 {'ext': '_LRUU', 'def': ['UPPER', 'UNIT', 'CONJ'], 'undef': ['TRANSA'], 'for': ['c', 'z', 'x']},
 {'ext': '_LRUN', 'def': ['UPPER', 'CONJ'], 'undef': ['TRANSA', 'UNIT'], 'for': ['c', 'z', 'x']},
 {'ext': '_LRLU', 'def': ['UNIT', 'CONJ'], 'undef': ['TRANSA', 'UPPER'], 'for': ['c', 'z', 'x']},
 {'ext': '_LRLN', 'def': ['CONJ'], 'undef': ['TRANSA', 'UPPER', 'UNIT'], 'for': ['c', 'z', 'x']},
 {'ext': '_LCUU', 'def': ['TRANSA', 'UPPER', 'UNIT', 'CONJ'], 'undef': [], 'for': ['c', 'z', 'x']},
 {'ext': '_LCUN', 'def': ['TRANSA', 'UPPER', 'CONJ'], 'undef': ['UNIT'], 'for': ['c', 'z', 'x']},
 {'ext': '_LCLU', 'def': ['TRANSA', 'UNIT', 'CONJ'], 'undef': ['UPPER'], 'for': ['c', 'z', 'x']},
 {'ext': '_LCLN', 'def': ['TRANSA', 'CONJ'], 'undef': ['UPPER', 'UNIT'], 'for': ['c', 'z', 'x']},
 {'ext': '_RNUU', 'def': ['UPPER', 'UNIT'], 'undef': ['TRANSA', 'CONJ'], 'for': ['c', 'z', 'x']},
 {'ext': '_RNUN', 'def': ['UPPER'], 'undef': ['TRANSA', 'UNIT', 'CONJ'], 'for': ['c', 'z', 'x']},
 {'ext': '_RNLU', 'def': ['UNIT'], 'undef': ['TRANSA', 'UPPER', 'CONJ'], 'for': ['c', 'z', 'x']},
 {'ext': '_RNLN', 'def': [], 'undef': ['TRANSA', 'UPPER', 'UNIT', 'CONJ'], 'for': ['c', 'z', 'x']},
 {'ext': '_RTUU', 'def': ['TRANSA', 'UPPER', 'UNIT'], 'undef': ['CONJ'], 'for': ['c', 'z', 'x']},
 {'ext': '_RTUN', 'def': ['TRANSA', 'UPPER'], 'undef': ['UNIT', 'CONJ'], 'for': ['c', 'z', 'x']},
 {'ext': '_RTLU', 'def': ['TRANSA', 'UNIT'], 'undef': ['UPPER', 'CONJ'], 'for': ['c', 'z', 'x']},
 {'ext': '_RTLN', 'def': ['TRANSA'], 'undef': ['UPPER', 'UNIT', 'CONJ'], 'for': ['c', 'z', 'x']},
 {'ext': '_RRUU', 'def': ['UPPER', 'UNIT', 'CONJ'], 'undef': ['TRANSA'], 'for': ['c', 'z', 'x']},
 {'ext': '_RRUN', 'def': ['UPPER', 'CONJ'], 'undef': ['TRANSA', 'UNIT'], 'for': ['c', 'z', 'x']},
 {'ext': '_RRLU', 'def': ['UNIT', 'CONJ'], 'undef': ['TRANSA', 'UPPER'], 'for': ['c', 'z', 'x']},
 {'ext': '_RRLN', 'def': ['CONJ'], 'undef': ['TRANSA', 'UPPER', 'UNIT'], 'for': ['c', 'z', 'x']},
 {'ext': '_RCUU', 'def': ['TRANSA', 'UPPER', 'UNIT', 'CONJ'], 'undef': [], 'for': ['c', 'z', 'x']},
 {'ext': '_RCUN', 'def': ['TRANSA', 'UPPER', 'CONJ'], 'undef': ['UNIT'], 'for': ['c', 'z', 'x']},
 {'ext': '_RCLU', 'def': ['TRANSA', 'UNIT', 'CONJ'], 'undef': ['UPPER'], 'for': ['c', 'z', 'x']},
 {'ext': '_RCLN', 'def': ['TRANSA', 'CONJ'], 'undef': ['UPPER', 'UNIT'], 'for': ['c', 'z', 'x']},

 # symm
 # syrk
 {'ext': '_UN', 'def': [], 'undef': ['LOWER', 'TRANS', 'CONJ'], 'for': ['s', 'd', 'c', 'z']},
 {'ext': '_UT', 'def': ['TRANS'], 'undef': ['LOWER', 'CONJ'], 'for': ['s', 'd', 'c', 'z']},
 {'ext': '_LN', 'def': ['LOWER'], 'undef': ['TRANS', 'CONJ'], 'for': ['s', 'd', 'c', 'z']},
 {'ext': '_LT', 'def': ['TRANS', 'LOWER'], 'undef': ['CONJ'], 'for': ['s', 'd', 'c', 'z']},
 {'ext': '_RU', 'def': ['RSIDE', 'NC'], 'undef': ['LOWER'], 'for': ['c', 'z']},
 {'ext': '_RL', 'def': ['RSIDE', 'NC', 'LOWER'], 'for': ['c', 'z']},
 # hem hemv_thread
 {'ext': '_U', 'def': ['HEMV', 'HER'], 'undef': ['LOWER'], 'for': ['c', 'z']},
 {'ext': '_L', 'def': ['HEMV', 'HER', 'LOWER'], 'for': ['c', 'z']},
 {'ext': '_V', 'def': ['HEMVREV', 'HERREV'], 'undef': ['LOWER'], 'for': ['c', 'z']},
 {'ext': '_M', 'def': ['HEMVREV', 'HERREV', 'LOWER'], 'for': ['c', 'z']}
]

 # cc -c -O2 -DSMALL_MATRIX_OPT -DMAX_STACK_ALLOC=2048 -Wall -m64 -DF_INTERFACE_GFORT -fPIC -DSMP_SERVER -DNO_WARMUP -DMAX_CPU_NUMBER=12 -DMAX_PARALLEL_NUMBER=1 -DBUILD_SINGLE=1 -DBUILD_DOUBLE=1 -DBUILD_COMPLEX=1 -DBUILD_COMPLEX16=1 -DVERSION=\"0.3.26.dev\" -msse3 -mssse3 -msse4.1 -mavx -mavx2 -mavx2 -UASMNAME -UASMFNAME -UNAME -UCNAME -UCHAR_NAME -UCHAR_CNAME -DASMNAME=strmm_RTUU -DASMFNAME=strmm_RTUU_ -DNAME=strmm_RTUU_ -DCNAME=strmm_RTUU -DCHAR_NAME=\"strmm_RTUU_\" -DCHAR_CNAME=\"strmm_RTUU\" -DNO_AFFINITY -I../.. -UDOUBLE  -UCOMPLEX -UCOMPLEX -UDOUBLE -DTRANSA -DUPPER -DUNIT trmm_R.c -o strmm_RTUU.o

symb_defs = {
    '?amax':  {'def': ['USE_ABS'], 'undef': ['USE_MIN']},
    '?amin':  {'def': ['USE_ABS', 'USE_MIN']},
    'i?max':  {'undef': ['USE_ABS', 'USE_MIN']},
    'i?amax': {'def': ['USE_ABS'], 'undef': ['USE_MIN']},
    'i?amin': {'def': ['USE_ABS', 'USE_MIN']},
    'i?min':  {'def': ['USE_MIN'], 'undef': ['USE_ABS']},
    '?max':   {'undef': ['USE_ABS', 'USE_MIN']},
    '?min':   {'def': ['USE_MIN'], 'undef': ['USE_ABS']},
    '?axpyc': {'def': ['CONJ']},
    '?dotu':  {'undef': ['CONJ']},
    '?dotc':  {'def': ['CONJ']},
    '?geru':  {'undef': ['CONJ']},
    '?gerc':  {'def': ['CONJ']},
    '?hemm':  {'def': ['HEMM']},
    '?herk': {'def': ['HEMM']},
    '?her2k':  {'def': ['HEMM']},
    '?gemm3m':  {'def': ['GEMM3M']},
    '?symm3m':  {'def': ['GEMM3M']},
    '?hemm3m':  {'def': ['HEMM', 'GEMM3M']},
    '?her_thread':  {'def': ['HER']},
    '?her2_thread':  {'def': ['HER']},
    '?hpr_thread':  {'def': ['HEMV']},
    '?trmm_kernel': {'def': ['TRMMKERNEL']},
    '?trsm_kernel': {'def': ['TRSMKERNEL']},
    '?dsdot': {'def': ['DSDOT']},
    '?bgemm':  {'def': ['HALF']},
    '?gemm_small_kernel_b0': {'def': ['B0']},
    'cblas_?dotu_sub':  {'def': ['CBLAS', 'FORCE_USE_STACK'], 'undef': ['CONJ']},
    'cblas_?dotc_sub':  {'def': ['CBLAS', 'FORCE_USE_STACK', 'CONJ']},
}

# 3m_ rules
m3_startswith = {
    '3m_i': ['-UUSE_ALPHA'],
    '3m_o': ['-DUSE_ALPHA'],
}
m3_endswith = {
    'copyr': ['-DREAL_ONLY'],
    'copyi': ['-DIMAGE_ONLY'],
}

# config.h file generation

_config_h = f'@_mbproot@/config.h'
_makefile_conf = f'@_mbproot@/Makefile.conf'
run_command(f'@_msproot@/c_check', _makefile_conf, _config_h, cc_id, check: true)
run_command(f'@_msproot@/f_check', _makefile_conf, _config_h, fc_id, check: true)

run_command(cc_id, '-o', f'@_mbproot@/getarch', 'getarch.c', 'cpuid.S', check: true)
_getarch_1_result = run_command(f'@_mbproot@/getarch', '1', check: true, capture: true)
run_command(py3,
            f'@_msproot@/write_to_file.py',
            _getarch_1_result.stdout(),
            _config_h,
            check: true)
_getarch_0_result = run_command(f'@_mbproot@/getarch', '0', check: true, capture: true)
run_command(py3,
            f'@_msproot@/write_to_file.py',
            _getarch_0_result.stdout(),
            _makefile_conf,
            check: true)

run_command(cc_id,
            '-DGEMM_MULTITHREAD_THRESHOLD=4',
            '-I.',
            f'-I@_mbproot@',
            '-o', 'getarch_2nd',
            'getarch_2nd.c',
            capture: true, check: true)
_getarch_2nd_1_result = run_command('./getarch_2nd', '1', check: true, capture: true)
run_command(py3,
            f'@_msproot@/write_to_file.py',
            _getarch_2nd_1_result.stdout(),
            _config_h,
            check: true)
_getarch_2nd_0_result = run_command('./getarch_2nd', '0', check: true, capture: true)
run_command(py3,
            f'@_msproot@/write_to_file.py',
            _getarch_2nd_0_result.stdout(),
            _makefile_conf,
            check: true)


_read_config_py = f'@_msproot@/read_config.py'

run_command(py3,
            _read_config_py,
            '--file1', _config_h,
            '--build_dir', f'@_mbproot@',
            check: true)

keyval = import('keyval')
conf_kv = keyval.load(f'@_mbproot@/config.kconf')
# NOTE(rg): conf_kv doesn't do any parsing, setup manually
conf_hdat = configuration_data()
foreach key,val : conf_kv
  if 'CHAR' in key
       conf_hdat.set_quoted(key, val)
    else
      conf_hdat.set(key, val)
  endif
endforeach

makefile_conf_kv = keyval.load(f'@_mbproot@/Makefile.conf')
makefile_conf_dat = configuration_data()
foreach key,val : makefile_conf_kv
  makefile_conf_dat.set(key, val)
endforeach

# Ignoring other hostarch checks and conflicts for arch in BSD for now
_inc = [include_directories('.')]
subdir('lapack-netlib')
subdir('interface')
subdir('driver/level2')
subdir('driver/level3')
subdir('driver/others')
subdir('kernel')

threads_dep = dependency('threads')

openblas = library('openblas',
                          link_whole: [
                           _interface,
                           _l2_driver,
                           _l3_driver,
                           _others,
                           _kern,
                          ],
                          dependencies: [threads_dep, quadmath_dep],
                          override_options: ['b_lundef=false', 'b_asneeded=false'],
                          install: true,
                         )

# Handle headers
fs = import('fs')

if not get_option('build_without_lapack')
  lapacke_root = 'lapack-netlib/LAPACKE/include'
  lapacke_headers = [ 'lapack.h', 'lapacke_config.h', 'lapacke.h', 'lapacke_mangling.h', 'lapacke_utils.h', ]

  foreach head : lapacke_headers
    fs.copyfile(f'@lapacke_root@/@head@',
                install_dir: 'include',
                install: true)
  endforeach

endif

# Paths to necessary files for header generation
fconfig_h = f'@_mbproot@/config.h'
fconfig_last = f'@_mbproot@/config_last.h'
template = f'@_msproot@/openblas_config_template.h'
common_interface = f'@_msproot@/common_interface.h'
cblas = f'@_msproot@/cblas.h'

if not as_subproject
  # Prepare config_last.h from config.h
  pcl = custom_target('prepare_config_last',
    output : 'config_last.h',
    command : [py3, f'@_msproot@/prepare_config_last.py',
               '--config', fconfig_h,
               '--output', fconfig_last,
               quad_prec ? '--quad-precision' : [],
               exprecision ? '--exprecision' : [],
              ],
    build_by_default : true,
  )

  # Generate the headers
  custom_target('gen_install_headers',
    output : ['openblas_config.h', 'f77blas.h', 'cblas.h'],
    command : [py3, f'@_msproot@/gen_install_headers.py',
               '--dest-dir', f'@_mbproot@',
               '--version', meson.project_version(),
               '--config-last', fconfig_last,
               '--template', template,
               '--common-interface', common_interface,
               '--cblas', cblas,
               not get_option('no_fortran') ? '--generate-f77blas' : [],
               not get_option('build_without_cblas') ? '--generate-cblas' : [],
              ],
    install : true,
    install_dir : 'include',
    depends : pcl,
  )

  pkg.generate(openblas,
               name: 'openblas',
               filebase: 'meson-openblas',
               description: 'OpenBLAS via meson build',
               version: f'@pkg_ver@_meson',
               install_dir: pkg_install_dir,
              )
endif

if build_testing
  subdir('test')
  subdir('ctest')
  subdir('utest')
endif


# Dependency setup
openblas_dep =  declare_dependency(
  link_with : openblas,
  include_directories : _inc,
  version: meson.project_version(),
)

netlib_lapack_dep = declare_dependency(
  link_with : netlib_lapack,
  include_directories : _inc,
  version: meson.project_version(),
)
