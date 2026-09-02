project(
  'mimalloc',
  'c',
  meson_version: '>=0.56.0',
  license: 'MIT',
  version: '3.5.1',
)

mi_sources = []
mi_deps = []
mi_args = []
mi_static_args = []
mi_shared_args = []

mi_sources += files(
  'src/prim/prim-tls.c',
  'src/prim/prim.c',
  'src/alloc-aligned.c',
  'src/alloc-posix.c',
  'src/alloc.c',
  'src/arena.c',
  'src/bitmap.c',
  'src/heap.c',
  'src/init.c',
  'src/libc.c',
  'src/options.c',
  'src/os.c',
  'src/page-map.c',
  'src/page.c',
  'src/random.c',
  'src/stats.c',
  'src/subproc.c',
  'src/theap.c',
  'src/threadlocal.c',
)

# System libraries
cc = meson.get_compiler('c')
if host_machine.system() == 'windows'
  psapi_dep = cc.find_library('psapi')
  shell32_dep = cc.find_library('shell32')
  user32_dep = cc.find_library('user32')
  advapi32_dep = cc.find_library('advapi32')
  bcrypt_dep = cc.find_library('bcrypt')
  mi_deps += [psapi_dep, shell32_dep, user32_dep, advapi32_dep, bcrypt_dep]
else
  thread_dep = dependency('threads')
  atomic_dep = cc.find_library(
    'atomic',
    required: false,
  )
  rt_dep = cc.find_library(
    'rt',
    required: false,
  )
  mi_deps += [thread_dep, atomic_dep, rt_dep]
endif

# Compile args
mi_static_args += ['-DMI_STATIC_LIB']
mi_shared_args += ['-DMI_SHARED_LIB', '-DMI_SHARED_LIB_EXPORT']
if not get_option('debug')
  mi_args += ['-DMI_BUILD_RELEASE']
endif
tls_model = get_option('tl_model')
if tls_model == 'PTHREADS'
  mi_args += ['-DMI_TLS_MODEL_PTHREADS=1']
elif tls_model == 'FIXED'
  mi_args += ['-DMI_TLS_MODEL=FIXED=1']
elif tls_model == 'LOCAL' or tls_model == 'LOCAL_DYNAMIC'
  mi_args += ['-DMI_TLS_MODEL_LOCAL=1']
elif tls_model == 'WIN32'
  mi_args += ['-DMI_TLS_MODEL_WIN32=1']
endif
if tls_model == 'LOCAL_DYNAMIC'
  mi_args += cc.get_supported_arguments('-ftls-model=local-dynamic')
else
  mi_args += cc.get_supported_arguments('-ftls-model=initial-exec')
endif
if host_machine.system() == 'cygwin' and cc.has_header_symbol(
  'corecrt.h',
  '_UCRT',
)
  mi_args += ['-DMI_MINGW_UCRT64=1']
endif

# malloc override
if get_option('override')
  # On MacOS use MI_OSX_ZONE and MI_OSX_INTERPOSE
  if host_machine.system() == 'darwin'
    mi_sources += files('src/prim/osx/alloc-override-zone.c')
    mi_args += ['-DMI_OSX_ZONE=1', '-DMI_OSX_INTERPOSE=1']
  endif
  # Disable built-in malloc
  mi_args += cc.get_supported_arguments('-fno-builtin-malloc')
  # Enable malloc override (except on static windows build)
  mi_shared_args += ['-DMI_MALLOC_OVERRIDE']
  if host_machine.system() != 'windows'
    mi_static_args += ['-DMI_MALLOC_OVERRIDE']
  endif
endif

# Windows redirect
if host_machine.system() == 'windows'
  if not get_option('win_redirect')
    mi_args += ['-DMI_WIN_NOREDIRECT=1']
  else
    error('Windows redirect not implemented yet')
  endif
endif

# Set shared and shared flags manually since Meson 1.3.0 is still too new
if get_option('default_library') == 'static'
  mi_args += mi_static_args
  message(
    'Using static library of mimalloc, make sure to include mimalloc-override.h in each source file to redefine malloc to mi_malloc',
  )
elif get_option('default_library') == 'shared'
  mi_args += mi_shared_args
else
  error('Building both static and shared libraries is not possible')
endif

# Library version
mi_version_list = meson.project_version().split('.')
mi_soversion = mi_version_list[0]
mi_version = mi_version_list[0] + '.' + mi_version_list[1]

# Library
mi_inc = include_directories('include')
mi_lib = library(
  'mimalloc',
  sources: mi_sources,
  c_args: mi_args,
  include_directories: mi_inc,
  dependencies: mi_deps,
  version: mi_version,
  soversion: mi_soversion,
  gnu_symbol_visibility: 'hidden',
  install: true,
)
mi_dep = declare_dependency(
  include_directories: mi_inc,
  link_with: mi_lib,
)
meson.override_dependency('mimalloc', mi_dep)

# Install Headers
install_headers(
  'include/mimalloc.h',
  'include/mimalloc-new-delete.h',
  'include/mimalloc-override.h',
  'include/mimalloc-stats.h',
)

# Install pkg-config file
pkg = import('pkgconfig')
pkg.generate(
  mi_lib,
  description: 'A compact general purpose allocator with excellent performance',
  url: 'https://github.com/microsoft/mimalloc/',
)
