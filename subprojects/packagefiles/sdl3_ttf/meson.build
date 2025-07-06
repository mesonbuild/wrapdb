project(
  'sdl3_ttf',
  'c',
  license: 'zlib',
  version: '3.2.2',
)

sdl_dep = dependency(
  'sdl3',
  version: '>=3.2.6',
)

freetype_dep = dependency('freetype2')
thread_dep = dependency(
  'threads',
  required: false,
)
harfbuzz_dep = dependency(
  'harfbuzz',
  required: false,
)
plutosvg_dep = dependency(
  'plutosvg',
  required: false,
)

subdir('src')
ttf_lib = library(
  'sdl3_ttf',
  ttf_src,
  include_directories: 'include',
  dependencies: [sdl_dep, freetype_dep, thread_dep, harfbuzz_dep, plutosvg_dep],
)

sdl3_ttf_dep = declare_dependency(
  include_directories: 'include',
  link_with: ttf_lib,
)
