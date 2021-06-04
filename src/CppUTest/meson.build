cpputest_src = files(
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
    'Utest.cpp'
)

cpputest_lib = static_library('CppUTest',
    cpputest_src,
    include_directories : cpputest_dirs)