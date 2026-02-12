project(
  'libpng',
  'c',
  version: '1.6.55',
  license: 'libpng-2.0',
  meson_version: '>=0.56.0',
)

png_versions = meson.project_version().split('.')
png_major_version = png_versions[0]
png_minor_version = png_versions[1]
png_micro_version = png_versions[2]
png_libname = 'png@0@@1@'.format(png_major_version, png_minor_version)
png_libversion = '@0@@1@.@2@.0'.format(
  png_major_version,
  png_minor_version,
  png_micro_version,
)

cc = meson.get_compiler('c')

include = include_directories('.')

c_args = []

if host_machine.system() == 'windows'
  add_project_arguments(
    '-D_CRT_NONSTDC_NO_DEPRECATE',
    '-D_CRT_SECURE_NO_DEPRECATE',
    language: 'c',
  )
  if get_option('default_library') != 'static'
    c_args += '-DPNG_BUILD_DLL'
  endif
endif

libpng_deps = [
  dependency('zlib'),
  cc.find_library(
    'm',
    required: false,
  ),
]

png_src = files(
  'png.c',
  'pngerror.c',
  'pngget.c',
  'pngmem.c',
  'pngpread.c',
  'pngread.c',
  'pngrio.c',
  'pngrtran.c',
  'pngrutil.c',
  'pngset.c',
  'pngtrans.c',
  'pngwio.c',
  'pngwrite.c',
  'pngwtran.c',
  'pngwutil.c',
)

png_libs = []

if host_machine.cpu_family() == 'aarch64' or cc.get_define('__ARM_NEON').strip() != ''
  # libpng falls back to 32-bit NEON intrinsics on clang-cl (see 386707c6)
  # which fails the build on the default soft-float ABI
  if cc.get_id() != 'clang-cl' or cc.check_header('arm_neon.h')
    png_src += files(
      'arm/arm_init.c',
      'arm/filter_neon_intrinsics.c',
      'arm/palette_neon_intrinsics.c',
    )
    c_args += '-DPNG_ARM_NEON_OPT=2'
  endif
elif host_machine.cpu_family() in ['x86', 'x86_64']
  png_src += files('intel/filter_sse2_intrinsics.c', 'intel/intel_init.c')
  c_args += '-DPNG_INTEL_SSE_OPT=1'
elif host_machine.cpu_family() == 'loongarch64'
  have_lsx = cc.has_argument('-mlsx')
  c_args += '-DPNG_LOONGARCH_LSX_OPT=@0@'.format(have_lsx.to_int())
  if have_lsx
    png_libs += static_library(
      'lsx',
      'loongarch/loongarch_lsx_init.c',
      'loongarch/filter_lsx_intrinsics.c',
      dependencies: libpng_deps,
      c_args: c_args + ['-mlsx'],
    )
  endif
elif host_machine.cpu_family() == 'ppc64' and host_machine.endian() == 'little'
  png_src += files('powerpc/filter_vsx_intrinsics.c', 'powerpc/powerpc_init.c')
  c_args += '-DPNG_POWERPC_VSX_OPT=2'
elif host_machine.cpu_family() in ['riscv32', 'riscv64']
  # As of 1.6.49, upstream CMake defaults RVV to off, while Autotools
  # defaults to on if the compiler supports it.  libpng also supports
  # autodetection at runtime (on Linux only, with substantial skepticism in
  # comments and documentation) and runtime enablement via the libpng API
  # (only on Autotools, which doesn't compile it in by default).  It's not
  # clear that RVV is widely supported by hardware.  Avoid the whole mess
  # for now.
  c_args += '-DPNG_RISCV_RVV_OPT=0'
endif

libpng = library(
  png_libname,
  png_src,
  version: png_libversion,
  dependencies: libpng_deps,
  link_with: png_libs,
  c_args: c_args,
  install: true,
)

pngincsubdir = 'lib' + png_libname
pngincludedir = get_option('includedir') / pngincsubdir

pkglibconf = configure_file(
  input: 'scripts/pnglibconf.h.prebuilt',
  output: 'pnglibconf.h',
  copy: true,
)

install_headers(
  'png.h',
  'pngconf.h',
  pkglibconf,
  subdir: pngincsubdir,
)

libpng_dep = declare_dependency(
  include_directories: include,
  link_with: libpng,
  dependencies: libpng_deps,
)
# Keep the older dependency name for backwards-compat with old-style
# dependency(..., fallback ['libpng': 'png_dep'])
png_dep = libpng_dep
meson.override_dependency('libpng', libpng_dep)

pkgconfig = import('pkgconfig')
pkgconfig.generate(
  libpng,
  name: 'libpng',
  description: 'Loads and saves PNG files',
  filebase: 'lib' + png_libname,
  subdirs: pngincsubdir,
)

if meson.version().version_compare('>=0.61') and host_machine.system() != 'windows'
  install_symlink(
    'libpng.pc',
    install_dir: get_option('libdir') / 'pkgconfig',
    pointing_to: 'lib' + png_libname + '.pc',
  )
else
  # With old Meson releases before 0.61,
  # install_symlink() function is not available.
  # On Windows, symlink generation requires privileged access
  # which we want to avoid.

  # Meson won't let us generate the same .pc file twice, so generate one
  # which Requires: the other one.
  pkgconfig.generate(
    name: 'libpng',
    description: 'Loads and saves PNG files',
    requires: libpng,
    subdirs: pngincsubdir,
  )
endif

if get_option('tests')
  png_test = executable(
    'pngtest',
    'pngtest.c',
    dependencies: libpng_dep,
    build_by_default: false,
  )
  test(
    'pngtest',
    png_test,
    args: files('pngtest.png'),
  )
endif
