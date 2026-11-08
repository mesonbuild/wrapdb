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

use_gcc = cc.get_id() == 'gcc'
use_clang = cc.get_id() == 'clang'
use_msvc = cc.get_id() == 'msvc'
gcc_atomics_supported = use_gcc or use_clang

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

basic_headers = [
  ['float.h'],
  ['stdarg.h'],
  ['stddef.h'],
  ['stdint.h'],
  ['alloca.h'],
  ['iconv.h'],
  ['inttypes.h'],
  ['limits.h'],
  ['malloc.h'],
  ['math.h'],
  ['memory.h'],
  ['signal.h'],
  ['stdio.h'],
  ['stdlib.h'],
  ['strings.h'],
  ['string.h'],
  ['sys/types.h'],
  ['wchar.h'],
  ['pthread_np.h'],
  ['linux/input.h'],
  ['ddraw.h'],
  ['dsound.h'],
  ['dinput.h'],
  ['dlfcn.h'],
  ['unistd.h'],
  ['setjmp.h'],
  ['time.h'],
  ['sys/sysctl.h'],
  ['pthread.h'],
  ['semaphore.h'],
  ['poll.h'],
  ['sys/inotify.h'],
]

check_functions = '''
  abs acos acosf asin asinf atan atan2 atan2f atanf atof atoi
  bcopy
  ceil ceilf copysign copysignf cos cosf
  exp expf
  fabs fabsf floor floorf fmod fmodf fseeko fseeko64
  getenv
  index
  log log10 log10f logf
  malloc memcmp memcpy memmove memset
  pow putenv
  rindex round
  scalbn setenv sin sinf sqrt sqrtf sscanf strchr
  strcmp strlcat strlcpy strlen strncmp strnlen
  strrchr strstr strtod strtok_r strtol strtoll strtoul strtoull
  unsetenv
  vsnprintf vsscanf
  dlopen
  fdatasync
  _strrev
  isinf
  isinff
  isnan
  isnanf
  sigaction
  sigtimedwait
  setjmp
  nanosleep
  gmtime_r
  sysconf
  sysctlbyname
  clock_gettime
  getpagesize
  pthread_setname_np
  pthread_set_name_np
  sem_timedwait
  poll
  inotify_init1
  '''
# check token ['HAVE_GETHOSTNAME']
# check token ['HAVE_WCSLEN']
# check token ['HAVE_WCSNLEN']
# check token ['HAVE_WCSLCPY']
# check token ['HAVE_WCSLCAT']
# check token ['HAVE_WCSSTR']
# check token ['HAVE_WCSCMP']
# check token ['HAVE_WCSNCMP']
# check token ['HAVE_WCSTOL']
# check token ['HAVE_STRPBRK']
# check token ['HAVE_STRNSTR']
# check token ['HAVE_ITOA']
# check token ['HAVE__LTOA']
# check token ['HAVE__UITOA']
# check token ['HAVE__ULTOA']
# check token ['HAVE__I64TOA']
# check token ['HAVE__UI64TOA']
# check token ['HAVE__COPYSIGN']
# check token ['HAVE_ISINF_FLOAT_MACRO']
# check token ['HAVE_ISNAN_FLOAT_MACRO']
# check token ['HAVE_LROUND']
# check token ['HAVE_LROUNDF']
# check token ['HAVE_MODF']
# check token ['HAVE_MODFF']
# check token ['HAVE_POWF']
# check token ['HAVE_ROUNDF']
# check token ['HAVE_SCALBNF']
# check token ['HAVE_TAN']
# check token ['HAVE_TANF']
# check token ['HAVE_TRUNC']
# check token ['HAVE_TRUNCF']
# check token ['HAVE__FSEEKI64']
# check token ['HAVE_FOPEN64']
# check token ['HAVE_MEMFD_CREATE']
# check token ['HAVE_POSIX_FALLOCATE']
# check token ['HAVE_SA_SIGACTION']
# check token ['HAVE_ST_MTIM']
# check token ['HAVE_LOCALTIME_R']
# check token ['HAVE_NL_LANGINFO']
# check token ['HAVE_ICONV']
# check token ['HAVE_GETAUXVAL']
# check token ['HAVE_ELF_AUX_INFO']
# check token ['HAVE__EXIT']
# check token ['HAVE_FCITX']
# check token ['HAVE_INOTIFY']
# check token ['HAVE_LIBUSB']
# check token ['HAVE_O_CLOEXEC']

found_headers = []

foreach i : basic_headers
  hname = i[0]
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
      dependencies: [sdl_deps],
    ),
  )
endforeach

cdata.set('HAVE_HIDAPI', 1)

sources = []

cdata.set('SDL_XKBCOMMON_VERSION_MAJOR', 0)
cdata.set('SDL_XKBCOMMON_VERSION_MINOR', 0)
cdata.set('SDL_XKBCOMMON_VERSION_PATCH', 0)

if host_machine.system() == 'darwin'
  add_languages(
    'objc',
    native: false,
  )
  add_project_arguments(
    '-fobjc-arc',
    language: 'objc',
  )
endif

if host_machine.system() == 'linux'

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
  sdl_deps += dependency(
    'libusb-1.0',
    required: true,
  )
  cdata.set('SDL_HIDAPI_LIBUSB', 1)
  sdl_deps += dependency('libudev')
  sdl_deps += dependency('dbus-1')
  sdl_deps += dependency('libpipewire-0.3')
  sdl_deps += dependency('wayland-client')
  sdl_deps += dependency('wayland-egl')
  sdl_deps += dependency('wayland-cursor')
  xkbcommon_dep = dependency('xkbcommon')
  sdl_deps += xkbcommon_dep
  cdata.set('HAVE_DBUS_DBUS_H', 1)
  wayland_scanner = find_program('wayland-scanner')
  subdir('wayland-protocols')
elif host_machine.system() == 'windows'

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
elif host_machine.subsystem() == 'macos'
  cdata.set('SDL_PLATFORM_APPLE', 1)
  cdata.set('SDL_THREAD_PTHREAD', 1)
  cdata.set('SDL_THREAD_PTHREAD_RECURSIVE_MUTEX', 1)
  cdata.set('SDL_LOADSO_DLOPEN', 1)
  cdata.set('SDL_PROCESS_POSIX', 1)
  cdata.set('SDL_FILESYSTEM_COCOA', 1)
  cdata.set('SDL_VIDEO_DRIVER_COCOA', 1)
  cdata.set('SDL_VIDEO_OPENGL_CGL', 1)
  cdata.set('SDL_VIDEO_OPENGL', 1)
  cdata.set('SDL_FSOPS_POSIX', 1)
  cdata.set('SDL_SENSOR_DUMMY', 1)
  cdata.set('SDL_POWER_MACOSX', 1)
  cdata.set('SDL_VIDEO_RENDER_GPU', 1)
  cdata.set('SDL_GPU_VULKAN', 1)
  cdata.set('SDL_GPU_METAL', 1)
  cdata.set('SDL_VIDEO_VULKAN', 1)
  cdata.set('SDL_VIDEO_METAL', 1)
  cdata.set('SDL_VIDEO_RENDER_VULKAN', 1)
  cdata.set('SDL_TIMER_UNIX', 1)
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
      'Metal',
      'QuartzCore',
      'UniformTypeIdentifiers',
    ],
  )
else
  error('Platform not yet supported.')
endif

if get_option('default_library') == 'both' and cc.get_argument_syntax() == 'msvc'
  error('default_library=both not supported when compiling with MSVC')
endif

subdir('src')

# FIXME, this is to work around a bug in upstream headers
cdata.set('SDL_LIBDECOR_VERSION_MAJOR', 99)
cdata.set('SDL_LIBDECOR_VERSION_MINOR', 99)
cdata.set('SDL_LIBDECOR_VERSION_PATCH', 99)

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

