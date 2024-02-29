# Build the demo app, small examples

# First thing define the common source:
common_srcs = files('../common/color.c', '../common/opj_getopt.c', 'convert.c', 'convertbmp.c', 'index.c')

if libtiff_dep.found()
  common_srcs += 'converttif.c'
endif

if libpng_dep.found()
  common_srcs += 'convertpng.c'
endif

# Headers file are located here:
inc_dirs = include_directories('../../lib/openjp2', '../common')

# Loop over all executables:
foreach exe : ['opj_decompress', 'opj_compress', 'opj_dump']
  exe_c = files(exe + '.c')
  exe_src = exe_c + common_srcs
  exe_deps = [libopenjp2_dep, libpng_dep, libtiff_dep, liblcms2_dep, rt_dep, m_dep]
  exe_exe = executable(
    exe,
    exe_src,
    include_directories: inc_dirs,
    dependencies: exe_deps,
    install: true,
  )
endforeach
