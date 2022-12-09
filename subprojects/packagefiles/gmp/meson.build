project(
  'gmp',
  'c',
  version : '6.2.1',
)

add_languages('cpp', required: get_option('cxx'))

if host_machine.cpu_family() != 'x86_64':
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
  add_project_arguments('-fomit-frame-pointer', ['c, cpp'])
endif

if profiling == 'prof':
  add_project_arguments('-p', ['c'])
elif profiling == 'gprof'
  add_project_arguments('-pg', ['c'])
elif profiling == 'instrument'
  add_project_arguments('-finstrument-functions', ['c'])
endif

fake_cpuid = get_option('fake-cpuid')
conf.set('WANT_FAKE_CPUID', fake_cpuid.to_int())

assembly = get_option('assembly')
fat = get_option('fat')

if fat and not assembly
  error('when doing a fat build, disabling assembly will not work')
endif

if fake_cpuid and not fat
  error('enabling fake-cpuid requires enabling fat')
endif

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


mpn_extra_functions = []
if assembly
  mpn_extra_functions += ['invert_limb_table']
endif

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
  conf.set('DEFN_LONG_LONG_LIMB', '#define _LONG_LONG_LIMB 1')
else:
  conf.set('DEFN_LONG_LONG_LIMB', '/* #undef _LONG_LONG_LIMB */')
endif

fat_path = []
fat_functions = []
fat_thresholds = []
if fat
  mpn_search_path = ['x86_64/fat', 'x86_64']
  fat_path = [
    'x86_64',
    'x86_64/fat',
    'x86_64/k8',
    'x86_64/k10',
    'x86_64/bd1',
    'x86_64/bt1',
    'x86_64/bt2',
    'x86_64/zen',
    'x86_64/pentium4',
    'x86_64/core2',
    'x86_64/coreinhm',
    'x86_64/coreisbr',
    'x86_64/coreihwl',
    'x86_64/coreibwl',
    'x86_64/skylake',
    'x86_64/atom',
    'x86_64/silvermont',
    'x86_64/goldmont',
    'x86_64/nano',
  ]
  fat_functions = [
    'add_n',
    'addmul_1',
    'bdiv_dbm1c',
    'com',
    'cnd_add_n',
    'cnd_sub_n',
    'copyd',
    'copyi',
    'dive_1',
    'divrem_1',
    'gcd_11',
    'lshift',
    'lshiftc',
    'mod_1',
    'mod_1_1',
    'mod_1_1_cps',
    'mod_1_2',
    'mod_1_2_cps',
    'mod_1_4',
    'mod_1_4_cps',
    'mod_34lsub1',
    'mode1o',
    'mul_1',
    'mul_basecase',
    'mullo_basecase',
    'pre_divrem_1',
    'pre_mod_1',
    'redc_1',
    'redc_2',
    'rshift',
    'sqr_basecase',
    'sub_n',
    'submul_1',
  ] + [  # 64-bits-specific functions
    'addmul_2',
    'addlsh1_n',
    'addlsh2_n',
    'sublsh1_n'
  ]
  fat_thresholds = [
    'MUL_TOOM22_THRESHOLD',
    'MUL_TOOM33_THRESHOLD',
    'SQR_TOOM2_THRESHOLD',
    'SQR_TOOM3_THRESHOLD',
    'BMOD_1_TO_MOD_1_THRESHOLD',
  ]
endif

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
      '-Wl,--export-all-symbols'
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
  'no_return'
]

foreach a : check_attributes
  if cc.has_function_attribute(a)
    conf.set('HAVE_ATTRIBUTE_' + &.underscorify().to_upper(), 1)
  endif
endforeach

conf.set('HAVE_ATTRIBUTE_MODE', 0)

if cc.compiles(
  '''
  void hid() __attribute__ ((visibility("hidden")));
  void hid() {}
  void pub() __attribute__ ((alias("hid")));
  '''
)
  conf.set('HAVE_HIDDEN_ALIAS', 1)
endif

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
# check token ['HAVE_ATTR_GET']
  ['HAVE_CLOCK', 'clock', '#include<time.h>'],
  ['HAVE_CLOCK_GETTIME', 'clock_gettime', '#include<time.h>'],
# check token ['HAVE_CPUTIME']
# check token ['HAVE_LIMB_BIG_ENDIAN']
# check token ['HAVE_LIMB_LITTLE_ENDIAN']
# check token ['HAVE_LOCALECONV']
# check token ['HAVE_DOUBLE_IEEE_BIG_ENDIAN']
# check token ['HAVE_DOUBLE_IEEE_LITTLE_ENDIAN']
# check token ['HAVE_DOUBLE_IEEE_LITTLE_SWAPPED']
# check token ['HAVE_DOUBLE_VAX_D']
# check token ['HAVE_DOUBLE_VAX_G']
# check token ['HAVE_DOUBLE_CRAY_CFP']
  ['HAVE_GETPAGESIZE', 'getpagesize', '#include<unistd.h>'],
# check token ['HAVE_GETRUSAGE']
# check token ['HAVE_GETSYSINFO']
  ['HAVE_GETTIMEOFDAY', 'gettimeofday', '#include<sys/time.h>'],
# check token ['HAVE_HIDDEN_ALIAS']
# check token ['HAVE_HOST_CPU_FAMILY_alpha']
# check token ['HAVE_HOST_CPU_FAMILY_m68k']
# check token ['HAVE_HOST_CPU_FAMILY_power']
# check token ['HAVE_HOST_CPU_FAMILY_powerpc']
# check token ['HAVE_HOST_CPU_FAMILY_x86']
# check token ['HAVE_HOST_CPU_FAMILY_x86_64']
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
# check token ['HAVE_NL_LANGINFO']
# check token ['HAVE_OBSTACK_VPRINTF']
# check token ['HAVE_POPEN']
# check token ['HAVE_PROCESSOR_INFO']
# check token ['HAVE_PSP_ITICKSPERCLKTICK']
# check token ['HAVE_PSTAT_GETPROCESSOR']
  ['HAVE_RAISE', 'raise', '#include<signal.h>'],
# check token ['HAVE_READ_REAL_TIME']
  ['HAVE_SIGACTION', 'sigaction', '#include<signal.h>'],
  ['HAVE_SIGALTSTACK', 'sigaltstack', '#include<signal.h>'],
# check token ['HAVE_SIGSTACK']
# check token ['HAVE_SSTREAM']
# check token ['HAVE_STACK_T']
# check token ['HAVE_STD__LOCALE']
  ['HAVE_STRCHR', 'strchr', '#include<string.h>'],
  ['HAVE_STRERROR', 'strerror', '#include<string.h>'],
# check token ['HAVE_STRNLEN']
  ['HAVE_STRTOL', 'strtol', '#include<stdlib.h>'],
  ['HAVE_STRTOUL', 'strtoul', '#include<stdlib.h>'],
  ['HAVE_SYSCONF', 'sysconf', '#include<unistd.h>'],
# check token ['HAVE_SYSCTL']
  ['HAVE_SYSCTLBYNAME', 'sysctlbyname', '#include<sys/sysctl.h>'],
# check token ['HAVE_SYSSGI']
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

configure_file(
  input: 'config.h.meson',
  output: 'config.h',
  configuration: conf,
)
