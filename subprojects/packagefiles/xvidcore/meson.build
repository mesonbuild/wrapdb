project(
  'xvidcore',
  'c',
  version: '1.3.7',
  license: 'GPL-2.0-or-later',
  meson_version: '>= 0.64.0',
  default_options: [
    'warning_level=2',
    meson.version().version_compare('>=1.3.0') ? 'c_std=gnu99,c99' : 'c_std=gnu99',
  ],
)

cc = meson.get_compiler('c')


host_os = host_machine.system()
cpu_family = host_machine.cpu_family()
endian = host_machine.endian()
sources = []
includes = []
nasm_args = []
c_args = []
deps = []
m_dep = cc.find_library(
  'm',
  required: false,
)
if host_os != 'windows'
  thread_dep = dependency(
    'threads',
    required: false,
  )
  if (thread_dep.found())
    if cc.has_header(
      'pthread.h',
      dependencies: thread_dep,
    )
      c_args += ['-DHAVE_PTHREAD']
      deps += thread_dep
    endif
  endif
endif

deps += m_dep

if endian == 'big'
  c_args += ['-DARCH_IS_BIG_ENDIAN']
else
  c_args += ['-DARCH_IS_LITTLE_ENDIAN']
endif

if cc.sizeof('void*') == 8
  c_args += ['-DARCH_IS_64BIT']
else
  c_args += ['-DARCH_IS_32BIT']
endif

if cc.has_header('stdint.h')
  c_args += ['-DHAVE_STDINT_H']
endif

if cc.has_header('inttypes.h')
  c_args += ['-DHAVE_INTTYPES_H']
endif

if cpu_family == 'x86_64'
  c_args += ['-DARCH_IS_X86_64']
  nasm_args += ['-DARCH_IS_X86_64']
elif cpu_family == 'x86'
  c_args += ['-DARCH_IS_IA32']
  nasm_args += ['-DARCH_IS_IA32']
elif (cpu_family == 'ppc' or cpu_family == 'ppc64') and endian == 'big'
  c_args += ['-DARCH_IS_PPC', '-maltivec', '-mabi=altivec']
else
  c_args += ['-DARCH_IS_GENERIC']
endif

if host_os == 'darwin' or (host_os == 'windows' and cpu_family == 'x86')
  nasm_args += ['-DPREFIX']

  if host_os == 'linux'
    nasm_args += ['-DMARK_FUNCS']
  endif

endif
if host_os == 'windows'
  c_args += [
    '-DWIN32',
    '-DHAVE_STDINT_H',
    '-DHAVE_INTTYPES_H',
    '-DHAVE_SYS_TYPES_H',
  ]
  if cc.get_argument_syntax() == 'msvc'
    c_args += [
      '/FIstdint.h',
      '-D_try=__try',
      '-D_except=__except',
      '/EHa',
      '/wd4996',
    ]
  endif
endif

add_project_arguments(
  c_args,
  language: 'c',
)

sources += files(
  'src/bitstream/bitstream.c',
  'src/bitstream/cbp.c',
  'src/bitstream/mbcoding.c',
  'src/dct/fdct.c',
  'src/dct/idct.c',
  'src/dct/simple_idct.c',
  'src/decoder.c',
  'src/encoder.c',
  'src/image/colorspace.c',
  'src/image/font.c',
  'src/image/image.c',
  'src/image/interpolate8x8.c',
  'src/image/postprocessing.c',
  'src/image/qpel.c',
  'src/image/reduced.c',
  'src/motion/estimation_bvop.c',
  'src/motion/estimation_common.c',
  'src/motion/estimation_gmc.c',
  'src/motion/estimation_pvop.c',
  'src/motion/estimation_rd_based.c',
  'src/motion/estimation_rd_based_bvop.c',
  'src/motion/gmc.c',
  'src/motion/motion_comp.c',
  'src/motion/sad.c',
  'src/motion/vop_type_decision.c',
  'src/plugins/plugin_2pass1.c',
  'src/plugins/plugin_2pass2.c',
  'src/plugins/plugin_dump.c',
  'src/plugins/plugin_lumimasking.c',
  'src/plugins/plugin_psnr.c',
  'src/plugins/plugin_psnrhvsm.c',
  'src/plugins/plugin_single.c',
  'src/plugins/plugin_ssim.c',
  'src/prediction/mbprediction.c',
  'src/quant/quant_h263.c',
  'src/quant/quant_matrix.c',
  'src/quant/quant_mpeg.c',
  'src/utils/emms.c',
  'src/utils/mbtransquant.c',
  'src/utils/mem_align.c',
  'src/utils/mem_transfer.c',
  'src/utils/timer.c',
  'src/xvid.c',
)

if (cpu_family == 'ppc' or cpu_family == 'ppc64') and endian == 'big'
  sources += files(
    'src/dct/ppc_asm/idct_altivec.c',
    'src/image/ppc_asm/colorspace_altivec.c',
    'src/image/ppc_asm/interpolate8x8_altivec.c',
    'src/image/ppc_asm/qpel_altivec.c',
    'src/motion/ppc_asm/sad_altivec.c',
    'src/quant/ppc_asm/quant_h263_altivec.c',
    'src/quant/ppc_asm/quant_mpeg_altivec.c',
    'src/utils/ppc_asm/altivec_trigger.c',
    'src/utils/ppc_asm/mem_transfer_altivec.c',
  )
elif cpu_family == 'x86' or cpu_family == 'x86_64'
  add_languages(
    'nasm',
    native: false,
  )
  add_project_arguments(
    nasm_args,
    language: 'nasm',
  )
  includes += include_directories('src/image/x86_asm')
  sources += files(
    'src/bitstream/x86_asm/cbp_mmx.asm',
    'src/bitstream/x86_asm/cbp_sse2.asm',
    'src/dct/x86_asm/fdct_mmx_ffmpeg.asm',
    'src/dct/x86_asm/fdct_mmx_skal.asm',
    'src/dct/x86_asm/fdct_sse2_skal.asm',
    'src/dct/x86_asm/idct_3dne.asm',
    'src/dct/x86_asm/idct_mmx.asm',
    'src/dct/x86_asm/idct_sse2_dmitry.asm',
    'src/image/x86_asm/colorspace_rgb_mmx.asm',
    'src/image/x86_asm/colorspace_yuv_mmx.asm',
    'src/image/x86_asm/colorspace_yuyv_mmx.asm',
    'src/image/x86_asm/deintl_sse.asm',
    'src/image/x86_asm/gmc_mmx.asm',
    'src/image/x86_asm/interpolate8x8_3dn.asm',
    'src/image/x86_asm/interpolate8x8_3dne.asm',
    'src/image/x86_asm/interpolate8x8_mmx.asm',
    'src/image/x86_asm/interpolate8x8_xmm.asm',
    'src/image/x86_asm/postprocessing_mmx.asm',
    'src/image/x86_asm/postprocessing_sse2.asm',
    'src/image/x86_asm/qpel_mmx.asm',
    'src/image/x86_asm/reduced_mmx.asm',
    'src/motion/x86_asm/sad_3dn.asm',
    'src/motion/x86_asm/sad_3dne.asm',
    'src/motion/x86_asm/sad_mmx.asm',
    'src/motion/x86_asm/sad_sse2.asm',
    'src/motion/x86_asm/sad_xmm.asm',
    'src/plugins/x86_asm/plugin_ssim-a.asm',
    'src/quant/x86_asm/quantize_h263_3dne.asm',
    'src/quant/x86_asm/quantize_h263_mmx.asm',
    'src/quant/x86_asm/quantize_mpeg_mmx.asm',
    'src/quant/x86_asm/quantize_mpeg_xmm.asm',
    'src/utils/x86_asm/cpuid.asm',
    'src/utils/x86_asm/interlacing_mmx.asm',
    'src/utils/x86_asm/mem_transfer_3dne.asm',
    'src/utils/x86_asm/mem_transfer_mmx.asm',
  )
endif

includes += include_directories(
  'src',
  'src/bitstream',
  'src/dct',
  'src/image',
  'src/motion',
  'src/plugins',
  'src/prediction',
  'src/quant',
  'src/utils',
)

# Install header 'xvid.h'
subdir('src')

xvidcore = library(
  'xvidcore',
  sources,
  install: true,
  dependencies: deps,
  include_directories: includes,
  vs_module_defs: 'build/generic/libxvidcore.def',
)

pkg = import('pkgconfig')

pkg.generate(xvidcore)

xvidcore_dep = declare_dependency(
  include_directories: includes,
  link_with: xvidcore,
)
meson.override_dependency('xvidcore', xvidcore_dep)

