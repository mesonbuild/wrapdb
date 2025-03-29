win_sources = host_machine.system() == 'windows' ? files('../win32/wingetopt.c') : []

examples = [
  {
    'e': 'producer',
    's': 'producer.c',
  },
  {
    'e': 'producer_cpp',
    's': 'producer.cpp',
  },
  {
    'e': 'consumer',
    's': 'consumer.c',
  },
  {
    'e': 'rdkafka_performance',
    's': 'rdkafka_performance.c',
  },
  {
    'e': 'rdkafka_example_cpp',
    's': 'rdkafka_example.cpp',
  },
  {
    'e': 'rdkafka_complex_consumer_example_cpp',
    's': 'rdkafka_complex_consumer_example.cpp',
  },
  {
    'e': 'openssl_engine_example_cpp',
    's': 'openssl_engine_example.cpp',
  },
]
if host_machine.system() != 'windows'
  examples += [
    {
      'e': 'rdkafka_example',
      's': 'rdkafka_example.c',
    },
    {
      'e': 'rdkafka_complex_consumer_example',
      's': 'rdkafka_complex_consumer_example.c',
    },
    {
      'e': 'kafkatest_verifiable_client',
      's': 'kafkatest_verifiable_client.cpp',
    },
  ]
endif

foreach ex : examples
  executable(
    ex['e'],
    [ex['s']] + win_sources,
    dependencies: rdkafka_dep,
    include_directories: include_directories('../src', '../src-cpp'),
    build_by_default: false,
  )
endforeach

