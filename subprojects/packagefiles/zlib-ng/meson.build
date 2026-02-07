project(
  'zlib-ng',
  'c',
  version: run_command(
    'get-version.py',
    'zlib-ng',
    capture: true,
    check: true,
  ).stdout().strip(),
  license: 'Zlib',
  meson_version: '>=0.63.0',
  default_options: ['c_std=c11'],
)

if get_option('b_lto')
  error('LTO cannot be used with runtime CPU detection')
endif

compile_args = ['-DWITH_OPTIM']
link_args = []
pkg_config_cflags = []
arch_libs = []

sym_prefix = {
  'ZLIB_SYMBOL_PREFIX': '',
}
general_section = 'General features'
arch_section = 'Architecture-specific features'

with_zlib_compat = get_option('zlib-compat')
if with_zlib_compat
  compile_args += '-DZLIB_COMPAT'
  suffix = ''
  def_suffix = 'compat'
  lib_version = run_command(
    'get-version.py',
    'zlib',
    capture: true,
    check: true,
  ).stdout().strip()
  pkg_version = lib_version + '.zlib-ng'
else
  suffix = '-ng'
  def_suffix = suffix
  lib_version = meson.project_version()
  pkg_version = lib_version
endif
summary(
  'Library version',
  pkg_version,
  section: general_section,
)
summary(
  'zlib compatibility',
  with_zlib_compat,
  section: general_section,
  bool_yn: true,
)

cc = meson.get_compiler('c')

configure_file(
  input: 'zlib@0@.map.in'.format(suffix),
  output: 'zlib@0@.map'.format(suffix),
  configuration: sym_prefix,
)
link_args += cc.get_supported_link_arguments(
  '-Wl,--version-script,@0@/zlib@1@.map'.format(
    meson.current_build_dir(),
    suffix,
  ),
  # force-disable LTO at link time in case -flto was passed manually
  '-fno-lto',
)

largefile_args = ['-D_LARGEFILE64_SOURCE=1', '-D__USE_LARGEFILE64']
foreach type : ['off64_t', '_off64_t']
  if cc.has_type(
    type,
    args: largefile_args,
    prefix: '#include <sys/types.h>',
  )
    compile_args += largefile_args
    break
  endif
endforeach

foreach h : ['linux/auxvec.h', 'sys/auxv.h', 'sys/sdt.h', 'arm_acle.h']
  found = cc.has_header(h)
  set_variable('have_' + h.underscorify(), found)
  if found
    compile_args += '-DHAVE_' + h.to_upper().underscorify()
  endif
endforeach

foreach f : [
  ['__builtin_assume_aligned', ['-DHAVE_BUILTIN_ASSUME_ALIGNED'], []],
  ['__builtin_ctz', ['-DHAVE_BUILTIN_CTZ'], []],
  ['__builtin_ctzll', ['-DHAVE_BUILTIN_CTZLL'], []],
  ['fseeko', [], ['-DNO_FSEEKO']],
  ['strerror', [], ['-DNO_STRERROR']],
]
  res = cc.has_function(f[0])
  set_variable('have_' + f[0], res)
  if res
    compile_args += f[1]
  else
    compile_args += f[2]
  endif
endforeach

foreach attr : [
  ['aligned', '-DHAVE_ATTRIBUTE_ALIGNED'],
  ['visibility:hidden', '-DHAVE_VISIBILITY_HIDDEN'],
  ['visibility:internal', '-DHAVE_VISIBILITY_INTERNAL'],
]
  if cc.has_function_attribute(attr[0])
    compile_args += attr[1]
  endif
endforeach

foreach opt : [
  ['inflate-strict', 'Inflate strict distance checking', ['-DINFLATE_STRICT']],
  [
    'inflate-allow-invalid-dist',
    'Zero fill for inflate invalid distances',
    ['-DINFLATE_ALLOW_INVALID_DISTANCE_TOOFAR_ARRR'],
  ],
]
  enable = get_option(opt[0])
  if enable
    compile_args += opt[2]
  endif
  summary(
    opt[1],
    enable,
    section: general_section,
    bool_yn: true,
  )
endforeach

src = [
  'arch/generic/adler32_c.c',
  'arch/generic/adler32_fold_c.c',
  'arch/generic/crc32_braid_c.c',
  'arch/generic/crc32_fold_c.c',
  'adler32.c',
  'compress.c',
  'cpu_features.c',
  'crc32.c',
  'crc32_braid_comb.c',
  'deflate.c',
  'deflate_fast.c',
  'deflate_huff.c',
  'deflate_medium.c',
  'deflate_quick.c',
  'deflate_rle.c',
  'deflate_slow.c',
  'deflate_stored.c',
  'functable.c',
  'infback.c',
  'inflate.c',
  'inftrees.c',
  'insert_string.c',
  'insert_string_roll.c',
  'trees.c',
  'uncompr.c',
  'zutil.c',
]

includedir = get_option('includedir')

zconf_cmd = ['process-zconf.py', '@INPUT0@']
if cc.has_header('unistd.h')
  zconf_cmd += '--have-unistd'
endif
if not cc.has_type(
  'ptrdiff_t',
  prefix: '#include <stddef.h>',
)
  zconf_cmd += ['--ptrdiff-type', 'uint@0@_t'.format(8 * cc.sizeof('void *'))]
endif
configure_file(
  command: zconf_cmd,
  input: 'zconf@0@.h.in'.format(suffix),
  output: 'zconf@0@.h'.format(suffix),
  capture: true,
  install: true,
  install_dir: includedir,
  # for meson < 0.64
  install_tag: 'devel',
)

configure_file(
  input: 'zlib@0@.h.in'.format(suffix),
  output: 'zlib@0@.h'.format(suffix),
  configuration: sym_prefix,
  install: true,
  install_dir: includedir,
  # for meson < 0.64
  install_tag: 'devel',
)

configure_file(
  input: 'zlib_name_mangling.h.empty',
  output: 'zlib_name_mangling@0@.h'.format(suffix),
  copy: true,
  install: true,
  install_dir: includedir,
  # for meson < 0.64
  install_tag: 'devel',
)

with_gzfileop = get_option('gzfileop') or get_option('zlib-compat')
if with_gzfileop
  compile_args += '-DWITH_GZFILEOP'
  pkg_config_cflags += '-DWITH_GZFILEOP'
  configure_file(
    input: 'gzread_mangle.h.in',
    output: 'gzread_mangle.h',
    configuration: sym_prefix,
  )
  src += ['gzlib.c', 'gzread.c', 'gzwrite.c']
endif
summary(
  'gzFile functions',
  with_gzfileop,
  section: general_section,
  bool_yn: true,
)

with_chorba = get_option('crc32-chorba')
if with_chorba
  src += 'arch/generic/crc32_chorba_c.c'
else
  compile_args += '-DWITHOUT_CHORBA'
endif
summary(
  'Chorba optimized CRC32',
  with_chorba,
  section: general_section,
  bool_yn: true,
)

cpu_family = host_machine.cpu_family()
system = host_machine.system()
cc_id = cc.get_id()
cc_syntax = cc.get_argument_syntax()

if system == 'windows'
  src += import('windows').compile_resources(
    'win32/zlib@0@1.rc'.format(suffix),
    include_directories: include_directories('.'),
  )

  compile_args += ['-D_CRT_SECURE_NO_DEPRECATE', '-D_CRT_NONSTDC_NO_DEPRECATE']
  if get_option('default_library') != 'static'
    compile_args += '-DZLIB_DLL'
  endif
endif

def = configure_file(
  input: 'win32/zlib@0@.def.in'.format(def_suffix),
  output: 'zlib.def',
  configuration: sym_prefix,
)

if cpu_family == 'x86_64' and get_option('sse2').allowed()
  if not have___builtin_ctz
    src += 'arch/generic/compare256_c.c'
  endif
else
  src += [
    'arch/generic/chunkset_c.c',
    'arch/generic/compare256_c.c',
    'arch/generic/slide_hash_c.c',
  ]
  compile_args += '-DWITH_ALL_FALLBACKS'
endif

if cpu_family in ['arm', 'aarch64']
  summary(
    'Architecture',
    'ARM',
    section: arch_section,
  )
  archdir = 'arch/arm'
  compile_args += '-DARM_FEATURES'
  src += archdir / 'arm_features.c'

  if system == 'linux'
    found_crc = false
    found_neon = false
    if cpu_family == 'aarch64'
      auxtests = [
        [
          'crc',
          ['sys/auxv.h'],
          'AT_HWCAP',
          'HWCAP_CRC32',
          '-DARM_AUXV_HAS_CRC32',
        ],
      ]
    else
      auxtests = [
        [
          'crc',
          ['sys/auxv.h'],
          'AT_HWCAP2',
          'HWCAP2_CRC32',
          '-DARM_AUXV_HAS_CRC32',
        ],
        [
          'crc',
          ['sys/auxv.h', 'asm/hwcap.h'],
          'AT_HWCAP2',
          'HWCAP2_CRC32',
          ['-DARM_AUXV_HAS_CRC32', '-DARM_ASM_HWCAP'],
        ],
        [
          'neon',
          ['sys/auxv.h'],
          'AT_HWCAP',
          'HWCAP_ARM_NEON',
          '-DARM_AUXV_HAS_NEON',
        ],
        [
          'neon',
          ['sys/auxv.h'],
          'AT_HWCAP',
          'HWCAP_NEON',
          '-DARM_AUXV_HAS_NEON',
        ],
      ]
    endif
    foreach auxtest : auxtests
      if get_variable('found_' + auxtest[0])
        continue
      endif
      testprog = ''
      foreach include : auxtest[1]
        testprog += '#include <@0@>\n'.format(include)
      endforeach
      testprog += 'int main() {return (getauxval(@0@) & @1@);}'.format(
        auxtest[2],
        auxtest[3],
      )
      if cc.compiles(
        testprog,
        name: '@0@ and @1@ in @2@'.format(
          auxtest[2],
          auxtest[3],
          ', '.join(auxtest[1]),
        ),
      )
        compile_args += auxtest[4]
        set_variable('found_' + auxtest[0], true)
      endif
    endforeach
    if not found_crc
      message('Cannot detect hardware CRC32 support with getauxval()')
    endif
    if cpu_family == 'arm' and not found_neon
      message('Cannot detect NEON support with getauxval()')
    endif
  endif
  if cc_id == 'msvc'
    compile_args += '-D_ARM_WINAPI_PARTITION_DESKTOP_SDK_AVAILABLE'
  endif

  armv8flags = []
  foreach arg : [
    '-march=armv8-a+crc',
    '-march=armv8-a+crc+simd',
    '-Wa,-march=armv8-a+crc',
    '-Wa,-march=armv8-a+crc+simd',
  ]
    if cc.has_argument(arg)
      armv8flags = [arg]
      break
    endif
  endforeach
  want_armv8 = get_option('armv8')
  have_armv8_asm = want_armv8.allowed() and cc.compiles(
    '''unsigned int f(unsigned int a, unsigned int b) {
        unsigned int c;
    #ifdef __aarch64__
        __asm__( "crc32w %w0, %w1, %w2" : "=r" (c) : "r" (a), "r" (b));
    #else
        __asm__( "crc32w %0, %1, %2" : "=r" (c) : "r" (a), "r" (b));
    #endif
        return (int)c;
    }
    int main(void) { return f(1,2); }''',
    name: 'ARMv8 inline asm',
    args: armv8flags,
  )
  have_armv8_intrin = want_armv8.allowed() and cc.compiles(
    '''#if defined(_MSC_VER)
    #include <intrin.h>
    #else
    #include <arm_acle.h>
    #endif
    unsigned int f(unsigned int a, unsigned int b) {
        return __crc32w(a, b);
    }
    int main(void) { return 0; }''',
    name: 'ARMv8 intrinsics',
    args: armv8flags,
  )
  have_armv8 = have_armv8_asm or have_armv8_intrin
  if have_armv8
    compile_args += '-DARM_CRC32'
    if have_armv8_intrin
      compile_args += '-DARM_CRC32_INTRIN'
    endif
    arch_libs += static_library(
      'armv8',
      archdir / 'crc32_armv8.c',
      c_args: compile_args + armv8flags,
      link_args: link_args,
    )
  endif
  want_armv8.require(have_armv8)
  summary(
    'ARMv8 optimized CRC',
    have_armv8,
    section: arch_section,
    bool_yn: true,
  )

  neonflags = []
  if cc_id == 'msvc'
    if cpu_family == 'arm'
      neonflags = ['/arch:VFPv4']
    endif
  else
    if cpu_family == 'aarch64'
      neonflags = ['-march=armv8-a+simd']
    else
      neonflags = ['-mfpu=neon']
    endif
  endif
  want_neon = get_option('neon')
  # avoid Alpine armv7 CI failure: https://github.com/zlib-ng/zlib-ng/issues/1844
  have_neon = want_neon.allowed() and not (
    cc_id == 'clang'
    and cpu_family == 'arm'
  ) and cc.compiles(
    '''#if defined(_M_ARM64) || defined(_M_ARM64EC)
    #  include <arm64_neon.h>
    #else
    #  include <arm_neon.h>
    #endif
    int main() { return 0; }''',
    name: 'NEON flag',
    args: neonflags,
  )
  if have_neon
    compile_args += '-DARM_NEON'
    if cc_id == 'msvc'
      compile_args += '-D__ARM_NEON__'
    endif
    if cc.compiles(
      '''#if defined(_MSC_VER) && (defined(_M_ARM64) || defined(_M_ARM64EC))
      #  include <arm64_neon.h>
      #else
      #  include <arm_neon.h>
      #endif
      int32x4x4_t f(int var[16]) { return vld1q_s32_x4(var); }
      int main(void) { return 0; }''',
      name: 'load 4 NEON vecs into a register range',
      args: neonflags,
    )
      compile_args += '-DARM_NEON_HASLD4'
    endif
    arch_libs += static_library(
      'neon',
      archdir / 'adler32_neon.c',
      archdir / 'chunkset_neon.c',
      archdir / 'compare256_neon.c',
      archdir / 'slide_hash_neon.c',
      c_args: compile_args + neonflags,
      link_args: link_args,
    )
  endif
  want_neon.require(have_neon)
  summary(
    'NEON',
    have_neon,
    section: arch_section,
    bool_yn: true,
  )

  if cpu_family == 'arm'
    # Upstream explicitly sets -march=armv6 or -Wa,-march=armv6, but this
    # also requires -mfloat-abi=soft since armv6 doesn't require an FPU.
    # Upstream deals with this by defaulting the entire library to
    # soft-float on 32-bit ARM, overriding the compiler's default.  Since
    # armv6 is probably not newer than the actual target arch, we instead
    # skip setting arch flags at all.
    have_armv6_asm = cc.compiles(
      '''unsigned int f(unsigned int a, unsigned int b) {
          unsigned int c;
          __asm__ ( "uqsub16 %0, %1, %2" : "=r" (c) : "r" (a), "r" (b) );
          return (int)c;
      }
      int main(void) { return f(1,2); }''',
      name: 'ARMv6 inline asm',
    )
    have_armv6_intrin = cc.compiles(
      '''#if defined(_MSC_VER)
      #include <intrin.h>
      #else
      #include <arm_acle.h>
      #endif
      unsigned int f(unsigned int a, unsigned int b) {
      #if defined(_MSC_VER)
          return _arm_uqsub16(a, b);
      #else
          return __uqsub16(a, b);
      #endif
      }
      int main(void) { return f(1,2); }''',
      name: 'ARMv6 intrinsics',
    )
    want_armv6 = get_option('armv6')
    have_armv6 = want_armv6.allowed() and (have_armv6_asm or have_armv6_intrin)
    if have_armv6
      compile_args += '-DARM_SIMD'
      if have_armv6_intrin
        compile_args += '-DARM_SIMD_INTRIN'
      endif
      src += archdir / 'slide_hash_armv6.c'
    endif
    want_armv6.require(have_armv6)
    summary(
      'ARMv6',
      have_armv6,
      section: arch_section,
      bool_yn: true,
    )
  endif

elif cpu_family == 'loongarch64'
  summary(
    'Architecture',
    'LoongArch',
    section: arch_section,
  )
  archdir = 'arch/loongarch'
  src += archdir / 'loongarch_features.c'
  compile_args += '-DLOONGARCH_FEATURES'

  want_la64crc = get_option('crc32-la')
  have_la64crc = want_la64crc.allowed() and cc.compiles(
    '''#include <larchintrin.h>
    int main(void) {
        char ch = 'a';
        int crc = __crc_w_b_w(ch, 0);
        return crc;
    }''',
    name: 'vectorized CRC32',
  )
  if have_la64crc
    src += archdir / 'crc32_la.c'
    compile_args += '-DLOONGARCH_CRC'
  endif
  want_la64crc.require(have_la64crc)
  summary(
    'vectorized CRC32',
    have_la64crc,
    section: arch_section,
    bool_yn: true,
  )

  lsxflags = ['-mlsx']
  want_lsx = get_option('lsx')
  have_lsx = want_lsx.allowed() and cc.compiles(
    '''#include <lsxintrin.h>
    __m128i f(__m128i a, __m128i b) {
        return __lsx_vabsd_b(a, b);
    }
    int main(void) { return 0; }''',
    name: 'vectorized LSX',
    args: lsxflags,
  )
  if have_lsx
    compile_args += '-DLOONGARCH_LSX'
    arch_libs += static_library(
      'lsx',
      archdir / 'adler32_lsx.c',
      archdir / 'chunkset_lsx.c',
      archdir / 'compare256_lsx.c',
      archdir / 'slide_hash_lsx.c',
      c_args: compile_args + lsxflags,
      link_args: link_args,
    )
  endif
  want_lsx.require(have_lsx)
  summary(
    'vectorized LSX',
    have_lsx,
    section: arch_section,
    bool_yn: true,
  )

  lasxflags = ['-mlasx']
  want_lasx = get_option('lasx')
  have_lasx = want_lasx.allowed() and have_lsx and cc.compiles(
    '''#include <lasxintrin.h>
    __m256i f(__m256i a, __m256i b) {
        return __lasx_xvabsd_b(a, b);
    }
    int main(void) { return 0; }''',
    name: 'vectorized LASX',
    args: lasxflags,
  )
  if have_lasx
    compile_args += '-DLOONGARCH_LASX'
    arch_libs += static_library(
      'lasx',
      archdir / 'adler32_lasx.c',
      archdir / 'chunkset_lasx.c',
      archdir / 'compare256_lasx.c',
      archdir / 'slide_hash_lasx.c',
      c_args: compile_args + lasxflags,
      link_args: link_args,
    )
  endif
  want_lasx.require(have_lasx)
  summary(
    'vectorized LASX',
    have_lasx,
    section: arch_section,
    bool_yn: true,
  )

elif cpu_family in ['ppc', 'ppc64']
  summary(
    'Architecture',
    'Power',
    section: arch_section,
  )
  archdir = 'arch/power'
  src += archdir / 'power_features.c'

  altivecflags = []
  want_altivec = get_option('altivec')
  foreach flag : ['-maltivec', '-mno-vsx']
    if want_altivec.allowed() and cc.compiles(
      '''#include <altivec.h>
      int main(void)
      {
          vector int a = vec_splats(0);
          vector int b = vec_splats(0);
          a = vec_add(a, b);
          return 0;
      }''',
      name: 'AltiVec with @0@'.format(flag),
      args: altivecflags + flag,
    )
      altivecflags += flag
    endif
  endforeach
  have_altivec = altivecflags.contains('-maltivec') and cc.compiles(
    '''#include <sys/auxv.h>
    #ifdef __FreeBSD__
    #include <machine/cpu.h>
    #endif
    int main() {
    #if defined(__FreeBSD__) || defined(__OpenBSD__)
        unsigned long hwcap;
        elf_aux_info(AT_HWCAP, &hwcap, sizeof(hwcap));
        return (hwcap & PPC_FEATURE_HAS_ALTIVEC);
    #else
        return (getauxval(AT_HWCAP) & PPC_FEATURE_HAS_ALTIVEC);
    #endif
    }''',
    name: 'AltiVec',
    args: altivecflags,
  )
  if have_altivec
    compile_args += ['-DPPC_FEATURES', '-DPPC_VMX']
    arch_libs += static_library(
      'altivec',
      archdir / 'adler32_vmx.c',
      archdir / 'slide_hash_vmx.c',
      c_args: compile_args + altivecflags,
      link_args: link_args,
    )
  endif
  want_altivec.require(have_altivec)
  summary(
    'AltiVec',
    have_altivec,
    section: arch_section,
    bool_yn: true,
  )

  power8flags = ['-mcpu=power8']
  want_power8 = get_option('power8')
  have_power8 = want_power8.allowed() and cc.compiles(
    '''#include <sys/auxv.h>
    #ifdef __FreeBSD__
    #include <machine/cpu.h>
    #endif
    int main() {
    #if defined(__FreeBSD__) || defined(__OpenBSD__)
        unsigned long hwcap;
        elf_aux_info(AT_HWCAP2, &hwcap, sizeof(hwcap));
        return (hwcap & PPC_FEATURE2_ARCH_2_07);
    #else
        return (getauxval(AT_HWCAP2) & PPC_FEATURE2_ARCH_2_07);
    #endif
    }''',
    name: 'POWER8',
    args: power8flags,
  )
  if want_power8.allowed() and not have_power8 and have_linux_auxvec_h and cc.compiles(
    '''#include <sys/auxv.h>
    #include <linux/auxvec.h>
    int main() {
        return (getauxval(AT_HWCAP2) & PPC_FEATURE2_ARCH_2_07);
    }''',
    name: 'POWER8 with auxvec.h',
    args: power8flags,
  )
    have_power8 = true
    compile_args += '-DPOWER_NEED_AUXVEC_H'
  endif
  if have_power8
    compile_args += ['-DPOWER_FEATURES', '-DPOWER8_VSX']
    power8_src = [
      archdir / 'adler32_power8.c',
      archdir / 'chunkset_power8.c',
      archdir / 'slide_hash_power8.c',
    ]
    if cpu_family == 'ppc64'
      compile_args += '-DPOWER8_VSX_CRC32'
      power8_src += archdir / 'crc32_power8.c'
    endif
    arch_libs += static_library(
      'power8',
      power8_src,
      c_args: compile_args + power8flags,
      link_args: link_args,
    )
  endif
  want_power8.require(have_power8)
  summary(
    'POWER8',
    have_power8,
    section: arch_section,
    bool_yn: true,
  )

  power9flags = ['-mcpu=power9']
  want_power9 = get_option('power9')
  have_power9 = want_power9.allowed() and cc.compiles(
    '''#include <sys/auxv.h>
    #ifdef __FreeBSD__
    #include <machine/cpu.h>
    #endif
    int main() {
    #if defined(__FreeBSD__) || defined(__OpenBSD__)
        unsigned long hwcap;
        elf_aux_info(AT_HWCAP2, &hwcap, sizeof(hwcap));
        return (hwcap & PPC_FEATURE2_ARCH_3_00);
    #else
        return (getauxval(AT_HWCAP2) & PPC_FEATURE2_ARCH_3_00);
    #endif
    }''',
    name: 'POWER9',
    args: power9flags,
  )
  if want_power9.allowed() and not have_power9 and have_linux_auxvec_h and cc.compiles(
    '''#include <sys/auxv.h>
    #include <linux/auxvec.h>
    int main() {
        return (getauxval(AT_HWCAP2) & PPC_FEATURE2_ARCH_3_00);
    }''',
    name: 'POWER9 with auxvec.h',
    args: power9flags,
  )
    have_power9 = true
    compile_args += '-DPOWER_NEED_AUXVEC_H'
  endif
  if have_power9
    compile_args += ['-DPOWER_FEATURES', '-DPOWER9']
    arch_libs += static_library(
      'power9',
      archdir / 'compare256_power9.c',
      c_args: compile_args + power9flags,
      link_args: link_args,
    )
  endif
  want_power9.require(have_power9)
  summary(
    'POWER9',
    have_power9,
    section: arch_section,
    bool_yn: true,
  )

elif cpu_family in ['riscv32', 'riscv64']
  summary(
    'Architecture',
    'RISC-V',
    section: arch_section,
  )
  archdir = 'arch/riscv'

  rvvflags = ['-march=rv64gcv']
  want_rvv = get_option('rvv')
  have_rvv = want_rvv.allowed() and cc.check_header(
    'riscv_vector.h',
    args: rvvflags,
  )
  if have_rvv
    compile_args += ['-DRISCV_FEATURES', '-DRISCV_RVV']
    arch_libs += static_library(
      'rvv',
      archdir / 'adler32_rvv.c',
      archdir / 'chunkset_rvv.c',
      archdir / 'compare256_rvv.c',
      archdir / 'slide_hash_rvv.c',
      c_args: compile_args + rvvflags,
      link_args: link_args,
    )
  endif
  want_rvv.require(have_rvv)
  summary(
    'RVV',
    have_rvv,
    section: arch_section,
    bool_yn: true,
  )

  zbcflags = ['-march=rv64gc_zbc']
  want_zbc = get_option('riscv-zbc')
  have_zbc = want_zbc.allowed() and cc.compiles(
    '''#include <stdint.h>
    uint64_t f(uint64_t a, uint64_t b) {
        uint64_t c;
        __asm__ __volatile__ ("clmul %[result], %[input_a], %[input_b]" : [result] "=r" (c) : [input_a] "r" (a), [input_b] "r" (b));
        return c;
    }
    int main(void) { return f(1, 2); }''',
    name: 'RISC-V Zbc inline asm',
    args: zbcflags,
  )
  if have_zbc
    compile_args += '-DRISCV_CRC32_ZBC'
    arch_libs += static_library(
      'zbc',
      archdir / 'crc32_zbc.c',
      c_args: compile_args + zbcflags,
      link_args: link_args,
    )
  endif
  want_zbc.require(have_zbc)
  summary(
    'RISC-V Zbc',
    have_zbc,
    section: arch_section,
    bool_yn: true,
  )

  riscvflags = []
  if have_rvv and have_zbc
    riscvflags = ['-march=rv64gcv_zbc']
  elif have_rvv
    riscvflags = ['-march=rv64gcv']
  elif have_zbc
    riscvflags = ['-march=rv64gc_zbc']
  endif
  arch_libs += static_library(
    'riscv',
    archdir / 'riscv_features.c',
    c_args: compile_args + riscvflags,
    link_args: link_args,
  )

elif cpu_family in ['s390', 's390x']
  summary(
    'Architecture',
    'S390',
    section: arch_section,
  )
  archdir = 'arch/s390'
  have_s390 = cc.compiles(
    '''#include <sys/auxv.h>
    #ifndef HWCAP_S390_VXRS
    #define HWCAP_S390_VXRS (1 << 11)
    #endif
    int main() {
        return (getauxval(AT_HWCAP) & HWCAP_S390_VXRS);
    }''',
    name: 'S390',
  )
  if have_s390
    compile_args += '-DS390_FEATURES'
    src += archdir / 's390_features.c'
  endif
  summary(
    'S390',
    have_s390,
    section: arch_section,
    bool_yn: true,
  )

  foreach direction : ['deflate', 'inflate']
    # off by default
    enable = get_option('dfltcc-' + direction).enabled()
    if enable
      compile_args += '-DS390_DFLTCC_' + direction.to_upper()
      src += archdir / 'dfltcc_@0@.c'.format(direction)
    endif
    summary(
      'DFLTCC ' + direction,
      enable,
      section: arch_section,
      bool_yn: true,
    )
  endforeach

  vgfmaflags = ['-march=z13']
  if cc_id == 'gcc'
    vgfmaflags += '-mzarch'
  elif cc_id == 'clang'
    vgfmaflags += '-fzvector'
  endif
  want_crc32_vx = get_option('crc32-vx')
  have_crc32_vx = want_crc32_vx.allowed() and cc.compiles(
    '''#include <vecintrin.h>
    int main(void) {
        unsigned long long a __attribute__((vector_size(16))) = { 0 };
        unsigned long long b __attribute__((vector_size(16))) = { 0 };
        unsigned char c __attribute__((vector_size(16))) = { 0 };
        c = vec_gfmsum_accum_128(a, b, c);
        return c[0];
    }''',
    name: 'VECTOR GALOIS FIELD MULTIPLY SUM AND ACCUMULATE',
    args: vgfmaflags,
  )
  if have_crc32_vx
    compile_args += '-DS390_CRC32_VX'
    arch_libs += static_library(
      'crc32vx',
      archdir / 'crc32-vx.c',
      c_args: compile_args + vgfmaflags,
      link_args: link_args,
    )
  endif
  want_crc32_vx.require(have_crc32_vx)
  summary(
    'CRC32-VX',
    have_crc32_vx,
    section: arch_section,
    bool_yn: true,
  )

elif cpu_family in ['x86', 'x86_64']
  summary(
    'Architecture',
    'x86',
    section: arch_section,
  )
  archdir = 'arch/x86'
  compile_args += '-DX86_FEATURES'

  if cc_id == 'msvc' and cc.version().version_compare('<17')
    message('Disabling SSE2/SSE4.1 Chorba variants on Visual Studio < 2022')
    compile_args += '-DWITHOUT_CHORBA_SSE'
  endif

  if cc_id == 'msvc'
    if cc.compiles(
      '''#include <intrin.h>
      static inline void cpuid_ms(int info, unsigned int *eax, unsigned int *ebx, unsigned int *ecx, unsigned int *edx) {
          unsigned int registers[4];
          __cpuid((int *)registers, info);
          *eax = registers[0];
          *ebx = registers[1];
          *ecx = registers[2];
          *edx = registers[3];
      }
      int main(void) {
        unsigned int eax, ebx, ecx, edx;
        cpuid_ms(0, &eax, &ebx, &ecx, &edx);
        return eax;
      }''',
      name: 'MSVC CPUID intrinsics',
    )
      compile_args += '-DHAVE_CPUID_MS'
    endif
  else
    if cc.has_header_symbol('cpuid.h', '__cpuid_count')
      compile_args += '-DHAVE_CPUID_GNU'
    endif
  endif

  xsaveflags = []
  if cc_id != 'msvc' and not cc_id.startswith('intel')
    xsaveflags = ['-mxsave']
  endif
  have_xsave = cc.compiles(
    '''#ifdef _MSC_VER
    #  include <intrin.h>
    #elif __GNUC__ == 8 && __GNUC_MINOR__ > 1
    #  include <xsaveintrin.h>
    #else
    #  include <immintrin.h>
    #endif
    unsigned int f(unsigned int a) { return (int) _xgetbv(a); }
    int main(void) { return 0; }''',
    name: 'XSAVE',
    args: xsaveflags,
  ) and not (cc_id == 'gcc' and cc.version().version_compare('< 8.2'))
  if have_xsave
    compile_args += '-DX86_HAVE_XSAVE_INTRIN'
  else
    xsaveflags = []
  endif
  summary(
    'XSAVE',
    have_xsave,
    section: arch_section,
    bool_yn: true,
  )
  arch_libs += static_library(
    'x86',
    archdir / 'x86_features.c',
    c_args: compile_args + xsaveflags,
    link_args: link_args,
  )

  sse2flags = []
  if cpu_family == 'x86'
    if cc_id == 'msvc'
      sse2flags = ['/arch:SSE2']
    else
      sse2flags = ['-msse2']
    endif
  endif
  want_sse2 = get_option('sse2')
  have_sse2 = want_sse2.allowed() and cc.compiles(
    '''#include <immintrin.h>
    __m128i f(__m128i x, __m128i y) { return _mm_sad_epu8(x, y); }
    int main(void) { return 0; }''',
    name: 'SSE2',
    args: sse2flags,
  )
  if have_sse2
    compile_args += '-DX86_SSE2'
    arch_libs += static_library(
      'sse2',
      archdir / 'chorba_sse2.c',
      archdir / 'chunkset_sse2.c',
      archdir / 'compare256_sse2.c',
      archdir / 'slide_hash_sse2.c',
      c_args: compile_args + sse2flags,
      link_args: link_args,
    )
  endif
  want_sse2.require(have_sse2)
  summary(
    'SSE2',
    have_sse2,
    section: arch_section,
    bool_yn: true,
  )

  ssse3flags = []
  if cc_syntax == 'msvc' and cc_id.startswith('intel')
    ssse3flags = ['/arch:SSSE3']
  elif cc_id != 'msvc'
    ssse3flags = ['-mssse3']
  endif
  want_ssse3 = get_option('ssse3').require(have_sse2)
  have_ssse3 = want_ssse3.allowed() and cc.compiles(
    '''#include <immintrin.h>
    __m128i f(__m128i u) {
      __m128i v = _mm_set1_epi32(1);
      return _mm_hadd_epi32(u, v);
    }
    int main(void) { return 0; }''',
    name: 'SSSE3',
    args: ssse3flags,
  )
  if have_ssse3
    compile_args += '-DX86_SSSE3'
    arch_libs += static_library(
      'ssse3',
      archdir / 'adler32_ssse3.c',
      archdir / 'chunkset_ssse3.c',
      c_args: compile_args + ssse3flags,
      link_args: link_args,
    )
  endif
  want_ssse3.require(have_ssse3)
  summary(
    'SSSE3',
    have_ssse3,
    section: arch_section,
    bool_yn: true,
  )

  sse41flags = []
  if cc_syntax == 'msvc' and cc_id.startswith('intel')
    sse41flags = ['/arch:SSE4.1']
  elif cc_id != 'msvc'
    sse41flags = ['-msse4.1']
  endif
  want_sse41 = get_option('sse41').require(have_ssse3)
  have_sse41 = want_sse41.allowed() and cc.compiles(
    '''#include <smmintrin.h>
    __m128i f(__m128i a, __m128i b) { return _mm_min_epi32(a, b); }
    int main(void) { return 0; }''',
    name: 'SSE4.1',
    args: sse41flags,
  )
  if have_sse41
    compile_args += '-DX86_SSE41'
    arch_libs += static_library(
      'sse41',
      archdir / 'chorba_sse41.c',
      c_args: compile_args + sse41flags,
      link_args: link_args,
    )
  endif
  want_sse41.require(have_sse41)
  summary(
    'SSE4.1',
    have_sse41,
    section: arch_section,
    bool_yn: true,
  )

  sse42flags = []
  if cc_syntax == 'msvc' and cc_id.startswith('intel')
    sse42flags = ['/arch:SSE4.2']
  elif cc_id != 'msvc'
    sse42flags = ['-msse4.2']
  endif
  want_sse42 = get_option('sse42').require(have_sse41)
  have_sse42 = want_sse42.allowed() and cc.compiles(
    '''#include <nmmintrin.h>
    unsigned int f(unsigned int a, unsigned int b) { return _mm_crc32_u32(a, b); }
    int main(void) { return 0; }''',
    name: 'SSE4.2',
    args: sse42flags,
  )
  if have_sse42
    compile_args += '-DX86_SSE42'
    arch_libs += static_library(
      'sse42',
      archdir / 'adler32_sse42.c',
      c_args: compile_args + sse42flags,
      link_args: link_args,
    )
  endif
  want_sse42.require(have_sse42)
  summary(
    'SSE4.2',
    have_sse42,
    section: arch_section,
    bool_yn: true,
  )

  pclmulflags = []
  if cc_id != 'msvc'
    pclmulflags = ['-mpclmul']
  endif
  # The pclmul code currently crashes on Mac in 32bit mode. Avoid for now.
  want_pclmulqdq = get_option('pclmulqdq').require(
    have_sse42 and not (system == 'darwin' and cpu_family == 'x86'),
  )
  have_pclmulqdq = want_pclmulqdq.allowed() and cc.compiles(
    '''#include <immintrin.h>
    #include <wmmintrin.h>
    __m128i f(__m128i a, __m128i b) { return _mm_clmulepi64_si128(a, b, 0x10); }
    int main(void) { return 0; }''',
    name: 'PCLMULQDQ',
    args: pclmulflags,
  )
  if have_pclmulqdq
    compile_args += '-DX86_PCLMULQDQ_CRC'
    arch_libs += static_library(
      'pclmulqdq',
      archdir / 'crc32_pclmulqdq.c',
      c_args: compile_args + sse42flags + pclmulflags,
      link_args: link_args,
    )
  endif
  want_pclmulqdq.require(have_pclmulqdq)
  summary(
    'PCLMULQDQ',
    have_pclmulqdq,
    section: arch_section,
    bool_yn: true,
  )

  if cc_id == 'msvc'
    avx2flags = ['/arch:AVX2']
  else
    avx2flags = ['-mavx2', '-mbmi2']
  endif
  want_avx2 = get_option('avx2').require(have_sse42)
  have_avx2 = want_avx2.allowed() and cc.compiles(
    '''#include <immintrin.h>
    __m256i f(__m256i x) {
        const __m256i y = _mm256_set1_epi16(1);
        return _mm256_subs_epu16(x, y);
    }
    int main(void) { return 0; }''',
    name: 'AVX2',
    args: avx2flags,
  )
  if have_avx2
    compile_args += '-DX86_AVX2'
    arch_libs += static_library(
      'avx2',
      archdir / 'adler32_avx2.c',
      archdir / 'chunkset_avx2.c',
      archdir / 'compare256_avx2.c',
      archdir / 'slide_hash_avx2.c',
      c_args: compile_args + avx2flags,
      link_args: link_args,
    )
  endif
  want_avx2.require(have_avx2)
  summary(
    'AVX2',
    have_avx2,
    section: arch_section,
    bool_yn: true,
  )

  if cc_id == 'msvc'
    avx512flags = ['/arch:AVX512']
  else
    avx512flags = [
      '-mavx512f',
      '-mavx512dq',
      '-mavx512bw',
      '-mavx512vl',
      '-mbmi2',
    ]
    # For CPUs that can benefit from AVX512, it seems GCC generates suboptimal
    # instruction scheduling unless you specify a reasonable -mtune= target
    foreach mtune : ['-mtune=cascadelake', '-mtune=skylake-avx512']
      if cc.has_argument(mtune)
        avx512flags += mtune
        break
      endif
    endforeach
  endif
  want_avx512 = get_option('avx512').require(have_avx2)
  have_avx512 = want_avx512.allowed() and cc.compiles(
    '''#include <immintrin.h>
    __m512i f(__m512i y) {
      __m512i x = _mm512_set1_epi8(2);
      return _mm512_sub_epi8(x, y);
    }
    int main(void) { return 0; }''',
    name: 'AVX512',
    args: avx512flags,
  )
  if have_avx512
    compile_args += '-DX86_AVX512'
    arch_libs += static_library(
      'avx512',
      archdir / 'adler32_avx512.c',
      archdir / 'chunkset_avx512.c',
      archdir / 'compare256_avx512.c',
      c_args: compile_args + avx512flags,
      link_args: link_args,
    )
  endif
  want_avx512.require(have_avx512)
  summary(
    'AVX512',
    have_avx512,
    section: arch_section,
    bool_yn: true,
  )

  if cc_id == 'msvc'
    avx512vnniflags = ['/arch:AVX512']
  else
    avx512vnniflags = [
      '-mavx512f',
      '-mavx512dq',
      '-mavx512bw',
      '-mavx512vl',
      '-mavx512vnni',
      '-mbmi2',
    ]
    # For CPUs that can benefit from AVX512, it seems GCC generates suboptimal
    # instruction scheduling unless you specify a reasonable -mtune= target
    foreach mtune : ['-mtune=cascadelake', '-mtune=skylake-avx512']
      if cc.has_argument(mtune)
        avx512vnniflags += mtune
        break
      endif
    endforeach
  endif
  want_avx512vnni = get_option('avx512vnni').require(have_avx2)
  have_avx512vnni = want_avx512vnni.allowed() and cc.compiles(
    '''#include <immintrin.h>
    int main(void) {
        const __m512i z512 = _mm512_setzero_si512();
        const __m256i z256 = _mm256_setzero_si256();
        volatile __m512i r512 = _mm512_dpbusd_epi32(z512, z512, z512);
        volatile __m256i r256 = _mm256_dpbusd_epi32(z256, z256, z256);
        (void)r512;
        (void)r256;
        return 0;
    }''',
    name: 'AVX512-VNNI',
    args: avx512vnniflags,
  )
  if have_avx512vnni
    compile_args += '-DX86_AVX512VNNI'
    arch_libs += static_library(
      'avx512vnni',
      archdir / 'adler32_avx512_vnni.c',
      c_args: compile_args + avx512vnniflags,
      link_args: link_args,
    )
  endif
  want_avx512vnni.require(have_avx512vnni)
  summary(
    'AVX512-VNNI',
    have_avx512vnni,
    section: arch_section,
    bool_yn: true,
  )

  vpclmulflags = []
  if cc_id != 'msvc'
    vpclmulflags = ['-mvpclmulqdq', '-mavx512f']
  endif
  want_vpclmulqdq = get_option('vpclmulqdq').require(
    have_avx512 and have_pclmulqdq and not (
      system == 'darwin'
      and cpu_family == 'x86'
    ),
  )
  have_vpclmulqdq = want_vpclmulqdq.allowed() and cc.compiles(
    '''#include <immintrin.h>
    #include <wmmintrin.h>
    __m512i f(__m512i a) {
        __m512i b = _mm512_setzero_si512();
        return _mm512_clmulepi64_epi128(a, b, 0x10);
    }
    int main(void) { return 0; }''',
    name: 'VPCLMULQDQ',
    args: vpclmulflags,
  )
  if have_vpclmulqdq
    compile_args += '-DX86_VPCLMULQDQ_CRC'
    arch_libs += static_library(
      'vpclmulqdq',
      archdir / 'crc32_vpclmulqdq.c',
      c_args: compile_args + pclmulflags + vpclmulflags + avx512flags,
      link_args: link_args,
    )
  endif
  want_vpclmulqdq.require(have_vpclmulqdq)
  summary(
    'VPCLMULQDQ',
    have_vpclmulqdq,
    section: arch_section,
    bool_yn: true,
  )

else
  summary(
    'Architecture',
    'generic',
    section: arch_section,
  )
endif

zlib_ng = library(
  'z' + suffix,
  src,
  c_args: compile_args,
  link_args: link_args,
  vs_module_defs: def,
  link_with: arch_libs,
  install: true,
  version: lib_version,
)

zlib_ng_dep = declare_dependency(
  compile_args: pkg_config_cflags,
  link_with: zlib_ng,
  include_directories: include_directories('.'),
)

meson.override_dependency('zlib' + suffix, zlib_ng_dep)

import('pkgconfig').generate(
  zlib_ng,
  name: 'zlib' + suffix,
  version: pkg_version,
  description: 'zlib-ng compression library',
  extra_cflags: pkg_config_cflags,
)

if get_option('tests').allowed()
  subdir('test')
endif
