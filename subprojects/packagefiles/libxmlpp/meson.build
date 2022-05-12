# This file is part of libxml++.

project('libxml++', 'cpp',
  version: '5.0.1',
  license: 'LGPLv2.1+',
  default_options: [
    'warning_level=1',
    'cpp_std=c++17'
  ],
  meson_version: '>= 0.55.0', # required for meson.override_dependency()
                              # and dep.get_variable(internal:)
)

xmlxx_api_version = '5.0'
xmlxx_pcname = meson.project_name() + '-' + xmlxx_api_version

xmlxx_version_array = meson.project_version().split('.')
xmlxx_major_version = xmlxx_version_array[0].to_int()
xmlxx_minor_version = xmlxx_version_array[1].to_int()
xmlxx_micro_version = xmlxx_version_array[2].to_int()

# http://www.gnu.org/software/libtool/manual/html_node/Updating-version-info.html
# The relation between libtool's current:revison:age interface versioning
# and the .so filename, .so.x.y.z, is
# x = current - age
# y = age
# z = revision
# If libtool_soversion is updated as described in libtool's documentation,
# x.y.z will usually *not* be equal to meson.project_version().
libtool_soversion = [1, 0, 0]
xmlxx_libversion = '@0@.@1@.@2@'.format(
  libtool_soversion[0] - libtool_soversion[2],
  libtool_soversion[2],
  libtool_soversion[1]
)
macos_darwin_versions = [
  libtool_soversion[0] + 1,
  '@0@.@1@'.format(libtool_soversion[0] + 1, libtool_soversion[1])
]

# Use these instead of meson.source_root() and meson.build_root() in subdirectories.
# source_root() and build_root() are not useful, if this is a subproject.
project_source_root = meson.current_source_dir()
project_build_root = meson.current_build_dir()

cpp_compiler = meson.get_compiler('cpp')
is_msvc = cpp_compiler.get_id() == 'msvc'
python3 = import('python').find_installation('python3')

python_version = python3.language_version()
python_version_req = '>= 3.5'
if not python_version.version_compare(python_version_req)
  error('Requires Python @0@, found @1@.'.format(python_version_req, python_version))
endif

# Do we build from a git repository?
# Suppose we do if and only if a '.git' directory or file exists.
cmd_py = '''
import os
import sys
sys.exit(os.path.isdir("@0@") or os.path.isfile("@0@"))
'''.format(project_source_root / '.git')
is_git_build = run_command(python3, '-c', cmd_py, check : false).returncode() != 0

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
  warning_level = get_option('dist-warnings')
else
  warning_level = get_option('warnings')
endif
build_deprecated_api = get_option('build-deprecated-api')
build_documentation_opt = get_option('build-documentation')
build_documentation = build_documentation_opt == 'true' or \
                     (build_documentation_opt == 'if-maintainer-mode' and maintainer_mode)
build_examples = get_option('build-examples')
build_tests = get_option('build-tests')
use_msvc14x_toolset_ver = get_option('msvc14x-parallel-installable')

# Installation directories are relative to {prefix}.
install_prefix = get_option('prefix')
install_includedir = get_option('includedir')
install_libdir = get_option('libdir')
install_datadir = get_option('datadir')
install_pkgconfigdir = install_libdir / 'pkgconfig'

# Dependencies.
# xmlxx_build_dep: Dependencies when building the libxml++ library.
# xmlxx_dep (created in libxml++/meson.build):
#   Dependencies when using the libxml++ library.

# libxml2's Windows-specific Makefiles don't create pkg-config files for us, so
# we may need to look for it manually on Windows
xml2_min_ver = '2.7.7'
xml2_req = '>= @0@'.format(xml2_min_ver)
xml2_dep = dependency('libxml-2.0', version: xml2_req)

if not xml2_dep.found()
  libxml2_lib = 'libxml2'
  xml2_dep =  cpp_compiler.find_library(libxml2_lib,
                                        has_headers: [
                                          'libxml/globals.h',
                                          'libxml/parser.h',
                                          'libxml/parserInternals.h',
                                          'libxml/relaxng.h',
                                          'libxml/tree.h',
                                          'libxml/xinclude.h',
                                          'libxml/xpath.h',
                                          'libxml/xpathInternals.h',
                                          'libxml/xmlerror.h',
                                          'libxml/xmlIO.h',
                                          'libxml/xmlreader.h',
                                          'libxml/xmlschemas.h',
                                        ])

  xml_min_ver_split = xml2_min_ver.split('.')
  xml_min_ver_int = xml_min_ver_split[0].to_int() * 10000 + \
                    xml_min_ver_split[1].to_int() * 100 + \
                    xml_min_ver_split[2].to_int()

  if not cpp_compiler.compiles('''#include <libxml/tree.h>
                                  #if LIBXML_VERSION < @0@
                                  # error libxml2 versions must be @1@ or later
                                  #endif'''.format(xml_min_ver_int.to_string(), xml2_min_ver),
                                  name : 'libxml2 is @0@ or later'.format(xml2_min_ver))
    error('Your libxml2 installation must be @0@ or later'.format(xml2_min_ver))
  endif
endif

xmlxx_requires = []
libxml2_lib_pkgconfig = ''

xmlxx_requires += ['libxml-2.0', xml2_req]
xmlxx_requires = ' '.join(xmlxx_requires)

# Make sure we link to libxml-2.0
xmlxx_build_dep = [xml2_dep]

# Some dependencies are required only in maintainer mode and/or if
# reference documentation shall be built.
mm_common_get = find_program('mm-common-get', required: false)
if maintainer_mode and not mm_common_get.found()
  message('Maintainer mode requires the \'mm-common-get\' command. If it is not found,\n' +
          'use \'-Dmaintainer-mode=false\' or install the \'mm-common\' package, version 1.0.0 or higher.')
  # If meson --wrap-mode != forcefallback, Meson falls back to the mm-common
  # subproject only if mm-common-get is required.
  mm_common_get = find_program('mm-common-get', required: true)
endif
perl = find_program('perl', required: build_documentation)
doxygen = find_program('doxygen', required: build_documentation)
dot = find_program('dot', required: build_documentation) # Used by Doxygen
xsltproc = find_program('xsltproc', required: build_documentation)

# Script files copied to 'untracked/' by mm-common-get.
script_dir = project_source_root / 'untracked' / 'build_scripts'
doc_reference_py = script_dir / 'doc-reference.py'
dist_changelog_py = script_dir / 'dist-changelog.py'
dist_build_scripts_py = script_dir / 'dist-build-scripts.py'

if maintainer_mode
  # Copy files to untracked/build_scripts and untracked/docs.
  run_command(mm_common_get, '--force', script_dir,
    project_source_root / 'untracked' / 'docs', check : false)
else
  cmd_py = '''
import os
import sys
sys.exit(os.path.isfile("@0@"))
'''.format(doc_reference_py)
  file_exists = run_command(python3, '-c', cmd_py, check : false).returncode() != 0
  if not file_exists
    warning('Missing files in untracked/. ' + \
      'Enable maintainer-mode if you want to build documentation or create a dist tarball.')
  endif
endif

# xmlxx's own script files.
xmlxx_script_dir = project_source_root / 'tools' / 'build_scripts'
tutorial_custom_cmd_py = xmlxx_script_dir / 'tutorial-custom-cmd.py'

# Add toolset version in builds done with Visual Studio 2017 or later
msvc14x_toolset_ver = ''

if is_msvc
  add_project_arguments(cpp_compiler.get_supported_arguments([ '/utf-8', '/wd4828']), language: 'cpp')

  if use_msvc14x_toolset_ver
    if cpp_compiler.version().version_compare('>=19.20')
      msvc14x_toolset_ver = '-vc142'
    elif cpp_compiler.version().version_compare('>=19.10')
      msvc14x_toolset_ver = '-vc141'
    endif
  endif
endif

xmlxx_libname = 'xml++' + msvc14x_toolset_ver + '-' + xmlxx_api_version

# Set compiler warnings.
warning_flags = []
if warning_level == 'max' or warning_level == 'fatal'
  if is_msvc
    warning_flags = ['/W4']
  else
    warning_flags = '-pedantic -Wall -Wextra -Wformat-security -Wsuggest-override -Wshadow -Wno-long-long'.split()
  endif
  if warning_level == 'fatal'
    if is_msvc
      warning_flags += ['/WX']
    else
      warning_flags += ['-Werror']
    endif
  endif
endif

warning_flags = cpp_compiler.get_supported_arguments(warning_flags)
add_project_arguments(warning_flags, language: 'cpp')

# MSVC: Ignore warnings that aren't really harmful, but make those
#       that should not be overlooked stand out.
if is_msvc
  foreach wd : ['/FImsvc_recommended_pragmas.h', '/wd4267', '/EHsc' ]
    disabled_warning = cpp_compiler.get_supported_arguments(wd)
    add_project_arguments(disabled_warning, language: 'cpp')
  endforeach
endif

# Configure files
pkg_conf_data = configuration_data()
pkg_conf_data.set('prefix', install_prefix)
pkg_conf_data.set('exec_prefix', '${prefix}')
pkg_conf_data.set('libdir', '${exec_prefix}' / install_libdir)
pkg_conf_data.set('datarootdir', '${prefix}' / install_datadir)
pkg_conf_data.set('datadir', '${datarootdir}')
pkg_conf_data.set('includedir', '${prefix}' / install_includedir)
pkg_conf_data.set('PACKAGE_NAME', meson.project_name()) # MSVC_NMake/libxml++/libxml++.rc
pkg_conf_data.set('PACKAGE_TARNAME', meson.project_name())
pkg_conf_data.set('PACKAGE_VERSION', meson.project_version())
pkg_conf_data.set('LIBXMLXX_MODULE_NAME', xmlxx_pcname)
pkg_conf_data.set('LIBXMLXX_API_VERSION', xmlxx_api_version)
pkg_conf_data.set('LIBXMLXX_MODULES', xmlxx_requires)
pkg_conf_data.set('LIBXML2_LIB_NO_PKGCONFIG', libxml2_lib_pkgconfig)
pkg_conf_data.set('MSVC_TOOLSET_VER', msvc14x_toolset_ver)

if not build_deprecated_api
  pkg_conf_data.set('LIBXMLXX_DISABLE_DEPRECATED', 1)
endif
pkg_conf_data.set('LIBXMLXX_MAJOR_VERSION', xmlxx_major_version)
pkg_conf_data.set('LIBXMLXX_MINOR_VERSION', xmlxx_minor_version)
pkg_conf_data.set('LIBXMLXX_MICRO_VERSION', xmlxx_micro_version)

# Configuration test
if cpp_compiler.compiles(files('tools' / 'conf_tests' / 'have_exception_ptr.cc'))
  pkg_conf_data.set('LIBXMLXX_HAVE_EXCEPTION_PTR', 1)
endif

# Static library?
library_build_type = get_option('default_library')

if cpp_compiler.get_argument_syntax() == 'msvc'
  if library_build_type == 'static' or library_build_type == 'both'
    error('Static builds are not supported by MSVC-style builds')
  endif
endif

configure_file(
  input: 'libxml++.pc.in',
  output: xmlxx_pcname + '.pc',
  configuration: pkg_conf_data,
  install_dir: install_pkgconfigdir,
)

install_includeconfigdir = install_libdir / xmlxx_pcname / 'include'
xmlxxconfig_h = configure_file(
  input: 'libxml++config.h.meson',
  output: 'libxml++config.h',
  configuration: pkg_conf_data,
  install_dir: install_includeconfigdir,
)

# add_dist_script() is not allowed in a subproject if meson.version() < 0.58.0.
can_add_dist_script = not meson.is_subproject()

subdir('MSVC_NMake/libxml++')
subdir('libxml++')
subdir('examples')
subdir('tests')
subdir('docs/reference')
subdir('docs/manual')

if can_add_dist_script
  # Add a ChangeLog file to the distribution directory.
  meson.add_dist_script(
    python3.path(), dist_changelog_py,
    project_source_root,
  )
  # Add build scripts to the distribution directory, and delete .gitignore
  # files and an empty $MESON_PROJECT_DIST_ROOT/build/ directory.
  meson.add_dist_script(
    python3.path(), dist_build_scripts_py,
    project_source_root,
    'untracked' / 'build_scripts',
  )
endif

if meson.is_subproject()
  pkgconfig_vars = {
    'htmlrefdir': install_prefix / install_docdir / 'reference' / 'html',
    'htmlrefpub': 'http://library.gnome.org/devel/libxml++/unstable/'
  }
  if build_documentation
    pkgconfig_vars += {'doxytagfile': tag_file.full_path()}
    # May be used in a main project.
    global_tag_file_target = tag_file
  endif
  xmlxx_dep = declare_dependency(
    dependencies: xmlxx_own_dep,
    variables: pkgconfig_vars,
  )

  # A main project that looks for xmlxx_pcname.pc shall find xmlxx_dep.
  meson.override_dependency(xmlxx_pcname, xmlxx_dep)
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

validate = get_option('validation') and can_parse_and_validate
explain_val = ''
if get_option('validation') and not validate
  explain_val = ' (requires xmllint)'
endif

build_pdf = build_pdf_by_default and can_build_pdf
explain_pdf = ''
if build_pdf_by_default and not build_pdf
  explain_pdf = ' (requires dblatex or (xmllint and docbook2pdf))'
endif

summary = [
  '',
  '------',
  meson.project_name() + ' ' + meson.project_version(),
  '',
  '         Maintainer mode: @0@@1@'.format(maintainer_mode_opt, real_maintainer_mode),
  '       Compiler warnings: @0@'.format(warning_level),
  '    Build deprecated API: @0@'.format(build_deprecated_api),
  'Build HTML documentation: @0@@1@'.format(build_documentation_opt, real_build_documentation),
  '          XML validation: @0@@1@'.format(validate, explain_val),
  '               Build PDF: @0@@1@'.format(build_pdf, explain_pdf),
  '  Build example programs: @0@'.format(build_examples),
  '     Build test programs: @0@'.format(build_tests),
  'Directories:',
  '                  prefix: @0@'.format(install_prefix),
  '              includedir: @0@'.format(install_prefix / install_includedir),
  '         includexmlxxdir: @0@'.format(install_prefix / install_includedir / xmlxx_pcname),
  '                  libdir: @0@'.format(install_prefix / install_libdir),
  '        includeconfigdir: @0@'.format(install_prefix / install_includeconfigdir),
  '            pkgconfigdir: @0@'.format(install_prefix / install_pkgconfigdir),
  '                 datadir: @0@'.format(install_prefix / install_datadir),
  '                  docdir: @0@'.format(install_prefix / install_docdir),
  '              devhelpdir: @0@'.format(install_prefix / install_devhelpdir),
  '             tutorialdir: @0@'.format(install_prefix / install_tutorialdir),
  '------',
]

message('\n'.join(summary))
