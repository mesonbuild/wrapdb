project(
  'libfuse',
  'c',
  version: '2.9.9',
  meson_version: '>=0.49.0',
)

platform = host_machine.system()
if platform == 'darwin'
  error(
    'libfuse does not support OS-X.\n' + 'Take a look at http://osxfuse.github.io/ instead',
  )
elif platform == 'cygwin' or platform == 'windows'
  error(
    'libfuse does not support Windows.\n' + 'Take a look at http://www.secfs.net/winfsp/ instead',
  )
endif

cc = meson.get_compiler('c')

# Common dependencies
if meson.version().version_compare('>= 0.60')
  iconv_dep = dependency(
    'iconv',
    required: false,
  )
else
  iconv_open_snippet = '''#include <iconv.h>
    int main() {
    iconv_open("","");
    }'''
  have_iconv = cc.links(
    iconv_open_snippet,
    name: 'iconv_open',
  )
  if not have_iconv
    iconv_dep = cc.find_library(
      'iconv',
      required: false,
    )
  else
    iconv_dep = declare_dependency()
  endif
endif
thread_dep = dependency('threads')

#
# Feature detection
#
cfg = configuration_data()
cfg.set_quoted('PACKAGE_VERSION', meson.project_version())

# Test for presence of some functions
test_funcs = [
  'fork',
  'fstatat',
  'openat',
  'readlinkat',
  'pipe2',
  'splice',
  'vmsplice',
  'posix_fallocate',
  'fdatasync',
  'utimensat',
  'copy_file_range',
  'fallocate',
]
foreach f : test_funcs
  cfg.set('HAVE_@0@'.format(f.underscorify().to_upper()), cc.has_function(f))
endforeach

cfg.set(
  'HAVE_SETXATTR',
  cc.has_function(
    'setxattr',
    prefix: '#include <sys/xattr.h>',
  ),
)
cfg.set('HAVE_ICONV', iconv_dep.found())

# Test if structs have specific member
foreach m : ['st_atim', 'st_atimespec']
  cfg.set(
    'HAVE_STRUCT_STAT_@0@'.format(m.underscorify().to_upper()),
    cc.has_member(
      'struct stat',
      m,
      prefix: '#include <sys/stat.h>\n',
      args: '-D_GNU_SOURCE',
    ),
  )
endforeach

# Write the test results into config.h (stored in build directory)
configure_file(
  output: 'config.h',
  configuration: cfg,
)

#
# Compiler configuration
#
add_project_arguments(
  '-D_REENTRANT',
  '-DHAVE_CONFIG_H',
  '-Wno-sign-compare',
  '-Wno-unused-result',
  '-Wstrict-prototypes',
  '-Wmissing-declarations',
  '-Wwrite-strings',
  '-fno-strict-aliasing',
  language: 'c',
)

# gcc-10 and newer support the symver attribute which we need to use if we
# want to support LTO
# recent clang and gcc both support __has_attribute (and if they are too old
# to have __has_attribute, then they are too old to support symver)
# other compilers might not have __has_attribute, but in those cases
# it is safe for this check to fail and for us to fallback to the old _asm_
# method for symver
code = ('''
#if defined __has_attribute
# if !__has_attribute (symver)
# error symver attribute not supported
# endif
#else
#error __has_attribute not defined, assume we do not have symver
#endif

int main(void) {
    return 0;
}'''
)
if cc.compiles(
  code,
  args: ['-O0', '-c'],
)
  message('Compiler supports symver attribute')
  add_project_arguments(
    '-DHAVE_SYMVER_ATTRIBUTE',
    language: 'c',
  )
else
  message('Compiler does not support symver attribute')
endif

# '.' will refer to current build directory, which contains config.h
include_dirs = include_directories('include', 'lib', '.')

#
# Read build files from sub-directories
#
subdirs = ['lib', 'include']
if get_option('utils') and not platform.endswith('bsd') and platform != 'dragonfly'
  subdirs += 'util'
endif

foreach n : subdirs
  subdir(n)
endforeach
