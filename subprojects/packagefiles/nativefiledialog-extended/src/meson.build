
inc_dirs = include_directories('include')

src_files = files('include/nfd.h', 'include/nfd.hpp')

install_subdir(
  'include',
  install_dir: get_option('includedir'),
)

deps = []
compile_args = []

if host_machine.system() == 'windows'
  src_files += files('nfd_win.cpp')
elif host_machine.system() == 'darwin'


  # For setting the filter list, macOS introduced allowedContentTypes in version 11.0 and deprecated allowedFileTypes in 12.0.
  # By default (set to ON), NFDe will use allowedContentTypes when targeting macOS >= 11.0.
  # Set this option to OFF to always use allowedFileTypes regardless of the target macOS version.
  # This is mainly needed for applications that are built on macOS >= 11.0 but should be able to run on lower versions
  # and should not be used otherwise.

  deps += dependency(
    'AppKit',
    required: true,
  )

  use_allowed_content_types_result = false

  use_allowed_content_types_feature = get_option('use_allowed_content_types')

  if use_allowed_content_types_feature.allowed()

    cpp = meson.get_compiler('cpp')

    macos_v11_or_higher = cpp.compiles(
      '''
        #include <Availability.h>
        #if !defined(__MAC_OS_X_VERSION_MIN_REQUIRED) || !defined(__MAC_11_0) || __MAC_OS_X_VERSION_MIN_REQUIRED < __MAC_11_0
        static_assert(false);
        #endif
        int main() { return 0; }
        ''',
    )

    if macos_v11_or_higher

      ufti_dep = dependency(
        'UniformTypeIdentifiers',
        required: false,
      )
      if not ufti_dep.found()
        if use_allowed_content_types_feature.enabled()
          error(
            'UniformTypeIdentifiers framework is not available even though we are targeting macOS >= 11.0',
          )
        endif
      else
        deps += ufti_dep
        use_allowed_content_types_result = true
      endif
    endif
  endif

  compile_args += ('-DNFD_MACOS_ALLOWEDCONTENTTYPES=' + (use_allowed_content_types_result ? '1' : '0')
)

  add_languages(
    'objc',
    native: false,
  )

  src_files += files('nfd_cocoa.m')


elif host_machine.system() == 'linux'

  # for Linux, we support GTK3 and xdg-desktop-portal
  use_xdg_portal_feature = get_option('xdg-desktop-portal')
  if use_xdg_portal_feature.auto()

    # in case of auto we prefer gtk3
    gtk3_dep = dependency(
      'gtk+-3.0',
      required: false,
    )

    if gtk3_dep.found()
      deps += gtk3_dep
      src_files += files('nfd_gtk.cpp')
    else
      deps += dependency(
        'dbus-1',
        required: true,
      )
      src_files += files('nfd_portal.cpp')
      compile_args += '-DNFD_PORTAL'
    endif

  elif use_xdg_portal_feature.disabled()
    deps += dependency(
      'gtk+-3.0',
      required: true,
    )
    src_files += files('nfd_gtk.cpp')
  else
    deps += dependency(
      'dbus-1',
      required: true,
    )
    src_files += files('nfd_portal.cpp')
    compile_args += '-DNFD_PORTAL'
  endif


  if get_option('append_extension_linux')
    compile_args += '-DNFD_APPEND_EXTENSION'
  endif

else
  error('not supported platform')
endif


private_compile_args = []
public_compile_args = []

if get_option('default_library') == 'shared'
  private_compile_args += '-DNFD_EXPORT'
  public_compile_args += '-DNFD_SHARED'
endif


nfde_lib = library(
  'nativefiledialog-extended',
  src_files,
  include_directories: inc_dirs,
  dependencies: deps,
  cpp_args: compile_args + private_compile_args,
  install: true,
)

nfde_dep = declare_dependency(
  include_directories: inc_dirs,
  version: meson.project_version(),
  link_with: nfde_lib,
  compile_args: compile_args + public_compile_args,
)
