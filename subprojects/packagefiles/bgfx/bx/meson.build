# bx - Foundation library for bgfx

bx_sources = files(
  'src/allocator.cpp',
  'src/bounds.cpp',
  'src/bx.cpp',
  'src/commandline.cpp',
  'src/crtnone.cpp',
  'src/debug.cpp',
  'src/dtoa.cpp',
  'src/easing.cpp',
  'src/file.cpp',
  'src/filepath.cpp',
  'src/hash.cpp',
  'src/math.cpp',
  'src/mutex.cpp',
  'src/os.cpp',
  'src/process.cpp',
  'src/semaphore.cpp',
  'src/settings.cpp',
  'src/sort.cpp',
  'src/string.cpp',
  'src/thread.cpp',
  'src/timer.cpp',
  'src/url.cpp',
)

bx_include = include_directories('include')
bx_3rdparty_include = include_directories('3rdparty')

# Platform compat includes
if host_machine.system() == 'darwin'
  bx_compat_include = include_directories('include/compat/osx')
elif host_machine.system() == 'linux'
  bx_compat_include = include_directories('include/compat/linux')
elif host_machine.system() == 'windows'
  cpp = meson.get_compiler('cpp')
  if cpp.get_id() == 'gcc'
    bx_compat_include = include_directories('include/compat/mingw')
  else
    bx_compat_include = include_directories('include/compat/msvc')
  endif
elif host_machine.system() == 'freebsd'
  bx_compat_include = include_directories('include/compat/freebsd')
else
  bx_compat_include = include_directories('include/compat/linux')
endif

bx_compile_args = [
  '-D__STDC_LIMIT_MACROS',
  '-D__STDC_FORMAT_MACROS',
  '-D__STDC_CONSTANT_MACROS',
]

cpp = meson.get_compiler('cpp')

# MSVC: SEH-compatible exception handling (PRIVATE — bx only, matches cmake)
if cpp.get_id() == 'msvc'
  bx_compile_args += ['/EHs-c-', '-D_HAS_EXCEPTIONS=0']
endif

if get_option('buildtype').startswith('debug')
  bx_compile_args += '-DBX_CONFIG_DEBUG=1'
else
  bx_compile_args += '-DBX_CONFIG_DEBUG=0'
endif

bx_deps = []

if host_machine.system() == 'windows'
  bx_deps += meson.get_compiler('cpp').find_library('psapi')
elif host_machine.system() == 'linux'
  bx_deps += dependency('threads')
  bx_deps += meson.get_compiler('cpp').find_library('dl')
  bx_deps += meson.get_compiler('cpp').find_library('rt')
elif host_machine.system() == 'darwin'
  bx_deps += dependency('appleframeworks', modules: ['Foundation'])
elif host_machine.system() == 'android'
  bx_deps += meson.get_compiler('cpp').find_library('log')
endif

bx_lib = static_library('bx',
  bx_sources,
  include_directories: [bx_include, bx_compat_include, bx_3rdparty_include],
  cpp_args: bx_compile_args,
  dependencies: bx_deps,
  override_options: ['cpp_std=c++20'],
)

bx_debug_define = get_option('buildtype').startswith('debug') ? '-DBX_CONFIG_DEBUG=1' : '-DBX_CONFIG_DEBUG=0'

bx_public_args = [
  '-D__STDC_LIMIT_MACROS',
  '-D__STDC_FORMAT_MACROS',
  '-D__STDC_CONSTANT_MACROS',
  bx_debug_define,
]

bx_dep = declare_dependency(
  include_directories: [bx_include, bx_compat_include],
  link_with: bx_lib,
  compile_args: bx_public_args,
  dependencies: bx_deps,
)
