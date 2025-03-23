project(
  'pugixml',
  'cpp',
  default_options: 'cpp_std=c++14',
  version: '1.14',
  meson_version: '>=0.49.0',
)

sources = files('src/pugixml.cpp')

if host_machine.system() == 'windows'
  win_mod = import('windows')
  sources += win_mod.compile_resources('scripts/pugixml_dll.rc')
endif

args = ['-DPUGIXML_API=__attribute__((visibility("default")))']
if host_machine.system() == 'windows'
  args = get_option('default_library') != 'static' ? '-DPUGIXML_API=__declspec(dllexport)' : []
endif

foreach opt : ['wchar_mode', 'compact', 'no_xpath', 'no_stl', 'no_exceptions']
  if get_option(opt)
    args += '-DPUGIXML_' + opt.to_upper()
  endif
endforeach

pugixml_lib = library(
  'pugixml',
  sources,
  cpp_args: args,
  version: meson.project_version(),
  gnu_symbol_visibility: 'hidden',
  soversion: host_machine.system() == 'windows' ? '' : '1',
  install: true,
)

export = []
if host_machine.system() == 'windows' and get_option('default_library') != 'static'
  export += '-DPUGIXML_API=__declspec(dllimport)'
endif

incdir = include_directories('src')

pugixml_dep = declare_dependency(
  compile_args: export,
  link_with: pugixml_lib,
  include_directories: incdir,
)

install_headers('src/pugiconfig.hpp', 'src/pugixml.hpp')

pconf = import('pkgconfig')
pconf.generate(
  pugixml_lib,
  description: 'Light-weight, simple and fast XML parser for C++ with XPath support.',
  url: 'https://pugixml.org/',
)

# This is a nice idea in theory, but in practice it turns out CMake needs a third file
# too, this one called "-targets.cmake", and there isn't a module method to create this.
# Watch this space for news: https://github.com/mesonbuild/meson/pull/9978
#
#if find_program('cmake', required: false).found()
#  cmake = import('cmake')
#  cmake.write_basic_package_version_file(
#    name: meson.project_name(),
#    version: meson.project_version(),
#    compatibility: 'SameMajorVersion',
#  )
#  cmake.configure_package_config_file(
#    input: 'scripts/pugixml-config.cmake.in',
#    name: meson.project_name(),
#    configuration: configuration_data(),
#  )
#endif

#Windows doesn't compile with C++17 until next version
if get_option('tests')
  subdir('tests')
  pugixml_check = executable(
    'pugixml-check',
    test_sources,
    dependencies: pugixml_dep,
  )
  test(
    'pugixml-check',
    pugixml_check,
    workdir: meson.current_source_dir(),
  )
endif
