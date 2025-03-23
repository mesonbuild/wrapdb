cpputest_sources = files(
  'CommandLineArguments.cpp',
  'CommandLineTestRunner.cpp',
  'JUnitTestOutput.cpp',
  'MemoryLeakDetector.cpp',
  'MemoryLeakWarningPlugin.cpp',
  'SimpleMutex.cpp',
  'SimpleString.cpp',
  'SimpleStringInternalCache.cpp',
  'TeamCityTestOutput.cpp',
  'TestFailure.cpp',
  'TestFilter.cpp',
  'TestHarness_c.cpp',
  'TestMemoryAllocator.cpp',
  'TestOutput.cpp',
  'TestPlugin.cpp',
  'TestRegistry.cpp',
  'TestResult.cpp',
  'TestTestingFixture.cpp',
  'Utest.cpp',
)

if get_option('cpputest_platform') != 'none'
  cpputest_sources += platform_source_file
endif

cpputest_lib = library(
  'CppUTest',
  cpputest_sources,
  include_directories: cpputest_includes,
)
