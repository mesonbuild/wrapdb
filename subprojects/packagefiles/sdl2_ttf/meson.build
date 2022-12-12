project(
  'sdl2_ttf',
  'c',
  version: '2.20.1',
  license: 'zlib',
  default_options: ['c_std=gnu99'],
)

cc = meson.get_compiler('c')

m_dep = cc.find_library('m', required : false)
freetype_dep = dependency('freetype2')
sdl2_dep = dependency('sdl2')

sdl2_ttf = library(
  'sdl2_ttf',
  'SDL_ttf.c',
  dependencies: [freetype_dep, m_dep, sdl2_dep],
)

depinc = include_directories('.')
sdl2_ttf_dep = declare_dependency(
  link_with: sdl2_ttf,
  version: meson.project_version(),
  include_directories: depinc,
)
