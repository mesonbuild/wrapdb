# Headers file are located here:
inc_dirs = include_directories('../../lib/openjp2', '../common', '../jp2', '../../lib/openjpip')

# Tool to embed metadata into JP2 file
opj_jpip_addxml_exe = executable(
  'opj_jpip_addxml',
  'opj_jpip_addxml.c',
  install: true,
)

# Install exe
if get_option('build_jpip_server')
  opj_server_srcs = 'opj_server.c'
  # Build executable
  opj_server_exe = executable('opj_server', opj_server_srcs, dependencies: m_dep, install: true)
endif

# Loop over all executables:
foreach exe : ['opj_dec_server', 'opj_jpip_transcode', 'opj_jpip_test']
  exe_c = exe + '.c'
  exe_c_args = []
  exe_src = exe_c + common_srcs
  exe_deps = [libopenjpip_dep, rt_dep, m_dep]
  exe_exe = executable(exe, exe_src, c_args: exe_c_args, dependencies: exe_deps, install: true)
endforeach
