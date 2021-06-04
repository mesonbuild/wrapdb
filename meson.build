project('libsrtp2', 'c', version: '2.2.0', license: 'BSD-3-Clause')

config = configuration_data()

config.set_quoted('PACKAGE_STRING', meson.project_name())
config.set_quoted('PACKAGE_VERSION', meson.project_version())

if host_machine.cpu_family() in [ 'x86', 'x86_64' ]
  config.set('CPU_CISC', 1,
    description: 'Define if building for a CISC machine (e.g. Intel).')
  config.set('HAVE_X86', 1,
    description: 'Define to use X86 inlined assembly code')
else
  config.set('CPU_RISC', 1,
    description: 'Define if building for a RISC machine (assume slow byte access).')
endif

cc = meson.get_compiler('c')

check_headers = [
  'byteswap.h',
  'inttypes.h',
  'stdint.h',
  'stdlib.h',
  'unistd.h',
  'arpa/inet.h',
  'machine/types.h',
  'netinet/in.h',
  'sys/socket.h',
  'sys/types.h',
  'sys/uio.h',
  'sys/int_types.h',
]

if host_machine.system() == 'windows'
  check_headers += [
    'windows.h',
    'winsock2.h',
  ]
endif

foreach h: check_headers
  if cc.has_header(h)
    config.set('HAVE_' + h.underscorify().to_upper(), 1)
  endif
endforeach

check_types = [
  'int8_t',
  'uint8_t',
  'int16_t',
  'uint16_t',
  'int32_t',
  'uint32_t',
  'uint64_t',
]

foreach t: check_types
  if cc.has_type(t, prefix: '#include <stdint.h>')
    config.set('HAVE_' + t.to_upper(), 1)
  endif
endforeach

foreach t: [ 'unsigned long', 'unsigned long long' ]
  config.set('SIZEOF_' + t.underscorify().to_upper(), cc.sizeof(t))
endforeach

foreach f: [ 'socket', 'inet_aton', 'usleep', 'sigaction' ]
  if cc.has_function(f)
    config.set('HAVE_' + f.to_upper(), 1)
  endif
endforeach

config.set('ENABLE_DEBUG_LOGGING', get_option('debug-logging'),
  description: 'Define to enabled debug logging for all mudules.')

libcrypto_dep = dependency('libcrypto', required: get_option('openssl'),
  fallback: [ 'openssl', 'openssl_dep' ])
if libcrypto_dep.found()
  add_project_arguments('-DOPENSSL', language : 'c')
endif

srtp2_deps = [ libcrypto_dep ]

if host_machine.system() == 'windows'
  srtp2_deps += [ cc.find_library('ws2_32') ]
endif

configure_file(output: 'config.h', configuration: config)
add_project_arguments('-DHAVE_CONFIG_H', language: 'c')

subdir('srtp')
subdir('srtp2')
subdir('test')
subdir('crypto/test')
