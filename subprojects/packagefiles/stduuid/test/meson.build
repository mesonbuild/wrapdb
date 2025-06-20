test_src_files = files('main.cpp', 'test_generators.cpp', 'test_uuid.cpp')

test_inc_dirs = inc_dirs
test_inc_dirs += include_directories('../catch')

test_flags = flags

if host_machine.system() == 'windows'
  test_flags += [
    windows_options_prefix + 'EHc',
    windows_options_prefix + 'Zc:hiddenFriend',
    windows_options_prefix + 'D_SCL_SECURE_NO_WARNINGS',
  ]
else
  test_flags += ['-fexceptions']
endif


all_tests = executable(
  'stduuid_all_tests',
  test_src_files,
  include_directories: test_inc_dirs,
  cpp_args: flags,
  override_options: override_options,
  dependencies: stduuid_dep,
)


test(
  'stduuid all tests',
  all_tests,
  timeout: 120,
)
