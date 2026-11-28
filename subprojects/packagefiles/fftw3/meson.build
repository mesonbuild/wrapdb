project(
  'fftw',
  'c',
  version: '3.3.10',
  license: 'GPL-2.0-or-later',
  meson_version: '>=0.60.0',
)

cc = meson.get_compiler('c')
cc_syntax = cc.get_argument_syntax()
cpu_family = host_machine.cpu_family()
system = host_machine.system()

m_dep = cc.find_library(
  'm',
  required: false,
)

cdata = configuration_data()
# PACKAGE and VERSION end up in the wisdom preamble, keep them as upstream
cdata.set_quoted('PACKAGE', 'fftw')
cdata.set_quoted('VERSION', meson.project_version())
cdata.set_quoted('PACKAGE_VERSION', meson.project_version())
cdata.set_quoted('FFTW_CC', '@0@ @1@'.format(cc.get_id(), cc.version()))
cdata.set('FFTW_ENABLE_ALLOCA', 1)

foreach h : [
  'alloca.h',
  'inttypes.h',
  'mach/mach_time.h',
  'malloc.h',
  'stddef.h',
  'stdint.h',
  'stdlib.h',
  'string.h',
  'sys/time.h',
  'sys/types.h',
  'unistd.h',
]
  if cc.has_header(h)
    cdata.set('HAVE_' + h.underscorify().to_upper(), 1)
  endif
endforeach
if cdata.has('HAVE_SYS_TIME_H') and cc.has_header('time.h')
  cdata.set('TIME_WITH_SYS_TIME', 1)
endif

foreach name, type : {
  'SIZEOF_DOUBLE': 'double',
  'SIZEOF_FLOAT': 'float',
  'SIZEOF_UNSIGNED_INT': 'unsigned int',
  'SIZEOF_UNSIGNED_LONG': 'unsigned long',
  'SIZEOF_UNSIGNED_LONG_LONG': 'unsigned long long',
  'SIZEOF_VOID_P': 'void *',
}
  cdata.set(name, cc.sizeof(type))
endforeach
if cc.has_type(
  'uintptr_t',
  prefix: '#include <stdint.h>',
)
  cdata.set('HAVE_UINTPTR_T', 1)
endif

foreach f : [
  ['abort', 'stdlib.h'],
  ['cosl', 'math.h'],
  ['drand48', 'stdlib.h'],
  ['gettimeofday', 'sys/time.h'],
  ['mach_absolute_time', 'mach/mach_time.h'],
  ['memalign', 'malloc.h'],
  ['posix_memalign', 'stdlib.h'],
  ['sinl', 'math.h'],
  ['snprintf', 'stdio.h'],
  ['tanl', 'math.h'],
]
  if cc.has_function(
    f[0],
    prefix: '#include <@0@>'.format(f[1]),
    dependencies: m_dep,
  )
    cdata.set('HAVE_' + f[0].to_upper(), 1)
  endif
endforeach
foreach d : [
  ['cosl', 'math.h'],
  ['drand48', 'stdlib.h'],
  ['memalign', 'malloc.h'],
  ['posix_memalign', 'stdlib.h'],
  ['sinl', 'math.h'],
  ['srand48', 'stdlib.h'],
]
  cdata.set10(
    'HAVE_DECL_' + d[0].to_upper(),
    cc.has_header_symbol(d[1], d[0]),
  )
endforeach

if cc.links(
  '''#include <math.h>
  int main(void) { return isnan(3.14159) ? 1 : 0; }''',
  dependencies: m_dep,
  name: 'isnan',
)
  cdata.set('HAVE_ISNAN', 1)
endif

# Same lookup as kernel/ifftw.h
if cc.links(
  '''#if defined(__GNUC__)
  #  define alloca __builtin_alloca
  #elif defined(_MSC_VER)
  #  include <malloc.h>
  #  define alloca _alloca
  #else
  #  include <alloca.h>
  #endif
  int main(void) { char *p = (char *) alloca(16); p[0] = 0; return p[0]; }''',
  name: 'alloca',
)
  cdata.set('HAVE_ALLOCA', 1)
endif

# kernel/kalloc.c uses _aligned_malloc with MSVC, and needs its own aligned
# malloc where neither memalign nor posix_memalign exist (e.g. MinGW)
if (
  not cdata.has('HAVE_MEMALIGN')
  and not cdata.has('HAVE_POSIX_MEMALIGN')
  and cc.get_define('_MSC_VER') == ''
)
  cdata.set('WITH_OUR_MALLOC', 1)
endif

if cpu_family in ['ia64', 'mips64', 'parisc', 'ppc', 'ppc64']
  cdata.set('ARCH_PREFERS_FMA', 1)
endif

threads_opt = get_option('threads')
if system == 'windows'
  # threads/threads.c uses the Win32 API directly
  threads_dep = dependency(
    '',
    required: false,
  )
  have_threads = threads_opt.allowed()
else
  threads_dep = dependency(
    'threads',
    required: threads_opt,
  )
  have_threads = threads_dep.found()
  if have_threads
    cdata.set('USING_POSIX_THREADS', 1)
  endif
endif
if have_threads
  cdata.set('HAVE_THREADS', 1)
endif

long_double_opt = get_option('long_double').require(
  cdata.has('HAVE_COSL') and cdata.has('HAVE_SINL') and cdata.has('HAVE_TANL'),
  error_message: 'long double precision requires cosl, sinl and tanl',
)
# fftw3.h only declares the quad precision API for GCC on x86 and IA-64
quad_opt = get_option('quad').require(
  cc.has_header_symbol(
    'fftw3.h',
    'fftwq_plan_dft',
    include_directories: include_directories('api'),
  ),
  error_message: 'quad precision is only supported with GCC on x86 and IA-64',
)
quadmath_dep = cc.find_library(
  'quadmath',
  required: quad_opt,
)
quad_opt = quad_opt.require(
  quadmath_dep.found(),
  error_message: 'quad precision requires libquadmath',
)
if quadmath_dep.found()
  cdata.set('HAVE_LIBQUADMATH', 1)
endif

configure_file(
  output: 'config.h',
  configuration: cdata,
)

# SIMD codelets are built with extra compiler flags in their own static
# libraries; the library selects them at runtime after checking the CPU.
if cc_syntax == 'msvc'
  sse2_args = []
  avx_args = ['/arch:AVX']
  avx2_args = ['/arch:AVX2']
  avx512_args = ['/arch:AVX512']
  neon_args = []
else
  sse2_args = ['-msse2']
  avx_args = ['-mavx']
  avx2_args = ['-mavx2', '-mfma']
  avx512_args = ['-mavx512f']
  neon_args = cpu_family == 'arm' ? ['-mfpu=neon'] : []
endif

x86 = cpu_family in ['x86', 'x86_64']
simd_isas = [
  {
    'name': 'sse2',
    'option': get_option('sse2').require(
      x86,
      error_message: 'SSE2 requires an x86 CPU',
    ),
    'define': 'HAVE_SSE2',
    'dirs': ['sse2'],
    'args': sse2_args,
    'precisions': ['double', 'single'],
    'code': '''#include <emmintrin.h>
      __m128d f(__m128d a, __m128d b) { return _mm_add_pd(a, b); }''',
  },
  {
    'name': 'avx',
    'option': get_option('avx').require(
      x86,
      error_message: 'AVX requires an x86 CPU',
    ),
    'define': 'HAVE_AVX',
    'dirs': ['avx'],
    'args': avx_args,
    'precisions': ['double', 'single'],
    'code': '''#include <immintrin.h>
      __m256d f(__m256d a, __m256d b) { return _mm256_add_pd(a, b); }''',
  },
  {
    'name': 'avx2',
    'option': get_option('avx2').require(
      x86,
      error_message: 'AVX2 requires an x86 CPU',
    ),
    'define': 'HAVE_AVX2',
    'dirs': ['avx2', 'avx2-128'],
    'args': avx2_args,
    'precisions': ['double', 'single'],
    'code': '''#include <immintrin.h>
      __m256d f(__m256d a, __m256d b, __m256d c) { return _mm256_fmadd_pd(a, b, c); }''',
  },
  {
    'name': 'avx512',
    'option': get_option('avx512').require(
      cpu_family == 'x86_64',
      error_message: 'AVX-512 requires an x86_64 CPU',
    ),
    'define': 'HAVE_AVX512',
    'dirs': ['avx512'],
    'args': avx512_args,
    'precisions': ['double', 'single'],
    'requires': 'avx2',
    'code': '''#include <immintrin.h>
      __m512d f(__m512d a, __m512d b, __m512d c) { return _mm512_fmadd_pd(a, b, c); }''',
  },
  {
    'name': 'neon',
    # Only AArch64 guarantees NEON. simd-neon.h relies on GCC style vector
    # initializers that MSVC does not support.
    'option': get_option('neon').disable_auto_if(cpu_family == 'arm').require(
      cpu_family in ['aarch64', 'arm'] and cc.get_id() != 'msvc',
      error_message: 'NEON requires an ARM CPU and a GCC compatible compiler',
    ),
    'define': 'HAVE_NEON',
    'dirs': ['neon'],
    'args': neon_args,
    'precisions': cpu_family == 'aarch64' ? ['double', 'single'] : ['single'],
    'code': '''#include <arm_neon.h>
      float32x4_t f(float32x4_t a, float32x4_t b) { return vaddq_f32(a, b); }''',
  },
]

enabled_isas = []
enabled_isa_names = []
foreach isa : simd_isas
  opt = isa['option']
  required_isa = isa.get('requires', '')
  if required_isa != ''
    opt = opt.require(
      required_isa in enabled_isa_names,
      error_message: '@0@ requires @1@'.format(isa['name'], required_isa),
    )
  endif
  ok = opt.allowed() and cc.compiles(
    isa['code'],
    args: isa['args'],
    name: isa['name'],
  )
  if opt.enabled() and not ok
    error(
      '@0@ was requested but the compiler does not support it'.format(
        isa['name'],
      ),
    )
  endif
  if ok
    enabled_isas += [isa]
    enabled_isa_names += isa['name']
  endif
  summary(
    isa['name'],
    ok,
    section: 'SIMD',
    bool_yn: true,
  )
endforeach

fftw_args = []
dep_args = []
if cc_syntax == 'msvc'
  # Some codelets need more sections than the default COFF limit
  fftw_args += '/bigobj'
endif
if system == 'windows' and get_option('default_library') != 'static'
  fftw_args += '-DFFTW_DLL'
  dep_args += '-DFFTW_DLL'
endif

inc = include_directories('.')

fftw_sources = []
subdir('kernel')
subdir('api')
subdir('dft')
subdir('rdft')
subdir('reodft')
subdir('simd-support')
subdir('threads')
if have_threads
  fftw_sources += fftw_threads_sources
endif

subdir('include')
install_headers('api/fftw3.h')

if get_option('tests').allowed()
  subdir('libbench2')
  subdir('tests')
endif

pkg = import('pkgconfig')

precisions = [
  {
    'name': 'double',
    'option': get_option('double'),
    'suffix': '',
    'args': [],
    'bench_args': [],
  },
  {
    'name': 'single',
    'option': get_option('single'),
    'suffix': 'f',
    'args': ['-DFFTW_SINGLE'],
    'bench_args': ['-DBENCHFFT_SINGLE'],
  },
  {
    'name': 'long_double',
    'option': long_double_opt,
    'suffix': 'l',
    'args': ['-DFFTW_LDOUBLE'],
    'bench_args': ['-DBENCHFFT_LDOUBLE'],
  },
  {
    'name': 'quad',
    'option': quad_opt,
    'suffix': 'q',
    'args': ['-DFFTW_QUAD'],
    'bench_args': ['-DBENCHFFT_QUAD'],
  },
]

foreach p : precisions
  precision = p['name']
  enabled = p['option'].allowed()
  summary(
    precision,
    enabled,
    section: 'Precisions',
    bool_yn: true,
  )
  if not enabled
    continue
  endif
  suffix = p['suffix']
  precision_args = p['args']
  precision_deps = [m_dep, threads_dep]
  if precision == 'quad'
    precision_deps += quadmath_dep
  endif

  # These must be visible to every source file, they decide the alignment
  # and which codelets get registered
  precision_isas = []
  foreach isa : enabled_isas
    if precision in isa['precisions']
      precision_isas += [isa]
      precision_args += '-D@0@=1'.format(isa['define'])
    endif
  endforeach

  simd_libs = []
  foreach isa : precision_isas
    isa_sources = []
    foreach d : isa['dirs']
      foreach f : dft_simd_codelets
        isa_sources += 'dft' / 'simd' / d / f
      endforeach
      foreach f : rdft_simd_codelets
        isa_sources += 'rdft' / 'simd' / d / f
      endforeach
    endforeach
    simd_libs += static_library(
      'fftw3@0@_@1@'.format(suffix, isa['name']),
      isa_sources,
      c_args: fftw_args + precision_args + isa['args'],
      include_directories: inc,
    )
  endforeach

  # libtool version 9:10:6
  fftw_lib = library(
    'fftw3' + suffix,
    fftw_sources,
    c_args: fftw_args + precision_args,
    include_directories: inc,
    link_whole: simd_libs,
    dependencies: precision_deps,
    version: '3.6.10',
    soversion: '3',
    darwin_versions: ['10', '10.10'],
    install: true,
  )

  pkg.generate(
    fftw_lib,
    filebase: 'fftw3' + suffix,
    name: 'FFTW',
    description: 'fast Fourier transform library',
    extra_cflags: get_option('default_library') == 'shared' ? dep_args : [],
  )

  fftw_dep = declare_dependency(
    compile_args: dep_args,
    include_directories: fftw_inc,
    link_with: fftw_lib,
  )
  meson.override_dependency('fftw3' + suffix, fftw_dep)
  set_variable('fftw3@0@_dep'.format(suffix), fftw_dep)

  if get_option('tests').allowed()
    bench = executable(
      'bench' + suffix,
      bench_sources,
      c_args: dep_args + precision_args + p['bench_args'],
      include_directories: inc,
      link_with: [
        fftw_lib,
        static_library(
          'bench2' + suffix,
          libbench2_sources,
          c_args: p['bench_args'],
          include_directories: inc,
          dependencies: precision_deps,
        ),
      ],
      dependencies: precision_deps,
    )
    foreach kind, args : bench_tests
      if kind != 'threads' or have_threads
        test(
          '@0@-@1@'.format(precision, kind),
          bench,
          args: args,
          timeout: 300,
        )
      endif
    endforeach
  endif
endforeach
