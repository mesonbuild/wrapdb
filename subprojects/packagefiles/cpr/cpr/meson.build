cpr_src = files(
  'accept_encoding.cpp',
  'async.cpp',
  'auth.cpp',
  'bearer.cpp',
  'callback.cpp',
  'cert_info.cpp',
  'cookies.cpp',
  'cprtypes.cpp',
  'curl_container.cpp',
  'curlholder.cpp',
  'curlmultiholder.cpp',
  'error.cpp',
  'file.cpp',
  'interceptor.cpp',
  'multipart.cpp',
  'multiperform.cpp',
  'parameters.cpp',
  'payload.cpp',
  'proxies.cpp',
  'proxyauth.cpp',
  'redirect.cpp',
  'response.cpp',
  'session.cpp',
  'ssl_ctx.cpp',
  'threadpool.cpp',
  'timeout.cpp',
  'unix_socket.cpp',
  'util.cpp',
)

var = meson.project_version().split('.')

cdata = configuration_data()
cdata.set('cpr_VERSION', meson.project_version())
cdata.set('cpr_VERSION_MAJOR', var[0])
cdata.set('cpr_VERSION_MINOR', var[1])
cdata.set('cpr_VERSION_PATCH', var[2])
cdata.set('cpr_VERSION_NUM', '0x10906')

configure_file(
  input: '../cmake/cprver.h.in',
  output: 'cprver.h',
  format: 'cmake',
  configuration: cdata,
)
