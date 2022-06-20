project('rdkafka', 'c', 'cpp', version: '1.9.0', default_options: ['cpp_std=c++17', 'c_std=c11'])
cc = meson.get_compiler('c')
cpp = meson.get_compiler('cpp')
pkgconfig = import('pkgconfig')

hdr = files(
  'src/rdkafka.h',
  'src-cpp/rdkafkacpp.h',
)
subdir('include-workaround-meson/librdkafka')
srcc = [
  'src/crc32c.c',
  'src/rdaddr.c',
  'src/rdavl.c',
  'src/rdbuf.c',
  'src/rdcrc32.c',
  'src/rdfnv1a.c',
  'src/rdkafka.c',
  'src/rdkafka_assignment.c',
  'src/rdkafka_assignor.c',
  'src/rdkafka_broker.c',
  'src/rdkafka_buf.c',
  'src/rdkafka_cgrp.c',
  'src/rdkafka_conf.c',
  'src/rdkafka_event.c',
  'src/rdkafka_feature.c',
  'src/rdkafka_lz4.c',
  'src/rdkafka_metadata.c',
  'src/rdkafka_metadata_cache.c',
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
  'src/rdkafka_timer.c',
  'src/rdkafka_topic.c',
  'src/rdkafka_transport.c',
  'src/rdkafka_interceptor.c',
  'src/rdkafka_header.c',
  'src/rdkafka_admin.c',
  'src/rdkafka_aux.c',
  'src/rdkafka_background.c',
  'src/rdkafka_idempotence.c',
  'src/rdkafka_txnmgr.c',
  'src/rdkafka_cert.c',
  'src/rdkafka_coord.c',
  'src/rdkafka_mock.c',
  'src/rdkafka_mock_handlers.c',
  'src/rdkafka_mock_cgrp.c',
  'src/rdkafka_error.c',
  'src/rdlist.c',
  'src/rdmap.c',
  'src/rdlog.c',
  'src/rdmurmur2.c',
  'src/rdports.c',
  'src/rdrand.c',
  'src/rdregex.c',
  'src/rdstring.c',
  'src/rdunittest.c',
  'src/rdvarint.c',
  'src/snappy.c',
  'src/tinycthread.c',
  'src/tinycthread_extra.c',
  'src/rdxxhash.c',
  'src/cJSON.c',
]
srccpp = [
  'src-cpp/ConfImpl.cpp',
  'src-cpp/ConsumerImpl.cpp',
  'src-cpp/HeadersImpl.cpp',
  'src-cpp/KafkaConsumerImpl.cpp',
  'src-cpp/MessageImpl.cpp',
  'src-cpp/MetadataImpl.cpp',
  'src-cpp/ProducerImpl.cpp',
  'src-cpp/QueueImpl.cpp',
  'src-cpp/RdKafka.cpp',
  'src-cpp/TopicImpl.cpp',
  'src-cpp/TopicPartitionImpl.cpp',
  'src-cpp/HandleImpl.cpp',
  'src-cpp/rdkafkacpp.h',
  'src-cpp/rdkafkacpp_int.h',
]

cjson = dependency('libcjson')
curl = dependency('libcurl', required: get_option('WITH_CURL'))
zlib = dependency('zlib', required: get_option('WITH_ZLIB'))
zstd = dependency('libzstd', required: get_option('WITH_ZSTD'))
lz4 = dependency('liblz4', required: get_option('WITH_LZ4_EXT'))
sasl = dependency('libsasl2', required: get_option('WITH_SASL')) # TODO: make SASL usable without libsasl2 on windows 
ssl = dependency('libssl', required: get_option('WITH_SSL'))
crypto = dependency('libcrypto', required: get_option('WITH_SSL'))
dl = dependency('dl', required : get_option('WITH_LIBDL'))
threads = dependency('threads')
math = cc.find_library('m', required : false)

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
conf.set10('WITH_SSL', ssl.found() and crypto.found())
conf.set10('WITH_SASL', sasl.found())
conf.set10('WITH_SASL_CYRUS', sasl.found())
conf.set10('WITH_LZ4_EXT', lz4.found())
conf.set10('HAVE_REGEX', cc.has_function('regcomp'))
conf.set10('HAVE_STRNDUP', cc.has_function('strndup'))
conf.set10('HAVE_RAND_R', cc.has_function('rand_r'))
conf.set10('WITH_C11THREADS', cc.has_function('thrd_create'))
conf.set('CMAKE_SHARED_LIBRARY_SUFFIX', 'so')

add_project_arguments('-DWITHOUT_WIN32_CONFIG', language: 'c')
if host_machine.system() == 'windows'
  add_project_arguments('-DENABLE_DEVEL=@0@'.format(conf.get('ENABLE_DEVEL')), language: 'c')
  add_project_arguments('-DWITH_SSL=@0@'.format(conf.get('WITH_SSL')), language: 'c')
  if get_option('buildtype') != 'static'
    add_project_arguments('-DLIBRDKAFKACPP_EXPORTS', language: 'cpp')
  endif
endif

# hack for upstream bug
if cpp.get_argument_syntax() == 'msvc'
  add_project_arguments('-D_Thread_local= ', language: 'c')
endif

built_with = 'meson ' + cc.get_id() + ' ' + cpp.get_id()
if ssl.found() and crypto.found()
  built_with += ' SSL'
  srcc += 'src/rdkafka_ssl.c'
endif
if dl.found()
  srcc += ['src/rddl.c', 'src/rdkafka_plugin.c']
  built_with += ' LIBDL PLUGINS'
endif
if host_machine.system() == 'windows'
  srcc += 'src/rdkafka_sasl_win32.c'
elif sasl.found()
  srcc += 'src/rdkafka_sasl_cyrus.c'
  built_with += ' SASL_CYRUS'
  if ssl.found() and crypto.found()
    srcc += [ 'src/rdkafka_sasl_scram.c', 'src/rdkafka_sasl_oauthbearer.c']
    conf.set10('WITH_SASL_SCRAM', true)
    conf.set10('WITH_SASL_OAUTHBEARER', true)
    built_with += ' SASL_SCRAM SASL_OAUTHBEARER'
  endif
endif

if zlib.found()
  srcc += 'src/rdgz.c'
  built_with += ' ZLIB'
endif
if zstd.found()
  srcc += 'src/rdkafka_zstd.c'
  built_with += ' ZSTD'
endif
if not lz4.found()
  srcc += ['src/lz4.c', 'src/lz4frame.c', 'src/lz4hc.c']
  built_with += ' LZ4'
endif
if curl.found()
  srcc += 'src/rdhttp.c'
endif
if conf.get('HAVE_REGEX') == 0
  srcc += 'src/regexp.c'
endif
if get_option('ENABLE_HDRHISTOGRAM')
  srcc += 'src/rdhdrhistogram.c'
endif

conf.set('BUILT_WITH', built_with)
configure_file(configuration: conf,
  input: 'packaging/cmake/config.h.in',
  output: 'config.h',
  format: 'cmake',
)

rdkafka_deps = [math, threads, dl, cjson, zlib, zstd, sasl, ssl, crypto, lz4, curl]
if host_machine.system() == 'windows'
  rdkafka_deps += [cpp.find_library('ws2_32'), cpp.find_library('iphlpapi'), cpp.find_library('secur32')]
  if ssl.found()
    rdkafka_deps += cpp.find_library('crypt32')
  endif
endif
rdkafka = library('rdkafka', srcc, install: true, dependencies: rdkafka_deps)
rdkafka_dep = declare_dependency(
  link_with: rdkafka,
  include_directories: include_directories('include-workaround-meson'),
  dependencies: rdkafka_deps,
)
pkgconfig.generate(rdkafka,
  subdirs: 'rdkafka',
  version : meson.project_version(),
  name: 'rdkafka',
  filebase: 'rdkafka',
  description: 'The Apache Kafka C/C++ library'
)
rdkafkapp = library('rdkafka++', srccpp, install: true, dependencies: rdkafka_dep)
rdkafkapp_dep = declare_dependency(
  link_with: rdkafkapp,
  include_directories: include_directories('include-workaround-meson'),
  dependencies: rdkafka_dep,
)
pkgconfig.generate(rdkafkapp,
  subdirs: 'rdkafka',
  version: meson.project_version(),
  name: 'rdkafka++',
  filebase: 'rdkafka',
  description: 'The Apache Kafka C/C++ library'
)

subdir('examples')
subdir('tests')
