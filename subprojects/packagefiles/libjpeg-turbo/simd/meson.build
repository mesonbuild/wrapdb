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

have_simd = false

simd_opt = get_option('simd')
if simd_opt.disabled()
  subdir_done()
endif

if host_cpu in ['x86', 'x86_64']
  nasm = find_program('nasm', required: simd_opt)
  if not nasm.found()
    subdir_done()
  endif

  x64 = host_cpu == 'x86_64'
  dir = x64 ? 'x86_64' : 'i386'

  args = ['-I@CURRENT_SOURCE_DIR@' / 'nasm', '-I@CURRENT_SOURCE_DIR@' / dir]

  suf = x64 ? '64' : '32'
  if host_system == 'windows'
    args += ['-DWIN' + suf, '-f', 'win' + suf]
  elif host_system == 'darwin'
    args += ['-DMACHO', '-f', 'macho' + suf]
  else
    args += ['-DELF', '-f', 'elf' + suf]
  endif

  if get_option('debug')
    args += '-g'
  endif

  if x64
    args += '-D__x86_64__'
  endif

  if host_system != 'windows'
    args += '-DPIC'
  endif

  args += ['-MD', '-MQ', '@OUTPUT@', '-MF', '@DEPFILE@', '-o', '@OUTPUT@', '@INPUT@']

  gen = generator(nasm,
    arguments: args,
    depfile: '@BASENAME@.dep',
    output: '@BASENAME@.obj',
  )

  simd_src = gen.process(x64 ? simd_src_x86_64 : simd_src_i386)

  have_simd = true
  simd = static_library('simd', dir / 'jsimd.c',
    simd_src, include_directories: incdir)
elif simd_opt.enabled()
  error('SIMD enabled, but CPU family not supported')
endif
