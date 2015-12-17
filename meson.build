# liblzma is what upstream uses for their pkg-config name
project('liblzma', 'c', version : '5.2.1', license : 'pd/lgpl2/gpl2/gpl3')

cc = meson.get_compiler('c')
cdata = configuration_data()

check_headers = [['byteswap.h', 'HAVE_BYTESWAP_H'],
  ['CommonCrypto/CommonDigest.h', 'HAVE_COMMONCRYPTO_COMMONDIGEST_H'],
  ['dlfcn.h', 'HAVE_DLFCN_H'],
  ['fcntlh', 'HAVE_FCNTL_H'],
  ['getopt.h', 'HAVE_GETOPT_H'],
  ['immintrin.h', 'HAVE_IMMINTRIN_H'],
  ['inttypes.h', 'HAVE_INTTYPES_H'],
  ['limits.h', 'HAVE_LIMITS_H'],
  ['memory.h', 'HAVE_MEMORY_H'],
  ['minix/sha2.h', 'HAVE_MINIX_SHA2_H'],
  ['sha256.h', 'HAVE_SHA256_H'],
  ['sha2.h', 'HAVE_SHA_2_H'],
  ['stdint.h', 'HAVE_STDINT_H'],
  ['stdlib.h', 'HAVE_STDLIB_H'],
  ['strings.h', 'HAVE_STRINGS_H'],
  ['sys/byteorder.h', 'HAVE_SYS_BYTEORDER_H'],
  ['sys/endian.h', 'HAVE_SYS_ENDIAN_H'],
  ['sys/param.h', 'HAVE_SYS_PARAM_H'],
  ['sys/stat.h', 'HAVE_SYS_STAT_H'],
  ['sys/time.h', 'HAVE_SYS_TIME_H'],
  ['sys/types.h', 'HAVE_SYS_TYPES_H'],
  ['unistd.h', 'HAVE_UNISTD_H'],
]

check_coders = [['decoder_arm', 'HAVE_DECODER_ARM'],
  ['decoder_armthumb', 'HAVE_DECODER_ARMTHUMB'],
  ['decoder_delta', 'HAVE_DECODER_DELTA'],
  ['decoder_ia64', 'HAVE_DECODER_IA64'],
  ['decoder_lzma1', 'HAVE_DECODER_LZMA1'],
  ['decoder_lzma2', 'HAVE_DECODER_LZMA2'],
  ['decoder_powerpc', 'HAVE_DECODER_POWERPC'],
  ['decoder_x86', 'HAVE_DECODER_X86'],
  ['encoder_arm', 'HAVE_ENCODER_ARM'],
  ['encoder_armthumb', 'HAVE_ENCODER_ARMTHUMB'],
  ['encoder_delta', 'HAVE_ENCODER_DELTA'],
  ['encoder_ia64', 'HAVE_ENCODER_IA64'],
  ['encoder_lzma1', 'HAVE_ENCODER_LZMA1'],
  ['encoder_lzma2', 'HAVE_ENCODER_LZMA2'],
  ['encoder_powerpc', 'HAVE_ENCODER_POWERPC'],
  ['encoder_x86', 'HAVE_ENCODER_X86']
]

foreach i : check_headers
  if cc.has_header(i.get(0))
    cdata.set(i.get(1), 1)
  endif
endforeach

foreach i : check_coders
  if get_option(i.get(0))
    cdata.set(i.get(1), 1)
  endif
endforeach

if cc.has_type('_Bool')
  cdata.set('HAVE__BOOL', 1)
endif

cdata.set('PACKAGE_NAME', '"liblzma"')
cdata.set('PACKAGE_URL', '"http://tukaani.org/xz/"')
cdata.set('PACKAGE_BUGREPORT', '"x@x"')

cdata.set('ASSUME_RAM', 128)
cdata.set('HAVE_CHECK_CRC32', 1)
cdata.set('HAVE_CHECK_CRC64', 1)
cdata.set('HAVE_CHECK_SHA256', 1)

configure_file(input : 'config.h.meson',
  output : 'config.h',
  configuration : cdata
)

confinc = include_directories('.')
subdir('src')

