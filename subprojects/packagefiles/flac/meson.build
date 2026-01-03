project(
  'flac',
  'c',
  version: '1.5.0',
  meson_version: '>=0.56',
  license: 'BSD-3-Clause',
)

cc = meson.get_compiler('c')

add_project_arguments(
  '-DHAVE_CONFIG_H',
  language: 'c',
)
if host_machine.system() == 'darwin'
  add_project_arguments(
    '-D_DARWIN_C_SOURCE',
    language: 'c',
  )
endif

if cc.get_argument_syntax() == 'msvc'
  add_project_arguments(
    '-D_CRT_SECURE_NO_WARNINGS',
    cc.get_supported_arguments('-Wno-deprecated-declarations'),
    language: 'c',
  )
endif

ogg_dep = dependency('ogg')
m_dep = cc.find_library(
  'm',
  required: false,
)
if meson.version().version_compare('>= 0.60')
  iconv_dep = dependency(
    'iconv',
    required: false,
  )
elif cc.links('#include <iconv.h>\nint main(){iconv_open("", "");}')
  iconv_dep = declare_dependency()
else
  iconv_dep = cc.find_library(
    'iconv',
    required: false,
  )
endif

cdata = configuration_data()

cheaders = [
  'byteswap.h',
  'inttypes.h',
  'memory.h',
  'stdint.h',
  'stdlib.h',
  'string.h',
  'sys/ioctl.h',
  'sys/param.h',
  'sys/stat.h',
  'sys/types.h',
  'termios.h',
  'unistd.h',
]

foreach h : cheaders
  cdata.set('HAVE_' + h.underscorify().to_upper(), cc.has_header(h))
endforeach

cdata.set('HAVE_CPUID_H', cc.check_header('cpuid.h'))
cdata.set('HAVE_X86INTRIN_H', cc.check_header('x86intrin.h'))
cdata.set10('FLAC__HAS_NEONINTRIN', cc.check_header('arm_neon.h'))
cdata.set10(
  'FLAC__HAS_A64NEONINTRIN',
  cc.check_header('arm_neon.h') and host_machine.cpu_family() == 'aarch64',
)
cdata.set('FLAC__USE_ALTIVEC', cc.check_header('altivec.h'))
cdata.set('WITH_AVX', cc.check_header('immintrin.h'))

cdata.set('PROJECT_VERSION', meson.project_version())
cdata.set10('CPU_IS_BIG_ENDIAN', host_machine.endian() == 'big')
cdata.set10('CPU_IS_LITTLE_ENDIAN', host_machine.endian() == 'little')
cdata.set('FLAC__CPU_ARM64', host_machine.cpu_family() == 'aarch64')
cdata.set('FLAC__CPU_PPC', host_machine.cpu_family() == 'ppc')
cdata.set('FLAC__CPU_PPC64', host_machine.cpu_family() == 'ppc64')
cdata.set('FLAC__ALIGN_MALLOC_DATA', host_machine.cpu_family() == 'x86_64')
cdata.set10('FLAC__HAS_X86INTRIN', cdata.get('HAVE_X86INTRIN_H'))
cdata.set('FLAC__SYS_DARWIN', host_machine.system() == 'darwin')
cdata.set('FLAC__SYS_LINUX', host_machine.system() == 'linux')
cdata.set10('OGG_FOUND', ogg_dep.found())
cdata.set('HAVE_ICONV', iconv_dep.found())
cdata.set10('HAVE_CLOCK_GETTIME', cc.has_function('clock_gettime'))
cdata.set10('HAVE_FSEEKO', cc.has_function('fseeko'))
cdata.set10('HAVE_GETOPT_LONG', cc.has_function('getopt_long'))
cdata.set10(
  'HAVE_LROUND',
  cc.has_function(
    'lround',
    dependencies: m_dep,
  ),
)
cdata.set('HAVE_BSWAP16', cc.has_function('__builtin_bswap16'))
cdata.set('HAVE_BSWAP32', cc.has_function('__builtin_bswap32'))

cdata.set('SIZEOF_OFF_T', cc.sizeof('off_t'))
cdata.set('SIZEOF_VOIDP', cc.sizeof('void*'))

configure_file(
  input: 'config.cmake.h.in',
  output: 'config.h',
  format: 'cmake@',
  configuration: cdata,
)

main_inc = include_directories('include', '.')

win32_utf8 = host_machine.system() == 'windows' ? files(
  'src/share/win_utf8_io/win_utf8_io.c',
) : []

subdir('src')

install_headers(
  'include/FLAC/all.h',
  'include/FLAC/assert.h',
  'include/FLAC/callback.h',
  'include/FLAC/export.h',
  'include/FLAC/format.h',
  'include/FLAC/metadata.h',
  'include/FLAC/ordinals.h',
  'include/FLAC/stream_decoder.h',
  'include/FLAC/stream_encoder.h',
  subdir: 'FLAC',
)
