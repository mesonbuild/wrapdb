project(
  'icu',
  'c',
  'cpp',
  version: '72.1',
  meson_version: '>=0.49.0',
  default_options: 'cpp_std=c++17',
)

cpp = meson.get_compiler('cpp')

if host_machine.system() == 'windows'
  add_project_arguments('-DU_PLATFORM_USES_ONLY_WIN32_API', language: 'cpp')
  add_project_arguments('-DWIN32', '-DWIN64', '-D_MBCS', language: 'cpp')
  add_project_arguments('-DU_PLATFORM_USES_ONLY_WIN32_API', language: 'c')
  add_project_arguments('-DWIN32', '-DWIN64', '-D_MBCS', language: 'c')
endif

if cpp.get_argument_syntax() == 'msvc'
  add_project_arguments('/utf-8', language: 'cpp')
  add_project_arguments('/utf-8', language: 'c')
endif

if meson.version().version_compare('>= 0.62')
  dl_dep = dependency('dl', required: false)
else
  dl_dep = cpp.find_library('dl', required: false)
endif

windows = import('windows')

# Compiler flags the users of this library must use.
usage_args = []

if get_option('default_library') == 'static'
  add_project_arguments('-DU_STATIC_IMPLEMENTATION', language: 'c')
  add_project_arguments('-DU_STATIC_IMPLEMENTATION', language: 'cpp')
  usage_args = ['-DU_STATIC_IMPLEMENTATION']
  if cpp.get_argument_syntax() == 'msvc'
    library_prefix = ''
    library_suffix = ''
  else
    library_prefix = 's'
    if get_option('buildtype') == 'debug'
      library_suffix = 'd'
    else
      library_suffix = ''
    endif
  endif
else
  library_prefix = ''
  library_suffix = ''
endif

subdir('source')
