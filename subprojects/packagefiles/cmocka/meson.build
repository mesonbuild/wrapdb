# Copyright © 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

project(
  'cmocka',
  'c',
  version: '1.1.7',
  license: 'APLv2',
  meson_version: '>= 0.54.1',
  default_options: ['c_std=c99', 'buildtype=debugoptimized'],
)

lib_version = '0.8.0'

inc_include = include_directories('include')

#####################
# Config Generation #
#####################

cc_dict = {
  'compiler': meson.get_compiler('c'),
  'machine': host_machine,
  'native': false,
}

cc_native_dict = {
  'compiler': meson.get_compiler('c', native: true),
  'machine': build_machine,
  'native': true,
}

entry = cc_dict
compiler = entry.get('compiler')
is_native = entry.get('native')
machine = entry.get('machine')

config = configuration_data()

if compiler.get_argument_syntax() == 'gcc'
  add_project_arguments(
    # I've explicitly skipped the duplicated -W versions when they also test
    # for the -Werror version
    compiler.get_supported_arguments(
      '-Wshadow',
      '-Wmissing-prototypes',
      '-Wcast-align',
      '-Werror=address',
      '-Werror=strict-prototypes',
      '-Werror=write-strings',
      '-Werror=implicit-function-declaration',
      '-Werror=pointer-arith',
      '-Werror=declaration-after-statement',
      '-Werror=return-type',
      '-Werror=uninitialized',
      '-Wimplicit-fallthrough',
      '-Werror=strict-overflow',
      '-Wstrict-overflow=2',
      '-Wno-format-zero-length',
      '-Wformat',
      '-Werror=format-security',
      '-Wno-gnu-zero-variadic-macro-arguments',
      '-D_GNU_SOURCE',
    ),
    language: 'c',
    native: is_native,
  )
  # We can't test the build type, so we can' add -D_FORTIFY_SOURCE=2 here
  if machine.system() == 'darwin'
    add_project_arguments(
      compiler.get_supported_arguments('-Wno-deprecated-declarations'),
      language: 'c',
      native: is_native,
    )
  endif
else
  add_project_arguments(
    '/D_CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES=1',
    '/D_CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES_COUNT=1',
    '/D_CRT_NONSTDC_NO_WARNINGS=1',
    '/D_CRT_SECURE_NO_WARNINGS=1',
    language: 'c',
    native: is_native,
  )
endif

# TODO: solaris extensions

foreach h : [
  'assert.h',
  'dlfcn.h',
  'inttypes.h',
  'io.h',
  'malloc.h',
  'memory.h',
  'setjmp.h',
  'signal.h',
  'stdarg.h',
  'stddef.h',
  'stdint.h',
  'stdio.h',
  'stdlib.h',
  'string.h',
  'strings.h',
  'sys/stat.h',
  'sys/types.h',
  'time.h',
  'unistd.h',
]
  if compiler.check_header(h)
    config.set('HAVE_@0@'.format(h.underscorify().to_upper()), 1)
  endif
endforeach

if compiler.has_member('struct timespec', 'tv_sec', prefix: '#include <time.h>')
  config.set('HAVE_STRUCT_TIMESPEC', 1)
endif

foreach f : [
  'calloc',
  'clock_gettime',
  'exit',
  'free',
  'longjmp',
  'malloc',
  'memcpy',
  'memset',
  'setjmp',
  'siglongjmp',
  'signal',
  'strsignal',
  'strcmp',
]
  if compiler.has_function(f)
    config.set('HAVE_@0@'.format(f.underscorify().to_upper()), 1)
  endif
endforeach

foreach f : ['fprintf', 'printf', 'snprintf', 'vsnprintf']
  if compiler.has_header_symbol('stdio.h', f)
    config.set('HAVE_@0@'.format(f.underscorify().to_upper()), 1)
  endif
endforeach

threads_dep = []
if not config.has('HAVE_CLOCK_GETTIME')
  if compiler.has_function('clock_gettime', dependencies: dependency('threads'))
    config.set('HAVE_@0@'.format(f.underscorify().to_upper()), 1)
    threads_dep = dependency('threads')
  endif
endif

if compiler.get_argument_syntax() == 'msvc'
  config.set('HAVE_MSVC_THREAD_LOCAL_STORAGE', compiler.compiles('__declspec(thread) int tls;'))
else
  config.set10('HAVE_GCC_THREAD_LOCAL_STORAGE', compiler.compiles('__thread int tls;'))
endif

config.set('WORDS_SIZEOF_VOID_P', compiler.sizeof('void*'))
if machine.endian() == 'big'
  config.set('WORDS_BIGENDIAN', 1)
endif

cfile = configure_file(
  input: 'config.h.cmake',
  output: 'config.h',
  format: 'cmake',
  configuration: config,
)

###########################
# Subdirectory Processing #
###########################

libcmocka = library(
  'cmocka',
  'src/cmocka.c',
  c_args: '-DHAVE_CONFIG_H=1',
  include_directories: inc_include,
  vs_module_defs: 'src/cmocka.def',
  soversion: host_machine.system() != 'windows' ? lib_version.split('.')[0] : '',
  version: lib_version,
  dependencies: threads_dep,
  install: true,
)

libcmocka_native = library(
  'cmocka_native',
  'src/cmocka.c',
  c_args: '-DHAVE_CONFIG_H=1',
  include_directories: inc_include,
  vs_module_defs: 'src/cmocka.def',
  soversion: build_machine.system() != 'windows' ? lib_version.split('.')[0] : '',
  version: lib_version,
  dependencies: threads_dep,
  install: false, # Cannot install native targets in cross builds
  native: true,
  build_by_default: false,
)

######################
# Dependency Targets #
######################

# TODO: doc, include, tests, example
# Since we're using this as a wrap, and it's a unit test framework we're not
# going to install it.

cmocka_dep = declare_dependency(
  link_with: libcmocka,
  include_directories: inc_include,
  version: meson.project_version(),
)

cmocka_native_dep = declare_dependency(
  link_with: libcmocka_native,
  include_directories: inc_include,
  version: meson.project_version(),
)
