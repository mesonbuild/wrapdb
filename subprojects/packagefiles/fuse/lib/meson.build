libfuse_sources = files(
  'buffer.c',
  'cuse_lowlevel.c',
  'fuse.c',
  'fuse_kern_chan.c',
  'fuse_loop.c',
  'fuse_loop_mt.c',
  'fuse_lowlevel.c',
  'fuse_misc.h',
  'fuse_mt.c',
  'fuse_opt.c',
  'fuse_session.c',
  'fuse_signals.c',
  'helper.c',
  'modules/subdir.c',
)

libfuse_sources += host_machine.system() == 'linux' ? files(
  'mount.c',
  'mount_util.c',
) : files(
  'mount_bsd.c',
)

deps = [thread_dep]
if cfg.get('HAVE_ICONV')
  libfuse_sources += files('modules/iconv.c')
  deps += iconv_dep
endif

if meson.version().version_compare('>= 0.62')
  deps += dependency('dl')
else
  libdl = cc.find_library(
    'dl',
    required: false,
  )
  if libdl.found()
    deps += libdl
  endif
endif

if host_machine.system().startswith('netbsd')
  deps += cc.find_library('perfuse')
  deps += cc.find_library('puffs')
else
  # Required for clock_gettime before glibc 2.17
  deps += cc.find_library('rt')
endif

fusermount_path = join_paths(get_option('prefix'), get_option('bindir'))
libfuse = library(
  'fuse',
  libfuse_sources,
  version: meson.project_version(),
  include_directories: include_dirs,
  dependencies: deps,
  install: true,
  link_depends: 'fuse_versionscript',
  c_args: [
    '-DFUSE_USE_VERSION=26',
    '-DFUSERMOUNT_DIR="@0@"'.format(fusermount_path),
  ],
  link_args: [
    '-Wl,--version-script,' + meson.current_source_dir() + '/fuse_versionscript',
  ],
)

pkg = import('pkgconfig')
pkg.generate(
  libfuse,
  description: 'Filesystem in Userspace',
  subdirs: 'fuse',
)

libfuse_dep = declare_dependency(
  include_directories: include_dirs,
  link_with: libfuse,
  dependencies: deps,
)
