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

poppler_configuration = configuration_data()
poppler_configuration.set('POPPLER_VERSION', meson.project_version())
poppler_version_parts = meson.project_version().split('.')
poppler_configuration.set('POPPLER_MAJOR_VERSION', poppler_version_parts[0])
poppler_configuration.set('POPPLER_MINOR_VERSION', poppler_version_parts[1])
poppler_configuration.set('POPPLER_MICRO_VERSION', poppler_version_parts[2])
poppler_library_so_version = 157
poppler_library_version = poppler_library_so_version.to_string() + '.0.0'

cpp_compiler = meson.get_compiler('cpp')
poppler_configuration.set10('HAVE_FSEEK64', cpp_compiler.has_function('fseek64'))
poppler_configuration.set10('HAVE_FSEEKO', cpp_compiler.has_header_symbol('stdio.h', 'fseeko'))
poppler_configuration.set10('HAVE_GMTIME_R', cpp_compiler.has_function('gmtime_r'))
poppler_configuration.set10('HAVE_LOCALTIME_R', cpp_compiler.has_function('localtime_r'))
poppler_configuration.set10('HAVE_LSEEK64', cpp_compiler.has_function('lseek64'))
poppler_configuration.set10('HAVE_POPEN', cpp_compiler.has_function('popen'))
poppler_configuration.set10('HAVE_PREAD64', cpp_compiler.has_function('pread64'))
poppler_configuration.set10('HAVE_STRTOK_R', cpp_compiler.has_function('strtok_r'))
poppler_configuration.set10('HAVE_TIMEGM', cpp_compiler.has_function('timegm'))

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

poppler_configuration.set10('WORDS_BIGENDIAN', host_machine.endian() == 'big')
poppler_configuration.set10('USE_FLOAT', get_option('use_float'))
summary('splash precision', get_option('use_float') ? 'float' : 'double')
# @todo ENABLE_ZLIB_UNCOMPRESS could be dependent on a meson configuration feature option 'zlib_uncompress'
poppler_configuration.set10('ENABLE_ZLIB_UNCOMPRESS', false)
# @todo ENABLE_PGP_SIGNATURES could be dependent on a meson configuration feature option 'pgp_signatures'
poppler_configuration.set10('ENABLE_PGP_SIGNATURES', false)
# @todo POPPLER_DATADIR could be dependent on a poppler-data subproject.
poppler_configuration.set('POPPLER_DATADIR', get_option('prefix') / 'share' / 'poppler')


# optional libcurl support
libcurl_dep = dependency(
  'libcurl',
  version: '>=7.81',
  required: get_option('libcurl'),
)
poppler_configuration.set10('ENABLE_LIBCURL', libcurl_dep.found())
poppler_configuration.set10('POPPLER_HAS_CURL_SUPPORT', libcurl_dep.found())
if libcurl_dep.found()
  poppler_library_sources += [
    'poppler/CurlCachedFile.cc',
    'poppler/CurlPDFDocBuilder.cc',
  ]
  poppler_library_dependencies += libcurl_dep
endif
summary('use libcurl', libcurl_dep.found())


# optional lcms2 dependency
lcms2_dep = dependency(
  'lcms2',
  version: '>= 2.12',
  required: get_option('lcms2'),
)
poppler_configuration.set10('ENABLE_LCMS', lcms2_dep.found())
poppler_configuration.set10('USE_CMS', lcms2_dep.found())
if lcms2_dep.found()
  poppler_library_dependencies += lcms2_dep
endif
summary('use lcms2', lcms2_dep.found())


# optional libpng dependency
libpng_dep = dependency(
  'libpng',
  required: get_option('libpng'),
)
poppler_configuration.set10('ENABLE_LIBPNG', libpng_dep.found())
if libpng_dep.found()
  poppler_library_dependencies += libpng_dep
endif
summary('use libpng', libpng_dep.found())


# optional libtiff dependency
libtiff_4_dep = dependency(
  'libtiff-4',
  version: '>=4.3',
  required: get_option('libtiff'),
)
poppler_configuration.set10('ENABLE_LIBTIFF', libtiff_4_dep.found())
if libtiff_4_dep.found()
  poppler_library_dependencies += libtiff_4_dep
endif
summary('use libtiff', libtiff_4_dep.found())


# gather signature backends
signature_backends = []


# optional nss dependency
nss_dep = dependency(
  'nss',
  version: '>=3.68',
  required: get_option('nss'),
)
poppler_configuration.set10('ENABLE_NSS3', nss_dep.found())
if nss_dep.found()
  poppler_library_sources += ['poppler/NSSCryptoSignBackend.cc']
  poppler_library_dependencies += nss_dep
  signature_backends += 'NSS'
endif
summary('use nss', nss_dep.found())


# optional gpgmepp dependency
gpgmepp_dep = dependency(
  'gpgmepp',
  version: '>=1.19',
  required: get_option('gpgmepp'),
)
poppler_configuration.set10('ENABLE_GPGME', gpgmepp_dep.found())
if gpgmepp_dep.found()
  poppler_library_sources += ['poppler/GPGMECryptoSignBackend.cc']
  poppler_library_dependencies += gpgmepp_dep
  signature_backends += 'GPG'
endif
summary('use gpgmepp', gpgmepp_dep.found())


# default_signature_backend depends on the backends gathered
if signature_backends.length() > 0
  poppler_configuration.set('DEFAULT_SIGNATURE_BACKEND', signature_backends[0])
else
  poppler_configuration.set('DEFAULT_SIGNATURE_BACKEND', 'None')
endif
poppler_configuration.set10('ENABLE_SIGNATURES', nss_dep.found() or gpgmepp_dep.found())


# option 'dct_decoder'
if get_option('dct_decoder') == 'libjpeg'
  libjpeg_dep = dependency('libjpeg')
  poppler_configuration.set10('ENABLE_LIBJPEG', true)
  poppler_configuration.set10('HAVE_DCT_DECODER', true)
  poppler_library_sources += 'poppler/DCTStream.cc'
  poppler_library_dependencies += libjpeg_dep
else
  poppler_configuration.set10('ENABLE_LIBJPEG', false)
  if get_option('dct_decoder') == 'unmaintained'
    poppler_configuration.set10('HAVE_DCT_DECODER', true)
  else  # none
    poppler_configuration.set10('HAVE_DCT_DECODER', false)
  endif
endif
summary('dct_decoder', get_option('dct_decoder'))


# option 'jpx_decoder'
if get_option('jpx_decoder') == 'libopenjp2'
  libopenjp2_dep = dependency(
    'libopenjp2',
    version: '>=2',
  )
  poppler_configuration.set10('ENABLE_LIBOPENJPEG', true)
  poppler_configuration.set10('HAVE_JPX_DECODER', true)
  poppler_library_sources += 'poppler/JPEG2000Stream.cc'
  poppler_library_dependencies += libopenjp2_dep
else
  poppler_configuration.set10('ENABLE_LIBOPENJPEG', false)
  poppler_library_sources += 'poppler/JPXStream.cc'
  if get_option('jpx_decoder') == 'unmaintained'
    poppler_configuration.set10('HAVE_JPX_DECODER', true)
    have_jpx_decoder = true
  else  # none
    poppler_configuration.set10('HAVE_JPX_DECODER', false)
  endif
endif
summary('jpx_decoder', get_option('jpx_decoder'))


# Boost support
boost_dep = dependency(
  'boost',
  required: get_option('boost'),
)
poppler_configuration.set10('USE_BOOST_HEADERS', boost_dep.found())
if boost_dep.found()
  poppler_library_dependencies += boost_dep
endif
summary('use boost', boost_dep.found())


# GLib wrapper
glib_dep = dependency(
  'glib-2.0',
  version: '>=2.72',
  required: get_option('glib'),
)
gobject_dep = dependency(
  'gobject-2.0',
  version: '>=2.72',
  required: get_option('glib'),
)
gio_dep = dependency(
  'gio-2.0',
  version: '>=2.72',
  required: get_option('glib'),
)
have_glib = glib_dep.found() and gobject_dep.found() and gio_dep.found()
cairo_dep = dependency(
  'cairo',
  version: '>=1.16.0',
  required: have_glib,
  not_found_message: 'Cairo is required for the GLib backend.',
)
if cairo_dep.found()
  poppler_configuration.set('CAIRO_FEATURE', '#define POPPLER_HAS_CAIRO 1')
else
  poppler_configuration.set('CAIRO_FEATURE', '#undef POPPLER_HAS_CAIRO')
endif
building_glib_wrapper = cairo_dep.found() and have_glib
if have_glib
  gtk3_dep = dependency(
    'gtk+-3.0',
    version: '>=3.24',
    required: false,
  )
else
  gtk3_dep = disabler()
endif


# cpp wrapper requires iconv
## this needs to be discovered here, so we can set the ICONV_CONST configuration
iconv_dep = dependency(
  'iconv',
  required: get_option('cpp'),
)
if iconv_dep.found() and cpp_compiler.compiles(
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
    dependencies: [iconv_dep],
    werror: true,
  )
  poppler_configuration.set('ICONV_CONST', 'const')
else
  poppler_configuration.set('ICONV_CONST', '')
endif


# relocatable is a Windows-only feature
# @todo allow turning it off via options
poppler_configuration.set10('ENABLE_RELOCATABLE', host_machine.system() == 'windows')


# fontconfig / font configuration support
if host_machine.system() == 'windows'
  poppler_configuration.set10('WITH_FONTCONFIGURATION_WIN32', true)
  poppler_configuration.set10('WITH_FONTCONFIGURATION_FONTCONFIG', false)
  poppler_configuration.set10('WITH_FONTCONFIGURATION_ANDROID', false)
  summary('font_configuration', 'win32')
elif host_machine.system() == 'android'
  poppler_configuration.set10('WITH_FONTCONFIGURATION_WIN32', false)
  poppler_configuration.set10('WITH_FONTCONFIGURATION_FONTCONFIG', false)
  poppler_configuration.set10('WITH_FONTCONFIGURATION_ANDROID', true)
  summary('font_configuration', 'android')
else
  poppler_configuration.set10('WITH_FONTCONFIGURATION_WIN32', false)
  poppler_configuration.set10('WITH_FONTCONFIGURATION_FONTCONFIG', false)
  poppler_configuration.set10('WITH_FONTCONFIGURATION_ANDROID', true)
  poppler_library_dependencies += dependency('fontconfig')
  summary('font_configuration', 'fontconfig')
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

configure_file(
  configuration: poppler_configuration,
  format: 'cmake',
  input: 'config.h.cmake',
  output: 'config.h',
)

subdir('poppler')

poppler_exports_h_in = files('poppler_exports.h.in')
# exports header file for private library
poppler_exports_h = configure_file(
  input: poppler_exports_h_in,
  output: 'poppler_private_export.h',
  configuration: {
    'NAME': 'PRIVATE',
    'PUBLIC_DEFINE': 'POPPLER_PRIVATE_EXPORT'
  }
)
poppler_library_sources += poppler_exports_h

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

poppler_library_dep = declare_dependency(
  include_directories: poppler_library_include_directories,
  dependencies: poppler_library_dependencies,
  link_with: poppler_library,
)
meson.override_dependency('poppler', poppler_library_dep)

if get_option('tests')
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
