project(
  'speexdsp',
  'c',
  version: '1.2.1',
  license: 'BSD-3-Clause',
  default_options: [
    meson.version().version_compare('>=1.3.0') ? 'c_std=gnu99,c99' : 'c_std=gnu99',
    'default_library=both',
    'warning_level=0',
  ],
)

# library versioning from speexdsp-1.2.0's configure.ac
# SPEEXDSP_LT_CURRENT=6, SPEEXDSP_LT_REVISION=1, SPEEXDSP_LT_AGE=5
lib_current = 6
lib_revision = 1
lib_age = 5
lib_soversion = lib_current - lib_age
lib_version = '@0@.@1@.@2@'.format(lib_soversion, lib_age, lib_revision)

cc = meson.get_compiler('c')
host_cpu_family = host_machine.cpu_family()

# Round up configuration data
add_project_arguments(
  '-DHAVE_CONFIG_H',
  language: 'c',
)
cdata = configuration_data()

arm_neon_code = '''
#include <stdint.h>
#include <arm_neon.h>
#include <math.h>

static void square4_serial(float*);
static void square4_vectorized(float*);
static int compare4(const float*, const float*);

static void square4_serial(float* array) {
    for (uint8_t i = 0; i < 4; ++i) {
        const float f = array[i];
        array[i] = f * f;
    }
}

static void square4_vectorized(float* array) {
    float32x4_t f = vld1q_f32(array);
    f = vmulq_f32(f, f);
    vst1q_f32(array, f);
}

static int compare4(const float* a, const float* b) {
    float sum_of_diffs = 0.0f;
    for (uint8_t i = 0; i < 4; ++i) {
        sum_of_diffs += fabsf(a[i] - b[i]);
    }
    const int rounded_sum = (int)(sum_of_diffs + 0.5f);
    return rounded_sum;
}

int main() {
    float values1[4] = {1.0f, 2.0f, 3.0f, 4.0f};
    square4_serial(values1);

    float values2[4] = {1.0f, 2.0f, 3.0f, 4.0f};
    square4_vectorized(values2);

    return compare4(values1, values2);
}
'''

# Set SIMD config data and flags
simd_type = 'None'
if get_option('simd')
  if host_cpu_family == 'x86_64'
    # x86-64 compilers all leverage SSE and SSE2 instructions by default (GCC, Clang, and MSVC)
    # so no additional flags are needed here.
    # Refs:
    #  - https://gcc.gnu.org/onlinedocs/gcc/x86-Options.html
    #  - https://docs.microsoft.com/en-us/cpp/build/reference/arch-x86
    cdata.set('USE_SSE', true)
    cdata.set('USE_SSE2', true)
    simd_type = 'SSE2'

  elif host_cpu_family == 'x86'
    # On 32-bit x86, setting "-mfpmath=sse" is the only way to both enable and use SSE extensions.
    # Ref: https://gcc.gnu.org/onlinedocs/gcc/x86-Options.html
    cdata.set('USE_SSE', true)
    cdata.set('USE_SSE2', true)
    simd_type = 'SSE2'
    sse_flags = ['-mfpmath=sse', '-msse', '-msse2']
    add_project_arguments(
      cc.get_supported_arguments(sse_flags),
      language: 'c',
    )

  elif host_cpu_family == 'arm'
    # Armv7.0-A refers to the generic Armv7-A architecture without any incremental architecture extensions.
    # Refs:
    #  - https://gcc.gnu.org/onlinedocs/gcc/ARM-Options.html
    #  - https://docs.microsoft.com/en-us/cpp/build/reference/arch-arm
    neon_flags = cc.get_supported_arguments(
      ['-march=armv7-a', '-mfpu=neon', '/arch:VFPv4'],
    )
    # The SIMD test code might need libmath to link
    m_dep = cc.find_library(
      'm',
      required: false,
    )
    neon_test = cc.run(
      arm_neon_code,
      args: neon_flags,
      dependencies: m_dep,
      name: 'system supports ARM NEON instructions',
    )
    can_use_neon = (neon_test.compiled() and neon_test.returncode() == 0)
    if can_use_neon
      cdata.set('USE_NEON', true)
      simd_type = 'NEON (armv7-a)'
      add_project_arguments(
        neon_flags,
        language: 'c',
      )
    endif

  elif host_cpu_family == 'aarch64'
    # Armv8.0-A refers to the generic Armv8-A architecture without any incremental architecture extensions.
    # Adding "+simd" is GCC's generic flag to add Armv8-A SIMD and floating-point instructions.
    # Refs:
    #  - https://gcc.gnu.org/onlinedocs/gcc/ARM-Options.html
    #  - https://developer.arm.com/documentation/101754/0618/armclang-Reference/armclang-Command-line-Options/-mcpu
    cdata.set('USE_NEON', true)
    simd_type = 'NEON (armv8-a)'
    add_project_arguments(
      cc.get_supported_arguments('-march=armv8-a+simd'),
      language: 'c',
    )
  endif
endif

# Set numerical representation config data
numerical_type = ''
fft_library = ''
if get_option('fixed-point')
  cdata.set('FIXED_POINT', true)
  numerical_type = 'fixed-point'

  cdata.set('USE_KISS_FFT', true)
  fft_library = 'Kiss FFT (built-in)'

  # The fixed-point implementation isn't written using SSE intrinsics
  # and "arch.h" checks that USE_SSE is disabled when using fixed-point,
  # so we explicitly disable it here to pass that check:
  cdata.set('USE_SSE', false)
  # However, we still let the compiler pack integer operations into SIMD
  # calls whenever possible and we inform the user that SIMD is active in
  # the Summary block.

else
  cdata.set('FLOATING_POINT', true)
  numerical_type = 'floating-point'

  cdata.set('USE_SMALLFT', true)
  fft_library = 'OggVorbis FFT (built-in)'
endif

summary(
  {
    'Optimization level': get_option('optimization'),
    'SIMD instructions': simd_type,
    'Numerical type': numerical_type,
    'FFT library': fft_library,
  },
  section: 'Library Summary',
)

# Set C99 variable-length array config data
cdata.set('VAR_ARRAYS', cc.get_id() != 'msvc')

# Set EXPORT config data
if cc.get_id() == 'msvc' and get_option('default_library') != 'static'
  cdata.set('EXPORT', '')
elif cc.has_function_attribute('visibility')
  cdata.set('EXPORT', 'extern __attribute__ ((visibility ("default")))')
else
  cdata.set('EXPORT', 'extern')
endif

# Populate config.h from the above data
configure_file(
  input: 'config.h.meson',
  output: 'config.h',
  configuration: cdata,
)

# Set header include paths
incdir = include_directories('.', 'include', 'include/speex')

# Nested Meson builds
subdir('include/speex')
subdir('libspeexdsp')
subdir('examples')
