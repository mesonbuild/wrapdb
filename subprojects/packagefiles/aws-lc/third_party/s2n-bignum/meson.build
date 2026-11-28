# For now use the bundled s2n-bignum until they create a versioned release so it
# can be imported into wrapdb.
# see https://github.com/mesonbuild/wrapdb/pull/2486 and https://github.com/awslabs/s2n-bignum/issues/313
s2n_bignum_root = meson.current_source_dir() / 's2n-bignum-imported'

s2n_bignum_inc = include_directories(
  's2n-bignum-imported/include',
)

arm_aes_xts = files(
  's2n-bignum-to-be-imported/arm/aes/aes-xts-dec.S',
  's2n-bignum-to-be-imported/arm/aes/aes-xts-enc.S',
)

bignum_asm_src = []

if cc.get_id() != 'msvc'
  if host_machine.cpu_family() == 'x86_64'
    bignum_asm_dir = s2n_bignum_root / 'x86_att'

    bignum_asm_src += files(
      bignum_asm_dir / 'p384/bignum_tomont_p384_alt.S',
      bignum_asm_dir / 'p384/bignum_deamont_p384_alt.S',
      bignum_asm_dir / 'curve25519/curve25519_x25519.S',
      bignum_asm_dir / 'curve25519/curve25519_x25519_alt.S',
      bignum_asm_dir / 'curve25519/curve25519_x25519base.S',
      bignum_asm_dir / 'curve25519/curve25519_x25519base_alt.S',
      bignum_asm_dir / 'sha3/sha3_keccak_f1600.S',
    )
  elif host_machine.cpu_family() == 'aarch64'
    bignum_asm_dir = s2n_bignum_root / 'arm'

    bignum_asm_src += files(
      bignum_asm_dir / 'curve25519/curve25519_x25519_byte.S',
      bignum_asm_dir / 'curve25519/curve25519_x25519_byte_alt.S',
      bignum_asm_dir / 'curve25519/curve25519_x25519base_byte.S',
      bignum_asm_dir / 'curve25519/curve25519_x25519base_byte_alt.S',
      bignum_asm_dir / 'fastmul/bignum_kmul_16_32.S',
      bignum_asm_dir / 'fastmul/bignum_kmul_32_64.S',
      bignum_asm_dir / 'fastmul/bignum_ksqr_16_32.S',
      bignum_asm_dir / 'fastmul/bignum_ksqr_32_64.S',
      bignum_asm_dir / 'fastmul/bignum_emontredc_8n.S',
      bignum_asm_dir / 'generic/bignum_ge.S',
      bignum_asm_dir / 'generic/bignum_mul.S',
      bignum_asm_dir / 'generic/bignum_optsub.S',
      bignum_asm_dir / 'generic/bignum_sqr.S',
      bignum_asm_dir / 'generic/bignum_copy_row_from_table.S',
      bignum_asm_dir / 'generic/bignum_copy_row_from_table_8n.S',
      bignum_asm_dir / 'generic/bignum_copy_row_from_table_16.S',
      bignum_asm_dir / 'generic/bignum_copy_row_from_table_32.S',
      bignum_asm_dir / 'sha3/sha3_keccak_f1600.S',
      bignum_asm_dir / 'sha3/sha3_keccak4_f1600_alt.S',
    )
  endif

  if host_machine.cpu_family() in ['x86_64', 'aarch64']
    bignum_asm_src += files(
      bignum_asm_dir / 'p256/p256_montjscalarmul.S',
      bignum_asm_dir / 'p256/p256_montjscalarmul_alt.S',
      bignum_asm_dir / 'p256/bignum_montinv_p256.S',
      bignum_asm_dir / 'p384/bignum_add_p384.S',
      bignum_asm_dir / 'p384/bignum_sub_p384.S',
      bignum_asm_dir / 'p384/bignum_neg_p384.S',
      bignum_asm_dir / 'p384/bignum_tomont_p384.S',
      bignum_asm_dir / 'p384/bignum_deamont_p384.S',
      bignum_asm_dir / 'p384/bignum_montmul_p384.S',
      bignum_asm_dir / 'p384/bignum_montmul_p384_alt.S',
      bignum_asm_dir / 'p384/bignum_montsqr_p384.S',
      bignum_asm_dir / 'p384/bignum_montsqr_p384_alt.S',
      bignum_asm_dir / 'p384/bignum_nonzero_6.S',
      bignum_asm_dir / 'p384/bignum_littleendian_6.S',
      bignum_asm_dir / 'p384/p384_montjdouble.S',
      bignum_asm_dir / 'p384/p384_montjdouble_alt.S',
      bignum_asm_dir / 'p384/p384_montjscalarmul.S',
      bignum_asm_dir / 'p384/p384_montjscalarmul_alt.S',
      bignum_asm_dir / 'p384/bignum_montinv_p384.S',
      bignum_asm_dir / 'p521/bignum_add_p521.S',
      bignum_asm_dir / 'p521/bignum_sub_p521.S',
      bignum_asm_dir / 'p521/bignum_neg_p521.S',
      bignum_asm_dir / 'p521/bignum_mul_p521.S',
      bignum_asm_dir / 'p521/bignum_mul_p521_alt.S',
      bignum_asm_dir / 'p521/bignum_sqr_p521.S',
      bignum_asm_dir / 'p521/bignum_sqr_p521_alt.S',
      bignum_asm_dir / 'p521/bignum_tolebytes_p521.S',
      bignum_asm_dir / 'p521/bignum_fromlebytes_p521.S',
      bignum_asm_dir / 'p521/p521_jdouble.S',
      bignum_asm_dir / 'p521/p521_jdouble_alt.S',
      bignum_asm_dir / 'p521/p521_jscalarmul.S',
      bignum_asm_dir / 'p521/p521_jscalarmul_alt.S',
      bignum_asm_dir / 'p521/bignum_inv_p521.S',
      bignum_asm_dir / 'curve25519/bignum_mod_n25519.S',
      bignum_asm_dir / 'curve25519/bignum_neg_p25519.S',
      bignum_asm_dir / 'curve25519/bignum_madd_n25519.S',
      bignum_asm_dir / 'curve25519/bignum_madd_n25519_alt.S',
      bignum_asm_dir / 'curve25519/edwards25519_decode.S',
      bignum_asm_dir / 'curve25519/edwards25519_decode_alt.S',
      bignum_asm_dir / 'curve25519/edwards25519_encode.S',
      bignum_asm_dir / 'curve25519/edwards25519_scalarmulbase.S',
      bignum_asm_dir / 'curve25519/edwards25519_scalarmulbase_alt.S',
      bignum_asm_dir / 'curve25519/edwards25519_scalarmuldouble.S',
      bignum_asm_dir / 'curve25519/edwards25519_scalarmuldouble_alt.S',
    )

    unset_variable('bignum_asm_dir')
  endif
endif
