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

cc = meson.get_compiler('c')

conf = configuration_data()
conf.set_quoted('PACKAGE_NAME', meson.project_name())
conf.set_quoted('PACKAGE_VERSION', meson.project_version())
conf.set_quoted('PACKAGE_BUGREPORT', 'bug-gdbm@gnu.org')

foreach h : ['sys/file.h', 'sys/termios.h', 'string.h', 'locale.h', 'getopt.h']
  conf.set10('HAVE_@0@'.format(h.underscorify().to_upper()), cc.has_header(h))
endforeach

functions = ['ftruncate', 'flock', 'lockf', 'fsync', 'setlocale', 'getopt_long']
if get_option('mmap')
  functions += ['mmap', 'msync']
endif

foreach f : functions
  conf.set10('HAVE_@0@'.format(f.underscorify().to_upper()), cc.has_function(f))
endforeach

conf.set('SIZEOF_OFF_T', cc.sizeof('off_t'))
conf.set10('HAVE_STRUCT_STAT_ST_BLKSIZE', cc.has_member('struct stat', 'st_blksize', prefix: '#include <sys/stat.h>'))
if cc.compiles('static __thread int x = 0;')
  conf.set('GDBM_THREAD_LOCAL', '__thread')
endif
configure_file(
  output: 'autoconf.h',
  configuration: conf,
)

autoconf_include = include_directories('.')
subdir('src')
