project(
  'tclap',
  'cpp',
  version: '1.2.4',
  license: 'MIT',
)

# This is a minimum meson.build to use TCLAP.
# TODO: Full porting from autotools remains to be done.


# --
# Library (Main Dependency)
# --

tclap_dep = declare_dependency(
  version: '1.2.4',
  include_directories: 'include',
)

# --
# Examples
# --

subdir('examples')

# --
# Tests
# --

subdir('tests')


