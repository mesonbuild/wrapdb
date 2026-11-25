# To update this list: `make -f meson/rewrite.mk curl_exe_src`.
curl_src = files(
  
  '../lib/curlx/base64.c',
  '../lib/curlx/basename.c',
  '../lib/curlx/dynbuf.c',
  '../lib/curlx/multibyte.c',
  '../lib/curlx/nonblock.c',
  '../lib/curlx/strcopy.c',
  '../lib/curlx/strdup.c',
  '../lib/curlx/strerr.c',
  '../lib/curlx/strparse.c',
  '../lib/curlx/timediff.c',
  '../lib/curlx/timeval.c',
  '../lib/curlx/version_win32.c',
  '../lib/curlx/wait.c',
  '../lib/curlx/warnless.c',
  '../lib/curlx/win32-fopen.c',
  '../lib/curlx/winapi.c',
  'toolx/tool_time.c',
  'config2setopts.c',
  'slist_wc.c',
  'terminal.c',
  'tool_cb_dbg.c',
  'tool_cb_hdr.c',
  'tool_cb_prg.c',
  'tool_cb_rea.c',
  'tool_cb_see.c',
  'tool_cb_soc.c',
  'tool_cb_wrt.c',
  'tool_cfgable.c',
  'tool_dirhie.c',
  'tool_doswin.c',
  'tool_easysrc.c',
  'tool_filetime.c',
  'tool_findfile.c',
  'tool_formparse.c',
  'tool_getparam.c',
  'tool_getpass.c',
  'tool_help.c',
  'tool_helpers.c',
  'tool_ipfs.c',
  'tool_libinfo.c',
  'tool_listhelp.c',
  'tool_main.c',
  'tool_msgs.c',
  'tool_operate.c',
  'tool_operhlp.c',
  'tool_paramhlp.c',
  'tool_parsecfg.c',
  'tool_progress.c',
  'tool_setopt.c',
  'tool_ssls.c',
  'tool_stderr.c',
  'tool_urlglob.c',
  'tool_util.c',
  'tool_vms.c',
  'tool_writeout.c',
  'tool_writeout_json.c',
  'tool_xattr.c',
  'var.c',
)

curl_exe = executable(
  'curl',
  curl_src,
  c_args: ['-DCURL_STATICLIB', debug_args],
  dependencies: [curl_ilib_dep, libuv_dep],
  install: get_option('tool').allowed(),
)

# `runtests.pl` runs this to learn about disabled features.
curlinfo_exe = executable(
  'curlinfo',
  'curlinfo.c',
  c_args: ['-DCURL_STATICLIB', debug_args],
  dependencies: [build_tests, curl_ilib_dep, libuv_dep],
)

curltool_lib = static_library(
  'curltool',
  curl_src,
  c_args: ['-DCURL_STATICLIB', '-DUNITTESTS', debug_args],
  dependencies: [build_tests, curl_iflags_dep, libuv_dep],
)

curltool_dep = declare_dependency(
  link_with: curltool_lib,
)
