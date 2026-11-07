project(
  'sdl3',
  'c',
  version: '3.4.14',
  license: 'zlib',
  meson_version: '>=1.6',
  default_options: ['c_std=none'],
)

cc = meson.get_compiler('c')

varr = meson.project_version().split('.')

sdl_major = varr[0].to_int()
sdl_minor = varr[1].to_int()
sdl_patch = varr[2].to_int()

cdata = configuration_data()

cdata.set('HAVE_LIBC', 1)
cdata.set('SDL_DEFAULT_ASSERT_LEVEL', true)

sdl_deps = [
  dependency('threads'),
  dependency(
    'dl',
    required: false,
  ),
  cc.find_library(
    'm',
    required: false,
  ),
]

add_project_arguments(
  '-DUSING_GENERATED_CONFIG_H',
  language: 'c',
)
add_project_arguments(
  '-DSDL_BUILD_MAJOR_VERSION=@0@'.format(sdl_major),
  '-DSDL_BUILD_MINOR_VERSION=@0@'.format(sdl_minor),
  '-DSDL_BUILD_MICRO_VERSION=@0@'.format(sdl_patch),
  language: 'c',
)

# BEGIN platform detection logic

# FIXME: detect this properly
platform_is_linux_desktop = (host_machine.system() == 'linux')
platform_is_android = (host_machine.system() == 'android')
platform_is_linux = platform_is_android or platform_is_linux_desktop

platform_is_darwin = (host_machine.system() == 'darwin')
# FIXME: detect this properly
platform_is_macos = platform_is_darwin
platform_is_ios = false

platform_is_windows = (host_machine.system() == 'windows')
# FIXME: detect this properly
platform_is_win32 = platform_is_windows
platform_is_winrt = false

platform_is_vita = (host_machine.system() == 'vita')
platform_is_os2 = (host_machine.system() == 'os2')

platform_is_dragonflybsd = (host_machine.system() == 'dragonfly')
platform_is_freebsd = (host_machine.system() == 'freebsd')
platform_is_netbsd = (host_machine.system() == 'netbsd')
platform_is_openbsd = (host_machine.system() == 'openbsd')

platform_is_bsd = (
  platform_is_dragonflybsd
  or platform_is_freebsd
  or platform_is_netbsd
  or platform_is_openbsd
)

platform_is_haiku = (host_machine.system() == 'haiku')

platform_is_emscripten = (host_machine.system() == 'emscripten')

platform_is_psp = (host_machine.system() == 'psp')

# FIXME: verify this
platform_is_nacl = (host_machine.system() == 'nacl')

# FIXME: darwin is technically a unix system, but we cannot differenciate between macOS and darwin
platform_is_unixlike = (
  platform_is_bsd
  or platform_is_emscripten
  or platform_is_haiku
  or platform_is_linux
)

platform_is_apple = (
  platform_is_macos
  or platform_is_ios
)

platform_is_unixlike_or_apple = platform_is_unixlike or platform_is_apple

cpu_arm32 = target_machine.cpu_family() == 'arm'
cpu_arm64 = target_machine.cpu_family() == 'aarch64'
cpu_loongarch64 = target_machine.cpu_family() == 'loongarch64'
cpu_ppc32 = target_machine.cpu_family() == 'ppc'
cpu_ppc64 = target_machine.cpu_family() == 'ppc64'
cpu_x86 = target_machine.cpu_family() == 'x86'
cpu_x64 = target_machine.cpu_family() == 'x86_64'

# END platform detection logic

use_gcc = cc.get_id() == 'gcc'
use_clang = cc.get_id() == 'clang'
use_msvc = cc.get_id() == 'msvc'

if platform_is_windows or use_msvc
  add_languages(
    'cpp',
    native: false,
  )
  cpp_compiler = meson.get_compiler('cpp')
endif

# The hidraw support doesn't catch Xbox, PS4 and Nintendo controllers,
#  so we'll just use libusb when it's available. libusb does not support iOS,
#  so we default to yes on iOS.
hidapi_libusb_available = not (platform_is_apple or platform_is_android)

assembly_default = use_gcc or use_clang or (
  use_msvc
  and cpp_compiler.version().version_compare(
  '>14.00',
  )
)
gcc_atomics_supported = use_gcc or use_clang
system_iconv_default = not (platform_is_windows or platform_is_apple)
oss_default = platform_is_unixlike and not (
  platform_is_linux
  or platform_is_netbsd
  or platform_is_openbsd
)
shared_available = not platform_is_emscripten

opt_gcc_atomics = get_option('use_gcc_atomics').require(gcc_atomics_supported)

have_gcc_atomics = opt_gcc_atomics.allowed() and cc.links(
  '''int main(int argc, char **argv) {
        int a;
        void *x, *y, *z;
        __sync_lock_test_and_set(&a, 4);
        __sync_lock_test_and_set(&x, y);
        __sync_fetch_and_add(&a, 1);
        __sync_bool_compare_and_swap(&a, 5, 10);
        __sync_bool_compare_and_swap(&x, y, z);
        return 0; }''',
  name: 'gcc atomics test',
)

have_gcc_sync_lock_and_test = not have_gcc_atomics and cc.links(
  '''int main(int argc, char **argv) {
        int a;
        __sync_lock_test_and_set(&a, 1);
        __sync_lock_release(&a);
        return 0; }''',
  name: 'gcc __sync_lock_test_and_set() test',
)

cdata.set10('HAVE_GCC_ATOMICS', have_gcc_atomics)
cdata.set10('HAVE_GCC_SYNC_LOCK_TEST_AND_SET', have_gcc_sync_lock_and_test)

core_subsystems = {
  'audio': {
    'deps': [],
  },
  'video': {
    'deps': [],
  },
  'gpu': {
    'deps': ['video'],
  },
  'render': {
    'deps': ['video'],
  },
  'camera': {
    'deps': ['video'],
  },
  'joystick': {
    'deps': [],
  },
  'haptic': {
    'deps': ['joystick'],  # Haptic requires some private functions from the joystick subsystem.
  },
  'hidapi': {
    'deps': [],
  },
  'power': {
    'deps': [],
  },
  'sensor': {
    'deps': [],
  },
  'dialog': {
    'deps': [],
  },
  'tray': {
    'deps': [],
  },
}

enabled_subsystems = []

foreach ss_name, subsystem : core_subsystems
  ss_enabled = get_option(f'use_@ss_name@').allowed()

  if ss_enabled
    require_deps = get_option(f'use_@ss_name@').enabled()
    foreach dep : subsystem['deps']
      have_dep = dep in enabled_subsystems
      if require_deps and not have_dep
        error(
          f'Subsystem @ss_name@ requires subsystem @dep@, which is not enabled',
        )
      endif
      ss_enabled = ss_enabled and have_dep
    endforeach
  endif

  if ss_enabled
    message('Subsystem "@0@" is ENABLED'.format(ss_name))
    enabled_subsystems += ss_name
  else
    cdata.set('SDL_@0@_DISABLED'.format(ss_name.to_upper()), 1)
    message('Subsystem "@0@" is DISABLED'.format(ss_name))
  endif
endforeach

opt_assembly = get_option('use_assembly').enable_auto_if(assembly_default).allowed()
assembly_options = {
  'avx': {
    'supported': cpu_x86 or cpu_x64,
    'check_code': '''
      #include <immintrin.h>
      void floats_add(float *dest, float *a, float *b, unsigned size) {
        for (; size >= 8; size -= 8, dest += 8, a += 8, b += 8) {
          _mm256_storeu_ps(dest, _mm256_add_ps(_mm256_loadu_ps(a), _mm256_loadu_ps(b)));
        }
      }
      int main(int argc, char **argv) {
        floats_add((float*)0, (float*)0, (float*)0, 0);
        return 0;
      }''',
    'gcc_clang_flags': ['-mavx'],
  },
  'avx2': {
    'supported': cpu_x86 or cpu_x64,
    'check_code': '''
      #include <immintrin.h>
      void ints_add(int *dest, int *a, int *b, unsigned size) {
        for (; size >= 8; size -= 8, dest += 8, a += 8, b += 8) {
          _mm256_storeu_si256((__m256i*)dest, _mm256_add_epi32(_mm256_loadu_si256((__m256i*)a), _mm256_loadu_si256((__m256i*)b)));
        }
      }
      int main(int argc, char **argv) {
        ints_add((int*)0, (int*)0, (int*)0, 0);
        return 0;
      }''',
    'gcc_clang_flags': ['-mavx2'],
  },
  'avx512f': {
    'supported': cpu_x86 or cpu_x64,
    'check_code': '''
      #include <immintrin.h>
      void floats_add(float *dest, float *a, float *b, unsigned size) {
        for (; size >= 16; size -= 16, dest += 16, a += 16, b += 16) {
          _mm512_storeu_ps(dest, _mm512_add_ps(_mm512_loadu_ps(a), _mm512_loadu_ps(b)));
        }
      }
      int main(int argc, char **argv) {
        floats_add((float*)0, (float*)0, (float*)0, 0);
        return 0;
      }''',
    'gcc_clang_flags': ['-mavx512f'],
  },
  'sse': {
    'supported': cpu_x86 or cpu_x64,
    'check_code': '''
      #include <xmmintrin.h>
      void floats_add(float *dest, float *a, float *b, unsigned size) {
        for (; size >= 4; size -= 4, dest += 4, a += 4, b += 4) {
          _mm_storeu_ps(dest, _mm_add_ps(_mm_loadu_ps(a), _mm_loadu_ps (b)));
        }
      }
      int main(int argc, char **argv) {
        floats_add((float*)0, (float*)0, (float*)0, 0);
        return 0;
      }''',
    'gcc_clang_flags': ['-msse'],
  },
  'sse2': {
    'supported': cpu_x86 or cpu_x64,
    'check_code': '''
      #include <emmintrin.h>
      void doubles_add(double *dest, double *a, double *b, unsigned size) {
        for (; size >= 4; size -= 4, dest += 4, a += 4, b += 4) {
          _mm_store_pd(dest, _mm_add_pd(_mm_loadu_pd(a), _mm_loadu_pd(b)));
        }
      }
      int main(int argc, char **argv) {
        doubles_add((double*)0, (double*)0, (double*)0, 0);
        return 0;
      }''',
    'gcc_clang_flags': ['-msse2'],
  },
  'sse3': {
    'supported': cpu_x86 or cpu_x64,
    'check_code': '''
      #include <pmmintrin.h>
      void ints_add(int *dest, int *a, int *b, unsigned size) {
        for (; size >= 4; size -= 4, dest += 4, a += 4, b += 4) {
          _mm_storeu_si128((__m128i*)dest, _mm_add_epi32(_mm_lddqu_si128((__m128i*)a), _mm_lddqu_si128((__m128i*)b)));
        }
      }
      int main(int argc, char **argv) {
        ints_add((int*)0, (int*)0, (int*)0, 0);
        return 0;
      }''',
    'gcc_clang_flags': ['-msse3'],
  },
  'sse4_1': {
    'supported': cpu_x86 or cpu_x64,
    'check_code': '''
      #include <smmintrin.h>
      void ints_mul(int *dest, int *a, int *b, unsigned size) {
        for (; size >= 4; size -= 4, dest += 4, a += 4, b += 4) {
          _mm_storeu_si128((__m128i*)dest, _mm_mullo_epi32(_mm_lddqu_si128((__m128i*)a), _mm_lddqu_si128((__m128i*)b)));
        }
      }
      int main(int argc, char **argv) {
        ints_mul((int*)0, (int*)0, (int*)0, 0);
        return 0;
      }''',
    'gcc_clang_flags': ['-msse4.1'],
  },
  'sse4_2': {
    'supported': cpu_x86 or cpu_x64,
    'check_code': '''
      #include <nmmintrin.h>
      __m128i bitmask;
      char data[16];
      int main(int argc, char **argv) {
        bitmask = _mm_cmpgt_epi64(_mm_set1_epi64x(0), _mm_loadu_si128((void*)data));
        return 0;
      }''',
    'gcc_clang_flags': ['-msse4.2'],
  },
  'mmx': {
    'supported': cpu_x86 or cpu_x64,
    'check_code': '''
      #include <mmintrin.h>
      void ints_add(int *dest, int *a, int *b, unsigned size) {
        for (; size >= 2; size -= 2, dest += 2, a += 2, b += 2) {
          *(__m64*)dest = _mm_add_pi32(*(__m64*)a, *(__m64*)b);
        }
      }
      int main(int argc, char *argv[]) {
        ints_add((int*)0, (int*)0, (int*)0, 0);
        return 0;
      }''',
    'gcc_clang_flags': ['-mmmx'],
  },
  'altivec': {
    'supported': cpu_ppc32 or cpu_ppc64,
    'check_code': '''
      #include <altivec.h>
      vector unsigned int vzero() {
          return vec_splat_u32(0);
      }
      int main(int argc, char **argv) { return 0; }''',
  },
  'armneon': {
    'supported': cpu_arm32 or cpu_arm64,
    'check_code': '''
      #include <arm_neon.h>
      void floats_add(float *dest, float *a, float *b, unsigned size) {
        for (; size >= 4; size -= 4, dest += 4, a += 4, b += 4) {
          vst1q_f32(dest, vaddq_f32(vld1q_f32(a), vld1q_f32(b)));
        }
      }
      int main(int argc, char *argv[]) {
        floats_add((float*)0, (float*)0, (float*)0, 0);
        return 0;
      }''',
  },
  'lsx': {
    'supported': cpu_loongarch64,
    'check_code': '''
      #ifndef __loongarch_sx
      #error Assembler CPP flag not enabled
      #endif
      int main(int argc, char **argv) { return 0; }''',
    'gcc_clang_flags': ['-mlsx'],
  },
  'lasx': {
    'supported': cpu_loongarch64,
    'check_code': '''
      #ifndef __loongarch_asx
      #error Assembler CPP flag not enabled
      #endif
      int main(int argc, char **argv) { return 0; }''',
    'gcc_clang_flags': ['-mlasx'],
  },
}
foreach asm, asm_flags : assembly_options
  compiler_flags = []
  if use_gcc or use_clang
    compiler_flags = asm_flags.get('gcc_clang_flags', [])
  endif
  asm_enabled = get_option(f'use_asm_@asm@').require(asm_flags.get('supported')).allowed() and cc.compiles(
    asm_flags.get('check_code'),
    args: compiler_flags,
    name: f'@asm@ assembly',
  )
  asm_up = asm.to_upper()
  cdata.set10(f'SDL_DISABLE_@asm_up@', not asm_enabled)
  if asm_enabled
    add_project_arguments(
      compiler_flags,
      language: 'c',
    )
  endif
endforeach


# Lets try to make the superproject std sane for SDL2
# https://github.com/mesonbuild/meson/issues/1889
sane_std = '''
#define _DEFAULT_SOURCE
#define _GNU_SOURCE
#define _ISOC11_SOURCE
#define _ISOC99_SOURCE
#define _POSIX_C_SOURCE 200809L
#define _XOPEN_SOURCE 700
#undef __STRICT_ANSI__
'''

# Work around missing typedefs errors
if platform_is_apple
  sane_std = '#include <sys/types.h>\n' + sane_std
endif

sdl_audio = enabled_subsystems.contains('audio')
sdl_camera = enabled_subsystems.contains('camera')
sdl_gpu = enabled_subsystems.contains('gpu')
sdl_hidapi = enabled_subsystems.contains('hidapi')
sdl_render = enabled_subsystems.contains('render')
sdl_video = enabled_subsystems.contains('video')

opt_prefer_dlopen = get_option('prefer_dlopen').require(shared_available)
opt_dlopen_notes = get_option('dlopen_notes').require(platform_is_unixlike)
opt_system_iconv = get_option('system_iconv').enable_auto_if(
  system_iconv_default,
).enabled()
opt_dbus = get_option('use_dbus').require(platform_is_unixlike)
opt_liburing = get_option('use_liburing').require(platform_is_unixlike)
opt_audio_disk = get_option('use_audio_disk').require(sdl_audio)
opt_audio_dummy = get_option('use_audio_dummy').require(sdl_audio)
opt_video_dummy = get_option('use_video_dummy').require(sdl_video)
opt_ibus = get_option('use_ibus').require(platform_is_unixlike)
opt_video_opengl = get_option('use_video_opengl').require(
  sdl_video and not platform_is_ios,
)
opt_video_opengles = get_option('use_video_opengles').require(sdl_video)
opt_audio_oss = get_option('use_audio_oss').require(
  platform_is_unixlike and sdl_audio,
)
opt_audio_alsa = get_option('use_audio_alsa').require(sdl_audio)
opt_audio_alsa_shared = get_option('use_audio_alsa_shared').require(
  opt_audio_alsa.allowed() and opt_prefer_dlopen.allowed(),
)
opt_audio_jack = get_option('use_audio_jack').require(sdl_audio)
opt_audio_jack_shared = get_option('use_audio_jack_shared').require(
  opt_audio_jack.allowed() and opt_prefer_dlopen.allowed(),
)
opt_pipewire = get_option('use_pipewire')
opt_pipewire_shared = get_option('use_pipewire_shared').require(
  opt_pipewire.allowed() and opt_prefer_dlopen.allowed(),
)
opt_audio_pulseaudio = get_option('use_audio_pulseaudio').require(sdl_audio)
opt_audio_pulseaudio_shared = get_option('use_audio_pulseaudio_shared').require(
  opt_audio_pulseaudio.allowed() and opt_prefer_dlopen.allowed(),
)
opt_audio_sndio = get_option('use_audio_sndio').require(sdl_audio)
opt_audio_sndio_shared = get_option('use_audio_sndio_shared').require(
  opt_audio_sndio.allowed() and opt_prefer_dlopen.allowed(),
)
opt_video_x11 = get_option('use_video_x11').require(sdl_video)
opt_video_x11_shared = get_option('use_video_x11_shared').require(
  opt_video_x11.allowed() and opt_prefer_dlopen.allowed(),
)
opt_fribidi = get_option('use_fribidi').require(opt_video_x11.allowed())
opt_fribidi_shared = get_option('use_fribidi_shared').require(
  opt_fribidi.allowed() and opt_prefer_dlopen.allowed(),
)
opt_libthai = get_option('use_libthai').require(opt_video_x11.allowed())
opt_libthai_shared = get_option('use_libthai_shared').require(
  opt_libthai.allowed() and opt_prefer_dlopen.allowed(),
)
opt_video_wayland = get_option('use_video_wayland').require(sdl_video)
opt_video_wayland_shared = get_option('use_video_wayland_shared').require(
  opt_video_wayland.allowed() and opt_prefer_dlopen.allowed(),
)
opt_video_wayland_libdecor = get_option('use_video_wayland_libdecor').require(
  opt_video_wayland.allowed(),
)
opt_video_wayland_libdecor_shared = get_option(
  'use_video_wayland_libdecor_shared',
).require(
  opt_video_wayland_libdecor.allowed() and opt_video_wayland_shared.allowed() and opt_prefer_dlopen.allowed(),
)
opt_video_rpi = get_option('use_video_rpi').require(
  sdl_video and platform_is_unixlike and (
    cpu_arm32
    or cpu_arm64
  ),
)
opt_video_rockchip = get_option('use_video_rockchip').require(
  sdl_video and platform_is_unixlike and (
    cpu_arm32
    or cpu_arm64
  ),
)
opt_video_cocoa = get_option('use_video_cocoa').require(platform_is_apple)
opt_joystick_xinput = get_option('use_joystick_xinput').require(
  platform_is_windows,
)
opt_directx = get_option('use_directx').require(
  (sdl_audio or sdl_video) and platform_is_windows,
)
opt_audio_wasapi = get_option('use_audio_wasapi').require(
  sdl_audio and platform_is_windows,
)
opt_render_d3d = get_option('use_render_d3d').require(
  sdl_render and opt_directx.allowed(),
)
opt_render_d3d11 = get_option('use_render_d3d11').require(
  sdl_render and opt_directx.allowed(),
)
opt_render_d3d12 = get_option('use_render_d3d12').require(
  sdl_render and opt_directx.allowed(),
)
opt_render_metal = get_option('use_render_metal').require(
  sdl_render and platform_is_apple,
)
opt_render_gpu = get_option('use_render_gpu').require(sdl_render and sdl_gpu)
opt_video_vivante = get_option('use_video_vivante').require(
  platform_is_unixlike and cpu_arm32,
)
opt_video_vulkan = get_option('use_video_vulkan').require(
  sdl_video and (
    platform_is_android
    or platform_is_apple
    or platform_is_linux
    or platform_is_freebsd
    or platform_is_openbsd
    or platform_is_windows
  ),
)
opt_video_metal = get_option('use_video_metal').require(platform_is_apple)
opt_video_openvr = get_option('use_video_openvr')
opt_video_kmsdrm = get_option('use_video_kmsdrm').require(sdl_video)
opt_video_kmsdrm_shared = get_option('use_video_kmsdrm_shared').require(
  opt_video_kmsdrm.allowed() and opt_prefer_dlopen.allowed(),
)
opt_video_offscreen = get_option('use_video_offscreen')
opt_camera_dummy = get_option('use_camera_dummy').require(sdl_camera)
opt_backgrounding_signal = get_option('backgrounding_signal')
opt_foregrounding_signal = get_option('foregrounding_signal')
opt_hidapi_libusb = get_option('use_hidapi_libusb').require(
  sdl_hidapi and hidapi_libusb_available,
)
opt_hidapi_libusb_shared = get_option('hidapi_libusb_shared').require(
  opt_hidapi_libusb.allowed() and opt_prefer_dlopen.allowed(),
)
opt_joystick_hidapi = get_option('use_joystick_hidapi').require(sdl_hidapi)
opt_joystick_virtual = get_option('use_joystick_virtual').require(sdl_hidapi)
opt_libudev = get_option('libudev').require(platform_is_unixlike)
opt_lean_and_mean = get_option('lean_and_mean')

basic_headers = [
  'float.h',
  'stdarg.h',
  'stddef.h',
  'stdint.h',
  'alloca.h',
  'iconv.h',
  'inttypes.h',
  'limits.h',
  'malloc.h',
  'math.h',
  'memory.h',
  'signal.h',
  'stdio.h',
  'stdlib.h',
  'strings.h',
  'string.h',
  'sys/types.h',
  'wchar.h',
  'pthread_np.h',
  'linux/input.h',
  'dlfcn.h',
  'pthread.h',
  'semaphore.h',
  'sys/inotify.h',
]

check_functions = '''
  abs acos acosf asin asinf atan atan2 atan2f atanf atof atoi
  bcopy
  ceil ceilf copysign copysignf cos cosf
  _Exit exp expf
  fabs fabsf floor floorf fmod fmodf fopen64 fseeko fseeko64
  getenv
  _i64toa index itoa
  log log10 log10f logf lround lroundf _ltoa
  malloc memcmp memcpy memmove memset modf modff
  pow powf putenv
  rindex round roundf
  scalbn scalbnf setenv sin sinf sqr sqrt sqrtf sscanf strchr
  strcmp strlcat strlcpy strlen strncmp strnlen strpbrk
  strrchr strstr strnstr strtod strtok_r strtol strtoll strtoul strtoull
  tan tanf trunc truncf
  unsetenv
  vsnprintf vsscanf
  wcsnlen wcscmp wcsdup wcslcat wcslcpy wcslen wcsncmp wcsstr wcstol

  dlopen
  clock_gettime
  pthread_setname_np
  pthread_set_name_np
  sem_timedwait
  inotify_init
  inotify_init1
  '''

if platform_is_windows
  check_functions += ' _copysign _fseeki64 _strrev _ui64toa _ultoa _wcsdup'

  if opt_directx.allowed()
    basic_headers += [
      'ddraw.h',
      'dsound.h',
      'dinput.h',
    ]
  endif
  basic_headers += 'dxgi.h'
  basic_headers += 'dxgi1_5.h'
  basic_headers += 'dxgi1_6.h'
  basic_headers += 'mfapi.h'
  basic_headers += 'mmdeviceapi.h'
  basic_headers += 'roapi.h'
  basic_headers += 'sensorsapi.h'
  basic_headers += 'shellscalingapi.h'
  basic_headers += 'tpcshrd.h'

  # Microsoft Windows GameInput is provided via the Microsoft Game Development Kit (GDK)
  have_gameinput_header_code = '''
    #include <stdbool.h>
    #define COBJMACROS
    #include <gameinput.h>
    int main(int argc, char **argv) {  }
  '''
  cdata.set10(
    'HAVE_GAMEINPUT_H',
    cc.compiles(
      have_gameinput_header_code,
      name: 'have GameInput support',
    ),
  )

  # Microsoft Windows gaming input header is provided by the Windows SDK (winrt)
  have_windows_gaming_input_header_code = '''
    #define COBJMACROS
    #include <windows.gaming.input.h>
    static __x_ABI_CWindows_CGaming_CInput_CIGamepadStatics2 *s2;
    int main(int argc, char **argv) {  }
  '''
  cdata.set10(
    'HAVE_WINDOWS_GAMING_INPUT_H',
    cc.compiles(
      have_windows_gaming_input_header_code,
      name: 'have Windows Gaming Input support',
    ),
  )

  if opt_joystick_xinput.allowed()
    # XInput(legacy) is provided by the Microsoft DirectX SDK and requires windows header include
    have_xinput_header_code = '''
      #include <windows.h>
      #include <xinput.h>
      int main(int argc, char **argv) { }
    '''
    cdata.set10(
      'HAVE_XINPUT_H',
      cc.compiles(
        have_xinput_header_code,
        name: 'have XInput support',
      ),
    )
  endif
else
  check_functions += ' strcasestr'

  basic_headers += 'unistd.h'
  check_functions += ' fdatasync gethostname getpagesize getresgid getresuid sysconf'

  check_functions += ' sigaction sigtimedwait'

  basic_headers += 'setjmp.h'
  check_functions += ' setjmp'

  basic_headers += 'time.h'
  check_functions += ' nanosleep gmtime_r localtime_r'

  basic_headers += 'langinfo.h'
  check_functions += ' nl_langinfo'

  basic_headers += 'sys/sysctl.h'
  check_functions += ' sysctlbyname'

  basic_headers += 'sys/auxv.h'
  check_functions += ' getauxval elf_aux_info'

  basic_headers += 'poll.h'
  check_functions += ' ppoll'

  basic_headers += 'sys/mman.h'
  check_functions += ' memfd_create'

  basic_headers += 'fcntl.h'
  check_functions += ' posix_fallocate'

  basic_headers += 'spawn.h'
  check_functions += ' posix_spawn_file_actions_addchdir posix_spawn_file_actions_addchdir_np'
endif

found_headers = []

foreach hname : basic_headers
  define = 'HAVE_@0@'.format(hname.underscorify().to_upper())
  if cc.has_header(hname)
    cdata.set10(define, true)
    found_headers += hname
  endif
endforeach

headers_prefix = sane_std
foreach h : found_headers
  headers_prefix += f'#include <@h@>\n'
endforeach

foreach f : check_functions.split()
  cdata.set10(
    'HAVE_@0@'.format(f.to_upper()),
    cc.has_function(
      f,
      prefix: headers_prefix,
      dependencies: sdl_deps,
    ),
  )
endforeach

# Math function checks
# (<math_fn>, <math_fn> handles float, <math_fn>f)
foreach math_fn : ['isinf', 'isnan']
  math_fn_define = math_fn.to_upper()
  cdata.set10(
    f'HAVE_@math_fn_define@',
    cc.compiles(
      f'''
    #include <math.h>
    int main() {
      double d = 3.14159;
      return @math_fn@(d);
    } ''',
      name: f'have @math_fn@',
      dependencies: sdl_deps,
    ),
  )
  cdata.set10(
    f'HAVE_@math_fn_define@_FLOAT_MACRO',
    cc.compiles(
      f'''
    #include <math.h>
    int main() {
      double f = 3.14159f;
      return @math_fn@(f);
    } ''',
      name: f'@math_fn@ handles float',
      dependencies: sdl_deps,
    ),
  )
  cdata.set10(
    f'HAVE_@math_fn_define@F',
    cc.compiles(
      f'''
    #include <math.h>
    int main() {
      double f = 3.14159f;
      return @math_fn@f(f);
    } ''',
      name: f'have @math_fn@f',
      dependencies: sdl_deps,
    ),
  )
endforeach

cdata.set10(
  'HAVE_SA_SIGACTION',
  cc.has_member(
    'struct sigaction',
    'sa_sigaction',
    prefix: headers_prefix,
  ),
)
cdata.set10(
  'HAVE_ST_MTIM',
  cc.has_member(
    'struct stat',
    'st_mtim',
    prefix: headers_prefix,
  ),
)
cdata.set10(
  'HAVE_O_CLOEXEC',
  cc.compiles(
    '''
    #include <fcntl.h>
    int flag = O_CLOEXEC;
    int main(int argc, char **argv) { return 0; }''',
    name: 'have O_CLOEXEC',
  ),
)

if platform_is_unixlike_or_apple
  cdata.set('SDL_THREAD_PTHREAD', 1)
  cdata.set10(
    'SDL_THREAD_PTHREAD_RECURSIVE_MUTEX',
    cc.compiles(
      '''
    #include <pthread.h>
    int main(int argc, char **argv) {
      pthread_mutexattr_t attr;
      pthread_mutexattr_settype(&attr, PTHREAD_MUTEX_RECURSIVE);
      return 0;
    }''',
      name: 'have PTHREAD_MUTEX_RECURSIVE',
    ),
  )
  if cdata.get('SDL_THREAD_PTHREAD_RECURSIVE_MUTEX', 0) == 0
    cdata.set10(
      'SDL_THREAD_PTHREAD_RECURSIVE_MUTEX_NP',
      cc.compiles(
        '''
      #include <pthread.h>
      int main(int argc, char **argv) {
        pthread_mutexattr_t attr;
        pthread_mutexattr_settype(&attr, PTHREAD_MUTEX_RECURSIVE_NP);
        return 0;
      }''',
        name: 'have PTHREAD_MUTEX_RECURSIVE_NP',
      ),
    )
  endif
elif platform_is_windows
  cdata.set('SDL_THREAD_WINDOWS', 1)
  cdata.set('SDL_THREAD_GENERIC_COND_SUFFIX', 1)
  cdata.set('SDL_THREAD_GENERIC_RWLOCK_SUFFIX', 1)
endif

if opt_system_iconv
  iconv_in_libc = cc.compiles(
    '''
    #define LIBICONV_PLUG 1 /* in case libiconv header is in include path */
    #include <stddef.h>
    #include <iconv.h>
    int main(int argc, char **argv) {
        return !iconv_open(NULL,NULL);
    }''',
    dependencies: sdl_deps,
    name: 'iconv (libc)',
  )
  iconv_dep = dependency(
    'iconv',
    method: 'system',
    required: false,
  )
  iconv_in_libiconv = cc.compiles(
    '''
    #include <stddef.h>
    #include <iconv.h>
    int main(int argc, char **argv) {
        return !iconv_open(NULL,NULL);
    }''',
    dependencies: sdl_deps + [iconv_dep],
    name: 'iconv (libiconv)',
  )

  cdata.set10('HAVE_ICONV', iconv_in_libc or iconv_in_libiconv)
  if (iconv_in_libiconv and (get_option('libiconv') or not iconv_in_libc))
    cdata.set10('SDL_USE_LIBICONV', true)
    sdl_deps += iconv_dep
  endif
endif

if opt_dbus.allowed()
  dbus_dep = dependency(
    'dbus-1',
    required: opt_dbus,
  ).partial_dependency(
    compile_args: true,
    includes: true,
    sources: true,
  )
  dbus_available = dbus_dep.found() and cc.has_header(
    'dbus/dbus.h',
    dependencies: sdl_deps + [dbus_dep],
  )
  cdata.set10('HAVE_DBUS_DBUS_H', dbus_available)
  cdata.set10('HAVE_FCITX', dbus_available)
  sdl_deps += dbus_dep
endif
have_dbus = cdata.get('HAVE_DBUS_DBUS_H', 0) != 0

if opt_ibus.allowed()
  ibus_dep = dependency(
    'ibus-1.0',
    required: opt_ibus,
  ).partial_dependency(
    compile_args: true,
    includes: true,
    sources: true,
  )
  ibus_available = ibus_dep.found() and cdata.get('HAVE_SYS_NOTIFY_H', 0) != 0 and cc.has_header(
    'ibus/ibus.h',
    dependencies: ibus_dep,
  )
  if ibus_available
    cdata.set10('HAVE_IBUS_IBUS_H', ibus_available)
    sdl_deps += ibus_dep
  endif
endif

cdata.set10(
  'HAVE_INOTIFY',
  cdata.get('HAVE_SYS_INOTIFY_H', 0) != 0 and cdata.get('HAVE_INOTIFY_INIT', 0) != 0,
)

dlopen_table = []

if opt_hidapi_libusb.allowed()
  libusb_dep = dependency(
    'libusb-1.0',
    required: opt_hidapi_libusb,
  )
  cdata.set10('HAVE_LIBUSB', libusb_dep.found())
  sdl_deps += libusb_dep
  dlopen_table += {
    'option': opt_hidapi_libusb_shared,
    'dep_var': 'libusb_dep',
    'lib': 'usb-1.0',
    'conf_var': 'SDL_LIBUSB_DYNAMIC',
  }
endif

if opt_libudev.allowed()
  libudev_dep = dependency(
    'libudev',
    required: opt_libudev,
  )
  have_libudev = libudev_dep.found() and cc.has_header(
    'libudev.h',
    dependencies: libudev_dep,
  )
  cdata.set10('HAVE_LIBUDEV_H', have_libudev)
  if have_libudev
    sdl_deps += libudev_dep
    dlopen_table += {
      'option': opt_libudev,
      'dep_var': 'libudev_dep',
      'lib': 'udev',
      'conf_var': 'SDL_UDEV_DYNAMIC',
    }
  endif
endif

sources = []

cdata.set('SDL_XKBCOMMON_VERSION_MAJOR', 0)
cdata.set('SDL_XKBCOMMON_VERSION_MINOR', 0)
cdata.set('SDL_XKBCOMMON_VERSION_PATCH', 0)

cdata.set('SDL_LIBDECOR_VERSION_MAJOR', 0)
cdata.set('SDL_LIBDECOR_VERSION_MINOR', 0)
cdata.set('SDL_LIBDECOR_VERSION_PATCH', 0)

if platform_is_apple
  add_languages(
    'objc',
    native: false,
  )
  add_project_arguments(
    '-fobjc-arc',
    language: 'objc',
  )
endif

if platform_is_linux
  cdata.set('SDL_PLATFORM_LINUX', 1)
  cdata.set10('SDL_INPUT_LINUXEV', cdata.get('HAVE_LINUX_INPUT_H', 0) != 0)
elif platform_is_windows
  cdata.set('SDL_PLATFORM_WIN32', 1)
  sdl_deps += cc.find_library('version')
  sdl_deps += cc.find_library('imm32')
  sdl_deps += cc.find_library('setupapi')
  sdl_deps += cc.find_library('winmm')
  sdl_deps += cc.find_library('opengl32')
elif platform_is_macos
  cdata.set('SDL_PLATFORM_APPLE', 1)
  cdata.set10('SDL_VIDEO_METAL', opt_video_metal.allowed())
  apple_modules = []
  if opt_video_metal.allowed()
    apple_modules += ['Metal']
  endif
  sdl_deps += dependency(
    'appleframeworks',
    modules: [
      'AudioToolbox',
      'AVFoundation',
      'Carbon',
      'Cocoa',
      'CoreAudio',
      'CoreFoundation',
      'CoreGraphics',
      'CoreHaptics',
      'CoreMedia',
      'CoreVideo',
      'ForceFeedback',
      'Foundation',
      'GameController',
      'IOKit',
      'QuartzCore',
      'UniformTypeIdentifiers',
    ] + apple_modules,
  )
else
  error('Platform not yet supported.')
endif

if get_option('default_library') == 'both' and cc.get_argument_syntax() == 'msvc'
  error('default_library=both not supported when compiling with MSVC')
endif

cdata.set10('DYNAPI_NEEDS_DLOPEN', platform_is_unixlike_or_apple)

if opt_dlopen_notes.allowed()
  compiler_supports_elfnotes = cc.compiles(
    '''
    #ifndef __ELF__
      ELF DL notes is only supported on ELF platforms
    #endif
    __attribute__ ((used,aligned(4),section(".note.dlopen"))) static const struct {
      struct { int a; int b; int c; } hdr; char name[4]; __attribute__((aligned(4))) char json[24];
    } dlnote = { { 4, 0x407c0c0aU, 16 }, "FDO", "[\"a\":{\"a\":\"1\",\"b\":\"2\"}]" };
    int main(int argc, char *argv[]) {
      return argc + dlnote.hdr.a;
    }''',
    name: 'compiler supports ELF notes',
    required: opt_dlopen_notes,
  )
  cdata.set10('SDL_DISABLE_DLOPEN_NOTES', not compiler_supports_elfnotes)
endif

if (sdl_audio or sdl_camera) and opt_pipewire.enable_auto_if(
  platform_is_unixlike,
).enabled()
  pipewire_dep = dependency(
    'libpipewire-0.3',
    required: opt_pipewire,
  )
  sdl_deps += pipewire_dep
  have_pipewire = pipewire_dep.found()
else
  have_pipewire = false
endif

subdir('src')

if cdata.get('SDL_VIDEO_DRIVER_WAYLAND', 0) != 0
  wayland_scanner = find_program('wayland-scanner')
  subdir('wayland-protocols')
endif

if opt_prefer_dlopen.allowed()
  find_dylib_name = find_program(
    './find-dylib-name.py',
    required: true,
  )

  foreach dep_entry : dlopen_table
    opt = dep_entry['option']
    if not opt.allowed()
      continue
    endif
    dep = get_variable(dep_entry['dep_var'])
    if dep.found()
      r = run_command(
        find_dylib_name,
        dep_entry['lib'],
        cc.cmd_array(),
        check: false,
      )

      if r.returncode() == 0
        lib = r.stdout().strip()
        cdata.set_quoted(dep_entry['conf_var'], lib)
        set_variable(
          dep_entry['dep_var'],
          dep.partial_dependency(
            compile_args: true,
            includes: true,
            sources: true,
          ),
        )
        message('Configured @0@ for dynamic loading'.format(lib))
      elif opt.enabled()
        error(f'Can\'t configure @lib@ for dynamic loading:', r.stderr())
      endif
    endif
  endforeach
endif

configure_file(
  input: 'include/build_config/SDL_build_config.h.cmake',
  output: 'SDL_build_config.h',
  configuration: cdata,
  format: 'cmake',
)

if get_option('default_library') == 'shared'
  extra_args = ['-DDLL_EXPORT']
else
  extra_args = []
endif

if opt_backgrounding_signal != 'OFF'
  extra_args += f'-DSDL_BACKGROUNDING_SIGNAL=@opt_backgrounding_signal@'
endif
if opt_foregrounding_signal != 'OFF'
  extra_args += f'-DSDL_FOREGROUNDING_SIGNAL=@opt_foregrounding_signal@'
endif
if opt_lean_and_mean
  extra_args += '-DSDL_LEAN_AND_MEAN'
endif

sdl_lib = library(
  'SDL3',
  sources,
  include_directories: ['include', 'src'],
  c_args: extra_args,
  dependencies: sdl_deps,
  install: true,
)

sdl3_dep = declare_dependency(
  include_directories: 'include',
  link_with: sdl_lib,
  dependencies: sdl_deps,
)

meson.override_dependency('sdl3', sdl3_dep)

