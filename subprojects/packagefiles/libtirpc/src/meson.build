sources = files(
  'auth_none.c',
  'auth_time.c',
  'auth_unix.c',
  'authunix_prot.c',
  'binddynport.c',
  'bindresvport.c',
  'clnt_bcast.c',
  'clnt_dg.c',
  'clnt_generic.c',
  'clnt_perror.c',
  'clnt_raw.c',
  'clnt_simple.c',
  'clnt_vc.c',
  'debug.c',
  'getnetconfig.c',
  'getnetpath.c',
  'getpeereid.c',
  'getpublickey.c',
  'getrpcent.c',
  'getrpcport.c',
  'key_call.c',
  'key_prot_xdr.c',
  'mt_misc.c',
  'netname.c',
  'netnamer.c',
  'pmap_clnt.c',
  'pmap_getmaps.c',
  'pmap_getport.c',
  'pmap_prot.c',
  'pmap_prot2.c',
  'pmap_rmt.c',
  'rpc_callmsg.c',
  'rpc_commondata.c',
  'rpc_dtablesize.c',
  'rpc_generic.c',
  'rpc_prot.c',
  'rpc_soc.c',
  'rpcb_clnt.c',
  'rpcb_prot.c',
  'rpcb_st_xdr.c',
  'rpcdname.c',
  'rtime.c',
  'svc.c',
  'svc_auth.c',
  'svc_auth_none.c',
  'svc_auth_unix.c',
  'svc_dg.c',
  'svc_generic.c',
  'svc_raw.c',
  'svc_run.c',
  'svc_simple.c',
  'svc_vc.c',
  'xdr.c',
  'xdr_array.c',
  'xdr_float.c',
  'xdr_mem.c',
  'xdr_rec.c',
  'xdr_reference.c',
  'xdr_sizeof.c',
  'xdr_stdio.c',
)

cargs = ['-DHAVE_CONFIG_H', '-D_XOPEN_SOURCE=700', '-D_GNU_SOURCE', '-DPORTMAP']
if get_option('authdes')
  sources += files(
    'auth_des.c',
    'authdes_prot.c',
    'des_crypt.c',
    'des_impl.c',
    'des_soft.c',
    'svc_auth_des.c',
  )
  cargs += '-DAUTHDES_SUPPORT'
endif

if gssapi_dep.found()
  sources += files(
    'auth_gss.c',
    'authgss_prot.c',
    'rpc_gss_utils.c',
    'svc_auth_gss.c',
  )
endif

libtirpc = library(
  'tirpc',
  sources,
  c_args: cargs,
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
