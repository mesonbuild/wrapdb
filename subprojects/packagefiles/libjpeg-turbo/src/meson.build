jconfig_h = configure_file(
  input: 'jconfig.h.in',
  output: 'jconfig.h',
  format: 'cmake@',
  configuration: cdata,
)

configure_file(
  input: 'jconfigint.h.in',
  output: 'jconfigint.h',
  format: 'cmake@',
  configuration: cdata,
)

configure_file(
  input: 'jversion.h.in',
  output: 'jversion.h',
  format: 'cmake@',
  configuration: cdata,
)

install_headers('jmorecfg.h', 'jerror.h', 'jpeglib.h', jconfig_h)

sources = files(
  'jcapimin.c',
  'jchuff.c',
  'jcicc.c',
  'jcinit.c',
  'jclhuff.c',
  'jcmarker.c',
  'jcmaster.c',
  'jcomapi.c',
  'jcparam.c',
  'jcphuff.c',
  'jctrans.c',
  'jdapimin.c',
  'jdatadst.c',
  'jdatasrc.c',
  'jdhuff.c',
  'jdicc.c',
  'jdinput.c',
  'jdlhuff.c',
  'jdmarker.c',
  'jdmaster.c',
  'jdphuff.c',
  'jdtrans.c',
  'jerror.c',
  'jfdctflt.c',
  'jmemmgr.c',
  'jmemnobs.c',
  'jpeg_nbits.c',
  'wrapper/jcapistd-12.c',
  'wrapper/jcapistd-16.c',
  'wrapper/jcapistd-8.c',
  'wrapper/jccoefct-12.c',
  'wrapper/jccoefct-8.c',
  'wrapper/jccolor-12.c',
  'wrapper/jccolor-16.c',
  'wrapper/jccolor-8.c',
  'wrapper/jcdctmgr-12.c',
  'wrapper/jcdctmgr-8.c',
  'wrapper/jcdiffct-12.c',
  'wrapper/jcdiffct-16.c',
  'wrapper/jcdiffct-8.c',
  'wrapper/jclossls-12.c',
  'wrapper/jclossls-16.c',
  'wrapper/jclossls-8.c',
  'wrapper/jcmainct-12.c',
  'wrapper/jcmainct-16.c',
  'wrapper/jcmainct-8.c',
  'wrapper/jcprepct-12.c',
  'wrapper/jcprepct-16.c',
  'wrapper/jcprepct-8.c',
  'wrapper/jcsample-12.c',
  'wrapper/jcsample-16.c',
  'wrapper/jcsample-8.c',
  'wrapper/jdapistd-12.c',
  'wrapper/jdapistd-16.c',
  'wrapper/jdapistd-8.c',
  'wrapper/jdcoefct-12.c',
  'wrapper/jdcoefct-8.c',
  'wrapper/jdcolor-12.c',
  'wrapper/jdcolor-16.c',
  'wrapper/jdcolor-8.c',
  'wrapper/jddctmgr-12.c',
  'wrapper/jddctmgr-8.c',
  'wrapper/jddiffct-12.c',
  'wrapper/jddiffct-16.c',
  'wrapper/jddiffct-8.c',
  'wrapper/jdlossls-12.c',
  'wrapper/jdlossls-16.c',
  'wrapper/jdlossls-8.c',
  'wrapper/jdmainct-12.c',
  'wrapper/jdmainct-16.c',
  'wrapper/jdmainct-8.c',
  'wrapper/jdmerge-12.c',
  'wrapper/jdmerge-8.c',
  'wrapper/jdpostct-12.c',
  'wrapper/jdpostct-16.c',
  'wrapper/jdpostct-8.c',
  'wrapper/jdsample-12.c',
  'wrapper/jdsample-16.c',
  'wrapper/jdsample-8.c',
  'wrapper/jfdctfst-12.c',
  'wrapper/jfdctfst-8.c',
  'wrapper/jfdctint-12.c',
  'wrapper/jfdctint-8.c',
  'wrapper/jidctflt-12.c',
  'wrapper/jidctflt-8.c',
  'wrapper/jidctfst-12.c',
  'wrapper/jidctfst-8.c',
  'wrapper/jidctint-12.c',
  'wrapper/jidctint-8.c',
  'wrapper/jidctred-12.c',
  'wrapper/jidctred-8.c',
  'wrapper/jquant1-12.c',
  'wrapper/jquant1-8.c',
  'wrapper/jquant2-12.c',
  'wrapper/jquant2-8.c',
  'wrapper/jutils-12.c',
  'wrapper/jutils-16.c',
  'wrapper/jutils-8.c',
)

sources += files(
# TODO: `with_arith_dec` / `with_arith_enc` only.
  'jaricom.c',
  # TODO: `with_arith_enc` only
  'jcarith.c',
  # TODO: `with_arith_dec` only
  'jdarith.c',
)

jpeg = library(
  'jpeg',
  sources,
  link_whole: simd,
  soversion: so_version,
  vs_module_defs: vs_defs,
  install: true,
)

pkg.generate(
  jpeg,
  description: 'A SIMD-accelerated JPEG codec that provides the libjpeg API',
  name: 'libjpeg',
)

jpeg_dep = declare_dependency(
  include_directories: incdir,
  link_with: jpeg,
)
meson.override_dependency('libjpeg', jpeg_dep)

if get_option('turbojpeg').allowed()
  install_headers('turbojpeg.h')

  turbojpeg = library(
    'turbojpeg',
    sources,
    files(
      'jdatadst-tj.c',
      'jdatasrc-tj.c',
      'rdbmp.c',
      'transupp.c',
      'turbojpeg.c',
      'wrapper/rdppm-12.c',
      'wrapper/rdppm-16.c',
      'wrapper/rdppm-8.c',
      'wrapper/wrppm-12.c',
      'wrapper/wrppm-16.c',
      'wrapper/wrppm-8.c',
      'wrbmp.c',
    ),
    c_args: ['-DBMP_SUPPORTED', '-DPPM_SUPPORTED'],
    install: true,
    link_whole: simd,
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

if get_option('tests').require(
  get_option('turbojpeg').allowed(),
  error_message: 'turbojpeg feature needed',
).allowed()
  tjunittest = executable(
    'tjunittest',
    ['tjunittest.c', 'tjutil.c', 'md5/md5.c', 'md5/md5hl.c'],
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
