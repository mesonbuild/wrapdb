project(
  'gmp',
  'c',
  version : '6.2.1',
)

cpp = get_option('cxx')
add_languages('cpp', required: cpp)

if host_machine.cpu_family() != 'x86_64'
  error('Unsupported cpu family : ', host_machine.cpu_family())
endif

conf = configuration_data()

conf.set10('WANT_ASSERT', get_option('assert'))
conf.set10('WANT_FFT', get_option('fft'))
conf.set10('WANT_OLD_FFT_FULL', get_option('old-fft-full'))

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
conf.set('HAVE_HOST_CPU_' + host_machine.cpu(), 1)
conf.set('HAVE_HOST_CPU_FAMILY_' + host_machine.cpu_family(), 1)

path_per_cpu = {
  'i786': ['x86_64/pentium4'],
  'pentium4': ['x86_64/pentium4'],
  'athlon64': ['x86_64/k8'],
  'k8': ['x86_64/k8'],
  'x86_64': ['x86_64/k8'],
  'k10': ['x86_64/k10', 'x86_64/k8'],
  'bobcat': ['x86_64/bt1', 'x86_64/k10', 'x86_64/k8'],
  'jaguar': ['x86_64/bt2', 'x86_64/bt1', 'x86_64/k10', 'x86_64/k8'],
  'jaguarnoavx': ['x86_64/bt2', 'x86_64/bt1', 'x86_64/k10', 'x86_64/k8'],
  'bulldozer': ['x86_64/bd1', 'x86_64/k10', 'x86_64/k8'],
  'bd1': ['x86_64/bd1', 'x86_64/k10', 'x86_64/k8'],
  'bulldozernoavx': ['x86_64/bd1', 'x86_64/k10', 'x86_64/k8'],
  'bd1noavx': ['x86_64/bd1', 'x86_64/k10', 'x86_64/k8'],
  'piledriver': ['x86_64/bd2', 'x86_64/bd1', 'x86_64/k10', 'x86_64/k8'],
  'bd2': ['x86_64/bd2', 'x86_64/bd1', 'x86_64/k10', 'x86_64/k8'],
  'piledrivernoavx': ['x86_64/bd2', 'x86_64/bd1', 'x86_64/k10', 'x86_64/k8'],
  'bd2noavx': ['x86_64/bd2', 'x86_64/bd1', 'x86_64/k10', 'x86_64/k8'],
  'steamroller': ['x86_64/bd3', 'x86_64/bd2', 'x86_64/bd1', 'x86_64/k10', 'x86_64/k8'],
  'bd3': ['x86_64/bd3', 'x86_64/bd2', 'x86_64/bd1', 'x86_64/k10', 'x86_64/k8'],
  'steamrollernoavx': ['x86_64/bd3', 'x86_64/bd2', 'x86_64/bd1', 'x86_64/k10', 'x86_64/k8'],
  'bd3noavx': ['x86_64/bd3', 'x86_64/bd2', 'x86_64/bd1', 'x86_64/k10', 'x86_64/k8'],
  'excavator': ['x86_64/bd4', 'x86_64/bd3', 'x86_64/bd2', 'x86_64/bd1', 'x86_64/k10', 'x86_64/k8'],
  'bd4': ['x86_64/bd4', 'x86_64/bd3', 'x86_64/bd2', 'x86_64/bd1', 'x86_64/k10', 'x86_64/k8'],
  'excavatornoavx': ['x86_64/bd4', 'x86_64/bd3', 'x86_64/bd2', 'x86_64/bd1', 'x86_64/k10', 'x86_64/k8'],
  'bd4noavx': ['x86_64/bd4', 'x86_64/bd3', 'x86_64/bd2', 'x86_64/bd1', 'x86_64/k10', 'x86_64/k8'],
  'zen': ['x86_64/zen'],
  'zennoavx': ['x86_64/zen'],
  'zen2': ['x86_64/zen2', 'x86_64/zen'],
  'zen2noavx': ['x86_64/zen2', 'x86_64/zen'],
  'zen3': ['x86_64/zen2', 'x86_64/zen'],
  'zen3noavx': ['x86_64/zen2', 'x86_64/zen'],
  'core2': ['x86_64/core2'],
  'corei': ['x86_64/coreinhm', 'x86_64/core2'],
  'coreinhm': ['x86_64/coreinhm', 'x86_64/core2'],
  'coreiwsm': ['x86_64/coreinhm', 'x86_64/core2'],
  'nehalem': ['x86_64/coreinhm', 'x86_64/core2'],
  'westmere': ['x86_64/coreinhm', 'x86_64/core2'],
  'coreisbr': ['x86_64/coreisbr', 'x86_64/coreinhm', 'x86_64/core2'],
  'coreisbrnoavx': ['x86_64/coreisbr', 'x86_64/coreinhm', 'x86_64/core2'],
  'coreiibr': ['x86_64/coreisbr', 'x86_64/coreinhm', 'x86_64/core2'],
  'coreiibrnoavx': ['x86_64/coreisbr', 'x86_64/coreinhm', 'x86_64/core2'],
  'sandybridge': ['x86_64/coreisbr', 'x86_64/coreinhm', 'x86_64/core2'],
  'sandybridgenoavx': ['x86_64/coreisbr', 'x86_64/coreinhm', 'x86_64/core2'],
  'ivybridge': ['x86_64/coreisbr', 'x86_64/coreinhm', 'x86_64/core2'],
  'ivybridgenoavx': ['x86_64/coreisbr', 'x86_64/coreinhm', 'x86_64/core2'],
  'coreihwl': ['x86_64/coreihwl', 'x86_64/coreisbr', 'x86_64/coreinhm', 'x86_64/core2'],
  'coreihwlnoavx': ['x86_64/coreihwl', 'x86_64/coreisbr', 'x86_64/coreinhm', 'x86_64/core2'],
  'haswell': ['x86_64/coreihwl', 'x86_64/coreisbr', 'x86_64/coreinhm', 'x86_64/core2'],
  'haswellnoavx': ['x86_64/coreihwl', 'x86_64/coreisbr', 'x86_64/coreinhm', 'x86_64/core2'],
  'coreibwl': ['x86_64/coreibwl', 'x86_64/coreihwl', 'x86_64/coreisbr', 'x86_64/coreinhm', 'x86_64/core2'],
  'coreibwlnoavx': ['x86_64/coreibwl', 'x86_64/coreihwl', 'x86_64/coreisbr', 'x86_64/coreinhm', 'x86_64/core2'],
  'broadwell': ['x86_64/coreibwl', 'x86_64/coreihwl', 'x86_64/coreisbr', 'x86_64/coreinhm', 'x86_64/core2'],
  'broadwellnoavx': ['x86_64/coreibwl', 'x86_64/coreihwl', 'x86_64/coreisbr', 'x86_64/coreinhm', 'x86_64/core2'],
  'skylake': ['x86_64/skylake', 'x86_64/coreibwl', 'x86_64/coreihwl', 'x86_64/coreisbr', 'x86_64/coreinhm', 'x86_64/core2'],
  'skylakenoavx': ['x86_64/skylake', 'x86_64/coreibwl', 'x86_64/coreihwl', 'x86_64/coreisbr', 'x86_64/coreinhm', 'x86_64/core2'],
  'kabylake': ['x86_64/skylake', 'x86_64/coreibwl', 'x86_64/coreihwl', 'x86_64/coreisbr', 'x86_64/coreinhm', 'x86_64/core2'],
  'kabylakenoavx': ['x86_64/skylake', 'x86_64/coreibwl', 'x86_64/coreihwl', 'x86_64/coreisbr', 'x86_64/coreinhm', 'x86_64/core2'],
  'atom': ['x86_64/atom'],
  'silvermont': ['x86_64/silvermont', 'x86_64/atom'],
  'goldmont': ['x86_64/goldmont', 'x86_64/silvermont', 'x86_64/atom'],
  'nano': ['x86_64/nano']
}

mpn_search_path = path_per_cpu.get(host_machine.cpu(), []) + ['x86_64']
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

# fat_path = []
# fat_functions = []
# fat_thresholds = []
# if fat
#   mpn_search_path = ['x86_64/fat', 'x86_64']
#   fat_path = [
#     'x86_64',
#     'x86_64/fat',
#     'x86_64/k8',
#     'x86_64/k10',
#     'x86_64/bd1',
#     'x86_64/bt1',
#     'x86_64/bt2',
#     'x86_64/zen',
#     'x86_64/pentium4',
#     'x86_64/core2',
#     'x86_64/coreinhm',
#     'x86_64/coreisbr',
#     'x86_64/coreihwl',
#     'x86_64/coreibwl',
#     'x86_64/skylake',
#     'x86_64/atom',
#     'x86_64/silvermont',
#     'x86_64/goldmont',
#     'x86_64/nano',
#   ]
#   fat_functions = [
#     'add_n',
#     'addmul_1',
#     'bdiv_dbm1c',
#     'com',
#     'cnd_add_n',
#     'cnd_sub_n',
#     'copyd',
#     'copyi',
#     'dive_1',
#     'divrem_1',
#     'gcd_11',
#     'lshift',
#     'lshiftc',
#     'mod_1',
#     'mod_1_1',
#     'mod_1_1_cps',
#     'mod_1_2',
#     'mod_1_2_cps',
#     'mod_1_4',
#     'mod_1_4_cps',
#     'mod_34lsub1',
#     'mode1o',
#     'mul_1',
#     'mul_basecase',
#     'mullo_basecase',
#     'pre_divrem_1',
#     'pre_mod_1',
#     'redc_1',
#     'redc_2',
#     'rshift',
#     'sqr_basecase',
#     'sub_n',
#     'submul_1',
#   ] + [  # 64-bits-specific functions
#     'addmul_2',
#     'addlsh1_n',
#     'addlsh2_n',
#     'sublsh1_n'
#   ]
#   fat_thresholds = [
#     'MUL_TOOM22_THRESHOLD',
#     'MUL_TOOM33_THRESHOLD',
#     'SQR_TOOM2_THRESHOLD',
#     'SQR_TOOM3_THRESHOLD',
#     'BMOD_1_TO_MOD_1_THRESHOLD',
#   ]
# endif

new_path = []
if get_option('nails')
  foreach p : mpn_search_path
    new_path += [p, p+'/nails']
  endforeach
  mpn_search_path = new_path
endif

if not assembly
  mpn_search_path = ['generic']
  conf.set('NO_ASM', 1)
endif

if get_option('default_library') != 'static'
    add_project_link_arguments(
      '-no-undefined',
      '-Wl,--export-all-symbols',
      language: ['c', 'cpp']
    )
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

# check token ['HAVE_ATTRIBUTE_CONST']
# check token ['HAVE_ATTRIBUTE_MALLOC']
# check token ['HAVE_ATTRIBUTE_MODE']
# check token ['HAVE_ATTRIBUTE_NORETURN']

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
  '''
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
# check token ['HAVE_NATIVE_mpn_add_n']
# check token ['HAVE_NATIVE_mpn_add_n_sub_n']
# check token ['HAVE_NATIVE_mpn_add_nc']
# check token ['HAVE_NATIVE_mpn_addaddmul_1msb0']
# check token ['HAVE_NATIVE_mpn_addlsh1_n']
# check token ['HAVE_NATIVE_mpn_addlsh2_n']
# check token ['HAVE_NATIVE_mpn_addlsh_n']
# check token ['HAVE_NATIVE_mpn_addlsh1_nc']
# check token ['HAVE_NATIVE_mpn_addlsh2_nc']
# check token ['HAVE_NATIVE_mpn_addlsh_nc']
# check token ['HAVE_NATIVE_mpn_addlsh1_n_ip1']
# check token ['HAVE_NATIVE_mpn_addlsh2_n_ip1']
# check token ['HAVE_NATIVE_mpn_addlsh_n_ip1']
# check token ['HAVE_NATIVE_mpn_addlsh1_nc_ip1']
# check token ['HAVE_NATIVE_mpn_addlsh2_nc_ip1']
# check token ['HAVE_NATIVE_mpn_addlsh_nc_ip1']
# check token ['HAVE_NATIVE_mpn_addlsh1_n_ip2']
# check token ['HAVE_NATIVE_mpn_addlsh2_n_ip2']
# check token ['HAVE_NATIVE_mpn_addlsh_n_ip2']
# check token ['HAVE_NATIVE_mpn_addlsh1_nc_ip2']
# check token ['HAVE_NATIVE_mpn_addlsh2_nc_ip2']
# check token ['HAVE_NATIVE_mpn_addlsh_nc_ip2']
# check token ['HAVE_NATIVE_mpn_addmul_1c']
# check token ['HAVE_NATIVE_mpn_addmul_2']
# check token ['HAVE_NATIVE_mpn_addmul_3']
# check token ['HAVE_NATIVE_mpn_addmul_4']
# check token ['HAVE_NATIVE_mpn_addmul_5']
# check token ['HAVE_NATIVE_mpn_addmul_6']
# check token ['HAVE_NATIVE_mpn_addmul_7']
# check token ['HAVE_NATIVE_mpn_addmul_8']
# check token ['HAVE_NATIVE_mpn_addmul_2s']
# check token ['HAVE_NATIVE_mpn_and_n']
# check token ['HAVE_NATIVE_mpn_andn_n']
# check token ['HAVE_NATIVE_mpn_bdiv_dbm1c']
# check token ['HAVE_NATIVE_mpn_bdiv_q_1']
# check token ['HAVE_NATIVE_mpn_pi1_bdiv_q_1']
# check token ['HAVE_NATIVE_mpn_cnd_add_n']
# check token ['HAVE_NATIVE_mpn_cnd_sub_n']
# check token ['HAVE_NATIVE_mpn_com']
# check token ['HAVE_NATIVE_mpn_copyd']
# check token ['HAVE_NATIVE_mpn_copyi']
# check token ['HAVE_NATIVE_mpn_div_qr_1n_pi1']
# check token ['HAVE_NATIVE_mpn_div_qr_2']
# check token ['HAVE_NATIVE_mpn_divexact_1']
# check token ['HAVE_NATIVE_mpn_divexact_by3c']
# check token ['HAVE_NATIVE_mpn_divrem_1']
# check token ['HAVE_NATIVE_mpn_divrem_1c']
# check token ['HAVE_NATIVE_mpn_divrem_2']
# check token ['HAVE_NATIVE_mpn_gcd_1']
# check token ['HAVE_NATIVE_mpn_gcd_11']
# check token ['HAVE_NATIVE_mpn_gcd_22']
# check token ['HAVE_NATIVE_mpn_hamdist']
# check token ['HAVE_NATIVE_mpn_invert_limb']
# check token ['HAVE_NATIVE_mpn_ior_n']
# check token ['HAVE_NATIVE_mpn_iorn_n']
# check token ['HAVE_NATIVE_mpn_lshift']
# check token ['HAVE_NATIVE_mpn_lshiftc']
# check token ['HAVE_NATIVE_mpn_lshsub_n']
# check token ['HAVE_NATIVE_mpn_mod_1']
# check token ['HAVE_NATIVE_mpn_mod_1_1p']
# check token ['HAVE_NATIVE_mpn_mod_1c']
# check token ['HAVE_NATIVE_mpn_mod_1s_2p']
# check token ['HAVE_NATIVE_mpn_mod_1s_4p']
# check token ['HAVE_NATIVE_mpn_mod_34lsub1']
# check token ['HAVE_NATIVE_mpn_modexact_1_odd']
# check token ['HAVE_NATIVE_mpn_modexact_1c_odd']
# check token ['HAVE_NATIVE_mpn_mul_1']
# check token ['HAVE_NATIVE_mpn_mul_1c']
# check token ['HAVE_NATIVE_mpn_mul_2']
# check token ['HAVE_NATIVE_mpn_mul_3']
# check token ['HAVE_NATIVE_mpn_mul_4']
# check token ['HAVE_NATIVE_mpn_mul_5']
# check token ['HAVE_NATIVE_mpn_mul_6']
# check token ['HAVE_NATIVE_mpn_mul_basecase']
# check token ['HAVE_NATIVE_mpn_mullo_basecase']
# check token ['HAVE_NATIVE_mpn_nand_n']
# check token ['HAVE_NATIVE_mpn_nior_n']
# check token ['HAVE_NATIVE_mpn_popcount']
# check token ['HAVE_NATIVE_mpn_preinv_divrem_1']
# check token ['HAVE_NATIVE_mpn_preinv_mod_1']
# check token ['HAVE_NATIVE_mpn_redc_1']
# check token ['HAVE_NATIVE_mpn_redc_2']
# check token ['HAVE_NATIVE_mpn_rsblsh1_n']
# check token ['HAVE_NATIVE_mpn_rsblsh2_n']
# check token ['HAVE_NATIVE_mpn_rsblsh_n']
# check token ['HAVE_NATIVE_mpn_rsblsh1_nc']
# check token ['HAVE_NATIVE_mpn_rsblsh2_nc']
# check token ['HAVE_NATIVE_mpn_rsblsh_nc']
# check token ['HAVE_NATIVE_mpn_rsh1add_n']
# check token ['HAVE_NATIVE_mpn_rsh1add_nc']
# check token ['HAVE_NATIVE_mpn_rsh1sub_n']
# check token ['HAVE_NATIVE_mpn_rsh1sub_nc']
# check token ['HAVE_NATIVE_mpn_rshift']
# check token ['HAVE_NATIVE_mpn_sbpi1_bdiv_r']
# check token ['HAVE_NATIVE_mpn_sqr_basecase']
# check token ['HAVE_NATIVE_mpn_sqr_diagonal']
# check token ['HAVE_NATIVE_mpn_sqr_diag_addlsh1']
# check token ['HAVE_NATIVE_mpn_sub_n']
# check token ['HAVE_NATIVE_mpn_sub_nc']
# check token ['HAVE_NATIVE_mpn_sublsh1_n']
# check token ['HAVE_NATIVE_mpn_sublsh2_n']
# check token ['HAVE_NATIVE_mpn_sublsh_n']
# check token ['HAVE_NATIVE_mpn_sublsh1_nc']
# check token ['HAVE_NATIVE_mpn_sublsh2_nc']
# check token ['HAVE_NATIVE_mpn_sublsh_nc']
# check token ['HAVE_NATIVE_mpn_sublsh1_n_ip1']
# check token ['HAVE_NATIVE_mpn_sublsh2_n_ip1']
# check token ['HAVE_NATIVE_mpn_sublsh_n_ip1']
# check token ['HAVE_NATIVE_mpn_sublsh1_nc_ip1']
# check token ['HAVE_NATIVE_mpn_sublsh2_nc_ip1']
# check token ['HAVE_NATIVE_mpn_sublsh_nc_ip1']
# check token ['HAVE_NATIVE_mpn_submul_1c']
# check token ['HAVE_NATIVE_mpn_tabselect']
# check token ['HAVE_NATIVE_mpn_udiv_qrnnd']
# check token ['HAVE_NATIVE_mpn_udiv_qrnnd_r']
# check token ['HAVE_NATIVE_mpn_umul_ppmm']
# check token ['HAVE_NATIVE_mpn_umul_ppmm_r']
# check token ['HAVE_NATIVE_mpn_xor_n']
# check token ['HAVE_NATIVE_mpn_xnor_n']
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

conf.set('SIZEOF_MP_LIMB_T', cc.sizeof('mp limb t'))
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

mpn_functions_optional = [
  'umul',
  'udiv',
  'invert_limb',
  'sqr_diagonal',
  'sqr_diag_addlsh1',
  'mul_2',
  'mul_3',
  'mul_4',
  'mul_5',
  'mul_6',
  'addmul_2',
  'addmul_3',
  'addmul_4',
  'addmul_5',
  'addmul_6',
  'addmul_7',
  'addmul_8',
  'addlsh1_n',
  'sublsh1_n',
  'rsblsh1_n',
  'rsh1add_n',
  'rsh1sub_n',
  'addlsh2_n',
  'sublsh2_n',
  'rsblsh2_n',
  'addlsh_n',
  'sublsh_n',
  'rsblsh_n',
  'add_n_sub_n',
  'addaddmul_1msb0',
]

mpn_extra_functions = []
if assembly
  mpn_extra_functions += ['invert_limb_table']
endif

mpn_functions = mpn_extra_functions + mpn_functions_optional + [
  'add',
  'add_1',
  'add_n',
  'sub',
  'sub_1',
  'sub_n',
  'cnd_add_n',
  'cnd_sub_n',
  'cnd_swap',
  'neg',
  'com',
  'mul_1',
  'addmul_1',
  'submul_1',
  'add_err1_n',
  'add_err2_n',
  'add_err3_n',
  'sub_err1_n',
  'sub_err2_n',
  'sub_err3_n',
  'lshift',
  'rshift',
  'dive_1',
  'diveby3',
  'divis',
  'divrem',
  'divrem_1',
  'divrem_2',
  'fib2_ui',
  'fib2m',
  'mod_1',
  'mod_34lsub1',
  'mode1o',
  'pre_divrem_1',
  'pre_mod_1',
  'dump',
  'mod_1_1',
  'mod_1_2',
  'mod_1_3',
  'mod_1_4',
  'lshiftc',
  'mul',
  'mul_fft',
  'mul_n',
  'sqr',
  'mul_basecase',
  'sqr_basecase',
  'nussbaumer_mul',
  'mulmid_basecase',
  'toom42_mulmid',
  'mulmid_n',
  'mulmid',
  'random',
  'random2',
  'pow_1',
  'rootrem',
  'sqrtrem',
  'sizeinbase',
  'get_str',
  'set_str',
  'compute_powtab',
  'scan0',
  'scan1',
  'popcount',
  'hamdist',
  'cmp',
  'zero_p',
  'perfsqr',
  'perfpow',
  'strongfibo',
  'gcd_11',
  'gcd_22',
  'gcd_1',
  'gcd',
  'gcdext_1',
  'gcdext',
  'gcd_subdiv_step',
  'gcdext_lehmer',
  'div_q',
  'tdiv_qr',
  'jacbase',
  'jacobi_2',
  'jacobi',
  'get_d',
  'matrix22_mul',
  'matrix22_mul1_inverse_vector',
  'hgcd_matrix',
  'hgcd2',
  'hgcd_step',
  'hgcd_reduce',
  'hgcd',
  'hgcd_appr',
  'hgcd2_jacobi',
  'hgcd_jacobi',
  'mullo_n',
  'mullo_basecase',
  'sqrlo',
  'sqrlo_basecase',
  'toom22_mul',
  'toom32_mul',
  'toom42_mul',
  'toom52_mul',
  'toom62_mul',
  'toom33_mul',
  'toom43_mul',
  'toom53_mul',
  'toom54_mul',
  'toom63_mul',
  'toom44_mul',
  'toom6h_mul',
  'toom6_sqr',
  'toom8h_mul',
  'toom8_sqr',
  'toom_couple_handling',
  'toom2_sqr',
  'toom3_sqr',
  'toom4_sqr',
  'toom_eval_dgr3_pm1',
  'toom_eval_dgr3_pm2',
  'toom_eval_pm1',
  'toom_eval_pm2',
  'toom_eval_pm2exp',
  'toom_eval_pm2rexp',
  'toom_interpolate_5pts',
  'toom_interpolate_6pts',
  'toom_interpolate_7pts',
  'toom_interpolate_8pts',
  'toom_interpolate_12pts',
  'toom_interpolate_16pts',
  'invertappr',
  'invert',
  'binvert',
  'mulmod_bnm1',
  'sqrmod_bnm1',
  'div_qr_1',
  'div_qr_1n_pi1',
  'div_qr_2',
  'div_qr_2n_pi1',
  'div_qr_2u_pi1',
  'sbpi1_div_q',
  'sbpi1_div_qr',
  'sbpi1_divappr_q',
  'dcpi1_div_q',
  'dcpi1_div_qr',
  'dcpi1_divappr_q',
  'mu_div_qr',
  'mu_divappr_q',
  'mu_div_q',
  'bdiv_q_1',
  'sbpi1_bdiv_q',
  'sbpi1_bdiv_qr',
  'sbpi1_bdiv_r',
  'dcpi1_bdiv_q',
  'dcpi1_bdiv_qr',
  'mu_bdiv_q',
  'mu_bdiv_qr',
  'bdiv_q',
  'bdiv_qr',
  'broot',
  'brootinv',
  'bsqrt',
  'bsqrtinv',
  'divexact',
  'bdiv_dbm1c',
  'redc_1',
  'redc_2',
  'redc_n',
  'powm',
  'powlo',
  'sec_powm',
  'sec_mul',
  'sec_sqr',
  'sec_div_qr',
  'sec_div_r',
  'sec_pi1_div_qr',
  'sec_pi1_div_r',
  'sec_add_1',
  'sec_sub_1',
  'sec_invert',
  'trialdiv',
  'remove',
  'and_n',
  'andn_n',
  'nand_n',
  'ior_n',
  'iorn_n',
  'nior_n',
  'xor_n',
  'xnor_n',
  'copyi',
  'copyd',
  'zero',
  'sec_tabselect',
  'comb_tables',
]

# functions that can be provided by multi-function file
multi_function_files = {
  'add_n': ['aors_n'],
  'sub_n': ['aors_n'],
  'add_err1_n': ['aors_err1_n'],
  'sub_err1_n': ['aors_err1_n'],
  'add_err2_n': ['aors_err2_n'],
  'sub_err2_n': ['aors_err2_n'],
  'add_err3_n': ['aors_err3_n'],
  'sub_err3_n': ['aors_err3_n'],
  'cnd_add_n': ['cnd_aors_n'],
  'cnd_sub_n': ['cnd_aors_n'],
  'sec_add_1': ['sec_aors_1'],
  'sec_sub_1': ['sec_aors_1'],
  'addmul_1': ['aorsmul_1'],
  'submul_1': ['aorsmul_1'],
  'mul_2': ['aormul_2'],
  'addmul_2': ['aormul_2'],
  'mul_3': ['aormul_3'],
  'addmul_3': ['aormul_3'],
  'mul_4': ['aormul_4'],
  'addmul_4': ['aormul_4'],
  'popcount': ['popham'],
  'hamdist': ['popham'],
  'and_n': ['logops_n'],
  'andn_n': ['logops_n'],
  'nand_n': ['logops_n'],
  'ior_n': ['logops_n'],
  'iorn_n': ['logops_n'],
  'nior_n': ['logops_n'],
  'xor_n': ['logops_n'],
  'xnor_n': ['logops_n'],
  'lshift': ['lorrshift'],
  'rshift': ['lorrshift'],
  'addlsh1_n': ['aorslsh1_n', 'aorrlsh1_n', 'aorsorrlsh1_n'],
  'sublsh1_n': ['aorslsh1_n', 'sorrlsh1_n', 'aorsorrlsh1_n'],
  'rsblsh1_n': ['aorrlsh1_n', 'sorrlsh1_n', 'aorsorrlsh1_n'],
  'addlsh2_n': ['aorslsh2_n', 'aorrlsh2_n', 'aorsorrlsh2_n'],
  'sublsh2_n': ['aorslsh2_n', 'sorrlsh2_n', 'aorsorrlsh2_n'],
  'rsblsh2_n': ['aorrlsh2_n', 'sorrlsh2_n', 'aorsorrlsh2_n'],
  'addlsh_n': ['aorslsh_n', 'aorrlsh_n', 'aorsorrlsh_n'],
  'sublsh_n': ['aorslsh_n', 'sorrlsh_n', 'aorsorrlsh_n'],
  'rsblsh_n': ['aorrlsh_n', 'sorrlsh_n', 'aorsorrlsh_n'],
  'rsh1add_n': ['rsh1aors_n'],
  'rsh1sub_n': ['rsh1aors_n'],
  'sec_div_qr': ['sec_div'],
  'sec_div_r': ['sec_div'],
  'sec_pi1_div_qr': ['sec_pi1_div'],
  'sec_pi1_div_r': ['sec_pi1_div'],
}

# the list of all object files used by mpn/Makefile.in and the
# top-level Makefile.in, respectively
mpn_objects = []
mpn_objs_in_libgmp = []

# links from the sources, to be removed by "make distclean"
gmp_srclinks = []

configure_file(
  input: 'config.h.meson',
  output: 'config.h',
  configuration: conf,
)
