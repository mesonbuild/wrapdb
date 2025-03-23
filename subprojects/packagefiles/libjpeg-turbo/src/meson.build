jconfig_h = configure_file(input: 'jconfig.h.in',
  output: 'jconfig.h',
  format: 'cmake@',
  configuration: cdata)

configure_file(input: 'jconfigint.h.in',
  output: 'jconfigint.h',
  format: 'cmake@',
  configuration: cdata)

configure_file(input: 'jversion.h.in',
  output: 'jversion.h',
  format: 'cmake@',
  configuration: cdata)

install_headers('jmorecfg.h', 'jerror.h', 'jpeglib.h', jconfig_h)

jpeg16_sources = [
  'jcapistd.c', 'jccolor.c', 'jcdiffct.c', 'jclossls.c', 'jcmainct.c',
  'jcprepct.c', 'jcsample.c', 'jdapistd.c', 'jdcolor.c', 'jddiffct.c',
  'jdlossls.c', 'jdmainct.c', 'jdpostct.c', 'jdsample.c', 'jutils.c',
]
jpeg12_sources = [
  jpeg16_sources, 'jccoefct.c', 'jcdctmgr.c', 'jdcoefct.c', 'jddctmgr.c',
  'jdmerge.c', 'jfdctfst.c', 'jfdctint.c', 'jidctflt.c', 'jidctfst.c',
  'jidctint.c', 'jidctred.c', 'jquant1.c', 'jquant2.c',
]
sources = [
  jpeg12_sources, 'jcapimin.c', 'jchuff.c', 'jcicc.c', 'jcinit.c',
  'jclhuff.c', 'jcmarker.c', 'jcmaster.c', 'jcomapi.c', 'jcparam.c',
  'jcphuff.c', 'jctrans.c', 'jdapimin.c', 'jdatadst.c', 'jdatasrc.c',
  'jdhuff.c', 'jdicc.c', 'jdinput.c', 'jdlhuff.c', 'jdmarker.c',
  'jdmaster.c', 'jdphuff.c', 'jdtrans.c', 'jerror.c', 'jfdctflt.c',
  'jmemmgr.c', 'jmemnobs.c', 'jpeg_nbits.c',
  # TODO: `with_arith_dec` / `with_arith_enc` only.
  'jaricom.c',
  # TODO: `with_arith_enc` only
  'jcarith.c',
  # TODO: `with_arith_dec` only
  'jdarith.c',
]

jpeg12 = static_library('jpeg12', jpeg12_sources,
  c_args: ['-DBITS_IN_JSAMPLE=12'],
  pic: get_option('default_library') != 'static',
)
jpeg16 = static_library('jpeg16', jpeg16_sources,
  c_args: ['-DBITS_IN_JSAMPLE=16'],
  pic: get_option('default_library') != 'static',
)
jpeg = library('jpeg', sources,
  link_whole: [jpeg12, jpeg16, simd],
  soversion: so_version,
  vs_module_defs: vs_defs,
  install: true,
)

pkg.generate(jpeg, description: 'A SIMD-accelerated JPEG codec that provides the libjpeg API', name: 'libjpeg')

jpeg_dep = declare_dependency(
  include_directories: incdir,
  link_with: jpeg
)

meson.override_dependency('libjpeg', jpeg_dep)

if get_option('jpeg-turbo').allowed()

  install_headers('turbojpeg.h')

  turbojpeg12 = static_library(
    'turbojpeg12',
    ['rdppm.c', 'wrppm.c'],
    c_args: ['-DBITS_IN_JSAMPLE=12', '-DPPM_SUPPORTED'],
    pic: get_option('default_library') != 'static',
  )

  turbojpeg16 = static_library(
    'turbojpeg16',
    ['rdppm.c', 'wrppm.c'],
    c_args: ['-DBITS_IN_JSAMPLE=16', '-DPPM_SUPPORTED'],
    pic: get_option('default_library') != 'static',
  )

  turbojpeg = library(
    'turbojpeg',
    sources + [
      'turbojpeg.c',
      'transupp.c',
      'jdatadst-tj.c',
      'jdatasrc-tj.c',
      'rdbmp.c',
      'rdppm.c',
      'wrbmp.c',
      'wrppm.c',
    ],
    c_args: ['-DBMP_SUPPORTED', '-DPPM_SUPPORTED'],
    install: true,
    link_with: [jpeg12, jpeg16, simd, turbojpeg12, turbojpeg16],
    soversion: '0.4.0',
  )

  pkg.generate(
    turbojpeg,
    description: 'A SIMD-accelerated JPEG codec that provides the TurboJPEG API',
    name: 'libturbojpeg',
  )

  turbojpeg_dep = declare_dependency(
    include_directories: incdir,
    link_with: turbojpeg,
  )

  meson.override_dependency('libturbojpeg', turbojpeg_dep)

endif

if get_option(
  'tests',
).require(
  get_option('jpeg-turbo').allowed(),
  error_message: 'jpeg-turbo feature needed',
).allowed()

  tjunittest = executable(
    'tjunittest',
    [
      'tjunittest.c',
      'tjutil.c',
      'md5/md5.c',
      'md5/md5hl.c',
    ],
    dependencies: turbojpeg_dep,
  )

  foreach _test, _args : {
    'tjunittest'                 : '',
    'tjunittest-alloc'           : '-alloc',
    'tjunittest-yuv'             : '-yuv',
    'tjunittest-yuv-alloc'       : '-yuv -alloc',
    'tjunittest-yuv-nopad'       : '-yuv -noyuvpad',
    'tjunittest-lossless'        : '-lossless',
    'tjunittest-lossless-alloc'  : '-lossless -alloc',
    'tjunittest-bmp'             : '-bmp',
    'tjunittest12'               : '-precision 12',
    'tjunittest12-alloc'         : '-precision 12 -alloc',
    'tjunittest12-lossless'      : '-precision 12 -lossless',
    'tjunittest12-lossless-alloc': '-precision 12 -lossless -alloc',
    'tjunittest12-bmp'           : '-precision 12 -bmp',
    'tjunittest2-lossless'       : '-precision 2',
    'tjunittest2-lossless-alloc' : '-precision 2 -alloc',
    'tjunittest2-bmp'            : '-precision 2 -bmp',
    'tjunittest3-lossless'       : '-precision 3',
    'tjunittest3-lossless-alloc' : '-precision 3 -alloc',
    'tjunittest3-bmp'            : '-precision 3 -bmp',
    'tjunittest4-lossless'       : '-precision 4',
    'tjunittest4-lossless-alloc' : '-precision 4 -alloc',
    'tjunittest4-bmp'            : '-precision 4 -bmp',
    'tjunittest5-lossless'       : '-precision 5',
    'tjunittest5-lossless-alloc' : '-precision 5 -alloc',
    'tjunittest5-bmp'            : '-precision 5 -bmp',
    'tjunittest6-lossless'       : '-precision 6',
    'tjunittest6-lossless-alloc' : '-precision 6 -alloc',
    'tjunittest6-bmp'            : '-precision 6 -bmp',
    'tjunittest7-lossless'       : '-precision 7',
    'tjunittest7-lossless-alloc' : '-precision 7 -alloc',
    'tjunittest7-bmp'            : '-precision 7 -bmp',
    'tjunittest9-lossless'       : '-precision 9',
    'tjunittest9-lossless-alloc' : '-precision 9 -alloc',
    'tjunittest9-bmp'            : '-precision 9 -bmp',
    'tjunittest10-lossless'      : '-precision 10',
    'tjunittest10-lossless-alloc': '-precision 10 -alloc',
    'tjunittest10-bmp'           : '-precision 10 -bmp',
    'tjunittest11-lossless'      : '-precision 11',
    'tjunittest11-lossless-alloc': '-precision 11 -alloc',
    'tjunittest11-bmp'           : '-precision 11 -bmp',
    'tjunittest13-lossless'      : '-precision 13',
    'tjunittest13-lossless-alloc': '-precision 13 -alloc',
    'tjunittest13-bmp'           : '-precision 13 -bmp',
    'tjunittest14-lossless'      : '-precision 14',
    'tjunittest14-lossless-alloc': '-precision 14 -alloc',
    'tjunittest14-bmp'           : '-precision 14 -bmp',
    'tjunittest15-lossless'      : '-precision 15',
    'tjunittest15-lossless-alloc': '-precision 15 -alloc',
    'tjunittest15-bmp'           : '-precision 15 -bmp',
    'tjunittest16-lossless'      : '-precision 16',
    'tjunittest16-lossless-alloc': '-precision 16 -alloc',
    'tjunittest16-bmp'           : '-precision 16 -bmp',
  }
    test(
      _test,
      tjunittest,
      args: _args.split(),
      timeout: 120,
    )
  endforeach

endif
