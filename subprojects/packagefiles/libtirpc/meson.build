project(
  'libtirpc',
  'c',
  license: 'BSD-3-Clause',
  version: '1.3.3',
)

if host_machine.system() != 'linux'
  error('Everything except Linux is unsupported.')
endif

cc = meson.get_compiler('c')

threads_dep = dependency('threads')
queue_dep = cc.has_header('sys/queue.h') ? dependency(
  '',
  required: false,
) : dependency('libbsd-overlay')

add_project_arguments(
  '-D_GNU_SOURCE',
  language: 'c',
)
add_project_arguments(
  '-DPORTMAP',
  language: 'c',
)
add_project_arguments(
  '-DHAVE_CONFIG_H',
  language: 'c',
)

cdata = configuration_data()
gssapi_dep = dependency(
  'krb5-gssapi',
  required: get_option('gssapi'),
)
if gssapi_dep.found() and cc.has_header('gssapi/gssapi_ext.h')
  add_project_arguments(
    '-DHAVE_GSSAPI_GSSAPI_EXT_H',
    language: 'c',
  )
else
  gssapi_dep = dependency(
    'gssapi',
    required: get_option('gssapi'),
  )
endif
if gssapi_dep.found()
  add_project_arguments(
    '-DHAVE_RPCSEC_GSS',
    language: 'c',
  )
endif

cdata.set('HAVE_FEATURES_H', cc.has_header('features.h'))
cdata.set10('HAVE_GETRPCBYNAME', cc.has_function('getrpcbyname'))
cdata.set10('HAVE_GETRPCBYNUMBER', cc.has_function('getrpcbynumber'))
cdata.set10('HAVE_SETRPCENT', cc.has_function('setrpcent'))
cdata.set10('HAVE_GETRPCENT', cc.has_function('getrpcent'))
cdata.set10('HAVE_ENDRPCENT', cc.has_function('endrpcent'))
cfile = configure_file(
  output: 'config.h',
  configuration: cdata,
)

incdirs = include_directories('.', 'tirpc')

sources = files(
  'src/auth_none.c',
  'src/auth_time.c',
  'src/auth_unix.c',
  'src/authunix_prot.c',
  'src/binddynport.c',
  'src/bindresvport.c',
  'src/clnt_bcast.c',
  'src/clnt_dg.c',
  'src/clnt_generic.c',
  'src/clnt_perror.c',
  'src/clnt_raw.c',
  'src/clnt_simple.c',
  'src/clnt_vc.c',
  'src/debug.c',
  'src/getnetconfig.c',
  'src/getnetpath.c',
  'src/getpeereid.c',
  'src/getpublickey.c',
  'src/getrpcent.c',
  'src/getrpcport.c',
  'src/key_call.c',
  'src/key_prot_xdr.c',
  'src/mt_misc.c',
  'src/netname.c',
  'src/netnamer.c',
  'src/pmap_clnt.c',
  'src/pmap_getmaps.c',
  'src/pmap_getport.c',
  'src/pmap_prot.c',
  'src/pmap_prot2.c',
  'src/pmap_rmt.c',
  'src/rpc_callmsg.c',
  'src/rpc_commondata.c',
  'src/rpc_dtablesize.c',
  'src/rpc_generic.c',
  'src/rpc_prot.c',
  'src/rpc_soc.c',
  'src/rpcb_clnt.c',
  'src/rpcb_prot.c',
  'src/rpcb_st_xdr.c',
  'src/rpcdname.c',
  'src/rtime.c',
  'src/svc.c',
  'src/svc_auth.c',
  'src/svc_auth_none.c',
  'src/svc_auth_unix.c',
  'src/svc_dg.c',
  'src/svc_generic.c',
  'src/svc_raw.c',
  'src/svc_run.c',
  'src/svc_simple.c',
  'src/svc_vc.c',
  'src/xdr.c',
  'src/xdr_array.c',
  'src/xdr_float.c',
  'src/xdr_mem.c',
  'src/xdr_rec.c',
  'src/xdr_reference.c',
  'src/xdr_sizeof.c',
  'src/xdr_stdio.c',
)

if get_option('authdes')
  sources += files(
    'src/auth_des.c',
    'src/authdes_prot.c',
    'src/des_crypt.c',
    'src/des_impl.c',
    'src/des_soft.c',
    'src/svc_auth_des.c',
  )
  add_project_arguments(
    '-DAUTHDES_SUPPORT',
    language: 'c',
  )
endif

if get_option('ipv6')
  add_project_arguments(
    '-DINET6',
    language: 'c',
  )
endif

if gssapi_dep.found()
  sources += files(
    'src/auth_gss.c',
    'src/authgss_prot.c',
    'src/rpc_gss_utils.c',
    'src/svc_auth_gss.c',
  )
endif

libtirpc = library(
  'tirpc',
  sources,
  dependencies: [gssapi_dep, queue_dep, threads_dep],
  include_directories: incdirs,
  install: true,
)

libtirpc_dep = declare_dependency(
  include_directories: incdirs,
  link_with: libtirpc,
)

pconf = import('pkgconfig')
pconf.generate(
  libtirpc,
  name: 'libtirpc',
  description: 'Transport Independent RPC Library',
  subdirs: 'tirpc',
)

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
