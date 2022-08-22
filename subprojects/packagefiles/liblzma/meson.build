# liblzma is what upstream uses for their pkg-config name
project('liblzma', 'c', version : '5.2.6', license : 'pd/lgpl2/gpl2/gpl3')

cc = meson.get_compiler('c')
cdata = configuration_data()

check_headers = [
  'byteswap.h',
  'CommonCrypto/CommonDigest.h',
  'dlfcn.h',
  'fcntlh',
  'getopt.h',
  'inttypes.h',
  'limits.h',
  'memory.h',
  'minix/sha2.h',
  'sha256.h',
  'sha2.h',
  'stdint.h',
  'stdlib.h',
  'strings.h',
  'sys/byteorder.h',
  'sys/endian.h',
  'sys/param.h',
  'sys/stat.h',
  'sys/time.h',
  'sys/types.h',
  'unistd.h',
]

check_coders = [
  'decoder_arm',
  'decoder_armthumb',
  'decoder_delta',
  'decoder_ia64',
  'decoder_lzma1',
  'decoder_lzma2',
  'decoder_powerpc',
  'decoder_x86',
  'encoder_arm',
  'encoder_armthumb',
  'encoder_delta',
  'encoder_ia64',
  'encoder_lzma1',
  'encoder_lzma2',
  'encoder_powerpc',
  'encoder_x86',
]

if (get_option('decoder_arm') or get_option('decoder_armthumb') or
  get_option('decoder_delta') or get_option('decoder_ia64') or
  get_option('decoder_lzma1') or get_option('decoder_lzma2') or
  get_option('decoder_powerpc') or get_option('decoder_x86'))
  cdata.set('HAVE_DECODERS', true)
endif

if (get_option('encoder_arm') or get_option('encoder_armthumb') or
  get_option('encoder_delta') or get_option('encoder_ia64') or
  get_option('encoder_lzma1') or get_option('encoder_lzma2') or
  get_option('encoder_powerpc') or get_option('encoder_x86'))
  cdata.set('HAVE_ENCODERS', true)
endif

foreach i : check_headers
  cdata.set('HAVE_@0@'.format(i.underscorify().to_upper()), cc.has_header(i))
endforeach

foreach i : check_coders
  cdata.set('HAVE_@0@'.format(i.underscorify().to_upper()), get_option(i))
endforeach

cdata.set('HAVE_IMMINTRIN_H', cc.check_header('immintrin.h'))
cdata.set10('HAVE__BOOL', cc.has_type('_Bool'))

cdata.set('PACKAGE_NAME', '"liblzma"')
cdata.set('PACKAGE_URL', '"http://tukaani.org/xz/"')
cdata.set('PACKAGE_BUGREPORT', '"x@x"')

cdata.set('ASSUME_RAM', 128)
cdata.set('HAVE_CHECK_CRC32', true)
cdata.set('HAVE_CHECK_CRC64', true)
cdata.set('HAVE_CHECK_SHA256', true)

configure_file(input : 'config.h.meson',
  output : 'config.h',
  configuration : cdata
)

confinc = include_directories('.')
subdir('src')
