all_examples = [
  'io_uring-cp.c',
  'io_uring-test.c',
  'io_uring-udp.c',
  'link-cp.c',
  'poll-bench.c',
  'send-zerocopy.c',
]

if has_ucontext
  all_examples += 'ucontext-cp.c'
endif

fs = import('fs')

foreach example_source : all_examples
  executable(
    fs.stem(example_source),
    example_source,
    dependencies: uring,
  )
endforeach
