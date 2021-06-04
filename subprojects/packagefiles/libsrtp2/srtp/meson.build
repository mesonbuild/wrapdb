srtp2_sources = [
  'ekt.c',
  'srtp.c',
  '../crypto/cipher/cipher.c',
  '../crypto/cipher/null_cipher.c',
  '../crypto/hash/auth.c',
  '../crypto/hash/null_auth.c',
  '../crypto/replay/rdb.c',
  '../crypto/replay/rdbx.c',
  '../crypto/replay/ut_sim.c',
  '../crypto/math/datatypes.c',
  '../crypto/math/stat.c',
  '../crypto/kernel/err.c',
  '../crypto/kernel/crypto_kernel.c',
  '../crypto/kernel/alloc.c',
  '../crypto/kernel/key.c',
]

if libcrypto_dep.found()
  srtp2_sources += [
    '../crypto/cipher/aes_icm_ossl.c',
    '../crypto/cipher/aes_gcm_ossl.c',
    '../crypto/hash/hmac_ossl.c',
  ]
else
  srtp2_sources += [
    '../crypto/cipher/aes_icm.c',
    '../crypto/cipher/aes.c',
    '../crypto/hash/hmac.c',
    '../crypto/hash/sha1.c',
  ]
endif

srtp2_include_directories = include_directories(
  '..',
  '../include',
  '../crypto/include',
)

libsrtp2_static = static_library(
  'srtp2',
  srtp2_sources,
  include_directories: srtp2_include_directories,
  dependencies: srtp2_deps,
  install: false
)

libsrtp2 = library(
  'srtp2',
  link_whole: [ libsrtp2_static ],
  version: meson.project_version(),
  vs_module_defs: '../srtp.def',
  install: true
)

libsrtp2_headers = [
  '../include/srtp.h',
  '../crypto/include/auth.h',
  '../crypto/include/cipher.h',
  '../crypto/include/crypto_types.h',
]

install_headers(libsrtp2_headers, subdir: 'srtp2')

libsrtp2_dep = declare_dependency(link_with : libsrtp2,
  include_directories : include_directories('..'),
  dependencies: srtp2_deps
)
