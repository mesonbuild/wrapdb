project(
  'sdl2_ttf',
  'c',
  version: '2.20.1',
  license: 'zlib',
  default_options: [
    meson.version().version_compare('>=1.3.0') ? 'c_std=gnu99,c99' : 'c_std=gnu99',
  ],
)

cc = meson.get_compiler('c')

c_args = []
if get_option('default_library') != 'static' and host_machine.system() == 'windows'
  c_args += '-DDLL_EXPORT'
endif

m_dep = cc.find_library(
  'm',
  required: false,
)
freetype_dep = dependency('freetype2')
sdl2_dep = dependency('sdl2')

sdl2_ttf = library(
  'sdl2_ttf',
  'SDL_ttf.c',
  c_args: c_args,
  dependencies: [freetype_dep, m_dep, sdl2_dep],
  install: true,
)

depinc = include_directories('.')
sdl2_ttf_dep = declare_dependency(
  link_with: sdl2_ttf,
  version: meson.project_version(),
  include_directories: depinc,
)
