# source code for openjpeg apps:

cappdata = configuration_data()

libpng_dep = dependency('libpng', required: get_option('bin_png'))
if libpng_dep.found()
  cappdata.set('OPJ_HAVE_LIBPNG', 1)
  cappdata.set('OPJ_HAVE_PNG_H', 1)
endif

libtiff_dep = dependency('libtiff-4', required: get_option('bin_tiff'))
if libtiff_dep.found()
  cappdata.set('OPJ_HAVE_LIBTIFF', 1)
  cappdata.set('OPJ_HAVE_TIFF_H', 1)
endif

liblcms2_dep = dependency('lcms2', required: get_option('bin_lcms2'))
if liblcms2_dep.found()
  cappdata.set('OPJ_HAVE_LIBLCMS2', 1)
  cappdata.set('OPJ_HAVE_LCMS2_H', 1)
endif

subdir('common')
# Part 1 & 2:
subdir('jp2')
# optionals components:
if get_option('build_jpip')
  subdir('jpip')
endif

# wx apps:
subdir('wx')
