# Copyright © 2019-2020, Intel Corporation
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:

#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Intel Corporation. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

project(
  'google-snappy',
  'cpp',
  version: '1.1.9',
  license: 'BSD3',
  meson_version: '>= 0.50',
)

cpp = meson.get_compiler('cpp')
conf = configuration_data()
pconf = configuration_data()
dep_null = dependency(
  '',
  required: false,
)

add_project_arguments(
  cpp.get_supported_arguments('-Wno-sign-compare'),
  language: 'cpp',
)

if host_machine.endian() == 'big'
  conf.set('SNAPPY_IS_BIG_ENDIAN', 1)
endif

foreach h : [
  'byteswap.h',
  'stddef.h',
  'stdint.h',
  'sys/endian.h',
  'sys/mman.h',
  'sys/resource.h',
  'sys/time.h',
  'sys/uio.h',
  'unistd.h',
  'windows.h',
]
  if cpp.has_header(h)
    conf.set('HAVE_' + h.to_upper().underscorify(), 1)
  endif
endforeach

foreach f : ['expect', 'ctzll']
  if cpp.has_function(f)
    conf.set('HAVE_BULITIN_' + f.to_upper(), 1)
  endif
endforeach
if conf.get('HAVE_SYS_MMAN_H', 0) == 1
  if cpp.has_function(
    'mmap',
    prefix: '#include <sys/mman.h>',
  )
    conf.set('HAVE_FUNC_MMAP', 1)
  endif
endif
if conf.get('HAVE_UNISTD_H', 0) == 1
  if cpp.has_function(
    'sysconf',
    prefix: '#include <unistd.h>',
  )
    conf.set('HAVE_FNC_SYSCONF', 1)
  endif
endif

configure_file(
  configuration: conf,
  output: 'config.h',
)

foreach h : ['HAVE_STDINT_H', 'HAVE_STDDEF_H', 'HAVE_SYS_UIO_H']
  pconf.set(h + '_01', conf.get(h, 0))
endforeach

version = meson.project_version().split('.')
pconf.set('PROJECT_VERSION_MAJOR', version[0])
pconf.set('PROJECT_VERSION_MINOR', version[1])
pconf.set('PROJECT_VERSION_PATCH', version[2])

configure_file(
  configuration: pconf,
  input: 'snappy-stubs-public.h.in',
  output: 'snappy-stubs-public.h',
  format: 'cmake',
)

libsnappy = library(
  'snappy',
  [
    'snappy-c.cc',
    'snappy-sinksource.cc',
    'snappy-stubs-internal.cc',
    'snappy.cc',
  ],
  cpp_args: ['-DHAVE_CONFIG_H'],
  version: meson.project_version(),
)

snappy_dep = declare_dependency(
  link_with: libsnappy,
  include_directories: include_directories('.'),
  version: meson.project_version(),
)
