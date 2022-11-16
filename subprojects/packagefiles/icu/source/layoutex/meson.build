sources = files(
  'LXUtilities.cpp',
  'ParagraphLayout.cpp',
  'RunArrays.cpp',
  'playout.cpp',
  'plruns.cpp',
)

layoutex_name = '@0@lx@1@'.format(library_prefix, library_suffix)

layoutex = library(
  layoutex_name,
  sources,
  include_directories: [incdir, include_directories('..')],
  c_args: '-DU_LAYOUTEX_IMPLEMENTATION',
  cpp_args: '-DU_LAYOUTEX_IMPLEMENTATION',
  link_with: [common_lib],
)
