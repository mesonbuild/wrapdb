project(
  'libebml',
  'cpp',
  license: 'LGPL-2.1-or-later',
  version: '1.4.5',
  meson_version: '>=0.50.0',
)

cpp = meson.get_compiler('cpp')
if host_machine.system() == 'windows' and cpp.has_header('winapifamily.h')
  add_project_arguments(
    '-DHAVE_WINAPIFAMILY_H',
    language: 'cpp',
  )
endif

if get_option('default_library') == 'static'
  add_project_arguments(
    '-DEBML_STATIC_DEFINE',
    language: 'cpp',
  )
endif

if host_machine.system() == 'windows'
  dllapi = '-DEBML_DLL_API=@0@'.format(
    get_option('default_library') != 'static' ? '__declspec(dllexport)' : '',
  )
else
  dllapi = '-DEBML_DLL_API=__attribute__((visibility("default")))'
endif

ebml_api = configuration_data()
ebml_conf = configure_file(
  output: 'ebml_export.h',
  configuration: ebml_api,
)

install_headers(
  'ebml/Debug.h',
  'ebml/EbmlBinary.h',
  'ebml/EbmlConfig.h',
  'ebml/EbmlContexts.h',
  'ebml/EbmlCrc32.h',
  'ebml/EbmlDate.h',
  'ebml/EbmlDummy.h',
  'ebml/EbmlElement.h',
  'ebml/EbmlEndian.h',
  'ebml/EbmlFloat.h',
  'ebml/EbmlHead.h',
  'ebml/EbmlId.h',
  'ebml/EbmlMaster.h',
  'ebml/EbmlSInteger.h',
  'ebml/EbmlStream.h',
  'ebml/EbmlString.h',
  'ebml/EbmlSubHead.h',
  'ebml/EbmlTypes.h',
  'ebml/EbmlUInteger.h',
  'ebml/EbmlUnicodeString.h',
  'ebml/EbmlVersion.h',
  'ebml/EbmlVoid.h',
  'ebml/IOCallback.h',
  'ebml/MemIOCallback.h',
  'ebml/MemReadIOCallback.h',
  'ebml/SafeReadIOCallback.h',
  'ebml/StdIOCallback.h',
  ebml_conf,
  subdir: 'ebml',
)

cpp_files = files(
  'src/Debug.cpp',
  'src/EbmlBinary.cpp',
  'src/EbmlContexts.cpp',
  'src/EbmlCrc32.cpp',
  'src/EbmlDate.cpp',
  'src/EbmlDummy.cpp',
  'src/EbmlElement.cpp',
  'src/EbmlFloat.cpp',
  'src/EbmlHead.cpp',
  'src/EbmlMaster.cpp',
  'src/EbmlSInteger.cpp',
  'src/EbmlStream.cpp',
  'src/EbmlString.cpp',
  'src/EbmlSubHead.cpp',
  'src/EbmlUInteger.cpp',
  'src/EbmlUnicodeString.cpp',
  'src/EbmlVersion.cpp',
  'src/EbmlVoid.cpp',
  'src/IOCallback.cpp',
  'src/MemIOCallback.cpp',
  'src/MemReadIOCallback.cpp',
  'src/SafeReadIOCallback.cpp',
  'src/StdIOCallback.cpp',
)

if get_option('win32_io') and host_machine.system() == 'windows'
  cpp_files += files('src/platform/win32/WinIOCallback.cpp')
endif

libebml = library(
  'libebml',
  cpp_files,
  cpp_args: dllapi,
  name_prefix: '',
  version: '5.0.0',
  soversion: host_machine.system() == 'windows' ? '' : '5',
  gnu_symbol_visibility: 'hidden',
  install: true,
)

dllapi = '-DEBML_DLL_API='
if host_machine.system() == 'windows' and get_option('default_library') != 'static'
  dllapi = '-DEBML_DLL_API=__declspec(dllimport)'
endif

libebml_dep = declare_dependency(
  compile_args: dllapi,
  include_directories: '.',
  link_with: libebml,
)

pkg = import('pkgconfig')
pkg.generate(
  libebml,
  description: 'Library for parsing EBML data structures',
)
