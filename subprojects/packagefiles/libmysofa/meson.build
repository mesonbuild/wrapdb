project(
  'libmysofa',
  'c',
  meson_version: '>= 0.63.0',
  version: '1.3.2',
  license: 'BSD-3-Clause',
  default_options: [
    'warning_level=2',
    meson.version().version_compare('>=1.3.0') ? 'c_std=gnu99,c99' : 'c_std=gnu99',
  ],
)

cc = meson.get_compiler('c')
pkg = import('pkgconfig')
if cc.links('#include <math.h>\nint main(){log(0);}')
  m_dep = declare_dependency()
else
  m_dep = cc.find_library('m')
endif
zlib = dependency('zlib')

conf_data = configuration_data()
conf_data.set('CMAKE_INSTALL_PREFIX', get_option('prefix'))

version_split = meson.project_version().split('.')
conf_data.set('CPACK_PACKAGE_VERSION_MAJOR', version_split[0])
conf_data.set('CPACK_PACKAGE_VERSION_MINOR', version_split[1])
conf_data.set('CPACK_PACKAGE_VERSION_PATCH', version_split[2])

configure_file(
  input: 'src/config.h.in',
  output: 'config.h',
  configuration: conf_data,
  format: 'cmake',
)

subdir('src/hrtf')

includes = include_directories('src/', 'src/hdf', 'src/hrtf', 'src/resampler')

sources = files(
  'src/hdf/btree.c',
  'src/hdf/dataobject.c',
  'src/hdf/fractalhead.c',
  'src/hdf/gcol.c',
  'src/hdf/gunzip.c',
  'src/hdf/superblock.c',
  'src/hrtf/cache.c',
  'src/hrtf/check.c',
  'src/hrtf/easy.c',
  'src/hrtf/interpolate.c',
  'src/hrtf/kdtree.c',
  'src/hrtf/lookup.c',
  'src/hrtf/loudness.c',
  'src/hrtf/minphase.c',
  'src/hrtf/neighbors.c',
  'src/hrtf/reader.c',
  'src/hrtf/resample.c',
  'src/hrtf/spherical.c',
  'src/hrtf/tools.c',
  'src/resampler/speex_resampler.c',
)

libmysofa = library(
  'mysofa',
  sources,
  install: true,
  include_directories: includes,
  dependencies: [zlib, m_dep],
  gnu_symbol_visibility: 'hidden',
  vs_module_defs: 'libmysofa.def',
)

pkg.generate(libmysofa)

libmysofa_dep = declare_dependency(
  include_directories: includes,
  link_with: libmysofa,
)

meson.override_dependency('libmysofa', libmysofa_dep)
