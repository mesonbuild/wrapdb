# Copyright © 2018 Dylan Baker
# Copyright © 2018,2020 Intel Corporation

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

project(
  'expat',
  'c',
  license: 'MIT',
  version: '2.7.3',
  meson_version: '>= 0.58',
)

dllver = '1.11.1'

config = configuration_data()
cc = meson.get_compiler('c')

config.set('PACKAGE_NAME', meson.project_name())
config.set('PACKAGE_TARNAME', meson.project_name())
config.set('PACKAGE_VERSION', meson.project_version())
config.set('PACKAGE_BUGREPORT', 'expat-bugs@libexpat.org')
config.set(
  'PACKAGE_STRING',
  '@0@ @1@'.format(meson.project_name(), meson.project_version()),
)

# Define how much context to retain around the current parse point.
config.set('XML_CONTEXT_BYTES', 1024)

dep_libbsd = dependency(
  'libbsd-overlay',
  required: get_option('use_libbsd'),
)
if dep_libbsd.type_name() == 'internal'
  config.set('HAVE_ARC4RANDOM_BUF', dep_libbsd.found())
  config.set('HAVE_ARC4RANDOM', dep_libbsd.found())
else
  config.set(
    'HAVE_ARC4RANDOM_BUF',
    cc.has_function(
      'arc4random_buf',
      dependencies: dep_libbsd,
    ),
  )
  config.set(
    'HAVE_ARC4RANDOM',
    cc.has_function(
      'arc4random',
      dependencies: dep_libbsd,
    ),
  )
endif

config.set('XML_ATTR_INFO', get_option('xml_attr_info'))
config.set('XML_DTD', get_option('xml_dtd'))
config.set10('XML_GE', get_option('xml_ge'))
config.set('XML_NS', get_option('xml_ns'))

foreach h : [
  'dlfcn',
  'fcntl',
  'inttypes',
  'memory',
  'stdint',
  'stdlib',
  'strings',
  'string',
  'sys/stat',
  'sys/types',
  'unistd',
]
  config.set(
    'HAVE_@0@_H'.format(h.underscorify().to_upper()),
    cc.has_header(h + '.h'),
  )
endforeach

_stdc = true
foreach h : ['stdlib', 'stdarg', 'string', 'float']
  if not cc.has_header('@0@.h'.format(h))
    _stdc = false
    break
  endif
endforeach
config.set('STDC_HEADERS', _stdc)

foreach f : ['getpagesize', 'mmap', 'getrandom']
  config.set('HAVE_@0@'.format(f.to_upper()), cc.has_function(f))
endforeach

if host_machine.endian() == 'little'
  config.set('BYTEORDER', 1234)
else
  config.set('BYTEORDER', 4321)
endif

if not cc.has_header_symbol('sys/types.h', 'off_t')
  config.set('off_t', 'long')
endif

config.set(
  'HAVE_SYSCALL_GETRANDOM',
  cc.has_header_symbol('sys/syscall.h', 'SYS_getrandom'),
)

# Install headers
config_h = configure_file(
  input: 'expat_config.h.cmake',
  output: 'expat_config.h',
  format: 'cmake@',
  configuration: config,
)
install_headers('lib/expat.h', 'lib/expat_external.h', config_h)

expat_static_args = []

add_project_arguments(
  '-DXML_ENABLE_VISIBILITY=1',
  language: 'c',
)
add_project_arguments(
  '-DHAVE_EXPAT_CONFIG_H',
  language: 'c',
)
add_project_arguments(
  cc.get_supported_arguments('-fno-strict-aliasing'),
  language: 'c',
)
if cc.get_argument_syntax() == 'msvc'
  add_project_arguments(
    '-D_CRT_SECURE_NO_WARNINGS',
    '-wd4996',
    language: 'c',
  )
endif

if host_machine.system() == 'windows'
  add_project_arguments(
    '-DXMLCALL=WINAPIV',
    language: 'c',
  )
  add_project_arguments(
    '-DXMLIMPORT=__declspec(dllexport)',
    language: 'c',
  )
  if get_option('default_library') == 'static'
    add_project_arguments(
      '-DXML_STATIC',
      language: 'c',
    )
    expat_static_args += '-DXML_STATIC'
  endif

  vard = configuration_data()
  vard.set('PROJECT_VERSION', meson.project_version())
  verf = configure_file(
    configuration: vard,
    format: 'cmake',
    input: 'win32/version.rc.cmake',
    output: 'version.rc',
  )
else
  add_project_arguments(
    '-DXMLIMPORT=__attribute__ ((visibility("default")))',
    language: 'c',
  )
  if get_option('use_dev_urandom')
    add_project_arguments(
      '-DXML_DEV_URANDOM',
      language: 'c',
    )
  endif
endif

defs = configuration_data()
if get_option('xml_dtd') or get_option('xml_ge')
  defs.set('_EXPAT_COMMENT_DTD_OR_GE', ' ')
else
  defs.set('_EXPAT_COMMENT_DTD_OR_GE', ';')
endif
if get_option('xml_attr_info')
  defs.set('_EXPAT_COMMENT_ATTR_INFO', ' ')
else
  defs.set('_EXPAT_COMMENT_ATTR_INFO', ';')
endif
dfile = configure_file(
  configuration: defs,
  format: 'cmake@',
  input: 'lib/libexpat.def.cmake',
  output: 'libexpat.def',
)

incdir = include_directories('lib')

sources = files('lib/xmlparse.c', 'lib/xmlrole.c', 'lib/xmltok.c')

if host_machine.system() == 'windows'
  sources += import('windows').compile_resources(
    verf,
    args: '-DVER_FILEVERSION=@0@,0'.format(
      meson.project_version().replace('.', ','),
    ),
  )
endif

libexpat = library(
  'expat',
  sources,
  include_directories: incdir,
  dependencies: dep_libbsd,
  version: dllver,
  soversion: host_machine.system() != 'windows' ? '1' : '',
  vs_module_defs: dfile,
  install: true,
  gnu_symbol_visibility: 'hidden',
)

expat_dep = declare_dependency(
  link_with: libexpat,
  include_directories: incdir,
  compile_args: expat_static_args,
)

pkg = import('pkgconfig')
pkg.generate(libexpat)

if get_option('build_tests')
  add_languages('cpp')

  libtest = static_library(
    'libtest',
    'tests/chardata.c',
    'tests/memcheck.c',
    'tests/minicheck.c',
    'tests/structdata.c',
    include_directories: incdir,
  )

  test(
    'runtests',
    executable(
      'runtests',
      'tests/runtests.c',
      include_directories: incdir,
      link_with: [libtest, libexpat],
    ),
  )
  test(
    'runtestspp',
    executable(
      'runtestspp',
      'tests/runtestspp.cpp',
      include_directories: incdir,
      link_with: [libtest, libexpat],
    ),
  )
endif

# TODO: tools, examples, tests, docs
# These are probably not necessary for a wrap, but someone might have use for
# them
