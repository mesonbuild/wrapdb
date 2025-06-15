# This file is part of cairomm.

project(
  'cairomm',
  'cpp',
  version: '1.18.0',
  license: 'LGPL-2.0-or-later',
  default_options: ['cpp_std=c++17', 'warning_level=1'],
  meson_version: '>= 0.58.0',  # required for meson.add_dist_script(python3, ...)
  # and meson.add_install_script(python3, ...)
)

cairomm_api_version = '1.16'
cairomm_pcname = meson.project_name() + '-' + cairomm_api_version

cairomm_version_array = meson.project_version().split('.')
cairomm_major_version = cairomm_version_array[0].to_int()
cairomm_minor_version = cairomm_version_array[1].to_int()
cairomm_micro_version = cairomm_version_array[2].to_int()

# http://www.gnu.org/software/libtool/manual/html_node/Updating-version-info.html
# The relation between libtool's current:revison:age interface versioning
# and the .so filename, .so.x.y.z, is
# x = current - age
# y = age
# z = revision
# If libtool_soversion is updated as described in libtool's documentation,
# x.y.z will usually *not* be equal to meson.project_version().
libtool_soversion = [5, 0, 4]
cairomm_libversion = '@0@.@1@.@2@'.format(
  libtool_soversion[0] - libtool_soversion[2],
  libtool_soversion[2],
  libtool_soversion[1],
)
macos_darwin_versions = [
  libtool_soversion[0] + 1,
  '@0@.@1@'.format(libtool_soversion[0] + 1, libtool_soversion[1]),
]

# Use these instead of meson.source_root() and meson.build_root() in subdirectories.
# source_root() and build_root() are not useful, if this is a subproject.
project_source_root = meson.current_source_dir()
project_build_root = meson.current_build_dir()

cpp_compiler = meson.get_compiler('cpp')
cpp_compiler_id = cpp_compiler.get_id()
is_msvc = cpp_compiler_id == 'msvc' or cpp_compiler_id.endswith('-cl')
is_cl_impersonator = is_msvc and cpp_compiler_id != 'msvc'
python3 = find_program(
  'python3',
  version: '>=3.5',
)

# Do we build from a git repository?
# Suppose we do if and only if the meson.build file is tracked by git.
cmd_py = '''
import shutil, subprocess, sys
git_exe = shutil.which('git')
if not git_exe:
  sys.exit(1)
cmd = [ git_exe, 'ls-files', '--error-unmatch', 'meson.build' ]
sys.exit(subprocess.run(cmd, cwd=sys.argv[1], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode)
'''
is_git_build = run_command(
  python3,
  '-c',
  cmd_py,
  project_source_root,
  check: false,
).returncode() == 0

# Are we testing a dist tarball while it's being built?
# There ought to be a better way. https://github.com/mesonbuild/meson/issues/6866
is_dist_check = project_source_root.contains('dist-unpack') and \
  project_build_root.contains('dist-build')

# Options.
maintainer_mode_opt = get_option('maintainer-mode')
maintainer_mode = maintainer_mode_opt == 'true' or \
  (maintainer_mode_opt == 'if-git-build' and is_git_build)
if is_dist_check
  message('Looks like a tarball is being tested. ' + \
  'Option "dist-warnings" is used instead of "warnings".')
  cpp_warnings = get_option('dist-warnings')
else
  cpp_warnings = get_option('warnings')
endif
warning_level = get_option('warning_level').to_int()
werror = get_option('werror')
build_deprecated_api = get_option('build-deprecated-api')
build_exceptions_api = get_option('build-exceptions-api')
build_documentation_opt = get_option('build-documentation')
build_documentation = build_documentation_opt == 'true' or \
  (build_documentation_opt == 'if-maintainer-mode' and maintainer_mode)
build_examples = get_option('build-examples')
build_tests_opt = get_option('build-tests')

use_msvc14x_toolset_ver = get_option('msvc14x-parallel-installable')

# Installation directories are relative to {prefix}.
install_prefix = get_option('prefix')
install_includedir = get_option('includedir')
install_libdir = get_option('libdir')
install_datadir = get_option('datadir')
install_pkgconfigdir = install_libdir / 'pkgconfig'

# Dependencies.
# cairomm_build_dep: Dependencies when building the cairomm library.
# cairomm_dep (created in cairomm/meson.build):
#   Dependencies when using the cairomm library.
sigcxx_req = '>= 3.0.0'
cairo_req = '>= 1.14.0'

# There are pkg-config files for sigc++ on MSVC, so just use that.
sigcxx_dep = dependency(
  'sigc++-3.0',
  version: sigcxx_req,
)
cairo_dep = dependency(
  'cairo',
  version: cairo_req,
  required: meson.is_subproject() or not is_msvc,
)

# This is clearly on Windows...
if not cairo_dep.found()
  cairo_dep = cpp_compiler.find_library(
    'cairo',
    has_headers: ['cairo.h', 'cairo-win32.h'],
  )
endif

cairomm_build_dep = [sigcxx_dep, cairo_dep]
cairomm_requires = ['sigc++-3.0', sigcxx_req]

cairomm_extra_libs = ''
if cairo_dep.type_name() == 'pkgconfig'
  cairomm_requires += ['cairo', cairo_req]
else
  cairomm_extra_libs = '-lcairo'
endif
cairomm_requires = ' '.join(cairomm_requires)

if is_msvc and not is_cl_impersonator
  # We must have Visual Studio 2017 15.7 or later...
  assert(
    cpp_compiler.version().split('.')[0].to_int() >= 19 and \
  cpp_compiler.version().split('.')[1].to_int() >= 15,
    'Visual Studio 2017 15.7 or later is required',
  )
endif

# Needed for M_PI on Visual Studio and some MinGW versions
if host_machine.system() == 'windows'
  add_project_arguments(
    '-D_USE_MATH_DEFINES',
    language: 'cpp',
  )
endif

# Some dependencies are required only in maintainer mode and/or
# if documentation shall be built.
mm_common_get = find_program(
  'mm-common-get',
  required: false,
)

if maintainer_mode and not mm_common_get.found()
  message(
    'Maintainer mode requires the \'mm-common-get\' command. If it is not found,\n' + 'use \'-Dmaintainer-mode=false\' or install the \'mm-common\' package, version 1.0.0 or higher.',
  )
  # If meson --wrap-mode != forcefallback, Meson falls back to the mm-common
  # subproject only if mm-common-get is required.
  mm_common_get = find_program(
    'mm-common-get',
    required: true,
  )
endif

doxygen = find_program(
  'doxygen',
  required: build_documentation,
)
dot = find_program(
  'dot',
  required: build_documentation,
)  # Used by Doxygen
xsltproc = find_program(
  'xsltproc',
  required: build_documentation,
)

# Some dependencies are required only for building the test programs.
USE_SHARED_BOOST = get_option('boost-shared')  # Use shared Boost::Test?

boost_unit_test_framework_dep = dependency(
  'boost',
  modules: 'unit_test_framework',
  static: not USE_SHARED_BOOST,
  version: '>=1.63.0',
  required: false,
)

fontconfig_dep = dependency(
  'fontconfig',
  required: false,
)
test_dep = [boost_unit_test_framework_dep, fontconfig_dep]
can_test = boost_unit_test_framework_dep.found() and \
  (fontconfig_dep.found() or host_machine.system() == 'windows')
build_tests = build_tests_opt == 'true' or \
  (build_tests_opt == 'if-dependencies-found' and can_test)
if build_tests and not can_test
  error(
    'Building the test programs requires Boost Test, version 1.33.1 or higher and Fontconfig.\n' + \
  'Install them or use -Dbuild-tests=false or -Dbuild-tests=if-dependencies-found',
  )
endif

script_dir = project_source_root / 'untracked' / 'build_scripts'
doc_reference_py = script_dir / 'doc-reference.py'
dist_changelog_py = script_dir / 'dist-changelog.py'
dist_build_scripts_py = script_dir / 'dist-build-scripts.py'

if maintainer_mode
  # Copy files to untracked/build_scripts and untracked/docs.
  run_command(
    mm_common_get,
    '--force',
    script_dir,
    project_source_root / 'untracked' / 'docs',
    check: true,
  )
elif not import('fs').is_file(doc_reference_py)
  warning(
    'Missing files in untracked/.\n  ' + \
  'Enable maintainer-mode if you want to build documentation or create a dist tarball.',
  )
endif

# Check if perl is required and available.
doc_perl_prop = run_command(
  python3,
  doc_reference_py,
  'get_script_property',
  '',  # MMDOCTOOLDIR is not used
  'requires_perl',
  check: false,
)
if not (doc_perl_prop.returncode() == 0 and doc_perl_prop.stdout() == 'false')
  # Perl is required, if documentation shall be built.
  perl = find_program(
    'perl',
    required: build_documentation,
  )
endif

# Set compiler warnings.
# Meson warns if any of the /W1, /W2, /W3, /W4, /Wall, -Wall, -Wextra, -Werror
# compiler options are added with add_project_arguments().
# Avoid such warnings, when possible.
# See _warn_about_builtin_args() in meson/mesonbuild/interpreter/interpreter.py.
warning_flags = []
if cpp_warnings == 'min'
  if warning_level == 0
    warning_flags = is_msvc ? ['/W2'] : ['-Wall']
  endif
elif cpp_warnings == 'max' or cpp_warnings == 'fatal'
  if warning_level < 3
    warning_flags = is_msvc ? ['/W4'] : ['-pedantic', '-Wall', '-Wextra']
  endif
  if not is_msvc
    warning_flags += '-Wformat-security -Wsuggest-override -Wzero-as-null-pointer-constant'.split()
  endif
  if cpp_warnings == 'fatal'
    if not werror
      warning_flags += is_msvc ? ['/WX'] : ['-Werror']
    endif
    warning_flags += ['-DSIGCXX_DISABLE_DEPRECATED']
  endif
endif

warning_flags = cpp_compiler.get_supported_arguments(warning_flags)
add_project_arguments(
  warning_flags,
  language: 'cpp',
)

# Add toolset version in builds done with Visual Studio 2017 or later
msvc14x_toolset_ver = ''

# MSVC: Ignore warnings that aren't really harmful, but make those
#       that should not be overlooked stand out.
if is_msvc
  disable_warnings_list = [
    '/EHsc',  # avoid warnings caused by exception handling model used
    '/utf-8',  # Avoid C4819 unicode conversion warnings when building on CJK locales
    '/wd4800',  # Implicit conversion from 'type' to bool. Possible information loss
  ]

  # Turn off harmless warnings but make potentially dangerous ones glaring,
  # distributed with GLib, if available
  use_recommended_pragmas = cpp_compiler.get_supported_arguments(
    '/FImsvc_recommended_pragmas.h',
  )
  if use_recommended_pragmas.length() > 0
    add_project_arguments(
      use_recommended_pragmas,
      language: 'cpp',
    )
  else
    disable_warnings_list += [
      '/wd4244',  # 'conversion' conversion from 'type1' to 'type2', possible loss of data
      '/wd4101',  # unreferenced local variable
    ]
  endif

  if host_machine.cpu_family() == 'x86_64' or host_machine.cpu_family() == 'aarch64'
    # 'var' : conversion from 'size_t' to 'type', possible loss of data (applies on 64-bit builds)
    disable_warnings_list += '/wd4267'
  endif

  add_project_arguments(
    cpp_compiler.get_supported_arguments(disable_warnings_list),
    language: 'cpp',
  )
  if use_msvc14x_toolset_ver
    if cpp_compiler.version().version_compare('>=19.30')
      msvc14x_toolset_ver = '-vc143'
    elif cpp_compiler.version().version_compare('>=19.20')
      msvc14x_toolset_ver = '-vc142'
    elif cpp_compiler.version().version_compare('>=19.10')
      msvc14x_toolset_ver = '-vc141'
    endif
  endif
endif

cairomm_libname = meson.project_name() + msvc14x_toolset_ver + '-' + cairomm_api_version

# Create cairommconfig.h.
mm_conf_data = configuration_data()
if not build_deprecated_api
  mm_conf_data.set('CAIROMM_DISABLE_DEPRECATED', 1)
endif
if build_exceptions_api
  mm_conf_data.set('CAIROMM_EXCEPTIONS_ENABLED', 1)
endif
mm_conf_data.set('CAIROMM_MAJOR_VERSION', cairomm_major_version)
mm_conf_data.set('CAIROMM_MINOR_VERSION', cairomm_minor_version)
mm_conf_data.set('CAIROMM_MICRO_VERSION', cairomm_micro_version)
mm_conf_data.set('VERSION', meson.project_version())  # for MSVC_NMake/cairomm/cairomm.rc

cairommconfig_h_meson = files('cairommconfig.h.meson')
install_includeconfigdir = install_libdir / cairomm_pcname / 'include'
configure_file(
  input: cairommconfig_h_meson,
  output: 'cairommconfig.h',
  configuration: mm_conf_data,
  install_dir: install_includeconfigdir,
)

# add_dist_script() is not allowed in a subproject if meson.version() < 0.58.0.
can_add_dist_script = not meson.is_subproject() or meson.version().version_compare(
  '>= 0.58.0',
)

subdir('MSVC_NMake/cairomm')
subdir('data')
subdir('cairomm')
subdir('examples')
subdir('tests')
subdir('docs/reference')

if can_add_dist_script
  # Add a ChangeLog file to the distribution directory.
  meson.add_dist_script(python3, dist_changelog_py, project_source_root)
  # Don't distribute these files and directories.
  dont_distribute = ['tools', '.gitlab-ci.yml', 'examples/Makefile.am_fragment']

  # Add build scripts to the distribution directory, and delete .gitignore
  # files and an empty $MESON_PROJECT_DIST_ROOT/build/ directory.
  meson.add_dist_script(
    python3,
    dist_build_scripts_py,
    project_source_root,
    'untracked' / 'build_scripts',
    dont_distribute,
  )
endif

if meson.is_subproject()
  pkgconfig_vars = {
    'htmlrefdir': install_prefix / install_docdir / 'reference' / 'html',
    'htmlrefpub': 'http://www.cairographics.org/documentation/cairomm/reference',
  }
  if build_documentation
    pkgconfig_vars += {
      'doxytagfile': tag_file.full_path(),
    }
    # May be used in a main project.
    global_tag_file_target = tag_file
  endif
  cairomm_dep = declare_dependency(
    dependencies: cairomm_own_dep,
    variables: pkgconfig_vars,
  )

  # A main project that looks for cairomm_pcname.pc shall find cairomm_dep.
  meson.override_dependency(cairomm_pcname, cairomm_dep)
endif

# Print a summary.
real_maintainer_mode = ''
if maintainer_mode_opt == 'if-git-build'
  real_maintainer_mode = ' (@0@)'.format(maintainer_mode)
endif

real_build_documentation = ''
if build_documentation_opt == 'if-maintainer-mode'
  real_build_documentation = ' (@0@)'.format(build_documentation)
endif

real_build_tests = ''
if build_tests_opt == 'if-dependencies-found'
  real_build_tests = ' (@0@)'.format(build_tests)
endif

summary = [
  '',
  '------',
  meson.project_name() + ' ' + meson.project_version(),
  '',
  '         Maintainer mode: @0@@1@'.format(
    maintainer_mode_opt,
    real_maintainer_mode,
  ),
  '       Compiler warnings: @0@ (warning_level: @1@, werror: @2@)'. \
  format(cpp_warnings, warning_level, werror),
  '    Build deprecated API: @0@'.format(build_deprecated_api),
  'Build HTML documentation: @0@@1@'.format(
    build_documentation_opt,
    real_build_documentation,
  ),
  '  Build example programs: @0@'.format(build_examples),
  '     Build test programs: @0@@1@'.format(build_tests_opt, real_build_tests),
  '   Use shared Boost Test: @0@'.format(USE_SHARED_BOOST),
  'Directories:',
  '                  prefix: @0@'.format(install_prefix),
  '              includedir: @0@'.format(install_prefix / install_includedir),
  '       includecairommdir: @0@'.format(
    install_prefix / install_includedir / cairomm_pcname,
  ),
  '                  libdir: @0@'.format(install_prefix / install_libdir),
  '        includeconfigdir: @0@'.format(
    install_prefix / install_includeconfigdir,
  ),
  '            pkgconfigdir: @0@'.format(install_prefix / install_pkgconfigdir),
  '                 datadir: @0@'.format(install_prefix / install_datadir),
  '                  docdir: @0@'.format(install_prefix / install_docdir),
  '              devhelpdir: @0@'.format(install_prefix / install_devhelpdir),
  '------',
]

message('\n'.join(summary))
