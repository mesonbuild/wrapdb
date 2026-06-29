vflags = ['-DX265_VERSION=@0@'.format(x265_version)]

if enable_assembly.allowed()
  c_args += ['-DENABLE_ASSEMBLY=1']
endif

primitives_libs = []
warndisable = []

if enable_assembly.allowed() and host_arch.startswith('x86')
  sse3 = files('vec/dct-sse3.cpp')
  ssse3 = files('vec/dct-ssse3.cpp')
  sse41 = files('vec/dct-sse41.cpp')

  if cpp.get_argument_syntax() == 'msvc'
    primitives = sse3 + ssse3 + sse41
    warndisable = cpp.get_supported_arguments('/wd4100')
    # x64 implies SSE4, so only add /arch:SSE2 if building for Win32
    if cc.get_id() == 'msvc'
      if host_arch == 'x86'
        primitives_arch_args = {
          'sse3': ['/arch:SSE2'],
          'ssse3': ['/arch:SSE2'],
          'sse41': ['/arch:SSE2'],
        }
      else
        primitives_arch_args = {
          'sse3': [],
          'ssse3': [],
          'sse41': [],
        }
      endif
    else
      primitives_arch_args = {
        'sse3': ['-msse3'],
        'ssse3': ['-mssse3'],
        'sse41': ['-msse4.1'],
      }
    endif
    foreach bit, depth : bit_depths
      foreach k, arch_args : primitives_arch_args
        primitives_args = c_args + get_variable(f'@depth@_args') + vflags + warndisable + arch_args
        primitives_libs += static_library(
          'primitives-@0@-@1@'.format(depth, k),
          get_variable(k),
          c_args: primitives_args,
          cpp_args: primitives_args,
          include_directories: include_dirs,
          build_by_default: false,
                  # gnu_symbol_visibility: 'inlineshidden',
        )
      endforeach
    endforeach
  endif

  if cpp.get_argument_syntax() == 'gcc'
    # llvm intrinsic headers cause shadow warnings
    warndisable = cpp.get_supported_arguments(
      '-Wno-shadow',
      '-Wno-unused-parameter',
    )

    if cpp.get_id() == 'clang' or cpp.version().version_compare('>= 4.3')
      primitives = sse3 + ssse3 + sse41
      primitives_arch_args = {
        'sse3': ['-msse3'],
        'ssse3': ['-mssse3'],
        'sse41': ['-msse4.1'],
      }

      foreach bit, depth : bit_depths
        foreach k, arch_args : primitives_arch_args
          primitives_args = c_args + get_variable(f'@depth@_args') + vflags + warndisable + arch_args
          primitives_libs += static_library(
            'primitives-@0@-@1@'.format(depth, k),
            get_variable(k),
            c_args: primitives_args,
            cpp_args: primitives_args,
            include_directories: include_dirs,
            build_by_default: false,
                      # gnu_symbol_visibility: 'inlineshidden',
          )
        endforeach
      endforeach
    endif
  endif

  vec_primitives = files('vec/vec-primitives.cpp')

  c_srcs = files(
    'x86/asm-primitives.cpp',
    'x86/blockcopy8.h',
    'x86/dct8.h',
    'x86/ipfilter8.h',
    'x86/loopfilter.h',
    'x86/mc.h',
    'x86/pixel.h',
    'x86/seaintegral.h',
  )

  a_srcs = files(
    'x86/blockcopy8.asm',
    'x86/const-a.asm',
    'x86/cpu-a.asm',
    'x86/dct8.asm',
    'x86/mc-a.asm',
    'x86/mc-a2.asm',
    'x86/pixel-a.asm',
    'x86/pixel-util8.asm',
    'x86/pixeladd8.asm',
    'x86/seaintegral.asm',
    'x86/ssd-a.asm',
  )

  hdr10_a_srcs = a_srcs + files(
    'x86/h-ipfilter16.asm',
    'x86/h4-ipfilter16.asm',
    'x86/intrapred16.asm',
    'x86/ipfilter16.asm',
    'x86/loopfilter.asm',
    'x86/sad16-a.asm',
    'x86/v4-ipfilter16.asm',
  )
  hdr12_a_srcs = hdr10_a_srcs

  sdr_a_srcs = a_srcs + files(
    'x86/h-ipfilter8.asm',
    'x86/intrapred8.asm',
    'x86/intrapred8_allangs.asm',
    'x86/ipfilter8.asm',
    'x86/loopfilter.asm',
    'x86/sad-a.asm',
    'x86/v4-ipfilter8.asm',
  )

  if host_arch != 'x86_64'
    pixel32_srcs = files('x86/pixel-32.asm')
    hdr10_a_srcs += pixel32_srcs
    hdr12_a_srcs += pixel32_srcs
    sdr_a_srcs += pixel32_srcs
  endif

  add_languages(
    'nasm',
    required: true,
    native: false,
  )

  include_dirs += include_directories('x86')
  if host_arch == 'x86_64'
    nasm_args += ['-DARCH_X86_64=1']
    # -DPIC was handled earlier
  else
    nasm_args += ['-DARCH_X86_64=0']
  endif

  foreach bit, depth : bit_depths
    primitives_libs += static_library(
      f'nasm-primitives-@depth@',
      get_variable(f'@depth@_a_srcs') + c_srcs,
      c_args: c_args + get_variable(f'@depth@_args') + vflags + warndisable,
      cpp_args: c_args + get_variable(f'@depth@_args') + vflags + warndisable,
      nasm_args: nasm_args + get_variable(f'@depth@_asm_args'),
      include_directories: include_dirs,
      build_by_default: false,
          # gnu_symbol_visibility: 'inlineshidden',
    )
  endforeach
endif

# have_aligned_stack isn't used anywhere

if enable_assembly.allowed() and host_arch == 'arm'
  c_srcs = files(
    'arm/asm-primitives.cpp',
    'arm/blockcopy8.h',
    'arm/dct8.h',
    'arm/ipfilter8.h',
    'arm/loopfilter.h',
    'arm/mc.h',
    'arm/pixel.h',
    'arm/seaintegral.h',
  )

  # these are only for 8-bit
  sdr_a_srcs = files(
    'arm/asm.S',
    'arm/blockcopy8.S',
    'arm/cpu-a.S',
    'arm/dct-a.S',
    'arm/mc-a.S',
    'arm/opfilter8.S',
    'arm/pixel-util.S',
    'arm/sad-a.S',
    'arm/ssd-a.S',
  )
endif

if enable_assembly.allowed() and host_arch == 'aarch64'
  if get_option('optimization') == '3'
    message('Detected CXX compiler using -O3 optimization level')
    c_args += '-DAUTO_VECTORIZE=1'
  endif

  c_srcs_neon = files(
    'aarch64/arm64-utils.cpp',
    'aarch64/arm64-utils.h',
    'aarch64/asm-primitives.cpp',
    'aarch64/dct-prim.cpp',
    'aarch64/dct-prim.h',
    'aarch64/filter-prim.cpp',
    'aarch64/filter-prim.h',
    'aarch64/fun-decls.h',
    'aarch64/intrapred-prim.cpp',
    'aarch64/loopfilter-prim.cpp',
    'aarch64/loopfilter-prim.h',
    'aarch64/mem-neon.h',
    'aarch64/pixel-prim.cpp',
    'aarch64/pixel-prim.h',
    'aarch64/sao-prim.cpp',
  )
  c_srcs_neon_dotprod = files('aarch64/filter-neon-dotprod.cpp')
  c_srcs_neon_i8mm = files('aarch64/filter-neon-i8mm.cpp')
  c_srcs_sve = files('aarch64/dct-prim-sve.cpp', 'aarch64/sao-prim-sve.cpp')
  c_srcs_sve2 = files('aarch64/sao-prim-sve2.cpp')

  arm_asms = files(
    'aarch64/asm.S',
    'aarch64/blockcopy8-common.S',
    'aarch64/blockcopy8.S',
    'aarch64/dct.S',
    'aarch64/intrapred.S',
    'aarch64/mc-a-common.S',
    'aarch64/mc-a.S',
    'aarch64/p2s-common.S',
    'aarch64/p2s.S',
    'aarch64/pixel-util-common.S',
    'aarch64/pixel-util.S',
    'aarch64/sad-a.S',
    'aarch64/ssd-a-common.S',
    'aarch64/ssd-a.S',
  )
  arm_asms_neon_dotprod = files(
    'aarch64/sad-neon-dotprod.S',
    'aarch64/ssd-neon-dotprod.S',
  )
  arm_asms_sve = files(
    'aarch64/asm-sve.S',
    'aarch64/blockcopy8-sve.S',
    'aarch64/p2s-sve.S',
    'aarch64/pixel-util-sve.S',
  )
  arm_asms_sve2 = files(
    'aarch64/mc-a-sve2.S',
    'aarch64/pixel-util-sve2.S',
    'aarch64/ssd-a-sve2.S',
  )

  aarch64_override_opts = []
  if get_option('aarch64_warnings_as_errors')
    aarch64_override_opts += 'werror=true'
  endif

  foreach bit, depth : bit_depths
    if cpu_has_neon
      primitives_args = c_args + arm_args + get_variable(f'@depth@_args') + vflags + aarch64_neon_flag
      primitives_libs += static_library(
        f'asm-primitives-neon-@depth@',
        c_srcs_neon + arm_asms,
        c_args: primitives_args + arm_args + get_variable(f'@depth@_asm_args'),
        cpp_args: primitives_args,
        include_directories: include_dirs,
        override_options: aarch64_override_opts,
        build_by_default: false,
              # gnu_symbol_visibility: 'inlineshidden',
      )
    endif
    if cpu_has_neon_dotprod
      primitives_args = c_args + arm_args + get_variable(f'@depth@_args') + vflags + aarch64_neon_dotprod_flag
      primitives_libs += static_library(
        f'asm-primitives-neon-dotprod-@depth@',
        c_srcs_neon_dotprod + arm_asms_neon_dotprod,
        c_args: primitives_args + get_variable(f'@depth@_asm_args'),
        cpp_args: primitives_args,
        include_directories: include_dirs,
        override_options: aarch64_override_opts,
        build_by_default: false,
              # gnu_symbol_visibility: 'inlineshidden',
      )
    endif
    if cpu_has_neon_i8mm
      primitives_args = c_args + get_variable(f'@depth@_args') + vflags + aarch64_neon_i8mm_flag
      primitives_libs += static_library(
        f'asm-primitives-neon-i8mm-@depth@',
        c_srcs_neon_i8mm,
        c_args: primitives_args + get_variable(f'@depth@_asm_args'),
        cpp_args: primitives_args,
        include_directories: include_dirs,
        override_options: aarch64_override_opts,
        build_by_default: false,
              # gnu_symbol_visibility: 'inlineshidden',
      )
    endif
    if cpu_has_sve and have_sve_bridge
      primitives_args = c_args + arm_args + get_variable(f'@depth@_args') + vflags + aarch64_sve_flag
      primitives_libs += static_library(
        f'asm-primitives-sve-@depth@',
        c_srcs_sve + arm_asms_sve,
        c_args: primitives_args + get_variable(f'@depth@_asm_args'),
        cpp_args: primitives_args,
        include_directories: include_dirs,
        override_options: aarch64_override_opts,
        build_by_default: false,
              # gnu_symbol_visibility: 'inlineshidden',
      )
    endif
    if cpu_has_sve2 and have_sve_bridge
      primitives_args = c_args + arm_args + get_variable(f'@depth@_args') + vflags + aarch64_sve2_flag
      primitives_libs += static_library(
        f'asm-primitives-sve2-@depth@',
        c_srcs_sve2 + arm_asms_sve2,
        c_args: primitives_args + get_variable(f'@depth@_asm_args'),
        cpp_args: primitives_args,
        include_directories: include_dirs,
        override_options: aarch64_override_opts,
        build_by_default: false,
              # gnu_symbol_visibility: 'inlineshidden',
      )
    endif
  endforeach
endif

if host_arch.startswith('ppc') and get_option('altivec')
  altivec_srcs = files(
    'ppc/dct_altivec.cpp',
    'ppc/intrapred_altivec.cpp',
    'ppc/ipfilter_altivec.cpp',
    'ppc/pixel_altivec.cpp',
  )
  foreach bit, depth : bit_depths
    primitives_args = c_args + get_variable(f'@depth@_args') + vflags + warndisable + cc.get_supported_arguments(
      [
        '-Wno-unused',
        '-Wno-unknown-pragmas',
        '-Wno-maybe-uninitialized',
      ],
    )
    primitives_libs += static_library(
      f'asm-primitives-altivec-@depth@',
      altivec_srcs,
      c_args: primitives_args,
      cpp_args: primitives_args,
      include_directories: include_dirs,
      build_by_default: false,
          # gnu_symbol_visibility: 'inlineshidden',
    )
  endforeach
endif

common = primitives_libs

foreach bit, depth : bit_depths
  common += static_library(
    f'version-@depth@',
    files('version.cpp'),
    cpp_args: c_args + get_variable(f'@depth@_args') + vflags,
    include_directories: include_dirs,
    build_by_default: false,
      # gnu_symbol_visibility: 'inlineshidden',
  )
endforeach

if cc.has_header_symbol('string.h', 'strtok_r')
  c_args += ['-DHAVE_STRTOK_R=1']
endif

if get_variable('cc_has_no_narrowing', false)
  c_args += ['-Wno-narrowing']
endif

common_files = files(
  'bitstream.cpp',
  # FIXME UPSTREAM: the x265_cpu_neon_test and x265_cpu_fast_neon_mrc_test
  # are defined in primitives under armv7a, but the gating is never
  # checked because they were defined under x86! o.O? --Amy
  'bitstream.h',
  'common.cpp',
  'common.h',
  'constants.cpp',
  'constants.h',
  'contexts.h',
  'cpu.cpp',
  'cpu.h',
  'cudata.cpp',
  'cudata.h',
  'dct.cpp',
  'deblock.cpp',
  'deblock.h',
  'frame.cpp',
  'frame.h',
  'framedata.cpp',
  'framedata.h',
  'intrapred.cpp',
  'ipfilter.cpp',
  'loopfilter.cpp',
  'lowpassdct.cpp',
  'lowres.cpp',
  'lowres.h',
  'md5.cpp',
  'md5.h',
  'mv.h',
  'param.cpp',
  'param.h',
  'piclist.cpp',
  'piclist.h',
  'picyuv.cpp',
  'picyuv.h',
  'pixel.cpp',
  'predict.cpp',
  'predict.h',
  'primitives-placeholders.cpp',
  'primitives.cpp',
  'primitives.h',
  'quant.cpp',
  'quant.h',
  'ringmem.cpp',
  'ringmem.h',
  'scaler.cpp',
  'scaler.h',
  'scalinglist.cpp',
  'scalinglist.h',
  'shortyuv.cpp',
  'shortyuv.h',
  'slice.cpp',
  'slice.h',
  'temporalfilter.cpp',
  'temporalfilter.h',
  'threading.cpp',
  'threading.h',
  'threadpool.cpp',
  'threadpool.h',
  'wavefront.cpp',
  'wavefront.h',
  'yuv.cpp',
  'yuv.h',
)

if host_machine.system() in ['windows', 'cygwin']
  common_files += files('winxp.cpp', 'winxp.h')
endif

foreach bit, depth : bit_depths
  common += static_library(
    f'common-@depth@',
    common_files + get_variable('vec_primitives', []),
    cpp_args: c_args + get_variable(f'@depth@_args') + vflags,
    include_directories: include_dirs,
    build_by_default: false,
      # gnu_symbol_visibility: 'inlineshidden',
  )
endforeach
