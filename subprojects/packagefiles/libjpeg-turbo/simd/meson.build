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

simd_opt = get_option('simd')
have_simd = false
simd = []

if host_cpu in ['x86', 'x86_64']
  have_simd = add_languages('nasm', required: simd_opt, native: false)
  if have_simd
    add_project_arguments('-DPIC', language: 'nasm')
    x64 = host_cpu == 'x86_64'
    dir = x64 ? 'x86_64' : 'i386'
    simd_src = x64 ? simd_src_x86_64 : simd_src_i386
    simd = static_library('simd', dir / 'jsimd.c',
      simd_src, include_directories: [incdir, 'nasm', dir])
  endif
elif simd_opt.enabled()
  error('SIMD enabled, but CPU family not supported')
endif
