ssl_src = files(
  'bio_ssl.cc',
  'custom_extensions.cc',
  'd1_both.cc',
  'd1_lib.cc',
  'd1_pkt.cc',
  'd1_srtp.cc',
  'dtls_method.cc',
  'dtls_record.cc',
  'encrypted_client_hello.cc',
  'extensions.cc',
  'handoff.cc',
  'handshake.cc',
  'handshake_client.cc',
  'handshake_server.cc',
  's3_both.cc',
  's3_lib.cc',
  's3_pkt.cc',
  'ssl_aead_ctx.cc',
  'ssl_asn1.cc',
  'ssl_buffer.cc',
  'ssl_cert.cc',
  'ssl_cipher.cc',
  'ssl_decrepit.c',
  'ssl_file.cc',
  'ssl_key_share.cc',
  'ssl_lib.cc',
  'ssl_privkey.cc',
  'ssl_session.cc',
  'ssl_stat.cc',
  'ssl_text.cc',
  'ssl_transcript.cc',
  'ssl_transfer_asn1.cc',
  'ssl_versions.cc',
  'ssl_x509.cc',
  't1_enc.cc',
  'tls13_both.cc',
  'tls13_client.cc',
  'tls13_enc.cc',
  'tls13_server.cc',
  'tls_method.cc',
  'tls_record.cc',
)

ssl_c_args = cc.get_supported_arguments('-Wno-unused-parameter')

ssl_private_c_args = ['-DBORINGSSL_IMPLEMENTATION']

libssl_awslc = library(
  'ssl-awslc',
  ssl_src,
  dependencies: [libcrypto_dep, wsa2_dep],
  link_with: [libcrypto_awslc],
  include_directories: inc,
  c_args: [ssl_private_c_args],
  cpp_args: [ssl_c_args, ssl_private_c_args, public_c_args, private_c_args],
  gnu_symbol_visibility: 'hidden',
  install: true,
)

libssl_dep = declare_dependency(
  link_with: libssl_awslc,
  dependencies: [wsa2_dep],
  include_directories: inc,
  compile_args: [public_c_args],
  variables: ['OPENSSL_IS_AWS_LC=1'],
)

meson.override_dependency('libssl-awslc', libssl_dep)

ssl_testcases = {
  'span_test': {
    'sources': files('span_test.cc'),
  },
  'ssl_alps_test': {
    'sources': files('ssl_alps_test.cc'),
  },
  'ssl_ciphers_test': {
    'sources': files('ssl_ciphers_test.cc'),
  },
  'ssl_client_hello_test': {
    'sources': files('ssl_client_hello_test.cc'),
  },
  'ssl_ech_test': {
    'sources': files('ssl_ech_test.cc'),
  },
  'ssl_encoding_test': {
    'sources': files('ssl_encoding_test.cc'),
  },
  'ssl_test': {
    'sources': files('ssl_c_test.c', 'ssl_handshake_test.cc', 'ssl_test.cc'),
  },
  'ssl_hybrid_handshake_test': {
    'sources': files('ssl_hybrid_handshake_test.cc'),
  },
  'ssl_key_share_test': {
    'sources': files('ssl_key_share_test.cc'),
  },
  'ssl_misc_test': {
    'sources': files('ssl_misc_test.cc'),
  },
  'ssl_quic_test': {
    'sources': files('ssl_quic_test.cc'),
  },
  'ssl_version_test': {
    'sources': files('ssl_version_test.cc'),
    'timeout': 3000,
    'suite': 'slow',
  },
}

test_c_args = cc.get_supported_arguments(
  '-Wno-ignored-qualifiers',
  '-Wno-pedantic',
  '-Wno-unused-value',
)

if tests_opt.allowed()
  ssl_common_test = static_library(
    'ssl_common_test_lib',
    files('ssl_common_test.cc'),
    cpp_args: [ssl_c_args, test_c_args, public_c_args, private_c_args],
    dependencies: [libssl_dep, libcrypto_dep, gtest_dep],
    link_with: libtest_util,
    include_directories: inc,
  )

  foreach testname, kwargs : ssl_testcases
    test_exe = executable(
      testname,
      kwargs['sources'],
      cpp_args: [ssl_c_args, test_c_args, public_c_args, private_c_args],
      dependencies: [libssl_dep, libcrypto_dep, gtest_dep],
      include_directories: inc,
      link_with: [ssl_common_test, libtest_util],
    )
    test(
      testname,
      test_exe,
      protocol: 'gtest',
      timeout: kwargs.get('timeout', 30),
      suite: kwargs.get('suite', 'libssl-awslc'),
    )
  endforeach
endif
