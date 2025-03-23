simd_src_x86_64 = [
  'x86_64/jccolor-avx2.asm', 'x86_64/jccolor-sse2.asm',
  'x86_64/jcgray-avx2.asm', 'x86_64/jcgray-sse2.asm',
  'x86_64/jchuff-sse2.asm', 'x86_64/jcphuff-sse2.asm',
  'x86_64/jcsample-avx2.asm', 'x86_64/jcsample-sse2.asm',
  'x86_64/jdcolor-avx2.asm', 'x86_64/jdcolor-sse2.asm',
  'x86_64/jdmerge-avx2.asm', 'x86_64/jdmerge-sse2.asm',
  'x86_64/jdsample-avx2.asm', 'x86_64/jdsample-sse2.asm',
  'x86_64/jfdctflt-sse.asm', 'x86_64/jfdctfst-sse2.asm',
  'x86_64/jfdctint-avx2.asm', 'x86_64/jfdctint-sse2.asm',
  'x86_64/jidctflt-sse2.asm', 'x86_64/jidctfst-sse2.asm',
  'x86_64/jidctint-avx2.asm', 'x86_64/jidctint-sse2.asm',
  'x86_64/jidctred-sse2.asm', 'x86_64/jquantf-sse2.asm',
  'x86_64/jquanti-avx2.asm', 'x86_64/jquanti-sse2.asm',
  'x86_64/jsimdcpu.asm',
]

simd_src_i386 = [
  'i386/jccolor-avx2.asm', 'i386/jccolor-mmx.asm', 'i386/jccolor-sse2.asm',
  'i386/jcgray-avx2.asm', 'i386/jcgray-mmx.asm', 'i386/jcgray-sse2.asm',
  'i386/jchuff-sse2.asm', 'i386/jcphuff-sse2.asm', 'i386/jcsample-avx2.asm',
  'i386/jcsample-mmx.asm', 'i386/jcsample-sse2.asm', 'i386/jdcolor-avx2.asm',
  'i386/jdcolor-mmx.asm', 'i386/jdcolor-sse2.asm', 'i386/jdmerge-avx2.asm',
  'i386/jdmerge-mmx.asm', 'i386/jdmerge-sse2.asm', 'i386/jdsample-avx2.asm',
  'i386/jdsample-mmx.asm', 'i386/jdsample-sse2.asm', 'i386/jfdctflt-3dn.asm',
  'i386/jfdctflt-sse.asm', 'i386/jfdctfst-mmx.asm', 'i386/jfdctfst-sse2.asm',
  'i386/jfdctint-avx2.asm', 'i386/jfdctint-mmx.asm', 'i386/jfdctint-sse2.asm',
  'i386/jidctflt-3dn.asm', 'i386/jidctflt-sse2.asm', 'i386/jidctflt-sse.asm',
  'i386/jidctfst-mmx.asm', 'i386/jidctfst-sse2.asm', 'i386/jidctint-avx2.asm',
  'i386/jidctint-mmx.asm', 'i386/jidctint-sse2.asm', 'i386/jidctred-mmx.asm',
  'i386/jidctred-sse2.asm', 'i386/jquant-3dn.asm', 'i386/jquantf-sse2.asm',
  'i386/jquanti-avx2.asm', 'i386/jquanti-sse2.asm', 'i386/jquant-mmx.asm',
  'i386/jquant-sse.asm', 'i386/jsimdcpu.asm',
]

simd_src_arm = files(
  'arm/jcgray-neon.c',
  'arm/jcphuff-neon.c',
  'arm/jcsample-neon.c',
  'arm/jdmerge-neon.c',
  'arm/jdsample-neon.c',
  'arm/jfdctfst-neon.c',
  'arm/jidctred-neon.c',
  'arm/jquanti-neon.c',
)

simd_opt = get_option('simd')
have_simd = false
simd = []

if host_cpu in ['x86', 'x86_64']
  have_simd = add_languages('nasm', required: simd_opt, native: false)
  if have_simd
    add_project_arguments('-DPIC', language: 'nasm')
    x64 = host_cpu == 'x86_64'
    # simulate upstream's "is ELF" check by excluding non-ELF OSes
    if x64 and host_machine.system() not in ['cygwin', 'darwin', 'windows']
      if cc.compiles('''
        #if (__CET__ & 3) == 0
        #error \"CET not enabled\"
        #endif
        int main(void) { return 0; }
      ''')
        add_project_arguments('-D__CET__', language: 'nasm')
      endif
    endif
    dir = x64 ? 'x86_64' : 'i386'
    simd_src = x64 ? simd_src_x86_64 : simd_src_i386
    simd = static_library('simd', dir / 'jsimd.c',
      simd_src, include_directories: [incdir, 'nasm', dir],
      pic: get_option('default_library') != 'static')
  endif
elif host_cpu in ['arm', 'aarch64']
  aarch = host_cpu == 'aarch64' ? 'aarch64' : 'aarch32'
  dir = 'arm' / aarch
  cdata_neon = configuration_data()

  needs_softfp_for_intrinsics = host_cpu == 'arm' and cc.compiles('''
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
    ''', name: 'does not need softfp for NEON intrinsics')
  neon_flags = []
  if host_cpu == 'arm'
    neon_flags += ['-mfpu=neon']
  endif
  if needs_softfp_for_intrinsics
    neon_flags += ['-mfloatabi=softfp']
  endif
  if host_cpu == 'arm'
    have_simd = cc.compiles('''#include <arm_neon.h>
      int main(int argc, char **argv) {
        uint16x8_t input = vdupq_n_u16((uint16_t)argc);
        uint8x8_t output = vmovn_u16(input);
        return (int)output[0];
      }''', args: neon_flags, name: 'supports NEON')
    if not have_simd
      if simd_opt.enabled()
        error('SIMD extensions not available for this architecture')
      else
        warning('SIMD extensions not available for this architecture')
        subdir_done()
      endif
    endif
  else
    have_simd = true
  endif

  if have_simd
    cdata_neon.set('HAVE_VLD1_S16_X3', cc.compiles('''#include <arm_neon.h>
      int main(int argc, char **argv) {
        int16_t input[12];
        int16x4x3_t output;
        int i;
        for (i = 0; i < 12; i++) input[i] = (int16_t)argc;
        output = vld1_s16_x3(input);
        vst3_s16(input, output);
        return (int)input[0];
      }''', args: neon_flags, name: 'supports vld1_s16_x3 intrinsic'))
    cdata_neon.set('HAVE_VLD1_U16_X2', cc.compiles('''
      #include <arm_neon.h>
      int main(int argc, char **argv) {
        uint16_t input[8];
        uint16x4x2_t output;
        int i;
        for (i = 0; i < 8; i++) input[i] = (uint16_t)argc;
        output = vld1_u16_x2(input);
        vst2_u16(input, output);
        return (int)input[0];
      }''', args: neon_flags, name: 'supports vld1_u16_x2 intrinsic'))
    cdata_neon.set('HAVE_VLD1Q_U8_X4', cc.compiles('''
      #include <arm_neon.h>
      int main(int argc, char **argv) {
        uint8_t input[64];
        uint8x16x4_t output;
        int i;
        for (i = 0; i < 64; i++) input[i] = (uint8_t)argc;
        output = vld1q_u8_x4(input);
        vst4q_u8(input, output);
        return (int)input[0];
      }''', args: neon_flags, name: 'supports vld1q_u8_x4 intrinsic'))

    subdir('arm')
    simd_src_arm += [neon_compat_h]

    # GCC 11 and earlier and some older versions of Clang do not have a full or
    # optimal set of Neon intrinsics, so for performance reasons, when using those
    # compilers, we default to using the older GAS implementation of the Neon SIMD
    # extensions for certain algorithms.  The presence or absence of the three
    # intrinsics we tested above is a reasonable proxy for this, except with GCC 10
    # and 11.

    default_neon_intrinsics = cdata_neon.get('HAVE_VLD1_S16_X3') and cdata_neon.get('HAVE_VLD1_U16_X2') and cdata_neon.get('HAVE_VLD1Q_U8_X4') and (cc.get_id() != 'gcc' or cc.version().version_compare('>= 12.0.0'))

    neon_intrinsics = get_option('neon-intrinsics').disable_auto_if(not  default_neon_intrinsics).enabled()

    if not neon_intrinsics
      if (host_cpu == 'armv7')
        gastest = '''
        .text
        .fpu neon
        .arch armv7a
        .object_arch armv4
        .arm
        pld [r0]
        vmovn.u16 d0, q0
        '''
      else
        gastest = '''
        .text
        MYVAR .req x0
        movi v0.16b, #100
        mov MYVAR, #100
        .unreq MYVAR
        '''
      endif
      f = configure_file(
        command: [python, '-c', 'import sys; print(sys.argv[1])', '@0@'.format(gastest)],
        input: 'CMakeLists.txt',
        output: 'gastest.S',
        capture: true,
      )
      # It is possible to run compile checks on generated files, however,
      # Meson versions earlier than 1.2.0 do not set the lookup path
      # correctly, causing Python to fail opening it.
      # https://github.com/mesonbuild/meson/issues/11983
      if meson.version().version_compare('>= 1.2.0')
        if not cc.compiles(f,
          args: ['-x', 'assembler-with-cpp'] + neon_flags,
          name: 'can use the partial NEON SIMD intrinsics implementation'
        )
          neon_intrinsics = true
        endif
      endif
    else
      neon_intrinsics = true
    endif

    if neon_intrinsics
      simd_src_arm += files(
        'arm/jccolor-neon.c',
        'arm/jidctint-neon.c',
      )
    endif

    if neon_intrinsics or host_cpu == 'aarch64'
      simd_src_arm += files(
        'arm/jidctfst-neon.c',
      )
    endif

    if neon_intrinsics or host_cpu == 'arm'
      simd_src_arm += files(
        dir / 'jchuff-neon.c',
        'arm/jdcolor-neon.c',
        'arm/jfdctint-neon.c',
      )
    endif

    if not neon_intrinsics
      simd_src_arm += files(
        dir / 'jsimd_neon.S'
      )
    endif

    add_project_arguments('-DNEON_INTRINSICS', language: 'c')
    simd = static_library('simd',
      simd_src_arm + files(
        dir / 'jsimd.c',
      ),
      pic: get_option('default_library') != 'static',
      include_directories: [incdir, 'arm', dir],
      c_args: neon_flags,
    )
  endif
elif simd_opt.enabled()
  error('SIMD enabled, but CPU family not supported')
endif
