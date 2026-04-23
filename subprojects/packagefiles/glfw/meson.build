#####  GLFW  #####
#@ Project file
project(
  'glfw',
  'c',
  version: '3.4',
  license: 'Zlib',
  default_options: ['b_ndebug=if-release', 'c_std=c99', 'warning_level=0'],
  meson_version: '>=0.58.0',
)
#@ Project variables
sys_os = host_machine.system()
sys_cc = meson.get_compiler('c')
opt_libdir = get_option('libdir')
is_posix = sys_os != 'windows'
opt_display = get_option('display-api')

if get_option('default_library') != 'static'
  add_project_arguments(
    '-D_GLFW_BUILD_DLL',
    language: 'c',
  )
endif

add_project_arguments(
  '-D_DEFAULT_SOURCE',
  language: 'c',
)

if opt_display == ['auto']
  if sys_os == 'windows'
    opt_display = ['win32']
  elif sys_os == 'darwin'
    opt_display = ['cocoa']
  else
    opt_display = ['x11']
  endif
endif

### Dependencies ###
deps = []
#@ Backend API
#  OSMesa
if opt_display.contains('osmesa')
  deps += dependency('osmesa')
endif

# X11
if opt_display.contains('x11')
  foreach x : ['x11', 'xrandr', 'xinerama', 'xcursor', 'xi']
    deps += dependency(
      x,
      required: true,
    )
  endforeach

  add_project_arguments(
    '-D_GLFW_X11',
    language: 'c',
  )
endif

# Wayland
if opt_display.contains('wayland')
  warning('Wayland support is experimental & incomplete.')
  warning(
    'GLFW < 3.4 cannot detect Wayland if both x11 and Wayland exist on-system!',
  )
  foreach w : [
    'wayland-client',
    'wayland-cursor',
    'wayland-server',
    'wayland-egl',
    'xkbcommon',
  ]
    deps += dependency(
      w,
      required: true,
    )
  endforeach
  wl_protocols = dependency('wayland-protocols')
  wl_dir = wl_protocols.get_variable('pkgdatadir')
  wl_scan_dep = dependency(
    'wayland-scanner',
    required: false,
    native: true,
  )
  if wl_scan_dep.found()
    wl_scanner = find_program(
      wl_scan_dep.get_variable(
        pkgconfig: 'wayland_scanner',
      ),
      native: true,
    )
  else
    wl_scanner = find_program(
      'wayland-scanner',
      native: true,
    )
  endif
  s_wayland = []

  protocols = [
    'fractional-scale-v1',
    'idle-inhibit-unstable-v1',
    'pointer-constraints-unstable-v1',
    'relative-pointer-unstable-v1',
    'viewporter',
    'wayland',
    'xdg-activation-v1',
    'xdg-decoration-unstable-v1',
    'xdg-shell',
  ]

  foreach proto : protocols
    xml_file = files('deps' / 'wayland' / (proto + '.xml'))
    header_file = proto + '-client-protocol.h'
    code_file = proto + '-client-protocol-code.h'

    s_wayland += custom_target(
      '@0@ client-header'.format(proto),
      command: ['wayland-scanner', 'client-header', '@INPUT@', '@OUTPUT@'],
      input: xml_file,
      output: header_file,
    )

    s_wayland += custom_target(
      '@0@ private-code'.format(proto),
      command: ['wayland-scanner', 'private-code', '@INPUT@', '@OUTPUT@'],
      input: xml_file,
      output: code_file,
    )
  endforeach

  add_project_arguments(
    '-D_GLFW_WAYLAND',
    language: 'c',
  )
endif

# Win32
if opt_display.contains('win32')
  if sys_os != 'windows'
    error('Non Windows is unsupported')
  endif

  add_project_arguments(
    '-D_GLFW_WIN32',
    language: 'c',
  )
endif

# Cocoa
if opt_display.contains('cocoa')
  if sys_os != 'darwin'
    error('Non macOS is unsupported')
  endif
  deps += dependency(
    'appleframeworks',
    modules: ['Cocoa', 'CoreFoundation', 'IOKit'],
  )

  add_project_arguments(
    '-D_GLFW_COCOA',
    language: 'c',
  )
endif

#@ System Dependencies
foreach l : ['m', 'rt']
  deps += sys_cc.find_library(
    l,
    required: false,
  )
endforeach
if meson.version().version_compare('>= 0.62')
  deps += dependency(
    'dl',
    required: false,
  )
else
  deps += sys_cc.find_library(
    'dl',
    required: false,
  )
endif
deps += dependency('threads')

### Targets ###
#@ Primary target:
##   GLFW library
#  Common files
s_common = files(
  'src/context.c',
  'src/egl_context.c',
  'src/init.c',
  'src/input.c',
  'src/monitor.c',
  'src/null_init.c',
  'src/null_joystick.c',
  'src/null_monitor.c',
  'src/null_window.c',
  'src/osmesa_context.c',
  'src/platform.c',
  'src/vulkan.c',
  'src/window.c',
)
#  OS files
if sys_os == 'darwin'
  s_os = files('src/cocoa_time.c', 'src/posix_module.c', 'src/posix_thread.c')
elif sys_os == 'windows'
  s_os = files('src/win32_module.c', 'src/win32_thread.c', 'src/win32_time.c')
else
  s_os = files('src/posix_module.c', 'src/posix_thread.c', 'src/posix_time.c')
endif

#  Backend files
s_display = []

if opt_display.contains('osmesa')
  s_display += files(
    'src/null_init.c',
    'src/null_joystick.c',
    'src/null_monitor.c',
    'src/null_window.c',
    'src/osmesa_context.c',
    'src/posix_thread.c',
    'src/posix_time.c',
  )
endif

if opt_display.contains('x11')
  s_display += files(
    'src/glx_context.c',
    'src/linux_joystick.c',
    'src/posix_poll.c',
    'src/x11_init.c',
    'src/x11_monitor.c',
    'src/x11_window.c',
    'src/xkb_unicode.c',
  )
endif

if opt_display.contains('wayland')
  s_display += files(
    'src/linux_joystick.c',
    'src/posix_poll.c',
    'src/wl_init.c',
    'src/wl_monitor.c',
    'src/wl_window.c',
    'src/xkb_unicode.c',
  )
endif

if opt_display.contains('win32')
  s_display += files(
    'src/wgl_context.c',
    'src/win32_init.c',
    'src/win32_joystick.c',
    'src/win32_monitor.c',
    'src/win32_window.c',
  )
endif

if opt_display.contains('cocoa')
  add_languages(
    'objc',
    native: false,
  )
  s_display += files(
    'src/cocoa_init.m',
    'src/cocoa_joystick.m',
    'src/cocoa_monitor.m',
    'src/cocoa_window.m',
    'src/nsgl_context.m',
  )
  if host_machine.system() == 'darwin'
    add_project_arguments(
      '-D_DARWIN_C_SOURCE',
      '-D_GLFW_COCOA',
      language: 'objc',
    )
  endif
endif

srcfiles = [s_common, s_os, s_display]
if opt_display.contains('wayland')
  srcfiles += s_wayland
endif
incdirs = include_directories('include', 'src')
#@ Flags
if host_machine.system() == 'darwin'
  add_project_arguments(
    '-D_DARWIN_C_SOURCE',
    language: 'c',
  )
endif
#  Build
glfw_lib = library(
  'glfw3',
  srcfiles,
  include_directories: incdirs,
  dependencies: deps,
  version: meson.project_version(),
  build_by_default: true,
  pic: true,
  install: get_option('install'),
)
glfw_dep = declare_dependency(
  include_directories: incdirs,
  link_with: glfw_lib,
)
if meson.version().version_compare('>=0.54.0')
  meson.override_dependency('glfw3', glfw_dep)
endif
#  Headers
if get_option('install')
  install_headers(
    'include/GLFW/glfw3.h',
    'include/GLFW/glfw3native.h',
    subdir: 'GLFW',
  )
endif
#@ Secondary target:
##   Test programs
if get_option('tests')
  subdir('tests')
endif
#@ Secondary target:
##   GLFW examples
if get_option('examples')
  subdir('examples')
endif


### Post
#@ Pkg-config
if get_option('install')
  pkg = import('pkgconfig')
  pkg.generate(
    glfw_lib,
    name: 'GLFW',
    description: 'A multi-platform library for OpenGL, windows, and input',
    url: 'https://www.glfw.org/',
    filebase: 'glfw3',
  )
endif
