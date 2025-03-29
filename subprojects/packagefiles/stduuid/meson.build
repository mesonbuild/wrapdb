
project(
  'stduuid',
  'cpp',
  default_options: ['default_library=static'],
  version: '1.2.3',
  license: 'MIT',
)

stduuid_version = meson.project_version()


flags = []
deps = []
inc_dirs = []
override_options = []

install = get_option('install')

cpp = meson.get_compiler('cpp')
is_msvc_or_similar = cpp.get_id() == 'msvc' or cpp.get_id() == 'clang-cl'

# IS this redundant, or is there no other way?
windows_options_prefix = '-'
if is_msvc_or_similar
  windows_options_prefix = '/'
endif

if get_option('system_generator').allowed()
  if host_machine.system() == 'windows'
    # the needed library is already present
    flags += (windows_options_prefix + 'DUUID_SYSTEM_GENERATOR')
  elif host_machine.system() == 'darwin'
    system_generator_dep = dependency(
      'CoreFoundation',
      'corefoundation',
      required: get_option('system_generator'),
    )
    if system_generator_dep.found()
      deps += system_generator_dep
      flags += '-DUUID_SYSTEM_GENERATOR'
    endif
  else

    system_generator_dep = dependency(
      'libuuid',
      'uuid',
      required: get_option('system_generator'),
    )
    if system_generator_dep.found()
      deps += system_generator_dep
      flags += '-DUUID_SYSTEM_GENERATOR'
    endif
  endif
endif


if get_option('time_generator')
  flags += (windows_options_prefix + 'DUUID_TIME_GENERATOR')
endif


is_in_cpp20_mode = cpp.compiles(
  '''
#if defined(__cplusplus) && (__cplusplus >= 202002L || (defined(_MSVC_LANG) && _MSVC_LANG >= 202002L))
#else
#error in cpp 20 mode
#endif
''',
)

if get_option('using_cxx20_span').enabled() and (not is_in_cpp20_mode)
  error('for the setting\'using_cxx20_span\' c++20 or newer is required')
endif


using_cxx20_span = (get_option('using_cxx20_span').enabled()
or (get_option('using_cxx20_span').auto()
and is_in_cpp20_mode)
)

if using_cxx20_span
  override_options += 'cpp_std=c++20'
else

  is_in_cpp17_mode = cpp.compiles(
    '''
#if defined(__cplusplus) && (__cplusplus >= 201703L || (defined(_MSVC_LANG) && _MSVC_LANG >= 201703L))
#else
#error in cpp 17 mode
#endif
''',
  )

  if not is_in_cpp17_mode
    error('at least c++17 is required to build this package')
  endif

  override_options += 'cpp_std=c++17'
  # this is needed, since other targets (like e.g. the test target) may need this include
  inc_dirs += include_directories('.')
  if install
    install_subdir(
      'gsl',
      install_dir: 'include',
    )
  endif
endif


inc_dirs += include_directories('include')
header_file = 'include/uuid.h'
if install
  install_headers(header_file)
endif

stduuid_dep = declare_dependency(
  include_directories: inc_dirs,
  sources: header_file,
  dependencies: deps,
  compile_args: flags,
  version: stduuid_version,
)


if get_option('tests')
  subdir('test')
endif
