# liblzma is what upstream uses for their pkg-config name
project('liblzma', 'c', version: '5.2.7', license: 'pd/lgpl2/gpl2/gpl3')

add_project_arguments('-D_GNU_SOURCE', language: 'c')

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
  'stdbool.h',
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

decoders = [
  'decoder_arm',
  'decoder_arm64',
  'decoder_armthumb',
  'decoder_delta',
  'decoder_ia64',
  'decoder_lzma1',
  'decoder_lzma2',
  'decoder_powerpc',
  'decoder_sparc',
  'decoder_x86',
]

encoders = [
  'encoder_arm',
  'encoder_arm64',
  'encoder_armthumb',
  'encoder_delta',
  'encoder_ia64',
  'encoder_lzma1',
  'encoder_lzma2',
  'encoder_powerpc',
  'encoder_sparc',
  'encoder_x86',
]

foreach d : decoders
  if get_option(d)
    cdata.set('HAVE_DECODERS', true)
    break
  endif
endforeach

foreach d : encoders
  if get_option(d)
    cdata.set('HAVE_ENCODERS', true)
    break
  endif
endforeach

foreach i : check_headers
  cdata.set('HAVE_@0@'.format(i.underscorify().to_upper()), cc.has_header(i))
endforeach

foreach i : decoders + encoders
  cdata.set('HAVE_@0@'.format(i.underscorify().to_upper()), get_option(i))
endforeach

cdata.set('HAVE_IMMINTRIN_H', cc.check_header('immintrin.h'))
cdata.set10('HAVE__BOOL', cc.has_type('_Bool'))

cdata.set_quoted('PACKAGE_NAME', 'XZ Utils')
cdata.set_quoted('PACKAGE_URL', 'https://tukaani.org/xz/')
cdata.set_quoted('PACKAGE_BUGREPORT', 'lasse.collin@tukaani.org')

cdata.set('ASSUME_RAM', 128)
cdata.set('HAVE_CHECK_CRC32', true)
cdata.set('HAVE_CHECK_CRC64', true)
cdata.set('HAVE_CHECK_SHA256', true)

configure_file(
  input: 'config.h.meson',
  output: 'config.h',
  configuration: cdata,
)

confinc = include_directories('.')
subdir('src')
