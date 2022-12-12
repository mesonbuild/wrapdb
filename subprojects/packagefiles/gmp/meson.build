project(
  'gmp',
  'c',
  version : '6.2.1',
  default_options: ['optimization=2']
)

if host_machine.cpu_family() != 'x86_64'
  error('Unsupported cpu family : ', host_machine.cpu_family())
endif


cpp = get_option('cxx')
add_languages('cpp', required: cpp)

conf = configuration_data()
conf.set('CFLAGS', '')  # only used by gmp.in.h when complied for tests, maybe not very important
conf.set('GMP_NAIL_BITS', 0)
conf.set('HAVE_HOST_CPU_FAMILY_power', 0)
conf.set('HAVE_HOST_CPU_FAMILY_powerpc', 0)
conf.set10('WANT_ASSERT', get_option('assert'))
conf.set10('WANT_FFT', get_option('fft'))
conf.set10('WANT_OLD_FFT_FULL', get_option('old-fft-full'))

# Tell gmp.h it's building gmp, not an application, used by windows DLL stuff.
add_project_arguments(
  '-pedantic',
  '-D__GMP_WITHIN_GMP',
  '-DHAVE_CONFIG_H',
  language: ['c', 'cpp'],
)

profiling = get_option('profiling')
if profiling != 'no'
  conf.set('WANT_PROFILING_' + profiling.to_upper(), 1)
endif

# -fomit-frame-pointer is incompatible with -pg on some chips
if profiling != 'gprof'
  add_project_arguments('-fomit-frame-pointer', language: ['c', 'cpp'])
endif

if profiling == 'prof'
  add_project_arguments('-p', ['c'])
elif profiling == 'gprof'
  add_project_arguments('-pg', ['c'])
elif profiling == 'instrument'
  add_project_arguments('-finstrument-functions', ['c'])
endif

fake_cpuid = get_option('fake-cpuid')
conf.set('WANT_FAKE_CPUID', fake_cpuid.to_int())

assembly = get_option('assembly')
# fat = get_option('fat')

# if fat and not assembly
#   error('when doing a fat build, disabling assembly will not work')
# endif

# if fake_cpuid and not fat
#   error('enabling fake-cpuid requires enabling fat')
# endif

host_machine_cpu = host_machine.cpu()
mpn_search_path = ['generic']
conf.set('NO_ASM', 1)
conf.set('HAVE_HOST_CPU_' + host_machine.cpu(), 1)
conf.set('HAVE_HOST_CPU_FAMILY_' + host_machine.cpu_family(), 1)
calling_conventions_objs = ['amd64call.lo', 'amd64check$U.lo']
speed_cyclecounter_obj = 'x86_64.lo'
cyclecounter_size = 2
conf.set('HAVE_SPEED_CYCLECOUNTER', cyclecounter_size)

limb = []
if host_machine.system() == 'cygwin'
  calling_conventions_objs = []
  limb = ['longlong']
  conf.set('HOST_DOS64', 1)
endif

if assembly and calling_conventions_objs.length() > 0
  conf.set('HAVE_CALLING_CONVENTIONS', 1)
endif

cc = meson.get_compiler('c')
conf.set('CC', cc.get_id())

# If we're supposed to be using a "long long" for a limb, check that it works.
if limb.get(0, '') == 'longlong'
  if not cc.compiles(
    '''
    long long  foo;
    long long  bar () { return foo; }
    int main () { return 0; }
    '''
  )
    error('the chosen compiler does not support long long')
  endif
  DEFN_LONG_LONG_LIMB='#define _LONG_LONG_LIMB 1'
else
  DEFN_LONG_LONG_LIMB='/* #undef _LONG_LONG_LIMB */'
endif
conf.set('DEFN_LONG_LONG_LIMB', DEFN_LONG_LONG_LIMB)

if get_option('default_library') != 'static'
    add_project_link_arguments(
      '-no-undefined',
      '-Wl,--export-all-symbols',
      language: ['c', 'cpp']
    )
    conf.set('LIBGMP_DLL', 1)
endif

check_declarations = [
  ['fgetc', 'stdio.h'],
  ['fscanf', 'stdio.h'],
  ['optarg', 'unistd.h'],
  ['ungetc', 'stdio.h'],
  ['vfprintf', 'stdio.h'],
  ['sys_errlist', 'errno.h'],
  ['sys_nerr', 'errno.h'],
]

foreach d : check_declarations
  if cc.has_header_symbol(d.get(1), d.get(0))
    conf.set('HAVE_DECL_' + d.get(0).to_upper(), 1)
  endif
endforeach

check_types = [
  'intmax_t',
  'intptr_t',
  'long double',
  'long long',
  'ptrdiff_t',
  'quad_t',
  'uint_least32_t',
]

foreach t : check_types
  if cc.has_type(t)
    conf.set('HAVE_' + t.underscorify().to_upper(), 1)
  endif
endforeach

check_attributes = [
  'const',
  'malloc',
  'noreturn'
]

foreach a : check_attributes
  if cc.has_function_attribute(a)
    conf.set('HAVE_ATTRIBUTE_' + a.underscorify().to_upper(), 1)
  endif
endforeach

conf.set('HAVE_ATTRIBUTE_MODE', 0)

if cc.compiles(
  '''
  void hid() __attribute__ ((visibility("hidden")));
  void hid() {}
  void pub() __attribute__ ((alias("hid")));
  ''',
  name: 'has hidden alias'
)
  conf.set('HAVE_HIDDEN_ALIAS', 1)
endif

alloca = get_option('alloca')
if alloca == 'yes'
  gmp_cv_option_alloca = 'alloca'
elif alloca == 'no'
  gmp_cv_option_alloca = 'malloc-reentrant'
elif alloca == 'reentrant' or alloca == 'notreentrant'
  if cc.has_function('alloca', prefix : '#include<alloca.h>')
    gmp_cv_option_alloca = 'alloca'
  else
    gmp_cv_option_alloca = 'malloc-' + alloca
  endif
else
  gmp_cv_option_alloca = alloca
endif

GMP_INCLUDE_GMP_H = (
  f'''
  #define __GMP_WITHIN_CONFIGURE 1   /* ignore template stuff */
  #define GMP_NAIL_BITS $GMP_NAIL_BITS
  #define GMP_LIMB_BITS 123
  @DEFN_LONG_LONG_LIMB@
  #include "gmp-h.in"
  '''
)

if not cc.compiles(
  f'''
  #include <stdio.h>
  @GMP_INCLUDE_GMP_H@
  #if ! _GMP_H_HAVE_FILE
  die die die
  #endif
  ''',
  include_directories: include_directories('')
)
  warning('gmp.h doesnt recognise <stdio.h>, FILE prototypes will be unavailable')
endif

if host_machine.endian() == 'big'
  conf.set('HAVE_LIMB_BIG_ENDIAN', 1)
else
  conf.set('HAVE_LIMB_LITTLE_ENDIAN', 1)
endif

# True for all x86_64 CPU ... right ?
conf.set('HAVE_DOUBLE_IEEE_LITTLE_ENDIAN', 1)

check_headers = [
  'alloca.h',
  'dlfcn.h',
  'fcntl.h',
  'float.h',
  'inttypes.h',
  'invent.h',
  'langinfo.h',
  'locale.h',
  'machine/hal/sysinfo.h',
  'memory.h',
  'nl_types.h',
  'stdint.h',
  'stdlib.h',
  'strings.h',
  'string.h',
  'sys/attributes.h',
  'sys/iograph.h',
  'sys/mman.h',
  'sys/param.h',
  'sys/processor.h',
  'sys/pstat.h',
  'sys/resource.h',
  'sys/stat.h',
  'sys/sysctl.h',
  'sys/sysinfo.h',
  'sys/syssgi.h',
  'sys/systemcfg.h',
  'sys/times.h',
  'sys/time.h',
  'sys/types.h',
  'unistd.h',
]

foreach h : check_headers
  if cc.has_header(h)
    conf.set('HAVE_' + h.underscorify().to_upper(), 1)
  endif
endforeach

check_functions = [
  ['HAVE_ALARM', 'alarm', '#include<unistd.h>'],
  ['HAVE_ALLOCA', 'alloca', '#include<alloca.h>'],
  ['HAVE_ATTR_GET', 'attr_get', '#include<attr/attributes.h>'],
  ['HAVE_CLOCK', 'clock', '#include<time.h>'],
  ['HAVE_CLOCK_GETTIME', 'clock_gettime', '#include<time.h>'],
# ['HAVE_CPUTIME'] not in glibc, can't find any manual page referencing it, most likely a very old API
  ['HAVE_LOCALECONV', 'localeconv', '#include<locale.h>'],
  ['HAVE_GETPAGESIZE', 'getpagesize', '#include<unistd.h>'],
  ['HAVE_GETRUSAGE', 'getrusage', '#include <sys/resource.h>'],
  ['HAVE_GETSYSINFO', 'getsysinfo', '#include<machine/hal_sysinfo.h>'],  # https://www.unix.com/man-page/osf1/2/getsysinfo/
  ['HAVE_GETTIMEOFDAY', 'gettimeofday', '#include<sys/time.h>'],
  ['HAVE_MEMSET', 'memset', '#include<string.h>'],
  ['HAVE_MMAP', 'mmap', '#include<sys/mman.h>'],
  ['HAVE_MPROTECT', 'mprotect', '#include<sys/mman.h>'],
  ['HAVE_NL_LANGINFO', 'nl_langinfo', '#include<langinfo.h>'],  # https://man7.org/linux/man-pages/man3/nl_langinfo.3.html
  ['HAVE_OBSTACK_VPRINTF', 'obstack_vprintf', '#include<stdio.h>'],  # https://www.gnu.org/software/libc/manual/html_node/Variable-Arguments-Output.html
  ['HAVE_POPEN', 'popen', '#include<stdio.h>'],
  ['HAVE_PROCESSOR_INFO', 'processor_info', '#include<sys/processor.h>'],  # https://www.unix.com/man-page/freebsd/2/processor_info/
  ['HAVE_PSTAT_GETPROCESSOR', 'pstat_getprocessor', '#include<sys/pstat.h>'],  # https://docstore.mik.ua/manuals/hp-ux/en/B2355-60130/pstat.2.html
  ['HAVE_RAISE', 'raise', '#include<signal.h>'],
  ['HAVE_READ_REAL_TIME', 'read_real_time', '#include<sys/time.h>'],  # https://www.ibm.com/docs/en/aix/7.1?topic=r-read-real-time-read-wall-timetime-base-time-mread-real-time-subroutine
  ['HAVE_SIGACTION', 'sigaction', '#include<signal.h>'],
  ['HAVE_SIGALTSTACK', 'sigaltstack', '#include<signal.h>'],
  ['HAVE_SIGSTACK', 'sigstack', '#include <signal.h>'],  # https://www.ibm.com/docs/en/zos/2.3.0?topic=functions-sigstack-set-get-signal-stack-context
# check token ['HAVE_STACK_T']
  ['HAVE_STRCHR', 'strchr', '#include<string.h>'],
  ['HAVE_STRERROR', 'strerror', '#include<string.h>'],
  ['HAVE_STRNLEN', 'strnlen', '#include<string.h>'],
  ['HAVE_STRTOL', 'strtol', '#include<stdlib.h>'],
  ['HAVE_STRTOUL', 'strtoul', '#include<stdlib.h>'],
  ['HAVE_SYSCONF', 'sysconf', '#include<unistd.h>'],
# ['HAVE_SYSCTL'] long-since deprecated  https://man7.org/linux/man-pages/man2/sysctl.2.html#NOTES
  ['HAVE_SYSCTLBYNAME', 'sysctlbyname', '#include<sys/sysctl.h>'],
  ['HAVE_SYSSGI', 'syssgi', '#include<sys/syssgi.h>'],  # http://www.polarhome.com/service/man/?qf=syssgi&tf=2&of=IRIX&sf=
  ['HAVE_TIMES', 'times', '#include<sys/times.h>'],
  ['HAVE_VSNPRINTF', 'vsnprintf', '#include<stdio.h>'],
]

foreach f : check_functions
  if cc.has_function(f.get(1), prefix : f.get(2))
    conf.set(f.get(0), 1)
  endif
endforeach

SIZEOF_MP_LIMB_T = cc.sizeof(
  'mp_limb_t',
  prefix: GMP_INCLUDE_GMP_H,
  include_directories: include_directories('')
)
conf.set('SIZEOF_MP_LIMB_T', SIZEOF_MP_LIMB_T)
conf.set('GMP_LIMB_BITS', 8 * SIZEOF_MP_LIMB_T)
conf.set('SIZEOF_UNSIGNED', cc.sizeof('unsigned'))
conf.set('SIZEOF_UNSIGNED_LONG', cc.sizeof('unsigned long'))
conf.set('SIZEOF_UNSIGNED_SHORT', cc.sizeof('unsigned short'))
conf.set('SIZEOF_VOID_P', cc.sizeof('void*'))

# check token ['HAVE_PSP_ITICKSPERCLKTICK']
if cc.has_member(
  'struct pst_processor',
  'psp_iticksperclktick',
  prefix: '#include <sys/pstat.h>'
)
  conf.set('HAVE_PSP_ITICKSPERCLKTICK', 1)
endif

# C++ tests, when required
if cpp
  cppc = meson.get_compiler('cpp')
  # Reasons for testing:
  #   <sstream> - not in g++ 2.95.2
  #   std::locale - not in g++ 2.95.4
  if cppc.has_header('sstream')
    conf.set('HAVE_SSTREAM', 1)
  endif
  if cc.has_type('std::locale', prefix: '#include <locale>')
    conf.set('HAVE_STD__LOCALE', 1)
  endif
endif

# if get_option('minithres')
#   mpn_search_path = ['minithres'] + mpn_search_path
# endif

configure_file(
  input: 'config.in.meson',
  output: 'config.h',
  configuration: conf,
)

gmp_h = configure_file(
  input: 'gmp.in.meson',
  output: 'gmp.h',
  configuration: conf,
)

install_headers(gmp_h)

if cpp
  install_headers('gmpxx.h')
endif

sources = files(
  'assert.c',
  'bootstrap.c',
  'compat.c',
  'errno.c',
  'extract-dbl.c',
  'gen-bases.c',
  'gen-fac.c',
  'gen-fib.c',
  'gen-jacobitab.c',
  'gen-psqr.c',
  'gen-trialdivtab.c',
  'invalid.c',
  'memory.c',
  'mp_bpl.c',
  'mp_clz_tab.c',
  'mp_dv_tab.c',
  'mp_get_fns.c',
  'mp_minv_tab.c',
  'mp_set_fns.c',
  'nextprime.c',
  'primesieve.c',
  'tal-debug.c',
  'tal-notreent.c',
  'tal-reent.c',
  'version.c',
)

subdir('mpn')
subdir('mpz')
subdir('mpq')
subdir('mpf')
subdir('printf')
subdir('scanf')
subdir('rand')
if cpp
  subdir('cxx')
endif
# subdir('demos')
# subdir('tune')
# subdir('doc')

gmp_lib = library(
    'gmp',
    sources,
    include_directories: include_directories('.'),
    version: meson.project_version(),
    install: true
)

gmp_dep = declare_dependency(
    include_directories: include_directories('.'),
    link_with: gmp_lib,
)
