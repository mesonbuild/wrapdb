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

# END platform detection logic

use_gcc = cc.get_id() == 'gcc'
use_clang = cc.get_id() == 'clang'
use_msvc = cc.get_id() == 'msvc'

# The hidraw support doesn't catch Xbox, PS4 and Nintendo controllers,
#  so we'll just use libusb when it's available. libusb does not support iOS,
#  so we default to yes on iOS.
hidapi_libusb_available = not (platform_is_apple or platform_is_android)

gcc_atomics_supported = use_gcc or use_clang
system_iconv_default = not (platform_is_windows or platform_is_apple)
oss_default = platform_is_unixlike and not (
  platform_is_linux
  or platform_is_netbsd
  or platform_is_openbsd
)

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
sdl_hidapi = enabled_subsystems.contains('hidapi')
sdl_video = enabled_subsystems.contains('video')

opt_system_iconv = get_option('system_iconv').enable_auto_if(
  system_iconv_default,
).enabled()
opt_dbus = get_option('use_dbus').require(platform_is_unixlike)
opt_audio_disk = get_option('use_audio_disk').require(sdl_audio)
opt_audio_dummy = get_option('use_audio_dummy').require(sdl_audio)
opt_video_dummy = get_option('use_video_dummy').require(sdl_video)
opt_audio_oss = get_option('use_audio_oss').require(
  platform_is_unixlike and sdl_audio,
)
opt_audio_alsa = get_option('use_audio_alsa').require(sdl_audio)
opt_audio_jack = get_option('use_audio_jack').require(sdl_audio)
opt_pipewire = get_option('use_pipewire')
opt_audio_pulseaudio = get_option('use_audio_pulseaudio').require(sdl_audio)
opt_audio_sndio = get_option('use_audio_sndio').require(sdl_audio)
opt_video_x11 = get_option('use_video_x11').require(sdl_video)
opt_video_wayland = get_option('use_video_wayland').require(sdl_video)
opt_video_wayland_libdecor = get_option('use_video_wayland_libdecor').require(
  opt_video_wayland.allowed(),
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
opt_directx = get_option('use_directx').require(
  (sdl_audio or sdl_video) and platform_is_windows,
)
opt_audio_wasapi = get_option('use_audio_wasapi').require(
  sdl_audio and platform_is_windows,
)
opt_video_vivante = get_option('use_video_vivante').require(
  platform_is_unixlike and cpu_arm32,
)
opt_video_metal = get_option('use_video_metal').require(platform_is_apple)
opt_video_kmsdrm = get_option('use_video_kmsdrm').require(sdl_video)
opt_video_offscreen = get_option('use_video_offscreen')
opt_hidapi_libusb = get_option('use_hidapi_libusb').require(
  sdl_hidapi and hidapi_libusb_available,
)

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
  basic_headers += 'mmdeviceapi.h'
  basic_headers += 'roapi.h'
  basic_headers += 'shellscalingapi.h'
  basic_headers += 'tpcshrd.h'
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

cdata.set10(
  'HAVE_INOTIFY',
  cdata.get('HAVE_SYS_INOTIFY_H', 0) != 0 and cdata.get('HAVE_INOTIFY_INIT', 0) != 0,
)

if opt_hidapi_libusb.allowed()
  libusb_dep = dependency(
    'libusb-1.0',
    required: opt_hidapi_libusb,
  )
  cdata.set10('HAVE_LIBUSB', libusb_dep.found())
  sdl_deps += libusb_dep
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

  ## some of these checks could be done via have include
  ## but it is done this way to be consistent from what CMake does
  ## additionally these values are not defined in the config file

  # check Kronos EGL support
  have_opengl_egl_code = '''
    #define EGL_API_FB
    #define MESA_EGL_NO_X11_HEADERS
    #define EGL_NO_X11
    #include <EGL/egl.h>
    #include <EGL/eglext.h>
    int main (int argc, char** argv) { return 0; }
  '''
  have_opengl_egl = cc.compiles(
    have_opengl_egl_code,
    name: 'have OpenGL EGL support',
  )
  # check OpenGL GLX support
  have_opengl_glx_code = '''
    #include <GL/glx.h>
    int main(int argc, char** argv) { return 0; }
  '''
  have_opengl_glx = cc.compiles(
    have_opengl_glx_code,
    name: 'have OpenGL GLX support',
  )

  # check OpenGL support
  have_opengl_code = '''
    #include <GL/gl.h>
    #include <GL/glext.h>
    int main(int argc, char** argv) { return 0; }
  '''
  have_opengl = cc.compiles(
    have_opengl_code,
    name: 'have OpenGL support',
  )


  # ideally this should have a check for compile like the cmake configuration, see sdlchecks.cmake
  cdata.set('SDL_PLATFORM_LINUX', 1)
  cdata.set('SDL_THREAD_PTHREAD', 1)
  cdata.set('SDL_LOADSO_DLOPEN', 1)
  cdata.set('SDL_PROCESS_POSIX', 1)
  cdata.set('SDL_SENSOR_DUMMY', 1)
  cdata.set('SDL_POWER_LINUX', 1)
  cdata.set('SDL_INPUT_LINUXEV', 1)
  if have_opengl_egl
    cdata.set('SDL_VIDEO_OPENGL_EGL', 1)
  endif
  if have_opengl_glx
    cdata.set('SDL_VIDEO_OPENGL_GLX', 1)
  endif
  if have_opengl
    cdata.set('SDL_VIDEO_OPENGL', 1)
    cdata.set('SDL_VIDEO_RENDER_OGL', 1)
  endif
  cdata.set('SDL_GPU_VULKAN', 1)
  cdata.set('SDL_VIDEO_VULKAN', 1)
  cdata.set('SDL_VIDEO_RENDER_VULKAN', 1)
  cdata.set('SDL_TIMER_UNIX', 1)
  sdl_deps += dependency('libudev')
elif platform_is_windows

  # XInput(legacy) is provided by the Microsoft DirectX SDK and requires windows header include
  have_xinput_header_code = '''
    #include <windows.h>
    #include <xinput.h>
    int main(int argc, char **argv) { }
  '''
  have_xinput_header = cc.compiles(
    have_xinput_header_code,
    name: 'have XInput support',
  )

  # Microsoft Windows gaming input header is provided by the Windows SDK (winrt)
  have_windows_gaming_input_header_code = '''
    #define COBJMACROS
    #include <windows.gaming.input.h>
    static __x_ABI_CWindows_CGaming_CInput_CIGamepadStatics2 *s2;
    int main(int argc, char **argv) {  }
  '''
  have_windows_gaming_input_header = cc.compiles(
    have_windows_gaming_input_header_code,
    name: 'have Windows Gaming Input support',
  )

  # Microsoft Windows GameInput is provided via the Microsoft Game Development Kit (GDK)
  have_gameinput_header_code = '''
    #include <stdbool.h>
    #define COBJMACROS
    #include <gameinput.h>
    int main(int argc, char **argv) {  }
  '''
  have_gameinput_header = cc.compiles(
    have_gameinput_header_code,
    name: 'have GameInput support',
  )
  add_languages(
    'cpp',
    native: false,
  )


  cdata.set('SDL_PLATFORM_WIN32', 1)
  cdata.set('SDL_THREAD_WINDOWS', 1)
  cdata.set('SDL_THREAD_GENERIC_COND_SUFFIX', 1)
  cdata.set('SDL_THREAD_GENERIC_RWLOCK_SUFFIX', 1)
  cdata.set('SDL_LOADSO_WINDOWS', 1)
  cdata.set('SDL_PROCESS_WINDOWS', 1)
  cdata.set('SDL_SENSOR_WINDOWS', 1)
  cdata.set('SDL_POWER_WINDOWS', 1)
  cdata.set('SDL_VIDEO_RENDER_D3D12', 1)
  cdata.set('SDL_GPU_VULKAN', 1)
  cdata.set('SDL_GPU_D3D12', 1)
  cdata.set('SDL_VIDEO_VULKAN', 1)
  cdata.set('SDL_VIDEO_RENDER_VULKAN', 1)
  cdata.set('SDL_VIDEO_OPENGL', 1)
  cdata.set('SDL_VIDEO_OPENGL_WGL', 1)
  cdata.set('SDL_VIDEO_RENDER_OGL', 1)

  if have_xinput_header
    cdata.set('SDL_JOYSTICK_XINPUT', 1)
    cdata.set('HAVE_XINPUT', true)
  endif
  if have_windows_gaming_input_header
    cdata.set('SDL_JOYSTICK_WGI', 1)
  endif
  if have_gameinput_header
    cdata.set('HAVE_GAMEINPUT_H', 1)
    cdata.set('SDL_JOYSTICK_GAMEINPUT', 1)
  endif
  cdata.set('SDL_JOYSTICK_RAWINPUT', 1)

  cdata.set('SDL_TIMER_WINDOWS', 1)
  sdl_deps += cc.find_library('version')
  sdl_deps += cc.find_library('imm32')
  sdl_deps += cc.find_library('setupapi')
  sdl_deps += cc.find_library('winmm')
  sdl_deps += cc.find_library('opengl32')
elif platform_is_macos
  cdata.set('SDL_PLATFORM_APPLE', 1)
  cdata.set('SDL_THREAD_PTHREAD', 1)
  cdata.set('SDL_THREAD_PTHREAD_RECURSIVE_MUTEX', 1)
  cdata.set('SDL_LOADSO_DLOPEN', 1)
  cdata.set('SDL_PROCESS_POSIX', 1)
  cdata.set('SDL_FILESYSTEM_COCOA', 1)
  cdata.set('SDL_VIDEO_OPENGL_CGL', 1)
  cdata.set('SDL_VIDEO_OPENGL', 1)
  cdata.set('SDL_FSOPS_POSIX', 1)
  cdata.set('SDL_SENSOR_DUMMY', 1)
  cdata.set('SDL_POWER_MACOSX', 1)
  cdata.set('SDL_VIDEO_RENDER_GPU', 1)
  cdata.set('SDL_GPU_VULKAN', 1)
  cdata.set('SDL_VIDEO_VULKAN', 1)
  cdata.set('SDL_VIDEO_RENDER_VULKAN', 1)
  cdata.set('SDL_TIMER_UNIX', 1)
  cdata.set10('SDL_VIDEO_METAL', opt_video_metal.allowed())
  cdata.set10('SDL_GPU_METAL', cdata.get('SDL_VIDEO_METAL', 0) != 0)
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

subdir('src')

if cdata.get('SDL_VIDEO_DRIVER_WAYLAND', 0) != 0
  wayland_scanner = find_program('wayland-scanner')
  subdir('wayland-protocols')
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

