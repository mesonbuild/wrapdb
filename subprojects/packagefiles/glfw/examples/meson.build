###  GLFW examples
#@ Constants
ex_include = include_directories('../include', '../src', '../deps')
glad_gl = '../deps/glad_gl.c'
getopt = '../deps/getopt.c'
tinycthread = '../deps/tinycthread.c'

#@ Flags
c_flags = []
if is_posix
  c_flags += '-D_XOPEN_SOURCE=700'
endif
if sys_os == 'darwin'
  c_flags += '-D_DARWIN_C_SOURCE'
endif
if sys_os == 'windows' and sys_cc.get_argument_syntax() == 'gcc'
  c_flags += '-D_USE_MATH_DEFINES'
endif

#@ Example executables
examples = {
  'offscreen': glad_gl,
  'boing': glad_gl,
  'gears': glad_gl,
  'heightmap': glad_gl,
  'particles': [tinycthread, getopt, glad_gl],
  'sharing': glad_gl,
  'simple': glad_gl,
  'splitview': glad_gl,
  'wave': glad_gl,
}
foreach name, dep : examples
  src = [name + '.c', dep]
  executable(
    name,
    src,
    include_directories: ex_include,
    c_args: c_flags,
    dependencies: [glfw_dep, deps],
    build_by_default: true,
    install: get_option('install'),
    install_dir: opt_libdir / 'GLFW' / 'examples',
  )
endforeach
