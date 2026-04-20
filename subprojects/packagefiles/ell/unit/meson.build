tests = [
  'test-unit',
  'test-queue',
  'test-hashmap',
  'test-endian',
  'test-string',
  'test-utf8',
  'test-main',
  'test-io',
  'test-ringbuf',
  'test-checksum',
  'test-settings',
  'test-netlink',
  'test-genl-msg',
  'test-rtnl',
  'test-siphash',
  'test-cipher',
  'test-random',
  'test-util',
  'test-uintset',
  'test-base64',
  'test-uuid',
  'test-pbkdf2',
  'test-dhcp',
  'test-dhcp6',
  'test-dir-watch',
  'test-ecc',
  'test-ecdh',
  'test-time',
  'test-path',
  'test-net',
  'test-sysctl',
  'test-minheap',
  'test-notifylist',
  'test-hwdb',
  'test-dbus',
  'test-dbus-util',
  'test-dbus-message',
  'test-dbus-message-fds',
  'test-dbus-properties',
  'test-dbus-service',
  'test-dbus-watch',
  'test-gvariant-util',
  'test-gvariant-message',
]

gen_headers = []
test_pem_cert_deps = []

if get_option('cert-tests')
  tests += ['test-pem', 'test-tls', 'test-key']

  cert_server_key_pem_tgt = custom_target(
    'cert-server-key.pem',
    output: 'cert-server-key.pem',
    command: [openssl, 'genrsa', '-out', '@OUTPUT@'],
  )

  ec_cert_server_key_pem_tgt = custom_target(
    'ec-cert-server-key.pem',
    output: 'ec-cert-server-key.pem',
    command: [
      openssl,
      'ecparam',
      '-out',
      '@OUTPUT@',
      '-name',
      'secp384r1',
      '-genkey',
    ],
  )

  cert_server_key_pkcs8_pem_tgt = custom_target(
    'cert-server-key-pkcs8.pem',
    input: cert_server_key_pem_tgt,
    output: 'cert-server-key-pkcs8.pem',
    command: [
      openssl,
      'pkcs8',
      '-topk8',
      '-nocrypt',
      '-in',
      '@INPUT@',
      '-out',
      '@OUTPUT@',
    ],
  )

  cert_server_csr_tgt = custom_target(
    'cert-server.csr',
    input: cert_server_key_pem_tgt,
    output: 'cert-server.csr',
    command: [
      openssl,
      'req',
      '-new',
      '-extensions',
      'cert_ext',
      '-config',
      files('gencerts.cnf'),
      '-subj',
      '/O=Foo Example Organization/CN=Foo Example Organization/emailAddress=foo@mail.example',
      '-key',
      '@INPUT@',
      '-out',
      '@OUTPUT@',
    ],
  )

  ec_cert_server_csr_tgt = custom_target(
    'ec-cert-server.csr',
    input: ec_cert_server_key_pem_tgt,
    output: 'ec-cert-server.csr',
    command: [
      openssl,
      'req',
      '-new',
      '-extensions',
      'cert_ext',
      '-config',
      files('gencerts.cnf'),
      '-subj',
      '/O=Foo Example Organization/CN=Foo Example Organization/emailAddress=foo@mail.example',
      '-key',
      '@INPUT@',
      '-out',
      '@OUTPUT@',
    ],
  )

  cert_ca_key_pem_tgt = custom_target(
    'cert-ca-key.pem',
    output: 'cert-ca-key.pem',
    command: [openssl, 'genrsa', '-out', '@OUTPUT@', '2048'],
  )

  cert_ca_pem_tgt = custom_target(
    'cert-ca.pem',
    input: cert_ca_key_pem_tgt,
    output: 'cert-ca.pem',
    command: [
      openssl,
      'req',
      '-x509',
      '-new',
      '-nodes',
      '-extensions',
      'ca_ext',
      '-config',
      files('gencerts.cnf'),
      '-subj',
      '/O=International Union of Example Organizations/CN=Certificate issuer guy/emailAddress=ca@mail.example',
      '-key',
      '@INPUT@',
      '-sha256',
      '-days',
      '10000',
      '-out',
      '@OUTPUT@',
    ],
  )

  cert_server_pem_tgt = custom_target(
    'cert-server.pem',
    input: [cert_server_csr_tgt, cert_ca_pem_tgt, cert_ca_key_pem_tgt],
    output: 'cert-server.pem',
    command: [
      openssl,
      'x509',
      '-req',
      '-extensions',
      'server_ext',
      '-extfile',
      files('gencerts.cnf'),
      '-in',
      '@INPUT0@',
      '-CA',
      '@INPUT1@',
      '-CAkey',
      '@INPUT2@',
      '-CAserial',
      'cert-ca.srl',
      '-CAcreateserial',
      '-sha256',
      '-days',
      '10000',
      '-out',
      '@OUTPUT@',
    ],
  )

  ec_cert_ca_key_pem_tgt = custom_target(
    'ec-cert-ca-key.pem',
    output: 'ec-cert-ca-key.pem',
    command: [
      openssl,
      'ecparam',
      '-out',
      '@OUTPUT@',
      '-name',
      'secp384r1',
      '-genkey',
    ],
  )

  ec_cert_ca_pem_tgt = custom_target(
    'ec-cert-ca.pem',
    input: ec_cert_ca_key_pem_tgt,
    output: 'ec-cert-ca.pem',
    command: [
      openssl,
      'req',
      '-x509',
      '-new',
      '-nodes',
      '-extensions',
      'ca_ext',
      '-config',
      files('gencerts.cnf'),
      '-subj',
      '/O=International Union of Example Organizations/CN=Certificate issuer guy/emailAddress=ca@mail.example',
      '-key',
      '@INPUT@',
      '-sha256',
      '-days',
      '10000',
      '-out',
      '@OUTPUT@',
    ],
  )

  ec_cert_server_pem_tgt = custom_target(
    'ec-cert-server.pem',
    input: [
      ec_cert_server_csr_tgt,
      ec_cert_ca_pem_tgt,
      ec_cert_ca_key_pem_tgt,
    ],
    output: 'ec-cert-server.pem',
    command: [
      openssl,
      'x509',
      '-req',
      '-extensions',
      'server_ext',
      '-extfile',
      files('gencerts.cnf'),
      '-in',
      '@INPUT0@',
      '-CA',
      '@INPUT1@',
      '-CAkey',
      '@INPUT2@',
      '-CAserial',
      'cert-ca.srl',
      '-CAcreateserial',
      '-sha256',
      '-days',
      '10000',
      '-out',
      '@OUTPUT@',
    ],
  )

  cert_client_key_pkcs1_pem_tgt = custom_target(
    'cert-client-key-pkcs1.pem',
    output: 'cert-client-key-pkcs1.pem',
    command: [openssl, 'genrsa', '-out', '@OUTPUT@'],
  )

  cert_client_key_pkcs8_pem_tgt = custom_target(
    'cert-client-key-pkcs8.pem',
    input: cert_client_key_pkcs1_pem_tgt,
    output: 'cert-client-key-pkcs8.pem',
    command: [
      openssl,
      'pkcs8',
      '-topk8',
      '-nocrypt',
      '-in',
      '@INPUT@',
      '-out',
      '@OUTPUT@',
    ],
  )

  cert_client_key_pkcs8_md5_des_pem_tgt = custom_target(
    'cert-client-key-pkcs8-md5-des.pem',
    input: cert_client_key_pkcs8_pem_tgt,
    output: 'cert-client-key-pkcs8-md5-des.pem',
    command: [
      openssl,
      'pkcs8',
      '-in',
      '@INPUT@',
      '-out',
      '@OUTPUT@',
      '-topk8',
      '-v1',
      'PBE-MD5-DES',
      '-passout',
      'pass:abc',
      openssl_legacy,
    ],
  )

  cert_client_key_pkcs8_v2_des_pem_tgt = custom_target(
    'cert-client-key-pkcs8-v2-des.pem',
    input: cert_client_key_pkcs8_pem_tgt,
    output: 'cert-client-key-pkcs8-v2-des.pem',
    command: [
      openssl,
      'pkcs8',
      '-in',
      '@INPUT@',
      '-out',
      '@OUTPUT@',
      '-topk8',
      '-v2',
      'des-cbc',
      '-v2prf',
      'hmacWithSHA1',
      '-passout',
      'pass:abc',
      openssl_legacy,
    ],
  )

  cert_client_key_pkcs8_v2_des_ede3_pem_tgt = custom_target(
    'cert-client-key-pkcs8-v2-des-ede3.pem',
    input: cert_client_key_pkcs8_pem_tgt,
    output: 'cert-client-key-pkcs8-v2-des-ede3.pem',
    command: [
      openssl,
      'pkcs8',
      '-in',
      '@INPUT@',
      '-out',
      '@OUTPUT@',
      '-topk8',
      '-v2',
      'des-ede3-cbc',
      '-v2prf',
      'hmacWithSHA224',
      '-passout',
      'pass:abc',
    ],
  )

  cert_client_key_pkcs8_v2_aes128_pem_tgt = custom_target(
    'cert-client-key-pkcs8-v2-aes128.pem',
    input: cert_client_key_pkcs8_pem_tgt,
    output: 'cert-client-key-pkcs8-v2-aes128.pem',
    command: [
      openssl,
      'pkcs8',
      '-in',
      '@INPUT@',
      '-out',
      '@OUTPUT@',
      '-topk8',
      '-v2',
      'aes128',
      '-v2prf',
      'hmacWithSHA256',
      '-passout',
      'pass:abc',
    ],
  )

  cert_client_key_pkcs8_sha1_des_pem_tgt = custom_target(
    'cert-client-key-pkcs8-sha1-des.pem',
    input: cert_client_key_pkcs8_pem_tgt,
    output: 'cert-client-key-pkcs8-sha1-des.pem',
    command: [
      openssl,
      'pkcs8',
      '-in',
      '@INPUT@',
      '-out',
      '@OUTPUT@',
      '-topk8',
      '-v1',
      'PBE-SHA1-DES',
      '-passout',
      'pass:abc',
      openssl_legacy,
    ],
  )

  cert_client_key_pkcs8_v2_aes256_pem_tgt = custom_target(
    'cert-client-key-pkcs8-v2-aes256.pem',
    input: cert_client_key_pkcs8_pem_tgt,
    output: 'cert-client-key-pkcs8-v2-aes256.pem',
    command: [
      openssl,
      'pkcs8',
      '-in',
      '@INPUT@',
      '-out',
      '@OUTPUT@',
      '-topk8',
      '-v2',
      'aes256',
      '-v2prf',
      'hmacWithSHA512',
      '-passout',
      'pass:abc',
    ],
  )

  cert_client_csr_tgt = custom_target(
    'cert-client.csr',
    input: cert_client_key_pkcs1_pem_tgt,
    output: 'cert-client.csr',
    command: [
      openssl,
      'req',
      '-new',
      '-extensions',
      'cert_ext',
      '-config',
      files('gencerts.cnf'),
      '-subj',
      '/O=Bar Example Organization/CN=Bar Example Organization/emailAddress=bar@mail.example',
      '-key',
      '@INPUT@',
      '-out',
      '@OUTPUT@',
    ],
  )

  cert_client_pem_tgt = custom_target(
    'cert-client.pem',
    input: [cert_client_csr_tgt, cert_ca_pem_tgt, cert_ca_key_pem_tgt],
    output: 'cert-client.pem',
    command: [
      openssl,
      'x509',
      '-req',
      '-extensions',
      'cert_ext',
      '-extfile',
      files('gencerts.cnf'),
      '-in',
      '@INPUT0@',
      '-CA',
      '@INPUT1@',
      '-CAkey',
      '@INPUT2@',
      '-CAserial',
      'cert-ca.srl',
      '-CAcreateserial',
      '-sha256',
      '-days',
      '10000',
      '-out',
      '@OUTPUT@',
    ],
  )

  cert_client_crt_tgt = custom_target(
    'cert-client.crt',
    input: cert_client_pem_tgt,
    output: 'cert-client.crt',
    command: [
      openssl,
      'x509',
      '-in',
      '@INPUT@',
      '-out',
      '@OUTPUT@',
      '-outform',
      'der',
    ],
  )

  cert_intca_key_pem_tgt = custom_target(
    'cert-intca-key.pem',
    output: 'cert-intca-key.pem',
    command: [openssl, 'genrsa', '-out', '@OUTPUT@'],
  )

  cert_intca_csr_tgt = custom_target(
    'cert-intca.csr',
    input: cert_intca_key_pem_tgt,
    output: 'cert-intca.csr',
    command: [
      openssl,
      'req',
      '-new',
      '-extensions',
      'int_ext',
      '-config',
      files('gencerts.cnf'),
      '-subj',
      '/O=International Union of Example Organizations/CN=Certificate issuer guy/emailAddress=ca@mail.example',
      '-key',
      '@INPUT@',
      '-out',
      '@OUTPUT@',
    ],
  )

  cert_intca_pem_tgt = custom_target(
    'cert-intca.pem',
    input: [cert_intca_csr_tgt, cert_ca_pem_tgt, cert_ca_key_pem_tgt],
    output: 'cert-intca.pem',
    command: [
      openssl,
      'x509',
      '-req',
      '-extensions',
      'int_ext',
      '-extfile',
      files('gencerts.cnf'),
      '-in',
      '@INPUT0@',
      '-CA',
      '@INPUT1@',
      '-CAkey',
      '@INPUT2@',
      '-CAserial',
      'cert-ca.srl',
      '-CAcreateserial',
      '-sha256',
      '-days',
      '10000',
      '-out',
      '@OUTPUT@',
    ],
  )

  cat = find_program('cat')

  cert_chain_pem_tgt = custom_target(
    'cert-chain.pem',
    input: [cert_intca_pem_tgt, cert_ca_pem_tgt],
    output: 'cert-chain.pem',
    capture: true,
    command: [cat, '@INPUT@'],
  )

  cert_entity_int_key_pem_tgt = custom_target(
    'cert-entity-int-key.pem',
    output: 'cert-entity-int-key.pem',
    command: [openssl, 'genrsa', '-out', '@OUTPUT@'],
  )

  cert_entity_int_csr_tgt = custom_target(
    'cert-entity-int.csr',
    input: cert_entity_int_key_pem_tgt,
    output: 'cert-entity-int.csr',
    command: [
      openssl,
      'req',
      '-new',
      '-extensions',
      'cert_ext',
      '-config',
      files('gencerts.cnf'),
      '-subj',
      '/O=Baz Example Organization/CN=Baz Example Organization/emailAddress=baz@mail.example',
      '-key',
      '@INPUT@',
      '-out',
      '@OUTPUT@',
    ],
  )

  cert_entity_int_pem_tgt = custom_target(
    'cert-entity-int.pem',
    input: [
      cert_entity_int_csr_tgt,
      cert_intca_pem_tgt,
      cert_intca_key_pem_tgt,
    ],
    output: 'cert-entity-int.pem',
    command: [
      openssl,
      'x509',
      '-req',
      '-extensions',
      'cert_ext',
      '-extfile',
      files('gencerts.cnf'),
      '-in',
      '@INPUT0@',
      '-CA',
      '@INPUT1@',
      '-CAkey',
      '@INPUT2@',
      '-CAserial',
      'cert-intca.srl',
      '-CAcreateserial',
      '-sha256',
      '-days',
      '10000',
      '-out',
      '@OUTPUT@',
    ],
  )

  cert_ca2_pem_tgt = custom_target(
    'cert-ca2.pem',
    input: cert_ca_key_pem_tgt,
    output: 'cert-ca2.pem',
    command: [
      openssl,
      'req',
      '-x509',
      '-new',
      '-nodes',
      '-extensions',
      'ca_no_akid_ext',
      '-config',
      files('gencerts.cnf'),
      '-subj',
      '/O=International Union of Example Organizations/CN=Certificate issuer guy/emailAddress=ca-no-akid@mail.example',
      '-key',
      '@INPUT@',
      '-sha256',
      '-days',
      '10000',
      '-out',
      '@OUTPUT@',
    ],
  )

  cert_client_key_pkcs1_des_pem_tgt = custom_target(
    'cert-client-key-pkcs1-des.pem',
    input: cert_client_key_pkcs1_pem_tgt,
    output: 'cert-client-key-pkcs1-des.pem',
    command: [
      openssl,
      'rsa',
      '-in',
      '@INPUT@',
      '-out',
      '@OUTPUT@',
      '-des',
      '-passout',
      'pass:abc',
      openssl_legacy,
    ],
  )

  cert_no_keyid_csr_tgt = custom_target(
    'cert-no-keyid.csr',
    input: cert_client_key_pkcs1_pem_tgt,
    output: 'cert-no-keyid.csr',
    command: [
      openssl,
      'req',
      '-new',
      '-config',
      files('gencerts.cnf'),
      '-subj',
      '/O=Baz Example Organization/CN=Baz Example Organization/emailAddress=baz@mail.example',
      '-key',
      '@INPUT@',
      '-out',
      '@OUTPUT@',
    ],
  )

  cert_no_keyid_pem_tgt = custom_target(
    'cert-no-keyid.pem',
    input: [cert_no_keyid_csr_tgt, cert_ca2_pem_tgt, cert_ca_key_pem_tgt],
    output: 'cert-no-keyid.pem',
    command: [
      openssl,
      'x509',
      '-req',
      '-extensions',
      'no_keyid_ext',
      '-extfile',
      files('gencerts.cnf'),
      '-in',
      '@INPUT0@',
      '-CA',
      '@INPUT1@',
      '-CAkey',
      '@INPUT2@',
      '-CAserial',
      'cert-ca2.srl',
      '-CAcreateserial',
      '-sha256',
      '-days',
      '10000',
      '-out',
      '@OUTPUT@',
    ],
  )

  cert_expired_csr_tgt = custom_target(
    'cert-expired.csr',
    input: cert_client_key_pkcs1_pem_tgt,
    output: 'cert-expired.csr',
    command: [
      openssl,
      'req',
      '-new',
      '-extensions',
      'cert_ext',
      '-config',
      files('gencerts.cnf'),
      '-subj',
      '/O=Bar Example Organization/CN=Bar Example Organization/emailAddress=bar@mail.example',
      '-key',
      '@INPUT@',
      '-out',
      '@OUTPUT@',
    ],
  )

  echo = find_program('echo')

  cert_ca_cnf_tgt = custom_target(
    'cert-ca.cnf',
    output: 'cert-ca.cnf',
    capture: true,
    command: [
      echo,
      '-e',
      '[example]\ndatabase=cert-ca-index.txt\nserial=cert-ca.srl\npolicy=dummy\n[dummy]',
    ],
  )

  cert_entity_pkcs12_rc2_sha1_p12_tgt = custom_target(
    'cert-entity-pkcs12-rc2-sha1.p12',
    input: [
      cert_entity_int_key_pem_tgt,
      cert_entity_int_pem_tgt,
      cert_chain_pem_tgt,
    ],
    output: 'cert-entity-pkcs12-rc2-sha1.p12',
    command: [
      openssl,
      'pkcs12',
      '-inkey',
      '@INPUT0@',
      '-in',
      '@INPUT1@',
      '-certfile',
      '@INPUT2@',
      '-out',
      '@OUTPUT@',
      '-export',
      '-passout',
      'pass:abc',
      '-certpbe',
      'PBE-SHA1-RC2-40',
      '-keypbe',
      'PBE-SHA1-RC2-128',
      '-macalg',
      'sha1',
      openssl_legacy,
    ],
  )

  cert_entity_combined_pem_tgt = custom_target(
    'cert-entity-combined.pem',
    input: cert_entity_pkcs12_rc2_sha1_p12_tgt,
    output: 'cert-entity-combined.pem',
    command: [
      openssl,
      'pkcs12',
      '-in',
      '@INPUT@',
      '-out',
      '@OUTPUT@',
      '-passin',
      'pass:abc',
      '-passout',
      'pass:abc',
      openssl_legacy,
    ],
  )

  gen_cert_expired_pem_sh = find_program('gen-cert-expired-pem.sh')
  cert_expired_pem_tgt = custom_target(
    'cert-expired.pem',
    input: [
      cert_expired_csr_tgt,
      cert_ca_pem_tgt,
      cert_ca_key_pem_tgt,
      cert_ca_cnf_tgt,
      files('gencerts.cnf'),
    ],
    output: 'cert-expired.pem',
    command: [
      gen_cert_expired_pem_sh,
      '@INPUT0@',
      '@INPUT1@',
      '@INPUT2@',
      '@INPUT3@',
      '@INPUT4@',
      '@OUTPUT@',
    ],
  )

  cert_entity_pkcs12_nomac_p12_tgt = custom_target(
    'cert-entity-pkcs12-nomac.p12',
    input: [cert_entity_int_key_pem_tgt, cert_entity_int_pem_tgt],
    output: 'cert-entity-pkcs12-nomac.p12',
    command: [
      openssl,
      'pkcs12',
      '-inkey',
      '@INPUT0@',
      '-in',
      '@INPUT1@',
      '-out',
      '@OUTPUT@',
      '-export',
      '-passout',
      'pass:abc',
      '-nomac',
    ],
  )

  cert_entity_pkcs12_des_sha256_p12_tgt = custom_target(
    'cert-entity-pkcs12-des-sha256.p12',
    input: [
      cert_entity_int_key_pem_tgt,
      cert_entity_int_pem_tgt,
      cert_chain_pem_tgt,
    ],
    output: 'cert-entity-pkcs12-des-sha256.p12',
    command: [
      openssl,
      'pkcs12',
      '-inkey',
      '@INPUT0@',
      '-in',
      '@INPUT1@',
      '-certfile',
      '@INPUT2@',
      '-out',
      '@OUTPUT@',
      '-export',
      '-passout',
      'pass:abc',
      '-certpbe',
      'PBE-SHA1-3DES',
      '-keypbe',
      'PBE-SHA1-2DES',
      '-macalg',
      'sha256',
    ],
  )

  cert_entity_pkcs12_rc4_sha384_p12_tgt = custom_target(
    'cert-entity-pkcs12-rc4-sha384.p12',
    input: [
      cert_entity_int_key_pem_tgt,
      cert_entity_int_pem_tgt,
      cert_chain_pem_tgt,
    ],
    output: 'cert-entity-pkcs12-rc4-sha384.p12',
    command: [
      openssl,
      'pkcs12',
      '-inkey',
      '@INPUT0@',
      '-in',
      '@INPUT1@',
      '-certfile',
      '@INPUT2@',
      '-out',
      '@OUTPUT@',
      '-export',
      '-passout',
      'pass:abc',
      '-certpbe',
      'PBE-SHA1-RC4-128',
      '-keypbe',
      'PBE-SHA1-RC2-40',
      '-macalg',
      'sha384',
      openssl_legacy,
    ],
  )

  cert_entity_pkcs12_pkcs5_sha512_p12_tgt = custom_target(
    'cert-entity-pkcs12-pkcs5-sha512.p12',
    input: [
      cert_entity_int_key_pem_tgt,
      cert_entity_int_pem_tgt,
      cert_chain_pem_tgt,
    ],
    output: 'cert-entity-pkcs12-pkcs5-sha512.p12',
    command: [
      openssl,
      'pkcs12',
      '-inkey',
      '@INPUT0@',
      '-in',
      '@INPUT1@',
      '-certfile',
      '@INPUT2@',
      '-out',
      '@OUTPUT@',
      '-export',
      '-passout',
      'pass:abc',
      '-certpbe',
      'des-cbc',
      '-keypbe',
      'des-cbc',
      '-macalg',
      'sha512',
      openssl_legacy,
    ],
  )

  key_ciphertext_dat_tgt = custom_target(
    'key-ciphertext.dat',
    input: ['plaintext.txt', cert_client_pem_tgt],
    output: 'key-ciphertext.dat',
    command: [
      openssl,
      'rsautl',
      '-encrypt',
      '-pkcs',
      '-in',
      '@INPUT0@',
      '-certin',
      '-inkey',
      '@INPUT1@',
      '-out',
      '@OUTPUT@',
    ],
  )

  key_signature_dat_tgt = custom_target(
    'key-signature.dat',
    input: 'plaintext.txt',
    output: 'key-signature.dat',
    command: [
      openssl,
      'rsautl',
      '-sign',
      '-pkcs',
      '-in',
      '@INPUT@',
      '-inkey',
      cert_client_key_pkcs1_pem_tgt,
      '-out',
      '@OUTPUT@',
    ],
  )

  pem_rsa_files = [
    ['cert-client-key-pkcs1-des3.pem', '-des3'],
    ['cert-client-key-pkcs1-aes128.pem', '-aes128'],
    ['cert-client-key-pkcs1-aes192.pem', '-aes192'],
    ['cert-client-key-pkcs1-aes256.pem', '-aes256'],
  ]

  foreach file : pem_rsa_files
    test_pem_cert_deps += custom_target(
      file[0],
      input: cert_client_key_pkcs1_pem_tgt,
      output: file[0],
      command: [
        openssl,
        'rsa',
        '-in',
        '@INPUT@',
        '-out',
        '@OUTPUT@',
        file[1],
        '-passout',
        'pass:abc',
      ],
    )
  endforeach

  built_headers = [
    ['plaintext.txt', 'key-plaintext.h'],
    [key_ciphertext_dat_tgt, 'key-ciphertext.h'],
    [key_signature_dat_tgt, 'key-signature.h'],
  ]

  foreach header : built_headers
    gen_headers += custom_target(
      header[1],
      input: header[0],
      output: header[1],
      capture: true,
      feed: true,
      command: [xxd, '-i'],
    )
  endforeach

  cert_verifs = [
    [cert_server_pem_tgt, cert_ca_pem_tgt],
    [ec_cert_server_pem_tgt, ec_cert_ca_pem_tgt],
    [cert_client_pem_tgt, cert_ca_pem_tgt],
    [cert_intca_pem_tgt, cert_ca_pem_tgt],
    [cert_entity_int_pem_tgt, cert_chain_pem_tgt],
    [cert_no_keyid_pem_tgt, cert_ca2_pem_tgt],
  ]
  foreach cert_verif : cert_verifs
    test(
      cert_verif[0].full_path() + '-verify',
      openssl,
      args: [
        'verify',
        '-CAfile',
        cert_verif[1].full_path(),
        cert_verif[0].full_path(),
      ],
    )
  endforeach

  test_pem_cert_deps += [
    # test_pem
    cert_client_key_pkcs8_md5_des_pem_tgt,
    cert_client_key_pkcs8_sha1_des_pem_tgt,
    cert_client_key_pkcs8_v2_des_pem_tgt,
    cert_client_key_pkcs8_v2_des_ede3_pem_tgt,
    cert_client_key_pkcs8_v2_aes128_pem_tgt,
    cert_client_key_pkcs8_v2_aes256_pem_tgt,
    cert_client_key_pkcs1_des_pem_tgt,
    cert_client_key_pkcs1_pem_tgt,
    cert_client_key_pkcs1_des_pem_tgt,
    cert_client_key_pkcs8_pem_tgt,
    cert_client_key_pkcs8_sha1_des_pem_tgt,
    cert_client_pem_tgt,
    cert_client_crt_tgt,
    cert_entity_combined_pem_tgt,
    cert_entity_pkcs12_nomac_p12_tgt,
    cert_entity_pkcs12_rc2_sha1_p12_tgt,
    cert_entity_pkcs12_des_sha256_p12_tgt,
    cert_entity_pkcs12_rc4_sha384_p12_tgt,
    cert_entity_pkcs12_pkcs5_sha512_p12_tgt,
    # test_key
    cert_ca_pem_tgt,
    cert_server_pem_tgt,
    cert_intca_pem_tgt,
    cert_entity_int_pem_tgt,
    cert_client_pem_tgt,
    cert_client_key_pkcs8_pem_tgt,
    # test_tls
    cert_chain_pem_tgt,
    cert_expired_pem_tgt,
    cert_ca2_pem_tgt,
    cert_no_keyid_pem_tgt,
    ec_cert_ca_pem_tgt,
    ec_cert_server_pem_tgt,
    cert_server_key_pkcs8_pem_tgt,
  ]
endif

# Mocking l_getrandom() to get a stable random seed
libell_private_ecdh_dep = declare_dependency(
  link_with: libell_private,
  link_args: '-Wl,-wrap,l_getrandom',
)

if get_option('tests') or get_option('cert-tests')
  foreach test_name : tests
    dep = test_name == 'test-ecdh' ? libell_private_ecdh_dep : libell_private_dep
    exe = executable(
      test_name,
      ['@0@.c'.format(test_name), gen_headers, test_pem_cert_deps],
      include_directories: include_directories('..'),
      c_args: [
        '-DUNITDIR="@0@/unit/"'.format(meson.project_source_root()),
        '-DCERTDIR="@0@/unit/"'.format(meson.project_build_root()),
      ],
      dependencies: dep,
      install: false,
    )

    test(
      test_name,
      exe,
      protocol: 'tap',
    )
  endforeach
endif
