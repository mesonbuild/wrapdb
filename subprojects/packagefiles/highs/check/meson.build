
catch_dep = declare_dependency(
  include_directories : include_directories('../extern')
)

test_sources = files([
  'TestAlienBasis.cpp',
  'TestDualise.cpp',
  'TestCheckSolution.cpp',
  'TestEkk.cpp',
  'TestFactor.cpp',
  'TestFreezeBasis.cpp',
  'TestHotStart.cpp',
  'TestMain.cpp',
  'TestOptions.cpp',
  'TestIO.cpp',
  'TestSort.cpp',
  'TestSetup.cpp',
  'TestFilereader.cpp',
  'TestHighsGFkSolve.cpp',
  'TestInfo.cpp',
  'TestBasis.cpp',
  'TestBasisSolves.cpp',
  'TestHighsHash.cpp',
  'TestHighsIntegers.cpp',
  'TestHighsParallel.cpp',
  'TestHighsRbTree.cpp',
  'TestHighsHessian.cpp',
  'TestHighsModel.cpp',
  'TestHSet.cpp',
  'TestLogging.cpp',
  'TestLpValidation.cpp',
  'TestLpModification.cpp',
  'TestLpOrientation.cpp',
  'TestQpSolver.cpp',
  'TestRays.cpp',
  'TestRanging.cpp',
  'TestSemiVariables.cpp',
  'TestThrow.cpp',
  'Avgas.cpp',
])

if host_machine.system() != 'darwin'
  test_sources += files([
    'TestSpecialLps.cpp',
    'TestLpSolvers.cpp',
    'TestMipSolver.cpp',
  ])
endif

if ipx_on
  test_sources += 'TestIpx.cpp'
endif

test_include_directories = include_directories([
  '../src/',
  '../src/lp_data',
  '../src/ipm/ipx/src',
  '../src/ipm/basiclu/src',
  '../src/ipm/ipx/include',
  '../src/ipm/basiclu/include',
])

unit_tests = executable('unit_tests', test_sources,
  dependencies : [ highs_dep, catch_dep ],
  include_directories : test_include_directories,
  build_by_default : false
)

capi_unit_tests = executable('capi_unit_tests', files('TestCAPI.c'),
  dependencies : [ highs_dep, catch_dep ],
  include_directories : test_include_directories,
  build_by_default : false
)

test('unit_tests', unit_tests)
test('capi_unit_tests', capi_unit_tests)
