project(
  'libaegis',
  'c',
  version: '0.4.0',
  license: 'MIT',
)

libaegis_sources = files(
  'src/aegis128l/aegis128l.c',
  'src/aegis128l/aegis128l_aesni.c',
  'src/aegis128l/aegis128l_altivec.c',
  'src/aegis128l/aegis128l_armcrypto.c',
  'src/aegis128l/aegis128l_soft.c',
  'src/aegis128x2/aegis128x2.c',
  'src/aegis128x2/aegis128x2_aesni.c',
  'src/aegis128x2/aegis128x2_altivec.c',
  'src/aegis128x2/aegis128x2_armcrypto.c',
  'src/aegis128x2/aegis128x2_avx2.c',
  'src/aegis128x2/aegis128x2_soft.c',
  'src/aegis128x4/aegis128x4.c',
  'src/aegis128x4/aegis128x4_aesni.c',
  'src/aegis128x4/aegis128x4_altivec.c',
  'src/aegis128x4/aegis128x4_armcrypto.c',
  'src/aegis128x4/aegis128x4_armcrypto.c',
  'src/aegis128x4/aegis128x4_avx2.c',
  'src/aegis128x4/aegis128x4_avx512.c',
  'src/aegis128x4/aegis128x4_soft.c',
  'src/aegis256/aegis256.c',
  'src/aegis256/aegis256_aesni.c',
  'src/aegis256/aegis256_altivec.c',
  'src/aegis256/aegis256_armcrypto.c',
  'src/aegis256/aegis256_soft.c',
  'src/aegis256x2/aegis256x2.c',
  'src/aegis256x2/aegis256x2_aesni.c',
  'src/aegis256x2/aegis256x2_altivec.c',
  'src/aegis256x2/aegis256x2_armcrypto.c',
  'src/aegis256x2/aegis256x2_avx2.c',
  'src/aegis256x2/aegis256x2_soft.c',
  'src/aegis256x4/aegis256x4.c',
  'src/aegis256x4/aegis256x4_aesni.c',
  'src/aegis256x4/aegis256x4_altivec.c',
  'src/aegis256x4/aegis256x4_armcrypto.c',
  'src/aegis256x4/aegis256x4_avx2.c',
  'src/aegis256x4/aegis256x4_avx512.c',
  'src/aegis256x4/aegis256x4_soft.c',
  'src/common/common.c',
  'src/common/cpu.c',
  'src/common/softaes.c',
)

libaegis_headers = [include_directories('src/include')]

libaegis_lib = library(
  'aegis',
  libaegis_sources,
  include_directories: libaegis_headers,
)

libaegis_dep = declare_dependency(
  include_directories: libaegis_headers,
  link_with: libaegis_lib,
)

