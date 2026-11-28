# `curl_config.h` generation. {{

config_h = configure_file(
  configuration: cdata,
  input: '../meson/curl_config.h.meson',
  output: 'curl_config.h',
)

add_project_arguments(
  '-DHAVE_CONFIG_H',
  language: 'c',
)

# }}}

# To update this list: `make -f meson/rewrite.mk curl_lib_src`.
curl_lib_src_names = [
  'curlx/base64.c',
  'curlx/basename.c',
  'curlx/dynbuf.c',
  'curlx/inet_ntop.c',
  'curlx/inet_pton.c',
  'curlx/multibyte.c',
  'curlx/nonblock.c',
  'curlx/snprintf.c',
  'curlx/strcopy.c',
  'curlx/strdup.c',
  'curlx/strerr.c',
  'curlx/strparse.c',
  'curlx/timediff.c',
  'curlx/timeval.c',
  'curlx/version_win32.c',
  'curlx/wait.c',
  'curlx/warnless.c',
  'curlx/win32-fopen.c',
  'curlx/winapi.c',
  'vauth/cleartext.c',
  'vauth/cram.c',
  'vauth/digest.c',
  'vauth/digest_sspi.c',
  'vauth/gsasl.c',
  'vauth/krb5_gssapi.c',
  'vauth/krb5_sspi.c',
  'vauth/ntlm.c',
  'vauth/ntlm_sspi.c',
  'vauth/oauth2.c',
  'vauth/spnego_gssapi.c',
  'vauth/spnego_sspi.c',
  'vauth/vauth.c',
  'vdns/asyn-ares.c',
  'vdns/asyn-base.c',
  'vdns/asyn-thrdd.c',
  'vdns/cf-dns.c',
  'vdns/dnscache.c',
  'vdns/doh.c',
  'vdns/hostip.c',
  'vdns/hostip4.c',
  'vdns/hostip6.c',
  'vdns/httpsrr.c',
  'vquic/capsule.c',
  'vquic/cf-capsule.c',
  'vquic/cf-ngtcp2-cmn.c',
  'vquic/cf-ngtcp2-proxy.c',
  'vquic/cf-ngtcp2.c',
  'vquic/cf-quiche.c',
  'vquic/vquic-tls.c',
  'vquic/vquic.c',
  'vssh/libssh.c',
  'vssh/libssh2.c',
  'vssh/vssh.c',
  'vtls/apple.c',
  'vtls/cipher_suite.c',
  'vtls/gtls.c',
  'vtls/hostcheck.c',
  'vtls/keylog.c',
  'vtls/mbedtls.c',
  'vtls/openssl.c',
  'vtls/rustls.c',
  'vtls/schannel.c',
  'vtls/schannel_verify.c',
  'vtls/vtls.c',
  'vtls/vtls_config.c',
  'vtls/vtls_scache.c',
  'vtls/vtls_spack.c',
  'vtls/wolfssl.c',
  'vtls/x509asn1.c',
  'altsvc.c',
  'amigaos.c',
  'api.c',
  'bufq.c',
  'bufref.c',
  'cf-h1-proxy.c',
  'cf-h2-proxy.c',
  'cf-haproxy.c',
  'cf-https-connect.c',
  'cf-ip-happy.c',
  'cf-recvbuf.c',
  'cf-setup.c',
  'cf-socket.c',
  'cfilters.c',
  'conncache.c',
  'connect.c',
  'content_encoding.c',
  'cookie.c',
  'creds.c',
  'cshutdn.c',
  'curl_addrinfo.c',
  'curl_ed25519.c',
  'curl_endian.c',
  'curl_fnmatch.c',
  'curl_fopen.c',
  'curl_get_line.c',
  'curl_gethostname.c',
  'curl_gssapi.c',
  'curl_memrchr.c',
  'curl_ntlm_core.c',
  'curl_range.c',
  'curl_sasl.c',
  'curl_sha512_256.c',
  'curl_share.c',
  'curl_sspi.c',
  'curl_threads.c',
  'curl_trc.c',
  'cw-out.c',
  'cw-pause.c',
  'dict.c',
  'dynhds.c',
  'easy.c',
  'easygetopt.c',
  'easyoptions.c',
  'escape.c',
  'fake_addrinfo.c',
  'file.c',
  'fileinfo.c',
  'formdata.c',
  'ftp.c',
  'ftplistparser.c',
  'getenv.c',
  'getinfo.c',
  'gopher.c',
  'hash.c',
  'headers.c',
  'hmac.c',
  'hsts.c',
  'http.c',
  'http1.c',
  'http2.c',
  'http_aws_sigv4.c',
  'http_chunks.c',
  'http_digest.c',
  'http_httpsig.c',
  'http_negotiate.c',
  'http_ntlm.c',
  'http_proxy.c',
  'idn.c',
  'if2ip.c',
  'imap.c',
  'ldap.c',
  'llist.c',
  'macos.c',
  'md4.c',
  'md5.c',
  'memdebug.c',
  'mime.c',
  'mprintf.c',
  'mqtt.c',
  'multi.c',
  'multi_ev.c',
  'multi_ntfy.c',
  'netrc.c',
  'openldap.c',
  'parsedate.c',
  'peer.c',
  'pingpong.c',
  'pop3.c',
  'progress.c',
  'protocol.c',
  'proxy.c',
  'psl.c',
  'ptrarray.c',
  'rand.c',
  'ratelimit.c',
  'request.c',
  'rtsp.c',
  'select.c',
  'sendf.c',
  'setopt.c',
  'sha256.c',
  'slist.c',
  'smtp.c',
  'socketpair.c',
  'socks.c',
  'socks_gssapi.c',
  'socks_sspi.c',
  'splay.c',
  'strcase.c',
  'strequal.c',
  'strerror.c',
  'telnet.c',
  'tftp.c',
  'thrdpool.c',
  'thrdqueue.c',
  'transfer.c',
  'u32_ptrset.c',
  'u8_strset.c',
  'uint-bset.c',
  'uint-spbset.c',
  'uint-table.c',
  'url.c',
  'urlapi.c',
  'version.c',
  'ws.c',
]
curl_lib_src = files(curl_lib_src_names)

# `unitprotos.h`, needed by the unit tests (see `tests/libtest/unitcheck.h`).
lib_build_inc = include_directories('.')
unitprotos_h = []
if build_unittests.found()
  unitprotos_h = custom_target(
    'unitprotos.h',
    command: [
      bash_exe,
      '-c',
      'cd "$0" && exec perl "$@"',
      meson.current_source_dir(),
      meson.project_source_root() / 'scripts/extract-unit-protos',
    ] + curl_lib_src_names,
    depend_files: curl_lib_src + files('../scripts/extract-unit-protos'),
    capture: true,
    output: 'unitprotos.h',
  )
endif

curl_lib = library(
  'curl',
  config_h,
  curl_lib_src,
  c_args: [
    '-DBUILDING_LIBCURL',
    curl_symbols_hiding_flags,
    public_args,
    debug_args,
  ],
  dependencies: [lib_deps, sys_deps],
  gnu_symbol_visibility: curl_symbols_hiding_visibility,
  include_directories: [CURL_PUBLIC_INC, CURL_INTERNAL_INC],
  install: true,
  version: '4.8.0',
)

pkg.generate(
  curl_lib,
  description: 'Library to transfer files with ftp, http, etc.',
  extra_cflags: public_args,
  name: 'libcurl',
  unescaped_variables: (
    # NOTE: variables with empty values are not allowed…
    (
      enabled_features.length() > 0 ? {
        'supported_features': ' '.join(enabled_features),
      } : {}
    ) + (
      enabled_protocols.length() > 0 ? {
        'supported_protocols': ' '.join(enabled_protocols),
      } : {}
    )
  ),
  url: 'https://curl.se/',
)

curl_dep = declare_dependency(
  compile_args: public_args,
  include_directories: CURL_PUBLIC_INC,
  link_with: curl_lib,
  sources: config_h,
)

meson.override_dependency('libcurl', curl_dep)

lib_deps_iflags = []
foreach _dep : lib_deps
  lib_deps_iflags += _dep.partial_dependency(
    compile_args: true,
    includes: true,
  )
endforeach

curl_iflags_dep = declare_dependency(
  dependencies: lib_deps_iflags,
  include_directories: [CURL_PUBLIC_INC, CURL_INTERNAL_INC],
)

curl_ilib_dep = declare_dependency(
  dependencies: [curl_dep, curl_iflags_dep, sys_deps],
)

curlu_flags = ['-DCURL_STATICLIB', '-DUNITTESTS']

curlu_lib = static_library(
  'curlu',
  config_h,
  curl_lib_src,
  c_args: [curlu_flags, '-DBUILDING_LIBCURL', debug_args],
  dependencies: [build_unittests, lib_deps],
  include_directories: [CURL_PUBLIC_INC, CURL_INTERNAL_INC],
)

curlu_dep = declare_dependency(
  dependencies: sys_deps,
  include_directories: [
    CURL_INTERNAL_INC,
    CURL_PUBLIC_INC,
  ],
  link_with: curlu_lib,
  sources: [config_h, unitprotos_h],
)

# vim: foldmethod=marker foldlevel=0
