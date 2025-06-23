project(
  'soundtouch',
  'c',
  'cpp',
  version: '2.3.2',
  license: 'LGPL-2.1-or-later',
  default_options: [
    'c_std=c11',
    # to avoid Meson's warning under MSVC
    'cpp_std=c++14',
    # See below ("ST_NO_EXCEPTION_HANDLING") for the rationale
    'cpp_eh=default',
    'pkgconfig.relocatable=true',
  ],
  meson_version: '>= 0.53',
)

cpp = meson.get_compiler('cpp')
system = host_machine.system()
cpu = host_machine.cpu()

openmp = dependency(
  'openmp',
  required: get_option('openmp'),
)
m = cpp.find_library(
  'm',
  required: false,
)

soundtouch_args = []

conf = configuration_data()

# Autotools applies -Ofast (implies -O3 -ffast-math) to allow gcc
# autovectorization generate effective SIMD code.
# I prefer here to do so only with these to avoid surprises
# at lower levels. -- amyspark
if get_option('optimization') in ['2', '3', 's']
  soundtouch_args += cpp.get_supported_arguments('/fp:fast', '-ffast-math')
endif

is_android_softfp = cpp.compiles(
  '''
#if defined(__SOFTFP__) && defined(ANDROID)
#else
#error "Not under Android soft FP"
#endif''',
  name: 'targeting Android with soft float implementation',
)

if get_option('integer_samples')
  conf.set('SOUNDTOUCH_INTEGER_SAMPLES', 1)
  soundtouch_args += ['-DSOUNDTOUCH_INTEGER_SAMPLES=1']
else
  conf.set('SOUNDTOUCH_FLOAT_SAMPLES', 1)
  soundtouch_args += ['-DSOUNDTOUCH_FLOAT_SAMPLES=1']
endif

neon_cpu = cpu in ['arm', 'aarch64']

# Use ARM instruction set instead of Thumb for improved calculation performance in ARM CPUs
if cpu == 'arm' and system == 'android'
  if cpp.get_define('__thumb__') != ''
    soundtouch_args += cpp.get_supported_arguments('-marm')
  endif
endif

if neon_cpu and get_option('neon')
  conf.set('SOUNDTOUCH_USE_NEON', 1)
  soundtouch_args += ['-DSOUNDTOUCH_USE_NEON=1']
  soundtouch_args += cpp.get_supported_arguments('-mfpu=neon')
endif

# GCC, by default, handles exceptions in C++ sources as /EHsc, allowing
# exceptions intra C++ code, and terminating the app on hitting a C function's
# stack.
# Grep ST_NO_EXCEPTION_HANDLING and see:
# https://learn.microsoft.com/en-us/cpp/build/reference/eh-exception-handling-model?view=msvc-170
# https://gcc.gnu.org/onlinedocs/gcc/Code-Gen-Options.html#index-fexceptions
#
# However, -fexceptions in Application.mk must be manually injected, as
# their toolchain does not add it for historical reasons.
# https://developer.android.com/ndk/guides/cpp-support?hl=es-419
if get_option('cpp_eh') in ['none']
  soundtouch_args += ['-DST_NO_EXCEPTION_HANDLING']
elif system == 'android'
  soundtouch_args += cpp.get_supported_arguments('-fexceptions')
endif

# Work around Android Clang / MS Clang not defining __GNUC__
# This affects cpuid detection in x86 and x64 targets
# Amyspark: careful with this flag, it may interfere with STTypes.h
if cpp.get_define('__clang__') != '' and cpp.get_define('__GNUC__') == ''
  soundtouch_args += cpp.get_supported_arguments('-fgnuc-version=10')
endif

# Amyspark: Turn off certain warnings that can trigger Werror
soundtouch_args += cpp.get_supported_arguments(
  '-Wno-unused-variable',
  '-Wno-sign-compare',
  '-Wno-unused-but-set-variable',
  '-Wno-inconsistent-missing-override',
  '-Wno-unused-const-variable',
)

if cpu == 'x86'
  soundtouch_args += cpp.get_supported_arguments('-mstackrealign')
endif

deps = [openmp, m]

subdir('include')
subdir('source')

pkg = import('pkgconfig')

pkg.generate(
  soundtouch_lib,
  name: 'SoundTouch',
  description: 'SoundTouch is an open-source audio processing library for changing the Tempo, Pitch and Playback Rates of audio streams or files',
  filebase: 'soundtouch',
  subdirs: 'soundtouch',
)
