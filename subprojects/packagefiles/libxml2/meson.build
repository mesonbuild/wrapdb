project(
  'libxml2',
  'c',
  version: '2.12.6',
  meson_version: '>=0.54.1',
  license: 'MIT',
  default_options: 'c_std=c99',
)

add_project_arguments('-D_GNU_SOURCE', language: 'c')

cc = meson.get_compiler('c')
# avoid false positive warnings about NULL fmt argument to __xmlSimpleError(),
# as upstream does
add_project_arguments(cc.get_supported_arguments('-Wno-format-extra-args'), language: 'c')
if host_machine.system() == 'windows'
  if cc.get_argument_syntax() != 'gcc'
    add_project_arguments('-D_CRT_SECURE_NO_WARNINGS', cc.get_supported_arguments('-Wno-deprecated-declarations'), language: 'c')
  endif
endif

cdata = configuration_data()

cdata.set('VERSION', meson.project_version())

if cc.has_function_attribute('destructor')
  cdata.set('ATTRIBUTE_DESTRUCTOR', '__attribute__((destructor))')
endif
cdata.set10('HAVE_ATTRIBUTE_DESTRUCTOR', cdata.has('ATTRIBUTE_DESTRUCTOR'))

if cc.has_header_symbol('sys/socket.h', 'AF_INET6') or cc.has_header_symbol('winsock2.h', 'AF_INET6')
  cdata.set('SUPPORT_IP6', 1)
endif

if cc.compiles('#include <stdarg.h> void a(va_list*) {}int main(){va_list ap1,ap2;a(&ap1);ap2=(va_list)ap1;return 0;}')
  cdata.set('VA_LIST_IS_ARRAY', 1)
endif

if cc.compiles('#include <sys/socket.h> int main(){send(1,(const char*)"",1,1);}') or cc.compiles('#include <winsock2.h> int main(){send(1,(const char*)"",1,1);}')
  cdata.set('SEND_ARG2_CAST', '/**/')
else
  cdata.set('SEND_ARG2_CAST', '(char *)')
endif

if cc.compiles('#include <netdb.h> int main(){gethostbyname((const char*)"");}') or cc.compiles('#include <ws2tcpip.h> int main(){gethostbyname((const char*)"");}')
  cdata.set('GETHOSTBYNAME_ARG_CAST', '/**/')
else
  cdata.set('GETHOSTBYNAME_ARG_CAST', '(char *)')
endif

if cc.compiles('_Thread_local int v;')
  cdata.set('XML_THREAD_LOCAL', '_Thread_local')
elif cc.compiles('__thread int v;')
  cdata.set('XML_THREAD_LOCAL', '__thread')
elif cc.compiles('__declspec(thread) int v;')
  cdata.set('XML_THREAD_LOCAL', '__declspec(thread)')
endif

if cc.has_header_symbol('stdarg.h', 'va_copy')
  cdata.set('HAVE_VA_COPY', 1)
endif

if cc.has_header_symbol('stdarg.h', '__va_copy')
  cdata.set('HAVE___VA_COPY', 1)
endif

deps = []

if meson.version().version_compare('>= 0.62')
  dl_lib = dependency('dl', disabler: true, required: false)
else
  dl_lib = cc.find_library('dl', disabler: true, required: false)
endif
if dl_lib.found()
  cdata.set('HAVE_DLOPEN', 1)
  cdata.set('HAVE_DLFCN_H', 1)
  deps += dl_lib
endif

math_lib = cc.find_library('m', required: false)
if math_lib.found()
  deps += math_lib
endif

if meson.version().version_compare('>= 0.60')
  iconv_lib = dependency('iconv', required: get_option('iconv'))
else
  if get_option('iconv').disabled()
    iconv_lib = dependency('', required: false)
  else
    iconv_check = '''
    #include <iconv.h>
    int main() {
      iconv_open("", "");
    }
    '''
    if cc.links(iconv_check, name: 'iconv_open')
      iconv_lib = declare_dependency()
    else
      iconv_lib = cc.find_library('iconv', required: false)
      if not cc.links(iconv_check, name: 'iconv_open in libiconv', dependencies: iconv_lib)
        iconv_lib = dependency('', required: false)
        if get_option('iconv').enabled()
          error('iconv enabled and not found')
        endif
      endif
    endif
  endif
endif
if iconv_lib.found()
  deps += iconv_lib
endif

if host_machine.system() == 'windows'
  pthread_dep = disabler()
  with_threads = true
else
  pthread_dep = dependency('threads', disabler: true, required: false)
  with_threads = pthread_dep.found()
  if with_threads
    deps += pthread_dep
  endif
endif
if with_threads and not cdata.has('XML_THREAD_LOCAL')
  warning('Your C compiler appears to not support thread-local storage. Future versions of libxml2 will require this feature for multi-threading.')
endif

lzma_dep = dependency('liblzma', required: false)
if lzma_dep.found()
  cdata.set('HAVE_LIBLZMA', 1)
  deps += lzma_dep
endif

zlib_dep = dependency('zlib', disabler: true, required: false)
if zlib_dep.found()
  cdata.set('HAVE_LIBZ', 1)
  cdata.set('HAVE_ZLIB_H', 1)
  deps += zlib_dep
endif

readline_lib = cc.find_library('readline', required: false)
if cc.has_header('readline/readline.h', dependencies: readline_lib)
  cdata.set('HAVE_LIBREADLINE', 1)
  deps += readline_lib
endif

history_lib = cc.find_library('history', required: false)
if cc.has_header('readline/history.h', dependencies: history_lib)
  cdata.set('HAVE_LIBHISTORY', 1)
  deps += history_lib
endif

ws2_dep = cc.find_library('ws2_32', required: host_machine.system() == 'windows')
if ws2_dep.found()
  deps += ws2_dep
endif

foreach t : ['socklen_t', 'size_t', 'int']
  if cc.compiles('#include <sys/socket.h> int main(){getsockopt(1,1,1,0,(@0@*)0);}'.format(t))
    cdata.set('XML_SOCKLEN_T', t)
    break
  endif
  if cc.compiles('#include <winsock2.h> int main(){getsockopt(1,1,1,0,(@0@*)0);}'.format(t), dependencies: ws2_dep)
    cdata.set('XML_SOCKLEN_T', t)
    break
  endif
endforeach

checked_headers = {
  'arpa/inet.h': [],
  'arpa/nameser.h': [],
  'dl.h': [],
  'fcntl.h': [],
  'float.h': [],
  'inttypes.h': [],
  'netdb.h': [],
  'netinet/in.h': [],
  'poll.h': [],
  'pthread.h': pthread_dep,
  'resolv.h': [],
  'stdint.h': [],
  'sys/mman.h': [],
  'sys/select.h': [],
  'sys/socket.h': [],
  'sys/stat.h': [],
  'sys/time.h': [],
  'sys/timeb.h': [],
  'sys/types.h': [],
  'unistd.h': [],
}

foreach h, d : checked_headers
  if cc.has_header(h, dependencies: d)
    cdata.set('HAVE_@0@'.format(h.underscorify().to_upper()), 1)
  endif
endforeach

checked_funcs = {
  'ftime': [],
  'gettimeofday': [],
  'isascii': [],
  'mmap': [],
  'munmap': [],
  'stat': [],
}

foreach f, d : checked_funcs
  if cc.has_function(f, dependencies: d)
    cdata.set('HAVE_@0@'.format(f.underscorify().to_upper()), 1)
  endif
endforeach

configure_file(
  input: 'config.h.cmake.in',
  output: 'config.h',
  format: 'cmake@',
  configuration: cdata,
)

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

withcdata.set10('WITH_TRIO', false)
withcdata.set10('WITH_THREADS', with_threads)
withcdata.set10('WITH_THREAD_ALLOC', false)
withcdata.set10('WITH_TREE', true)
withcdata.set10('WITH_OUTPUT', true)
withcdata.set10('WITH_PUSH', true)
withcdata.set10('WITH_READER', true)
withcdata.set10('WITH_PATTERN', true)
withcdata.set10('WITH_WRITER', true)
withcdata.set10('WITH_SAX1', true)
withcdata.set10('WITH_FTP', false)
withcdata.set10('WITH_HTTP', true)
withcdata.set10('WITH_VALID', true)
withcdata.set10('WITH_HTML', true)
withcdata.set10('WITH_LEGACY', false)
withcdata.set10('WITH_C14N', true)
withcdata.set10('WITH_CATALOG', true)
withcdata.set10('WITH_DOCB', true)
withcdata.set10('WITH_XPATH', true)
withcdata.set10('WITH_XPTR', true)
withcdata.set10('WITH_XPTR_LOCS', false)
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
if system == 'cygwin'
  module_ext = '.cygdll'
elif system == 'darwin'
  module_ext = '.bundle'
elif system == 'windows'
  module_ext = '.dll'
else
  module_ext = '.so'
endif

withcdata.set('MODULE_EXTENSION', module_ext)

withcdata.set10('WITH_ZLIB', zlib_dep.found())
withcdata.set10('WITH_LZMA', lzma_dep.found())

subdir('include/libxml')

sources = files(
  'HTMLparser.c',
  'HTMLtree.c',
  'SAX.c',
  'SAX2.c',
  'buf.c',
  'c14n.c',
  'catalog.c',
  'chvalid.c',
  'debugXML.c',
  'dict.c',
  'encoding.c',
  'entities.c',
  'error.c',
  'globals.c',
  'hash.c',
  'legacy.c',
  'list.c',
  'nanoftp.c',
  'nanohttp.c',
  'parser.c',
  'parserInternals.c',
  'pattern.c',
  'relaxng.c',
  'schematron.c',
  'threads.c',
  'tree.c',
  'uri.c',
  'valid.c',
  'xinclude.c',
  'xlink.c',
  'xmlIO.c',
  'xmlmemory.c',
  'xmlmodule.c',
  'xmlreader.c',
  'xmlregexp.c',
  'xmlsave.c',
  'xmlschemas.c',
  'xmlschemastypes.c',
  'xmlstring.c',
  'xmlunicode.c',
  'xmlwriter.c',
  'xpath.c',
  'xpointer.c',
  'xzlib.c',
)

if host_machine.system() == 'windows'
  subdir('win32')
endif

cargs = with_threads ? ['-D_REENTRANT'] : []
cargs += get_option('default_library') == 'static' ? '-DLIBXML_STATIC' : []

link_args = cc.get_supported_link_arguments(
  [
    # lld 16 defaults to --no-undefined-version but the version script
    # can contain symbols disabled by configuration options.
    '-Wl,--undefined-version',
    '-Wl,--version-script=@0@'.format(meson.current_source_dir() / 'libxml2.syms')
  ]
)

incdir = include_directories('include')
xml2lib = library(
  'xml2',
  sources,
  c_args: cargs,
  link_args: link_args,
  include_directories: incdir,
  dependencies: deps,
  version: meson.project_version(),
  gnu_symbol_visibility: 'default',
  install: true,
)

libxml2_dep = declare_dependency(
  link_with: xml2lib,
  include_directories: incdir,
  dependencies: deps,
  variables: 'modules=@0@'.format(withcdata.get('WITH_MODULES')),
  compile_args: get_option('default_library') == 'static' ? '-DLIBXML_STATIC' : [],
)

pkg = import('pkgconfig')
pkg.generate(
  xml2lib,
  name: 'libXML',
  description: 'libXML library version2.',
  filebase: 'libxml-2.0',
  subdirs: 'libxml2',
  variables: 'modules=@0@'.format(withcdata.get('WITH_MODULES')),
  extra_cflags: get_option('default_library') == 'static' ? '-DLIBXML_STATIC' : [],
)

executable('xmllint', 'xmllint.c', dependencies: libxml2_dep, install: true)

dictexe = executable('testdict', 'testdict.c', dependencies: libxml2_dep)

test('dict', dictexe)
