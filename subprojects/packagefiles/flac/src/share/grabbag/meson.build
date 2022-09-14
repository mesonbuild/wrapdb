grabbag = static_library(
  'grabbag',
  'alloc.c',
  'cuesheet.c',
  'file.c',
  'picture.c',
  'replaygain.c',
  'seektable.c',
  'snprintf.c',
  include_directories: main_inc,
  link_with: [flac_lib, replaygain_analysis],
)
