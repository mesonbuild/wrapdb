project(
  'libtirpc',
  'c',
  license: 'BSD-3-Clause',
  version: '1.3.7',
  meson_version: '>=0.60.0',
)

if host_machine.system() != 'linux'
  error('Everything except Linux is unsupported.')
endif

cc = meson.get_compiler('c')

threads_dep = dependency('threads')
gssapi_dep = dependency(
  'krb5-gssapi',
  'gssapi',
  required: get_option('gssapi'),
)

if cc.has_header('sys/queue.h')
  queue_dep = dependency(
    '',
    required: false,
  )
else
  queue_dep = dependency('libbsd-overlay')
endif

cdata = configuration_data()
cdata.set('HAVE_RPCSEC_GSS', gssapi_dep.found())
cdata.set(
  'HAVE_GSS_PNAME_TO_UID',
  cc.has_function(
    'gss_pname_to_uid',
    dependencies: gssapi_dep,
  ),
)
cdata.set(
  'HAVE_GSSAPI_GSSAPI_EXT_H',
  cc.has_header(
    'gssapi/gssapi_ext.h',
    dependencies: gssapi_dep,
  ),
)
cdata.set('INET6', cc.has_header('netinet/ip6.h'))
cdata.set10('HAVE_ENDRPCENT', cc.has_function('endrpcent'))
cdata.set10('HAVE_GETRPCBYNAME', cc.has_function('getrpcbyname'))
cdata.set10('HAVE_GETRPCBYNUMBER', cc.has_function('getrpcbynumber'))
cdata.set10('HAVE_GETRPCENT', cc.has_function('getrpcent'))
cdata.set10('HAVE_SETRPCENT', cc.has_function('setrpcent'))
if queue_dep.found()
  cdata.set10('HAVE_GETPEERID', true)
else
  cdata.set10('HAVE_GETPEERID', cc.has_function('getpeerid'))
endif
cfile = configure_file(
  output: 'config.h',
  configuration: cdata,
)

incdirs = include_directories('.', 'tirpc')

subdir('src')

install_data(
  'doc/netconfig',
  install_dir: get_option('sysconfdir'),
)

install_headers(
  'tirpc/netconfig.h',
  subdir: 'tirpc',
)

install_headers(
  'tirpc/rpc/auth_des.h',
  'tirpc/rpc/auth_gss.h',
  'tirpc/rpc/auth.h',
  'tirpc/rpc/auth_unix.h',
  'tirpc/rpc/clnt.h',
  'tirpc/rpc/clnt_soc.h',
  'tirpc/rpc/clnt_stat.h',
  'tirpc/rpc/des_crypt.h',
  'tirpc/rpc/des.h',
  'tirpc/rpc/key_prot.h',
  'tirpc/rpc/nettype.h',
  'tirpc/rpc/pmap_clnt.h',
  'tirpc/rpc/pmap_prot.h',
  'tirpc/rpc/pmap_rmt.h',
  'tirpc/rpc/raw.h',
  'tirpc/rpc/rpcb_clnt.h',
  'tirpc/rpc/rpcb_prot.h',
  'tirpc/rpc/rpc_com.h',
  'tirpc/rpc/rpcent.h',
  'tirpc/rpc/rpc.h',
  'tirpc/rpc/rpc_msg.h',
  'tirpc/rpc/rpcsec_gss.h',
  'tirpc/rpc/svc_auth_gss.h',
  'tirpc/rpc/svc_auth.h',
  'tirpc/rpc/svc_dg.h',
  'tirpc/rpc/svc.h',
  'tirpc/rpc/svc_mt.h',
  'tirpc/rpc/svc_soc.h',
  'tirpc/rpc/types.h',
  'tirpc/rpc/xdr.h',
  subdir: 'tirpc/rpc',
)

install_headers(
  'tirpc/rpcsvc/crypt.h',
  subdir: 'tirpc/rpcsvc',
)
