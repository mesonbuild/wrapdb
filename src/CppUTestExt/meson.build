cpputest_ext_src = files(
    'CodeMemoryReportFormatter.cpp',
    'GTest.cpp',
    'IEEE754ExceptionsPlugin.cpp',
    'MemoryReportAllocator.cpp',
    'MemoryReporterPlugin.cpp',
    'MemoryReportFormatter.cpp',
    'MockActualCall.cpp',
    'MockExpectedCall.cpp',
    'MockExpectedCallsList.cpp',
    'MockFailure.cpp',
    'MockNamedValue.cpp',
    'MockSupport_c.cpp',
    'MockSupport.cpp',
    'MockSupportPlugin.cpp',
    'OrderedTest.cpp'
)

cpputest_ext_lib = static_library('CppUTestExt',
    cpputest_ext_src,
    include_directories : cpputest_dirs)