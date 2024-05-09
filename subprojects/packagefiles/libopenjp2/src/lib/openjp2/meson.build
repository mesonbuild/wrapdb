openjp2_srcs = files(
  'bio.c',
  'cio.c',
  'dwt.c',
  'event.c',
  'function_list.c',
  'ht_dec.c',
  'image.c',
  'invert.c',
  'j2k.c',
  'jp2.c',
  'mct.c',
  'mqc.c',
  'openjpeg.c',
  'opj_clock.c',
  'opj_malloc.c',
  'pi.c',
  'sparse_array.c',
  't1.c',
  't2.c',
  'tcd.c',
  'tgt.c',
  'thread.c',
)

openjp2_headers = files(
  'bio.h',
  'cio.h',
  'dwt.h',
  'event.h',
  'function_list.h',
  'image.h',
  'invert.h',
  'j2k.h',
  'jp2.h',
  'mct.h',
  'mqc.h',
  'mqc_inl.h',
  'openjpeg.h',
  'opj_clock.h',
  'opj_codec.h',
  'opj_includes.h',
  'opj_intmath.h',
  'opj_malloc.h',
  'pi.h',
  'sparse_array.h',
  't1.h',
  't2.h',
  'tcd.h',
  'tgt.h',
  'thread.h',
)

if get_option('build_jpip')
  add_project_arguments('-DUSE_JPIP', language: 'c')
  openjp2_srcs += files('cidx_manager.c', 'phix_manager.c', 'ppix_manager.c', 'thix_manager.c', 'tpix_manager.c')
  openjp2_headers += files('cidx_manager.h', 'indexbox_manager.h')
endif

opj_config = configuration_data()
opj_config.set('OPENJPEG_VERSION_MAJOR', openjpeg_version_major)
opj_config.set('OPENJPEG_VERSION_MINOR', openjpeg_version_minor)
opj_config.set('OPENJPEG_VERSION_BUILD', openjpeg_version_build)

opj_private_config = configuration_data()
check_headers = [
 'assert.h',
 'ctype.h',
 'dlfcn.h',
 'float.h',
 'inttypes.h',
 'malloc.h',
 'math.h',
 'memory.h',
 'stdarg.h',
 'stdint.h',
 'stdlib.h',
 'stdio.h',
 'strings.h',
 'string.h',
 'sys/stat.h',
 'sys/types.h',
 'time.h',
 'unistd.h',
 'winsock2.h',
]

foreach h : check_headers
  opj_private_config.set('HAVE_@0@'.format(h.underscorify().to_upper()), cc.has_header(h))
endforeach

foreach h : ['malloc.h']
  opj_private_config.set('OPJ_HAVE_@0@'.format(h.underscorify().to_upper()), cc.has_header(h))
endforeach

opj_private_config.set('OPJ_HAVE__ALIGNED_MALLOC', cc.has_function('_aligned_malloc', prefix: '#include <malloc.h>'))
opj_private_config.set('OPJ_HAVE_FSEEKO', cc.has_function('fseeko').to_string('ON', 'OFF'))
opj_private_config.set('OPJ_HAVE_MEMALIGN', cc.has_function('memalign', prefix: '#include <malloc.h>'))
opj_private_config.set('OPJ_HAVE_POSIX_MEMALIGN', cc.has_function('posix_memalign', prefix: '#include <stdlib.h>'))
opj_private_config.set('OPJ_BIG_ENDIAN', host_machine.endian() == 'big')
opj_private_config.set('PACKAGE_VERSION', meson.project_version())

#-----------------------------------------------------------------------------
# opj_config.h generation (1/2)
# Check if some include files are provided by the system
# These files are mandatory

# For the following files, we provide an alternative, they are not mandatory


# Enable Large file support
opj_config.set('OPJ_HAVE_LARGEFILES', 1)

configure_file(
  input: 'opj_config.h.cmake.in',
  output: 'opj_config.h',
  configuration: opj_config,
  format: 'cmake@',
  install_dir: get_option('includedir') / openjpeg_version_subdir,
)
configure_file(
  input: 'opj_config_private.h.cmake.in',
  output: 'opj_config_private.h',
  configuration: opj_private_config,
  format: 'cmake@',
)

inc_dirs = include_directories('.')

openjp2_c_args = [
  '-DNDEBUG',
  '-fstrict-aliasing',
  '-ffast-math',
  '-funroll-loops',
  '-fomit-frame-pointer',
  '-ffinite-math-only',
  '-Wall',
]

if get_option('opj_disable_tpsot_fix')
  openjp2_c_args += '-DOPJ_DISABLE_TPSOT_FIX'
endif

if get_option('build_luts_generator')
  t1_generate_luts_exe = executable('t1_generate_luts', 't1_generate_luts.c', dependencies: m_dep)
endif

#################################################################################
# threading configuration
#################################################################################
if not get_option('opj_use_thread')
  message('Use stub thread implementation')
  openjp2_c_args += '-DMUTEX_stub'
  thread_dep = dependency('', required: false)
elif host_system == 'windows'
  message('Use win32 thread implementation')
  openjp2_c_args += '-DMUTEX_win32'
  thread_dep = dependency('', required: false)
elif pthread_dep.found()
  message('Use pthread implementation')
  openjp2_c_args += '-DMUTEX_pthread'
  thread_dep = pthread_dep
else
  error('FATAL_ERROR: No thread library found and thread/mutex support is required by "opj_use_thread" option')
endif

open_jp2_deps = [m_dep, thread_dep]

# Build the library
openjp2_lib = library(
  'openjp2',
  openjp2_srcs,
  include_directories: inc_dirs,
  c_args: openjp2_c_args,
  install: true,
  dependencies: open_jp2_deps,
  soversion: '7',
  version: meson.project_version(),
)

libopenjp2_dep = declare_dependency(
  link_with: openjp2_lib,
  include_directories: inc_dirs,
  compile_args: opj_static_args,
)

install_headers(
  [
    'openjpeg.h',
  ],
  subdir: openjpeg_version_subdir,
)

if get_option('build_unit_tests')
  bench_dwt_exe = executable('bench_dwt', 'bench_dwt.c', dependencies: [libopenjp2_dep, m_dep, thread_dep])

  test_sparse_array_exe = executable(
    'test_sparse_array',
    'test_sparse_array.c',
    dependencies: [libopenjp2_dep, m_dep, thread_dep],
  )
endif
