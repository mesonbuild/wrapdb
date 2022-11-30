project(
  'gmp',
  'c',
  'cpp',
  version : '6.2.1',
)

conf = configuration_data()

conf.set('WANT_ASSERT', get_option('assert').to_int())
conf.set('WANT_FFT', get_option('fft').to_int())
conf.set('WANT_OLD_FFT_FULL', get_option('old-fft-full').to_int())

profiling = get_option('profiling')
if profiling != 'no'
  conf.set('WANT_PROFILING_' + profiling.to_upper(), 1)
endif
fomit_frame_pointer = []
if profiling == 'gprof':
  fomit_frame_pointer += ['-fomit-frame-pointer']
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

abi_list = ['standard']
cc_list = ['gcc', 'cc']
gcc_cflags = ['-O2', '-pedantic']
gcc_64_cflags = ['-O2', '-pedantic']
cc_cflags = ['-O']
cc_64_cflags = ['-O']
SPEED_CYCLECOUNTER_OBJ = []
cyclecounter_size = 2
mpn_search_path = []

conf.set('HAVE_HOST_CPU_FAMILY_power', 0)
conf.set('HAVE_HOST_CPU_FAMILY_powerpc', 0)

variables = {
  'alpha': {
    'mpn_search_path': []
  }
}


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
  'nl/types.h',
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

cc = meson.get_compiler('c')

foreach h : check_headers
  if cc.has_header(h)
    conf.set('HAVE_' + h.underscorify().to_upper(), 1)
  endif
endforeach

check_functions = [
  ['HAVE_ALARM', 'alarm', '#include<unistd.h>'],
  ['HAVE_ALLOCA', 'alloca', '#include<alloca.h>'],
# check token ['HAVE_ATTRIBUTE_CONST']
# check token ['HAVE_ATTRIBUTE_MALLOC']
# check token ['HAVE_ATTRIBUTE_MODE']
# check token ['HAVE_ATTRIBUTE_NORETURN']
# check token ['HAVE_ATTR_GET']
# check token ['HAVE_CALLING_CONVENTIONS']
  ['HAVE_CLOCK', 'clock', '#include<time.h>'],
  ['HAVE_CLOCK_GETTIME', 'clock_gettime', '#include<time.h>'],
# check token ['HAVE_CPUTIME']
# check token ['HAVE_DECL_FGETC']
# check token ['HAVE_DECL_FSCANF']
# check token ['HAVE_DECL_OPTARG']
# check token ['HAVE_DECL_SYS_ERRLIST']
# check token ['HAVE_DECL_SYS_NERR']
# check token ['HAVE_DECL_UNGETC']
# check token ['HAVE_DECL_VFPRINTF']
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
# check token ['HAVE_INTMAX_T']
# check token ['HAVE_INTPTR_T']
# check token ['HAVE_LIMB_BIG_ENDIAN']
# check token ['HAVE_LIMB_LITTLE_ENDIAN']
# check token ['HAVE_LOCALECONV']
# check token ['HAVE_LONG_DOUBLE']
# check token ['HAVE_LONG_LONG']
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
# check token ['HAVE_PTRDIFF_T']
# check token ['HAVE_QUAD_T']
  ['HAVE_RAISE', 'raise', '#include<signal.h>'],
# check token ['HAVE_READ_REAL_TIME']
  ['HAVE_SIGACTION', 'sigaction', '#include<signal.h>'],
  ['HAVE_SIGALTSTACK', 'sigaltstack', '#include<signal.h>'],
# check token ['HAVE_SIGSTACK']
# check token ['HAVE_SPEED_CYCLECOUNTER']
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
# check token ['HAVE_UINT_LEAST32_T']
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
