project(
  'libgrapheme',
  'c',
  version: '3.0.0',
  default_options: ['c_std=c99', 'warning_level=3', 'b_lundef=false'],
  meson_version: '>=0.57.0',
  license: 'ISC',
)

foreach native : [true, false]
  add_project_arguments(
    '-D_DEFAULT_SOURCE',
    language: 'c',
    native: native,
  )
endforeach

pkg_mod = import('pkgconfig')
cc = meson.get_compiler('c')
cc_id = cc.get_id()
os_name = target_machine.system()

chdir_wrapper = files('chdir_wrapper.py')

subdir('src')

subdir('gen')

version = meson.project_version()
version_split = version.split('.')
soversion = '@0@.@1@'.format(version_split[0], version_split[1])
lib_c_args = []
lib_link_args = []

# To produce the same binary as with the Makefile approach, we need to
# add the -ffreestanding and -nostdlib flags
if get_option('stdlib') == false
  lib_c_args += ['-ffreestanding']
  lib_link_args += ['-nostdlib']
endif

libgrapheme = library(
  'grapheme',
  [src_files, gen_headers],
  install: true,
  version: version,
  soversion: soversion,
  c_args: lib_c_args,
  link_args: lib_link_args,
)

install_headers('grapheme.h')

libgrapheme_dep = declare_dependency(
  link_with: libgrapheme,
  include_directories: include_directories('.'),
)

pkg_mod.generate(
  libgrapheme,
  name: 'libgrapheme',
  description: 'Unicode string library',
  url: 'https://libs.suckless.org/libgrapheme/',
)

if get_option('test')
  subdir('test')
endif

if get_option('benchmark')
  subdir('benchmark')
endif

meson.override_dependency('libgrapheme', libgrapheme_dep)
