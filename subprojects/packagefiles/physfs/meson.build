project(
  'physfs',
  'c',
  version: '3.2.0',
  meson_version: '>=0.54.0',
  default_options: ['c_std=gnu99'],
)

feature_args = []
public_args = []

if get_option('default_library') == 'static'
  public_args += '-DPHYSFS_STATIC'
endif

# Files that don't correspond to configurable archivers
sources = files(
  'src/physfs.c',
  'src/physfs_archiver_dir.c',
  'src/physfs_archiver_unpacked.c',
  'src/physfs_byteorder.c',
  'src/physfs_platform_android.c',
  'src/physfs_platform_os2.c',
  'src/physfs_platform_posix.c',
  'src/physfs_platform_qnx.c',
  'src/physfs_platform_unix.c',
  'src/physfs_platform_windows.c',
  'src/physfs_unicode.c',
)

deps = [dependency('threads')]

if host_machine.system() == 'darwin'
  add_languages(
    'objc',
    native: false,
  )
  sources += files('src/physfs_platform_apple.m')
  deps += dependency(
    'appleframeworks',
    modules: ['IOKit', 'Foundation'],
  )
elif host_machine.system() == 'haiku'
  add_languages(
    'cpp',
    native: false,
  )
  sources += files('src/physfs_platform_haiku.cpp')
  deps += [dependency('be'), dependency('root')]
endif

# Values are defaults (for auto feature value)
archivers = {
  'zip'     : true,
  '7z'      : true,
  'grp'     : false,
  'wad'     : false,
  'hog'     : false,
  'mvl'     : false,
  'qpak'    : false,
  'slb'     : false,
  'iso9660' : false,
  'vdf'     : false,
}

foreach archiver, default_value : archivers
  sources += files('src/physfs_archiver_@0@.c'.format(archiver))
  archiver_opt = get_option(archiver)
  is_enabled = archiver_opt.auto() ? default_value : archiver_opt.enabled()
  feature_args += '-DPHYSFS_SUPPORTS_@0@=@1@'.format(
    archiver.to_upper(),
    is_enabled.to_int(),
  )
  summary(
    archiver,
    is_enabled.to_string('enabled', 'disabled'),
    section: 'Archive support',
  )
endforeach

full_library_args = [feature_args, public_args]

physfs_lib = library(
  'physfs',
  sources,
  c_args: full_library_args,
  cpp_args: full_library_args,
  objc_args: full_library_args,
  dependencies: deps,
  gnu_symbol_visibility: 'hidden',
)

depinc = include_directories('src')
physfs_dep = declare_dependency(
  include_directories: depinc,
  link_with: physfs_lib,
  compile_args: public_args,
)
