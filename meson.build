project('reflex', 'cpp',
        version : '3.0.1',
        license : 'BSD-3-Clause')

includes = include_directories('include')

cpp = meson.get_compiler('cpp')

flags = cpp.get_supported_arguments(['-Wno-non-virtual-dtor'])
add_project_arguments(flags, language : 'cpp')

unicode_sources = files(
  'unicode/block_scripts.cpp',
  'unicode/language_scripts.cpp',
  'unicode/letter_scripts.cpp',
)

libreflex_sources = files(
  'lib/convert.cpp',
  'lib/debug.cpp',
  'lib/error.cpp',
  'lib/input.cpp',
  'lib/matcher.cpp',
  'lib/pattern.cpp',
  'lib/posix.cpp',
  'lib/unicode.cpp',
  'lib/utf8.cpp',
)

libreflex = library(
  'reflex',
  libreflex_sources, unicode_sources,
  include_directories : includes)

libreflexmin_sources = files(
  'lib/debug.cpp',
  'lib/error.cpp',
  'lib/input.cpp',
  'lib/matcher.cpp',
  'lib/pattern.cpp',
  'lib/utf8.cpp',
)

libreflexmin = library(
  'reflexmin',
  libreflexmin_sources,
  include_directories : includes)

reflex_sources = files(
  'src/reflex.cpp',
)

reflex = executable(
  'reflex',
  reflex_sources,
  link_with : libreflex,
  include_directories : includes,
  install : true)

reflex_dep = declare_dependency(
  link_with : libreflex,
  include_directories : includes)

meson.override_find_program('reflex', reflex)
