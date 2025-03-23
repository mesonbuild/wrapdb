project(
  'jbig2dec',
  'c',
  version: '0.20',
  meson_version: '>=0.64.0',
)

cc = meson.get_compiler('c')

fs = import('fs')

progs_opt = get_option('progs')
tests_opt = get_option('tests')

lib_inc = [
  'jbig2_arith.h',
  'jbig2_arith_iaid.h',
  'jbig2_arith_int.h',
  'jbig2_generic.h',
  'jbig2_halftone.h',
  'jbig2_huffman.h',
  'jbig2_hufftab.h',
  'jbig2_image.h',
  'jbig2_image_rw.h',
  'jbig2_mmr.h',
  'jbig2_page.h',
  'jbig2_priv.h',
  'jbig2_refinement.h',
  'jbig2_segment.h',
  'jbig2_symbol_dict.h',
  'jbig2_text.h',
  'memento.h',
  'os_types.h',
  'sha1.h',
]
lib_src = [
  'jbig2.c',
  'jbig2_arith.c',
  'jbig2_arith_iaid.c',
  'jbig2_arith_int.c',
  'jbig2_generic.c',
  'jbig2_halftone.c',
  'jbig2_huffman.c',
  'jbig2_hufftab.c',
  'jbig2_image.c',
  'jbig2_image_pbm.c',
  'jbig2_mmr.c',
  'jbig2_page.c',
  'jbig2_refinement.c',
  'jbig2_segment.c',
  'jbig2_symbol_dict.c',
  'jbig2_text.c',
]
progs_src = ['jbig2dec.c', 'sha1.c']
tests_src = []

m_dep = cc.find_library(
  'm',
  required: false,
)

png_dep = dependency(
  'libpng',
  required: progs_opt.disabled() ? progs_opt : false,
)
if png_dep.found()
  progs_src += 'jbig2_image_png.c'
endif

add_project_arguments(
  '-DHAVE_CONFIG_H',
  language: 'c',
)

cdata = configuration_data()
cdata.set('HAVE_LIBPNG', png_dep.found())
cdata.set('WORDS_BIGENDIAN', host_machine.endian() == 'big' ? 1 : false)

foreach _header : ['stdint.h', 'string.h']
  cdata.set(
    'HAVE_' + _header.underscorify().to_upper(),
    cc.has_header(_header) ? 1 : false,
  )
endforeach

if (progs_opt.allowed()
and cc.has_function(
  'getopt_long',
  prefix: '#include<getopt.h>',
)
)
  cdata.set('HAVE_GETOPT_H', 1)
else
  progs_src += ['getopt.c', 'getopt.h', 'getopt1.c']
endif

# Optional replacement for int…_t / uint…_t types.
cdata.set('JBIG2_STDINT_H', '')
cdata.set('JBIG2_INT8_T'  , '')
cdata.set('JBIG2_INT16_T' , '')
cdata.set('JBIG2_INT32_T' , '')
if cdata.get('HAVE_STDINT_H').to_string() != '1'
  sizeof_types = {}
  foreach _type : ['char', 'short', 'int', 'long']
    sizeof_types += {
      _type: cc.sizeof(_type),
    }
  endforeach
  foreach _spec : [
    ['int8' , 1, 'char'],
    ['int16', 2, 'short char int'],
    ['int32', 4, 'int long short'],
  ]
    _name = _spec[0]
    _size = _spec[1]
    _typelist = _spec[2]
    _type = ''
    foreach _candidate : _typelist.split()
      if _size == sizeof_types[_candidate]
        _type = _candidate
        break
      endif
    endforeach
    if _type == ''
      error(
        'could not find a suitable replacement type for @0@_t / u@0@_t'.format(
          _name,
        ),
      )
    endif
    message('using @0@ for @1@_t / u@1@_t'.format(_type, _name))
    cdata.set('JBIG2_@0@_T'.format(_name.to_upper()), _type)
  endforeach
endif

subdir('include')
subdir('src')
