###  GLFW examples
#@ Constants
ex_include = include_directories('../include', '../src', '../deps')
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
  'boing': [],
  'gears': [],
  'heightmap': [],
  'offscreen': [],
  'particles': [tinycthread, getopt],
  'sharing': [],
  'splitview': [],
  'triangle-opengl': [],
  'triangle-opengles': [],
  'wave': [],
  'windows': [],
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
