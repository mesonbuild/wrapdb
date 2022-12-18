project(
  'gdbm',
  'c',
  version: '1.23',
  license: 'lgpl',
  meson_version: '>=0.49.0',
)

if host_machine.system() == 'windows'
  error('Windows is unsupported')
endif

conf = configuration_data()
conf.set_quoted('PACKAGE', meson.project_name())
conf.set_quoted('PACKAGE_NAME', meson.project_name())
conf.set_quoted('PACKAGE_TARNAME', meson.project_name())
conf.set_quoted('PACKAGE_VERSION', meson.project_version())
conf.set_quoted('VERSION', meson.project_version())
conf.set_quoted('PACKAGE_STRING', '@0@ @1@'.format(meson.project_name(), meson.project_version()))
conf.set_quoted('PACKAGE_URL', 'http://www.gnu.org/software/gdbm')
conf.set_quoted('PACKAGE_BUGREPORT', 'bug-gdbm@gnu.org')
conf.set_quoted('LT_OBJDIR', '.libs/')
conf.set('STDC_HEADERS', 1)

cc = meson.get_compiler('c')

conf.set('SIZEOF_OFF_T', cc.sizeof('off_t'))
if cc.compiles('static __thread int x = 0;')
  conf.set('GDBM_THREAD_LOCAL', '__thread')
endif

if cc.has_type('unsigned long long int')
  conf.set('HAVE_UNSIGNED_LONG_LONG_INT', 1)
endif

if cc.has_header_symbol('linux/fs.h', 'FICLONE')
  conf.set('GDBM_FAILURE_ATOMIC', 1)
endif

foreach s : ['st_blksize', 'st_mtim', 'st_mtimespec']
  if cc.has_member('struct stat', s, prefix: '#include <sys/stat.h>')
    conf.set('HAVE_STRUCT_STAT_@0@'.format(s.underscorify().to_upper()), 1)
  endif
endforeach

deps = []
if meson.version().version_compare('>= 0.62')
  dl_dep = dependency('dl', disabler: true, required: get_option('dl'))
else
  dl_dep = cpp.find_library('dl', disabler: true, required: get_option('dl'))
endif
if dl_dep.found()
  deps += dl_dep
endif

if meson.version().version_compare('>= 0.60')
  iconv_dep = dependency('iconv', disabler: true, required: get_option('nls'))
else
  iconv_dep = dependency('', disabler: true, required: false)
endif
if iconv_dep.found()
  conf.set('HAVE_ICONV', 1)
  deps += iconv_dep
endif

if meson.version().version_compare('>= 0.59')
  intl_dep = dependency('intl', disabler: true, required: get_option('nls'))
else
  intl_dep = dependency('', disabler: true, required: false)
endif
if intl_dep.found()
  conf.set('ENABLE_NLS', 1)
  deps += intl_dep
endif

readline_dep = dependency('readline', disabler: true, required: false)
if readline_dep.found()
  conf.set('WITH_READLINE', 1)
  deps += readline_dep
endif

headers = {
  'dlfcn.h': dl_dep,
  'getopt.h': [],
  'inttypes.h': [],
  'locale.h': [],
  'readline/readline.h': readline_dep,
  'stdint.h': [],
  'stdio.h': [],
  'stdlib.h': [],
  'string.h': [],
  'strings.h': [],
  'sys/file.h': [],
  'sys/param.h': [],
  'sys/stat.h': [],
  'sys/termios.h': [],
  'sys/types.h': [],
  'unistd.h': [],
}

foreach h, d : headers
  if cc.has_header(h, dependencies: d)
    conf.set('HAVE_@0@'.format(h.underscorify().to_upper()), 1)
  endif
endforeach

functions = {
  'dcgettext': intl_dep,
  'flock': [],
  'fsync': [],
  'ftruncate': [],
  'getline': [],
  'getopt_long': [],
  'getpagesize': [],
  'gettext': intl_dep,
  'lockf': [],
  'rl_completion_matches': readline_dep,
  'setlocale': [],
}

if get_option('mmap')
  functions += {'mmap': [], 'msync': []}
endif

foreach f, d : functions
  if cc.has_function(f, dependencies: d)
    conf.set('HAVE_@0@'.format(f.underscorify().to_upper()), 1)
  endif
endforeach

configure_file(
  input: 'autoconf.h.meson',
  output: 'autoconf.h',
  configuration: conf,
)

autoconf_include = include_directories('.')
subdir('src')
