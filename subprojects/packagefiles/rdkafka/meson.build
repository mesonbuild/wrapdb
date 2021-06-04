project('rdkafka', 'c', 'cpp', version: '1.5.2')
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

regex = cc.compiles('''
	#include <stddef.h>
	#include <regex.h>
	void foo (void) {
		regcomp(NULL, NULL, 0);
		regexec(NULL, NULL, 0, NULL, 0);
		regerror(0, NULL, NULL, 0);
		regfree(NULL);
	}
''', name: 'have regex')

zlib = dependency('zlib', required: get_option('WITH_ZLIB'), static: get_option('default_library') == 'static', fallback: ['zlib', 'zlib_dep'])
zstd = dependency('libzstd', required: get_option('WITH_ZSTD'), static: get_option('default_library') == 'static', fallback: ['zstd', 'zstd_dep'])
lz4 = dependency('liblz4', required: get_option('ENABLE_LZ4_EXT'), static: get_option('default_library') == 'static', fallback: ['lz4', 'lz4_dep'])
sasl = dependency('libsasl2', required: get_option('WITH_SASL'), static: get_option('default_library') == 'static') # TODO: make SASL usable without libsasl2 on windows 
ssl = dependency('openssl', required: get_option('WITH_SSL'), static: get_option('default_library') == 'static')
dl = cc.find_library('dl', required : get_option('WITH_LIBDL'))
threads = dependency('threads')

conf = configuration_data()

conf.set10('WITHOUT_OPTIMIZATION', get_option('WITHOUT_OPTIMIZATION'))
conf.set10('ENABLE_DEVEL', get_option('ENABLE_DEVEL'))
conf.set10('ENABLE_REFCNT_DEBUG', get_option('ENABLE_REFCNT_DEBUG'))
conf.set10('ENABLE_SHAREDPTR_DEBUG', get_option('ENABLE_SHAREDPTR_DEBUG'))
conf.set10('WITH_PLUGINS', dl.found())
conf.set10('WITH_LIBDL', dl.found())
conf.set10('WITH_ZLIB', zlib.found())
conf.set10('WITH_ZSTD', zstd.found())
conf.set10('WITH_SSL', ssl.found())
conf.set10('WITH_SASL', sasl.found())
conf.set10('ENABLE_LZ4_EXT', lz4.found())
conf.set10('HAVE_REGEX', regex)
conf.set('CMAKE_SHARED_LIBRARY_SUFFIX', 'so')

built_with = 'meson ' + cc.get_id() + ' ' + cpp.get_id()
if ssl.found()
	built_with += ' SSL'
	srcc += 'src/rdkafka_ssl.c'
endif
if dl.found()
	srcc += ['src/rddl.c', 'src/rdkafka_plugin.c']
	built_with += ' LIBDL PLUGINS'
endif
if sasl.found()
  if host_machine.system() == 'windows'
	srcc += 'src/rdkafka_sasl_win32.c'
  else
	srcc += 'src/rdkafka_sasl_cyrus.c'
	conf.set10('WITH_SASL_CYRUS', true)
	built_with += ' SASL_CYRUS'
  endif
  if ssl.found()
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
if lz4.found()
	srcc += ['src/lz4.c', 'src/lz4frame.c', 'src/lz4hc.c']
	built_with += ' LZ4'
endif
if not regex
	srcc += 'src/regexp.c'
endif

conf.set('BUILT_WITH', built_with)
configure_file(configuration: conf,
	input: 'packaging/cmake/config.h.in',
	output: 'config.h',
	format: 'cmake',
)

rdkafka = library('rdkafka', srcc, install: true, dependencies: [threads, dl, zlib, zstd, sasl, ssl, lz4])
rdkafka_dep = declare_dependency(
	link_with: rdkafka,
	include_directories: include_directories('include-workaround-meson'),
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
)
pkgconfig.generate(rdkafkapp,
	subdirs: 'rdkafka',
	version: meson.project_version(),
	name: 'rdkafka++',
	filebase: 'rdkafka',
	description: 'The Apache Kafka C/C++ library'
)
