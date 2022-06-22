reflex_sources = files(
  'reflex.cpp',
)

reflex = executable(
  'reflex',
  reflex_sources,
  link_with : libreflex,
  include_directories : includes,
  install : true)

meson.override_find_program('reflex', reflex)
