libarchive_fe = static_library(
  'libarchive_fe',
  ['lafe_err.c', 'line_reader.c', 'passphrase.c'],
  dependencies: libarchive_dep,
)

libarchive_fe_dep = declare_dependency(
  dependencies: libarchive_dep,
  include_directories: include_directories('.'),
  link_with: libarchive_fe,
)
