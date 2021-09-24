project('flac', 'c', version: '1.3.3')

cc = meson.get_compiler('c')

add_project_arguments('-DHAVE_CONFIG_H', language: 'c')

ogg_dep = dependency('ogg')
m_dep = cc.find_library('m', required: false)

cdata = configuration_data()

check_headers = [
  ['HAVE_BYTESWAP_H', 'byteswap.h'],
  ['HAVE_CPUID_H', 'cpuid.h'],
  ['HAVE_INTTYPES_H', 'inttypes.h'],
  ['HAVE_MEMORY_H', 'memory.h'],
  ['HAVE_STDINT_H', 'stdint.h'],
  ['HAVE_STDLIB_H', 'stdlib.h'],
  ['HAVE_STRING_H', 'string.h'],
  ['HAVE_SYS_IOCTL_H', 'sys/ioctl.h'],
  ['HAVE_SYS_PARAM_H', 'sys/param.h'],
  ['HAVE_SYS_STAT_H', 'sys/stat.h'],
  ['HAVE_SYS_TYPES_H', 'sys/types.h'],
  ['HAVE_TERMIOS_H', 'termios.h'],
  ['HAVE_UNISTD_H', 'unistd.h'],
  ['HAVE_X86INTRIN_H', 'x86intrin.h'],
]

foreach h : check_headers
  if cc.has_header(h.get(1))
    cdata.set(h.get(0), 1)
  endif
endforeach

cdata.set10('CPU_IS_BIG_ENDIAN', host_machine.endian() == 'big')
cdata.set10('CPU_IS_LITTLE_ENDIAN', host_machine.endian() == 'little')
cdata.set10('OGG_FOUND', ogg_dep.found())
cdata.set10('FLAC__HAS_X86INTRIN', cc.has_header('x86intrin.h'))
cdata.set('FLAC__SYS_DARWIN', host_machine.system() == 'darein')
cdata.set('FLAC__SYS_LINUX', host_machine.system() == 'linux')
cdata.set10('HAVE_CLOCK_GETTIME', cc.has_function('clock_gettime', prefix: '#include<time.h>'))
cdata.set10('HAVE_FSEEKO', cc.has_function('fseeko', prefix: '#include<stdio.h>'))
cdata.set10('HAVE_GETOPT_LONG', cc.has_function('getopt_long', prefix: '#include<getopt.h>'))
cdata.set10('HAVE_LROUND', cc.has_function('lround', prefix: '#include<math.h>'))

cdata.set('SIZEOF_OFF_T', cc.sizeof('off_t'))
cdata.set('SIZEOF_VOIDP', cc.sizeof('void*'))

configure_file(input: 'config.h.meson',
    output: 'config.h',
    configuration: cdata)

main_inc = include_directories('include', '.')

subdir('src')

flac_dep = declare_dependency(include_directories: 'include',
    link_with: flac_lib)
