project(
  'rdkafka',
  'c',
  'cpp',
  version: '2.10.0',
  default_options: ['cpp_std=c++17', 'c_std=c11', 'warning_level=0'],
  meson_version: '>=0.57.0',
)

cc = meson.get_compiler('c')
cpp = meson.get_compiler('cpp')
pkgconfig = import('pkgconfig')

if cc.get_argument_syntax() == 'msvc'
  add_project_arguments(
    '-D_CRT_SECURE_NO_WARNINGS',
    cc.get_supported_arguments(
      '-Wno-deprecated-declarations',
      '-Wno-format',
      '-Wno-incompatible-pointer-types',
      '-Wno-pointer-sign',
      '-Wno-self-assign-field',
      '-Wno-visibility',
    ),
    language: 'c',
  )
  add_project_arguments(
    '-D_CRT_SECURE_NO_WARNINGS',
    cpp.get_supported_arguments(
      '-Wno-deprecated-declarations',
      '-Wno-format',
      '-Wno-incompatible-pointer-types',
      '-Wno-pointer-sign',
      '-Wno-self-assign-field',
      '-Wno-visibility',
    ),
    language: 'cpp',
  )
endif

if host_machine.system() == 'windows'
  add_project_arguments(
    '-D_WIN32_WINNT=0x0600',
    '-DUNICODE',
    language: 'c',
  )
  add_project_arguments(
    '-D_WIN32_WINNT=0x0600',
    '-DUNICODE',
    language: 'cpp',
  )
endif

hdr = files('src-cpp/rdkafkacpp.h', 'src/rdkafka.h')
subdir('include-workaround-meson/librdkafka')

srcc = files(
  'src/crc32c.c',
  'src/nanopb/pb_common.c',
  'src/nanopb/pb_decode.c',
  'src/nanopb/pb_encode.c',
  'src/opentelemetry/common.pb.c',
  'src/opentelemetry/metrics.pb.c',
  'src/opentelemetry/resource.pb.c',
  'src/rdaddr.c',
  'src/rdavl.c',
  'src/rdbase64.c',
  'src/rdbuf.c',
  'src/rdcrc32.c',
  'src/rdfnv1a.c',
  'src/rdkafka.c',
  'src/rdkafka_admin.c',
  'src/rdkafka_assignment.c',
  'src/rdkafka_assignor.c',
  'src/rdkafka_aux.c',
  'src/rdkafka_background.c',
  'src/rdkafka_broker.c',
  'src/rdkafka_buf.c',
  'src/rdkafka_cert.c',
  'src/rdkafka_cgrp.c',
  'src/rdkafka_conf.c',
  'src/rdkafka_coord.c',
  'src/rdkafka_error.c',
  'src/rdkafka_event.c',
  'src/rdkafka_feature.c',
  'src/rdkafka_fetcher.c',
  'src/rdkafka_header.c',
  'src/rdkafka_idempotence.c',
  'src/rdkafka_interceptor.c',
  'src/rdkafka_lz4.c',
  'src/rdkafka_metadata.c',
  'src/rdkafka_metadata_cache.c',
  'src/rdkafka_mock.c',
  'src/rdkafka_mock_cgrp.c',
  'src/rdkafka_mock_handlers.c',
  'src/rdkafka_msg.c',
  'src/rdkafka_msgset_reader.c',
  'src/rdkafka_msgset_writer.c',
  'src/rdkafka_offset.c',
  'src/rdkafka_op.c',
  'src/rdkafka_partition.c',
  'src/rdkafka_pattern.c',
  'src/rdkafka_queue.c',
  'src/rdkafka_range_assignor.c',
  'src/rdkafka_request.c',
  'src/rdkafka_roundrobin_assignor.c',
  'src/rdkafka_sasl.c',
  'src/rdkafka_sasl_plain.c',
  'src/rdkafka_sticky_assignor.c',
  'src/rdkafka_subscription.c',
  'src/rdkafka_telemetry.c',
  'src/rdkafka_telemetry_decode.c',
  'src/rdkafka_telemetry_encode.c',
  'src/rdkafka_timer.c',
  'src/rdkafka_topic.c',
  'src/rdkafka_transport.c',
  'src/rdkafka_txnmgr.c',
  'src/rdlist.c',
  'src/rdlog.c',
  'src/rdmap.c',
  'src/rdmurmur2.c',
  'src/rdports.c',
  'src/rdrand.c',
  'src/rdregex.c',
  'src/rdstring.c',
  'src/rdunittest.c',
  'src/rdvarint.c',
  'src/rdxxhash.c',
  'src/snappy.c',
  'src/tinycthread.c',
  'src/tinycthread_extra.c',
)

srccpp = files(
  'src-cpp/ConfImpl.cpp',
  'src-cpp/ConsumerImpl.cpp',
  'src-cpp/HandleImpl.cpp',
  'src-cpp/HeadersImpl.cpp',
  'src-cpp/KafkaConsumerImpl.cpp',
  'src-cpp/MessageImpl.cpp',
  'src-cpp/MetadataImpl.cpp',
  'src-cpp/ProducerImpl.cpp',
  'src-cpp/QueueImpl.cpp',
  'src-cpp/RdKafka.cpp',
  'src-cpp/TopicImpl.cpp',
  'src-cpp/TopicPartitionImpl.cpp',
)

cjson = dependency('libcjson')
curl = dependency(
  'libcurl',
  required: get_option('WITH_CURL'),
)
zlib = dependency(
  'zlib',
  required: get_option('WITH_ZLIB'),
)
zstd = dependency(
  'libzstd',
  required: get_option('WITH_ZSTD'),
)
lz4 = dependency(
  'liblz4',
  required: get_option('WITH_LZ4_EXT'),
)
sasl = dependency(
  'libsasl2',
  required: get_option('WITH_SASL'),
)  # TODO: make SASL usable without libsasl2 on windows
ssl = dependency(
  'openssl',
  required: get_option('WITH_SSL'),
)
if meson.version().version_compare('>= 0.62.0')
  dl = dependency(
    'dl',
    required: get_option('WITH_LIBDL'),
  )
else
  dl = cc.find_library(
    'dl',
    required: get_option('WITH_LIBDL'),
  )
endif
threads = dependency('threads')
regex = dependency(
  'regex',
  required: false,
)
math = cc.find_library(
  'm',
  required: false,
)

conf = configuration_data()
conf.set10('WITHOUT_OPTIMIZATION', get_option('WITHOUT_OPTIMIZATION'))
conf.set10('ENABLE_DEVEL', get_option('ENABLE_DEVEL'))
conf.set10('ENABLE_REFCNT_DEBUG', get_option('ENABLE_REFCNT_DEBUG'))
conf.set10('WITH_PKGCONFIG', find_program('pkg-config').found())
conf.set10('WITH_HDRHISTOGRAM', get_option('ENABLE_HDRHISTOGRAM'))
conf.set10('WITH_ZLIB', zlib.found())
conf.set10('WITH_CURL', curl.found())
conf.set10('WITH_OAUTHBEARER_OIDC', false)
conf.set10('WITH_ZSTD', zstd.found())
conf.set10('WITH_LIBDL', dl.found())
conf.set10('WITH_PLUGINS', dl.found())
conf.set10('WITH_SSL', ssl.found())
conf.set10('WITH_SASL', sasl.found())
conf.set10(
  'WITH_SASL_CYRUS',
  sasl.found() and host_machine.system() != 'windows',
)
conf.set10('WITH_LZ4_EXT', lz4.found())
conf.set10(
  'HAVE_REGEX',
  cc.has_function(
    'regcomp',
    dependencies: regex,
  ),
)
conf.set10(
  'HAVE_STRNDUP',
  host_machine.system() != 'windows' and cc.has_function('strndup'),
)
conf.set10(
  'HAVE_RAND_R',
  cc.has_header_symbol(
    'stdlib.h',
    'rand_r',
    args: '-D_POSIX_THREAD_SAFE_FUNCTIONS',
  ),
)
conf.set10(
  'WITH_C11THREADS',
  cc.has_function(
    'thrd_create',
    dependencies: threads,
  ) and host_machine.system() != 'windows',
)
conf.set(
  'CMAKE_SHARED_LIBRARY_SUFFIX',
  host_machine.system() == 'windows' ? '.dll' : '.so',
)

built_with = 'meson ' + cc.get_id() + ' ' + cpp.get_id()
if ssl.found()
  built_with += ' SSL'
  srcc += files('src/rdkafka_ssl.c')
endif
if dl.found()
  srcc += files('src/rddl.c', 'src/rdkafka_plugin.c')
  built_with += ' LIBDL PLUGINS'
endif
if host_machine.system() == 'windows'
  srcc += files('src/rdkafka_sasl_win32.c')
elif sasl.found()
  srcc += files('src/rdkafka_sasl_cyrus.c')
  built_with += ' SASL_CYRUS'
  if ssl.found()
    srcc += files('src/rdkafka_sasl_oauthbearer.c', 'src/rdkafka_sasl_scram.c')
    conf.set10('WITH_SASL_SCRAM', true)
    conf.set10('WITH_SASL_OAUTHBEARER', true)
    built_with += ' SASL_SCRAM SASL_OAUTHBEARER'
  endif
endif

if zlib.found()
  srcc += files('src/rdgz.c')
  built_with += ' ZLIB'
endif
if zstd.found()
  srcc += files('src/rdkafka_zstd.c')
  built_with += ' ZSTD'
endif
if not lz4.found()
  srcc += files('src/lz4.c', 'src/lz4frame.c', 'src/lz4hc.c')
  built_with += ' LZ4'
endif
if curl.found()
  srcc += files('src/rdhttp.c')
endif
if conf.get('HAVE_REGEX') == 0
  srcc += files('src/regexp.c')
endif
if get_option('ENABLE_HDRHISTOGRAM')
  srcc += files('src/rdhdrhistogram.c')
endif

#upstream is broken and all config.h entries must be passed as compiler flags
if host_machine.system() == 'windows'
  add_project_arguments(
    '-DWITHOUT_WIN32_CONFIG',
    language: 'c',
  )
  #hack for rand_r
  add_project_arguments(
    '-D_POSIX_THREAD_SAFE_FUNCTIONS',
    language: 'c',
  )
  foreach c : conf.keys()
    add_project_arguments(
      '-D@0@=@1@'.format(c, conf.get(c)),
      language: 'c',
    )
  endforeach
  if get_option('default_library') != 'static'
    add_project_arguments(
      '-DLIBRDKAFKA_EXPORTS',
      language: 'c',
    )
    add_project_arguments(
      '-DLIBRDKAFKACPP_EXPORTS',
      language: 'cpp',
    )
  endif
  # hack for upstream bug
  if cpp.get_argument_syntax() == 'msvc'
    add_project_arguments(
      '-D_Thread_local=',
      language: 'c',
    )
  endif
endif

conf.set('BUILT_WITH', built_with)
configure_file(
  configuration: conf,
  input: 'packaging/cmake/config.h.in',
  output: 'config.h',
  format: 'cmake',
)

rdkafka_deps = [
  math,
  regex,
  threads,
  dl,
  cjson,
  zlib,
  zstd,
  sasl,
  ssl,
  lz4,
  curl,
]
if host_machine.system() == 'windows'
  rdkafka_deps += [cpp.find_library('ws2_32'), cpp.find_library('iphlpapi')]
  rdkafka_deps += cpp.find_library(
    'crypt32',
    required: get_option('WITH_SSL'),
  )
  rdkafka_deps += cpp.find_library(
    'secur32',
    required: get_option('WITH_SASL'),
  )
endif

rdkafka = library(
  'rdkafka',
  srcc,
  install: true,
  dependencies: rdkafka_deps,
  include_directories: include_directories('src'),
)

depinc = include_directories('include-workaround-meson')
rdkafka_dep = declare_dependency(
  link_with: rdkafka,
  include_directories: depinc,
  dependencies: rdkafka_deps,
)

pkgconfig.generate(
  rdkafka,
  subdirs: 'rdkafka',
  version: meson.project_version(),
  name: 'rdkafka',
  filebase: 'rdkafka',
  description: 'The Apache Kafka C/C++ library',
)

rdkafkapp = library(
  'rdkafka++',
  srccpp,
  install: true,
  dependencies: rdkafka_dep,
)

rdkafkapp_dep = declare_dependency(
  link_with: rdkafkapp,
  include_directories: depinc,
  dependencies: rdkafka_dep,
)

pkgconfig.generate(
  rdkafkapp,
  subdirs: 'rdkafka',
  version: meson.project_version(),
  name: 'rdkafka++',
  filebase: 'rdkafka',
  description: 'The Apache Kafka C/C++ library',
)

subdir('examples')
subdir('tests')
