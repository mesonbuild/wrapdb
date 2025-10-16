socket = cc.has_header(
  'sys/socket.h',
  required: get_option('raf-cache'),
)

if not socket
  subdir_done()
endif

curl_dep = dependency(
  'libcurl',
  required: get_option('raf-cache'),
)

if not curl_dep.found()
  subdir_done()
endif

executable(
  'ref-cache',
  'cmsg_wrap.c',
  'http_parser.c',
  'listener.c',
  'log_files.c',
  'main.c',
  'misc.c',
  'ping.c',
  'poll_wrap_epoll.c',
  'poll_wrap_poll.c',
  'ref_files.c',
  'request_handler.c',
  'sendfile_wrap.c',
  'server.c',
  'transaction.c',
  'upstream.c',
  '../cram/pooled_alloc.c',
  dependencies: [curl_dep, htslib_dep],
)
