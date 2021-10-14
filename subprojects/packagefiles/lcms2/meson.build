project('Little-CMS', 'c',
  version: '2.12',
  meson_version: '>=0.55.0',
)

library_version = '2.0.12'

cc = meson.get_compiler('c')

lcms2_srcs = [
  'src/cmsalpha.c',
  'src/cmscgats.c',
  'src/cmserr.c',
  'src/cmsgmt.c',
  'src/cmsintrp.c',
  'src/cmsio1.c',
  'src/cmsmd5.c',
  'src/cmsnamed.c',
  'src/cmspack.c',
  'src/cmsplugin.c',
  'src/cmssamp.c',
  'src/cmstypes.c',
  'src/cmswtpnt.c',
  'src/cmscam02.c',
  'src/cmscnvrt.c',
  'src/cmsgamma.c',
  'src/cmshalf.c',
  'src/cmsio0.c',
  'src/cmslut.c',
  'src/cmsmtrx.c',
  'src/cmsopt.c',
  'src/cmspcs.c',
  'src/cmsps2.c',
  'src/cmssm.c',
  'src/cmsvirt.c',
  'src/cmsxform.c',
]

install_headers([
  'include/lcms2.h',
  'include/lcms2_plugin.h'
])

inc_dirs = include_directories('include')

deps = [
  cc.find_library('m', required: false),
  dependency('threads'),
  dependency('zlib'),
  dependency('libtiff-4'),
]

cargs = ['-DHasTHREADS=1', '-DHasZLIB=1', '-DHasTIFF=1']

if cc.has_argument('-fvisibility')
  cargs +='-DHAVE_FUNC_ATTRIBUTE_VISIBILITY=1'
elif cc.get_id() == 'msvc'
  cargs += '-DCMS_DLL_BUILD=1'
endif

liblcms2_lib = library('lcms2', lcms2_srcs,
  include_directories : inc_dirs,
  gnu_symbol_visibility: 'hidden',
  dependencies: deps,
  c_args: cargs,
  version: library_version,
  install: true,
)

liblcms2_dep = declare_dependency(
  link_with : liblcms2_lib,
  include_directories : inc_dirs
)

pkg = import('pkgconfig')
pkg.generate(liblcms2_lib)
