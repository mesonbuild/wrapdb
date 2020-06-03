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
  license : 'MIT',
  version : '2.2.9',
  meson_version : '>= 0.50.0',
)

config = configuration_data()
cc = meson.get_compiler('c')

# Define how much context to retain around the current parse point.
config.set('XML_CONTEXT_BYTES', 1024)

dep_libbsd = dependency('libbsd', required : get_option('use_libbsd'))
if dep_libbsd.found()
  config.set('HAVE_LIBBSD', true)
endif

if dep_libbsd.found()
  header = 'bsd/stdlib.h'
else
  header = 'stdlib.h'
endif

if cc.has_header_symbol(header, 'arc4random_buf')
  config.set('HAVE_ARC4RANDOM_BUF', true)
elif cc.has_header_symbol(header, 'arc4random')
  config.set('HAVE_ARC4RANDOM', true)
endif

if get_option('xml_dtd')
  config.set('XML_DTD', true)
endif
if get_option('xml_ns')
  config.set('XML_NS', true)
endif

foreach h : ['dlfcn', 'fcntl', 'inttypes', 'memory', 'stdint', 'stdlib',
             'strings', 'string', 'sys/stat', 'sys/types', 'unistd']
  if cc.has_header(h + '.h')
    config.set('HAVE_@0@_H'.format(h.underscorify().to_upper()), true)
  endif
endforeach

_stdc = true
foreach h : ['stdlib', 'stdarg', 'string', 'float']
  if not cc.has_header('@0@.h'.format(h))
    _stdc = false
    break
  endif
endforeach
if _stdc
  config.set('STDC_HEADERS', true)
endif

foreach f : ['getpagesize', 'mmap', 'getrandom']
  if cc.has_function(f)
    config.set('HAVE_@0@'.format(f.to_upper()), true)
  endif
endforeach

if host_machine.endian() == 'little'
  config.set('BYTEORDER', 1234)
else
  config.set('BYTEORDER', 4321)
endif


if not (config.get('HAVE_SYS_TYPES_H', false) and
        cc.has_header_symbol('sys/types.h', 'off_t'))
  config.set('off_t', 'long')
endif
if not (config.get('HAVE_SYS_TYPES_H', false) and
        cc.has_header_symbol('sys/types.h', 'size_t'))
  config.set('size_t', 'unsigned')
endif

if cc.compiles('''
      #include <stdlib.h>       /* for NULL */
      #include <unistd.h>       /* for syscall */
      #include <sys/syscall.h>  /* for SYS_getrandom */
      int main() {
        syscall(SYS_getrandom, NULL, 0, 0);
        return 0;
      }''',
      name : 'SYS_getrandom',
    )
  config.set('HAVE_SYSCALL_GETRANDOM', true)
endif

# Install headers
config_h = configure_file(
  configuration : config,
  output : 'expat_config.h',
  install_dir : get_option('includedir'),
  install : true,
)
install_headers('lib/expat.h', 'lib/expat_external.h')

# pkg-config file
pkgdata = configuration_data()
pkgdata.set('prefix', get_option('prefix'))
pkgdata.set('exec_prefix', get_option('prefix'))
pkgdata.set('libdir', '${prefix}/' + get_option('libdir'))
pkgdata.set('includedir', '${prefix}/' + get_option('includedir'))
pkgdata.set('PACKAGE_VERSION', meson.project_version())

configure_file(
  input : 'expat.pc.in',
  output : 'expat.pc',
  configuration : pkgdata,
  install_dir : join_paths(get_option('libdir'), 'pkgconfig'),
  install: true
)

add_project_arguments('-DHAVE_EXPAT_CONFIG_H', language : ['c'])
if cc.has_argument('-fno-strict-aliasing')
  add_project_arguments('-fno-strict-aliasing', language : ['c'])
endif
if cc.get_id() == 'msvc'
  add_project_arguments('-D_CRT_SECURE_NO_WARNINGS', '-wd4996', language : ['c'])
  if get_option('default_library') == 'static'
    add_project_arguments('-DXML_STATIC', language : ['c'])
  endif
endif
if not ['windows', 'cygwin'].contains(host_machine.system())
  if get_option('use_dev_urandom')
    add_project_arguments('-DXML_DEV_URANDOM', language : ['c'])
  endif
endif

_files = [
  files(
    'lib/xmlparse.c',
    'lib/xmlrole.c',
    'lib/xmltok.c',
  ),
  config_h,
]

# the lib/libexpat.def file is not valid with mingw, only with mvsc, intel-cl,
# and clang-cl
if cc.get_id() != 'gcc'
  libexpat = library(
    'expat',
    _files,
    vs_module_defs : 'lib/libexpat.def',
    include_directories : include_directories('lib'),
    dependencies : dep_libbsd,
    version : '1.6.11',
    soversion : host_machine.system() != 'windows' ? '1' : '',
    install : true,
    gnu_symbol_visibility : 'hidden',
  )
else
  libexpat = library(
    'expat',
    _files,
    include_directories : include_directories('lib'),
    dependencies : dep_libbsd,
    version : '1.6.11',
    soversion : host_machine.system() != 'windows' ? '1' : '',
    install : true,
    gnu_symbol_visibility : get_option('build_tests') ? 'default' : 'hidden',
  )
endif

expat_dep = declare_dependency(
  sources : config_h,
  link_with : libexpat,
  include_directories : include_directories('lib'),
)

if get_option('build_tests')
  add_languages('cpp')

  libtest = static_library(
    'libtest',
    [
      'tests/chardata.c',
      'tests/memcheck.c',
      'tests/minicheck.c',
      'tests/structdata.c',
    ],
    include_directories : include_directories('lib'),
  )

  test(
    'runtests',
    executable(
      'runtests',
      'tests/runtests.c',
      include_directories : include_directories('lib'),
      link_with : [libtest, libexpat],
    )
  )
  test(
    'runtestspp',
    executable(
      'runtestspp',
      'tests/runtestspp.cpp',
      include_directories : include_directories('lib'),
      link_with : [libtest, libexpat],
    )
  )
endif

# TODO: tools, examples, tests, docs
# These are probably not necessary for a wrap, but someone might have use for
# them
