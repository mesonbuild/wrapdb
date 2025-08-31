# pkg-config support for GTest is in the master
# branch of the upstream repository.
# In order to be consistent with the upstream
# naming and the library conventions, the
# following changes have been made:
#
#   gtest_mainless_dep -> gtest_dep
#   gtest_with_main_dep -> gtest_main_dep

gtest_incdir = include_directories(
  'include',
  '.',
  is_system: true,
)

if host_machine.system() == 'windows' and get_option('default_library') != 'static'
  dllexp = '-DGTEST_CREATE_SHARED_LIBRARY=1'
  dllimp = '-DGTEST_LINKED_AS_SHARED_LIBRARY=1'
else
  dllexp = []
  dllimp = []
endif

gtest_lib = library(
  'gtest-all',
  sources: files('src/gtest-all.cc'),
  gnu_symbol_visibility: 'hidden',
  cpp_args: dllexp,
  override_options: override_cpp,
  dependencies: dependency('threads'),
  include_directories: gtest_incdir,
)

gtest_main_lib = library(
  'gtest_main',
  sources: files('src/gtest_main.cc'),
  gnu_symbol_visibility: 'hidden',
  cpp_args: dllexp,
  override_options: override_cpp,
  include_directories: gtest_incdir,
  link_with: gtest_lib,
)

gtest_dep = declare_dependency(
  compile_args: dllimp,
  include_directories: gtest_incdir,
  link_with: gtest_lib,
  dependencies: dependency('threads'),
)

gtest_main_dep = declare_dependency(
  link_with: gtest_main_lib,
  dependencies: gtest_dep,
)
