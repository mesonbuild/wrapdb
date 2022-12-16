project(
  'tiff',
  'c',
  version: files('VERSION'),
  meson_version: '>=0.57.0',
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

cdata.set('HOST_FILLORDER', host_machine.endian() == 'big' ? 'FILLORDER_LSB2MSB' : 'FILLORDER_LSB2MSB')
cdata.set10('HOST_BIG_ENDIAN', host_machine.endian() == 'big')

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

cdata.set('PACKAGE_BUGREPORT', 'tiff@lists.maptools.org')
cdata.set('PACKAGE_NAME', 'LibTIFF Software')
cdata.set('PACKAGE_STRING', '@0@ @1@'.format(cdata.get('PACKAGE_NAME'), meson.project_version()))
cdata.set('PACKAGE_TARNAME', meson.project_name())
cdata.set('PACKAGE_URL', 'https://gitlab.com/libtiff/libtiff')
cdata.set('PACKAGE_VERSION', meson.project_version())

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

subdir('libtiff')

libtiff4_dep = declare_dependency(
  include_directories: 'libtiff',
  link_with: tiff4_lib,
)

subdir('test')
