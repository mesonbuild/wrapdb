project('cmph', 'c', version: '2.0', license: ['LGPL-2', 'MPL-1.1'])

cc = meson.get_compiler('c')

add_project_arguments('-DHAVE_CONFIG_H', language: 'c')

cdata = configuration_data()

check_headers = [
  ['HAVE_DLFCN_H', 'dlfcn.h'],
  ['HAVE_GETOPT_H', 'getopt.h'],
  ['HAVE_INTTYPES_H', 'inttypes.h'],
  ['HAVE_MATH_H', 'math.h'],
  ['HAVE_MEMORY_H', 'memory.h'],
  ['HAVE_STDINT_H', 'stdint.h'],
  ['HAVE_STDLIB_H', 'stdlib.h'],
  ['HAVE_STRINGS_H', 'strings.h'],
  ['HAVE_STRING_H', 'string.h'],
  ['HAVE_SYS_STAT_H', 'sys/stat.h'],
  ['HAVE_SYS_TYPES_H', 'sys/types.h'],
  ['HAVE_UNISTD_H', 'unistd.h'],
]

foreach h : check_headers
  if cc.has_header(h.get(1))
    cdata.set(h.get(0), 1)
  endif
endforeach

cdata.set_quoted('PACKAGE_NAME', meson.project_name())
cdata.set_quoted('PACKAGE_URL', 'https://sourceforge.net/projects/cmph/')
cdata.set_quoted('PACKAGE_BUGREPORT', 'https://sourceforge.net/p/cmph/bugs/')
cdata.set_quoted('VERSION', meson.project_version())
cdata.set10('_LARGEFILE_SOURCE', cc.has_function('fseeko', prefix: '#define _LARGEFILE_SOURCE\n#include<stdio.h>'))

if host_machine.system() != 'windows'
  cdata.set('_FILE_OFFSET_BITS', 64)
else
  add_project_arguments([
      # XXX the "standard" macro on Windows is _WIN32 but cmph expects spelling without underscore
      '-DWIN32',
      # XXX The usual set of Microsoft CRT flags for POSIX code
      '-D_CRT_SECURE_NO_DEPRECATE',
      '-D_CRT_NONSTDC_NO_DEPRECATE',
    ],
    language: 'c'
  )
endif

add_project_arguments(cc.get_supported_arguments([
    # XXX harmful warnings which break -Werror builds of parent projects
    '-Wno-unused-function',
    '-Wno-unused-but-set-variable',
  ]),
  language: 'c'
)

configure_file(
  input: 'config.h.meson',
  output: 'config.h',
  configuration: cdata,
)

subdir('src')
cmph_dep = declare_dependency(
  include_directories: 'src',
  link_with: cmph_lib,
)

pkgconfig_cdata = configuration_data({
  'prefix': get_option('prefix'),
  'exec_prefix': get_option('prefix'),
  'libdir': '${prefix}/' + get_option('libdir'),
  'includedir': '${prefix}/' + get_option('includedir'),
  'VERSION': meson.project_version(),
})
configure_file(
  input: 'cmph.pc.in',
  output: 'cmph.pc',
  configuration: pkgconfig_cdata,
  install_dir: join_paths(get_option('libdir'), 'pkgconfig'),
  install: true,
)

if get_option('build_tests')
  subdir('tests')
endif
