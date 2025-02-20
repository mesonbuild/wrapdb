# pkg-config support for GMock is in the master
# branch of the upstream repository.
# In order to be consistent with the upstream
# naming and the library conventions, the
# following changes have been made:
#
#   gmock_mainless_dep -> gmock_dep
#   gmock_with_main_dep -> gmock_main_dep
#
# Both GMock dependencies now include GTest,
# as this mimicks the same behavior as the
# upstream repo.

gmock_incdir = include_directories('include', '.', is_system: true)

if host_machine.system() == 'windows' and get_option('default_library') != 'static'
    target_type = 'static_library'
else
    target_type = 'shared_library'
endif

gmock_lib = build_target(
    'gmock-all',
    sources: files('src/gmock-all.cc'),
    #can't do the following because of dllimport
    #dependencies: gtest_dep,
    include_directories: [gtest_incdir, gmock_incdir],
    link_with: gtest_lib,
    target_type: target_type,
)

gmock_main_lib = build_target(
    'gmock_main',
    sources: files('src/gmock_main.cc'),
    #can't do the following because of dllimport
    #dependencies: gmock_dep,
    include_directories: [gtest_incdir, gmock_incdir],
    link_with: [gtest_lib, gmock_lib],
    target_type: target_type,
)

gmock_dep = declare_dependency(
    include_directories: gmock_incdir,
    link_with: gmock_lib,
    dependencies: gtest_dep,
)

gmock_main_dep = declare_dependency(
    link_with: gmock_main_lib,
    dependencies: gmock_dep,
)
