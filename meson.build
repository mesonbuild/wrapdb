project('libtiff4', 'c')

cdata = configuration_data()
cc = meson.get_compiler('c')
is_64 = cc.sizeof('void*') == 8

if cc.get_id() == 'msvc'
  cdata.set('TIFF_INT8_T', '__int8')
  cdata.set('TIFF_UINT8_T', 'unsigned __int8')
  cdata.set('TIFF_INT16_T', '__int16')
  cdata.set('TIFF_UINT16_T', 'unsigned __int16')
  cdata.set('TIFF_INT32_T', '__int32')
  cdata.set('TIFF_UINT32_T', 'unsigned __int32')
  cdata.set('TIFF_INT64_T', '__int64')
  cdata.set('TIFF_UINT64_T', 'unsigned __int64')
  cdata.set('TIFF_UINT64_FORMAT', '"%U64d"')
  if is_64
    cdata.set('TIFF_SSIZE_T', '__int64')
    cdata.set('TIFF_SSIZE_FORMAT', '"%I64d"')
  else
    cdata.set('TIFF_SSIZE_T', '__int32')
    cdata.set('TIFF_SSIZE_FORMAT', '"%d"')
  endif
else
  cdata.set('TIFF_INT8_T', 'char')
  cdata.set('TIFF_UINT8_T', 'unsigned char')
  cdata.set('TIFF_INT16_T', 'short')
  cdata.set('TIFF_UINT16_T', 'unsigned short')
  cdata.set('TIFF_INT32_T', 'int')
  cdata.set('TIFF_UINT32_T', 'unsigned int')
  cdata.set('TIFF_INT64_T', 'long')
  cdata.set('TIFF_UINT64_T', 'unsigned long')
  cdata.set('TIFF_UINT64_FORMAT', '"%uld"')
  if is_64
    cdata.set('TIFF_SSIZE_T', 'long')
    cdata.set('TIFF_SSIZE_FORMAT', '"%ld"')
  else
    cdata.set('TIFF_SSIZE_T', 'int')
    cdata.set('TIFF_SSIZE_FORMAT', '"%d"')
  endif
endif

check_headers = [
  ['HAVE_ASSERT_H', 'assert.h'],
  ['HAVE_DLFCN_H', 'dlfcn.h'],
  ['HAVE_FCNTL_H', 'fcntl.h'],
  ['HAVE_GLUT_GLUT_H', 'glut/glut.h'],
  ['HAVE_GL_GLUT_H', 'gl/glut.h'],
  ['HAVE_GL_GLU_H', 'gl/glu.h'],
  ['HAVE_GL_GL_H', 'gl/gl.h'],
  ['HAVE_INTTYPES_H', 'inttypes.h'],
  ['HAVE_IO_H', 'io.h'],
  ['HAVE_MEMORY_H', 'memory.h'],
  ['HAVE_OPENGL_GLU_H', 'opengl/glu.h'],
  ['HAVE_OPENGL_GL_H', 'opengl/gl.h'],
  ['HAVE_SEARCH_H', 'search.h'],
  ['HAVE_STDINT_H', 'stdint.h'],
  ['HAVE_STDLIB_H', 'stdlib.h'],
  ['HAVE_STRINGS_H', 'strings.h'],
  ['HAVE_STRING_H', 'string.h'],
  ['HAVE_SYS_STAT_H', 'sys/stat.h'],
  ['HAVE_SYS_TYPES_H', 'sys/types.h'],
  ['HAVE_UNISTD_H', 'unistd.h'],
  ['HAVE_WINDOWS_H', 'windows.h'],
]

foreach h : check_headers
  if cc.has_header(h.get(1))
    cdata.set(h.get(0), 1)
  endif
endforeach

check_functions = [
# check token ['HAVE_DECL_OPTARG']
  ['HAVE_FSEEKO', 'fseeko', '#include<stdio.h>'],
# check token ['HAVE_GETOPT']
# check token ['HAVE_IEEEFP']
# check token ['HAVE_JBG_NEWLEN']
# check token ['HAVE_LFIND']
  ['HAVE_MMAP', 'mmap', '#include<sys/mman.h>'],
# check token ['HAVE_PTHREAD']
# check token ['HAVE_SETMODE']
  ['HAVE_SNPRINTF', 'snprintf', '#include<stdio.h>'],
  ['HAVE_STRCASECMP', 'strcasecmp', '#include<strings.h>'],
  ['HAVE_STRTOL', 'strtol', '#include<stdlib.h>'],
  ['HAVE_STRTOLL', 'strtoll', '#include<stdlib.h>'],
  ['HAVE_STRTOUL', 'strtoul', '#include<stdlib.h>'],
  ['HAVE_STRTOULL', 'strtoull', '#include<stdlib.h>'],
# check token ['HAVE_VARARGS_GLU_TESSCB']
]

foreach f : check_functions
  if cc.has_function(f.get(1), prefix : f.get(2))
    cdata.set(f.get(0), 1)
  endif
endforeach

cdata.set('SIZEOF_SIGNED_INT', cc.sizeof('signed int'))
cdata.set('SIZEOF_SIGNED_LONG', cc.sizeof('signed long'))
cdata.set('SIZEOF_SIGNED_LONG_LONG', cc.sizeof('signed long long'))
cdata.set('SIZEOF_SIZE_T', cc.sizeof('size_t'))
cdata.set('SIZEOF_UNSIGNED_CHAR_P', cc.sizeof('unsigned char*'))
cdata.set('SIZEOF_UNSIGNED_INT', cc.sizeof('unsigned int'))
cdata.set('SIZEOF_UNSIGNED_LONG', cc.sizeof('unsigned long'))
cdata.set('SIZEOF_UNSIGNED_LONG_LONG', cc.sizeof('unsigned long long'))

cdata.set('HOST_FILLORDER', 'FILLORDER_LSB2MSB')
cdata.set('HAVE_IEEEFP', 1)
cdata.set('LZW_SUPPORT', 1)

subdir('libtiff')

libtiff4_dep = declare_dependency(include_directories: 'libtiff',
  link_with: tiff4_lib)

