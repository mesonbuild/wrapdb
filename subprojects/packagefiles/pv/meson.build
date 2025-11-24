project(
  'pv',
  'c',
  license: 'GPL-3.0-or-later',
  version: '1.10.2',
  meson_version: '>=0.59.0',
)

cc = meson.get_compiler('c')
cdata = configuration_data()
feature_macros = [
  '-D_ALL_SOURCE',
  '-D_DARWIN_C_SOURCE',
  '-D_GNU_SOURCE',
  '-D_NETBSD_SOURCE',
  '-D_OPENBSD_SOURCE',
  '-D_POSIX_SOURCE',
]

ncurses_dep = dependency(
  'curses',
  required: get_option('ncurses'),
)
intl_dep = cc.find_library(
  'intl',
  required: false,
)
rt_dep = cc.find_library(
  'rt',
  required: false,
)

m_dep = dependency(
  '',
  required: false,
)
foreach _fn : ['fmod', 'sqrtl']
  if not cc.has_function(
    _fn,
    prefix: '#include <math.h>',
  )
    m_dep = cc.find_library('m')
    break
  endif
endforeach

foreach _spec : [
  ['fcntl.h', 'posix_fadvise splice'],
  ['getopt.h', 'getopt_long'],
  ['langinfo.h'],
  ['libgen.h', 'basename'],
  ['libintl.h', 'gettext'],
  ['limits.h'],
  ['locale.h', 'setlocale'],
  ['math.h', 'fmod sqrtl'],
  ['signal.h', 'SA_SIGINFO'],
  ['stdbool.h'],
  ['stdint.h'],
  ['stdio.h', 'vsnprintf'],
  ['stdlib.h', 'posix_memalign strtoul'],
  [
    'string.h',
    'memcpy memmove memrchr memset strchr strerror strlcat strrchr strstr',
  ],
  ['sys/file.h'],
  ['sys/ioctl.h'],
  ['sys/ipc.h'],
  ['sys/sysmacros.h'],
  ['sys/param.h'],
  ['sys/select.h', 'select'],
  ['sys/shm.h', 'shmget'],
  ['sys/stat.h', 'mkdir'],
  ['sys/time.h', 'setitimer'],
  ['term.h'],
  ['termios.h'],
  ['time.h', 'clock_gettime nanosleep'],
  [
    'unistd.h',
    'alarm dup2 fdatasync fpathconf getcwd getopt setproctitle sysconf',
  ],
  ['wchar.h'],
  ['wctype.h'],
]
  _hdr = _spec[0]
  _symlist = _spec.get(1, '').split()
  _has_hdr = cc.has_header(_hdr)
  cdata.set('HAVE_' + _hdr.underscorify().to_upper(), _has_hdr)
  foreach _sym : _symlist
    _flag = 'HAVE_' + _sym.underscorify().to_upper()
    if cdata.get(_flag, false)
      continue
    endif
    cdata.set(
      _flag,
      _has_hdr and cc.has_header_symbol(
        _hdr,
        _sym,
        args: feature_macros,
      ),
    )
  endforeach
endforeach

foreach _sym : ['SA_SIGINFO']
  cdata.set('HAVE_DECL_' + _sym, cdata.get('HAVE_' + _sym))
endforeach

_missing = []
foreach _hdr : [
  'fcntl.h',
  'limits.h',
  'stdio.h',
  'stdlib.h',
  'string.h',
  'sys/file.h',
  'sys/time.h',
  'unistd.h',
]
  if not cdata.get('HAVE_' + _hdr.underscorify().to_upper())
    _missing += [_hdr]
  endif
endforeach
if _missing.length() > 0
  error('unsupported system, missing required headers: ' + ', '.join(_missing))
endif

_missing = []
foreach _fn : [
  'alarm',
  'basename',
  'clock_gettime',
  'dup2',
  'getcwd',
  'memcpy',
  'memmove',
  'memset',
  'mkdir',
  'select',
  'setlocale',
  'strchr',
  'strerror',
  'strrchr',
  'strstr',
]
  if not cdata.get('HAVE_' + _fn.underscorify().to_upper())
    _missing += [_fn]
  endif
endforeach
if _missing.length() > 0
  error('unsupported system, missing required functions: ' + ', '.join(_missing))
endif

foreach _type : ['_Bool']
  cdata.set(
    'HAVE_' + _type.underscorify().to_upper(),
    cc.has_type(
      _type,
      args: feature_macros,
    ),
  )
endforeach

if meson.is_cross_build()
  message('Assuming siginfo_t provides a signal sender\'s PID')
  siginfo_provides_pid = true
else
  siginfo_provides_pid = cc.run(
    '''
    #include <string.h>
    #include <signal.h>
    #include <unistd.h>

    static pid_t signalSender = 0;

    #ifdef SA_SIGINFO
    static void receiveUSR2( __attribute__((unused))
                           int sig, siginfo_t * info, __attribute__((unused))
                           void *ucontext)
    {
           if (NULL != info)
                   signalSender = info->si_pid;
    }
    #endif

    int main(int argc, char **argv) {
           struct sigaction sa;
           memset(&sa, 0, sizeof(sa));
    #ifdef SA_SIGINFO
           sa.sa_sigaction = receiveUSR2;
           (void) sigemptyset(&(sa.sa_mask));
           sa.sa_flags = SA_SIGINFO;
           (void) sigaction(SIGUSR2, &sa, NULL);
           raise(SIGUSR2);
    #endif
           return signalSender < 1 ? 1 : 0;
    }
    ''',
    name: 'siginfo_t provides a signal sender\'s PID',
  ).returncode() == 0
endif
cdata.set('SIGINFO_PROVIDES_PID', siginfo_provides_pid)

cdata.set(
  'HAVE_GETTEXT',
  cdata.get('HAVE_GETTEXT') and cc.has_function(
    'gettext',
    dependencies: intl_dep,
  ),
)

cdata.set('ENABLE_NCURSES', ncurses_dep.found())

nls_opt = get_option('nls').require(
  cdata.get('HAVE_GETTEXT'),
  error_message: 'not supported',
)
cdata.set('ENABLE_NLS', nls_opt.allowed())

ipc_opt = get_option('ipc').require(
  cdata.get('HAVE_SHMGET') and cdata.get('HAVE_SYS_IPC_H') and cdata.get(
    'HAVE_SYS_SHM_H',
  ),
  error_message: 'not supported',
)
cdata.set('HAVE_IPC', ipc_opt.allowed())

splice_opt = get_option('splice').require(
  cdata.get('HAVE_SPLICE'),
  error_message: 'need "splice" system call',
)
cdata.set('HAVE_SPLICE', splice_opt.allowed())

foreach _spec : [
  ['sys/stat.h', 'struct stat', 'st_blksize'],
  ['sys/stat.h', 'struct stat', 'st_rdev'],
]
  cdata.set(
    'HAVE_' + _spec[1].underscorify().to_upper() + '_' + _spec[2].underscorify().to_upper(),
    cc.has_member(
      _spec[1],
      _spec[2],
      prefix: '#include <' + _spec[0] + '>',
    ),
  )
endforeach

summary(
  {
    'ncurses support': ncurses_dep.found(),
    'IPC messaging': ipc_opt.allowed(),
    'Native language support': nls_opt.allowed(),
    'Use splice system call': splice_opt.allowed(),
  },
  bool_yn: true,
)

foreach _flag : cdata.keys()
  cdata.set(_flag, cdata.get(_flag) ? 1 : false)
endforeach

cdata.set_quoted(
  'LOCALEDIR',
  get_option('prefix') / get_option('localedir'),
)
cdata.set_quoted('PACKAGE', meson.project_name())
cdata.set_quoted('PACKAGE_BUGREPORT', 'pv@ivarch.com')
cdata.set_quoted('PACKAGE_NAME', meson.project_name())
cdata.set_quoted('PACKAGE_VERSION', meson.project_version())
cdata.set_quoted('PACKAGE_URL', 'https://www.ivarch.com/programs/pv.shtml')

subdir('src/include')

pv = executable(
  'pv',
  [
    config_h,
    'src/main/debug.c',
    'src/main/help.c',
    'src/main/main.c',
    'src/main/options.c',
    'src/main/version.c',
    'src/pv/format/averagerate.c',
    'src/pv/format/barstyle.c',
    'src/pv/format/bufferpercent.c',
    'src/pv/format/bytes.c',
    'src/pv/format/eta.c',
    'src/pv/format/fineta.c',
    'src/pv/format/lastwritten.c',
    'src/pv/format/name.c',
    'src/pv/format/previousline.c',
    'src/pv/format/progressbar.c',
    'src/pv/format/rate.c',
    'src/pv/format/sgr.c',
    'src/pv/format/timer.c',
    'src/pv/calc.c',
    'src/pv/cursor.c',
    'src/pv/display.c',
    'src/pv/elapsedtime.c',
    'src/pv/file.c',
    'src/pv/loop.c',
    'src/pv/number.c',
    'src/pv/proctitle.c',
    'src/pv/remote.c',
    'src/pv/signal.c',
    'src/pv/state.c',
    'src/pv/string.c',
    'src/pv/transfer.c',
    'src/pv/watchpid.c',
  ],
  c_args: feature_macros + ['-DHAVE_CONFIG_H'],
  dependencies: [intl_dep, m_dep, ncurses_dep, rt_dep],
  implicit_include_directories: false,
  include_directories: 'src/include',
  install: true,
)
meson.override_find_program('pv', pv)

tests_opt = get_option('tests').disable_auto_if(
  # Tests are way too flaky on macOS.
  host_machine.system() == 'darwin',
)
sh = find_program(
  'sh',
  required: tests_opt,
)
if tests_opt.require(sh.found()).allowed()
  subdir('tests')
endif
