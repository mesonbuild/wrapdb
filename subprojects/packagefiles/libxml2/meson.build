project('libxml2', 'c', version : '2.9.7', license : 'mit')

cdata = configuration_data()

cdata.set('PACKAGE', meson.project_name())
cdata.set('VERSION', meson.project_version())
cdata.set('PACKAGE_NAME', meson.project_name())
cdata.set('PACKAGE_STRING', '@0@ @1@'.format(meson.project_name(), meson.project_version()))

cc = meson.get_compiler('c')

have_ipv6 = cc.compiles('''#include <sys/types.h>
#include <sys/socket.h>

void func() {
     struct sockaddr_storage ss;
     socket(AF_INET6, SOCK_STREAM, 0);
}''', name : 'Supports IPv6')
cdata.set('SUPPORT_IP6', have_ipv6)

cdata.set('XML_SOCKLEN_T', 'socklen_t')

checked_headers = [
  'ansidecl.h',
  'arpa/inet.h',
  'arpa/nameser.h',
  'ctype.h',
  'dirent.h',
  'dl.h',
  'dlfcn.h',
  'errno.h',
  'fcntl.h',
  'float.h',
  'ieeefp.h',
  'ieeefp.h',
  'inttypes.h',
  'fp_class.h',
  'limits.h',
  'lzma.h',
  'malloc.h',
  'math.h',
  'memory.h',
  'nan.h',
  'ndir.h',
  'netdb.h',
  'netinet/in.h',
  'poll.h',
  'pthread.h',
  'resolv.h',
  'signal.h',
  'stdarg.h',
  'stdint.h',
  'stdlib.h',
  'string.h',
  'strings.h',
  'sys/dir.h',
  'sys/mman.h',
  'sys/ndir.h',
  'sys/select.h',
  'sys/socket.h',
  'sys/stat.h',
  'sys/time.h',
  'sys/timeb.h',
  'sys/types.h',
  'time.h',
  'unistd.h',
  'zlib.h',
]

foreach h : checked_headers
  if cc.has_header(h)
    cdata.set('HAVE_' + h.underscorify().to_upper(), 1)
  endif
endforeach

cdata.set('ICONV_CONST', '')
cdata.set('SEND_ARG2_CAST', '')
cdata.set('GETHOSTBYNAME_ARG_CAST', '')

checked_funcs = [
  ['finite', 'HAVE_FINITE'],
  ['strdup', 'HAVE_STRDUP'],
  ['strndup', 'HAVE_STRNDUP'],
  ['strerror', 'HAVE_STRERROR'],
  ['finite', 'HAVE_FINITE'],
  ['isnand', 'HAVE_ISNAND'],
  ['fp_class', 'HAVE_FP_CLASS'],
  ['class', 'HAVE_CLASS'],
  ['fpclass', 'HAVE_FPCLASS'],
  ['strftime', 'HAVE_STRFTIME'],
  ['localtime', 'HAVE_LOCALTIME'],
  ['gettimeofday', 'HAVE_GETTIMEOFDAY'],
  ['ftime', 'HAVE_FTIME'],
  ['stat', 'HAVE_STAT'],
  ['_stat', 'HAVE__STAT'],
  ['signal', 'HAVE_SIGNAL'],
  ['rand', 'HAVE_RAND'],
  ['rand_r', 'HAVE_RAND_R'],
  ['srand', 'HAVE_SRAND'],
  ['time', 'HAVE_TIME'],
  ['isascii', 'HAVE_ISASCII'],
  ['mmap', 'HAVE_MMAP'],
  ['munmap', 'HAVE_MUNMAP'],
  ['putenv', 'HAVE_PUTENV'],
  ['printf', 'HAVE_PRINTF'],
  ['sprintf', 'HAVE_SPRINTF'],
  ['fprintf', 'HAVE_FPRINTF'],
  ['snprintf', 'HAVE_SNPRINTF'],
  ['vfprintf', 'HAVE_VFPRINTF'],
  ['vsprintf', 'HAVE_VSPRINTF'],
  ['vsnprintf', 'HAVE_VSNPRINTF'],
  ['sscanf', 'HAVE_SSCANF'],
  ['getaddrinfo', 'HAVE_GETADDRINFO'],
  ['va_copy', 'HAVE_VA_COPY'],
  ['__va_copy', 'HAVE___VA_COPY'],
]
foreach f : checked_funcs
  if (cc.has_function(f.get(0)))
    cdata.set(f.get(1), 1)
  endif
endforeach

dl_lib = cc.find_library('dl', required: false)
if (dl_lib.found() and cc.has_function('dlopen', args: '-ldl'))
  cdata.set('HAVE_DLOPEN', 1)
endif

math_lib = cc.find_library('m', required: false)

iconv_lib = cc.find_library('iconv', required : false)

lzma_dep = dependency('liblzma', required: false)
if (lzma_dep.found())
  cdata.set('HAVE_LIBLZMA', 1)
endif

thread_dep = dependency('threads', required: false)
if (thread_dep.found())
   c_args = ['-D_REENTRANT']
endif

zlib_dep = dependency('zlib', required: false, fallback: ['zlib', 'zlib_dep'])
if not zlib_dep.found()
  zlib_dep = cc.find_library('z', required: false)
endif
if zlib_dep.found()
  cdata.set('HAVE_LIBZ', 1)
endif

readline_lib = cc.find_library('readline', required: false)
if readline_lib.found()
  cdata.set('HAVE_LIBREADLINE', 1)
endif

history_lib = cc.find_library('history', required: false)
if history_lib.found()
  cdata.set('HAVE_LIBHISTORY', 1)
endif

deps = [math_lib, iconv_lib, dl_lib, lzma_dep, thread_dep, zlib_dep, readline_lib, history_lib]

if target_machine.system() == 'windows'
  deps += cc.find_library('ws2_32')
endif

configure_file(input : 'config.h.meson',
  output : 'config.h',
  configuration : cdata)

withcdata = configuration_data()
withcdata.set10('HAVE_LIBLZMA', lzma_dep.found())
version = meson.project_version()
version_array = version.split('.')
major = version_array[0].to_int()
minor = version_array[1].to_int()
micro = version_array[2].to_int()
version_number = major * 10000 + minor * 100 + micro
withcdata.set('VERSION', version)
withcdata.set('LIBXML_VERSION_NUMBER', version_number)
withcdata.set('LIBXML_VERSION_STRING', '@0@'.format(version_number))
withcdata.set('LIBXML_VERSION_EXTRA', '')

need_trio = false
pprefix = '#include <stdio.h>'
if (not cc.has_function('printf', prefix: pprefix) or
    not cc.has_function('sprintf', prefix: pprefix) or
    not cc.has_function('fprintf', prefix: pprefix) or
    not cc.has_function('snprintf', prefix: pprefix) or
    not cc.has_function('vfprintf', prefix: pprefix) or
    not cc.has_function('vsprintf', prefix: pprefix) or
    not cc.has_function('vsnprintf', prefix: pprefix) or
    not cc.has_function('sscanf', prefix: pprefix))
    need_trio = true
endif
withcdata.set10('WITH_TRIO', need_trio)

withcdata.set10('WITH_THREADS', thread_dep.found())
withcdata.set10('WITH_THREAD_ALLOC', false)
withcdata.set10('WITH_TREE', true)
withcdata.set10('WITH_OUTPUT', true)
withcdata.set10('WITH_PUSH', true)
withcdata.set10('WITH_READER', true)
withcdata.set10('WITH_PATTERN', true)
withcdata.set10('WITH_WRITER', true)
withcdata.set10('WITH_SAX1', true)
withcdata.set10('WITH_FTP', true)
withcdata.set10('WITH_HTTP', true)
withcdata.set10('WITH_VALID', true)
withcdata.set10('WITH_HTML', true)
withcdata.set10('WITH_LEGACY', true)
withcdata.set10('WITH_C14N', true)
withcdata.set10('WITH_CATALOG', true)
withcdata.set10('WITH_DOCB', true)
withcdata.set10('WITH_XPATH', true)
withcdata.set10('WITH_XPTR', true)
withcdata.set10('WITH_XINCLUDE', true)
withcdata.set10('WITH_ICONV', iconv_lib.found())
withcdata.set10('WITH_ICU', false)
withcdata.set10('WITH_ISO8859X', true)
withcdata.set10('WITH_DEBUG', true)
withcdata.set10('WITH_MEM_DEBUG', false)
withcdata.set10('WITH_RUN_DEBUG', false)
withcdata.set10('WITH_REGEXPS', true)
withcdata.set10('WITH_SCHEMAS', true)
withcdata.set10('WITH_SCHEMATRON', true)
withcdata.set10('WITH_MODULES', dl_lib.found())

system = target_machine.system()
module_ext = '.so'
if (system == 'windows' or system == 'cygwin')
  module_ext = '.dll'
endif
withcdata.set('MODULE_EXTENSION', module_ext)

withcdata.set10('WITH_ZLIB', zlib_dep.found())
withcdata.set10('WITH_LZMA', lzma_dep.found())


subdir('include/libxml')

trio_sources = [ 'triostr.c', 'trio.c', 'trionan.c' ]
sources = [
  'SAX.c',
  'entities.c',
  'encoding.c',
  'error.c',
  'parserInternals.c',
  'parser.c',
  'tree.c',
  'hash.c',
  'list.c',
  'xmlIO.c',
  'xmlmemory.c',
  'uri.c',
  'valid.c',
  'xlink.c',
  'HTMLparser.c',
  'HTMLtree.c',
  'debugXML.c',
  'xpath.c',
  'xpointer.c',
  'xinclude.c',
  'nanohttp.c',
  'nanoftp.c',
  'catalog.c',
  'globals.c',
  'threads.c',
  'c14n.c',
  'xmlstring.c',
  'buf.c',
  'xmlregexp.c',
  'xmlschemas.c',
  'xmlschemastypes.c',
  'xmlunicode.c',
  'xmlreader.c',
  'relaxng.c',
  'dict.c',
  'SAX2.c',
  'xmlwriter.c',
  'legacy.c',
  'chvalid.c',
  'pattern.c',
  'xmlsave.c',
  'xmlmodule.c',
  'schematron.c',
  'xzlib.c'
]

if (need_trio)
  sources += trio_sources
endif

incdir = include_directories('include')

xml2lib = library('xml2', sources,
                  c_args : c_args,
                  include_directories : incdir,
                  dependencies: deps,
                  install: true)
xml2lib_dep = declare_dependency(link_with: xml2lib,
                                 include_directories: incdir,
                                 dependencies: deps)
pkg = import('pkgconfig')
pkg.generate(name : 'libXML',
             description: 'libXML library version2.',
             filebase: 'libxml-2.0',
             libraries: xml2lib,
             subdirs: 'libxml2',
             variables: 'modules=@0@'.format(withcdata.get('WITH_MODULES')))


executable('xmllint', 'xmllint.c',
           dependencies: xml2lib_dep,
           install: true)

dictexe = executable('testdict', 'testdict.c',
                     dependencies : xml2lib_dep)

test('dict', dictexe)
