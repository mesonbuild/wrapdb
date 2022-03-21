project('libmatroska', 'cpp',
  version : '1.6.3',
  default_options : ['warning_level=1', 'cpp_std=c++14'])

cpp = meson.get_compiler('cpp')
if cpp.get_id() == 'msvc'
  matroska_export = configure_file(output: 'matroska_export.h', configuration: {'MATROSKA_DLL_API': '__declspec(dllexport)'})
else
  matroska_export = configure_file(output: 'matroska_export.h', configuration: {'MATROSKA_DLL_API': ''})
endif

libebml = dependency('libebml')

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
  subdir : 'matroska'
)

libmatroska_incdir = include_directories(['.'])

libmatroska = library('matroska',
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
  include_directories : libmatroska_incdir,
  dependencies : libebml,
  install : true,
)

pkg = import('pkgconfig')
pkg.generate(libmatroska)

libmatroska_dep = declare_dependency(
  include_directories : libmatroska_incdir,
  link_with : libmatroska,
)
