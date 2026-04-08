project(
  'tclap',
  'cpp',
  version: '1.2.5',
  license: 'MIT',
  meson_version: '>=0.56.0',
)

# This is a minimum meson.build to use TCLAP.
# TODO: Full porting from autotools remains to be done.


# --
# Library (Main Dependency)
# --

tclap_dep = declare_dependency(
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


