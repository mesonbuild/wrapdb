# @todo Functionality missing from this port yet:
# - check minimum dependency versions
# - poppler-data
# - Gtk documentation
# - manual and unit tests in test
# - fuzz tests
# - gperf
# - libjpeg version test
# - version script for linker?


project(
  'poppler',
  'cpp',
  'c',
  version: '26.02.0',
  license: 'GPL-2.0',
  meson_version: '>=1.3.0',
  default_options: {
    'cpp_std': 'c++23',
  },
)

poppler_version = meson.project_version()
poppler_version_parts = poppler_version.split('.')
poppler_major_version = poppler_version_parts[0]
poppler_minor_version = poppler_version_parts[1]
poppler_micro_version = poppler_version_parts[2]
poppler_library_so_version = 157
poppler_library_version = poppler_library_so_version.to_string() + '.0.0'

cpp_compiler = meson.get_compiler('cpp')
have_fseek64 = cpp_compiler.has_function('fseek64')
have_fseeko = cpp_compiler.has_header_symbol('stdio.h', 'fseeko')
have_gmtime_r = cpp_compiler.has_function('gmtime_r')
have_localtime_r = cpp_compiler.has_function('localtime_r')
have_lseek64 = cpp_compiler.has_function('lseek64')
have_popen = cpp_compiler.has_function('popen')
have_pread64 = cpp_compiler.has_function('pread64')
have_strtok_r = cpp_compiler.has_function('strtok_r')
have_timegm = cpp_compiler.has_function('timegm')

poppler_library_cpp_arguments = []

poppler_library_dependencies = [
  dependency(
    'freetype2',
    version: '>=2.11',
  ),
  dependency('zlib'),
]

poppler_library_include_directories = include_directories('.', 'poppler')

poppler_library_sources = [
  'goo/GooString.cc',
  'goo/GooTimer.cc',
  'goo/ImgWriter.cc',
  'goo/JpegWriter.cc',
  'goo/NetPBMWriter.cc',
  'goo/PNGWriter.cc',
  'goo/TiffWriter.cc',
  'goo/ft_utils.cc',
  'goo/gbase64.cc',
  'goo/gbasename.cc',
  'goo/gfile.cc',
  'goo/glibc.cc',
  'goo/glibc_strtok_r.cc',
  'goo/grandom.cc',
  'goo/gstrtod.cc',
  'fofi/FoFiBase.cc',
  'fofi/FoFiEncodings.cc',
  'fofi/FoFiTrueType.cc',
  'fofi/FoFiType1.cc',
  'fofi/FoFiType1C.cc',
  'fofi/FoFiIdentifier.cc',
  'poppler/Annot.cc',
  'poppler/AnnotStampImageHelper.cc',
  'poppler/Array.cc',
  'poppler/CachedFile.cc',
  'poppler/Catalog.cc',
  'poppler/CharCodeToUnicode.cc',
  'poppler/CMap.cc',
  'poppler/CryptoSignBackend.cc',
  'poppler/DateInfo.cc',
  'poppler/Decrypt.cc',
  'poppler/Dict.cc',
  'poppler/Error.cc',
  'poppler/FDPDFDocBuilder.cc',
  'poppler/FILECacheLoader.cc',
  'poppler/FileSpec.cc',
  'poppler/FlateEncoder.cc',
  'poppler/FontEncodingTables.cc',
  'poppler/Form.cc',
  'poppler/FontInfo.cc',
  'poppler/Function.cc',
  'poppler/Gfx.cc',
  'poppler/GfxFont.cc',
  'poppler/GfxState.cc',
  'poppler/GlobalParams.cc',
  'poppler/Hints.cc',
  'poppler/ImageEmbeddingUtils.cc',
  'poppler/JArithmeticDecoder.cc',
  'poppler/JBIG2Stream.cc',
  'poppler/JSInfo.cc',
  'poppler/Lexer.cc',
  'poppler/Link.cc',
  'poppler/Linearization.cc',
  'poppler/LocalPDFDocBuilder.cc',
  'poppler/MarkedContentOutputDev.cc',
  'poppler/NameToCharCode.cc',
  'poppler/Object.cc',
  'poppler/OptionalContent.cc',
  'poppler/Outline.cc',
  'poppler/OutputDev.cc',
  'poppler/Page.cc',
  'poppler/PageTransition.cc',
  'poppler/Parser.cc',
  'poppler/PDFDoc.cc',
  'poppler/PDFDocBuilder.cc',
  'poppler/PDFDocEncoding.cc',
  'poppler/PDFDocFactory.cc',
  'poppler/ProfileData.cc',
  'poppler/PreScanOutputDev.cc',
  'poppler/PSTokenizer.cc',
  'poppler/SignatureInfo.cc',
  'poppler/Stream.cc',
  'poppler/StructTreeRoot.cc',
  'poppler/StructElement.cc',
  'poppler/UnicodeMap.cc',
  'poppler/UnicodeMapFuncs.cc',
  'poppler/UnicodeTypeTable.cc',
  'poppler/UTF.cc',
  'poppler/XRef.cc',
  'poppler/PSOutputDev.cc',
  'poppler/TextOutputDev.cc',
  'poppler/PageLabelInfo.cc',
  'poppler/SecurityHandler.cc',
  'poppler/Sound.cc',
  'poppler/ViewerPreferences.cc',
  'poppler/Movie.cc',
  'poppler/Rendition.cc',
  'poppler/CertificateInfo.cc',
  'poppler/BBoxOutputDev.cc',
  'poppler/SplashOutputDev.cc',
  'splash/Splash.cc',
  'splash/SplashBitmap.cc',
  'splash/SplashClip.cc',
  'splash/SplashFTFont.cc',
  'splash/SplashFTFontEngine.cc',
  'splash/SplashFTFontFile.cc',
  'splash/SplashFont.cc',
  'splash/SplashFontEngine.cc',
  'splash/SplashFontFile.cc',
  'splash/SplashFontFileID.cc',
  'splash/SplashPath.cc',
  'splash/SplashPattern.cc',
  'splash/SplashScreen.cc',
  'splash/SplashState.cc',
  'splash/SplashXPath.cc',
  'splash/SplashXPathScanner.cc',
]

# optional libcurl support
libcurl_depedency = dependency(
  'libcurl',
  version: '>=7.81',
  required: get_option('libcurl'),
)
enable_libcurl = libcurl_depedency.found()
if enable_libcurl == true
  poppler_library_sources += [
    'poppler/CurlCachedFile.cc',
    'poppler/CurlPDFDocBuilder.cc',
  ]
  poppler_library_dependencies += libcurl_depedency
endif

# optional lcms2 dependency
lcms2_dependency = dependency(
  'lcms2',
  version: '>= 2.12',
  required: get_option('lcms2'),
)
enable_lcms2 = lcms2_dependency.found()
if enable_lcms2 == true
  poppler_library_dependencies += lcms2_dependency
endif

# optional libpng dependency
libpng_dependency = dependency(
  'libpng',
  required: get_option('libpng'),
)
enable_libpng = libpng_dependency.found()
if enable_libpng == true
  poppler_library_dependencies += libpng_dependency
endif

# optional libtiff dependency
libtiff_4_dependency = dependency(
  'libtiff-4',
  version: '>=4.3',
  required: get_option('libtiff'),
)
enable_libtiff_4 = libtiff_4_dependency.found()
if enable_libtiff_4 == true
  poppler_library_dependencies += libtiff_4_dependency
endif

# gather signature backends
signature_backends = []

# optional nss dependency
nss_dependency = dependency(
  'nss',
  version: '>=3.68',
  required: get_option('nss'),
)
enable_nss = nss_dependency.found()
if enable_nss == true
  poppler_library_sources += ['poppler/NSSCryptoSignBackend.cc']
  poppler_library_dependencies += nss_dependency
  signature_backends += 'NSS'
endif

# optional gpgmepp dependency
gpgmepp_dependency = dependency(
  'gpgmepp',
  version: '>=1.19',
  required: get_option('gpgmepp'),
)
enable_gpgmepp = gpgmepp_dependency.found()
if enable_gpgmepp == true
  poppler_library_sources += ['poppler/GPGMECryptoSignBackend.cc']
  poppler_library_dependencies += gpgmepp_dependency
  signature_backends += 'GPG'
endif

# default_signature_backend depends on the backends gathered
if signature_backends.length() > 0
  default_signature_backend = signature_backends[0]
else
  default_signature_backend = 'None'
endif
enable_signatures = enable_nss or enable_gpgmepp

# option 'dct_decoder'
if get_option('dct_decoder') == 'libjpeg'
  libjpeg_dependency = dependency('libjpeg')
  enable_libjpeg = true
  have_dct_decoder = true
  poppler_library_dependencies += libjpeg_dependency
  poppler_library_sources += 'poppler/DCTStream.cc'
else
  enable_libjpeg = false
  if get_option('dct_decoder') == 'unmaintained'
    have_dct_decoder = true
  else  # none
    have_dct_decoder = false
  endif
endif

# JPEG2000 support
if get_option('jpx_decoder') == 'libopenjp2'
  libopenjp2_dependency = dependency(
    'libopenjp2',
    version: '>=2',
  )
  enable_libopenjp2 = true
  have_jpx_decoder = true
  poppler_library_dependencies += libopenjp2_dependency
  poppler_library_sources += 'poppler/JPEG2000Stream.cc'
else
  enable_libopenjp2 = false
  poppler_library_sources += 'poppler/JPXStream.cc'
  if get_option('jpx_decoder') == 'unmaintained'
    have_jpx_decoder = true
  else  # none
    have_jpx_decoder = false
  endif
endif

# Boost support
boost_dependency = dependency(
  'boost',
  required: get_option('boost'),
)
use_boost_headers = boost_dependency.found()
if use_boost_headers == true
  poppler_library_dependencies += boost_dependency
endif


# GLib wrapper
glib_dependency = dependency(
  'glib-2.0',
  version: '>=2.72',
  required: get_option('glib'),
)
gobject_dependency = dependency(
  'gobject-2.0',
  version: '>=2.72',
  required: get_option('glib'),
)
gio_dependency = dependency(
  'gio-2.0',
  version: '>=2.72',
  required: get_option('glib'),
)
have_glib = glib_dependency.found() and gobject_dependency.found() and gio_dependency.found()
cairo_dependency = dependency(
  'cairo',
  version: '>=1.16.0',
  required: have_glib,
  not_found_message: 'Cairo is required for the GLib backend.',
)
have_cairo = cairo_dependency.found()
if have_cairo == true
  cairo_feature = '#define POPPLER_HAS_CAIRO 1'
else
  cairo_feature = '#undef POPPLER_HAS_CAIRO'
endif
building_glib_wrapper = have_cairo and have_glib
if have_glib == true
  gtk3_dependency = dependency(
    'gtk+-3.0',
    version: '>=3.24',
    required: have_glib,
  )
else
  gtk3_dependency = disabler()
endif


# cpp wrapper requires iconv
## this needs to be discovered here, so we can set the ICONV_CONST configuration
iconv_dependency = dependency(
  'iconv',
  required: get_option('cpp'),
)
compile_check_iconv_const = false
if iconv_dependency.found() == true
  compile_check_iconv_const = cpp_compiler.compiles(
    '''
  #include <iconv.h>
  int main(){
    iconv_t conv = 0;
    const char* in = 0;
    size_t ilen = 0;
    char* out = 0;
    size_t olen = 0;
    iconv(conv, &in, &ilen, &out, &olen);
    return 0;
  }''',
    dependencies: [iconv_dependency],
    werror: true,
  )
endif


# relocatable is a Windows-only feature
enable_relocatable = false
# @todo allow turning it off via options
if host_machine.system() == 'windows'
  enable_relocatable = true
endif

# fontconfig / font configuration support
with_font_configuration_android = false
with_font_configuration_fontconfig = false
with_font_configuration_win32 = false
if host_machine.system() == 'windows'
  font_configuration = 'win32'
  with_font_configuration_win32 = true
elif host_machine.system() == 'android'
  font_configuration == 'android'
  with_font_configuration_android = true
else
  font_configuration = 'fontconfig'
  poppler_library_dependencies += dependency('fontconfig')
  with_font_configuration_fontconfig = true
endif

poppler_font_widths = [
  'CourierWidths',
  'CourierBoldWidths',
  'CourierBoldObliqueWidths',
  'CourierObliqueWidths',
  'HelveticaWidths',
  'HelveticaBoldWidths',
  'HelveticaBoldObliqueWidths',
  'HelveticaObliqueWidths',
  'SymbolWidths',
  'TimesBoldWidths',
  'TimesBoldItalicWidths',
  'TimesItalicWidths',
  'TimesRomanWidths',
  'ZapfDingbatsWidths',
]

# @todo add generator for font width files with gperf
foreach poppler_font_width : poppler_font_widths
  poppler_library_sources += [
    'poppler' / (
      poppler_font_width + '.pregenerated.c'
    ),
  ]
endforeach

poppler_configuration = configuration_data()
poppler_configuration.set('POPPLER_VERSION', meson.project_version())
poppler_configuration.set('POPPLER_MAJOR_VERSION', poppler_major_version)
poppler_configuration.set('POPPLER_MINOR_VERSION', poppler_minor_version)
poppler_configuration.set('POPPLER_MICRO_VERSION', poppler_micro_version)
poppler_configuration.set10('HAVE_FSEEK64', have_fseek64)
poppler_configuration.set10('HAVE_FSEEKO', have_fseeko)
poppler_configuration.set10('HAVE_GMTIME_R', have_gmtime_r)
poppler_configuration.set10('HAVE_LOCALTIME_R', have_localtime_r)
poppler_configuration.set10('HAVE_LSEEK64', have_lseek64)
poppler_configuration.set10('HAVE_POPEN', have_popen)
poppler_configuration.set10('HAVE_PREAD64', have_pread64)
poppler_configuration.set10('HAVE_STRTOK_R', have_strtok_r)
poppler_configuration.set10('HAVE_TIMEGM', have_timegm)
poppler_configuration.set(
  'ICONV_CONST',
  compile_check_iconv_const ? 'const' : '',
)
poppler_configuration.set10('ENABLE_LIBCURL', enable_libcurl)
poppler_configuration.set10('POPPLER_HAS_CURL_SUPPORT', enable_libcurl)
poppler_configuration.set10('ENABLE_LIBJPEG', enable_libjpeg)
poppler_configuration.set10('ENABLE_LCMS', enable_lcms2)
poppler_configuration.set10('USE_CMS', enable_lcms2)
poppler_configuration.set10('ENABLE_LIBPNG', enable_libpng)
poppler_configuration.set10('ENABLE_LIBTIFF', enable_libtiff_4)
poppler_configuration.set10('ENABLE_NSS3', enable_nss)
poppler_configuration.set10('ENABLE_GPGME', enable_gpgmepp)
poppler_configuration.set10('ENABLE_SIGNATURES', enable_signatures)
poppler_configuration.set('DEFAULT_SIGNATURE_BACKEND', default_signature_backend)
poppler_configuration.set10('HAVE_DCT_DECODER', have_dct_decoder)
poppler_configuration.set10('ENABLE_LIBOPENJPEG', enable_libopenjp2)
poppler_configuration.set10('HAVE_JPX_DECODER', have_jpx_decoder)
poppler_configuration.set10('ENABLE_RELOCATABLE', enable_relocatable)
poppler_configuration.set10(
  'WITH_FONTCONFIGURATION_WIN32',
  with_font_configuration_win32,
)
poppler_configuration.set10(
  'WITH_FONTCONFIGURATION_FONTCONFIG',
  with_font_configuration_fontconfig,
)
poppler_configuration.set10(
  'WITH_FONTCONFIGURATION_ANDROID',
  with_font_configuration_android,
)
poppler_configuration.set('CAIRO_FEATURE', cairo_feature)
# @todo ENABLE_ZLIB_UNCOMPRESS could be dependent on a meson configuration feature option 'zlib_uncompress'
poppler_configuration.set10('ENABLE_ZLIB_UNCOMPRESS', false)
# @todo ENABLE_PGP_SIGNATURES should be dependent on a meson configuration feature option 'pgp_signatures'
poppler_configuration.set10('ENABLE_PGP_SIGNATURES', false)
# @todo POPPLER_DATADIR should be dependent on the pkgconfig of the poppler-data project.
poppler_configuration.set(
  'POPPLER_DATADIR',
  get_option('prefix') / 'share' / 'poppler',
)
poppler_configuration.set10('USE_BOOST_HEADERS', use_boost_headers)
poppler_configuration.set10('USE_FLOAT', get_option('use_float'))
poppler_configuration.set10('WORDS_BIGENDIAN', host_machine.endian() == 'big')
configure_file(
  configuration: poppler_configuration,
  format: 'cmake',
  input: 'config.h.cmake',
  output: 'config.h',
)

subdir('poppler')

# defines for poppler_private_export.h
if get_option('default_library') != 'static'
  poppler_library_cpp_arguments += '-DPOPPLER_PRIVATE_EXPORTS'
else
  poppler_library_cpp_arguments += '-DPOPPLER_PRIVATE_STATIC_DEFINE'
endif

# MSVC complains about dll-interface for embedded members of the internal API library
if cpp_compiler.get_id() == 'msvc'
  poppler_library_cpp_arguments += '/wd4251'
endif

poppler_library = library(
  'poppler',
  cpp_args: poppler_library_cpp_arguments,
  dependencies: poppler_library_dependencies,
  include_directories: poppler_library_include_directories,
  install: true,
  sources: poppler_library_sources,
  soversion: poppler_library_so_version,
  version: poppler_library_version,
)

pkgconfig_module = import('pkgconfig')
pkgconfig_module.generate(
  poppler_library,
  description: 'PDF rendering library.',
)

poppler_library_dependency = declare_dependency(
  include_directories: poppler_library_include_directories,
  dependencies: poppler_library_dependencies,
  link_with: poppler_library,
)
meson.override_dependency('poppler', poppler_library_dependency)

if get_option('tests') == true
  poppler_test_subproject = subproject('poppler-test')
  poppler_test_directory = poppler_test_subproject.get_variable(
    'poppler_test_directory',
  )
endif

utils_include_directory = include_directories('utils')
subdir('utils')
subdir('cpp')
subdir('glib')
subdir('qt5')
subdir('qt6')
subdir('test')

summary(
  {
    'font_configuration': font_configuration,
    'dct_decoder': get_option('dct_decoder'),
    'jpx_decoder': get_option('jpx_decoder'),
    'use boost': use_boost_headers,
    'use lcms2': enable_lcms2,
    'use libcurl': enable_libcurl,
    'use libpng': enable_libpng,
    'use libtiff': enable_libtiff_4,
    'use nss': enable_nss,
    'use gpgmepp': enable_gpgmepp,
    'splash precision': get_option('use_float') ? 'float' : 'double',
    'C++ wrapper': building_cpp_wrapper,
    'GLib wrapper': building_glib_wrapper,
    '  GLib demo': building_glib_wrapper_demo,
    '  GObject introspection': building_gobject_introspection,
    'Qt5 wrapper': building_qt5_wrapper,
    '  Qt5 demo': building_qt5_wrapper_demo,
    'Qt6 wrapper': building_qt6_wrapper,
    '  Qt6 demo': building_qt6_wrapper_demo,
    'tests': get_option('tests'),
    'tools': building_tools,
  },
)
