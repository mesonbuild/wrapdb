project(
  'mpdecimal',
  'c',
  'cpp',
  version: '2.5.1',
  license: 'BSD-2-Clause',
  default_options: ['c_std=c99', 'cpp_std=c++14', 'b_ndebug=true'],
)

library_soversion = '3'
library_version = meson.project_version()
v = library_version.split('.')
compat_version = '.'.join([v[0], v[1]])

cc = meson.get_compiler('c')
m_dep = cc.find_library(
  'm',
  required: false,
)

conf = configuration_data()

have_uint128_t = cc.sizeof('__uint128_t') > 0

# x64 with gcc asm:
gcc_asm_for_x64 = cc.compiles(
  '''
  int main()
  {
    __asm__ __volatile__ ("movq %rcx, %rax");
  }''',
  name: 'x64 gcc inline assembler',
)

# x87 with gcc asm:
gcc_asm_for_x87 = cc.compiles(
  '''
  int main()
  {
    unsigned short cw;
    __asm__ __volatile__ ("fnstcw %0" : "=m" (cw));
    __asm__ __volatile__ ("fldcw %0" : : "m" (cw));
  }''',
  name: 'x87 gcc inline assembler',
)

# _FORTIFY_SOURCE wrappers for memmove and bcopy are incorrect:
# https://sourceware.org/ml/libc-alpha/2010-12/msg00009.html
if cc.run(
  '''
  #include <stdio.h>
  #include <stdlib.h>
  #include <string.h>
  void foo(void *p, void *q) { memmove(p, q, 19); }
  int main() {
    char a[32] = "123456789000000000";
    foo(&a[9], a);
    if (strcmp(a, "123456789123456789000000000") != 0)
      return 1;
    foo(a, &a[9]);
    if (strcmp(a, "123456789000000000") != 0)
      return 1;
    return 0;
  }''',
  args: ['-O2', '-D_FORTIFY_SOURCE=2'],
  name: 'glibc _FORTIFY_SOURCE/memmove',
).returncode() != 0

  warning(
    '''
***************************** WARNING *********************************

Detected glibc _FORTIFY_SOURCE/memmove bug. See:

    https://sourceware.org/ml/libc-alpha/2010-12/msg00009.html

Enabling -U_FORTIFY_SOURCE workaround. If -D_FORTIFY_SOURCE is also
present in the command line, make sure that the order of the two
options is:

   ... -D_FORTIFY_SOURCE=2 ... -U_FORTIFY_SOURCE ...

A better solution is to upgrade glibc or to report the bug to your
OS vendor.

***************************** WARNING *********************************
''',
  )
  add_project_arguments(
    '-U_FORTIFY_SOURCE',
    language: 'c',
  )
endif


# Values for the MPD_HEADER_CONFIG variable
mpd_header_config_64 = '''
/* ABI: 64-bit */
#define MPD_CONFIG_64 1

#ifdef MPD_CONFIG_32
  #error "cannot use MPD_CONFIG_32 with 64-bit header."
#endif

#ifdef CONFIG_32
  #error "cannot use CONFIG_32 with 64-bit header."
#endif'''

mpd_header_config_32 = '''
/* ABI: 32-bit */
#define MPD_CONFIG_32 1

#ifdef MPD_CONFIG_64
  #error "cannot use MPD_CONFIG_64 with 32-bit header."
#endif

#ifdef CONFIG_64
  #error "cannot use CONFIG_64 with 32-bit header."
#endif'''

mpd_header_config_32_legacy = '''
/* ABI: 32-bit */
#define MPD_CONFIG_32 1

/* libmpdec was compiled without support for int64_t */
#define MPD_LEGACY_COMPILER 1

#ifdef MPD_CONFIG_64
  #error "cannot use MPD_CONFIG_64 with 32-bit header."
#endif

#ifdef CONFIG_64
  #error "cannot use CONFIG_64 with 32-bit header."
#endif'''

mpd_header_config_universal = '''
/* Mac OS X: support for building universal binaries */
#if defined(MPD_CONFIG_64) || defined(MPD_CONFIG_32)
  #error "cannot use MPD_CONFIG_64 or MPD_CONFIG_32 with universal header."
#endif

#if defined(CONFIG_64) || defined(CONFIG_32)
  #error "cannot use CONFIG_64 or CONFIG_32 with universal header."
#endif

#if defined(__ppc__)
  #define MPD_CONFIG_32 1
  #ifdef UNIVERSAL
    #define CONFIG_32
    #define ANSI
  #endif
#elif defined(__ppc64__)
  #define MPD_CONFIG_64 1
  #ifdef UNIVERSAL
    #define CONFIG_64
    #define ANSI
  #endif
#elif defined(__i386__)
  #define MPD_CONFIG_32 1
  #ifdef UNIVERSAL
    #define CONFIG_32
    #define ANSI
  #endif
#elif defined(__x86_64__)
  #define MPD_CONFIG_64 1
  #ifdef UNIVERSAL
    #define CONFIG_64
    #define ASM
  #endif
#elif defined(__arm64__)
  #define MPD_CONFIG_64 1
  #ifdef UNIVERSAL
    #define CONFIG_64
    #define ANSI
  #endif
#else
  #error "unknown architecture for universal build."
#endif'''


machine = get_option('machine')

if machine == 'auto'
  if host_machine.system() == 'windows'
    if have_uint128_t
      machine = 'uint128'
    elif host_machine.cpu_family() == 'x86'
      machine = 'ppro'
    elif host_machine.cpu_family() == 'x86_64'
      machine = 'x64'
    endif
  else
    if cc.sizeof('size_t') == 8
      if gcc_asm_for_x64
        machine = 'x64'
      elif have_uint128_t
        machine = 'uint128'
      else
        machine = 'ansi64'
      endif
    else
      if cc.get_id() == 'ccomp'
        machine = 'ansi-legacy'
      else
        machine = 'ansi32'
      endif
      if gcc_asm_for_x87
        if cc.get_id() == 'gcc' or cc.get_id() == 'clang'
          if target_machine.system() != 'darwin'
            machine = 'ppro'
          endif
        endif
      endif
    endif
  endif
endif


add_project_arguments(
  cc.get_supported_arguments('-Wno-unknown-pragmas'),
  language: ['c', 'cpp'],
)


if machine == 'x64'
  conf.set('MPD_HEADER_CONFIG', mpd_header_config_64)
  add_project_arguments(
    '-DCONFIG_64',
    language: 'c',
  )
  if host_machine.system() == 'windows'
    add_project_arguments(
      '-DMASM',
      language: 'c',
    )
  else
    add_project_arguments(
      '-DASM',
      language: 'c',
    )
    add_project_arguments(
      '-m64',
      language: ['c', 'cpp'],
    )
    add_project_link_arguments(
      '-m64',
      language: ['c', 'cpp'],
    )
  endif

elif machine == 'uint128'
  conf.set('MPD_HEADER_CONFIG', mpd_header_config_64)
  add_project_arguments(
    '-DCONFIG_64',
    '-DANSI',
    '-DHAVE_UINT128_T',
    language: 'c',
  )
  if host_machine.system() != 'windows'
    add_project_arguments(
      '-m64',
      language: ['c', 'cpp'],
    )
    add_project_link_arguments(
      '-m64',
      language: ['c', 'cpp'],
    )
  endif

elif machine == 'ansi64'
  conf.set('MPD_HEADER_CONFIG', mpd_header_config_64)
  add_project_arguments(
    '-DCONFIG_64',
    '-DANSI',
    language: 'c',
  )
  if host_machine.system() != 'windows'
    add_project_arguments(
      '-m64',
      language: ['c', 'cpp'],
    )
    add_project_link_arguments(
      '-m64',
      language: ['c', 'cpp'],
    )
  endif

elif machine == 'ppro'
  conf.set('MPD_HEADER_CONFIG', mpd_header_config_32)
  add_project_arguments(
    '-DCONFIG_32',
    '-DPPRO',
    '-DASM',
    language: 'c',
  )
  if host_machine.system() == 'windows'
    add_project_arguments(
      '-DMASM',
      language: 'c',
    )
  else
    add_project_arguments(
      '-DASM',
      language: 'c',
    )
    add_project_arguments(
      '-m32',
      language: ['c', 'cpp'],
    )
    add_project_link_arguments(
      '-m32',
      language: ['c', 'cpp'],
    )
  endif

  # Some versions of gcc miscompile inline asm:
  # https://gcc.gnu.org/bugzilla/show_bug.cgi?id=46491
  # https://gcc.gnu.org/ml/gcc/2010-11/msg00366.html
  if cc.get_id() == 'gcc' and cc.run(
    '''
    __attribute__((noinline)) int
    foo(int *p) {
      int r;
      asm ( "movl \$6, (%1)\n\t"
            "xorl %0, %0\n\t"
            : "=r" (r) : "r" (p) : "memory"
      );
      return r;
    }
    int main() {
      int p = 8;
      if ((foo(&p) ? : p) != 6)
        return 1;
      return 0;
    }''',
    args: ['-O2'],
    name: 'gcc ipa-pure-const',
  ).returncode() != 0

    add_project_arguments(
      '-fno-ipa-pure-const',
      language: 'c',
    )
  endif

elif machine == 'ansi32'
  conf.set('MPD_HEADER_CONFIG', mpd_header_config_32)
  add_project_arguments(
    '-DCONFIG_32',
    '-DANSI',
    language: 'c',
  )
  if host_machine.system() != 'windows' and cc.sizeof('size_t') > 4
    add_project_arguments(
      '-m32',
      language: ['c', 'cpp'],
    )
    add_project_link_arguments(
      '-m32',
      language: ['c', 'cpp'],
    )
  endif

elif machine == 'ansi-legacy'
  conf.set('MPD_HEADER_CONFIG', mpd_header_config_32_LEGACY)
  add_project_arguments(
    '-DCONFIG_32',
    '-DANSI',
    '-DLEGACY_COMPILER',
    language: 'c',
  )
  if host_machine.system() != 'windows'
    add_project_arguments(
      '-m32',
      language: ['c', 'cpp'],
    )
    add_project_link_arguments(
      '-m32',
      language: ['c', 'cpp'],
    )
  endif

elif machine == 'universal'
  add_project_arguments(
    '-DUNIVERSAL',
    language: 'c',
  )
  conf.set('MPD_HEADER_CONFIG', mpd_header_config_UNIVERSAL)
  if host_machine.system() == 'windows'
    error('machine "universal" not supported on Windows')
  endif

endif

libmpdec_c_args = []
libmpdecpp_cpp_args = []
if cc.get_argument_syntax() == 'msvc'
  add_project_arguments(
    '/wd4200',
    '/wd4204',
    '/wd4221',
    '/D_CRT_SECURE_NO_WARNINGS',
    '/nologo',
    language: 'c',
  )
  if get_option('default_library') != 'static'
    libmpdec_c_args = ['/DBUILD_LIBMPDEC']
    libmpdecpp_cpp_args = ['/DBUILD_LIBMPDECXX']
  endif
  vcver = machine == 'x64' ? '64vc' : '32vc'
  mpdecimal_h = configure_file(
    input: 'libmpdec/mpdecimal@0@.h'.format(vcver),
    output: 'mpdecimal.h',
    copy: true,
  )
else
  mpdecimal_h = configure_file(
    input: 'libmpdec/mpdecimal.h.in',
    output: 'mpdecimal.h',
    configuration: conf,
  )
endif

libmpdec_sources = files(
  'libmpdec/basearith.c',
  'libmpdec/constants.c',
  'libmpdec/context.c',
  'libmpdec/convolute.c',
  'libmpdec/crt.c',
  'libmpdec/difradix2.c',
  'libmpdec/fnt.c',
  'libmpdec/fourstep.c',
  'libmpdec/io.c',
  'libmpdec/mpalloc.c',
  'libmpdec/mpdecimal.c',
  'libmpdec/mpsignal.c',
  'libmpdec/numbertheory.c',
  'libmpdec/sixstep.c',
  'libmpdec/transpose.c',
)

if cc.get_argument_syntax() == 'msvc' and machine == 'x64'
  ml = find_program('ml64')
  libmpdec_sources += custom_target(
    'vcdiv64.asm.obj',
    input: 'libmpdec/vcdiv64.asm',
    output: 'vcdiv64.asm.obj',
    command: [ml, '/Cx', '/Fo', '@OUTPUT@', '/c', '@INPUT@'],
  )
endif

libmpdec = library(
  'mpdec',
  libmpdec_sources,
  c_args: libmpdec_c_args,
  dependencies: m_dep,
  version: library_version,
  soversion: library_soversion,
  darwin_versions: [compat_version, library_version],
  override_options: ['optimization=2'],
)

mpdec_dep = declare_dependency(
  link_with: libmpdec,
  # mpdecimal.h is generated in the project root directory
  include_directories: include_directories('.', 'libmpdec'),
)

libmpdecpp_sources = files('libmpdec++/decimal.cc')

libmpdecpp = library(
  'mpdec++',
  libmpdecpp_sources,
  mpdecimal_h,
  cpp_args: libmpdecpp_cpp_args,
  dependencies: [m_dep, mpdec_dep],
  version: library_version,
  soversion: library_soversion,
  darwin_versions: [compat_version, library_version],
  override_options: ['optimization=3'],
)

install_headers(mpdecimal_h, 'libmpdec++/decimal.hh')

mpdecpp_dep = declare_dependency(
  link_with: libmpdecpp,
  include_directories: include_directories('libmpdec++'),
  dependencies: mpdec_dep,
)

if get_option('examples')
  subdir('libmpdec/examples')
  subdir('libmpdec++/examples')
endif

if get_option('tests')
  subdir('tests')
  subdir('tests++')
endif
