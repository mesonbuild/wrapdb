#
# Just a warning before you remove the hash symbol from "'TestTestMacros.cpp'",
# it generates an error like this.
#
# tests/TestTestMacros.cpp:167:27: error: expected ';' at end of declaration list
#      ~FixtureDtorThrows() _NOEXCEPT_OP(false) {
#                          ^
#                          ;
#

test_cases = files('Main.cpp',
    'TestAssertHandler.cpp',
    'TestCheckMacros.cpp',
    'TestChecks.cpp',
    'TestCompositeTestReporter.cpp',
    'TestCurrentTest.cpp',
    'TestDeferredTestReporter.cpp',
    'TestExceptions.cpp',
    'TestLongMacros.cpp',
    'TestMemoryOutStream.cpp',
    'TestRequireMacrosWithExceptionsOff.cpp',
    'TestRequireMacrosWithExceptionsOn.cpp',
    'TestTest.cpp',
    'TestTestList.cpp',
#    'TestTestMacros.cpp',
    'TestTestResults.cpp',
    'TestTestRunner.cpp',
    'TestTestSuite.cpp',
    'TestTimeConstraint.cpp',
    'TestTimeConstraintMacro.cpp',
    'TestUnitTestPP.cpp',
    'TestXmlTestReporter.cpp'
)

test('Run test cases', executable('TestUnitTest++', test_cases, dependencies : unittest_cpp_dep))