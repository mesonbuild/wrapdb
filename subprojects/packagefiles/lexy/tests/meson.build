

test_dependencies = [dependency('doctest')]


test_src = files('doctest_main.cpp')

test_dependencies += lexy_dep

test_flags = ['-DLEXY_TEST']


if (cpp.get_id() == 'msvc')
  test_flags += ['/Zc:preprocessor', '/utf-8', '/bigobj']
endif

tests = []

# Add the individual tests.
subdir('lexy')
subdir('lexy_ext')
subdir('examples')
# note: not inlcuded, since heavy cmake (dark) magic is invloved here and this generates many files!
# subdir('playground')

foreach test : tests
  name = test[0]
  files = test[1]

  text_exe = executable(
    'lexy_test_' + name,
    files,
    test_src,
    dependencies: test_dependencies,
    override_options: override_options,
    cpp_args: test_flags,
  )

  test('lexy_test_' + name, text_exe, is_parallel: true)
endforeach





