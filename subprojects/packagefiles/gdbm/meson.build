project('gdbm', 'c', version: '1.14.1', license: 'lgpl')
cc = meson.get_compiler('c')

conf = configuration_data()
conf.set_quoted('PACKAGE_NAME', meson.project_name())
conf.set_quoted('PACKAGE_VERSION', meson.project_version())
conf.set_quoted('PACKAGE_BUGREPORT', 'bug-gdbm@gnu.org')

headers = ['sys/file.h', 'sys/termios.h', 'string.h', 'locale.h', 'getopt.h']
foreach header : headers
    conf.set('HAVE_' + header.underscorify().to_upper(),
        cc.has_header(header) ? 1 : 0)
endforeach

functions = ['ftruncate', 'flock', 'lockf', 'fsync', 'setlocale', 'getopt_long']
if get_option('mmap')
    functions += ['mmap', 'msync']
endif
foreach function : functions
    conf.set('HAVE_' + function.underscorify().to_upper(),
        cc.has_function(function) ? 1 : 0)
endforeach

conf.set('SIZEOF_OFF_T', cc.sizeof('off_t'))
conf.set('HAVE_STRUCT_STAT_ST_BLKSIZE', 
    cc.has_member('struct stat', 'st_blksize', prefix: '#include <sys/stat.h>') ? 1 : 0)
if cc.compiles('static __thread int x = 0;')
    conf.set('GDBM_THREAD_LOCAL', '__thread')
endif
configure_file(output: 'autoconf.h', configuration: conf)
autoconf_include = include_directories('.')

subdir('src')
