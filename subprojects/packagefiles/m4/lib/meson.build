cc = meson.get_compiler('c')
cdata = configuration_data()
generated_header_data = configuration_data()

if host_machine.cpu_family() == 'x86'
  cdata.set('__i386__', 1)
endif
if host_machine.cpu_family() == 'x86_64' and cc.get_define('__ILP32__') != '' or cc.get_define(
  '_ILP32',
) != ''
  cdata.set('__x86_64_x32__', 1)
endif
if host_machine.cpu_family() == 'x86_64' and cc.get_define('__ILP32__') == '' and cc.get_define(
  '_ILP32',
) == ''
  cdata.set('__x86_64__', 1)
endif
if host_machine.cpu_family() == 'alpha'
  cdata.set('__alpha__', 1)
endif
if host_machine.cpu_family() == 'arm' and cc.get_define('__ARM_PCS') != ''
  cdata.set('__arm__', 1)
endif
if host_machine.cpu_family() == 'arm' and cc.get_define('__ARM_PCS_VFP') != ''
  cdata.set('__armhf__', 1)
endif
if host_machine.cpu_family() == 'aarch64' and cc.get_define('__ILP32__') != '' or cc.get_define(
  '_ILP32',
) != ''
  cdata.set('__arm64_ilp32__', 1)
endif
if host_machine.cpu_family() == 'aarch64' and cc.get_define('__ILP32__') == '' and cc.get_define(
  '_ILP32',
) == ''
  cdata.set('__arm64__', 1)
endif
if host_machine.cpu_family() == 'parisc' and cc.get_define('__ILP64__') == '' and cc.get_define(
  '_ILP64',
) == ''
  cdata.set('__hppa__', 1)
endif
if host_machine.cpu_family() == 'parisc' and cc.get_define('__ILP64__') != '' or cc.get_define(
  '_ILP64',
) != ''
  cdata.set('__hppa64__', 1)
endif
if host_machine.cpu_family() == 'ia64' and cc.get_define('_ILP32') != ''
  cdata.set('__ia64_ilp32__', 1)
endif
if host_machine.cpu_family() == 'ia64' and cc.get_define('_ILP32') == ''
  cdata.set('__ia64__', 1)
endif
if host_machine.cpu_family() == 'm68k'
  cdata.set('__m68k__', 1)
endif
if host_machine.cpu_family() == 'mips' and cc.get_define('_MIPS_SIM') != cc.get_define(
  '_ABIN32',
)
  cdata.set('__mips__', 1)
endif
if host_machine.cpu_family() == 'mips' and cc.get_define('_MIPS_SIM') == cc.get_define(
  '_ABIN32',
)
  cdata.set('__mipsn32__', 1)
endif
if host_machine.cpu_family() == 'mips64'
  cdata.set('__mips64__', 1)
endif
if host_machine.cpu_family() == 'ppc'
  cdata.set('__powerpc__', 1)
endif
if host_machine.cpu_family() == 'ppc64' and cc.get_define('_CALL_ELF') != '2'
  cdata.set('__powerpc64__', 1)
endif
if host_machine.cpu_family() == 'ppc64' and cc.get_define('_CALL_ELF') == '2'
  cdata.set('__powerpc64_elfv2__', 1)
endif
if host_machine.cpu_family() == 'riscv32'
  cdata.set('__riscv32__', 1)
endif
if host_machine.cpu_family() == 'riscv64'
  cdata.set('__riscv64__', 1)
endif
if host_machine.cpu_family() == 'riscv32' and cc.get_define(
  '__riscv_float_abi_single',
) == '' and cc.get_define(
  '__riscv_float_abi_double',
) == ''
  cdata.set('__riscv32_ilp32__', 1)
endif
if host_machine.cpu_family() == 'riscv32' and cc.get_define(
  '__riscv_float_abi_single',
) != ''
  cdata.set('__riscv32_ilp32f__', 1)
endif
if host_machine.cpu_family() == 'riscv32' and cc.get_define(
  '__riscv_float_abi_double',
) != ''
  cdata.set('__riscv32_ilp32d__', 1)
endif
if host_machine.cpu_family() == 'riscv64' and cc.get_define('__LP64__') == '' and cc.get_define(
  '__riscv_float_abi_single',
) == '' and cc.get_define(
  '__riscv_float_abi_double',
) == ''
  cdata.set('__riscv64_ilp32__', 1)
endif
if host_machine.cpu_family() == 'riscv64' and cc.get_define('__LP64__') == '' and cc.get_define(
  '__riscv_float_abi_single',
) != ''
  cdata.set('__riscv64_ilp32f__', 1)
endif
if host_machine.cpu_family() == 'riscv64' and cc.get_define('__LP64__') == '' and cc.get_define(
  '__riscv_float_abi_double',
) != ''
  cdata.set('__riscv64_ilp32d__', 1)
endif
if host_machine.cpu_family() == 'riscv64' and cc.get_define('__LP64__') != '' and cc.get_define(
  '__riscv_float_abi_single',
) == '' and cc.get_define(
  '__riscv_float_abi_double',
) == ''
  cdata.set('__riscv64_lp64__', 1)
endif
if host_machine.cpu_family() == 'riscv64' and cc.get_define('__LP64__') != '' and cc.get_define(
  '__riscv_float_abi_single',
) != ''
  cdata.set('__riscv64_lp64f__', 1)
endif
if host_machine.cpu_family() == 'riscv64' and cc.get_define('__LP64__') != '' and cc.get_define(
  '__riscv_float_abi_double',
) != ''
  cdata.set('__riscv64_lp64d__', 1)
endif
if host_machine.cpu_family() == 's390'
  cdata.set('__s390__', 1)
endif
if host_machine.cpu_family() == 's390x'
  cdata.set('__s390x__', 1)
endif
if host_machine.cpu_family() == 'sh4'
  cdata.set('__sh__', 1)
endif
if host_machine.cpu_family() == 'sparc'
  cdata.set('__sparc__', 1)
endif
if host_machine.cpu_family() == 'sparc64'
  cdata.set('__sparc64__', 1)
endif

check_headers = [
  'alloca.h',
  'arpa/inet.h',
  'bp/sym.h',
  'crtdefs.h',
  'dirent.h',
  'error.h',
  'features.h',
  'getopt.h',
  'iconv.h',
  'inttypes.h',
  'langinfo.h',
  'libintl.h',
  'limits.h',
  'malloc.h',
  'math.h',
  'minix/config.h',
  'netdb.h',
  'netinet/in.h',
  'os.h',
  'paths.h',
  'pthread.h',
  'random.h',
  'regex.h',
  'sched.h',
  'sdkddkver.h',
  'search.h',
  'semaphore.h',
  'sigsegv.h',
  'spawn.h',
  'stdint.h',
  'stdio.h',
  'stdio_ext.h',
  'stdlib.h',
  'string.h',
  'strings.h',
  'sys/bitypes.h',
  'sys/cdefs.h',
  'sys/inttypes.h',
  'sys/ioctl.h',
  'sys/loadavg.h',
  'sys/mman.h',
  'sys/param.h',
  'sys/random.h',
  'sys/select.h',
  'sys/single_threaded.h',
  'sys/socket.h',
  'sys/stat.h',
  'sys/time.h',
  'sys/types.h',
  'sys/uio.h',
  'sys/wait.h',
  'threads.h',
  'unistd.h',
  'wchar.h',
  'wctype.h',
  'winsock2.h',
  'ws2tcpip.h',
  'xlocale.h',
]

have_header_args = []

foreach h : check_headers
  if cc.has_header(h)
    cdata.set('HAVE_' + h.underscorify().to_upper(), 1)
    have_header_args += '-DHAVE_' + h.underscorify().to_upper() + '=1'
    generated_header_data.set10('HAVE_' + h.underscorify().to_upper(), true)
  else
    generated_header_data.set10('HAVE_' + h.underscorify().to_upper(), false)
  endif
endforeach
if cc.has_header('stdlib.h') and cc.has_header('stdarg.h') and cc.has_header(
  'string.h',
) and cc.has_header(
  'float.h',
) and cc.has_header_symbol(
  'string.h',
  'memchr',
) and cc.has_header_symbol(
  'stdlib.h',
  'free',
)
  cdata.set('STDC_HEADERS', 1)
  have_header_args += '-DSTDC_HEADERS=1'
endif


ac_includes_default = '''#include <stdio.h>
#ifdef HAVE_SYS_TYPES_H
# include <sys/types.h>
#endif
#ifdef HAVE_SYS_STAT_H
# include <sys/stat.h>
#endif
#ifdef STDC_HEADERS
# include <stdlib.h>
# include <stddef.h>
#else
# ifdef HAVE_STDLIB_H
#  include <stdlib.h>
# endif
#endif
#ifdef HAVE_STRING_H
# if !defined STDC_HEADERS && defined HAVE_MEMORY_H
#  include <memory.h>
# endif
# include <string.h>
#endif
#ifdef HAVE_STRINGS_H
# include <strings.h>
#endif
#ifdef HAVE_INTTYPES_H
# include <inttypes.h>
#endif
#ifdef HAVE_STDINT_H
# include <stdint.h>
#endif
#ifdef HAVE_UNISTD_H
# include <unistd.h>
#endif'''

extension_args = []

unconditional_extensions = [
  '_ALL_SOURCE',
  '_DARWIN_C_SOURCE',
  '_GNU_SOURCE',
  '_HPUX_ALT_XOPEN_SOCKET_API',
  '_NETBSD_SOURCE',
  '_OPENBSD_SOURCE',
  '_POSIX_PTHREAD_SEMANTICS',
  '__STDC_WANT_IEC_60559_ATTRIBS_EXT__',
  '__STDC_WANT_IEC_60559_BFP_EXT__',
  '__STDC_WANT_IEC_60559_DFP_EXT__',
  '__STDC_WANT_IEC_60559_FUNCS_EXT__',
  '__STDC_WANT_IEC_60559_TYPES_EXT__',
  '__STDC_WANT_LIB_EXT2__',
  '__STDC_WANT_MATH_SPEC_FUNCS__',
  '_TANDEM_SOURCE',
]

foreach ext : unconditional_extensions
  cdata.set(ext, 1)
  extension_args += '-D' + ext + '=1'
endforeach

if cc.compiles(
  '#define __EXTENSIONS__ 1\n' + ac_includes_default,
  args: have_header_args,
)
  cdata.set('__EXTENSIONS__', 1)
  extension_args += '-D__EXTENSIONS__=1'
endif
if host_machine.system() == 'minix'
  cdata.set('_MINIX', 1)
  extension_args += '-D_MINIX=1'
endif
if host_machine.system() == 'minix'
  cdata.set('_POSIX_SOURCE', 1)
  extension_args += '-D_POSIX_SOURCE=1'
endif
if host_machine.system() == 'minix'
  cdata.set('_POSIX_1_SOURCE', 2)
  extension_args += '-D_POSIX_1_SOURCE=2'
endif
if not cc.compiles('#include <wchar.h>\\nmbstate_t x;') and cc.compiles(
  '#define _XOPEN_SOURCE 500\\n#include <wchar.h>\\nmbstate_t x;',
)
  cdata.set('_XOPEN_SOURCE', 500)
  extension_args += '-D_XOPEN_SOURCE=500'
endif


check_types = [
  ['HAVE_INTMAX_T', 'intmax_t', 'stdint.h'],
  ['HAVE_INTTYPES_H_WITH_UINTMAX', 'uintmax_t', 'inttypes.h'],
  ['HAVE_MAX_ALIGN_T', 'max_align_t', 'stddef.h'],
  ['HAVE_MODE_T', 'mode_t', 'sys/types.h'],
  ['HAVE_PID_T', 'pid_t', 'sys/types.h'],
  ['HAVE_POSIX_SPAWNATTR_T', 'posix_spawnattr_t', 'spawn.h'],
  ['HAVE_POSIX_SPAWN_FILE_ACTIONS_T', 'posix_spawn_file_actions_t', 'spawn.h'],
  ['HAVE_PTHREAD_T', 'pthread_t', 'pthread.h'],
  ['HAVE_SA_FAMILY_T', 'sa_family_t', 'sys/socket.h'],
  ['HAVE_SIGHANDLER_T', 'sighandler_t', 'signal.h'],
  ['HAVE_SIGINFO_T', 'siginfo_t', 'signal.h'],
  ['HAVE_SIGSET_T', 'sigset_t', 'signal.h'],
  ['HAVE_SIG_ATOMIC_T', 'sig_atomic_t', 'signal.h'],
  ['HAVE_SSIZE_T', 'ssize_t', 'sys/types.h'],
  ['HAVE_STDINT_H_WITH_UINTMAX', 'uintmax_t', 'stdint.h'],
  ['HAVE_STRUCT_RANDOM_DATA', 'struct random_data', 'stdlib.h'],
  ['HAVE_STRUCT_SOCKADDR_STORAGE', 'struct sockaddr_storage', 'sys/socket.h'],
  ['HAVE_TYPE_VOLATILE_SIG_ATOMIC_T', 'sig_atomic_t', 'signal.h'],
  ['HAVE_UID_T', 'uid_t', 'sys/types.h'],
  ['HAVE_UNSIGNED_LONG_LONG_INT', 'unsigned long long', 'stdint.h'],
  ['HAVE_WCHAR_T', 'wchar_t', 'wchar.h'],
  ['HAVE_WINT_T', 'wint_t', 'wchar.h'],
  ['HAVE__BOOL', '_Bool', 'stdint.h'],
]
foreach f : check_types
  if cc.has_type(
    f.get(1),
    prefix: '#include <@0@>'.format(f.get(2)),
    args: extension_args,
  )
    cdata.set(f.get(0), 1)
    generated_header_data.set10(f.get(0), true)
  else
    generated_header_data.set10(f.get(0), false)
  endif

endforeach

if cc.compiles(
  '''#include <signal.h>
struct sigaction m_sigaction;
void f(void) { (void)m_sigaction.sa_sigaction; }''',
  name: 'struct sigaction has sa_sigaction member',
)
  cdata.set('HAVE_STRUCT_SIGACTION_SA_SIGACTION', 1)
  generated_header_data.set10('HAVE_STRUCT_SIGACTION_SA_SIGACTION', true)
else
  generated_header_data.set10('HAVE_STRUCT_SIGACTION_SA_SIGACTION', false)
endif

# Bcrypt
if host_machine.system() == 'windows'
  if cc.has_header(
    'bcrypt.h',
    prefix: '#include <windows.h>',
  )
    cdata.set('HAVE_BCRYPT_H', 1)
    generated_header_data.set10('HAVE_BCRYPT_H', true)

    if cc.compiles(
      '''#include <windows.h>
#if !(_WIN32_WINNT >= _WIN32_WINNT_WIN7)
  cannot assume it
#endif''',
    )
      cdata.set10('HAVE_LIB_BCRYPT', true)
      generated_header_data.set10('HAVE_LIB_BCRYPT', true)
      getrandom_dep = cc.find_library('bcrypt')
    else
      generated_header_data.set10('HAVE_LIB_BCRYPT', false)
      getrandom_dep = cc.find_library('advapi32')
    endif
  else
    generated_header_data.set10('HAVE_BCRYPT_H', false)
    generated_header_data.set10('HAVE_LIB_BCRYPT', false)
    getrandom_dep = cc.find_library('advapi32')
  endif
endif

check_declarations = [
  ['HAVE_DECL_ALARM', 'alarm', 'unistd.h'],
  ['HAVE_DECL_CLEARERR_UNLOCKED', 'clearerr_unlocked', 'stdio.h'],
  ['HAVE_DECL_COPYSIGN', 'copysign', 'math.h'],
  ['HAVE_DECL_COPYSIGNF', 'copysignf', 'math.h'],
  ['HAVE_DECL_COPYSIGNL', 'copysignl', 'math.h'],
  ['HAVE_DECL_DIRFD', 'dirfd', 'dirent.h'],
  ['HAVE_DECL_EACCESS', 'eaccess', 'unistd.h'],
  ['HAVE_DECL_ECVT', 'ecvt', 'stdlib.h'],
  ['HAVE_DECL_EXECVPE', 'execvpe', 'unistd.h'],
  ['HAVE_DECL_FCHDIR', 'fchdir', 'unistd.h'],
  ['HAVE_DECL_FCLOSEALL', 'fcloseall', 'stdio.h'],
  ['HAVE_DECL_FCVT', 'fcvt', 'stdlib.h'],
  ['HAVE_DECL_FDATASYNC', 'fdatasync', 'unistd.h'],
  ['HAVE_DECL_FDOPENDIR', 'fdopendir', 'dirent.h'],
  ['HAVE_DECL_FEOF_UNLOCKED', 'feof_unlocked', 'stdio.h'],
  ['HAVE_DECL_FERROR_UNLOCKED', 'ferror_unlocked', 'stdio.h'],
  ['HAVE_DECL_FFLUSH_UNLOCKED', 'fflush_unlocked', 'stdio.h'],
  ['HAVE_DECL_FGETS_UNLOCKED', 'fgets_unlocked', 'stdio.h'],
  ['HAVE_DECL_FPURGE', 'fpurge', 'stdio.h'],
  ['HAVE_DECL_FPUTC_UNLOCKED', 'fputc_unlocked', 'stdio.h'],
  ['HAVE_DECL_FPUTS_UNLOCKED', 'fputs_unlocked', 'stdio.h'],
  ['HAVE_DECL_FREAD_UNLOCKED', 'fread_unlocked', 'stdio.h'],
  ['HAVE_DECL_FSEEKO', 'fseeko', 'stdio.h'],
  ['HAVE_DECL_FTELLO', 'ftello', 'stdio.h'],
  ['HAVE_DECL_FWRITE_UNLOCKED', 'fwrite_unlocked', 'stdio.h'],
  ['HAVE_DECL_GCVT', 'gcvt', 'stdlib.h'],
  ['HAVE_DECL_GETCHAR_UNLOCKED', 'getchar_unlocked', 'stdio.h'],
  ['HAVE_DECL_GETCWD', 'getcwd', 'unistd.h'],
  ['HAVE_DECL_GETC_UNLOCKED', 'getc_unlocked', 'stdio.h'],
  ['HAVE_DECL_GETDELIM', 'getdelim', 'stdio.h'],
  ['HAVE_DECL_GETDOMAINNAME', 'getdomainname', 'unistd.h'],
  ['HAVE_DECL_GETDTABLESIZE', 'getdtablesize', 'unistd.h'],
  ['HAVE_DECL_GETLINE', 'getline', 'stdio.h'],
  ['HAVE_DECL_GETLOADAVG', 'getloadavg', 'stdlib.h'],
  ['HAVE_DECL_GETLOGIN', 'getlogin', 'unistd.h'],
  ['HAVE_DECL_GETLOGIN_R', 'getlogin_r', 'unistd.h'],
  ['HAVE_DECL_GETPAGESIZE', 'getpagesize', 'unistd.h'],
  ['HAVE_DECL_GETUSERSHELL', 'getusershell', 'unistd.h'],
  ['HAVE_DECL_INET_PTON', 'inet_pton', 'arpa/inet.h'],
  ['HAVE_DECL_INITSTATE', 'initstate', 'stdlib.h'],
  ['HAVE_DECL_ISBLANK', 'isblank', 'ctype.h'],
  ['HAVE_DECL_ISWBLANK', 'iswblank', 'wctype.h'],
  ['HAVE_DECL_MBRTOWC', 'mbrtowc', 'wchar.h'],
  ['HAVE_DECL_MBSINIT', 'mbsinit', 'wchar.h'],
  ['HAVE_DECL_MEMMEM', 'memmem', 'string.h'],
  ['HAVE_DECL_MEMRCHR', 'memrchr', 'string.h'],
  ['HAVE_DECL_OBSTACK_PRINTF', 'obstack_printf', 'stdio.h'],
  ['HAVE_DECL_O_CLOEXEC', 'O_CLOEXEC', 'fcntl.h'],
  ['HAVE_DECL_POSIX_SPAWN', 'posix_spawn', 'spawn.h'],
  ['HAVE_DECL_PROGRAM_INVOCATION_NAME', 'program_invocation_name', 'errno.h'],
  [
    'HAVE_DECL_PROGRAM_INVOCATION_SHORT_NAME',
    'program_invocation_short_name',
    'errno.h',
  ],
  ['HAVE_DECL_PUTCHAR_UNLOCKED', 'putchar_unlocked', 'stdio.h'],
  ['HAVE_DECL_PUTC_UNLOCKED', 'putc_unlocked', 'stdio.h'],
  ['HAVE_DECL_SETENV', 'setenv', 'stdlib.h'],
  ['HAVE_DECL_SETHOSTNAME', 'sethostname', 'unistd.h'],
  ['HAVE_DECL_SETSTATE', 'setstate', 'stdlib.h'],
  ['HAVE_DECL_SLEEP', 'sleep', 'unistd.h'],
  ['HAVE_DECL_SNPRINTF', 'snprintf', 'stdio.h'],
  ['HAVE_DECL_STRDUP', 'strdup', 'string.h'],
  ['HAVE_DECL_STRERROR_R', 'strerror_r', 'string.h'],
  ['HAVE_DECL_STRNDUP', 'strndup', 'string.h'],
  ['HAVE_DECL_STRNLEN', 'strnlen', 'string.h'],
  ['HAVE_DECL_STRSIGNAL', 'strsignal', 'string.h'],
  ['HAVE_DECL_STRTOK_R', 'strtok_r', 'string.h'],
  ['HAVE_DECL_SYS_SIGLIST', 'sys_siglist', 'signal.h'],
  ['HAVE_DECL_TOWLOWER', 'towlower', 'wctype.h'],
  ['HAVE_DECL_TRUNCATE', 'truncate', 'unistd.h'],
  ['HAVE_DECL_TTYNAME_R', 'ttyname_r', 'unistd.h'],
  ['HAVE_DECL_UNSETENV', 'unsetenv', 'stdlib.h'],
  ['HAVE_DECL_VSNPRINTF', 'vsnprintf', 'stdio.h'],
  ['HAVE_DECL_WCRTOMB', 'wcrtomb', 'wchar.h'],
  ['HAVE_DECL_WCSDUP', 'wcsdup', 'wchar.h'],
  ['HAVE_DECL_WCTOB', 'wctob', 'wchar.h'],
  ['HAVE_DECL_WCWIDTH', 'wcwidth', 'wchar.h'],
  ['HAVE_DECL__FSEEKI64', '_fseeki64', 'stdio.h'],
  ['HAVE_DECL__PUTENV', '_putenv', 'stdlib.h'],
  ['HAVE_DECL__SNPRINTF', '_snprintf', 'stdio.h'],
  ['HAVE_DECL__SYS_SIGLIST', '_sys_siglist', 'signal.h'],
  ['HAVE_DECL___ARGV', '__argv', 'stdlib.h'],
  ['HAVE_DECL___FPENDING', '__fpending', 'stdio_ext.h'],
  ['HAVE_DECL_ENVIRON', 'environ', 'unistd.h'],
  ['HAVE_ENVIRON_DECL', 'environ', 'unistd.h'],
  ['HAVE_LC_MESSAGES', 'LC_MESSAGES', 'locale.h'],
  ['HAVE_MAP_ANONYMOUS', 'MAP_ANONYMOUS', 'sys/mman.h'],
  ['HAVE_OBSTACK', 'obstack_init', 'obstack.h'],  # it's a define
  ['HAVE_PTHREAD_MUTEX_RECURSIVE', 'PTHREAD_MUTEX_RECURSIVE', 'pthread.h'],
  ['HAVE_VAR___PROGNAME', '__progname', 'stdlib.h'],
]

# HAVe_DECL_FOO tends to want to be explicitly 1 or 0, rather than 1 or undefined.
foreach f : check_declarations
  cdata.set10(
    f.get(0),
    cc.has_header_symbol(
      f.get(2),
      f.get(1),
      prefix: ac_includes_default,
      args: have_header_args + extension_args,
    ),
  )
endforeach

check_functions = [
  ['HAVE_MBRLEN', 'mbrlen', '#include<wchar.h>'],
  ['HAVE_MBSNRTOWCS', 'mbsnrtowcs', '#include<wchar.h>'],
  ['HAVE_MBSRTOWCS', 'mbsrtowcs', '#include<wchar.h>'],
  ['HAVE_WCPCPY', 'wcpcpy', '#include<wchar.h>'],
  ['HAVE_WCPNCPY', 'wcpncpy', '#include<wchar.h>'],
  ['HAVE_WCSCASECMP', 'wcscasecmp', '#include<wchar.h>'],
  ['HAVE_WCSCAT', 'wcscat', '#include<wchar.h>'],
  ['HAVE_WCSCHR', 'wcschr', '#include<wchar.h>'],
  ['HAVE_WCSCMP', 'wcscmp', '#include<wchar.h>'],
  ['HAVE_WCSCOLL', 'wcscoll', '#include<wchar.h>'],
  ['HAVE_WCSCPY', 'wcscpy', '#include<wchar.h>'],
  ['HAVE_WCSCSPN', 'wcscspn', '#include<wchar.h>'],
  ['HAVE_WCSDUP', 'wcsdup', '#include<wchar.h>'],
  ['HAVE_WCSFTIME', 'wcsftime', '#include<wchar.h>'],
  ['HAVE_WCSNCASECMP', 'wcsncasecmp', '#include<wchar.h>'],
  ['HAVE_WCSNCAT', 'wcsncat', '#include<wchar.h>'],
  ['HAVE_WCSNCMP', 'wcsncmp', '#include<wchar.h>'],
  ['HAVE_WCSNCPY', 'wcsncpy', '#include<wchar.h>'],
  ['HAVE_WCSNRTOMBS', 'wcsnrtombs', '#include<wchar.h>'],
  ['HAVE_WCSPBRK', 'wcspbrk', '#include<wchar.h>'],
  ['HAVE_WCSRCHR', 'wcsrchr', '#include<wchar.h>'],
  ['HAVE_WCSRTOMBS', 'wcsrtombs', '#include<wchar.h>'],
  ['HAVE_WCSSPN', 'wcsspn', '#include<wchar.h>'],
  ['HAVE_WCSSTR', 'wcsstr', '#include<wchar.h>'],
  ['HAVE_WCSTOK', 'wcstok', '#include<wchar.h>'],
  ['HAVE_WCSWIDTH', 'wcswidth', '#include<wchar.h>'],
  ['HAVE_WCSXFRM', 'wcsxfrm', '#include<wchar.h>'],
  ['HAVE_WMEMCHR', 'wmemchr', '#include<wchar.h>'],
  ['HAVE_WMEMCMP', 'wmemcmp', '#include<wchar.h>'],
  ['HAVE_WMEMCPY', 'wmemcpy', '#include<wchar.h>'],
  ['HAVE_WMEMMOVE', 'wmemmove', '#include<wchar.h>'],
  ['HAVE_WMEMPCPY', 'wmempcpy', '#include<wchar.h>'],
  ['HAVE_WMEMSET', 'wmemset', '#include<wchar.h>'],
  ['HAVE_FUTIMENS', 'futimens', '#include<sys/stat.h>'],
  ['HAVE_GETUMASK', 'getumask', '#include<sys/stat.h>'],
  ['HAVE_LCHMOD', 'lchmod', '#include<sys/stat.h>'],
  ['HAVE_MKDIRAT', 'mkdirat', '#include<sys/stat.h>'],
  ['HAVE_MKFIFO', 'mkfifo', '#include<sys/stat.h>'],
  ['HAVE_MKFIFOAT', 'mkfifoat', '#include<sys/stat.h>'],
  ['HAVE_MKNOD', 'mknod', '#include<sys/stat.h>'],
  ['HAVE_MKNODAT', 'mknodat', '#include<sys/stat.h>'],
  ['HAVE_UTIMENSAT', 'utimensat', '#include<sys/stat.h>'],
  ['HAVE_LANGINFO_CODESET', 'CODESET', '#include<langinfo.h>'],
  ['HAVE_LANGINFO_T_FMT_AMPM', 'T_FMT_AMPM', '#include<langinfo.h>'],
  ['HAVE_LANGINFO_ALTMON', 'ALTMON_1', '#include<langinfo.h>'],
  ['HAVE_LANGINFO_ERA', 'ERA', '#include<langinfo.h>'],
  ['HAVE_LANGINFO_YESEXPR', 'YESEXPR', '#include<langinfo.h>'],
  ['HAVE_ALIGNED_ALLOC', 'aligned_alloc', '#include<stdlib.h>'],
  ['HAVE_ALLOCA', 'alloca', '#include<alloca.h>'],
  ['HAVE_ATOLL', 'atoll', '#include<stdlib.h>'],
  ['HAVE_BTOWC', 'btowc', '#include<wchar.h>'],
  [
    'HAVE_CANONICALIZE_FILE_NAME',
    'canonicalize_file_name',
    '#include<stdlib.h>',
  ],
  ['HAVE_CATGETS', 'catgets', '#include<nl_types.h>'],
  [
    'HAVE_CFLOCALECOPYPREFERREDLANGUAGES',
    'CFLocaleCopyPreferredLanguages',
    '#include<CoreFoundation/CFLocale.h>',
  ],
  [
    'HAVE_CFPREFERENCESCOPYAPPVALUE',
    'CFPreferencesCopyAppValue',
    '#include<CoreFoundation/CFPreferences.h>',
  ],
  ['HAVE_CHOWN', 'chown', '#include<unistd.h>'],
  ['HAVE_CLOCK_GETTIME', 'clock_gettime', '#include<time.h>'],
  ['HAVE_CLOCK_SETTIME', 'clock_settime', '#include<time.h>'],
  ['HAVE_CLOSEDIR', 'closedir', '#include<dirent.h>'],
  ['HAVE_CLOSE_RANGE', 'close_range', '#include<linux/close_range.h>'],
  ['HAVE_CONFSTR', 'confstr', '#include<unistd.h>'],
  ['HAVE_COPYSIGNF_IN_LIBC', 'copysignf', '#include<math.h>'],
  ['HAVE_COPYSIGNL_IN_LIBC', 'copysignl', '#include<math.h>'],
  ['HAVE_COPYSIGN_IN_LIBC', 'copysign', '#include<math.h>'],
  ['HAVE_COPY_FILE_RANGE', 'copy_file_range', '#include<unistd.h>'],
  ['HAVE_DCGETTEXT', 'dcgettext', '#include<libintl.h>'],
  ['HAVE_DIRFD', 'dirfd', '#include<dirent.h>'],
  ['HAVE_DPRINTF', 'dprintf', '#include<stdio.h>'],
  ['HAVE_DUP3', 'dup3', '#include<unistd.h>'],
  ['HAVE_DUPLOCALE', 'duplocale', '#include<locale.h>'],
  ['HAVE_ERROR_AT_LINE', 'error_at_line', '#include<error.h>'],
  ['HAVE_EUIDACCESS', 'euidaccess', '#include<unistd.h>'],
  ['HAVE_EXECVPE', 'execvpe', '#include<unistd.h>'],
  ['HAVE_EXPLICIT_BZERO', 'explicit_bzero', '#include<string.h>'],
  ['HAVE_EXPLICIT_MEMSET', 'explicit_memset', '#include<string.h>'],
  ['HAVE_FACCESSAT', 'faccessat', '#include<unistd.h>'],
  ['HAVE_FCHDIR', 'fchdir', '#include<unistd.h>'],
  ['HAVE_FCHMODAT', 'fchmodat', '#include<sys/stat.h>'],
  ['HAVE_FCHOWNAT', 'fchownat', '#include<unistd.h>'],
  ['HAVE_FCNTL', 'fcntl', '#include<fcntl.h>'],
  ['HAVE_FDATASYNC', 'fdatasync', '#include<unistd.h>'],
  ['HAVE_FDOPENDIR', 'fdopendir', '#include<dirent.h>'],
  ['HAVE_FFSL', 'ffsl', '#include<strings.h>'],
  ['HAVE_FFSLL', 'ffsll', '#include<strings.h>'],
  ['HAVE_FPURGE', 'fpurge', '#include<stdio.h>'],
  ['HAVE_FREELOCALE', 'freelocale', '#include<locale.h>'],
  ['HAVE_FREE_POSIX', 'free', '#include<stdlib.h>'],
  ['HAVE_FREXPL_IN_LIBC', 'frexpl', '#include<math.h>'],
  ['HAVE_FREXP_IN_LIBC', 'frexp', '#include<math.h>'],
  ['HAVE_FSEEKO', 'fseeko', '#include<stdio.h>'],
  ['HAVE_FSTATAT', 'fstatat', '#include<sys/stat.h>'],
  ['HAVE_FSYNC', 'fsync', '#include<unistd.h>'],
  ['HAVE_FTRUNCATE', 'ftruncate', '#include<unistd.h>'],
  ['HAVE_GETCWD', 'getcwd', '#include<unistd.h>'],
  ['HAVE_GETDTABLESIZE', 'getdtablesize', '#include<unistd.h>'],
  ['HAVE_GETEGID', 'getegid', '#include<unistd.h>'],
  ['HAVE_GETENTROPY', 'getentropy', '#include<unistd.h>'],
  ['HAVE_GETEUID', 'geteuid', '#include<unistd.h>'],
  ['HAVE_GETEXECNAME', 'getexecname', '#include<stdlib.h>'],
  ['HAVE_GETGID', 'getgid', '#include<unistd.h>'],
  ['HAVE_GETGROUPS', 'getgroups', '#include<unistd.h>'],
  ['HAVE_GETHOSTNAME', 'gethostname', '#include<unistd.h>'],
  ['HAVE_GETLOCALENAME_L', 'getlocalename_l', '#include<locale.h>'],
  ['HAVE_GETOPT_LONG_ONLY', 'getopt_long_only', '#include<getopt.h>'],
  ['HAVE_GETPAGESIZE', 'getpagesize', '#include<unistd.h>'],
  ['HAVE_GETPASS', 'getpass', '#include<unistd.h>'],
  ['HAVE_GETPROGNAME', 'getprogname', '#include<stdlib.h>'],
  ['HAVE_GETRANDOM', 'getrandom', '#include<sys/random.h>'],
  ['HAVE_GETRLIMIT', 'getrlimit', '#include<sys/resource.h>'],
  ['HAVE_GETSUBOPT', 'getsubopt', '#include<stdlib.h>'],
  ['HAVE_GETTEXT', 'gettext', '#include<libintl.h>'],
  ['HAVE_GETTIMEOFDAY', 'gettimeofday', '#include<sys/time.h>'],
  ['HAVE_GETUID', 'getuid', '#include<unistd.h>'],
  ['HAVE_GOOD_USELOCALE', 'uselocale', '#include<locale.h>'],
  ['HAVE_GRANTPT', 'grantpt', '#include<stdlib.h>'],
  ['HAVE_GROUP_MEMBER', 'group_member', '#include<unistd.h>'],
  ['HAVE_ICONV', 'iconv', '#include<iconv.h>'],
  ['HAVE_INET_PTON', 'inet_pton', '#include<arpa/inet.h>'],
  ['HAVE_INITSTATE', 'initstate', '#include<stdlib.h>'],
  ['HAVE_IOCTL', 'ioctl', '#include<sys/ioctl.h>'],
  ['HAVE_ISBLANK', 'isblank', '#include<ctype.h>'],
  ['HAVE_ISNAND_IN_LIBC', 'isnand', '#include<ieeefp.h>'],
  ['HAVE_ISNANF_IN_LIBC', 'isnanf', '#include<ieeefp.h>'],
  ['HAVE_ISNANL_IN_LIBC', 'isnanl', '#include<ieeefp.h>'],
  ['HAVE_ISSETUGID', 'issetugid', '#include<unistd.h>'],
  ['HAVE_ISWBLANK', 'iswblank', '#include<wctype.h>'],
  ['HAVE_ISWCNTRL', 'iswcntrl', '#include<wctype.h>'],
  ['HAVE_ISWCTYPE', 'iswctype', '#include<wctype.h>'],
  ['HAVE_LANGINFO_CODESET', 'nl_langinfo', '#include<langinfo.h>'],
  ['HAVE_LCHOWN', 'lchown', '#include<unistd.h>'],
  ['HAVE_LDEXPL_IN_LIBC', 'ldexpl', '#include<math.h>'],
  ['HAVE_LDEXP_IN_LIBC', 'ldexp', '#include<math.h>'],
  ['HAVE_LINK', 'link', '#include<unistd.h>'],
  ['HAVE_LINKAT', 'linkat', '#include<unistd.h>'],
  ['HAVE_LSTAT', 'lstat', '#include<sys/stat.h>'],
  ['HAVE_MALLOC_POSIX', 'malloc', '#include<stdlib.h>'],
  ['HAVE_MBRTOWC', 'mbrtowc', '#include<wchar.h>'],
  ['HAVE_MBSINIT', 'mbsinit', '#include<wchar.h>'],
  ['HAVE_MBSLEN', 'mbslen', '#include<wchar.h>'],
  ['HAVE_MBSSTR', 'mbsstr', '#include<wchar.h>'],
  ['HAVE_MBTOWC', 'mbtowc', '#include<wchar.h>'],
  ['HAVE_MEMPCPY', 'mempcpy', '#include<string.h>'],
  ['HAVE_MEMRCHR', 'memrchr', '#include<string.h>'],
  ['HAVE_MEMSET_S', 'memset_s', '#include<string.h>'],
  ['HAVE_MKDTEMP', 'mkdtemp', '#include<stdlib.h>'],
  ['HAVE_MKOSTEMP', 'mkostemp', '#include<stdlib.h>'],
  ['HAVE_MKOSTEMPS', 'mkostemps', '#include<stdlib.h>'],
  ['HAVE_MKSTEMP', 'mkstemp', '#include<stdlib.h>'],
  ['HAVE_MKSTEMPS', 'mkstemps', '#include<stdlib.h>'],
  ['HAVE_MPROTECT', 'mprotect', '#include<sys/mman.h>'],
  ['HAVE_MQUERY', 'mquery', '#include<sys/mman.h>'],
  [
    'HAVE_MSVC_INVALID_PARAMETER_HANDLER',
    '_set_invalid_parameter_handler',
    '#include<stdlib.h>',
  ],
  ['HAVE_NEWLOCALE', 'newlocale', '#include<locale.h>'],
  ['HAVE_NL_LANGINFO', 'nl_langinfo', '#include<langinfo.h>'],
  ['HAVE_OPENAT', 'openat', '#include<fcntl.h>'],
  ['HAVE_OPENDIR', 'opendir', '#include<dirent.h>'],
  ['HAVE_PCLOSE', 'pclose', '#include<stdio.h>'],
  ['HAVE_PIPE', 'pipe', '#include<unistd.h>'],
  ['HAVE_PIPE2', 'pipe2', '#include<unistd.h>'],
  ['HAVE_POPEN', 'popen', '#include<stdio.h>'],
  ['HAVE_POSIX_MEMALIGN', 'posix_memalign', '#include<stdlib.h>'],
  ['HAVE_POSIX_OPENPT', 'posix_openpt', '#include<stdlib.h>'],
  ['HAVE_POSIX_SPAWN', 'posix_spawn', '#include<spawn.h>'],
  [
    'HAVE_POSIX_SPAWN_FILE_ACTIONS_ADDCHDIR',
    'posix_spawn_file_actions_addchdir',
    '#include <spawn.h>',
  ],
  [
    'HAVE_POSIX_SPAWN_FILE_ACTIONS_ADDFCHDIR',
    'posix_spawn_file_actions_addfchdir',
    '#include <spawn.h>',
  ],
  ['HAVE_PREAD', 'pread', '#include<unistd.h>'],
  ['HAVE_PSTAT_GETPROCVM', 'pstat_getprocvm', '#include<sys/pstat.h>'],
  ['HAVE_PTHREAD_ATFORK', 'pthread_atfork', '#include<pthread.h>'],
  ['HAVE_PTHREAD_RWLOCK', 'pthread_rwlock_init', '#include<pthread.h>'],
  ['HAVE_PTHREAD_SIGMASK', 'pthread_sigmask', '#include<signal.h>'],
  ['HAVE_PTHREAD_SPINLOCK_T', 'pthread_spin_init', '#include<pthread.h>'],
  ['HAVE_PTSNAME', 'ptsname', '#include<stdlib.h>'],
  ['HAVE_PTSNAME_R', 'ptsname_r', '#include<stdlib.h>'],
  ['HAVE_PWRITE', 'pwrite', '#include<unistd.h>'],
  ['HAVE_QSORT_R', 'qsort_r', '#include<stdlib.h>'],
  ['HAVE_RAISE', 'raise', '#include<signal.h>'],
  ['HAVE_RANDOM', 'random', '#include<stdlib.h>'],
  ['HAVE_RANDOM_R', 'random_r', '#include<stdlib.h>'],
  ['HAVE_RAWMEMCHR', 'rawmemchr', '#include<string.h>'],
  ['HAVE_READDIR', 'readdir', '#include<dirent.h>'],
  ['HAVE_READLINK', 'readlink', '#include<unistd.h>'],
  ['HAVE_READLINKAT', 'readlinkat', '#include<unistd.h>'],
  ['HAVE_REALLOCARRAY', 'reallocarray', '#include<stdlib.h>'],
  ['HAVE_REALPATH', 'realpath', '#include<stdlib.h>'],
  ['HAVE_RENAMEAT', 'renameat', '#include<stdio.h>'],
  ['HAVE_REWINDDIR', 'rewinddir', '#include<dirent.h>'],
  ['HAVE_RE_COMPILE_PATTERN', 're_compile_pattern', '#include<regex.h>'],
  ['HAVE_RE_SEARCH', 're_search', '#include<regex.h>'],
  ['HAVE_RE_SET_REGISTERS', 're_set_registers', '#include<regex.h>'],
  ['HAVE_RPMATCH', 'rpmatch', '#include<stdlib.h>'],
  ['HAVE_SCHED_SETPARAM', 'sched_setparam', '#include<sched.h>'],
  ['HAVE_SCHED_SETSCHEDULER', 'sched_setscheduler', '#include<sched.h>'],
  ['HAVE_SECURE_GETENV', 'secure_getenv', '#include<stdlib.h>'],
  ['HAVE_SETDTABLESIZE', 'setdtablesize', '#include<unistd.h>'],
  ['HAVE_SETEGID', 'setegid', '#include<unistd.h>'],
  ['HAVE_SETENV', 'setenv', '#include<stdlib.h>'],
  ['HAVE_SETEUID', 'seteuid', '#include<unistd.h>'],
  ['HAVE_SETHOSTNAME', 'sethostname', '#include<unistd.h>'],
  ['HAVE_SETRLIMIT', 'setrlimit', '#include<sys/resource.h>'],
  ['HAVE_SETSTATE', 'setstate', '#include<stdlib.h>'],
  ['HAVE_SHUTDOWN', 'shutdown', '#include<sys/socket.h>'],
  ['HAVE_SIGABBREV_NP', 'sigabbrev_np', '#include<string.h>'],
  ['HAVE_SIGACTION', 'sigaction', '#include<signal.h>'],
  ['HAVE_SIGALTSTACK', 'sigaltstack', '#include<signal.h>'],
  ['HAVE_SIGDESCR_NP', 'sigdescr_np', '#include<string.h>'],
  ['HAVE_SIGINTERRUPT', 'siginterrupt', '#include<signal.h>'],
  ['HAVE_SIGPROCMASK', 'sigprocmask', '#include<signal.h>'],
  ['HAVE_SLEEP', 'sleep', '#include<unistd.h>'],
  ['HAVE_SNPRINTF', 'snprintf', '#include<stdio.h>'],
  ['HAVE_STPCPY', 'stpcpy', '#include<string.h>'],
  ['HAVE_STPNCPY', 'stpncpy', '#include<string.h>'],
  ['HAVE_STRCASESTR', 'strcasestr', '#include<string.h>'],
  ['HAVE_STRCHRNUL', 'strchrnul', '#include<string.h>'],
  ['HAVE_STRERRORNAME_NP', 'strerrorname_np', '#include<string.h>'],
  ['HAVE_STRERROR_R', 'strerror_r', '#include<string.h>'],
  ['HAVE_STRNDUP', 'strndup', '#include<string.h>'],
  ['HAVE_STRNLEN', 'strnlen', '#include<string.h>'],
  ['HAVE_STRPBRK', 'strpbrk', '#include<string.h>'],
  ['HAVE_STRSEP', 'strsep', '#include<string.h>'],
  ['HAVE_STRSIGNAL', 'strsignal', '#include<string.h>'],
  ['HAVE_STRTOD', 'strtod', '#include<stdlib.h>'],
  ['HAVE_STRTOL', 'strtol', '#include<stdlib.h>'],
  ['HAVE_STRTOLD', 'strtold', '#include<stdlib.h>'],
  ['HAVE_STRTOLL', 'strtoll', '#include<stdlib.h>'],
  ['HAVE_STRTOUL', 'strtoul', '#include<stdlib.h>'],
  ['HAVE_STRTOULL', 'strtoull', '#include<stdlib.h>'],
  ['HAVE_STRVERSCMP', 'strverscmp', '#include<string.h>'],
  ['HAVE_SYMLINK', 'symlink', '#include<unistd.h>'],
  ['HAVE_SYMLINKAT', 'symlinkat', '#include<unistd.h>'],
  ['HAVE_THRD_CREATE', 'thrd_create', '#include<threads.h>'],
  ['HAVE_TOWLOWER', 'towlower', '#include<wctype.h>'],
  ['HAVE_TSEARCH', 'tsearch', '#include<search.h>'],
  ['HAVE_UNLINKAT', 'unlinkat', '#include<unistd.h>'],
  ['HAVE_UNLOCKPT', 'unlockpt', '#include<stdlib.h>'],
  ['HAVE_UNSETENV', 'unsetenv', '#include<stdlib.h>'],
  ['HAVE_USELOCALE', 'uselocale', '#include<locale.h>'],
  ['HAVE_USLEEP', 'usleep', '#include<unistd.h>'],
  ['HAVE_VASNPRINTF', 'vasnprintf', '#include<stdio.h>'],
  ['HAVE_VASPRINTF', 'vasprintf', '#include<stdio.h>'],
  ['HAVE_VDPRINTF', 'vdprintf', '#include<stdio.h>'],
  ['HAVE_VFORK', 'vfork', '#include<unistd.h>'],
  ['HAVE_WAITID', 'waitid', '#include<sys/wait.h>'],
  ['HAVE_WAITPID', 'waitpid', '#include<sys/wait.h>'],
  ['HAVE_WCRTOMB', 'wcrtomb', '#include<wchar.h>'],
  ['HAVE_WCSLEN', 'wcslen', '#include<wchar.h>'],
  ['HAVE_WCSNLEN', 'wcsnlen', '#include<wchar.h>'],
  ['HAVE_WCTOB', 'wctob', '#include<wchar.h>'],
  ['HAVE_WCWIDTH', 'wcwidth', '#include<wchar.h>'],
  ['HAVE_WORKING_SIGALTSTACK', 'sigaltstack', '#include<signal.h>'],
  ['HAVE_WORKING_USELOCALE', 'uselocale', '#include<locale.h>'],
  ['HAVE__CHSIZE', '_chsize', '#include<io.h>'],
  ['HAVE__EXIT', '_exit', '#include<stdlib.h>'],
  ['HAVE__FSEEKI64', '_fseeki64', '#include<stdio.h>'],
  ['HAVE__FTELLI64', '_ftelli64', '#include<stdio.h>'],
  [
    'HAVE__SET_INVALID_PARAMETER_HANDLER',
    '_set_invalid_parameter_handler',
    '#include<stdlib.h>',
  ],
  ['HAVE___FPURGE', '__fpurge', '#include<stdio_ext.h>'],
  ['HAVE___FREADAHEAD', '__freadahead', '#include<stdio_ext.h>'],
  ['HAVE___FREADING', '__freading', '#include<stdio_ext.h>'],
  ['HAVE___SECURE_GETENV', '__secure_getenv', '#include<stdlib.h>'],
  ['HAVE___XPG_STRERROR_R', '__xpg_strerror_r', '#include<string.h>'],
]

# HAVE_FOO tends to want to be 1 or undefined
# generated_header_data needs to be defined to 0, however.
foreach f : check_functions
  if cc.has_function(
    f.get(1),
    prefix: f.get(2) + '\n' + ac_includes_default,
    args: have_header_args + extension_args,
  )
    cdata.set(f.get(0), 1)
    generated_header_data.set10(f.get(0), true)
  else
    generated_header_data.set10(f.get(0), false)
  endif
endforeach


cdata.set(
  'D_INO_IN_DIRENT',
  1,
  description: 'Define if struct dirent has a member d_ino that actually works.',
)
cdata.set(
  'FLEXIBLE_ARRAY_MEMBER',
  '',
  description: 'Define to nothing if C supports flexible array members, and to 1 if it does not.',
)
cdata.set(
  'ENABLE_NLS',
  0,
  description: '''Define to 1 if translation of program messages to the user's native language is requested''',
)
cdata.set(
  'FUNC_FFLUSH_STDIN',
  -1,
  description: 'Define to 1 if fflush is known to work on stdin as per POSIX.1-2008, 0 if fflush is known to not work, -1 if unknown.',
)
cdata.set('FUNC_REALPATH_WORKS', 1)
cdata.set(
  'GETTIMEOFDAY_TIMEZONE',
  'void',
  description: '''Define this to 'void' or 'struct timezone' to match the system's declaration of the second argument to gettimeofday.''',
)
cdata.set(
  'MALLOC_0_IS_NONNULL',
  1,
  description: 'If malloc(0) is != NULL, define this to 1. Otherwise define this to 0.',
)

cdata.set('ENABLE_CHANGEWORD', get_option('enable_changeword'))
cdata.set('NEED_SETLOCALE_IMPROVED', 0)
cdata.set('NEED_SETLOCALE_MTSAFE', 0)
cdata.set('NL_LANGINFO_MTSAFE', 1)
cdata.set_quoted('PACKAGE', 'm4')
cdata.set_quoted('PACKAGE_BUGREPORT', 'bug-m4@gnu.org')
cdata.set_quoted('PACKAGE_NAME', 'GNU M4')
cdata.set_quoted('PACKAGE_STRING', 'GNU M4 ' + meson.project_version())
cdata.set_quoted('PACKAGE_TARNAME', 'm4')
cdata.set_quoted('PACKAGE_URL', 'https://www.gnu.org/software/m4/')
cdata.set_quoted('PACKAGE_VERSION', meson.project_version())
cdata.set('PROMOTED_MODE_T', 'mode_t')
cdata.set('SETLOCALE_NULL_ALL_MTSAFE', 1)
cdata.set('SETLOCALE_NULL_ONE_MTSAFE', 1)
cdata.set('SIGNAL_SAFE_LIST', 1)

stack_direction_result = cc.run(
  '''#include <stdio.h>
int
find_stack_direction (int *addr, int depth)
{
  int dir, dummy = 0;
  if (! addr)
    addr = &dummy;
  *addr = addr < &dummy ? 1 : addr == &dummy ? 0 : -1;
  dir = depth ? find_stack_direction (addr, depth - 1) : 0;
  return dir + dummy;
}
int
main (int argc, char *argv[])
{
    printf("%d", find_stack_direction (NULL, argc + 20));
    return 0;
}''',
  name: 'Determine STACK_DIRECTION',
)

if stack_direction_result.stdout().to_int() > 0
  message('STACK_DIRECTION=1')
  cdata.set('STACK_DIRECTION', 1)
else
  message('STACK_DIRECTION=-1')
  cdata.set('STACK_DIRECTION', -1)
endif

syscmd_shell = get_option('with_syscmd_shell')
kill_printed = false
if syscmd_shell.startswith('default')
  sh = find_program('bash', 'sh', 'cmd')
  syscmd_shell = sh.full_path()
endif

cdata.set_quoted('SYSCMD_SHELL', syscmd_shell)
cdata.set_quoted('VERSION', '1.4.19')

if (cc.get_define(
    'O_BINARY',
  prefix: '#include<fcntl.h>',
  ) == '')
  if (cc.get_define(
      '_O_BINARY',
    prefix: '#include<fcntl.h>',
    ) != '')
    cdata.set('O_BINARY', '_O_BINARY')
    cdata.set('O_TEXT', '_O_TEXT')
  else
    cdata.set('O_BINARY', '0')
    cdata.set('O_TEXT', '0')
  endif
endif
cdata.set('_GL_ATTRIBUTE_SPEC_PRINTF_SYSTEM', '__printf__')
cdata.set('_GL_ATTRIBUTE_SPEC_PRINTF_STANDARD', '__printf__')
cdata.set('GNULIB_XALLOC', 1)
cdata.set('GNULIB_XALLOC_DIE', 1)
cdata.set('GNULIB_FILENAMECAT', 1)
cdata.set('GNULIB_CLOSE_STREAM', 1)
cdata.set10('GNULIB_MBSLEN', not cdata.has('HAVE_MBSLEN'))
cdata.set10('GNULIB_MBSSTR', not cdata.has('HAVE_MBSSTR'))
cdata.set('GNULIB_CANONICALIZE', 1)
cdata.set('GNULIB_CANONICALIZE_LGPL', 1)
cdata.set('ICONV_CONST', '')
if cdata.get('HAVE_DECL_EACCESS') == 0
  cdata.set(
    'eaccess',
    'access',
    description: 'Define as \'access\' if you don\'t have the eaccess() function.',
  )
endif

cdata.set('GNULIB_FD_SAFER_FLAG', 1)

libm4_c_args = []
if host_machine.system() == 'windows'
  libm4_c_args += '-DEXECUTE_IMPL_AVOID_POSIX_SPAWN=1'
  libm4_c_args += '-DSPAWN_PIPE_IMPL_AVOID_POSIX_SPAWN=1'
  libm4_c_args += '-D_Restrict_arr_'
  libm4_c_args += '/FI../lib/nononnull.h'
  cdata.set('RENAME_OPEN_FILE_WORKS', '0')
  cdata.set('GNULIB_POSIX_SPAWN_FILE_ACTIONS_ADDCHDIR', 0)
  cdata.set('GNULIB_MSVC_NOTHROW', 1)
  cdata.set('GNULIB_PIPE2_SAFER', 1)
  cdata.set('GNULIB_FOPEN_SAFER', 1)
  cdata.set('GNULIB_FOPEN_GNU', 1)
  cdata.set('GNULIB_OPEN', 1)
  cdata.set('GNULIB_FOPEN', 1)
  cdata.set('GNULIB_FFLUSH', 1)
  cdata.set('GNULIB_FSEEKO', 1)
  cdata.set('GNULIB_LSEEK', 1)
  cdata.set('GNULIB_FTELLO', 1)
  cdata.set('GNULIB_FPURGE', 1)
  cdata.set('GNULIB_RENAME', 1)
  cdata.set('REPLACE_OPEN', 1)
  cdata.set('REPLACE_FOPEN', 1)
  cdata.set('REPLACE_FFLUSH', 1)
  cdata.set('REPLACE_FSEEKO', 1)
  cdata.set('REPLACE_LSEEK', 1)
  cdata.set('REPLACE_FTELLO', 1)
  cdata.set('REPLACE_FPURGE', 1)
  cdata.set('REPLACE_RENAME', 1)
else
  libm4_c_args += '-DGCC_LINT'
  cdata.set('RENAME_OPEN_FILE_WORKS', '1')
  cdata.set('GNULIB_POSIX_SPAWN_FILE_ACTIONS_ADDCHDIR', 1)
  cdata.set('GNULIB_MSVC_NOTHROW', 0)
  cdata.set('GNULIB_PIPE2_SAFER', 1)
  cdata.set('GNULIB_FOPEN_SAFER', 1)
  cdata.set('GNULIB_FOPEN_GNU', 0)
  cdata.set('GNULIB_OPEN', 0)
  cdata.set('GNULIB_FOPEN', 0)
  cdata.set('GNULIB_FFLUSH', 0)
  cdata.set('GNULIB_FSEEKO', 0)
  cdata.set('GNULIB_LSEEK', 0)
  cdata.set('GNULIB_FTELLO', 0)
  cdata.set('GNULIB_FPURGE', 0)
  cdata.set('GNULIB_RENAME', 0)
  cdata.set('REPLACE_OPEN', 0)
  cdata.set('REPLACE_FOPEN', 0)
  cdata.set('REPLACE_FFLUSH', 0)
  cdata.set('REPLACE_FSEEKO', 0)
  cdata.set('REPLACE_LSEEK', 0)
  cdata.set('REPLACE_FTELLO', 0)
  cdata.set('REPLACE_FPURGE', 0)
  cdata.set('REPLACE_RENAME', 0)
endif

if cc.run(
  '''#include <sys/types.h> /* for off_t */
#include <stdio.h> /* for SEEK_CUR */
#if HAVE_UNISTD_H
# include <unistd.h>
#else /* on Windows with MSVC */
# include <io.h>
#endif

int main(int argc, char *argv[]) {
    return lseek (0, (off_t)0, SEEK_CUR) < 0;
}
''',
).returncode() == 0
  cdata.set('LSEEK_PIPE_BROKEN', 1)
endif

cdata.set('REPLACE_FDOPEN', 0)
cdata.set('GNULIB_FDOPEN', 0)

if not cdata.has('HAVE_SSIZE_T')
  cdata.set('ssize_t', 'ptrdiff_t')
endif
if not cdata.has('HAVE_PID_T')
  cdata.set('pid_t', 'intptr_t')
endif
if not cdata.has('HAVE_UID_T')
  cdata.set('uid_t', 'int')
endif
if not cdata.has('HAVE_MODE_T')
  cdata.set('mode_t', 'int')
endif

configure_file(
  input: 'config.h.meson',
  output: 'config.h',
  configuration: cdata,
)

configmake_data = configuration_data()
configmake_data.set_quoted('PREFIX', get_option('prefix'))
configmake_data.set_quoted('EXEC_PREFIX', get_option('prefix'))
configmake_data.set_quoted('BINDIR', get_option('prefix') / get_option('bindir'))
configmake_data.set_quoted(
  'SBINDIR',
  get_option('prefix') / get_option('sbindir'),
)
configmake_data.set_quoted(
  'LIBEXECDIR',
  get_option('prefix') / get_option('libexecdir'),
)
configmake_data.set_quoted(
  'DATAROOTDIR',
  get_option('prefix') / get_option('datadir'),
)
configmake_data.set_quoted(
  'DATADIR',
  get_option('prefix') / get_option('datadir'),
)
configmake_data.set_quoted(
  'SYSCONFDIR',
  get_option('prefix') / get_option('sysconfdir'),
)
configmake_data.set_quoted('SHAREDSTATEDIR', get_option('sharedstatedir'))
configmake_data.set_quoted('LOCALSTATEDIR', get_option('localstatedir'))
configmake_data.set_quoted('RUNSTATEDIR', get_option('prefix') / 'var/run')
configmake_data.set_quoted(
  'INCLUDEDIR',
  get_option('prefix') / get_option('includedir'),
)
configmake_data.set_quoted(
  'OLDINCLUDEDIR',
  get_option('prefix') / get_option('includedir'),
)
configmake_data.set_quoted(
  'DOCDIR',
  get_option('prefix') / get_option('datadir') / 'doc/m4',
)
configmake_data.set_quoted(
  'INFODIR',
  get_option('prefix') / get_option('datadir') / 'info',
)
configmake_data.set_quoted(
  'HTMLDIR',
  get_option('prefix') / get_option('datadir') / 'doc/m4',
)
configmake_data.set_quoted(
  'DVIDIR',
  get_option('prefix') / get_option('datadir') / 'doc/m4',
)
configmake_data.set_quoted(
  'PDFDIR',
  get_option('prefix') / get_option('datadir') / 'doc/m4',
)
configmake_data.set_quoted(
  'PSDIR',
  get_option('prefix') / get_option('datadir') / 'doc/m4',
)
configmake_data.set_quoted('LIBDIR', get_option('prefix') / get_option('libdir'))
configmake_data.set_quoted(
  'LISPDIR',
  get_option('prefix') / get_option('datadir') / 'emacs/site-lisp',
)
configmake_data.set_quoted(
  'LOCALEDIR',
  get_option('prefix') / get_option('localedir'),
)
configmake_data.set_quoted('MANDIR', get_option('prefix') / get_option('mandir'))
configmake_data.set_quoted(
  'PKGDATADIR',
  get_option('prefix') / get_option('datadir') / 'm4',
)
configmake_data.set_quoted(
  'PKGINCLUDEDIR',
  get_option('prefix') / get_option('includedir') / 'm4',
)
configmake_data.set_quoted(
  'PKGLIBDIR',
  get_option('prefix') / get_option('libdir') / 'm4',
)
configmake_data.set_quoted(
  'PKGLIBEXECDIR',
  get_option('prefix') / get_option('libexecdir') / 'm4',
)

configure_file(
  input: 'configmake.h.meson',
  output: 'configmake.h',
  configuration: configmake_data,
)

generated_header_data.set('PRAGMA_SYSTEM_HEADER', '#pragma GCC system_header')
if cc.compiles('#include_next <string.h>')
  generated_header_data.set('INCLUDE_NEXT', 'include_next')
  generated_header_data.set('NEXT_STRING_H', '<string.h>')
  generated_header_data.set('NEXT_UNISTD_H', '<unistd.h>')
  generated_header_data.set('NEXT_SPAWN_H', '<spawn.h>')
  generated_header_data.set('NEXT_STDLIB_H', '<stdlib.h>')
  generated_header_data.set('NEXT_SYS_WAIT_H', '<sys/wait.h>')
  generated_header_data.set('NEXT_SYS_TYPES_H', '<sys/types.h>')
  generated_header_data.set('NEXT_SYS_STAT_H', '<sys/stat.h>')
  generated_header_data.set('NEXT_SYS_RANDOM_H', '<sys/random.h>')
  generated_header_data.set('NEXT_STDIO_H', '<stdio.h>')
  generated_header_data.set('NEXT_STDDEF_H', '<stddef.h>')
  generated_header_data.set('NEXT_SIGNAL_H', '<signal.h>')
  generated_header_data.set('NEXT_FCNTL_H', '<fcntl.h>')
  generated_header_data.set('NEXT_LANGINFO_H', '<langinfo.h>')
  generated_header_data.set('NEXT_LOCALE_H', '<locale.h>')
  generated_header_data.set('NEXT_GETOPT_H', '<getopt.h>')
  generated_header_data.set('NEXT_WCHAR_H', '<wchar.h>')
elif cc.compiles('#include <../include/string.h>')
  generated_header_data.set('INCLUDE_NEXT', 'include')
  generated_header_data.set('NEXT_STRING_H', '<../include/string.h>')
  generated_header_data.set('NEXT_UNISTD_H', '<../include/unistd.h>')
  generated_header_data.set('NEXT_SPAWN_H', '<../include/spawn.h>')
  generated_header_data.set('NEXT_STDLIB_H', '<../include/stdlib.h>')
  generated_header_data.set('NEXT_SYS_WAIT_H', '<../include/sys/wait.h>')
  generated_header_data.set('NEXT_SYS_TYPES_H', '<../include/sys/types.h>')
  generated_header_data.set('NEXT_SYS_STAT_H', '<../include/sys/stat.h>')
  generated_header_data.set('NEXT_SYS_RANDOM_H', '<../include/sys/random.h>')
  generated_header_data.set('NEXT_STDIO_H', '<../include/stdio.h>')
  generated_header_data.set('NEXT_STDDEF_H', '<../include/stddef.h>')
  generated_header_data.set('NEXT_SIGNAL_H', '<../include/signal.h>')
  generated_header_data.set('NEXT_FCNTL_H', '<../include/fcntl.h>')
  generated_header_data.set('NEXT_LANGINFO_H', '<../include/langinfo.h>')
  generated_header_data.set('NEXT_LOCALE_H', '<../include/locale.h>')
  generated_header_data.set('NEXT_GETOPT_H', '<../include/getopt.h>')
  generated_header_data.set('NEXT_WCHAR_H', '<../include/wchar.h>')
elif cc.compiles('#include <../ucrt/string.h>')
  generated_header_data.set('INCLUDE_NEXT', 'include')
  generated_header_data.set('NEXT_STRING_H', '<../ucrt/string.h>')
  generated_header_data.set('NEXT_UNISTD_H', '<../ucrt/unistd.h>')
  generated_header_data.set('NEXT_SPAWN_H', '<../ucrt/spawn.h>')
  generated_header_data.set('NEXT_STDLIB_H', '<../ucrt/stdlib.h>')
  generated_header_data.set('NEXT_SYS_WAIT_H', '<../ucrt/sys/wait.h>')
  generated_header_data.set('NEXT_SYS_TYPES_H', '<../ucrt/sys/types.h>')
  generated_header_data.set('NEXT_SYS_STAT_H', '<../ucrt/sys/stat.h>')
  generated_header_data.set('NEXT_SYS_RANDOM_H', '<../ucrt/sys/random.h>')
  generated_header_data.set('NEXT_STDIO_H', '<../ucrt/stdio.h>')
  generated_header_data.set('NEXT_STDDEF_H', '<../ucrt/stddef.h>')
  generated_header_data.set('NEXT_SIGNAL_H', '<../ucrt/signal.h>')
  generated_header_data.set('NEXT_FCNTL_H', '<../ucrt/fcntl.h>')
  generated_header_data.set('NEXT_LANGINFO_H', '<../ucrt/langinfo.h>')
  generated_header_data.set('NEXT_LOCALE_H', '<../ucrt/locale.h>')
  generated_header_data.set('NEXT_GETOPT_H', '<../ucrt/getopt.h>')
  generated_header_data.set('NEXT_WCHAR_H', '<../ucrt/wchar.h>')
else
  error('Can\'t figure out how to #include_next')
endif
generated_header_data.set('GUARD_PREFIX', 'GL_M4')
generated_header_data.merge_from(cdata)
generated_header_data.set('ASM_SYMBOL_PREFIX', '')
generated_header_data.set('GNULIBHEADERS_OVERRIDE_WINT_T', 0)
generated_header_data.set('GNULIB_ACCESS', 0)
generated_header_data.set('GNULIB_ALIGNED_ALLOC', 0)
generated_header_data.set('GNULIB_ATOLL', 0)
generated_header_data.set('GNULIB_BTOWC', 0)
generated_header_data.set('GNULIB_CALLOC_POSIX', 0)
generated_header_data.set('GNULIB_CHDIR', 0)
generated_header_data.set('GNULIB_CHOWN', 0)
generated_header_data.set('GNULIB_CLOSE', 0)
generated_header_data.set('GNULIB_COPY_FILE_RANGE', 0)
generated_header_data.set('GNULIB_CREAT', 0)
generated_header_data.set('GNULIB_DPRINTF', 0)
generated_header_data.set('GNULIB_DUP', 0)
generated_header_data.set('GNULIB_DUP2', 0)
generated_header_data.set('GNULIB_DUP3', 0)
generated_header_data.set('GNULIB_DUPLOCALE', 0)
generated_header_data.set('GNULIB_EUIDACCESS', 0)
generated_header_data.set('GNULIB_EXECL', 0)
generated_header_data.set('GNULIB_EXECLE', 0)
generated_header_data.set('GNULIB_EXECLP', 0)
generated_header_data.set('GNULIB_EXECV', 0)
generated_header_data.set('GNULIB_EXECVE', 0)
generated_header_data.set('GNULIB_EXECVP', 0)
generated_header_data.set('GNULIB_EXECVPE', 0)
generated_header_data.set('GNULIB_EXPLICIT_BZERO', 0)
generated_header_data.set('GNULIB_FACCESSAT', 0)
generated_header_data.set('GNULIB_FCHDIR', 0)
generated_header_data.set('GNULIB_FCHMODAT', 0)
generated_header_data.set('GNULIB_FCHOWNAT', 0)
generated_header_data.set('GNULIB_FCLOSE', 0)
generated_header_data.set('GNULIB_FDATASYNC', 0)
generated_header_data.set('GNULIB_FFSL', 0)
generated_header_data.set('GNULIB_FFSLL', 0)
generated_header_data.set('GNULIB_FGETC', 0)
generated_header_data.set('GNULIB_FGETS', 0)
generated_header_data.set('GNULIB_FPRINTF', 0)
generated_header_data.set('GNULIB_FPRINTF_POSIX', 0)
generated_header_data.set('GNULIB_FPUTC', 0)
generated_header_data.set('GNULIB_FPUTS', 0)
generated_header_data.set('GNULIB_FREAD', 0)
generated_header_data.set('GNULIB_FREELOCALE', 0)
generated_header_data.set('GNULIB_FREE_POSIX', 0)
generated_header_data.set('GNULIB_FREOPEN', 0)
generated_header_data.set('GNULIB_FSCANF', 0)
generated_header_data.set('GNULIB_FSEEK', 0)
generated_header_data.set('GNULIB_FSTAT', 0)
generated_header_data.set('GNULIB_FSTATAT', 0)
generated_header_data.set('GNULIB_FSYNC', 0)
generated_header_data.set('GNULIB_FTELL', 0)
generated_header_data.set('GNULIB_FTRUNCATE', 0)
generated_header_data.set('GNULIB_FUTIMENS', 0)
generated_header_data.set('GNULIB_FWRITE', 0)
generated_header_data.set('GNULIB_GETC', 0)
generated_header_data.set('GNULIB_GETCHAR', 0)
generated_header_data.set('GNULIB_GETCWD', 0)
generated_header_data.set('GNULIB_GETDELIM', 0)
generated_header_data.set('GNULIB_GETDOMAINNAME', 0)
generated_header_data.set('GNULIB_GETENTROPY', 0)
generated_header_data.set('GNULIB_GETGROUPS', 0)
generated_header_data.set('GNULIB_GETHOSTNAME', 0)
generated_header_data.set('GNULIB_GETLINE', 0)
generated_header_data.set('GNULIB_GETLOADAVG', 0)
generated_header_data.set('GNULIB_GETLOGIN', 0)
generated_header_data.set('GNULIB_GETLOGIN_R', 0)
generated_header_data.set('GNULIB_GETOPT_POSIX', 0)
generated_header_data.set('GNULIB_GETPAGESIZE', 0)
generated_header_data.set('GNULIB_GETPASS', 0)
generated_header_data.set('GNULIB_GETSUBOPT', 0)
generated_header_data.set('GNULIB_GETUMASK', 0)
generated_header_data.set('GNULIB_GETUSERSHELL', 0)
generated_header_data.set('GNULIB_GRANTPT', 0)
generated_header_data.set('GNULIB_GROUP_MEMBER', 0)
generated_header_data.set('GNULIB_ISATTY', 0)
generated_header_data.set('GNULIB_LCHMOD', 0)
generated_header_data.set('GNULIB_LCHOWN', 0)
generated_header_data.set('GNULIB_LINK', 0)
generated_header_data.set('GNULIB_LINKAT', 0)
generated_header_data.set('GNULIB_LOCALECONV', 0)
generated_header_data.set('GNULIB_LOCALENAME', 0)
generated_header_data.set('GNULIB_MALLOC_POSIX', 0)
generated_header_data.set('GNULIB_MBRLEN', 0)
generated_header_data.set('GNULIB_MBRTOWC', 0)
generated_header_data.set('GNULIB_MBSCASECMP', 0)
generated_header_data.set('GNULIB_MBSCASESTR', 0)
generated_header_data.set('GNULIB_MBSCHR', 0)
generated_header_data.set('GNULIB_MBSCSPN', 0)
generated_header_data.set('GNULIB_MBSINIT', 0)
generated_header_data.set('GNULIB_MBSNCASECMP', 0)
generated_header_data.set('GNULIB_MBSNLEN', 0)
generated_header_data.set('GNULIB_MBSNRTOWCS', 0)
generated_header_data.set('GNULIB_MBSPBRK', 0)
generated_header_data.set('GNULIB_MBSPCASECMP', 0)
generated_header_data.set('GNULIB_MBSRCHR', 0)
generated_header_data.set('GNULIB_MBSRTOWCS', 0)
generated_header_data.set('GNULIB_MBSSEP', 0)
generated_header_data.set('GNULIB_MBSSPN', 0)
generated_header_data.set('GNULIB_MBSTOK_R', 0)
generated_header_data.set('GNULIB_MBTOWC', 0)
generated_header_data.set('GNULIB_MDA_ACCESS', 0)
generated_header_data.set('GNULIB_MDA_CHDIR', 0)
generated_header_data.set('GNULIB_MDA_CHMOD', 0)
generated_header_data.set('GNULIB_MDA_CLOSE', 0)
generated_header_data.set('GNULIB_MDA_CREAT', 0)
generated_header_data.set('GNULIB_MDA_DUP', 0)
generated_header_data.set('GNULIB_MDA_DUP2', 0)
generated_header_data.set('GNULIB_MDA_ECVT', 0)
generated_header_data.set('GNULIB_MDA_EXECL', 0)
generated_header_data.set('GNULIB_MDA_EXECLE', 0)
generated_header_data.set('GNULIB_MDA_EXECLP', 0)
generated_header_data.set('GNULIB_MDA_EXECV', 0)
generated_header_data.set('GNULIB_MDA_EXECVE', 0)
generated_header_data.set('GNULIB_MDA_EXECVP', 0)
generated_header_data.set('GNULIB_MDA_EXECVPE', 0)
generated_header_data.set('GNULIB_MDA_FCLOSEALL', 0)
generated_header_data.set('GNULIB_MDA_FCVT', 0)
generated_header_data.set('GNULIB_MDA_FDOPEN', 0)
generated_header_data.set('GNULIB_MDA_FILENO', 0)
generated_header_data.set('GNULIB_MDA_GCVT', 0)
generated_header_data.set('GNULIB_MDA_GETCWD', 0)
generated_header_data.set('GNULIB_MDA_GETPID', 0)
generated_header_data.set('GNULIB_MDA_GETW', 0)
generated_header_data.set('GNULIB_MDA_ISATTY', 0)
generated_header_data.set('GNULIB_MDA_LSEEK', 0)
generated_header_data.set('GNULIB_MDA_MEMCCPY', 0)
generated_header_data.set('GNULIB_MDA_MKTEMP', 0)
generated_header_data.set('GNULIB_MDA_OPEN', 0)
generated_header_data.set('GNULIB_MDA_PUTENV', 0)
generated_header_data.set('GNULIB_MDA_PUTW', 0)
generated_header_data.set('GNULIB_MDA_READ', 0)
generated_header_data.set('GNULIB_MDA_RMDIR', 0)
generated_header_data.set('GNULIB_MDA_STRDUP', 0)
generated_header_data.set('GNULIB_MDA_SWAB', 0)
generated_header_data.set('GNULIB_MDA_TEMPNAM', 0)
generated_header_data.set('GNULIB_MDA_UMASK', 0)
generated_header_data.set('GNULIB_MDA_UNLINK', 0)
generated_header_data.set('GNULIB_MDA_WCSDUP', 0)
generated_header_data.set('GNULIB_MDA_WRITE', 0)
generated_header_data.set('GNULIB_MEMCHR', 0)
generated_header_data.set('GNULIB_MEMMEM', 0)
generated_header_data.set('GNULIB_MEMRCHR', 0)
generated_header_data.set('GNULIB_MKDIR', 0)
generated_header_data.set('GNULIB_MKDIRAT', 0)
generated_header_data.set('GNULIB_MKFIFO', 0)
generated_header_data.set('GNULIB_MKFIFOAT', 0)
generated_header_data.set('GNULIB_MKNOD', 0)
generated_header_data.set('GNULIB_MKNODAT', 0)
generated_header_data.set('GNULIB_MKOSTEMP', 0)
generated_header_data.set('GNULIB_MKOSTEMPS', 0)
generated_header_data.set('GNULIB_MKSTEMPS', 0)
generated_header_data.set('GNULIB_NEWLOCALE', 0)
generated_header_data.set('GNULIB_NONBLOCKING', 0)
generated_header_data.set('GNULIB_OBSTACK_PRINTF', 0)
generated_header_data.set('GNULIB_OBSTACK_PRINTF_POSIX', 0)
generated_header_data.set('GNULIB_OPENAT', 0)
generated_header_data.set('GNULIB_OVERRIDES_STRUCT_STAT', 0)
generated_header_data.set('GNULIB_PCLOSE', 0)
generated_header_data.set('GNULIB_PERROR', 0)
generated_header_data.set('GNULIB_PIPE', 0)
generated_header_data.set('GNULIB_POPEN', 0)
generated_header_data.set('GNULIB_POSIX_MEMALIGN', 0)
generated_header_data.set('GNULIB_POSIX_OPENPT', 0)
generated_header_data.set('GNULIB_POSIX_SPAWN', 0)
generated_header_data.set('GNULIB_POSIX_SPAWNATTR_DESTROY', 0)
generated_header_data.set('GNULIB_POSIX_SPAWNATTR_GETFLAGS', 0)
generated_header_data.set('GNULIB_POSIX_SPAWNATTR_GETPGROUP', 0)
generated_header_data.set('GNULIB_POSIX_SPAWNATTR_GETSCHEDPARAM', 0)
generated_header_data.set('GNULIB_POSIX_SPAWNATTR_GETSCHEDPOLICY', 0)
generated_header_data.set('GNULIB_POSIX_SPAWNATTR_GETSIGDEFAULT', 0)
generated_header_data.set('GNULIB_POSIX_SPAWNATTR_GETSIGMASK', 0)
generated_header_data.set('GNULIB_POSIX_SPAWNATTR_INIT', 0)
generated_header_data.set('GNULIB_POSIX_SPAWNATTR_SETFLAGS', 0)
generated_header_data.set('GNULIB_POSIX_SPAWNATTR_SETPGROUP', 0)
generated_header_data.set('GNULIB_POSIX_SPAWNATTR_SETSCHEDPARAM', 0)
generated_header_data.set('GNULIB_POSIX_SPAWNATTR_SETSCHEDPOLICY', 0)
generated_header_data.set('GNULIB_POSIX_SPAWNATTR_SETSIGDEFAULT', 0)
generated_header_data.set('GNULIB_POSIX_SPAWNATTR_SETSIGMASK', 0)
generated_header_data.set('GNULIB_POSIX_SPAWNP', 0)
generated_header_data.set('GNULIB_POSIX_SPAWN_FILE_ACTIONS_ADDCLOSE', 0)
generated_header_data.set('GNULIB_POSIX_SPAWN_FILE_ACTIONS_ADDDUP2', 0)
generated_header_data.set('GNULIB_POSIX_SPAWN_FILE_ACTIONS_ADDFCHDIR', 0)
generated_header_data.set('GNULIB_POSIX_SPAWN_FILE_ACTIONS_ADDOPEN', 0)
generated_header_data.set('GNULIB_POSIX_SPAWN_FILE_ACTIONS_DESTROY', 0)
generated_header_data.set('GNULIB_POSIX_SPAWN_FILE_ACTIONS_INIT', 0)
generated_header_data.set('GNULIB_PREAD', 0)
generated_header_data.set('GNULIB_PRINTF', 0)
generated_header_data.set('GNULIB_PRINTF_POSIX', 0)
generated_header_data.set('GNULIB_PTHREAD_SIGMASK', 0)
generated_header_data.set('GNULIB_PTSNAME', 0)
generated_header_data.set('GNULIB_PTSNAME_R', 0)
generated_header_data.set('GNULIB_PUTC', 0)
generated_header_data.set('GNULIB_PUTCHAR', 0)
generated_header_data.set('GNULIB_PUTENV', 0)
generated_header_data.set('GNULIB_PUTS', 0)
generated_header_data.set('GNULIB_PWRITE', 0)
generated_header_data.set('GNULIB_QSORT_R', 0)
generated_header_data.set('GNULIB_RAISE', 0)
generated_header_data.set('GNULIB_RANDOM', 0)
generated_header_data.set('GNULIB_RANDOM_R', 0)
generated_header_data.set('GNULIB_READ', 0)
generated_header_data.set('GNULIB_READLINKAT', 0)
generated_header_data.set('GNULIB_REALLOC_POSIX', 0)
generated_header_data.set('GNULIB_REMOVE', 0)
generated_header_data.set('GNULIB_RENAMEAT', 0)
generated_header_data.set('GNULIB_RMDIR', 0)
generated_header_data.set('GNULIB_RPMATCH', 0)
generated_header_data.set('GNULIB_SCANF', 0)
generated_header_data.set('GNULIB_SETENV', 0)
generated_header_data.set('GNULIB_SETHOSTNAME', 0)
generated_header_data.set('GNULIB_SETLOCALE', 0)
generated_header_data.set('GNULIB_SIGABBREV_NP', 0)
generated_header_data.set('GNULIB_SIGDESCR_NP', 0)
generated_header_data.set('GNULIB_SIGNAL_H_SIGPIPE', 0)
generated_header_data.set('GNULIB_SLEEP', 0)
generated_header_data.set('GNULIB_SNPRINTF', 0)
generated_header_data.set('GNULIB_SPRINTF_POSIX', 0)
generated_header_data.set('GNULIB_STAT', 0)
generated_header_data.set('GNULIB_STDIO_H_NONBLOCKING', 0)
generated_header_data.set('GNULIB_STDIO_H_SIGPIPE', 0)
generated_header_data.set('GNULIB_STPNCPY', 0)
generated_header_data.set('GNULIB_STRCASESTR', 0)
generated_header_data.set('GNULIB_STRCHRNUL', 0)
generated_header_data.set('GNULIB_STRDUP', 0)
generated_header_data.set('GNULIB_STRERROR', 0)
generated_header_data.set('GNULIB_STRERRORNAME_NP', 0)
generated_header_data.set('GNULIB_STRERROR_R', 0)
generated_header_data.set('GNULIB_STRNCAT', 0)
generated_header_data.set('GNULIB_STRNLEN', 0)
generated_header_data.set('GNULIB_STRPBRK', 0)
generated_header_data.set('GNULIB_STRSEP', 0)
generated_header_data.set('GNULIB_STRSTR', 0)
generated_header_data.set('GNULIB_STRTOD', 0)
generated_header_data.set('GNULIB_STRTOK_R', 0)
generated_header_data.set('GNULIB_STRTOL', 0)
generated_header_data.set('GNULIB_STRTOLD', 0)
generated_header_data.set('GNULIB_STRTOLL', 0)
generated_header_data.set('GNULIB_STRTOUL', 0)
generated_header_data.set('GNULIB_STRTOULL', 0)
generated_header_data.set('GNULIB_STRVERSCMP', 0)
generated_header_data.set('GNULIB_SYMLINK', 0)
generated_header_data.set('GNULIB_SYMLINKAT', 0)
generated_header_data.set('GNULIB_SYSTEM_POSIX', 0)
generated_header_data.set('GNULIB_TMPFILE', 0)
generated_header_data.set('GNULIB_TRUNCATE', 0)
generated_header_data.set('GNULIB_TTYNAME_R', 0)
generated_header_data.set('GNULIB_UNISTD_H_GETOPT', 0)
generated_header_data.set('GNULIB_UNLINK', 0)
generated_header_data.set('GNULIB_UNLINKAT', 0)
generated_header_data.set('GNULIB_UNLOCKPT', 0)
generated_header_data.set('GNULIB_UNSETENV', 0)
generated_header_data.set('GNULIB_USLEEP', 0)
generated_header_data.set('GNULIB_UTIMENSAT', 0)
generated_header_data.set('GNULIB_VDPRINTF', 0)
generated_header_data.set('GNULIB_VFPRINTF', 0)
generated_header_data.set('GNULIB_VFPRINTF_POSIX', 0)
generated_header_data.set('GNULIB_VFSCANF', 0)
generated_header_data.set('GNULIB_VPRINTF', 0)
generated_header_data.set('GNULIB_VPRINTF_POSIX', 0)
generated_header_data.set('GNULIB_VSCANF', 0)
generated_header_data.set('GNULIB_VSNPRINTF', 0)
generated_header_data.set('GNULIB_VSPRINTF_POSIX', 0)
generated_header_data.set('GNULIB_WCPCPY', 0)
generated_header_data.set('GNULIB_WCPNCPY', 0)
generated_header_data.set('GNULIB_WCRTOMB', 0)
generated_header_data.set('GNULIB_WCSCASECMP', 0)
generated_header_data.set('GNULIB_WCSCAT', 0)
generated_header_data.set('GNULIB_WCSCHR', 0)
generated_header_data.set('GNULIB_WCSCMP', 0)
generated_header_data.set('GNULIB_WCSCOLL', 0)
generated_header_data.set('GNULIB_WCSCPY', 0)
generated_header_data.set('GNULIB_WCSCSPN', 0)
generated_header_data.set('GNULIB_WCSDUP', 0)
generated_header_data.set('GNULIB_WCSFTIME', 0)
generated_header_data.set('GNULIB_WCSLEN', 0)
generated_header_data.set('GNULIB_WCSNCASECMP', 0)
generated_header_data.set('GNULIB_WCSNCAT', 0)
generated_header_data.set('GNULIB_WCSNCMP', 0)
generated_header_data.set('GNULIB_WCSNCPY', 0)
generated_header_data.set('GNULIB_WCSNLEN', 0)
generated_header_data.set('GNULIB_WCSNRTOMBS', 0)
generated_header_data.set('GNULIB_WCSPBRK', 0)
generated_header_data.set('GNULIB_WCSRCHR', 0)
generated_header_data.set('GNULIB_WCSRTOMBS', 0)
generated_header_data.set('GNULIB_WCSSPN', 0)
generated_header_data.set('GNULIB_WCSSTR', 0)
generated_header_data.set('GNULIB_WCSTOK', 0)
generated_header_data.set('GNULIB_WCSWIDTH', 0)
generated_header_data.set('GNULIB_WCSXFRM', 0)
generated_header_data.set('GNULIB_WCTOB', 0)
generated_header_data.set('GNULIB_WCTOMB', 0)
generated_header_data.set('GNULIB_WMEMCHR', 0)
generated_header_data.set('GNULIB_WMEMCMP', 0)
generated_header_data.set('GNULIB_WMEMCPY', 0)
generated_header_data.set('GNULIB_WMEMMOVE', 0)
generated_header_data.set('GNULIB_WMEMPCPY', 0)
generated_header_data.set('GNULIB_WMEMSET', 0)
generated_header_data.set('GNULIB_WRITE', 0)
generated_header_data.set('GNULIB__EXIT', 0)
generated_header_data.set('HAVE_POSIX_SIGNALBLOCKING', 0)
generated_header_data.set('LOCALENAME_ENHANCE_LOCALE_FUNCS', 0)
generated_header_data.set('PRAGMA_COLUMNS', '')
generated_header_data.set('REPLACE_ACCESS', 0)
generated_header_data.set('REPLACE_ALIGNED_ALLOC', 0)
generated_header_data.set('REPLACE_BTOWC', 0)
generated_header_data.set('REPLACE_CALLOC', 0)
generated_header_data.set('REPLACE_CANONICALIZE_FILE_NAME', 0)
generated_header_data.set('REPLACE_CHOWN', 0)
generated_header_data.set('REPLACE_CLOSE', 0)
generated_header_data.set('REPLACE_CREAT', 0)
generated_header_data.set('REPLACE_DPRINTF', 0)
generated_header_data.set('REPLACE_DUP', 0)
generated_header_data.set('REPLACE_DUP2', 0)
generated_header_data.set('REPLACE_DUPLOCALE', 0)
generated_header_data.set('REPLACE_EXECL', 0)
generated_header_data.set('REPLACE_EXECLE', 0)
generated_header_data.set('REPLACE_EXECLP', 0)
generated_header_data.set('REPLACE_EXECV', 0)
generated_header_data.set('REPLACE_EXECVE', 0)
generated_header_data.set('REPLACE_EXECVP', 0)
generated_header_data.set('REPLACE_EXECVPE', 0)
generated_header_data.set('REPLACE_FACCESSAT', 0)
generated_header_data.set('REPLACE_FCHMODAT', 0)
generated_header_data.set('REPLACE_FCHOWNAT', 0)
generated_header_data.set('REPLACE_FCLOSE', 0)
generated_header_data.set('REPLACE_FCNTL', 0)
generated_header_data.set('REPLACE_FFSLL', 0)
generated_header_data.set('REPLACE_FPRINTF', 0)
generated_header_data.set('REPLACE_FREE', 0)
generated_header_data.set('REPLACE_FREELOCALE', 0)
generated_header_data.set('REPLACE_FREOPEN', 0)
generated_header_data.set('REPLACE_FSEEK', 0)
generated_header_data.set('REPLACE_FSTAT', 0)
generated_header_data.set('REPLACE_FSTATAT', 0)
generated_header_data.set('REPLACE_FTELL', 0)
generated_header_data.set('REPLACE_FTELLO', 0)
generated_header_data.set('REPLACE_FTRUNCATE', 0)
generated_header_data.set('REPLACE_FUTIMENS', 0)
generated_header_data.set('REPLACE_GETCWD', 0)
generated_header_data.set('REPLACE_GETDELIM', 0)
generated_header_data.set('REPLACE_GETDOMAINNAME', 0)
generated_header_data.set('REPLACE_GETDTABLESIZE', 0)
generated_header_data.set('REPLACE_GETGROUPS', 0)
generated_header_data.set('REPLACE_GETLINE', 0)
generated_header_data.set('REPLACE_GETLOGIN_R', 0)
generated_header_data.set('REPLACE_GETPAGESIZE', 0)
generated_header_data.set('REPLACE_GETPASS', 0)
generated_header_data.set('REPLACE_GETRANDOM', 0)
generated_header_data.set('REPLACE_INITSTATE', 0)
generated_header_data.set('REPLACE_ISATTY', 0)
generated_header_data.set('REPLACE_LCHOWN', 0)
generated_header_data.set('REPLACE_LINK', 0)
generated_header_data.set('REPLACE_LINKAT', 0)
generated_header_data.set('REPLACE_LOCALECONV', 0)
generated_header_data.set('REPLACE_LSTAT', 0)
generated_header_data.set('REPLACE_MALLOC', 0)
generated_header_data.set('REPLACE_MBRLEN', 0)
generated_header_data.set('REPLACE_MBRTOWC', 0)
generated_header_data.set('REPLACE_MBSINIT', 0)
generated_header_data.set('REPLACE_MBSNRTOWCS', 0)
generated_header_data.set('REPLACE_MBSRTOWCS', 0)
generated_header_data.set('REPLACE_MBSTATE_T', 0)
generated_header_data.set('REPLACE_MBTOWC', 0)
generated_header_data.set('REPLACE_MEMCHR', 0)
generated_header_data.set('REPLACE_MEMMEM', 0)
generated_header_data.set('REPLACE_MKDIR', 0)
generated_header_data.set('REPLACE_MKFIFO', 0)
generated_header_data.set('REPLACE_MKFIFOAT', 0)
generated_header_data.set('REPLACE_MKNOD', 0)
generated_header_data.set('REPLACE_MKNODAT', 0)
generated_header_data.set('REPLACE_MKSTEMP', 0)
generated_header_data.set('REPLACE_NEWLOCALE', 0)
generated_header_data.set('REPLACE_NL_LANGINFO', 0)
generated_header_data.set('REPLACE_NULL', 0)
generated_header_data.set('REPLACE_OBSTACK_PRINTF', 0)
generated_header_data.set('REPLACE_OPENAT', 0)
generated_header_data.set('REPLACE_PERROR', 0)
generated_header_data.set('REPLACE_POPEN', 0)
generated_header_data.set('REPLACE_POSIX_MEMALIGN', 0)
generated_header_data.set('REPLACE_POSIX_SPAWN', 0)
generated_header_data.set('REPLACE_POSIX_SPAWN_FILE_ACTIONS_ADDCHDIR', 0)
generated_header_data.set('REPLACE_POSIX_SPAWN_FILE_ACTIONS_ADDCLOSE', 0)
generated_header_data.set('REPLACE_POSIX_SPAWN_FILE_ACTIONS_ADDDUP2', 0)
generated_header_data.set('REPLACE_POSIX_SPAWN_FILE_ACTIONS_ADDFCHDIR', 0)
generated_header_data.set('REPLACE_POSIX_SPAWN_FILE_ACTIONS_ADDOPEN', 0)
generated_header_data.set('REPLACE_PREAD', 0)
generated_header_data.set('REPLACE_PRINTF', 0)
generated_header_data.set('REPLACE_PTHREAD_SIGMASK', 0)
generated_header_data.set('REPLACE_PTSNAME', 0)
generated_header_data.set('REPLACE_PTSNAME_R', 0)
generated_header_data.set('REPLACE_PUTENV', 0)
generated_header_data.set('REPLACE_PWRITE', 0)
generated_header_data.set('REPLACE_QSORT_R', 0)
generated_header_data.set('REPLACE_RAISE', 0)
generated_header_data.set('REPLACE_RANDOM', 0)
generated_header_data.set('REPLACE_RANDOM_R', 0)
generated_header_data.set('REPLACE_READ', 0)
generated_header_data.set('REPLACE_READLINK', 0)
generated_header_data.set('REPLACE_READLINKAT', 0)
generated_header_data.set('REPLACE_REALLOC', 0)
generated_header_data.set('REPLACE_REALLOCARRAY', 0)
generated_header_data.set('REPLACE_REALPATH', 0)
generated_header_data.set('REPLACE_REMOVE', 0)
generated_header_data.set('REPLACE_RENAMEAT', 0)
generated_header_data.set('REPLACE_RMDIR', 0)
generated_header_data.set('REPLACE_SETENV', 0)
generated_header_data.set('REPLACE_SETLOCALE', 0)
generated_header_data.set('REPLACE_SETSTATE', 0)
generated_header_data.set('REPLACE_SLEEP', 0)
generated_header_data.set('REPLACE_SNPRINTF', 0)
generated_header_data.set('REPLACE_SPRINTF', 0)
generated_header_data.set('REPLACE_STAT', 0)
generated_header_data.set('REPLACE_STDIO_READ_FUNCS', 0)
generated_header_data.set('REPLACE_STDIO_WRITE_FUNCS', 0)
generated_header_data.set('REPLACE_STPNCPY', 0)
generated_header_data.set('REPLACE_STRCASESTR', 0)
generated_header_data.set('REPLACE_STRCHRNUL', 0)
generated_header_data.set('REPLACE_STRDUP', 0)
generated_header_data.set('REPLACE_STRERROR', 0)
generated_header_data.set('REPLACE_STRERRORNAME_NP', 0)
generated_header_data.set('REPLACE_STRERROR_R', 0)
generated_header_data.set('REPLACE_STRNCAT', 0)
generated_header_data.set('REPLACE_STRNDUP', 0)
generated_header_data.set('REPLACE_STRNLEN', 0)
generated_header_data.set('REPLACE_STRSIGNAL', 0)
generated_header_data.set('REPLACE_STRSTR', 0)
generated_header_data.set('REPLACE_STRTOD', 0)
generated_header_data.set('REPLACE_STRTOK_R', 0)
generated_header_data.set('REPLACE_STRTOL', 0)
generated_header_data.set('REPLACE_STRTOLD', 0)
generated_header_data.set('REPLACE_STRTOLL', 0)
generated_header_data.set('REPLACE_STRTOUL', 0)
generated_header_data.set('REPLACE_STRTOULL', 0)
generated_header_data.set('REPLACE_STRUCT_LCONV', 0)
generated_header_data.set('REPLACE_SYMLINK', 0)
generated_header_data.set('REPLACE_SYMLINKAT', 0)
generated_header_data.set('REPLACE_TMPFILE', 0)
generated_header_data.set('REPLACE_TRUNCATE', 0)
generated_header_data.set('REPLACE_TTYNAME_R', 0)
generated_header_data.set('REPLACE_UNLINK', 0)
generated_header_data.set('REPLACE_UNLINKAT', 0)
generated_header_data.set('REPLACE_UNSETENV', 0)
generated_header_data.set('REPLACE_USLEEP', 0)
generated_header_data.set('REPLACE_UTIMENSAT', 0)
generated_header_data.set('REPLACE_VASPRINTF', 0)
generated_header_data.set('REPLACE_VDPRINTF', 0)
generated_header_data.set('REPLACE_VFPRINTF', 0)
generated_header_data.set('REPLACE_VPRINTF', 0)
generated_header_data.set('REPLACE_VSNPRINTF', 0)
generated_header_data.set('REPLACE_VSPRINTF', 0)
generated_header_data.set('REPLACE_WCRTOMB', 0)
generated_header_data.set('REPLACE_WCSFTIME', 0)
generated_header_data.set('REPLACE_WCSNRTOMBS', 0)
generated_header_data.set('REPLACE_WCSRTOMBS', 0)
generated_header_data.set('REPLACE_WCSTOK', 0)
generated_header_data.set('REPLACE_WCSWIDTH', 0)
generated_header_data.set('REPLACE_WCTOB', 0)
generated_header_data.set('REPLACE_WCTOMB', 0)
generated_header_data.set('REPLACE_WCWIDTH', 0)
generated_header_data.set('REPLACE_WRITE', 0)
generated_header_data.set('UNDEFINE_STRTOK_R', 0)
generated_header_data.set('UNISTD_H_HAVE_SYS_RANDOM_H', 0)
generated_header_data.set('UNISTD_H_HAVE_WINSOCK2_H', 0)
generated_header_data.set('UNISTD_H_HAVE_WINSOCK2_H_AND_USE_SOCKETS', 0)
generated_header_data.set('WINDOWS_64_BIT_ST_SIZE', 0)
generated_header_data.set('WINDOWS_STAT_INODES', 0)
generated_header_data.set('WINDOWS_STAT_TIMESPEC', 0)
if host_machine.system() == 'windows' and not cc.compiles(
  '''#include <sys/types.h>
struct stat buf;
int verify_offt_size[sizeof (off_t) >= 8 ? 1 : -1];''',
)
  generated_header_data.set('WINDOWS_64_BIT_OFF_T', 1)
else
  generated_header_data.set('WINDOWS_64_BIT_OFF_T', 0)
endif


generated_header_data.set10(
  'GNULIB_ENVIRON',
  cdata.get('HAVE_ENVIRON_DECL') == 0,
)
generated_header_data.set10(
  'GNULIB_REALLOCARRAY',
  not cdata.has('HAVE_REALLOCARRAY'),
)
generated_header_data.set10('GNULIB_MEMPCPY', not cdata.has('HAVE_MEMPCPY'))
generated_header_data.set10('GNULIB_STRNDUP', not cdata.has('HAVE_STRNDUP'))
generated_header_data.set10('GNULIB_WAITPID', not cdata.has('HAVE_WAITPID'))
generated_header_data.set10('GNULIB_RAWMEMCHR', not cdata.has('HAVE_RAWMEMCHR'))
generated_header_data.set10(
  'GNULIB_SECURE_GETENV',
  not cdata.has('HAVE_SECURE_GETENV'),
)
generated_header_data.set10(
  'GNULIB_CANONICALIZE_FILE_NAME',
  not cdata.has('HAVE_CANONICALIZE_FILE_NAME'),
)
generated_header_data.set10('GNULIB_SIGACTION', not cdata.has('HAVE_SIGACTION'))
generated_header_data.set10(
  'GNULIB_SIGPROCMASK',
  not cdata.has('HAVE_SIGPROCMASK'),
)
generated_header_data.set10('GNULIB_REALPATH', not cdata.has('HAVE_REALPATH'))
generated_header_data.set10(
  'GNULIB_NL_LANGINFO',
  not cdata.has('HAVE_NL_LANGINFO'),
)
generated_header_data.set10(
  'GNULIB_SETLOCALE_NULL',
  not cdata.has('HAVE_NL_LANGINFO'),
)
generated_header_data.set10('GNULIB_STRSIGNAL', not cdata.has('HAVE_STRSIGNAL'))
generated_header_data.set10('GNULIB_MKSTEMP', not cdata.has('HAVE_MKSTEMP'))
generated_header_data.set10('GNULIB_MKDTEMP', not cdata.has('HAVE_MKDTEMP'))
generated_header_data.set10('GNULIB_READLINK', not cdata.has('HAVE_READLINK'))
generated_header_data.set10(
  'GNULIB_VASNPRINTF',
  not cdata.has('HAVE_VASNPRINTF'),
)
generated_header_data.set10('GNULIB_VASPRINTF', not cdata.has('HAVE_VASPRINTF'))
generated_header_data.set10('GNULIB_WCWIDTH', not cdata.has('HAVE_WCWIDTH'))
generated_header_data.set10('GNULIB_FCNTL', not cdata.has('HAVE_FCNTL'))
generated_header_data.set10('GNULIB_STPCPY', not cdata.has('HAVE_STPCPY'))
generated_header_data.set10(
  'GNULIB_TEMPNAME',
  not cdata.has('HAVE_MKDTEMP') or not cdata.has('HAVE_MKSTEMP'),
)
generated_header_data.set10('GNULIB_PIPE2', not cdata.has('HAVE_PIPE2'))
generated_header_data.set10(
  'GNULIB_GETDTABLESIZE',
  not cdata.has('HAVE_GETDTABLESIZE'),
)
generated_header_data.set10('GNULIB_GETRANDOM', not cdata.has('HAVE_GETRANDOM'))
generated_header_data.set10('GNULIB_LSTAT', not cdata.has('HAVE_LSTAT'))
generated_header_data.set10(
  'GNULIB_MDA_MKDIR',
  host_machine.system() == 'windows',
)


# STRING.H
configure_file(
  input: 'string.in.h.meson',
  output: 'string.h',
  configuration: generated_header_data,
)

# STDIO.H
configure_file(
  input: 'stdio.in.h.meson',
  output: 'stdio.h',
  configuration: generated_header_data,
)

# SPAWN.H
configure_file(
  input: 'spawn.in.h.meson',
  output: 'spawn.h',
  configuration: generated_header_data,
)

# UNISTD.H
if generated_header_data.get('GNULIB_ENVIRON') == 1
  configure_file(
    input: 'unistd.in.h.meson',
    output: 'unistd.h',
    configuration: generated_header_data,
  )
endif

# STDLIB.H
if generated_header_data.get('GNULIB_REALLOCARRAY') == 1
  configure_file(
    input: 'stdlib.in.h.meson',
    output: 'stdlib.h',
    configuration: generated_header_data,
  )
endif

# SIGSEGV.H
if not cdata.has('HAVE_SIGSEGV_H')
  configure_file(
    input: 'sigsegv.in.h',
    output: 'sigsegv.h',
    copy: true,
  )
endif

# ALLOCA.H
if not cdata.has('HAVE_ALLOCA_H')
  configure_file(
    input: 'alloca.in.h',
    output: 'alloca.h',
    configuration: generated_header_data,
  )
endif

# STDIO.H
if not cdata.has('HAVE_MAX_ALIGN_T')
  configure_file(
    input: 'stddef.in.h.meson',
    output: 'stddef.h',
    configuration: generated_header_data,
  )
endif

# SIGNAL.H
if not cdata.has('HAVE_SIGSET_T')
  configure_file(
    input: 'signal.in.h.meson',
    output: 'signal.h',
    configuration: generated_header_data,
  )
endif

# FCNTL.H
if cdata.get('HAVE_DECL_O_CLOEXEC') == 0
  configure_file(
    input: 'fcntl.in.h.meson',
    output: 'fcntl.h',
    configuration: generated_header_data,
  )
endif

# LANGINFO.H
if not cdata.has('HAVE_LANGINFO_H')
  configure_file(
    input: 'langinfo.in.h.meson',
    output: 'langinfo.h',
    configuration: generated_header_data,
  )
endif

# LOCALE.H
if generated_header_data.get('GNULIB_SETLOCALE_NULL') == 1
  configure_file(
    input: 'locale.in.h.meson',
    output: 'locale.h',
    configuration: generated_header_data,
  )
endif

# GETOPT.H
if not cdata.has('HAVE_GETOPT_H')
  configure_file(
    input: 'getopt.in.h.meson',
    output: 'getopt.h',
    configuration: generated_header_data,
  )
  configure_file(
    input: 'getopt-cdefs.in.h',
    output: 'getopt-cdefs.h',
    configuration: generated_header_data,
  )
endif

if generated_header_data.get('GNULIB_WCWIDTH') == 1
  configure_file(
    input: 'wchar.in.h.meson',
    output: 'wchar.h',
    configuration: generated_header_data,
  )
  configure_file(
    input: 'uniwidth.in.h',
    output: 'uniwidth.h',
    copy: true,
  )
  configure_file(
    input: 'unitypes.in.h',
    output: 'unitypes.h',
    copy: true,
  )
endif
sys_random_src = files('sys_random.in.h.meson')
sys_wait_src = files('sys_wait.in.h.meson')
sys_types_src = files('sys_types.in.h.meson')
sys_stat_src = files('sys_stat.in.h.meson')
cppdefs_src = files('c++defs.h')
warnonuse_src = files('warn-on-use.h')
arg_nonnull_src = files('warn-on-use.h')
subdir('sys')

lib_inc = include_directories('.')
m4lib_src = [
  'trim.c',
  'asyncsafe-spin.c',
  'basename-lgpl.c',
  'basename.c',
  'bitrotate.c',
  'c-stack.c',
  'c-strcasecmp.c',
  'c-ctype.c',
  'canonicalize-lgpl.c',
  'canonicalize.c',
  'clean-temp-simple.c',
  'clean-temp.c',
  'close-stream.c',
  'closein.c',
  'closeout.c',
  'concat-filename.c',
  'dup-safer.c',
  'execute.c',
  'exitfail.c',
  'fatal-signal.c',
  'fd-safer.c',
  'file-set.c',
  'filenamecat-lgpl.c',
  'filenamecat.c',
  'findprog-in.c',
  'freadahead.c',
  'gl_avltree_oset.c',
  'gl_linked_list.c',
  'gl_linkedhash_list.c',
  'gl_list.c',
  'gl_oset.c',
  'gl_xlist.c',
  'gl_xoset.c',
  'hash-pjw.c',
  'hash-triple-simple.c',
  'hash.c',
  'localcharset.c',
  'malloc/scratch_buffer_dupfree.c',
  'malloc/scratch_buffer_grow.c',
  'malloc/scratch_buffer_grow_preserve.c',
  'malloc/scratch_buffer_set_array_size.c',
  'malloca.c',
  'mbchar.c',
  'mbiter.c',
  'mbuiter.c',
  'memchr2.c',
  'mkstemp-safer.c',
  'pipe-safer.c',
  'progname.c',
  'propername.c',
  'quotearg.c',
  'sig-handler.c',
  'sigsegv.c',
  'spawn-pipe.c',
  'stackvma.c',
  'striconv.c',
  'strnlen1.c',
  'tmpdir.c',
  'verror.c',
  'version-etc-fsf.c',
  'version-etc.c',
  'wait-process.c',
  'xalloc-die.c',
  'xasprintf.c',
  'xmalloc.c',
  'xmalloca.c',
  'xprintf.c',
  'xsize.c',
  'xstriconv.c',
  'xstrndup.c',
  'xvasprintf.c',
]

if host_machine.system() == 'windows'
  m4lib_src += [
    'windows-spawn.c',
    'windows-spin.c',  # used by asyncsafe-spin.c only for windows
    'msvc-nothrow.c',
    'msvc-inval.c',
  ]
else
  m4lib_src += 'spawn_faction_addchdir.c'
endif

if generated_header_data.get('GNULIB_STRNDUP') == 1
  m4lib_src += 'strndup.c'
endif

if cdata.get('HAVE_DECL___FPENDING') == 0
  m4lib_src += 'fpending.c'
endif

if not cdata.has('HAVE_RAWMEMCHR')
  m4lib_src += 'rawmemchr.c'
endif

if not cdata.has('HAVE_SECURE_GETENV')
  m4lib_src += 'secure_getenv.c'
endif

if not cdata.has('HAVE_ERROR_AT_LINE')
  m4lib_src += 'error.c'
endif

if generated_header_data.get('GNULIB_REALLOCARRAY') == 1
  m4lib_src += 'reallocarray.c'
endif

if not cdata.has('HAVE_SYS_WAIT_H') or not cdata.has('HAVE_SYS_TYPES_H')
  m4lib_src += sys_files
endif

if cdata.get('HAVE_OBSTACK') == 0
  m4lib_src += 'obstack.c'
endif

if generated_header_data.get('GNULIB_SIGACTION') == 1
  m4lib_src += 'sigaction.c'
endif

if not cdata.has('HAVE_REGEX_H') or not cdata.has('HAVE_RE_COMPILE_PATTERN')
  m4lib_src += [
    'regex.c',
    'malloc/dynarray_resize.c',
    'malloc/dynarray_emplace_enlarge.c',
    'malloc/dynarray_finalize.c',
  ]
endif

if not cdata.has('HAVE_GETPROGNAME')
  m4lib_src += 'getprogname.c'
endif

if generated_header_data.get('GNULIB_NL_LANGINFO') == 1
  m4lib_src += 'nl_langinfo.c'
  m4lib_src += 'nl_langinfo-lock.c'
  m4lib_src += 'setlocale_null.c'
endif

if not cdata.has('HAVE_GETOPT_H')
  m4lib_src += 'getopt.c'
  m4lib_src += 'getopt1.c'
endif

if generated_header_data.get('GNULIB_FSEEKO') == 1
  m4lib_src += 'fseeko.c'
endif

if generated_header_data.get('GNULIB_STRSIGNAL') == 1
  m4lib_src += 'strsignal.c'
endif

if generated_header_data.get('GNULIB_SIGPROCMASK') == 1
  m4lib_src += 'sigprocmask.c'
endif

if generated_header_data.get('GNULIB_MKSTEMP') == 1
  m4lib_src += 'mkstemp.c'
endif

if generated_header_data.get('GNULIB_MKDTEMP') == 1
  m4lib_src += 'mkdtemp.c'
endif

if generated_header_data.get('GNULIB_WAITPID') == 1
  m4lib_src += 'waitpid.c'
endif

if generated_header_data.get('GNULIB_TEMPNAME') == 1
  m4lib_src += 'tempname.c'
endif

if generated_header_data.get('GNULIB_MEMPCPY') == 1
  m4lib_src += 'mempcpy.c'
endif

if generated_header_data.get('GNULIB_READLINK') == 1
  m4lib_src += 'readlink.c'
endif

if generated_header_data.get('GNULIB_VASPRINTF') == 1
  m4lib_src += 'vasprintf.c'
endif

if generated_header_data.get('GNULIB_VASNPRINTF') == 1
  m4lib_src += 'vasnprintf.c'
  m4lib_src += 'printf-parse.c'
  m4lib_src += 'printf-args.c'
endif

if generated_header_data.get('GNULIB_WCWIDTH') == 1
  m4lib_src += 'wcwidth.c'
  m4lib_src += 'uniwidth/width.c'
endif

if generated_header_data.get('GNULIB_FCNTL') == 1
  m4lib_src += 'fcntl.c'
endif

if generated_header_data.get('GNULIB_STPCPY') == 1
  m4lib_src += 'stpcpy.c'
endif

if generated_header_data.get('GNULIB_PIPE2') == 1
  m4lib_src += 'pipe2.c'
endif

if cdata.has('GNULIB_PIPE2_SAFER')
  m4lib_src += 'pipe2-safer.c'
endif

if cdata.has('GNULIB_FD_SAFER_FLAG')
  m4lib_src += 'dup-safer-flag.c'
  m4lib_src += 'fd-safer-flag.c'
endif

if generated_header_data.get('GNULIB_MBSLEN') == 1
  m4lib_src += 'mbslen.c'
endif

if generated_header_data.get('GNULIB_MBSSTR') == 1
  m4lib_src += 'mbsstr.c'
endif

if generated_header_data.get('GNULIB_GETDTABLESIZE') == 1
  m4lib_src += 'getdtablesize.c'
endif

if generated_header_data.get('GNULIB_LSTAT') == 1
  m4lib_src += 'lstat.c'
endif

if generated_header_data.get('GNULIB_GETRANDOM') == 1
  m4lib_src += 'getrandom.c'
endif

if generated_header_data.get('GNULIB_FOPEN') == 1
  m4lib_src += 'fopen.c'
endif

if generated_header_data.get('GNULIB_FOPEN_SAFER') == 1
  m4lib_src += 'fopen-safer.c'
endif

if generated_header_data.get('GNULIB_OPEN') == 1
  m4lib_src += 'open.c'
  m4lib_src += 'cloexec.c'
endif

if generated_header_data.get('GNULIB_FFLUSH') == 1
  m4lib_src += 'fflush.c'
  m4lib_src += 'freading.c'
endif

if generated_header_data.get('GNULIB_LSEEK') == 1
  m4lib_src += 'lseek.c'
endif

if generated_header_data.get('GNULIB_FTELLO') == 1
  m4lib_src += 'ftello.c'
endif

if generated_header_data.get('GNULIB_FPURGE') == 1
  m4lib_src += 'fpurge.c'
endif

if generated_header_data.get('GNULIB_RENAME') == 1
  m4lib_src += 'rename.c'
endif

m4_lib_nononnull_h = configure_file(
  input: 'nononnull.h.meson',
  output: 'nononnull.h',
  copy: true,
)

m4_lib = static_library(
  'm4',
  m4lib_src,
  m4_lib_nononnull_h,
  c_args: libm4_c_args,
  override_options: override_opts,
)
if host_machine.system() == 'windows'
  m4_dep = declare_dependency(
    link_with: m4_lib,
    dependencies: getrandom_dep,
    compile_args: libm4_c_args,
    include_directories: lib_inc,
  )
else
  m4_dep = declare_dependency(
    link_with: m4_lib,
    compile_args: libm4_c_args,
    include_directories: lib_inc,
  )
endif
