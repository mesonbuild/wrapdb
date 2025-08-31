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

gmock_incdir = include_directories(
  'include',
  '.',
  is_system: true,
)

cpp = meson.get_compiler('cpp')

if cpp.get_argument_syntax() == 'msvc'
  gmock_lib = static_library(
    'gmock-all',
    files('../googletest/src/gtest-all.cc', 'src/gmock-all.cc'),
    override_options: override_cpp,
    include_directories: [gtest_incdir, gmock_incdir],
  )

  gmock_main_lib = static_library(
    'gmock_main',
    files(
      '../googletest/src/gtest-all.cc',
      'src/gmock-all.cc',
      'src/gmock_main.cc',
    ),
    override_options: override_cpp,
    include_directories: [gtest_incdir, gmock_incdir],
  )

  gmock_dep = declare_dependency(
    include_directories: [gtest_incdir, gmock_incdir],
    link_with: gmock_lib,
  )

  gmock_main_dep = declare_dependency(
    include_directories: [gtest_incdir, gmock_incdir],
    link_with: gmock_main_lib,
  )
else
  gmock_lib = library(
    'gmock-all',
    files('src/gmock-all.cc'),
    #can't do the following because of dllimport
    #dependencies: gtest_dep,
    override_options: override_cpp,
    dependencies: dependency('threads'),
    include_directories: [gtest_incdir, gmock_incdir],
    link_with: gtest_lib,
  )

  gmock_main_lib = library(
    'gmock_main',
    files('src/gmock_main.cc'),
    #can't do the following because of dllimport
    #dependencies: gmock_dep,
    override_options: override_cpp,
    include_directories: [gtest_incdir, gmock_incdir],
    link_with: [gtest_lib, gmock_lib],
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
endif
