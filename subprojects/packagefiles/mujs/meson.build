project(
  'mujs',
  'c',
  version: '1.3.8',
  license: 'ISC',
  meson_version: '>=0.59.0',
)

override_opts = ['c_std=c99']

cc = meson.get_compiler('c')

progs_opt = get_option('progs')

m_dep = cc.find_library(
  'm',
  required: false,
)
readline_dep = dependency(
  'readline',
  required: progs_opt.disabled() ? progs_opt : false,
)

mujs_lib = library(
  'mujs',
  'one.c',
  dependencies: m_dep,
  override_options: override_opts,
  install: true,
  vs_module_defs: 'mujs.def',
)

mujs_dep = declare_dependency(
  include_directories: include_directories('.'),
  link_with: mujs_lib,
)
meson.override_dependency('mujs', mujs_dep)

pkg = import('pkgconfig')
pkg.generate(
  mujs_lib,
  description: 'MuJS embeddable Javascript interpreter',
)

install_headers('mujs.h')

if get_option('progs').allowed()
  subdir('tools')
endif
