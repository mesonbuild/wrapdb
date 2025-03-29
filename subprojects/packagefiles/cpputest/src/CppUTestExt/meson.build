cpputest_ext_sources = files(
  'CodeMemoryReportFormatter.cpp',
  'GTest.cpp',
  'IEEE754ExceptionsPlugin.cpp',
  'MemoryReportAllocator.cpp',
  'MemoryReportFormatter.cpp',
  'MemoryReporterPlugin.cpp',
  'MockActualCall.cpp',
  'MockExpectedCall.cpp',
  'MockExpectedCallsList.cpp',
  'MockFailure.cpp',
  'MockNamedValue.cpp',
  'MockSupport.cpp',
  'MockSupportPlugin.cpp',
  'MockSupport_c.cpp',
  'OrderedTest.cpp',
)

cpputest_ext_lib = library(
  'CppUTest',
  cpputest_ext_sources,
  include_directories: cpputest_includes,
)
