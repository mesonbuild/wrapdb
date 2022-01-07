project('liblangtag', 'c', version: '0.6.3')

cc = meson.get_compiler('c')

xml_dep = dependency('libxml-2.0')
threads_dep = []
dl_dep = cc.find_library('dl', required: false)

cdata = configuration_data()
check_headers = [
  ['HAVE_DIRENT_H', 'dirent.h'],
  ['HAVE_DLFCN_H', 'dlfcn.h'],
  ['HAVE_EXECINFO_H', 'execinfo.h'],
  ['HAVE_INTTYPES_H', 'inttypes.h'],
  ['HAVE_LIBGEN_H', 'libgen.h'],
  ['HAVE_MEMORY_H', 'memory.h'],
  ['HAVE_STDINT_H', 'stdint.h'],
  ['HAVE_STDLIB_H', 'stdlib.h'],
  ['HAVE_STRINGS_H', 'strings.h'],
  ['HAVE_STRING_H', 'string.h'],
  ['HAVE_SYS_PARAM_H', 'sys/param.h'],
  ['HAVE_SYS_STAT_H', 'sys/stat.h'],
  ['HAVE_SYS_TYPES_H', 'sys/types.h'],
  ['HAVE_UNISTD_H', 'unistd.h'],
]

foreach h : check_headers
  if cc.has_header(h.get(1))
    cdata.set(h.get(0), 1)
  endif
endforeach

check_functions = [
# check token ['HAVE_BACKTRACE']
# check token ['HAVE_GETEGID']
# check token ['HAVE_GETEUID']
# check token ['HAVE_GETGID']
  ['HAVE_GETUID', 'getuid', '#include<unistd.h>'],
# check token ['HAVE_PTHREAD']
# check token ['HAVE_PTHREAD_PRIO_INHERIT']
# check token ['HAVE_SECURE_GETENV']
  ['HAVE_STRNDUP', 'strndup', '#include<string.h>'],
  ['HAVE_VASPRINTF', 'vasprintf', '#include<stdio.h>'],
# check token ['HAVE_VA_COPY']
  ['HAVE_VSNPRINTF', 'vsnprintf', '#include<stdio.h>'],
# check token ['HAVE___SECURE_GETENV']
# check token ['HAVE_VA_COPY']
]

if host_machine.system() != 'windows'
  cdata.set('HAVE_PTHREAD', 1)
  thread_dep = dependency('threads')
  cdata.set('ENABLE_MODULE', 1)
else
  cdata.set('ENABLE_MODULE', 0)
endif

if cc.get_id() == 'msvc'
  cdata.set('HAVE_VA_COPY', 1)
endif

foreach f : check_functions
  if cc.has_function(f.get(1), prefix : f.get(2))
    cdata.set(f.get(0), 1)
  endif
endforeach

cdata.set('SIZEOF_CHAR', cc.sizeof('char'))
cdata.set('SIZEOF_INT', cc.sizeof('int'))
cdata.set('SIZEOF_LONG', cc.sizeof('long'))
cdata.set('SIZEOF_LONG_LONG', cc.sizeof('long long'))
cdata.set('SIZEOF_SHORT', cc.sizeof('short'))
cdata.set('SIZEOF_VOIDP', cc.sizeof('voidp'))
cdata.set('ALIGNOF_VOID_P', cc.alignment('void*'))

# Because we are not living in the 1980s any more.
cdata.set('LT_HAVE_INLINE', 1)
cdata.set('LT_CAN_INLINE', 1)

cdata.set_quoted('LT_MODULE_SUFFIX', host_machine.system() == 'windows' ? 'dll' : 'so')

configure_file(input : 'config.h.meson',
  output : 'config.h',
  configuration : cdata)

# The source code lacks function export annotations, so
# it can not be built as a shared library under MSVC,
# because no symbols get exported.
#
# The original uses libtool magic to export symbols on unix.
#
# I think

ttype = host_machine.system() == 'windows' ? 'static_library' : 'library'

liblangtag_lib = build_target('langtag',
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
  c_args: ['-D__LANGTAG_COMPILATION',
           '-D__LANGTAG_PRIVATE',
           '-DHAVE_CONFIG_H',
           '-DREGDATADIR="@0@/liblangtag"'.format(get_option('datadir')),
           '-DLANGTAG_EXT_MODULE_PATH="@0@"'.format(get_option('libdir') / 'liblangtag')],
  dependencies: [xml_dep, threads_dep, dl_dep],
)

liblangtag_dep = declare_dependency(include_directories: '.',
  link_with: liblangtag_lib)
