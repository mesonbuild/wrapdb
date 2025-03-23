project(
  'libarchive',
  'c',
  version: '3.7.8',
  meson_version: '>=0.54.1',
)

cdata = configuration_data()
cdata.set('VERSION', meson.project_version())
cdata.set('BSDCAT_VERSION_STRING', meson.project_version())
cdata.set('BSDCPIO_VERSION_STRING', meson.project_version())
cdata.set('BSDTAR_VERSION_STRING', meson.project_version())
cdata.set('LIBARCHIVE_VERSION_STRING', meson.project_version())
cdata.set('SAFE_TO_DEFINE_EXTENSIONS', 1)

cc = meson.get_compiler('c')
add_project_arguments(
  cc.get_supported_arguments('-Wformat', '-Wformat-security'),
  language: 'c',
)
add_project_arguments(
  '-DHAVE_CONFIG_H',
  language: 'c',
)
if host_machine.system() == 'windows'
  if get_option('default_library') == 'static'
    add_project_arguments(
      '-DLIBARCHIVE_STATIC',
      language: 'c',
    )
  endif
  if cc.sizeof('void*') == 4
    add_project_arguments(
      '-D__MINGW_USE_VC2005_COMPAT',
      language: 'c',
    )
  endif
  add_project_arguments(
    '-D_CRT_SECURE_NO_WARNINGS',
    language: 'c',
  )
  cdata.set(
    '_WIN32_WINNT',
    '0x0A00',
    description: 'Windows Server 2003 APIs',
  )
  cdata.set(
    'NTDDI_VERSION',
    '0x0A000000',
    description: 'Windows Server 2003 APIs',
  )
  cdata.set(
    'WINVER',
    '0x0A00',
    description: 'Windows Server 2003 APIs',
  )
else
  add_project_arguments(
    '-D__LIBARCHIVE_ENABLE_VISIBILITY',
    language: 'c',
  )
endif

if cc.sizeof('long') == 4
  cdata.set('_FILE_OFFSET_BITS', 64)
endif

sizes = [
  '__int64',
  'int16_t',
  'int32_t',
  'int64_t',
  'intmax_t',
  'uint8_t',
  'uint16_t',
  'uint32_t',
  'uint64_t',
  'uintmax_t',
  'unsigned __int64',
]
foreach s : sizes
  cdata.set(
    'HAVE_@0@'.format(s.underscorify().to_upper()),
    cc.has_type(
      s,
      prefix: '#include <stdint.h>',
    ),
  )
endforeach

sizes = [
  'short',
  'int',
  'long',
  'long long',
  'unsigned',
  'unsigned long',
  'unsigned long long',
  'unsigned short',
]

foreach s : sizes
  upper = s.underscorify().to_upper()
  cdata.set(
    'SIZEOF_@0@_CODE'.format(upper),
    '#define @0@ @1@'.format('SIZEOF_@0@'.format(upper), cc.sizeof(s)),
  )
endforeach

cdata.set10(
  'HAVE_WCHAR_T',
  cc.has_type(
    'wchar_t',
    prefix: '#include <wchar.h>',
  ),
)
cdata.set(
  'SIZEOF_WCHAR_T',
  cc.sizeof(
    'wchar_t',
    prefix: '#include <wchar.h>',
  ),
)

minmax = {
  'INT32_MAX': 'stdint.h',
  'INT32_MIN': 'stdint.h',
  'INT64_MAX': 'stdint.h',
  'INT64_MIN': 'stdint.h',
  'INTMAX_MAX': 'stdint.h',
  'INTMAX_MIN': 'stdint.h',
  'SIZE_MAX': 'stdint.h',
  'SSIZE_MAX': 'limits.h',
  'UINT32_MAX': 'stdint.h',
  'UINT64_MAX': 'stdint.h',
  'UINTMAX_MAX': 'stdint.h',
}

foreach m, h : minmax
  if cc.has_header_symbol(h, m)
    cdata.set('HAVE_DECL_@0@'.format(m), 1)
  endif
endforeach

mingw_funcs = {}

if cc.has_header_symbol('langinfo.h', 'D_MD_ORDER')
  cdata.set('HAVE_D_MD_ORDER', 1)
endif

if cc.has_header_symbol('linux/fs.h', 'FS_IOC_GETFLAGS')
  cdata.set('HAVE_WORKING_FS_IOC_GETFLAGS', 1)
endif

if cc.has_header_symbol('errno.h', 'EFTYPE')
  cdata.set('HAVE_EFTYPE', 1)
endif

if cc.has_header_symbol('errno.h', 'EILSEQ')
  cdata.set('HAVE_EILSEQ', 1)
endif

if cc.has_header_symbol('ext2fs/ext2_fs.h', 'EXT2_IOC_GETFLAGS')
  cdata.set('HAVE_WORKING_EXT2_IOC_GETFLAGS', 1)
endif

if cc.has_header_symbol('unistd.h', 'sysconf')
  cdata.set('HAVE_SYSCONF', 1)
endif

foreach w : ['_mkgmtime', 'ctime_s', 'gmtime_s', 'localtime_s']
  if cc.has_header_symbol('time.h', w)
    cdata.set('HAVE_@0@'.format(w.to_upper()), 1)
  endif
endforeach

mem = [
  'st_birthtime',
  'st_birthtimespec.tv_nsec',
  'st_mtimespec.tv_nsec',
  'st_mtim.tv_nsec',
  'st_mtime_n',
  'st_umtime',
  'st_mtime_usec',
  'st_blksize',
  'st_flags',
]
foreach m : mem
  if cc.has_member(
    'struct stat',
    m,
    prefix: '#include <sys/stat.h>',
  )
    cdata.set('HAVE_STRUCT_STAT_@0@'.format(m.underscorify().to_upper()), 1)
  endif
endforeach

if cc.has_member(
  'struct tm',
  'tm_gmtoff',
  prefix: '#include <time.h>',
)
  cdata.set('HAVE_STRUCT_TM_TM_GMTOFF', 1)
endif

foreach a : ['acl_t', 'acl_entry_t', 'acl_permset_t', 'acl_tag_t']
  if cc.has_type(
    a,
    prefix: '#include <sys/acl.h>',
  )
    cdata.set('HAVE_@0@'.format(a.to_upper()), 1)
  endif
endforeach

foreach h : ['dirent.h', 'sys/ndir.h', 'sys/dir.h', 'ndir.h']
  if cc.has_header_symbol(h, 'DIR')
    cdata.set('HAVE_@0@'.format(h.underscorify().to_upper()), 1)
    break
  endif
endforeach

foreach h : ['sys/types.h', 'sys/time.h', 'time.h']
  if cc.has_member(
    'struct tm',
    'tm_sec',
    prefix: '#include <@0@>'.format(h),
  )
    cdata.set('TIME_WITH_SYS_TIME', 1)
    break
  endif
endforeach

if cc.has_header_symbol('sys/sysmacros.h', 'major')
  cdata.set('MAJOR_IN_SYSMACROS', 1)
endif

if cc.has_header_symbol('crtdbg.h', '_CrtSetReportMode')
  cdata.set('HAVE__CrtSetReportMode', 1)
endif

types = {
  'dev_t': 'unsigned int',
  'id_t': 'short',
  'gid_t': 'short',
  'mode_t': 'unsigned short',
  'off_t': 'int64_t',
  'pid_t': 'int',
  'size_t': 'unsigned long',
  'ssize_t': 'ptrdiff_t',
  'uid_t': 'short',
}

foreach t, v : types
  if not cc.has_type(
    t,
    prefix: '#include <sys/types.h>',
    args: '-D_GNU_SOURCE',
  )
    cdata.set(t, v)
  endif
endforeach

if host_machine.system() in ['cygwin', 'linux']
  cdata.set('ARCHIVE_XATTR_LINUX', 1)
endif

deps = []
if meson.version().version_compare('>= 0.62')
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

if dl_dep.found()
  cdata.set('HAVE_DLFCN_H', 1)
endif

attr_dep = dependency(
  'libattr',
  disabler: true,
  required: get_option('xattr'),
)
if attr_dep.found()
  cdata.set('HAVE_LIBATTR', 1)
  deps += attr_dep
endif

# compression dependencies
zlib_dep = dependency(
  'zlib',
  disabler: true,
  required: get_option('zlib'),
)
if zlib_dep.found()
  cdata.set('HAVE_LIBZ', 1)
  cdata.set('HAVE_ZLIB_H', 1)
  deps += zlib_dep
endif

bz2_dep = dependency(
  'bzip2',
  disabler: true,
  required: get_option('bz2lib'),
)
if bz2_dep.found()
  cdata.set('HAVE_LIBBZ2', 1)
  deps += bz2_dep
endif

b2_dep = dependency(
  'libb2',
  disabler: true,
  required: get_option('libb2'),
)
if b2_dep.found()
  cdata.set('HAVE_LIBB2', 1)
  deps += b2_dep
endif

lz4_dep = dependency(
  'liblz4',
  disabler: true,
  required: get_option('lz4'),
)
if lz4_dep.found()
  cdata.set('HAVE_LIBLZ4', 1)
  deps += lz4_dep
endif

zstd_dep = dependency(
  'libzstd',
  disabler: true,
  required: get_option('zstd'),
)
if zstd_dep.found()
  cdata.set('HAVE_LIBZSTD', 1)
  cdata.set('HAVE_ZSTD_H', 1)
  deps += zstd_dep
  if zstd_dep.version().version_compare('>=0.8.1')
    cdata.set('HAVE_ZSTD_compressStream', 1)
  endif
endif

lzma_dep = dependency(
  'liblzma',
  disabler: true,
  required: get_option('lzma'),
)
if lzma_dep.found()
  cdata.set('HAVE_LIBLZMA', 1)
  deps += lzma_dep
  if lzma_dep.version().version_compare('>=5.2.0')
    cdata.set('HAVE_LZMA_STREAM_ENCODER_MT', 1)
  endif
endif

lzo2_dep = dependency(
  'lzo2',
  required: get_option('lzo2'),
)
if lzo2_dep.found()
  cdata.set('HAVE_LIBLZO2', 1)
  deps += lzo2_dep
endif

crypto_dep = dependency(
  'libcrypto',
  required: get_option('openssl'),
)
if crypto_dep.found()
  cdata.set('HAVE_LIBCRYPTO', 1)
  deps += crypto_dep
  foreach f : ['md5', 'rmd160', 'sha1', 'sha256', 'sha384', 'sha512']
    if not cc.has_header_symbol(
      'openssl/ssl.h',
      'OPENSSL_NO_@0@'.format(f.to_upper()),
    )
      cdata.set('ARCHIVE_CRYPTO_@0@_OPENSSL'.format(f.to_upper()), 1)
    endif
  endforeach
  if cc.has_header_symbol('openssl/evp.h', 'PKCS5_PBKDF2_HMAC_SHA1')
    cdata.set('HAVE_PKCS5_PBKDF2_HMAC_SHA1', 1)
  endif
endif

# just dependencies
xml2_dep = dependency(
  'libxml-2.0',
  required: get_option('xml2'),
)
if xml2_dep.found()
  cdata.set('HAVE_LIBXML2', 1)
  deps += xml2_dep
else
  expat_dep = dependency(
    'expat',
    required: get_option('expat'),
  )
  if expat_dep.found()
    cdata.set('HAVE_LIBEXPAT', 1)
    deps += expat_dep
  endif
endif

if meson.version().version_compare('>= 0.60')
  iconv_dep = dependency(
    'iconv',
    disabler: true,
    required: get_option('iconv'),
  )
elif get_option('iconv').enabled()
  error('Feature iconv cannot be enabled')
else
  iconv_dep = dependency(
    '',
    required: false,
  )
endif
if iconv_dep.found()
  cdata.set('HAVE_ICONV', 1)
  cdata.set(
    'ICONV_CONST',
    cc.compiles(
      '''
    #include <iconv.h>
    size_t iconv(iconv_t, const char**, size_t*, char**, size_t*);
    int main(){}
    ''',
      dependencies: iconv_dep,
    ) ? 'const' : '',
  )
  deps += iconv_dep
else
  cdata.set('ICONV_CONST', '')
endif

rx_support = false
rx_dep = dependency(
  '',
  required: false,
)
if not get_option('regex').disabled()
  foreach rx_support : get_option('regex_provider')
    if (rx_support == 'libc'
and cc.has_function(
      'regcomp',
      prefix: '#include <regex.h>',
    )
)
      rx_dep = declare_dependency()
      cdata.set('HAVE_REGEX_H', 1)
      break
    elif rx_support == 'libregex'
      regex_dep = cc.find_library(
        'regex',
        disabler: true,
        required: false,
      )
      if cc.has_function(
        'regcomp',
        dependencies: regex_dep,
        prefix: '#include <regex.h>',
      )
        rx_dep = regex_dep
        cdata.set('HAVE_REGEX_H', 1)
        break
      endif
    elif rx_support == 'libpcreposix'
      pcre_dep = dependency(
        'libpcreposix',
        disabler: true,
        required: false,
      )
      # Note: on macOS, Apple provides a system pcre with pkg-config but without headers…
      if cc.has_header(
        'pcreposix.h',
        dependencies: pcre_dep.partial_dependency(
          compile_args: true,
          includes: true,
        ),
      )
        rx_dep = pcre_dep
        cdata.set('HAVE_PCREPOSIX_H', 1)
        break
      endif
    elif rx_support == 'libpcre2posix'
      pcre2_dep = dependency(
        'libpcre2-posix',
        disabler: true,
        required: false,
      )
      if pcre2_dep.found()
        cdata.set('HAVE_PCRE2POSIX_H', 1)
        rx_dep = pcre2_dep
        break
      endif
    endif
  endforeach
  if not rx_dep.found()
    if get_option('regex').enabled()
      error('Feature regex cannot be enabled')
    endif
    rx_support = false
  endif
endif
deps += rx_dep

libacl_dep = dependency(
  'libacl',
  disabler: true,
  required: get_option('acl'),
)
if libacl_dep.found()
  cdata.set('HAVE_LIBACL', 1)
  cdata.set('ARCHIVE_ACL_LIBACL', 1)
  deps += libacl_dep
endif

headers = {
  'acl/libacl.h': libacl_dep.partial_dependency(
    compile_args: true,
    includes: true,
  ),
  'attr/xattr.h': attr_dep.partial_dependency(
    compile_args: true,
    includes: true,
  ),
  'blake2.h': b2_dep.partial_dependency(
    compile_args: true,
    includes: true,
  ),
  'bzlib.h': bz2_dep.partial_dependency(
    compile_args: true,
    includes: true,
  ),
  'copyfile.h': [],
  'ctype.h': [],
  'direct.h': [],
  'errno.h': [],
  'ext2fs/ext2_fs.h': [],
  'fcntl.h': [],
  'grp.h': [],
  'iconv.h': iconv_dep.partial_dependency(
    compile_args: true,
    includes: true,
  ),
  'inttypes.h': [],
  'io.h': [],
  'langinfo.h': [],
  'libxml/xmlreader.h': xml2_dep.partial_dependency(
    compile_args: true,
    includes: true,
  ),
  'libxml/xmlwriter.h': xml2_dep.partial_dependency(
    compile_args: true,
    includes: true,
  ),
  'limits.h': [],
  'linux/ext2_fs.h': [],
  'linux/fiemap.h': [],
  'linux/fs.h': [],
  'linux/magic.h': [],
  'linux/types.h': [],
  'localcharset.h': [],
  'locale.h': [],
  'lz4.h': lz4_dep.partial_dependency(
    compile_args: true,
    includes: true,
  ),
  'lz4hc.h': lz4_dep.partial_dependency(
    compile_args: true,
    includes: true,
  ),
  'lzma.h': lzma_dep.partial_dependency(
    compile_args: true,
    includes: true,
  ),
  'membership.h': [],
  'memory.h': [],
  'paths.h': [],
  'poll.h': [],
  'process.h': [],
  'pthread.h': [],
  'pwd.h': [],
  'readpassphrase.h': [],
  'signal.h': [],
  'spawn.h': [],
  'stdarg.h': [],
  'stdint.h': [],
  'stdlib.h': [],
  'string.h': [],
  'strings.h': [],
  'sys/acl.h': [],
  'sys/cdefs.h': [],
  'sys/ea.h': [],
  'sys/extattr.h': [],
  'sys/ioctl.h': [],
  'sys/mkdev.h': [],
  'sys/mount.h': [],
  'sys/param.h': [],
  'sys/poll.h': [],
  'sys/richacl.h': [],
  'sys/select.h': [],
  'sys/stat.h': [],
  'sys/statfs.h': [],
  'sys/statvfs.h': [],
  'sys/sysmacros.h': [],
  'sys/time.h': [],
  'sys/types.h': [],
  'sys/utime.h': [],
  'sys/utsname.h': [],
  'sys/vfs.h': [],
  'sys/wait.h': [],
  'sys/xattr.h': [],
  'time.h': [],
  'unistd.h': [],
  'utime.h': [],
  'wchar.h': [],
  'wctype.h': [],
  'wincrypt.h': [],
  'windows.h': [],
  'winioctl.h': [],
}

foreach h, d : headers
  if cc.has_header(
    h,
    dependencies: d,
  )
    cdata.set('HAVE_@0@'.format(h.underscorify().to_upper()), 1)
  endif
endforeach

functions = {
  'acl_create_entry': libacl_dep.partial_dependency(
    compile_args: true,
    includes: true,
  ),
  'acl_get_perm': libacl_dep.partial_dependency(
    compile_args: true,
    includes: true,
  ),
  'acl_init': libacl_dep.partial_dependency(
    compile_args: true,
    includes: true,
  ),
  'acl_set_fd': libacl_dep.partial_dependency(
    compile_args: true,
    includes: true,
  ),
  'acl_set_file': libacl_dep.partial_dependency(
    compile_args: true,
    includes: true,
  ),
  'arc4random_buf': [],
  'chflags': [],
  'chown': [],
  'chroot': [],
  'ctime_r': [],
  'cygwin_conv_path': [],
  'dirfd': [],
  'fchdir': [],
  'fchflags': [],
  'fchmod': [],
  'fchown': [],
  'fcntl': [],
  'fdopendir': [],
  'fgetxattr': [],
  'flistxattr': [],
  'fork': [],
  'fseeko': [],
  'fsetxattr': [],
  'fstat': [],
  'fstatat': [],
  'fstatfs': [],
  'fstatvfs': [],
  'ftruncate': [],
  'futimens': [],
  'futimes': [],
  'futimesat': [],
  'geteuid': [],
  'getgrgid_r': [],
  'getgrnam_r': [],
  'getpwnam_r': [],
  'getpwuid_r': [],
  'getpid': [],
  'getvfsbyname': [],
  'getxattr': [],
  'gmtime_r': [],
  'lchflags': [],
  'lchmod': [],
  'lchown': [],
  'lgetxattr': [],
  'link': [],
  'linkat': [],
  'listxattr': [],
  'llistxattr': [],
  'locale_charset': iconv_dep.partial_dependency(
    compile_args: true,
    includes: true,
  ),
  'localtime_r': [],
  'lsetxattr': [],
  'lstat': [],
  'lutimes': [],
  'mbrtowc': [],
  'memmove': [],
  'mkdir': [],
  'mkfifo': [],
  'mknod': [],
  'mkstemp': [],
  'nl_langinfo': [],
  'openat': [],
  'pipe': [],
  'poll': [],
  'posix_spawnp': [],
  'readdir_r': [],
  'readlink': [],
  'readlinkat': [],
  'readpassphrase': [],
  'select': [],
  'setenv': [],
  'setlocale': [],
  'setxattr': [],
  'sigaction': [],
  'statfs': [],
  'statvfs': [],
  'strchr': [],
  'strdup': [],
  'strerror': [],
  'strerror_r': [],
  'strftime': [],
  'strncpy_s': [],
  'strnlen': [],
  'strrchr': [],
  'symlink': [],
  'tcgetattr': [],
  'tcsetattr': [],
  'timegm': [],
  'tzset': [],
  'unlinkat': [],
  'unsetenv': [],
  'utime': [],
  'utimes': [],
  'utimensat': [],
  'vprintf': [],
  'vfork': [],
  'wcrtomb': [],
  'wcscmp': [],
  'wcscpy': [],
  'wcslen': [],
  'wctomb': [],
  'wmemcmp': [],
  'wmemcpy': [],
  'wmemmove': [],
  '_fseeki64': [],
  '_get_timezone': [],
}

foreach f, d : functions
  if cc.has_function(
    f,
    dependencies: d,
  )
    cdata.set('HAVE_@0@'.format(f.underscorify().to_upper()), 1)
  endif
endforeach

if cdata.has('HAVE_STRERROR_R')
  cdata.set('HAVE_DECL_STRERROR_R', 1)
endif

incdirs = include_directories('.')

subdir('libarchive')

if get_option('progs').length() > 0

  subdir('libarchive_fe')

  foreach _prog : ['cat', 'cpio', 'tar']
    if 'all' in get_option('progs') or 'bsd' + _prog in get_option('progs')
      subdir(_prog)
    endif
  endforeach

endif

summary(
  {
    'regex support': rx_support,
  },
  bool_yn: true,
)
