project(
  'pugixml',
  'cpp',
  default_options: 'cpp_std=c++14',
  version: '1.13',
  meson_version: '>=0.50.0',
)

sources = files('src/pugixml.cpp')

win = host_machine.system() == 'windows'
if win
  win_mod = import('windows')
  sources += win_mod.compile_resources('scripts/pugixml_dll.rc')
endif

args = []
if win
  args += '-DPUGIXML_API=@0@'.format(get_option('default_library') != 'static' ? '__declspec(dllexport)' : '""')
else
  args += '-DPUGIXML_API=__attribute__((visibility("default")))'
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
  name_prefix: win ? '' : [],
  version: meson.project_version(),
  gnu_symbol_visibility: 'hidden',
  soversion: win ? '' : '1',
  install: true,
)

if win
  export = get_option('default_library') != 'static' ? '__declspec(dllimport)' : '""'
else
  export = '__attribute__((visibility("default")))'
endif

pugixml_dep = declare_dependency(
  compile_args: '-DPUGIXML_API=@0@'.format(export),
  link_with: pugixml_lib,
  include_directories: 'src',
)

install_headers(
  'src/pugiconfig.hpp',
  'src/pugixml.hpp',
)

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
if get_option('tests') and not win
  subdir('tests')
  pugixml_check = executable('pugixml-check', test_sources, dependencies: pugixml_dep)
  test('pugixml-check', pugixml_check, workdir: meson.current_source_dir())
endif
