have_rdtsc = cc.has_header_symbol('intrin.h', '__rdtsc')
if have_rdtsc
  c_args += '-DHAVE_RDTSC=1'
elif host_arch.startswith('x86')
  # FIXME UPSTREAM: On AppleClang x86_64 __rdtsc is a builtin --Amy
  if cc.compiles(
    'int main() { return __rdtsc(); }',
    name: 'Has __rdtsc as a builtin',
  )
    c_args += '-DHAVE_RDTSC=1'
    # Cheats forced inclusion of intrin.h with HAVE_RDTSC
    include_dirs += include_directories('../meson')
  endif
endif

# add X86 assembly files
if host_arch.startswith('x86')
  nasm_src = files('checkasm-a.asm')
  # add ARM assembly files
elif host_arch == 'arm'
  nasm_src = files('checkasm-arm.S')
else
  nasm_src = []
endif

testbench_srcs = nasm_src + files(
  'intrapredharness.cpp',
  'intrapredharness.h',
  'ipfilterharness.cpp',
  'ipfilterharness.h',
  'mbdstharness.cpp',
  'mbdstharness.h',
  'pixelharness.cpp',
  'pixelharness.h',
  'testbench.cpp',
  'testharness.h',
)

# FIXME UPSTREAM: on CMake checkasm-arm uses NASM_FLAGS,
# that was wrong since day one! --Amy
if enable_assembly.allowed() and host_arch.startswith('x86')
  foreach bit, depth : bit_depths
    testbench_args = c_args + get_variable(f'@depth@_args')
    testbench = executable(
      f'TestBench-@depth@',
      testbench_srcs,
      c_args: testbench_args,
      cpp_args: testbench_args,
      nasm_args: nasm_args + get_variable(f'@depth@_asm_args'),
      objects: x265_lib.extract_all_objects(
        recursive: true,
      ),
      include_directories: include_dirs,
      dependencies: platform_libs,
    )
    test(f'TestBench-@depth@', testbench)
  endforeach
else
  # FIXME: let me know if this needs getting @depth@_asm_args --Amy
  foreach bit, depth : bit_depths
    testbench_args = c_args + get_variable(f'@depth@_args')
    testbench = executable(
      f'TestBench-@depth@',
      testbench_srcs,
      c_args: testbench_args,
      cpp_args: testbench_args,
      objects: x265_lib.extract_all_objects(
        recursive: true,
      ),
      include_directories: include_dirs,
      dependencies: platform_libs,
    )
    test(f'TestBench-@depth@', testbench)
  endforeach
endif
