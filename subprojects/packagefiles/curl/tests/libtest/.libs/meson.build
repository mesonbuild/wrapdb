# `runtests.pl` expects `libhostname.so` and `libstubgss.so`
# to be present in a `.libs` subdirectory of `tests/libtest`.

libtest_targets += shared_library(
  'hostname',
  '../sethostname.c',
  c_args: curl_symbols_hiding_flags,
  dependencies: curl_iflags_dep,
  gnu_symbol_visibility: curl_symbols_hiding_visibility,
)

if gss_api_opt.allowed()
  libtest_targets += shared_library('stubgss', '../stub_gssapi.c')
endif
