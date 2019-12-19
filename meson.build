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
  ['c'],
  version : '1.1.5',
  license : 'APLv2',
  meson_version : '>= 0.48.0',
  default_options : ['c_std=c99', 'buildtype=debugoptimized'],
)

lib_version = '0.5.0'

cc = meson.get_compiler('c')

if ['gcc', 'clang'].contains(cc.get_id())
  add_project_arguments(
    # I've explicitly skipped the duplicated -W versions when they also test
    # for the -Werror version
    cc.get_supported_arguments(
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
      '-fno-common',
    ),
    language : ['c'],
  )
  # We can't test the build type, so we can' add -D_FORTIFY_SOURCE=2 here
  if host_machine.system() == 'darwin'
    if cc.has_argument('-Wno-deprecated-declarations')
      add_project_arguments('-Wno-deprecated-declarations', language : ['c'])
    endif
  endif
elif cc.get_id() == 'msvc'
  add_project_arguments(
    '/D_CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES=1',
    '/D_CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES_COUNT=1',
    '/D_CRT_NONSTDC_NO_WARNINGS=1',
    '/D_CRT_SECURE_NO_WARNINGS=1',
    language : ['c'],
  )
endif

# TODO: solaris extensions

conf = configuration_data()

foreach h : ['assert.h', 'inttypes.h', 'io.h', 'malloc.h', 'memory.h',
             'setjmp.h', 'signal.h', 'stdarg.h', 'stddef.h', 'stdint.h',
             'stdio.h', 'stdlib.h', 'string.h', 'strings.h', 'sys/stat.h',
             'sys/types.h', 'time.h', 'unistd.h']
  if cc.check_header(h)
    conf.set('HAVE_@0@'.format(h.underscorify().to_upper()), 1)
  endif
endforeach

if conf.get('HAVE_TIME_H', 0) == 1
  if cc.has_member('struct timespec', 'tv_sec', prefix : '#include <time.h>')
    conf.set('HAVE_STRUCT_TIMESPEC', 1)
  endif
endif

foreach f : ['calloc', 'exit', 'fprintf', 'free', 'longjmp', 'siglongjmp',
             'malloc', 'memcpy', 'memset', 'printf', 'setjmp', 'signal',
             'strsignal', 'strcmp', 'clock_gettime']
  if cc.has_function(f)
    conf.set('HAVE_@0@'.format(f.underscorify().to_upper()), 1)
  endif
endforeach

if host_machine.system() == 'windows'
  foreach f : ['_vsnprintf_s', '_vsnprtinf', '_snprintf_s', '_snprintf']
    if cc.has_function(f)
      conf.set('HAVE_@0@'.format(f.underscorify().to_upper()), 1)
    endif
  endforeach
  foreach f : ['snprintf', 'vsnprintf']
    if cc.has_header_symbol('stdio.h', f)
      conf.set('HAVE_@0@'.format(f.underscorify().to_upper()), 1)
    endif
  endforeach
else
  foreach f : ['snprintf', 'vsnprintf']
    if cc.has_function(f)
      conf.set('HAVE_@0@'.format(f.underscorify().to_upper()), 1)
    endif
  endforeach
endif

if host_machine.system() == 'windows'
  if cc.compiles('''
      __declspec(thread) int tls;

      int main(void) {
        return 0;
      }''',
      name : 'Thread Local Storage')
    conf.set('HAVE_MSVC_THREAD_LOCAL_STORAGE', 1)
  endif
else
  if cc.compiles('''
      __thread int tls;

      int main(void) {
        return 0;
      }''',
      name : 'Thread Local Storage')
    conf.set('HAVE_GCC_THREAD_LOCAL_STORAGE', 1)
  endif
endif

dep_rt = cc.find_library('rt', required : false)

if (conf.get('HAVE_TIME_H', 0) == 1 and
    conf.get('HAVE_STRUCT_TIMESPEC', 0) == 1 and
    conf.get('HAVE_CLOCK_GETTIME', 0) == 1)
  if cc.has_header_symbol('time.h', 'CLOCK_REALTIME')
    conf.set('HAVE_CLOCK_REALTIME', 1)
  endif
endif  

conf.set('WORDS_SIZEOF_VOID_P', cc.sizeof('void *'))
if host_machine.endian() == 'big'
  conf.set('WORDS_BIGENDIAN', 1)
endif

# TODO: pkg-config
# TODO: cmake-config

inc_include = include_directories('include')

subdir('private')  # someplace safe to put the generated config.h file
subdir('src')

# TODO: doc, include, tests, example
# Since we're using this as a wrap, and it's a unit test framework we're not
# going to install it.

cmocka_dep = declare_dependency(
  link_with : libcmocka,
  include_directories : inc_include,
  version : meson.project_version(),
)
