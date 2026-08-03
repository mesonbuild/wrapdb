
asm_src = []
fips_asm_src = []
test_asm_src = []

if host_machine.system() == 'linux' and host_machine.cpu_family() == 'x86_64'
  asm_src += files(
    'linux-x86_64/crypto/chacha/chacha-x86_64.S',
    'linux-x86_64/crypto/cipher_extra/aes128gcmsiv-x86_64.S',
    'linux-x86_64/crypto/cipher_extra/aesni-sha1-x86_64.S',
    'linux-x86_64/crypto/cipher_extra/aesni-sha256-x86_64.S',
    'linux-x86_64/crypto/cipher_extra/chacha20_poly1305_x86_64.S',
  )

  fips_asm_src += files(
    'linux-x86_64/crypto/fipsmodule/aesni-gcm-avx512.S',
    'linux-x86_64/crypto/fipsmodule/aesni-gcm-x86_64.S',
    'linux-x86_64/crypto/fipsmodule/aesni-x86_64.S',
    'linux-x86_64/crypto/fipsmodule/aesni-xts-avx512.S',
    'linux-x86_64/crypto/fipsmodule/ghash-ssse3-x86_64.S',
    'linux-x86_64/crypto/fipsmodule/ghash-x86_64.S',
    'linux-x86_64/crypto/fipsmodule/md5-x86_64.S',
    'linux-x86_64/crypto/fipsmodule/p256-x86_64-asm.S',
    'linux-x86_64/crypto/fipsmodule/p256_beeu-x86_64-asm.S',
    'linux-x86_64/crypto/fipsmodule/rdrand-x86_64.S',
    'linux-x86_64/crypto/fipsmodule/rsaz-2k-avx512.S',
    'linux-x86_64/crypto/fipsmodule/rsaz-3k-avx512.S',
    'linux-x86_64/crypto/fipsmodule/rsaz-4k-avx512.S',
    'linux-x86_64/crypto/fipsmodule/rsaz-avx2.S',
    'linux-x86_64/crypto/fipsmodule/sha1-x86_64.S',
    'linux-x86_64/crypto/fipsmodule/sha256-x86_64.S',
    'linux-x86_64/crypto/fipsmodule/sha512-x86_64.S',
    'linux-x86_64/crypto/fipsmodule/vpaes-x86_64.S',
    'linux-x86_64/crypto/fipsmodule/x86_64-mont.S',
    'linux-x86_64/crypto/fipsmodule/x86_64-mont5.S',
  )

  test_asm_src += files(
    'linux-x86_64/crypto/test/trampoline-x86_64.S',
  )
elif host_machine.system() == 'linux' and host_machine.cpu_family() == 'x86'
  asm_src += files(
    'linux-x86/crypto/chacha/chacha-x86.S',
  )

  fips_asm_src += files(
    'linux-x86/crypto/fipsmodule/aesni-x86.S',
    'linux-x86/crypto/fipsmodule/bn-586.S',
    'linux-x86/crypto/fipsmodule/co-586.S',
    'linux-x86/crypto/fipsmodule/ghash-ssse3-x86.S',
    'linux-x86/crypto/fipsmodule/ghash-x86.S',
    'linux-x86/crypto/fipsmodule/md5-586.S',
    'linux-x86/crypto/fipsmodule/sha1-586.S',
    'linux-x86/crypto/fipsmodule/sha256-586.S',
    'linux-x86/crypto/fipsmodule/sha512-586.S',
    'linux-x86/crypto/fipsmodule/vpaes-x86.S',
    'linux-x86/crypto/fipsmodule/x86-mont.S',
  )

  test_asm_src += files(
    'linux-x86/crypto/test/trampoline-x86.S',
  )
elif host_machine.system() == 'linux' and host_machine.cpu_family() == 'aarch64'
  asm_src += files(
    'linux-aarch64/crypto/chacha/chacha-armv8.S',
    'linux-aarch64/crypto/cipher_extra/chacha20_poly1305_armv8.S',
  )

  fips_asm_src += files(
    'linux-aarch64/crypto/fipsmodule/aesv8-armx.S',
    'linux-aarch64/crypto/fipsmodule/aesv8-gcm-armv8-unroll8.S',
    'linux-aarch64/crypto/fipsmodule/aesv8-gcm-armv8.S',
    'linux-aarch64/crypto/fipsmodule/armv8-mont.S',
    'linux-aarch64/crypto/fipsmodule/bn-armv8.S',
    'linux-aarch64/crypto/fipsmodule/ghash-neon-armv8.S',
    'linux-aarch64/crypto/fipsmodule/ghashv8-armx.S',
    'linux-aarch64/crypto/fipsmodule/keccak1600-armv8.S',
    'linux-aarch64/crypto/fipsmodule/md5-armv8.S',
    'linux-aarch64/crypto/fipsmodule/p256-armv8-asm.S',
    'linux-aarch64/crypto/fipsmodule/p256_beeu-armv8-asm.S',
    'linux-aarch64/crypto/fipsmodule/rndr-armv8.S',
    'linux-aarch64/crypto/fipsmodule/sha1-armv8.S',
    'linux-aarch64/crypto/fipsmodule/sha256-armv8.S',
    'linux-aarch64/crypto/fipsmodule/sha512-armv8.S',
    'linux-aarch64/crypto/fipsmodule/vpaes-armv8.S',
  )

  test_asm_src += files(
    'linux-aarch64/crypto/test/trampoline-armv8.S',
  )
elif host_machine.system() == 'linux' and host_machine.cpu() == 'ppc64le'
  fips_asm_src += files(
    'linux-ppc64le/crypto/fipsmodule/aesp8-ppc.S',
    'linux-ppc64le/crypto/fipsmodule/ghashp8-ppc.S',
  )

  test_asm_src += files(
    'linux-ppc64le/crypto/test/trampoline-ppc.S',
  )
elif host_machine.system() == 'linux' and host_machine.cpu_family() == 'arm'
  asm_src += files(
    'linux-arm/crypto/chacha/chacha-armv4.S',
  )

  fips_asm_src += files(
    'linux-arm/crypto/fipsmodule/aesv8-armx.S',
    'linux-arm/crypto/fipsmodule/armv4-mont.S',
    'linux-arm/crypto/fipsmodule/bsaes-armv7.S',
    'linux-arm/crypto/fipsmodule/ghash-armv4.S',
    'linux-arm/crypto/fipsmodule/ghashv8-armx.S',
    'linux-arm/crypto/fipsmodule/sha1-armv4-large.S',
    'linux-arm/crypto/fipsmodule/sha256-armv4.S',
    'linux-arm/crypto/fipsmodule/sha512-armv4.S',
    'linux-arm/crypto/fipsmodule/vpaes-armv7.S',
  )

  test_asm_src += files(
    'linux-arm/crypto/test/trampoline-armv4.S',
  )
elif host_machine.system() == 'windows' and host_machine.cpu_family() == 'x86_64'
  asm_src += files(
    'win-x86_64/crypto/chacha/chacha-x86_64.asm',
    'win-x86_64/crypto/cipher_extra/aes128gcmsiv-x86_64.asm',
    'win-x86_64/crypto/cipher_extra/aesni-sha1-x86_64.asm',
    'win-x86_64/crypto/cipher_extra/aesni-sha256-x86_64.asm',
    'win-x86_64/crypto/cipher_extra/chacha20_poly1305_x86_64.asm',
  )

  fips_asm_src += files(
    'win-x86_64/crypto/fipsmodule/aesni-gcm-avx512.asm',
    'win-x86_64/crypto/fipsmodule/aesni-gcm-x86_64.asm',
    'win-x86_64/crypto/fipsmodule/aesni-x86_64.asm',
    'win-x86_64/crypto/fipsmodule/aesni-xts-avx512.asm',
    'win-x86_64/crypto/fipsmodule/ghash-ssse3-x86_64.asm',
    'win-x86_64/crypto/fipsmodule/ghash-x86_64.asm',
    'win-x86_64/crypto/fipsmodule/md5-x86_64.asm',
    'win-x86_64/crypto/fipsmodule/p256-x86_64-asm.asm',
    'win-x86_64/crypto/fipsmodule/p256_beeu-x86_64-asm.asm',
    'win-x86_64/crypto/fipsmodule/rdrand-x86_64.asm',
    'win-x86_64/crypto/fipsmodule/rsaz-2k-avx512.asm',
    'win-x86_64/crypto/fipsmodule/rsaz-3k-avx512.asm',
    'win-x86_64/crypto/fipsmodule/rsaz-4k-avx512.asm',
    'win-x86_64/crypto/fipsmodule/rsaz-avx2.asm',
    'win-x86_64/crypto/fipsmodule/sha1-x86_64.asm',
    'win-x86_64/crypto/fipsmodule/sha256-x86_64.asm',
    'win-x86_64/crypto/fipsmodule/sha512-x86_64.asm',
    'win-x86_64/crypto/fipsmodule/vpaes-x86_64.asm',
    'win-x86_64/crypto/fipsmodule/x86_64-mont.asm',
    'win-x86_64/crypto/fipsmodule/x86_64-mont5.asm',
  )

  test_asm_src += files(
    'win-x86_64/crypto/test/trampoline-x86_64.asm',
  )
elif host_machine.system() == 'windows' and host_machine.cpu_family() == 'x86'
  asm_src += files(
    'win-x86/crypto/chacha/chacha-x86.asm',
  )

  fips_asm_src += files(
    'win-x86/crypto/fipsmodule/aesni-x86.asm',
    'win-x86/crypto/fipsmodule/bn-586.asm',
    'win-x86/crypto/fipsmodule/co-586.asm',
    'win-x86/crypto/fipsmodule/ghash-ssse3-x86.asm',
    'win-x86/crypto/fipsmodule/ghash-x86.asm',
    'win-x86/crypto/fipsmodule/md5-586.asm',
    'win-x86/crypto/fipsmodule/sha1-586.asm',
    'win-x86/crypto/fipsmodule/sha256-586.asm',
    'win-x86/crypto/fipsmodule/sha512-586.asm',
    'win-x86/crypto/fipsmodule/vpaes-x86.asm',
    'win-x86/crypto/fipsmodule/x86-mont.asm',
  )

  test_asm_src += files(
    'win-x86/crypto/test/trampoline-x86.asm',
  )
elif host_machine.system() == 'windows' and host_machine.cpu_family() == 'aarch64'
  asm_src += files(
    'win-aarch64/crypto/chacha/chacha-armv8.S',
    'win-aarch64/crypto/cipher_extra/chacha20_poly1305_armv8.S',
  )

  fips_asm_src += files(
    'win-aarch64/crypto/fipsmodule/aesv8-armx.S',
    'win-aarch64/crypto/fipsmodule/aesv8-gcm-armv8-unroll8.S',
    'win-aarch64/crypto/fipsmodule/aesv8-gcm-armv8.S',
    'win-aarch64/crypto/fipsmodule/armv8-mont.S',
    'win-aarch64/crypto/fipsmodule/bn-armv8.S',
    'win-aarch64/crypto/fipsmodule/ghash-neon-armv8.S',
    'win-aarch64/crypto/fipsmodule/ghashv8-armx.S',
    'win-aarch64/crypto/fipsmodule/keccak1600-armv8.S',
    'win-aarch64/crypto/fipsmodule/md5-armv8.S',
    'win-aarch64/crypto/fipsmodule/p256-armv8-asm.S',
    'win-aarch64/crypto/fipsmodule/p256_beeu-armv8-asm.S',
    'win-aarch64/crypto/fipsmodule/rndr-armv8.S',
    'win-aarch64/crypto/fipsmodule/sha1-armv8.S',
    'win-aarch64/crypto/fipsmodule/sha256-armv8.S',
    'win-aarch64/crypto/fipsmodule/sha512-armv8.S',
    'win-aarch64/crypto/fipsmodule/vpaes-armv8.S',
  )

  test_asm_src += files(
    'win-aarch64/crypto/test/trampoline-armv8.S',
  )
elif host_machine.system() == 'darwin' and host_machine.cpu_family() == 'x86_64'
  asm_src += files(
    'mac-x86_64/crypto/chacha/chacha-x86_64.S',
    'mac-x86_64/crypto/cipher_extra/aes128gcmsiv-x86_64.S',
    'mac-x86_64/crypto/cipher_extra/aesni-sha1-x86_64.S',
    'mac-x86_64/crypto/cipher_extra/aesni-sha256-x86_64.S',
    'mac-x86_64/crypto/cipher_extra/chacha20_poly1305_x86_64.S',
  )

  fips_asm_src += files(
    'mac-x86_64/crypto/fipsmodule/aesni-gcm-avx512.S',
    'mac-x86_64/crypto/fipsmodule/aesni-gcm-x86_64.S',
    'mac-x86_64/crypto/fipsmodule/aesni-x86_64.S',
    'mac-x86_64/crypto/fipsmodule/aesni-xts-avx512.S',
    'mac-x86_64/crypto/fipsmodule/ghash-ssse3-x86_64.S',
    'mac-x86_64/crypto/fipsmodule/ghash-x86_64.S',
    'mac-x86_64/crypto/fipsmodule/md5-x86_64.S',
    'mac-x86_64/crypto/fipsmodule/p256-x86_64-asm.S',
    'mac-x86_64/crypto/fipsmodule/p256_beeu-x86_64-asm.S',
    'mac-x86_64/crypto/fipsmodule/rdrand-x86_64.S',
    'mac-x86_64/crypto/fipsmodule/rsaz-2k-avx512.S',
    'mac-x86_64/crypto/fipsmodule/rsaz-3k-avx512.S',
    'mac-x86_64/crypto/fipsmodule/rsaz-4k-avx512.S',
    'mac-x86_64/crypto/fipsmodule/rsaz-avx2.S',
    'mac-x86_64/crypto/fipsmodule/sha1-x86_64.S',
    'mac-x86_64/crypto/fipsmodule/sha256-x86_64.S',
    'mac-x86_64/crypto/fipsmodule/sha512-x86_64.S',
    'mac-x86_64/crypto/fipsmodule/vpaes-x86_64.S',
    'mac-x86_64/crypto/fipsmodule/x86_64-mont.S',
    'mac-x86_64/crypto/fipsmodule/x86_64-mont5.S',
  )

  test_asm_src += files(
    'mac-x86_64/crypto/test/trampoline-x86_64.S',
  )
elif host_machine.system() == 'darwin' and host_machine.cpu_family() == 'aarch64'
  asm_src += files(
    'ios-aarch64/crypto/chacha/chacha-armv8.S',
    'ios-aarch64/crypto/cipher_extra/chacha20_poly1305_armv8.S',
  )

  fips_asm_src += files(
    'ios-aarch64/crypto/fipsmodule/aesv8-armx.S',
    'ios-aarch64/crypto/fipsmodule/aesv8-gcm-armv8-unroll8.S',
    'ios-aarch64/crypto/fipsmodule/aesv8-gcm-armv8.S',
    'ios-aarch64/crypto/fipsmodule/armv8-mont.S',
    'ios-aarch64/crypto/fipsmodule/bn-armv8.S',
    'ios-aarch64/crypto/fipsmodule/ghash-neon-armv8.S',
    'ios-aarch64/crypto/fipsmodule/ghashv8-armx.S',
    'ios-aarch64/crypto/fipsmodule/keccak1600-armv8.S',
    'ios-aarch64/crypto/fipsmodule/md5-armv8.S',
    'ios-aarch64/crypto/fipsmodule/p256-armv8-asm.S',
    'ios-aarch64/crypto/fipsmodule/p256_beeu-armv8-asm.S',
    'ios-aarch64/crypto/fipsmodule/rndr-armv8.S',
    'ios-aarch64/crypto/fipsmodule/sha1-armv8.S',
    'ios-aarch64/crypto/fipsmodule/sha256-armv8.S',
    'ios-aarch64/crypto/fipsmodule/sha512-armv8.S',
    'ios-aarch64/crypto/fipsmodule/vpaes-armv8.S',
  )

  test_asm_src += files(
    'ios-aarch64/crypto/test/trampoline-armv8.S',
  )
endif

err_data = files('err_data.c')

if gtest_dep.found()
  tar = find_program(
    'tar',
    native: true,
  )
  crypto_test_data = custom_target(
    'crypto_test_data',
    output: 'crypto_test_data.cc',
    input: 'crypto_test_data.cc.tar.bz2',
    command: [tar, 'jxf', '@INPUT@', '-O'],
    capture: true,
  )
endif
