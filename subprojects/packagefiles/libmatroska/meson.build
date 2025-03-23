project(
  'libmatroska',
  'cpp',
  license: 'LGPL-2.1-or-later',
  version: '1.7.1',
  meson_version: '>=0.48.0',
)

if host_machine.system() == 'windows'
  dllapi = '-DMATROSKA_DLL_API=@0@'.format(
    get_option('default_library') != 'static' ? '__declspec(dllexport)' : '',
  )
else
  dllapi = '-DMATROSKA_DLL_API=__attribute__ ((visibility("default")))'
endif

matroska_api = configuration_data()
matroska_export = configure_file(
  output: 'matroska_export.h',
  configuration: matroska_api,
)

libebml = dependency(
  'libebml',
  version: '>=1.4.4',
)

install_headers(
  'matroska/FileKax.h',
  'matroska/KaxAttached.h',
  'matroska/KaxAttachments.h',
  'matroska/KaxBlockData.h',
  'matroska/KaxBlock.h',
  'matroska/KaxChapters.h',
  'matroska/KaxClusterData.h',
  'matroska/KaxCluster.h',
  'matroska/KaxConfig.h',
  'matroska/KaxContentEncoding.h',
  'matroska/KaxContexts.h',
  'matroska/KaxCuesData.h',
  'matroska/KaxCues.h',
  'matroska/KaxDefines.h',
  'matroska/KaxInfoData.h',
  'matroska/KaxInfo.h',
  'matroska/KaxSeekHead.h',
  'matroska/KaxSegment.h',
  'matroska/KaxSemantic.h',
  'matroska/KaxTag.h',
  'matroska/KaxTags.h',
  'matroska/KaxTrackAudio.h',
  'matroska/KaxTrackEntryData.h',
  'matroska/KaxTracks.h',
  'matroska/KaxTrackVideo.h',
  'matroska/KaxTypes.h',
  'matroska/KaxVersion.h',
  matroska_export,
  subdir: 'matroska',
)

install_headers(
  'matroska/c/libmatroska.h',
  'matroska/c/libmatroska_t.h',
  subdir: 'matroska/c',
)

libmatroska_incdir = include_directories('.', 'matroska')

libmatroska = library(
  'libmatroska',
  'src/FileKax.cpp',
  'src/KaxAttached.cpp',
  'src/KaxAttachments.cpp',
  'src/KaxBlock.cpp',
  'src/KaxBlockData.cpp',
  'src/KaxCluster.cpp',
  'src/KaxContexts.cpp',
  'src/KaxCues.cpp',
  'src/KaxCuesData.cpp',
  'src/KaxInfoData.cpp',
  'src/KaxSeekHead.cpp',
  'src/KaxSegment.cpp',
  'src/KaxSemantic.cpp',
  'src/KaxTracks.cpp',
  'src/KaxVersion.cpp',
  cpp_args: dllapi,
  name_prefix: '',
  version: '7.0.0',
  soversion: host_machine.system() == 'windows' ? '' : '7',
  gnu_symbol_visibility: 'hidden',
  include_directories: libmatroska_incdir,
  dependencies: libebml,
  install: true,
)

dllapi = '-DMATROSKA_DLL_API='
if host_machine.system() == 'windows' and get_option('default_library') != 'static'
  dllapi = '-DMATROSKA_DLL_API=__declspec(dllimport)'
endif

libmatroska_dep = declare_dependency(
  compile_args: dllapi,
  include_directories: libmatroska_incdir,
  dependencies: libebml,
  link_with: libmatroska,
)

pkg = import('pkgconfig')
pkg.generate(
  libmatroska,
  description: 'Library for parsing EBML data structures',
)
