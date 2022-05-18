###  GLFW test programs
#@ Constants
tst_include = include_directories('../include', '../src', '../deps')
glad_gl = '../deps/glad_gl.c'
glad_vulkan = '../deps/glad_vulkan.c'
getopt = '../deps/getopt.c'
tinycthread = '../deps/tinycthread.c'

#@ Flags
c_flags = []
if is_posix
  c_flags += '-D_XOPEN_SOURCE=700'
endif
if host_machine.system() == 'darwin'
  c_flags += '-D_DARWIN_C_SOURCE'
endif

#@ Test executables
tests = [['clipboard', [getopt, glad_gl]],
         ['events', [getopt, glad_gl]],
         ['msaa', [getopt, glad_gl]],
         ['glfwinfo', [getopt, glad_gl, glad_vulkan]],
         ['iconify', [getopt, glad_gl]],
         ['monitors', [getopt, glad_gl]],
         ['reopen', glad_gl],
         ['cursor', glad_gl],
         ['empty', [tinycthread, glad_gl]],
         ['gamma', glad_gl],
         ['icon', glad_gl],
         ['inputlag', [getopt, glad_gl]],
         ['joysticks', glad_gl],
         ['opacity', glad_gl],
         ['tearing', glad_gl],
         ['threads', [tinycthread, glad_gl]],
         ['timeout', glad_gl],
         ['title', glad_gl],
         ['triangle-vulkan', glad_vulkan],
         ['windows', [getopt, glad_gl]]]
foreach t : tests
  name = t[0]
  src = [t[0] + '.c', t[1]]
  executable(name, src,
             include_directories : tst_include,
             c_args : c_flags,
             dependencies : [glfw_dep, deps],
             build_by_default : true,
             install : get_option('install'),
             install_dir : opt_libdir / 'GLFW' / 'tests')
endforeach
