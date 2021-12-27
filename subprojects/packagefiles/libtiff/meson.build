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
  # Detect type size assuming 8-bit chars
  cdata.set('TIFF_INT8_T', 'char')
  cdata.set('TIFF_UINT8_T', 'unsigned char')

  compiler_sizeofs = {
    'short'    : [cc.sizeof('short')    ,'h' ],
    'int'      : [cc.sizeof('int')      ,''  ],
    'long'     : [cc.sizeof('long')     ,'l' ],
    'long long': [cc.sizeof('long long'),'ll'],
  }
  signed_tiff_types_sizes = {
    'TIFF_INT16' : 2,
    'TIFF_INT32' : 4,
    'TIFF_INT64' : 8,
    'TIFF_SSIZE' : cc.sizeof('void*'),
  }
  unsigned_tiff_types_sizes = {
    'TIFF_UINT16' : 2,
    'TIFF_UINT32' : 4,
    'TIFF_UINT64' : 8,
  }

  foreach tiff_type, target_size: signed_tiff_types_sizes
    foreach type_name, infos: compiler_sizeofs
      type_size   = infos[0]
      type_printf = infos[1]
      if type_size == target_size
        cdata.set(tiff_type+'_T',type_name)
        cdata.set(tiff_type+'_FORMAT', '"%'+type_printf+'d"')
        break
      endif
    endforeach
  endforeach

  foreach tiff_type, target_size: unsigned_tiff_types_sizes
    foreach type_name, infos: compiler_sizeofs
      type_size   = infos[0]
      type_printf = infos[1]
      if type_size == target_size
        cdata.set(tiff_type+'_T','unsigned '+type_name)
        cdata.set(tiff_type+'_FORMAT', '"%'+type_printf+'ud"')
        break
      endif
    endforeach
  endforeach
endif

check_headers = [
  'assert.h',
  'dlfcn.h',
  'fcntl.h',
  'glut/glut.h',
  'gl/glut.h',
  'gl/glu.h',
  'gl/gl.h',
  'inttypes.h',
  'io.h',
  'memory.h',
  'opengl/glu.h',
  'opengl/gl.h',
  'search.h',
  'stdint.h',
  'stdlib.h',
  'strings.h',
  'string.h',
  'sys/stat.h',
  'sys/types.h',
  'unistd.h',
  'windows.h',
]

foreach h : check_headers
  if cc.has_header(h)
    cdata.set('HAVE_' + h.underscorify().to_upper(), 1)
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
