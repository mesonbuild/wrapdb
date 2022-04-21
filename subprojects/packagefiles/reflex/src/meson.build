reflex_sources = files(
  'reflex.cpp',
)

reflex = executable(
  'reflex',
  reflex_sources,
  link_with : libreflex,
  include_directories : includes,
  install : true)

if meson.version().version_compare('>=0.46.0')
  meson.override_find_program('reflex', reflex)
endif
