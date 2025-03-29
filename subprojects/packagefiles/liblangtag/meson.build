project(
  'liblangtag',
  'c',
  license: 'LGPL-3.0-or-later',
  version: '0.6.7',
  meson_version: '>=0.49.0',
)

cc = meson.get_compiler('c')

xml_dep = dependency('libxml-2.0')
threads_dep = dependency('threads')
if meson.version().version_compare('>= 0.62.0')
  dl_dep = dependency(
    'dl',
    required: false,
  )
else
  dl_dep = cc.find_library(
    'dl',
    required: false,
  )
endif

cdata = configuration_data()

foreach h : [
  'dirent.h',
  'dlfcn.h',
  'libgen.h',
  'memory.h',
  'string.h',
  'sys/param.h',
  'unistd.h',
]
  cdata.set10('HAVE_@0@'.format(h.underscorify().to_upper()), cc.has_header(h))
endforeach

cdata.set('HAVE_EXECINFO_H', cc.has_header('execinfo.h'))
cdata.set10(
  'HAVE_PTHREAD',
  cc.has_header('pthread.h') and host_machine.system() != 'windows',
)

foreach f : ['backtrace', 'strndup', 'vasprintf', 'vsnprintf']
  cdata.set10(
    'HAVE_@0@'.format(f.underscorify().to_upper()),
    cc.has_function(
      f,
      prefix: '#include <stdio.h>',
    ),
  )
endforeach

if cdata.get('HAVE_VASPRINTF') == 1
  add_project_arguments(
    '-D_GNU_SOURCE',
    language: 'c',
  )
endif

foreach f : ['getegid', 'geteuid', 'getgid', 'getuid']
  cdata.set('HAVE_@0@'.format(f.underscorify().to_upper()), cc.has_function(f))
endforeach

cdata.set('HAVE___SECURE_GETENV', cc.has_function('__secure_getenv'))

cdata.set('ALIGNOF_VOID_P', cc.sizeof('void*'))

# Because we are not living in the 1980s any more.
cdata.set('LT_CAN_INLINE', true)

cdata.set_quoted(
  'LT_MODULE_SUFFIX',
  host_machine.system() == 'windows' ? 'dll' : 'so',
)

if host_machine.system() != 'windows'
  cdata.set('ENABLE_MODULE', 1)
else
  cdata.set('ENABLE_MODULE', 0)
endif

configure_file(
  output: 'config.h',
  configuration: cdata,
)

# The source code lacks function export annotations, so
# it can not be built as a shared library under MSVC,
# because no symbols get exported.
#
# The original uses libtool magic to export symbols on unix.
#
# I think

ttype = host_machine.system() == 'windows' ? 'static_library' : 'library'

liblangtag_lib = build_target(
  'langtag',
  'liblangtag/lt-database.c',
  'liblangtag/lt-error.c',
  'liblangtag/lt-ext-module.c',
  'liblangtag/lt-ext-module-data.c',
  'liblangtag/lt-extension.c',
  'liblangtag/lt-extlang.c',
  'liblangtag/lt-extlang-db.c',
  'liblangtag/lt-grandfathered.c',
  'liblangtag/lt-grandfathered-db.c',
  'liblangtag/lt-iter.c',
  'liblangtag/lt-lang.c',
  'liblangtag/lt-lang-db.c',
  'liblangtag/lt-list.c',
  'liblangtag/lt-mem.c',
  'liblangtag/lt-messages.c',
  'liblangtag/lt-redundant.c',
  'liblangtag/lt-redundant-db.c',
  'liblangtag/lt-region.c',
  'liblangtag/lt-region-db.c',
  'liblangtag/lt-relation-db.c',
  'liblangtag/lt-script.c',
  'liblangtag/lt-script-db.c',
  'liblangtag/lt-string.c',
  'liblangtag/lt-tag.c',
  'liblangtag/lt-trie.c',
  'liblangtag/lt-utils.c',
  'liblangtag/lt-variant.c',
  'liblangtag/lt-variant-db.c',
  'liblangtag/lt-xml.c',
  target_type: ttype,
  c_args: [
    '-D__LANGTAG_COMPILATION',
    '-D__LANGTAG_PRIVATE',
    '-DHAVE_CONFIG_H',
    '-DREGDATADIR="@0@/liblangtag"'.format(get_option('datadir')),
    '-DLANGTAG_EXT_MODULE_PATH="@0@"'.format(get_option('libdir') / 'liblangtag'),
  ],
  dependencies: [xml_dep, threads_dep, dl_dep],
)

depinc = include_directories('.')
liblangtag_dep = declare_dependency(
  include_directories: depinc,
  link_with: liblangtag_lib,
)
