all_examples = [
  'io_uring-close-test.c',
  'io_uring-cp.c',
  'io_uring-test.c',
  'io_uring-udp.c',
  'link-cp.c',
  'poll-bench.c',
  'send-zerocopy.c',
  'rsrc-update-bench.c',
]

if has_ucontext
  all_examples += 'ucontext-cp.c'
endif

fs = import('fs')

example_c_args = cc.get_supported_arguments('-Wno-sign-compare')

foreach example_source : all_examples
  executable(
    fs.stem(example_source),
    example_source,
    c_args: example_c_args,
    dependencies: [uring, thread_dep],
  )
endforeach
