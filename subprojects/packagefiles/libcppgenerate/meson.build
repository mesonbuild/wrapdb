project(
  'libcppgenerate',
  'cpp',
  version: '0.2',
  default_options: ['warning_level=3', 'cpp_std=c++11', 'default_library=both'],
)

# Version of dynamic library
library_version = '0.0.2'

# Do not install unnecessary things when used as a subproject
install = not meson.is_subproject()

src = files(
  'cppgenerate/argument.cpp',
  'cppgenerate/class.cpp',
  'cppgenerate/codeblock.cpp',
  'cppgenerate/constructor.cpp',
  'cppgenerate/cppgenerateutils.cpp',
  'cppgenerate/enum.cpp',
  'cppgenerate/membervariable.cpp',
  'cppgenerate/method.cpp',
  'cppgenerate/printer.cpp',
  'cppgenerate/variable.cpp',
)

shared_lib = []
static_lib = []

if get_option('default_library') == 'both'
  if install
    both_libs = both_libraries(
      'cppgenerate',
      src,
      version: library_version,
      install: true,
    )
    static_lib = both_libs.get_static_lib()
    shared_lib = both_libs.get_shared_lib()
  else
    # When in a subproject, only install the necessary shared library
    static_lib = static_library(
      'cppgenerate',
      src,
    )
    shared_lib = shared_library(
      'cppgenerate',
      src,
      version: library_version,
      install: true,
    )
  endif
elif get_option('default_library') == 'shared'
  shared_lib = shared_library(
    'cppgenerate',
    src,
    version: library_version,
    install: true,
  )
elif get_option('default_library') == 'static'
  static_lib = static_library(
    'cppgenerate',
    src,
    install: install,
  )
endif

if install
  install_headers(
    'cppgenerate/accessmodifier.h',
    'cppgenerate/argument.h',
    'cppgenerate/class.h',
    'cppgenerate/codeblock.h',
    'cppgenerate/constructor.h',
    'cppgenerate/cppgenerateutils.h',
    'cppgenerate/enum.h',
    'cppgenerate/membervariable.h',
    'cppgenerate/method.h',
    'cppgenerate/printer.h',
    'cppgenerate/variable.h',
    subdir: 'cppgenerate',
  )
endif

# Configure .pc files
fs = import('fs')

# Base configuration object used for shared library
dynamic_lib_cfg = configuration_data()
dynamic_lib_cfg.set('PROJECT_VERSION', meson.project_version())
dynamic_lib_cfg.set('PKG_CONFIG_REQUIRES', '')
dynamic_lib_cfg.set('CMAKE_INSTALL_PREFIX', get_option('prefix'))
if fs.is_absolute(get_option('includedir'))
  dynamic_lib_cfg.set('PKG_CONFIG_INCLUDEDIR', get_option('includedir'))
else
  dynamic_lib_cfg.set(
    'PKG_CONFIG_INCLUDEDIR',
    '${prefix}' / get_option('includedir'),
  )
endif
if fs.is_absolute(get_option('libdir'))
  dynamic_lib_cfg.set('PKG_CONFIG_LIBDIR', get_option('libdir'))
else
  dynamic_lib_cfg.set('PKG_CONFIG_LIBDIR', '${prefix}' / get_option('libdir'))
endif
dynamic_lib_cfg.set('PKG_CONFIG_LIBS', '-L${libdir} -lcppgenerate')
dynamic_lib_cfg.set('PKG_CONFIG_CFLAGS', '-I${includedir}')

# Static library configuration object based off of dynamic_lib_cfg
static_lib_cfg = dynamic_lib_cfg

static_lib_cfg.set('PKG_CONFIG_STATIC_LIBS', '-L${libdir} -l:libcppgenerate.a')

# Configure and install pkg-config files if the relevant library is being built
if install and get_option('default_library') in ['shared', 'both']
  configure_file(
    input: 'cppgenerate.pc.cmake',
    output: 'cppgenerate.pc',
    configuration: dynamic_lib_cfg,
    format: 'cmake',
    install: true,
    install_dir: get_option('libdir') / 'pkgconfig',
  )
endif
if install and get_option('default_library') in ['static', 'both']
  configure_file(
    input: 'cppgenerate-static.pc.cmake',
    output: 'cppgenerate-static.pc',
    configuration: static_lib_cfg,
    format: 'cmake',
    install: true,
    install_dir: get_option('libdir') / 'pkgconfig',
  )
endif

public_flags = []

if build_machine.system() == 'windows'
  public_flags += '-DCPPGENERATE_STATIC'
endif

# Declare dependency when used as a subproject
if get_option('default_library') in ['shared', 'both']
  shared_dep = declare_dependency(
    compile_args: public_flags,
    link_with: shared_lib,
    include_directories: '.',
  )
  meson.override_dependency('cppgenerate', shared_dep)
endif
if get_option('default_library') in ['static', 'both']
  static_dep = declare_dependency(
    compile_args: public_flags,
    link_with: static_lib,
    include_directories: '.',
  )
  meson.override_dependency('cppgenerate-static', static_dep)
endif

# Pick an appropriate dependency object for building tests and examples
if get_option('default_library') == 'both'
  if meson.version().version_compare('>=1.6.0')
    if get_option('default_both_libraries') == 'shared'
      internal_lib = shared_lib
    elif get_option('default_both_libraries') == 'static'
      internal_lib = static_lib
    elif get_option('default_both_libraries') == 'auto'
      internal_lib = shared_lib
    endif
  else
    internal_lib = shared_lib
  endif
elif get_option('default_library') == 'shared'
  internal_lib = shared_lib
elif get_option('default_library') == 'static'
  internal_lib = static_lib
endif

internal_dep = declare_dependency(
  link_with: internal_lib,
  include_directories: '.',
)

if get_option('enable-tests')
  subdir('tests')
endif
if get_option('enable-examples')
  subdir('examples')
endif
