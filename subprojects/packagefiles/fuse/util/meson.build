executable('fusermount', ['fusermount.c', '../lib/mount_util.c'],
           include_directories: include_dirs,
           install: true,
           install_dir: get_option('bindir')
          )

executable('ulockmgr_server', ['ulockmgr_server.c'],
           include_directories: include_dirs,
           install: true,
           dependencies: [dependency('threads')],
           install_dir: get_option('bindir')
          )

executable('mount.fuse', ['mount.fuse.c'],
           include_directories: include_dirs,
           link_with: [ libfuse ],
           install: true,
           install_dir: get_option('sbindir'),
           c_args: '-DFUSE_USE_VERSION=26')


udevrulesdir = get_option('udevrulesdir')
if udevrulesdir == ''
  udev = dependency('udev')
  udevrulesdir = join_paths(udev.get_pkgconfig_variable('udevdir'), 'rules.d')
endif

meson.add_install_script('install_helper.sh',
                         join_paths(get_option('prefix'), get_option('sysconfdir')),
                         join_paths(get_option('prefix'), get_option('bindir')),
                         udevrulesdir,
                         '@0@'.format(get_option('useroot')))


