all_examples = [
  'io_uring-close-test.c',
  'io_uring-cp.c',
  'io_uring-test.c',
  'io_uring-udp.c',
  'kdigest.c',
  'link-cp.c',
  'napi-busy-poll-client.c',
  'napi-busy-poll-server.c',
  'poll-bench.c',
  'proxy.c',
  'reg-wait.c',
  'rsrc-update-bench.c',
  'send-zerocopy.c',
  'zcrx.c',
]

if has_ucontext
  all_examples += 'ucontext-cp.c'
endif

fs = import('fs')

example_c_args = cc.get_supported_arguments('-Wno-sign-compare')

foreach example_source : all_examples
  executable(
    fs.stem(example_source),
    [example_source, 'helpers.c'],
    c_args: example_c_args,
    dependencies: [uring, thread_dep],
  )
endforeach
