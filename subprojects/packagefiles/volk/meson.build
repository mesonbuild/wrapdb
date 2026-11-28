project(
  'volk',
  'c',
  'cpp',
  version: '3.3.0',
  license: 'LGPL-3.0-or-later AND Apache-2.0',
  meson_version: '>=0.63.0',
  default_options: ['cpp_std=c++17'],
)

cc = meson.get_compiler('c')
py = import('python').find_installation(
  modules: ['mako'],
)

version_parts = meson.project_version().split('.')
soversion = '@0@.@1@'.format(version_parts[0], version_parts[1])

# MSVC lacks C99 complex types, so upstream compiles everything as C++ there
is_msvc = cc.get_argument_syntax() == 'msvc'
src_ext = is_msvc ? 'cc' : 'c'

# Compiler names used by gen/archs.xml
if is_msvc
  compiler_name = 'msvc'
elif cc.get_id() == 'gcc'
  compiler_name = 'gnu'
else
  compiler_name = cc.get_id()
endif

cpu_family = host_machine.cpu_family()
cpu_is_x86 = cpu_family in ['x86', 'x86_64']
is_64bit = cc.sizeof('void*') == 8

volk_args = []
foreach h : ['cpuid.h', 'intrin.h', 'fenv.h', 'dlfcn.h']
  if cc.has_header(h)
    volk_args += '-DHAVE_@0@'.format(h.underscorify().to_upper())
  endif
endforeach
if (
  host_machine.system() == 'darwin'
  or not cc.has_header_symbol('stdlib.h', 'aligned_alloc')
)
  if cc.has_header_symbol('stdlib.h', 'posix_memalign')
    volk_args += '-DHAVE_POSIX_MEMALIGN'
  endif
endif

# GCC does not align the stack for AVX spills on Windows
# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=54412
if cc.get_id() == 'gcc' and host_machine.system() in ['windows', 'cygwin']
  volk_args += cc.get_supported_arguments('-Wa,-muse-unaligned-vector-move')
endif

volk_public_incs = include_directories('include', 'kernels')
volk_incs = [volk_public_incs]
if is_msvc
  volk_args += [
    '-D_USE_MATH_DEFINES',
    '-DHAVE_CONFIG_H',
    '/wo4309',
    '/wd4752',
    '/wo4273',
    '/wo4838',
  ]
  volk_incs += include_directories('cmake/msvc')
endif

use_cpu_features = cpu_family.startswith('mips') or cpu_family in [
  'arm',
  'aarch64',
  'x86',
  'x86_64',
  'ppc',
  'ppc64',
  'riscv32',
  'riscv64',
]
cpu_features_deps = []
if use_cpu_features
  subdir('cpu_features')
  volk_args += '-DVOLK_CPU_FEATURES=1'
endif

orc_dep = dependency(
  'orc-0.4',
  version: '>0.4.11',
  method: 'pkg-config',
  required: get_option('orc'),
)
have_orc = false
if orc_dep.found()
  orcc = find_program(
    'orcc',
    native: true,
    required: get_option('orc'),
  )
  have_orc = orcc.found()
endif

########################################################################
# Determine the archs supported by the compiler (lib/CMakeLists.txt)
########################################################################
compile_utils = files('gen/volk_compile_utils.py')

have_rvv_intrinsics = cc.compiles(
  files('cmake/Checks/check-rvv-intrinsics.c'),
  name: 'RVV intrinsics',
)

available_archs = []
arch_flags = {}
arch_flag_lines = run_command(
  py,
  compile_utils,
  '--mode',
  'arch_flags',
  '--compiler',
  compiler_name,
  check: true,
).stdout().strip().split(';')
foreach line : arch_flag_lines
  fields = line.split(',')
  arch = fields[0]
  flags = []
  foreach i : range(1, fields.length())
    flags += fields[i]
  endforeach
  arch_flags += {
    arch: flags,
  }

  if arch.startswith('rv') and not have_rvv_intrinsics
    continue
  endif
  if flags.length() > 0
    if not cc.has_multi_arguments(flags)
      continue
    endif
    # Upstream uses a link check, which also rejects unusable float ABIs
    if not cc.links(
      'int main(void) { return 0; }',
      args: flags,
      name: '@0@ flags'.format(arch),
    )
      continue
    endif
  endif
  available_archs += arch
endforeach

overruled_archs = []
if cpu_is_x86
  if not is_64bit and 'avx' in available_archs
    if not cc.links(
      '''#include <immintrin.h>
      int main(void) { __m128 a; __m64 b; __m128 foo = _mm_cvtpi32_ps(a, b); return 0; }''',
      args: arch_flags['avx'],
      name: '_mm_cvtpi32_ps with AVX',
    )
      overruled_archs += 'avx'
    endif
  endif
else
  overruled_archs += [
    '3dnow',
    'mmx',
    'popcount',
    'fma',
    'sse',
    'sse2',
    'sse3',
    'ssse3',
    'sse4_a',
    'sse4_1',
    'sse4_2',
    'avx',
    'avx2',
    'avx512f',
    'avx512cd',
    'avx512dq',
  ]
endif

if cc.compiles(
  '''#include <arm_neon.h>
  int main(void) { uint8_t *dest; uint8x8_t res; vst1_u8(dest, res); }''',
  args: cc.get_supported_arguments('-Wno-uninitialized'),
  name: 'NEON intrinsics',
)
  if not cc.compiles(
    '''#include <volk/volk_common.h>
    int main(void) { __VOLK_ASM("vrev32.8 q0, q0"); }''',
    include_directories: volk_incs,
    name: 'neonv7 assembly',
  )
    overruled_archs += 'neonv7'
  endif
  if not cc.compiles(
    '''#include <volk/volk_common.h>
    int main(void) { __VOLK_ASM("sub v1.4s,v1.4s,v1.4s"); }''',
    include_directories: volk_incs,
    name: 'neonv8 assembly',
  )
    overruled_archs += 'neonv8'
  endif
else
  overruled_archs += ['neon', 'neonv7', 'neonv8']
endif

if not have_orc
  overruled_archs += 'orc'
endif

if cpu_is_x86
  overruled_archs += is_64bit ? '32' : '64'
  if is_msvc
    if is_64bit
      overruled_archs += 'mmx'
    endif
    # built-in for MSVC > 2013
    available_archs += ['sse', 'sse2']
  endif
endif

if cpu_family != 'riscv64'
  overruled_archs += 'riscv64'
endif

archs = []
foreach arch : available_archs
  if arch not in overruled_archs
    archs += arch
  endif
endforeach
available_archs = archs
message('Available architectures: ' + ' '.join(available_archs))

########################################################################
# Determine the machines to build for the available archs
########################################################################
available_machines = run_command(
  py,
  compile_utils,
  '--mode',
  'machines',
  '--archs',
  ';'.join(available_archs),
  check: true,
).stdout().strip().split(';')

# A machine is redundant when a superset of it (e.g. with orc) is available
foreach arch : ['mmx', 'orc', '64', '32']
  redundant_machines = []
  foreach machine : available_machines
    machine_no_arch = machine.replace('_' + arch, '')
    if machine_no_arch != machine
      redundant_machines += machine_no_arch
    endif
  endforeach
  machines = []
  foreach machine : available_machines
    if machine not in redundant_machines
      machines += machine
    endif
  endforeach
  available_machines = machines
endforeach
message('Available machines: ' + ' '.join(available_machines))

machine_flags = {}
foreach machine : available_machines
  flags = []
  # MSVC needs no flags for intrinsics, but clang-cl does, and takes clang's
  if cc.get_id() != 'msvc'
    flags = run_command(
      py,
      compile_utils,
      '--mode',
      'machine_flags',
      '--machine',
      machine,
      '--compiler',
      cc.get_id() == 'clang-cl' ? 'clang' : compiler_name,
      check: true,
    ).stdout().strip().split()
  endif
  # At -O0, -funsafe-math-optimizations makes GCC load -0.0f as +0.0f, which
  # breaks the sign masks of the NEON sin/cos kernels
  if (
    cc.get_id() == 'gcc'
    and get_option('optimization') in ['plain', '0']
    and '-funsafe-math-optimizations' in flags
  )
    flags += ['-fsigned-zeros', '-fno-associative-math']
  endif
  machine_flags += {
    machine: flags,
  }
endforeach

########################################################################
# Code generation
########################################################################
# Upstream globs the kernels and assembly sources
glob_command = [
  py,
  '-c',
  'import pathlib, sys; print(";".join(sorted(p.name for p in pathlib.Path(sys.argv[1]).glob(sys.argv[2]))))',
]

kernel_names = []
kernel_headers = []
foreach name : run_command(
  glob_command,
  meson.current_source_dir() / 'kernels' / 'volk',
  '*.h',
  check: true,
).stdout().strip().split(';')
  kernel_names += name.replace('.h', '')
  kernel_headers += files('kernels' / 'volk' / name)
endforeach

tmpl_command = [
  py,
  files('gen/volk_tmpl_utils.py'),
  '--input',
  '@INPUT@',
  '--output',
  '@OUTPUT@',
]
tmpl_depends = kernel_headers + files(
  'gen/archs.xml',
  'gen/machines.xml',
  'gen/volk_arch_defs.py',
  'gen/volk_compile_utils.py',
  'gen/volk_kernel_defs.py',
  'gen/volk_machine_defs.py',
  'gen/volk_tmpl_utils.py',
)

subdir('include/volk')
subdir('lib')

pkg = import('pkgconfig')
pkg.generate(
  volk_lib,
  description: 'VOLK: Vector Optimized Library of Kernels',
  extra_cflags: volk_dep_args,
)
