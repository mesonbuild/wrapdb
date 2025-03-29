tests_opt = get_option('tests')
gtest_dep = dependency(
  'gtest_main',
  required: tests_opt,
)
tests_opt = tests_opt.require(
  gtest_dep.found() and cpp_available,
  error_message: 'missing C++ compiler',
)

if tests_opt.disabled()
  subdir_done()
endif

gumbo_test = executable(
  'gumbo_test',
  [
    'attribute.cc',
    'char_ref.cc',
    'parser.cc',
    'string_buffer.cc',
    'string_piece.cc',
    'test_utils.cc',
    'utf8.cc',
    'vector.cc',
  ] + (
  # Does not link with MSVC: missing "C" specifier to
  # `extern const char* kGumboTagNames[];` declaration.
    cpp.get_id() in ['clang-cl', 'msvc'] ? [] : ['tokenizer.cc']
  ),
  dependencies: [
    gumbo_dep.partial_dependency(
      compile_args: true,
      includes: true,
    ),
    gtest_dep,
  ],
  # The testsuite need access to some private
  # symbols (not exported by the DLL on Windows).
  objects: gumbo_lib.extract_all_objects(
    recursive: true,
  ),
)

test(
  'gumbo_test',
  gumbo_test,
  protocol: 'gtest',
)
