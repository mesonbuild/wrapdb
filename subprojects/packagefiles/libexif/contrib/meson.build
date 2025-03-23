if not get_option('examples')
  subdir_done()
endif

#executable('cam_features', 'examples/cam_features.c', dependencies: exif_dep)
executable(
  'photographer',
  'examples/photographer.c',
  dependencies: exif_dep,
)
executable(
  'thumbnail',
  'examples/thumbnail.c',
  dependencies: exif_dep,
)
executable(
  'write-exif',
  'examples/write-exif.c',
  dependencies: exif_dep,
)
