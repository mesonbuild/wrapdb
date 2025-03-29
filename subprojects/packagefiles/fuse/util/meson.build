executable(
  'fusermount',
  'fusermount.c',
  '../lib/mount_util.c',
  include_directories: include_dirs,
  install: true,
)

#does not compile with glibc greater than 2.33
if cc.get_define(
  '__GLIBC_MINOR__',
  prefix: '#include <stdint.h>\n',
) < '34'
  executable(
    'ulockmgr_server',
    'ulockmgr_server.c',
    include_directories: include_dirs,
    install: true,
    dependencies: thread_dep,
  )
endif

executable(
  'mount.fuse',
  'mount.fuse.c',
  include_directories: include_dirs,
  link_with: libfuse,
  install: true,
  install_dir: get_option('sbindir'),
  c_args: '-DFUSE_USE_VERSION=26',
)


udevrulesdir = get_option('udevrulesdir')
if udevrulesdir == ''
  udev = dependency('udev')
  udevrulesdir = join_paths(udev.get_pkgconfig_variable('udevdir'), 'rules.d')
endif

# Unable to include the `install_helper.sh` from the fuse3 branch since it is
# not in the allowed files of `sanity_check.py`
#
# meson.add_install_script('install_helper.sh',
#                          join_paths(get_option('prefix'), get_option('sysconfdir')),
#                          join_paths(get_option('prefix'), get_option('bindir')),
#                          udevrulesdir,
#                          '@0@'.format(get_option('useroot')))
