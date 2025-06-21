project(
  'wren',
  'c',
  version: '0.4.0',
  license: 'mit',
)

cc = meson.get_compiler('c')

sources = [
  'src/vm/wren_compiler.c',
  'src/vm/wren_core.c',
  'src/vm/wren_debug.c',
  'src/vm/wren_primitive.c',
  'src/vm/wren_utils.c',
  'src/vm/wren_value.c',
  'src/vm/wren_vm.c',
  'src/optional/wren_opt_meta.c',
  'src/optional/wren_opt_random.c',
]

c_args = []

if get_option('meta').disabled()
  c_args += '-DWREN_OPT_META=0'
endif

if get_option('random').disabled()
  c_args += '-DWREN_OPT_RANDOM=0'
endif

system_deps = [
  cc.find_library(
    'm',
    required: false,
  ),
]

incdir = include_directories('src/vm', 'src/optional', 'src/include')

wrenlib = library(
  'wren',
  sources,
  dependencies: system_deps,
  include_directories: incdir,
  c_args: c_args,
)

headerdir = include_directories('src/include')

wren_dep = declare_dependency(
  link_with: wrenlib,
  include_directories: headerdir,
)
