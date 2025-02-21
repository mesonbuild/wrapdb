# pkg-config support for GTest is in the master
# branch of the upstream repository.
# In order to be consistent with the upstream
# naming and the library conventions, the
# following changes have been made:
#
#   gtest_mainless_dep -> gtest_dep
#   gtest_with_main_dep -> gtest_main_dep

gtest_incdir = include_directories('include', '.', is_system : true)

if host_machine.system() == 'windows'
  target_type = 'static_library'
else
  target_type = 'shared_library'
endif

gtest_src = files('src/gtest-all.cc')
gtest_lib = build_target(
    'gtest-all',
    sources: gtest_src,
    include_directories: gtest_incdir,
    target_type: target_type,
)

gtest_main_lib = build_target(
    'gtest_main',
    sources: files('src/gtest_main.cc'),
    include_directories: gtest_incdir,
    link_with: gtest_lib,
    target_type: target_type,
)

gtest_dep = declare_dependency(
    include_directories : gtest_incdir,
    link_with: [gtest_lib],
    dependencies : dependency('threads')
)

gtest_main_dep = declare_dependency(
    include_directories : gtest_incdir,
    link_with: [gtest_lib, gtest_main_lib],
    dependencies : dependency('threads')
)
