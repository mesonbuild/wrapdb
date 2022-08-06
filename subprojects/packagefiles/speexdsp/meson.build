project(
  'speexdsp',
  'c',
  version: '1.2.1',
  license: 'BSD-3-Clause',
  default_options: ['c_std=gnu99', 'default_library=both', 'warning_level=0'],
)

# library versioning from speexdsp-1.2.0's configure.ac
# SPEEXDSP_LT_CURRENT=6, SPEEXDSP_LT_REVISION=1, SPEEXDSP_LT_AGE=5
lib_current = 6
lib_revision = 1
lib_age = 5
lib_soversion = lib_current - lib_age
lib_version = '@0@.@1@.@2@'.format(lib_soversion, lib_age, lib_revision)

c_args = []
cc = meson.get_compiler('c')
host_cpu_family = host_machine.cpu_family()

# Round up configuration data
add_project_arguments('-DHAVE_CONFIG_H', language: 'c')
cdata = configuration_data()

# Set SIMD config data and flags
simd_type = 'None'
if get_option('simd')
  if host_cpu_family == 'x86_64'
    cdata.set('USE_SSE', true)
    cdata.set('USE_SSE2', true)
    # x86-64 compilers all leverage SSE and SSE2 instructions by default (GCC, Clang, and MSVC)
    # so no additional flags are needed here.
    # Refs:
    #  - https://gcc.gnu.org/onlinedocs/gcc/x86-Options.html
    #  - https://docs.microsoft.com/en-us/cpp/build/reference/arch-x86
    simd_type = 'SSE2'

  elif host_cpu_family == 'x86'
    cdata.set('USE_SSE', true)
    cdata.set('USE_SSE2', true)
    # On 32-bit x86, setting "-mfpmath=sse" is the only way to both enable and use SSE extensions.
    # Ref: https://gcc.gnu.org/onlinedocs/gcc/x86-Options.html
    c_args += [
      '-mfpmath=sse',
      '-msse',
      '-msse2',
    ]
    simd_type = 'SSE2'

  elif host_cpu_family == 'arm' and cc.get_define('__thumb__') != '1'
    cdata.set('USE_NEON', true)
    # Armv7.0-A refers to the generic Armv7-A architecture without any incremental architecture extensions. 
    # Refs:
    #  - https://gcc.gnu.org/onlinedocs/gcc/ARM-Options.html
    #  - https://docs.microsoft.com/en-us/cpp/build/reference/arch-arm
    c_args += [
      '-march=armv7-a',
      '-mfpu=neon',
      '/arch:VFPv4',
    ]
    simd_type = 'NEON (armv7-a)'

    # Armv8.0-A refers to the generic Armv8-A architecture without any incremental architecture extensions. 
    # Adding "+simd" is GCC's generic flag to add Armv8-A SIMD and floating-point instructions. 
    # Refs:
    #  - https://gcc.gnu.org/onlinedocs/gcc/ARM-Options.html
    #  - https://developer.arm.com/documentation/101754/0618/armclang-Reference/armclang-Command-line-Options/-mcpu
  elif host_cpu_family == 'aarch64'
    cdata.set('USE_NEON', true)
    c_args += '-march=armv8-a+simd'
    simd_type = 'NEON (armv8-a)'
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
  {'Optimization level': get_option('optimization'), 'SIMD instructions': simd_type, 'Numerical type': numerical_type, 'FFT library': fft_library},
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

# Add supported flags to the build
add_project_arguments(cc.get_supported_arguments(c_args), language: 'c')

# Set header include paths
incdir = include_directories(
  '.',
  'include',
  'include/speex',
)

# Nested Meson builds
subdir('include/speex')
subdir('libspeexdsp')
subdir('examples')
