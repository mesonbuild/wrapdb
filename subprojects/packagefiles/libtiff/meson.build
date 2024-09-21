project(
  'tiff',
  'c',
  version: files('VERSION'),
  meson_version: '>=0.57.0',
)
# calculate library version from configure.ac values
libtiff_current = 7
libtiff_revision = 0
libtiff_age = 1
library_version = '@0@.@1@.@2@'.format(
    libtiff_current - libtiff_age,
    libtiff_age,
    libtiff_revision
)

cc = meson.get_compiler('c')
m_dep = cc.find_library('m', required: false)
jbig_dep = cc.find_library('jbig', required: get_option('jbig'))
jpeg_dep = dependency('libjpeg', required: get_option('jpeg'))
lerc_dep = dependency('liblerc', required: get_option('lerc'))
lzma_dep = dependency('liblzma', required: get_option('lzma'))
webp_dep = dependency('libwebp', required: get_option('webp'))
zlib_dep = dependency('zlib', required: get_option('zlib'))
zstd_dep = dependency('libzstd', required: get_option('zstd'))

cdata = configuration_data()

cdata.set10('HOST_BIG_ENDIAN', host_machine.endian() == 'big')
if host_machine.endian() == 'big'
  # missing cmakedefine in tif_config.h.cmake.in
  # https://gitlab.com/libtiff/libtiff/-/merge_requests/664
  # this is how upstream handles it in cmake/ProcessorChecks.cmake
  add_project_arguments('-DWORDS_BIGENDIAN', language : 'c')
endif

cdata.set('TIFF_INT8_T', 'int8_t')
cdata.set('TIFF_UINT8_T', 'uint8_t')
cdata.set('TIFF_INT16_T', 'int16_t')
cdata.set('TIFF_UINT16_T', 'uint16_t')
cdata.set('TIFF_INT32_T', 'int32_t')
cdata.set('TIFF_UINT32_T', 'uint32_t')
cdata.set('TIFF_INT64_T', 'int64_t')
cdata.set('TIFF_UINT64_T', 'uint64_t')
cdata.set('TIFF_SSIZE_T', cc.sizeof('void*') == 8 ? 'int64_t' : 'int32_t')
cdata.set('SIZEOF_SIZE_T', cc.sizeof('size_t'))

check_headers = [
  'assert.h',
  'fcntl.h',
  'GLUT/glut.h',
  'io.h',
  'GL/glut.h',
  'GL/glu.h',
  'GL/gl.h',
  'OpenGL/glu.h',
  'OpenGL/gl.h',
  'strings.h',
  'sys/types.h',
  'unistd.h',
]

foreach h : check_headers
  if cc.has_header(h)
    cdata.set('HAVE_@0@'.format(h.underscorify().to_upper()), 1)
  endif
endforeach

foreach f : ['fseeko', 'mmap', 'setmode']
  if cc.has_function(f)
    cdata.set('HAVE_@0@'.format(f.underscorify().to_upper()), 1)
  endif
endforeach

cdata.set('HAVE_JBG_NEWLEN', jbig_dep.found())
cdata.set10('HAVE_DECL_OPTARG', cc.has_header_symbol('unistd.h', 'optarg'))
cdata.set10('HAVE_GETOPT', cc.has_header_symbol('getopt.h', 'getopt'))

if jpeg_dep.found()
  if jpeg_dep.type_name() == 'internal'
    # libjpeg is coming from a sibling subproject that hasn't been built
    # yet, so we can't inspect build artifacts.  The best we can do is
    # assume it's libjpeg-turbo rather than an out-of-tree libjpeg wrap,
    # and check its version number.
    have_jpeg12 = jpeg_dep.version().version_compare('>=3')
    if have_jpeg12
      message('Found sibling libjpeg-turbo >= 3.0.0; enabling 12-bit JPEG support')
    endif
  else
    have_jpeg12 = cc.has_function(
      'jpeg12_read_scanlines',
      dependencies: jpeg_dep
    )
  endif
  if have_jpeg12
    # missing cmakedefine in tif_config.h.cmake.in
    # https://gitlab.com/libtiff/libtiff/-/merge_requests/664
    add_project_arguments('-DHAVE_JPEGTURBO_DUAL_MODE_8_12', language : 'c')
  endif
endif

cdata.set('PACKAGE_BUGREPORT', 'tiff@lists.osgeo.org')
cdata.set('PACKAGE_NAME', 'LibTIFF Software')
cdata.set('PACKAGE_TARNAME', meson.project_name())
cdata.set('PACKAGE_URL', 'https://gitlab.com/libtiff/libtiff')

cdata.set('LIBTIFF_VERSION', meson.project_version())
cdata.set('LIBTIFF_MAJOR_VERSION', meson.project_version().split('.')[0])
cdata.set('LIBTIFF_MINOR_VERSION', meson.project_version().split('.')[1])
cdata.set('LIBTIFF_MICRO_VERSION', meson.project_version().split('.')[2])
cdata.set('LIBTIFF_RELEASE_DATE', import('fs').read('RELEASE-DATE').strip())

cdata.set('CCITT_SUPPORT', true)
cdata.set('PACKBITS_SUPPORT', true)
cdata.set('LZW_SUPPORT', true)
cdata.set('THUNDER_SUPPORT', true)
cdata.set('NEXT_SUPPORT', true)
cdata.set('LOGLUV_SUPPORT', true)
cdata.set10('MDI_SUPPORT', true)
cdata.set10('SUBIFD_SUPPORT', true)
cdata.set('CXX_SUPPORT', false)
cdata.set('CHUNKY_STRIP_READ_SUPPORT', false)

cdata.set('LIBJPEG_12_PATH', '')
cdata.set('STRIPCHOP_DEFAULT', 'TIFF_STRIPCHOP')
cdata.set('DEFAULT_EXTRASAMPLE_AS_ALPHA', true)
cdata.set('HAVE_IEEEFP', true)
cdata.set('STRIP_SIZE_DEFAULT', 8192)

cdata.set('JBIG_SUPPORT', jbig_dep.found())
cdata.set('JPEG_SUPPORT', jpeg_dep.found())
cdata.set('LERC_SUPPORT', lerc_dep.found())
cdata.set('LZMA_SUPPORT', lzma_dep.found())
cdata.set('WEBP_SUPPORT', webp_dep.found())
cdata.set('ZSTD_SUPPORT', zstd_dep.found())
cdata.set('ZIP_SUPPORT', zlib_dep.found())
cdata.set('PIXARLOG_SUPPORT', zlib_dep.found())

cdata.set('CHECK_JPEG_YCBCR_SUBSAMPLING', true)
cdata.set('TIFF_MAX_DIR_COUNT', 1048576)

# example variable in tiffconf.h.cmake.in comment
cdata.set('VAR', 'VAR')

subdir('libtiff')

libtiff4_dep = declare_dependency(
  include_directories: 'libtiff',
  link_with: tiff4_lib,
)

import('pkgconfig').generate(
  tiff4_lib,
  filebase: 'libtiff-4',
  name: 'libtiff',
  description: 'Tag Image File Format (TIFF) library.',
)

subdir('test')
