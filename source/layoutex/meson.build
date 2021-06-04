sources = files(
  'ParagraphLayout.cpp',
  'RunArrays.cpp',
  'LXUtilities.cpp',
  'playout.cpp',
  'plruns.cpp',
)

layoutex = library('layoutex',
  sources,
  include_directories : [incdir, include_directories('..')],
  c_args : '-DU_LAYOUTEX_IMPLEMENTATION',
  cpp_args : '-DU_LAYOUTEX_IMPLEMENTATION',
  link_with: [common_lib],
)
