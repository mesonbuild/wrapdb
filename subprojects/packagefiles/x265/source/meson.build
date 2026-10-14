x265_build = '215'

x265_def = configure_file(
  input: 'x265.def.in',
  output: 'x265.def',
  configuration: {
    'X265_BUILD': x265_build,
  },
  format: 'cmake',
)

x265_ver = []
vflag = []

cc = meson.get_compiler('c')
cpp = meson.get_compiler('cpp')

host_system = host_machine.system()
host_arch = host_machine.cpu_family()

if not ['windows', 'cygwin'].contains(host_system)
  makever_py = find_program(
    'meson/makever.py',
    native: true,
  )
  makedef_args = [makever_py]

  if host_system in ['darwin', 'ios']
    makedef_args += ['--os', 'darwin']
  elif host_system in ['windows', 'cygwin']
    makedef_args += ['--os', 'win']
  else
    makedef_args += ['--os', 'linux']
  endif

  if cc.symbols_have_underscore_prefix()
    makedef_args += ['--prefix', '_']
  else
    makedef_args += ['--prefix', '']
  endif

  x265_ver = custom_target(
    'x265.ver',
    command: makedef_args + ['@INPUT@'],
    input: x265_def,
    output: '@BASENAME@.ver',
    capture: true,
  )

  if host_system in ['darwin', 'ios']
    vflag = '-Wl,-exported_symbols_list,@0@'.format(x265_ver.full_path())
  else
    vflag = '-Wl,--version-script,@0@'.format(x265_ver.full_path())
  endif
endif

x265_config = configure_file(
  input: 'x265_config.h.in',
  output: 'x265_config.h',
  configuration: {
    'X265_BUILD': x265_build,
  },
  format: 'cmake',
)

ptr_size = cpp.sizeof('void*')

c_args = []
include_dirs = []

aarch64_runtime_cpu_detect = get_option('aarch64_runtime_cpu_detect')

if host_arch.startswith('x86')
  c_args += '-DX265_ARCH_X86=1'
  if ptr_size == 4
    message('Detected x86 target processor')
  else
    c_args += '-DX86_64=1'
    message('Detected x86_64 target processor')
  endif
elif host_arch.startswith('ppc')
  c_args += '-DX265_ARCH_POWER=1'
  if ptr_size == 8
    c_args += '-DPPC64=1'
    message('Detected POWER PPC64 target processor')
  else
    message('Detected POWER target processor')
  endif

  # FIXME UPSTREAM: too many errors in the WrapDB CI to count
  # e.g. ppc/intrapred_altivec.cpp:374:23: error: call to 'vec_perm' is ambiguous
  if cc.get_id() == 'clang'
    message('clang does not build under Altivec, disabling')
    host_arch = '@0@_with_broken_compiler'.format(host_arch)
  endif
elif host_arch == 'arm'
  if meson.is_cross_build()
    message('Cross compiling for ARM arch')
  else
    message('Detected ARM target processor')
  endif
  c_args += ['-DX265_ARCH_ARM=1', '-DHAVE_ARMV6=1']
elif host_arch == 'aarch64'
  message('Detected ARM64 target processor')

  # FIXME UPSTREAM: clang-cl breaks down on Windows.h inclusion in cpu.cpp:
  # https://developercommunity.visualstudio.com/t/Arm64-cross-build-breaks-down-on-windows/11022346
  if cc.get_id() == 'clang-cl'
    message('clang-cl does not build under aarch64, disabling')
    host_arch = 'aarch64_with_broken_compiler'
  endif

  aarch64_runtime_cpu_detect = aarch64_runtime_cpu_detect.disable_if(
    not ['linux', 'darwin', 'ios', 'windows'].contains(host_system),
  )

  enable_neon = get_option('neon')
  enable_neon_dotprod = get_option('neon_dotprod')
  enable_neon_i8mm = get_option('neon_i8mm')
  enable_sve = get_option('sve')
  enable_sve2 = get_option('sve2')

  # Compiler flags for AArch64 extensions.
  aarch64_neon_flag = '-march=armv8-a'
  # Neon DotProd is mandatory from Armv8.4.
  aarch64_neon_dotprod_flag = '-march=armv8.2-a+dotprod'
  # Neon I8MM is mandatory from Armv8.6.
  aarch64_neon_i8mm_flag = '-march=armv8.2-a+dotprod+i8mm'
  aarch64_sve_flag = '-march=armv8.2-a+dotprod+i8mm+sve'
  # SVE2 is only available from Armv9.0, and armv9-a implies +dotprod and +sve.
  aarch64_sve2_flag = '-march=armv9-a+i8mm+sve2'
else
  message('Unknown processor @0@'.format(host_arch))
endif

platform_libs = [
  dependency('threads'),
  cc.find_library(
    'rt',
    required: false,
  ),
]

dl_lib = cc.find_library(
  'dl',
  required: false,
)
if dl_lib.found()
  platform_libs += [dl_lib]
endif

numa_lib = dependency(
  'numa',
  required: get_option('libnuma'),
)
if numa_lib.found()
  # Try to detect the NUMA V2 API (numa_node_of_cpu symbol)
  have_numa_v2 = cc.has_function(
    'numa_node_of_cpu',
    includes: ['numa.h'],
    dependencies: numa_lib,
  )
  if have_numa_v2
    message('libnuma found, building with support for NUMA nodes')
    c_args += '-DHAVE_LIBNUMA'
    platform_libs += [numa_lib]
  endif
endif

if get_option('no_atomics')
  c_args += '-DNO_ATOMICS=1'
endif

vmaf_lib = cc.find_library(
  'vmaf',
  required: get_option('libvmaf'),
)
if vmaf_lib.found()
  c_args += '-DENABLE_LIBVMAF'
  platform_libs += vmaf_lib
endif

if host_system in ['darwin', 'ios']
  c_args += '-DMACOS=1'
endif

if cc.get_argument_syntax() == 'msvc'
  c_args += '/Ob2'  # always inline

  if not cc.has_header('stdint.h')
    include_dirs += include_directories('compat/msvc')
  endif
endif

if cc.has_define('_MSC_VER')
  # disable Microsoft's suggestions for proprietary secure APIs
  c_args += '-D_CRT_SECURE_NO_WARNINGS=1'
endif

if cc.has_header('inttypes.h')
  c_args += '-DHAVE_INT_TYPES_H=1'
endif

enable_hdr10_plus = get_option('hdr10_plus')

nasm_args = []
# On Meson, it is not possible to build shared libraries without PIC.
# Also, PIC on static libraries is governed by b_staticpic.
# This means that we can get the case where we would need a static_library
# that builds itself with and without PIC.
# So let's disable that case altogether.
if get_option('default_library') == 'both' and not get_option('b_staticpic')
  error('Mixing b_staticpic=false and default_library=both is not allowed.')
elif (get_option('default_library') == 'static' and get_option('b_staticpic')) or get_option(
  'default_library',
) != 'static'
  c_args += ['-DPIC']
  nasm_args += ['-DPIC']
endif

if cc.symbols_have_underscore_prefix()
  nasm_args += ['-DPREFIX']
endif

if host_system == 'linux'
  cpuinfo = run_command(
    'cat',
    '/proc/cpuinfo',
    capture: true,
    check: true,
  ).stdout()
elif host_system == 'darwin'
  cpuinfo = run_command(
    'sysctl',
    '-a',
    capture: true,
    check: true,
  ).stdout()
endif

if cc.get_argument_syntax() != 'msvc'
  c_args += ['-Wshadow', '-D__STDC_LIMIT_MACROS=1']
  c_args += cpp.get_supported_arguments('-Wno-class-memaccess')

  if get_option('native_build')
    c_args += '-march=native'
  elif host_arch == 'x86'
    if not cc.has_define('__i686__')
      c_args += ['-march=i686']
      cc_version = cc.version()
      if host_system == 'windows' and cc.get_id() == 'gcc' and cc_version.version_compare(
        '>= 6.0',
      ) and cc_version.version_compare(
        '< 7.0',
      )
        c_args += [-'mpreferred-stack-boundary=2']
      endif
    endif
  endif

  if host_arch == 'arm' and meson.is_cross_build()
    arm_args = ['-march=armv6', '-mfloat-abi=soft', '-mfpu=vfp', '-marm']
  elif host_arch == 'arm'
    if host_system == 'linux'
      cpu_has_neon = 'neon' in cpuinfo
    elif host_system == 'darwin'
      cpu_has_neon = 'hw.optional.neon: 1' in cpuinfo
    endif
    if cpu_has_neon
      arm_args = [
        '-mcpu=native',
        '-mfloat-abi=hard',
        '-mfpu=neon',
        '-marm',
        '-DHAVE_NEON',
      ]
    else
      arm_args = ['-mcpu=native', '-mfloat-abi=hard', '-mfpu=vfp', '-marm']
    endif
  elif host_arch == 'aarch64'
    c_args += ['-DX265_ARCH_ARM64=1']
    cpu_has_neon = true

    if aarch64_runtime_cpu_detect.allowed()
      c_args += ['-DAARCH64_RUNTIME_CPU_DETECT=1']
      message('Configuring build for run-time CPU feature detection')
    endif

    if aarch64_runtime_cpu_detect.allowed() or meson.is_cross_build()
      cpu_has_neon_dotprod = true
      cpu_has_neon_i8mm = true
      cpu_has_sve = true
      cpu_has_sve2 = true
    elif host_system == 'linux'
      cpu_has_neon_dotprod = 'asimddp' in cpuinfo
      cpu_has_neon_i8mm = 'i8mm' in cpuinfo
      cpu_has_sve = 'sve ' in cpuinfo.split()
      cpu_has_sve2 = 'sve2' in cpuinfo
    elif host_system == 'darwin'
      cpu_has_neon_dotprod = 'hw.optional.arm.FEAT_DotProd: 1' in cpuinfo
      cpu_has_neon_i8mm = 'hw.optional.arm.FEAT_I8MM: 1' in cpuinfo
      cpu_has_sve = 'hw.optional.sve: 1' in cpuinfo.split()
      cpu_has_sve2 = 'hw.optional.sve2: 1' in cpuinfo
    else
      warning('Compile-time CPU feature detection unsupported on this platform')
    endif

    if enable_sve.allowed() or enable_sve2.allowed()
      # Check whether the compiler can compile SVE functions that require
      # backup/restore of SVE registers according to AAPCS.
      # https://github.com/llvm/llvm-project/issues/80009.
      sve_compilation_test = '''
#include <arm_sve.h>
void other();
svfloat32_t func(svfloat32_t a) {
  other();
  return a;
}
int main() { return 0; }'''

      sve_compilation_c_test_compiled = cc.compiles(
        sve_compilation_test,
        args: c_args + aarch64_sve_flag,
      )
      sve_compilation_cpp_test_compiled = cpp.compiles(
        sve_compilation_test,
        args: c_args + aarch64_sve_flag,
      )

      # Check if arm_neon_sve_bridge.h is available.
      sve_header_test = '''
#ifndef __ARM_NEON_SVE_BRIDGE
#error 1
#endif
#include <arm_sve.h>
#include <arm_neon_sve_bridge.h>
int main() { return 0; }'''
      sve_header_c_test_compiled = cc.compiles(
        sve_header_test,
        args: c_args + aarch64_sve_flag,
        name: 'arm_neon_sve_bridge.h is available in C',
      )
      sve_header_cpp_test_compiled = cpp.compiles(
        sve_header_test,
        args: c_args + aarch64_sve_flag,
        name: 'arm_neon_sve_bridge.h is available in C++',
      )

      enable_sve = enable_sve.disable_if(
        not sve_compilation_c_test_compiled or not sve_compilation_cpp_test_compiled,
      )
      enable_sve2 = enable_sve2.disable_if(
        not sve_compilation_c_test_compiled or not sve_compilation_cpp_test_compiled,
      )

      if sve_compilation_c_test_compiled and sve_compilation_cpp_test_compiled and sve_header_c_test_compiled and sve_header_cpp_test_compiled
        c_args += '-DHAVE_SVE_BRIDGE=1'
        have_sve_bridge = true
      else
        have_sve_bridge = false
      endif

      # Impose constraint that disabling one extension disables all 'higher order' ones.
      if enable_neon.disabled()
        message('Disabling Neon')
        cpu_has_neon = false
      endif
      enable_neon_dotprod = enable_neon.disable_if(enable_neon.disabled())
      if enable_neon_dotprod.disabled()
        message('Disabling Neon DotProd')
        cpu_has_neon_dotprod = false
      endif
      enable_neon_i8mm = enable_neon_i8mm.disable_if(
        enable_neon_dotprod.disabled(),
      )
      if enable_neon_i8mm.disabled()
        message('Disabling Neon I8MM')
        cpu_has_neon_i8mm = false
      endif
      # FIXME UPSTREAM: have_sve_bridge needs to be taken into account in
      # asm-primitives.cpp, not here --Amy
      enable_sve = enable_sve.disable_if(
        enable_neon_i8mm.disabled() or not have_sve_bridge,
      )
      if enable_sve.disabled()
        message('Disabling SVE')
        cpu_has_sve = false
      endif
      enable_sve2 = enable_sve2.disable_if(
        enable_sve.disabled() or not have_sve_bridge,
      )
      if enable_sve2.disabled()
        message('Disabling SVE2')
        cpu_has_sve2 = false
      endif

      if cpu_has_neon
        message('Found Neon')
        c_args += '-DHAVE_NEON=1'
      endif
      if cpu_has_neon_dotprod
        message('Found Neon DotProd')
        c_args += '-DHAVE_NEON_DOTPROD=1'
      endif
      if cpu_has_neon_i8mm
        message('Found Neon I8MM')
        c_args += '-DHAVE_NEON_I8MM=1'
      endif
      if cpu_has_sve
        message('Found SVE')
        c_args += '-DHAVE_SVE=1'
      endif
      if cpu_has_sve2
        message('Found SVE2')
        c_args += '-DHAVE_SVE2=1'
      endif
      # Do not allow implicit vector type conversions in Clang builds (this
      # is already the default in GCC builds).
      arm_args = cc.get_supported_arguments('-flax-vector-conversions=none')
    endif
  endif

  # See earlier for handling of DPIC

  # skipping profiling, that's Meson managed afaiu
  # skipping static CRT, same as above
  cc_has_no_strict_overflow = cc.has_argument('-Wno-strict-overflow')
  cc_has_no_narrowing = cc.has_argument('-Wno-narrowing')
  c_args += cc.get_supported_arguments('-Wno-array-bounds')
  c_args += cc.get_supported_arguments('-ffast-math')
  if host_arch == 'aarch64'  # host_arch already considers cross build
    c_args += cc.get_supported_arguments('-mstackrealign')
  endif
  c_args += cc.get_supported_arguments('-fno-exceptions')
  # skipping fsanitize etc., same as above
endif

# FIXME UPSTREAM: upstream on armv7 doesn't include -frtti for Android --Amy
# https://gitlab.freedesktop.org/gstreamer/cerbero/-/commit/01dfa050fd9d659b6fddc5238d42e893b728c414
# FIXME UPSTREAM: Meson thinks that all code tolerates _FILE_OFFSET_BITS=64...
# not! --Amy
# https://android.googlesource.com/platform/bionic/+/master/docs/32-bit-abi.md
if host_system == 'android'
  c_args += '-frtti'
  if host_arch == 'arm' and cc.get_define('_FILE_OFFSET_BITS') != ''
    c_args += '-U_FILE_OFFSET_BITS'
  endif
endif

nasm_found = add_languages(
  'nasm',
  required: false,
  native: false,
)

enable_assembly = get_option('asm')

# FIXME UPSTREAM: Upstream always disables assembly when armv7. They didn't
# check that ENABLE_NEON as an option never exists there! --Amy
if host_arch == 'aarch64'  # in ['arm', 'aarch64']
  # Force ENABLE_ASSEMBLY to be OFF when all SIMD extensions are disabled.
  enable_assembly = enable_assembly.disable_if(enable_neon.disabled())

  # FIXME UPSTREAM: there are no checks for visual studio!
  # Also see earlier disabling of aarch64 with clang-cl
  enable_assembly = enable_assembly.disable_if(cc.has_define('_MSC_VER'))
elif nasm_found and host_arch == 'x86'
  nasm = meson.get_compiler('nasm')
  nasm_version = nasm.version()
  enable_assembly = enable_assembly.disable_if(
    nasm_version.version_compare('>= 2.13.0'),
  )
else
  enable_assembly = enable_assembly.disable_if(not nasm_found)
endif

if enable_assembly.allowed()
  c_args += '-DENABLE_ASSEMBLY'
endif

if get_option('checked_build')
  c_args += '-DCHECKED_BUILD=1'
endif

high_bit_depth = get_option('high_bit_depth').disable_if(
  not ['x86_64', 'aarch64', 'ppc64'].contains(host_arch),
)

bit_depths = {
  '8': 'sdr',
}

sdr_args = ['-DHIGH_BIT_DEPTH=0', '-DX265_DEPTH=8']
if high_bit_depth.allowed()
  if get_option('12bit')
    hdr12_args = ['-DHIGH_BIT_DEPTH=1', '-DX265_DEPTH=12']
    sdr_args += ['-DLINKED_12BIT=1']
    bit_depths += {
      '12': 'hdr12',
    }
  endif
  if get_option('10bit')
    hdr10_args = ['-DHIGH_BIT_DEPTH=1', '-DX265_DEPTH=10']
    sdr_args += ['-DLINKED_10BIT=1']
    bit_depths += {
      '10': 'hdr10',
    }
  endif
endif

if enable_hdr10_plus
  include_dirs += [
    include_directories('.'),
    include_directories('dynamicHDR10'),
  ]
  subdir('dynamicHDR10')
  c_args += ['-DENABLE_HDR10_PLUS']
endif

# svt-hevc unsupported as of Aug 2024
# https://www.phoronix.com/news/Intel-Discontinues-SVT-HEVC

if high_bit_depth.allowed()
  if get_option('12bit')
    hdr12_args += ['-DX265_NS=x265_12bit', '-DEXPORT_C_API=0']
    hdr12_asm_args = hdr12_args + ['-DHIGH_BIT_DEPTH=1', '-DBIT_DEPTH=12']
  endif
  if get_option('10bit')
    hdr10_args += ['-DX265_NS=x265_10bit', '-DEXPORT_C_API=0']
    hdr10_asm_args = hdr10_args + ['-DHIGH_BIT_DEPTH=1', '-DBIT_DEPTH=10']
  endif
endif
# This Meson port ships with 8-bit by default. 10 and 12-bit are additive --Amy
sdr_args += ['-DX265_NS=x265', '-DEXPORT_C_API=1']
sdr_asm_args = sdr_args + ['-DHIGH_BIT_DEPTH=0', '-DBIT_DEPTH=8']

# skipping windows XP support etc.

if host_arch.startswith('ppc')
  # IBM Power8
  if get_option('altivec')
    c_args += [
      '-DHAVE_ALTIVEC=1',
      '-maltivec',
      '-mabi=altivec',
      '-flax-vector-conversions',
      '-fpermissive',
    ]
  else
    c_args += ['-DHAVE_ALTIVEC=0']
  endif

  if get_option('cpu_power8')
    c_args += ['-mcpu=power8', '-DX265_ARCH_POWER8=1']
  endif
endif

git = find_program(
  'git',
  native: true,
)

version_py = find_program(
  'meson/version.py',
  native: true,
)

version_data = run_command(
  version_py,
  '--git',
  git,
  meson.project_source_root(),
  capture: true,
  check: true,
)

x265_version = ''
x265_latest_tag = ''
foreach line : version_data.stdout().splitlines()
  if '=' in line
    kv = line.split('=')
    set_variable(kv[0].strip().to_lower(), kv[1].strip())
  endif
endforeach

include_dirs += [
  include_directories('.'),
  include_directories('common'),
  include_directories('encoder'),
]

if get_option('detailed_cu_stats')
  c_args += '-DDETAILED_CU_STATS'
endif

if get_option('alpha')
  c_args += '-DENABLE_ALPHA'
endif

if get_option('multiview')
  c_args += '-DENABLE_MULTIVIEW'
endif

if get_option('scc_ext')
  c_args += '-DENABLE_SCC_EXT'
endif

subdir('encoder')
subdir('common')

x265_rc = []

if host_system == 'windows'
  windows = import('windows')
  version_list = x265_version.split('+')[0].split('.')

  x265_rc_file = configure_file(
    input: 'x265.rc.in',
    output: 'x265.rc',
    configuration: {
      'X265_VERSION': x265_version,
      'X265_VERSION_MAJOR': version_list[0],
      'X265_VERSION_MINOR': version_list[1],
      'X265_BRANCH_ID': 0,  # TODO: 0 - stable, 1 - default or other
      'X265_TAG_DISTANCE': x265_tag_distance,
    },
  )
  x265_rc = windows.compile_resources(x265_rc_file)
endif

x265_objs = []
foreach l : encoders
  x265_objs += l.extract_all_objects(
    recursive: true,
  )
endforeach
foreach l : common
  x265_objs += l.extract_all_objects(
    recursive: true,
  )
endforeach

x265_version = x265_build

if x265_latest_tag != '' or not git.found()
  x265_version = x265_latest_tag
endif

if enable_hdr10_plus
  # FIXME UPSTREAM: hdr10plus doesn't export any symbol on Windows, I don't
  # think Multicoreware intended this --Amy
  if host_system == 'windows'
    dynamicHDR10_lib = static_library(
      'hdr10plus',
      dynamicHDR10_srcs,
      c_args: c_args,
      cpp_args: c_args,
      include_directories: include_dirs,
      override_options: ['cpp_std=c++11', 'warning_level=2'],
      dependencies: platform_libs,
      # gnu_symbol_visibility: 'inlineshidden',
      install: true,
    )
  else
    dynamicHDR10_lib = library(
      'hdr10plus',
      dynamicHDR10_srcs,
      c_args: c_args,
      cpp_args: c_args,
      include_directories: include_dirs,
      override_options: ['cpp_std=c++11', 'warning_level=2'],
      link_args: cc.get_supported_link_arguments('-Wl,-Bsymbolic,-znoexecstack'),
      dependencies: platform_libs,
      # gnu_symbol_visibility: 'inlineshidden',
      install: true,
    )
  endif
  x265_objs += dynamicHDR10_lib.extract_all_objects(
    recursive: true,
  )
  x265_lib = library(
    'x265',
    [x265_config, x265_rc],
    include_directories: include_dirs,
    objects: x265_objs,
    link_args: cc.get_supported_link_arguments('-Wl,-Bsymbolic,-znoexecstack') + vflag,
    dependencies: platform_libs,
    link_depends: x265_ver,
    vs_module_defs: x265_def,
    soversion: x265_build,
    version: x265_version,
    # FIXME: https://github.com/mesonbuild/meson/issues/15234
    # prelink: true,
    # FIXME: inlineshidden takes effect on prelinking
    # And on macOS, -exported_symbols_list cannot unhide the symbols
    # gnu_symbol_visibility: 'inlineshidden',
    install: true,
  )
else
  x265_lib = library(
    'x265',
    [x265_config, x265_rc],
    include_directories: include_dirs,
    link_whole: encoders + common,
    link_args: cc.get_supported_arguments('-Wl,-Bsymbolic,-znoexecstack') + vflag,
    dependencies: platform_libs,
    link_depends: x265_ver,
    vs_module_defs: x265_def,
    soversion: x265_build,
    version: x265_version,
    # FIXME: https://github.com/mesonbuild/meson/issues/15234
    # prelink: true,
    # FIXME: inlineshidden takes effect on prelinking
    # And on macOS, -exported_symbols_list cannot unhide the symbols
    # gnu_symbol_visibility: 'inlineshidden',
    install: true,
  )
endif

pkg = import('pkgconfig')

pc_file = pkg.generate(
  x265_lib,
  description: 'H.265/HEVC video encoder',
)

cli = get_option('cli')

# FIXME UPSTREAM: y4m.cpp also forces _FILE_OFFSET_BITS. See above as to why
# that's a nono --Amy
cli = cli.disable_if(host_system == 'android' and host_arch == 'arm')

if cli.allowed()
  input_files = files(
    'input/input.cpp',
    'input/input.h',
    'input/y4m.cpp',
    'input/y4m.h',
    'input/yuv.cpp',
    'input/yuv.h',
  )
  output_files = files(
    'output/output.cpp',
    'output/output.h',
    'output/raw.cpp',
    'output/raw.h',
    'output/reconplay.cpp',
    'output/reconplay.h',
    'output/y4m.cpp',
    'output/y4m.h',
    'output/yuv.cpp',
    'output/yuv.h',
  )

  getopt_lib = []
  if not cc.has_header('getopt.h')
    include_dirs += include_directories('compat/getopt')
    getopt_lib = static_library(
      'getopt',
      files('compat/getopt/getopt.c', 'compat/getopt/getopt.h'),
      c_args: cc.get_supported_arguments('/wd4100', '/wd4131') + '-DHAVE_STRING_H=1',
      include_directories: include_dirs,
          # gnu_symbol_visibility: 'inlineshidden',
    )
  endif

  cli = executable(
    'x265',
    input_files + output_files + files(
      'abrEncApp.cpp',
      'abrEncApp.h',
      'x265.cpp',
      'x265.h',
      'x265cli.cpp',
      'x265cli.h',
    ),
    extra_files: files('../COPYING'),
    # FIXME UPSTREAM: what happens when the CLI uses 10 or 12-bit depth?
    # Is it supposed to be built under 8-bit? --Amy
    cpp_args: [c_args, sdr_args],
    # The CLI cannot link to the shared library on Windows, it
    # requires internal APIs not exported from the DLL
    objects: x265_lib.extract_all_objects(
      recursive: true,
    ),
    include_directories: include_dirs,
    link_whole: [getopt_lib],
    install: true,
  )
endif

install_headers(files('x265.h') + x265_config)

# FIXME UPSTREAM: testbench.cpp force requires x265::setupAssemblyPrimitives,
# which is not available on armv7 when not ENABLE_ASSEMBLY --Amy
# FIXME: the above should use "and host_arch.startswith('x86')" --Amy
# FIXME UPSTREAM: upstream doesn't do any detection for runnable binaries --Amy
# FIXME UPSTREAM: upstream test for addAvg[8x8] 10-bit on NEON doesn't tolerate anything
# other than optimization=3 --Amy
enable_tests = get_option('tests').disable_if(
  enable_assembly.disabled() or not meson.can_run_host_binaries() or get_option(
    'optimization',
  ) != '3',
)

if enable_tests.allowed()
  subdir('test')
endif
