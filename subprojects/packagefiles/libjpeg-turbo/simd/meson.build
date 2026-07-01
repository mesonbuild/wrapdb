simd_src_x86_64 = [
  'x86_64/jccolor-avx2.asm',
  'x86_64/jccolor-sse2.asm',
  'x86_64/jcgray-avx2.asm',
  'x86_64/jcgray-sse2.asm',
  'x86_64/jchuff-sse2.asm',
  'x86_64/jcphuff-sse2.asm',
  'x86_64/jcsample-avx2.asm',
  'x86_64/jcsample-sse2.asm',
  'x86_64/jdcolor-avx2.asm',
  'x86_64/jdcolor-sse2.asm',
  'x86_64/jdmerge-avx2.asm',
  'x86_64/jdmerge-sse2.asm',
  'x86_64/jdsample-avx2.asm',
  'x86_64/jdsample-sse2.asm',
  'x86_64/jfdctflt-sse.asm',
  'x86_64/jfdctfst-sse2.asm',
  'x86_64/jfdctint-avx2.asm',
  'x86_64/jfdctint-sse2.asm',
  'x86_64/jidctflt-sse2.asm',
  'x86_64/jidctfst-sse2.asm',
  'x86_64/jidctint-avx2.asm',
  'x86_64/jidctint-sse2.asm',
  'x86_64/jidctred-sse2.asm',
  'x86_64/jquantf-sse2.asm',
  'x86_64/jquanti-avx2.asm',
  'x86_64/jquanti-sse2.asm',
  'x86_64/jsimdcpu.asm',
  'jsimd.c',
]

simd_src_i386 = [
  'i386/jccolor-avx2.asm',
  'i386/jccolor-mmx.asm',
  'i386/jccolor-sse2.asm',
  'i386/jcgray-avx2.asm',
  'i386/jcgray-mmx.asm',
  'i386/jcgray-sse2.asm',
  'i386/jchuff-sse2.asm',
  'i386/jcphuff-sse2.asm',
  'i386/jcsample-avx2.asm',
  'i386/jcsample-mmx.asm',
  'i386/jcsample-sse2.asm',
  'i386/jdcolor-avx2.asm',
  'i386/jdcolor-mmx.asm',
  'i386/jdcolor-sse2.asm',
  'i386/jdmerge-avx2.asm',
  'i386/jdmerge-mmx.asm',
  'i386/jdmerge-sse2.asm',
  'i386/jdsample-avx2.asm',
  'i386/jdsample-mmx.asm',
  'i386/jdsample-sse2.asm',
  'i386/jfdctflt-3dn.asm',
  'i386/jfdctflt-sse.asm',
  'i386/jfdctfst-mmx.asm',
  'i386/jfdctfst-sse2.asm',
  'i386/jfdctint-avx2.asm',
  'i386/jfdctint-mmx.asm',
  'i386/jfdctint-sse2.asm',
  'i386/jidctflt-3dn.asm',
  'i386/jidctflt-sse2.asm',
  'i386/jidctflt-sse.asm',
  'i386/jidctfst-mmx.asm',
  'i386/jidctfst-sse2.asm',
  'i386/jidctint-avx2.asm',
  'i386/jidctint-mmx.asm',
  'i386/jidctint-sse2.asm',
  'i386/jidctred-mmx.asm',
  'i386/jidctred-sse2.asm',
  'i386/jquantf-3dn.asm',
  'i386/jquantf-sse2.asm',
  'i386/jquanti-avx2.asm',
  'i386/jquanti-sse2.asm',
  'i386/jquanti-mmx.asm',
  'i386/jquantf-sse.asm',
  'i386/jsimdcpu.asm',
  'jsimd.c',
]

simd_src_arm = files(
  'arm/jccolor-neon.c',
  'arm/jcgray-neon.c',
  'arm/jcphuff-neon.c',
  'arm/jcsample-neon.c',
  'arm/jdcolor-neon.c',
  'arm/jdmerge-neon.c',
  'arm/jdsample-neon.c',
  'arm/jfdctfst-neon.c',
  'arm/jfdctint-neon.c',
  'arm/jidctfst-neon.c',
  'arm/jidctint-neon.c',
  'arm/jidctred-neon.c',
  'arm/jquanti-neon.c',
  'jsimd.c',
)

simd_src_ppc = files(
  'powerpc/jccolor-altivec.c',
  'powerpc/jcgray-altivec.c',
  'powerpc/jcsample-altivec.c',
  'powerpc/jdcolor-altivec.c',
  'powerpc/jdmerge-altivec.c',
  'powerpc/jdsample-altivec.c',
  'powerpc/jfdctfst-altivec.c',
  'powerpc/jfdctint-altivec.c',
  'powerpc/jidctfst-altivec.c',
  'powerpc/jidctint-altivec.c',
  'powerpc/jquanti-altivec.c',
  'powerpc/jsimdcpu.c',
  'jsimd.c',
)

simd_src_riscv = files(
  'riscv64/jccolor-rvv.c',
  'riscv64/jcgray-rvv.c',
  'riscv64/jcsample-rvv.c',
  'riscv64/jdcolor-rvv.c',
  'riscv64/jdmerge-rvv.c',
  'riscv64/jdsample-rvv.c',
  'riscv64/jfdctfst-rvv.c',
  'riscv64/jfdctint-rvv.c',
  'riscv64/jidctfst-rvv.c',
  'riscv64/jidctint-rvv.c',
  'riscv64/jquanti-rvv.c',
  'riscv64/jsimdcpu.c',
  'riscv64/jsimdcpu.S',
  'jsimd.c',
)

simd_src_mips64 = files(
  'mips64/jccolor-mmi.c',
  'mips64/jcgray-mmi.c',
  'mips64/jcsample-mmi.c',
  'mips64/jdcolor-mmi.c',
  'mips64/jdmerge-mmi.c',
  'mips64/jdsample-mmi.c',
  'mips64/jfdctfst-mmi.c',
  'mips64/jfdctint-mmi.c',
  'mips64/jidctfst-mmi.c',
  'mips64/jidctint-mmi.c',
  'mips64/jquanti-mmi.c',
  'mips64/jsimdcpu.c',
  'jsimd.c',
)

simd_opt = get_option('simd')
have_simd = false
simd = []
simd_architecture = 'NONE'

foreach _sym : ['getauxval', 'elf_aux_info']
  if cc.has_header_symbol('sys/auxv.h', _sym)
    add_project_arguments(
      '-DHAVE_' + _sym.to_upper(),
      language: 'c',
    )
  endif
endforeach

if host_cpu in ['x86', 'x86_64']
  simd_architecture = host_cpu == 'x86' ? 'I386' : 'X86_64'
  have_simd = add_languages(
    'nasm',
    required: simd_opt,
    native: false,
  )
  if have_simd
    add_project_arguments(
      '-DPIC',
      language: 'nasm',
    )
    x64 = host_cpu == 'x86_64'
    # simulate upstream's "is ELF" check by excluding non-ELF OSes
    if x64 and host_machine.system() not in ['cygwin', 'darwin', 'windows']
      if cc.compiles(
        '''
        #if (__CET__ & 3) == 0
        #error \"CET not enabled\"
        #endif
        int main(void) { return 0; }
      ''',
      )
        add_project_arguments(
          '-D__CET__',
          language: 'nasm',
        )
      endif
    endif
    dir = x64 ? 'x86_64' : 'i386'
    simd_src = x64 ? simd_src_x86_64 : simd_src_i386
    simd = static_library(
      'simd',
      simd_src,
      include_directories: [incdir, 'nasm', dir],
      pic: get_option('default_library') != 'static',
    )
  endif
elif host_cpu in ['arm', 'aarch64']
  simd_architecture = host_cpu == 'aarch64' ? 'ARM64' : 'ARM'
  aarch = host_cpu == 'aarch64' ? 'aarch64' : 'aarch32'
  dir = 'arm' / aarch
  cdata_neon = configuration_data()

  needs_softfp_for_intrinsics = host_cpu == 'arm' and cc.compiles(
    '''
    #if defined(__ARM_NEON__) || (!defined(__linux__) && !defined(ANDROID) && !defined(__ANDROID__))
    #error \"Neon run-time auto-detection will not be used\"
    #endif
    #if __ARM_PCS_VFP == 1
    #error \"float ABI = hard\"
    #endif
    #if __SOFTFP__ != 1
    #error \"float ABI = softfp\"
    #endif
    int main(void) { return 0; }"
    ''',
    name: 'does not need softfp for Neon intrinsics',
  )
  neon_flags = []
  if host_cpu == 'arm'
    neon_flags += ['-mfpu=neon']
  endif
  if needs_softfp_for_intrinsics
    neon_flags += ['-mfloatabi=softfp']
  endif
  if host_cpu == 'arm'
    have_simd = cc.compiles(
      '''#include <arm_neon.h>
      int main(int argc, char **argv) {
        uint16x8_t input = vdupq_n_u16((uint16_t)argc);
        uint8x8_t output = vmovn_u16(input);
        return (int)output[0];
      }''',
      args: neon_flags,
      name: 'supports Neon',
    )
    if not have_simd
      if simd_opt.enabled()
        error('SIMD extensions not available for this architecture')
      else
        warning('SIMD extensions not available for this architecture')
      endif
    endif
  else
    have_simd = true
  endif

  if have_simd
    cdata_neon.set(
      'HAVE_VLD1_S16_X3',
      cc.compiles(
        '''#include <arm_neon.h>
      int main(int argc, char **argv) {
        int16_t input[12];
        int16x4x3_t output;
        int i;
        for (i = 0; i < 12; i++) input[i] = (int16_t)argc;
        output = vld1_s16_x3(input);
        vst3_s16(input, output);
        return (int)input[0];
      }''',
        args: neon_flags,
        name: 'supports vld1_s16_x3 intrinsic',
      ),
    )
    cdata_neon.set(
      'HAVE_VLD1_U16_X2',
      cc.compiles(
        '''
      #include <arm_neon.h>
      int main(int argc, char **argv) {
        uint16_t input[8];
        uint16x4x2_t output;
        int i;
        for (i = 0; i < 8; i++) input[i] = (uint16_t)argc;
        output = vld1_u16_x2(input);
        vst2_u16(input, output);
        return (int)input[0];
      }''',
        args: neon_flags,
        name: 'supports vld1_u16_x2 intrinsic',
      ),
    )
    cdata_neon.set(
      'HAVE_VLD1Q_U8_X4',
      cc.compiles(
        '''
      #include <arm_neon.h>
      int main(int argc, char **argv) {
        uint8_t input[64];
        uint8x16x4_t output;
        int i;
        for (i = 0; i < 64; i++) input[i] = (uint8_t)argc;
        output = vld1q_u8_x4(input);
        vst4q_u8(input, output);
        return (int)input[0];
      }''',
        args: neon_flags,
        name: 'supports vld1q_u8_x4 intrinsic',
      ),
    )

    subdir('arm')

    # GCC 11 and earlier and some older versions of Clang do not have a full or
    # optimal set of Neon intrinsics.  The presence or absence of the three
    # intrinsics we tested above is a reasonable proxy for this, except with GCC 10
    # and 11.
    if not cdata_neon.get('HAVE_VLD1_S16_X3') or not cdata_neon.get(
      'HAVE_VLD1_U16_X2',
    ) or not cdata_neon.get(
      'HAVE_VLD1Q_U8_X4',
    ) or (
      cc.get_id() == 'gcc'
      and cc.version().version_compare('< 12.0.0')
    )
      warning(
        'The compiler\'s Arm Neon intrinsics implementation is incomplete or suboptimal.  Performance will suffer.  Use GCC 12 or later or Clang for full performance.',
      )
    endif

    simd = static_library(
      'simd',
      dir / 'jchuff-neon.c',
      dir / 'jsimdcpu.c',
      simd_src_arm,
      neon_compat_h,
      pic: get_option('default_library') != 'static',
      include_directories: [incdir, 'arm'],
      c_args: neon_flags,
    )
  endif
elif host_cpu in ['ppc', 'ppc64']
  simd_architecture = 'POWERPC'
  have_simd = cc.compiles(
    '''
    #include <altivec.h>
    int main(void) {
      __vector int vi = { 0, 0, 0, 0 };
      int i[4];
      vec_st(vi, 0, i);
      return i[0];
    }''',
    args: '-maltivec',
    name: 'AltiVec',
  )
  if have_simd
    simd = static_library(
      'simd',
      simd_src_ppc,
      include_directories: [incdir, 'powerpc'],
      pic: get_option('default_library') != 'static',
      c_args: '-maltivec',
    )
  endif
elif host_cpu == 'riscv64'
  simd_architecture = 'RISCV64'
  have_simd = cc.compiles(
    '''
    #include <riscv_vector.h>
    int main(int argc, char **argv) {
      size_t vl = __riscv_vsetvl_e32m8(32);
      vuint32m8_t tmp0 = __riscv_vmv_v_x_u32m8(argc, vl);
      vuint16m4_t tmp1 = __riscv_vnclipu_wx_u16m4(tmp0, 1, __RISCV_VXRM_RNU, vl);
      vuint16m4_t tmp2 = __riscv_vnclipu_wx_u16m4(tmp0, 1, __RISCV_VXRM_RDN, vl);
      vuint8m2_t tmp3 = __riscv_vmv_v_x_u8m2(argc, vl);
      vuint8m2_t tmp4 = __riscv_vmv_v_x_u8m2(argc, vl);
      vuint8m2x2_t tmp5 = __riscv_vcreate_v_u8m2x2(tmp3, tmp4);
      return __riscv_vmv_x_s_u16m4_u16(tmp1) + __riscv_vmv_x_s_u16m4_u16(tmp2) +
             __riscv_vmv_x_s_u8m2_u8(__riscv_vget_v_u8m2x2_u8m2(tmp5, 0)) +
             __riscv_vmv_x_s_u8m2_u8(__riscv_vget_v_u8m2x2_u8m2(tmp5, 1));
    }
    ''',
    args: '-march=rv64gcv',
    name: 'RVV',
  )
  if have_simd
    simd = static_library(
      'simd',
      simd_src_riscv,
      include_directories: [incdir, 'riscv64'],
      pic: get_option('default_library') != 'static',
      c_args: '-march=rv64gcv',
    )
  endif
elif host_cpu == 'loongarch64'
  simd_architecture = 'MIPS64'
  have_simd = cc.compiles(
    '''
    #if !(defined(__mips__) && __mips_isa_rev < 6)
    #error \"Loongson MMI can't work with MIPS Release 6+\"
    #endif
    int main(void) {
      int c = 0, a = 0, b = 0;
      asm (
        \"paddb %0, %1, %2\"
        : \"=f\" (c)
        : \"f\" (a), \"f\" (b)
      );
      return c;
    }
    ''',
    args: '-Wa,-mloongson-mmi,-mloongson-ext',
    name: 'MMI',
  )
  if have_simd
    simd = static_library(
      'simd',
      simd_src_mips64,
      include_directories: [incdir, 'mips64'],
      pic: get_option('default_library') != 'static',
      c_args: [
        '-Wa,-mloongson-mmi,-mloongson-ext',
        cc.get_supported_arguments('-fno-strict-aliasing'),
      ],
    )
  endif
elif simd_opt.enabled()
  error('SIMD enabled, but CPU family not supported')
endif
