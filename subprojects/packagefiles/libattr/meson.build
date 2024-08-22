project(
  'attr',
  'c',
  version: '2.5.1',
  default_options: ['warning_level=3'],
)

add_project_arguments(
  '-DSYSCONFDIR="@0@"'.format(get_option('prefix') / get_option('sysconfdir')),
  '-DLOCALEDIR="@0@"'.format(get_option('prefix') / get_option('localedir')),
  language: 'c',
)

cdata = configuration_data()
cfile = configure_file(
  configuration: cdata,
  output: 'config.h',
)

cc = meson.get_compiler('c')

gnu_sym_ldflag = '-Wl,--version-script,@0@/exports'.format(meson.current_source_dir())
link_args = []
if get_option('default_library') != 'static' and cc.links('', name: '-Wl,--version-script', args: ['-shared', gnu_sym_ldflag])
  link_args += gnu_sym_ldflag
endif

incdirs = include_directories('include')

libattr = library(
  'attr',
  'libattr/attr_copy_action.c',
  'libattr/attr_copy_check.c',
  'libattr/attr_copy_fd.c',
  'libattr/attr_copy_file.c',
  'libattr/libattr.c',
  'libattr/syscalls.c',
  include_directories: incdirs,
  install: true,
  link_args: link_args,
)


libattr_dep = declare_dependency(
  include_directories: incdirs,
  link_with: libattr,
)
