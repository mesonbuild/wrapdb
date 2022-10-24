# source code for openjpeg apps:

cappdata = configuration_data()

if get_option('bin_png')
  libpng_dep = dependency('libpng')
else
  # always an empty not-found dependency
  libpng_dep = dependency('', required: false)
endif

if libpng_dep.found()
  cappdata.set('OPJ_HAVE_LIBPNG', 1)
  cappdata.set('OPJ_HAVE_PNG_H', 1)
endif

if get_option('bin_tiff')
  libtiff_dep = dependency('libtiff-4')
else
  # always an empty not-found dependency
  libtiff_dep = dependency('', required: false)
endif

if libtiff_dep.found()
  cappdata.set('OPJ_HAVE_LIBTIFF', 1)
  cappdata.set('OPJ_HAVE_TIFF_H', 1)
endif

if get_option('bin_lcms2')
  liblcms2_dep = dependency('lcms2')
else
  # always an empty not-found dependency
  liblcms2_dep = dependency('', required: false)
endif

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
