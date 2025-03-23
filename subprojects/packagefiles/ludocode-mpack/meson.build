project(
  'mpack',
  'c',
  version: '1.1.1',
  license: 'MIT',
  default_options: [
    meson.version().version_compare('>=1.3.0') ? 'c_std=gnu99,c99' : 'c_std=gnu99',
  ],
)
incdir = include_directories('src/mpack')

src = files(
  'src/mpack/mpack-common.c',
  'src/mpack/mpack-expect.c',
  'src/mpack/mpack-node.c',
  'src/mpack/mpack-platform.c',
  'src/mpack/mpack-reader.c',
  'src/mpack/mpack-writer.c',
)

headers = files('src/mpack/mpack.h')

# mpack is a copylib, so it's not intended to be built as a DLL, so it
# doesn't have any dllexport directives, so we can't build it as a DLL on
# Windows: https://github.com/mesonbuild/meson/issues/7838
# Ideally we'd only ever build it as a static library, but limit the refusal
# to MSVC for backward compatibility.
if meson.get_compiler('c').get_id() == 'msvc'
  mpack = static_library(
    'mpack',
    src,
    install: true,
  )
else
  mpack = library(
    'mpack',
    src,
    install: true,
  )
endif

ludocode_mpack_dep = declare_dependency(
  link_with: mpack,
  include_directories: incdir,
)

install_headers(headers)

pkg = import('pkgconfig')

pkg.generate(
  name: 'mpack',
  description: 'mpack msgpack serialization library',
  libraries: mpack,
)

if meson.version().version_compare('>=0.54.0')
  meson.override_dependency('ludocode-mpack', ludocode_mpack_dep)
endif
