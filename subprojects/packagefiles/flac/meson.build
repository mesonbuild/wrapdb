project('flac', 'c', version: '1.3.4')

cc = meson.get_compiler('c')

add_project_arguments('-DHAVE_CONFIG_H', language: 'c')
if host_machine.system() == 'darwin'
  add_project_arguments('-D_DARWIN_C_SOURCE', language: 'c')
endif

ogg_dep = dependency('ogg')
m_dep = cc.find_library('m', required: false)

cdata = configuration_data()

check_headers = [
  'inttypes.h',
  'stdint.h',
  'string.h',
]

foreach h : check_headers
  if cc.has_header(h)
    cdata.set('HAVE_' + h.underscorify().to_upper(), 1)
  endif
endforeach

cdata.set('HAVE_BYTESWAP_H', cc.has_header('byteswap.h'))
cdata.set('HAVE_MEMORY_H', cc.has_header('memory.h'))
cdata.set('HAVE_STDLIB_H', cc.has_header('stdlib.h'))
cdata.set('HAVE_SYS_IOCTL_H', cc.has_header('sys/ioctl.h'))
cdata.set('HAVE_SYS_PARAM_H', cc.has_header('sys/param.h'))
cdata.set('HAVE_SYS_STAT_H', cc.has_header('sys/stat.h'))
cdata.set('HAVE_SYS_TYPES_H', cc.has_header('sys/types.h'))
cdata.set('HAVE_TERMIOS_H', cc.has_header('termios.h'))
cdata.set('HAVE_UNISTD_H', cc.has_header('unistd.h'))
cdata.set('HAVE_X86INTRIN_H', cc.has_header('x86intrin.h'))
cdata.set_quoted('PACKAGE_VERSION', meson.project_version())
cdata.set10('CPU_IS_BIG_ENDIAN', host_machine.endian() == 'big')
cdata.set10('CPU_IS_LITTLE_ENDIAN', host_machine.endian() == 'little')
cdata.set10('OGG_FOUND', ogg_dep.found())
cdata.set10('FLAC__HAS_X86INTRIN', cc.has_header('x86intrin.h'))
cdata.set('FLAC__SYS_DARWIN', host_machine.system() == 'darwin')
cdata.set('FLAC__SYS_LINUX', host_machine.system() == 'linux')
cdata.set10('HAVE_CLOCK_GETTIME', cc.has_function('clock_gettime', prefix: '#include<time.h>'))
cdata.set10('HAVE_FSEEKO', cc.has_function('fseeko', prefix: '#include<stdio.h>'))
cdata.set10('HAVE_GETOPT_LONG', cc.has_function('getopt_long', prefix: '#include<getopt.h>'))
cdata.set10('HAVE_LROUND', cc.has_function('lround', prefix: '#include<math.h>'))

if host_machine.cpu_family() == 'x86' or host_machine.cpu_family() == 'x86_64'
  cdata.set('HAVE_CPUID_H', cc.has_header('cpuid.h'))
endif

cdata.set('SIZEOF_OFF_T', cc.sizeof('off_t'))
cdata.set('SIZEOF_VOIDP', cc.sizeof('void*'))

configure_file(input: 'config.h.meson',
    output: 'config.h',
    configuration: cdata)

main_inc = include_directories('include', '.')

subdir('src')

flac_dep = declare_dependency(include_directories: 'include',
    link_with: flac_lib)
