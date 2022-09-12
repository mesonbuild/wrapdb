project('reflex', 'cpp',
        version: '3.2.11',
        license: 'BSD-3-Clause',
        meson_version: '>=0.49.0')

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

libreflexmin_sources = files(
  'lib/debug.cpp',
  'lib/error.cpp',
  'lib/input.cpp',
  'lib/matcher.cpp',
  'lib/pattern.cpp',
  'lib/utf8.cpp',
)

#no dllexport being used here. Must use static library.
if cpp.get_argument_syntax() != 'msvc'
  libreflexmin = library(
    'reflexmin',
    libreflexmin_sources,
    include_directories : includes)

  libreflex = library(
    'reflex',
    libreflex_sources, unicode_sources,
    include_directories : includes)
else
  libreflexmin = static_library(
    'reflexmin',
    libreflexmin_sources,
    include_directories : includes)

  libreflex = static_library(
    'reflex',
    libreflex_sources, unicode_sources,
    include_directories : includes)
endif

subdir('src')

reflex_dep = declare_dependency(
  link_with : libreflex,
  include_directories : includes)
