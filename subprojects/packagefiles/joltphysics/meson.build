project(
  'joltphysics',
  'cpp',
  license: 'MIT',
  version: '5.3.0',
  meson_version: '>=0.59.0',
  default_options: ['cpp_rtti=false', 'cpp_eh=none'],
)

cpp = meson.get_compiler('cpp')

# meson reports msys2 as windows, so we have to check for clang + windows
# to catch clang on msys2. This doesn't catch clang-cl on windows so thats
# fine.
if cpp.get_id() == 'clang' and host_machine.system() == 'windows'
  error(
    'unsupported architecture: Clang on cygwin/msys2 cannot build jolt due to linking issues, sorry',
  )
endif

if host_machine.cpu_family() in ['ppc64', 'loongarch64']
  error(
    'unsupported architecture: Jolt 5.3.0 cannot be built on ppc64 or loongarch64, 5.4.0+ is required',
  )
endif

# Source files
sources = files(
  'Jolt/AABBTree/AABBTreeBuilder.cpp',
  'Jolt/Core/Color.cpp',
  'Jolt/Core/Factory.cpp',
  'Jolt/Core/IssueReporting.cpp',
  'Jolt/Core/JobSystemSingleThreaded.cpp',
  'Jolt/Core/JobSystemThreadPool.cpp',
  'Jolt/Core/JobSystemWithBarrier.cpp',
  'Jolt/Core/LinearCurve.cpp',
  'Jolt/Core/Memory.cpp',
  'Jolt/Core/Profiler.cpp',
  'Jolt/Core/RTTI.cpp',
  'Jolt/Core/Semaphore.cpp',
  'Jolt/Core/StringTools.cpp',
  'Jolt/Core/TickCounter.cpp',
  'Jolt/Geometry/ConvexHullBuilder.cpp',
  'Jolt/Geometry/ConvexHullBuilder2D.cpp',
  'Jolt/Geometry/Indexify.cpp',
  'Jolt/Geometry/OrientedBox.cpp',
  'Jolt/Math/Vec3.cpp',
  'Jolt/Physics/Body/Body.cpp',
  'Jolt/Physics/Body/BodyCreationSettings.cpp',
  'Jolt/Physics/Body/BodyInterface.cpp',
  'Jolt/Physics/Body/BodyManager.cpp',
  'Jolt/Physics/Body/MassProperties.cpp',
  'Jolt/Physics/Body/MotionProperties.cpp',
  'Jolt/Physics/Character/Character.cpp',
  'Jolt/Physics/Character/CharacterBase.cpp',
  'Jolt/Physics/Character/CharacterVirtual.cpp',
  'Jolt/Physics/Collision/BroadPhase/BroadPhase.cpp',
  'Jolt/Physics/Collision/BroadPhase/BroadPhaseBruteForce.cpp',
  'Jolt/Physics/Collision/BroadPhase/BroadPhaseQuadTree.cpp',
  'Jolt/Physics/Collision/BroadPhase/QuadTree.cpp',
  'Jolt/Physics/Collision/CastConvexVsTriangles.cpp',
  'Jolt/Physics/Collision/CastSphereVsTriangles.cpp',
  'Jolt/Physics/Collision/CollideConvexVsTriangles.cpp',
  'Jolt/Physics/Collision/CollideSphereVsTriangles.cpp',
  'Jolt/Physics/Collision/CollisionDispatch.cpp',
  'Jolt/Physics/Collision/CollisionGroup.cpp',
  'Jolt/Physics/Collision/EstimateCollisionResponse.cpp',
  'Jolt/Physics/Collision/GroupFilter.cpp',
  'Jolt/Physics/Collision/GroupFilterTable.cpp',
  'Jolt/Physics/Collision/ManifoldBetweenTwoFaces.cpp',
  'Jolt/Physics/Collision/NarrowPhaseQuery.cpp',
  'Jolt/Physics/Collision/NarrowPhaseStats.cpp',
  'Jolt/Physics/Collision/PhysicsMaterial.cpp',
  'Jolt/Physics/Collision/PhysicsMaterialSimple.cpp',
  'Jolt/Physics/Collision/Shape/BoxShape.cpp',
  'Jolt/Physics/Collision/Shape/CapsuleShape.cpp',
  'Jolt/Physics/Collision/Shape/CompoundShape.cpp',
  'Jolt/Physics/Collision/Shape/ConvexHullShape.cpp',
  'Jolt/Physics/Collision/Shape/ConvexShape.cpp',
  'Jolt/Physics/Collision/Shape/CylinderShape.cpp',
  'Jolt/Physics/Collision/Shape/DecoratedShape.cpp',
  'Jolt/Physics/Collision/Shape/EmptyShape.cpp',
  'Jolt/Physics/Collision/Shape/HeightFieldShape.cpp',
  'Jolt/Physics/Collision/Shape/MeshShape.cpp',
  'Jolt/Physics/Collision/Shape/MutableCompoundShape.cpp',
  'Jolt/Physics/Collision/Shape/OffsetCenterOfMassShape.cpp',
  'Jolt/Physics/Collision/Shape/PlaneShape.cpp',
  'Jolt/Physics/Collision/Shape/RotatedTranslatedShape.cpp',
  'Jolt/Physics/Collision/Shape/ScaledShape.cpp',
  'Jolt/Physics/Collision/Shape/Shape.cpp',
  'Jolt/Physics/Collision/Shape/SphereShape.cpp',
  'Jolt/Physics/Collision/Shape/StaticCompoundShape.cpp',
  'Jolt/Physics/Collision/Shape/TaperedCapsuleShape.cpp',
  'Jolt/Physics/Collision/Shape/TaperedCylinderShape.cpp',
  'Jolt/Physics/Collision/Shape/TriangleShape.cpp',
  'Jolt/Physics/Collision/TransformedShape.cpp',
  'Jolt/Physics/Constraints/ConeConstraint.cpp',
  'Jolt/Physics/Constraints/Constraint.cpp',
  'Jolt/Physics/Constraints/ConstraintManager.cpp',
  'Jolt/Physics/Constraints/ContactConstraintManager.cpp',
  'Jolt/Physics/Constraints/DistanceConstraint.cpp',
  'Jolt/Physics/Constraints/FixedConstraint.cpp',
  'Jolt/Physics/Constraints/GearConstraint.cpp',
  'Jolt/Physics/Constraints/HingeConstraint.cpp',
  'Jolt/Physics/Constraints/MotorSettings.cpp',
  'Jolt/Physics/Constraints/PathConstraint.cpp',
  'Jolt/Physics/Constraints/PathConstraintPath.cpp',
  'Jolt/Physics/Constraints/PathConstraintPathHermite.cpp',
  'Jolt/Physics/Constraints/PointConstraint.cpp',
  'Jolt/Physics/Constraints/PulleyConstraint.cpp',
  'Jolt/Physics/Constraints/RackAndPinionConstraint.cpp',
  'Jolt/Physics/Constraints/SixDOFConstraint.cpp',
  'Jolt/Physics/Constraints/SliderConstraint.cpp',
  'Jolt/Physics/Constraints/SpringSettings.cpp',
  'Jolt/Physics/Constraints/SwingTwistConstraint.cpp',
  'Jolt/Physics/Constraints/TwoBodyConstraint.cpp',
  'Jolt/Physics/DeterminismLog.cpp',
  'Jolt/Physics/IslandBuilder.cpp',
  'Jolt/Physics/LargeIslandSplitter.cpp',
  'Jolt/Physics/PhysicsScene.cpp',
  'Jolt/Physics/PhysicsSystem.cpp',
  'Jolt/Physics/PhysicsUpdateContext.cpp',
  'Jolt/Physics/Ragdoll/Ragdoll.cpp',
  'Jolt/Physics/SoftBody/SoftBodyCreationSettings.cpp',
  'Jolt/Physics/SoftBody/SoftBodyMotionProperties.cpp',
  'Jolt/Physics/SoftBody/SoftBodyShape.cpp',
  'Jolt/Physics/SoftBody/SoftBodySharedSettings.cpp',
  'Jolt/Physics/StateRecorderImpl.cpp',
  'Jolt/Physics/Vehicle/MotorcycleController.cpp',
  'Jolt/Physics/Vehicle/TrackedVehicleController.cpp',
  'Jolt/Physics/Vehicle/VehicleAntiRollBar.cpp',
  'Jolt/Physics/Vehicle/VehicleCollisionTester.cpp',
  'Jolt/Physics/Vehicle/VehicleConstraint.cpp',
  'Jolt/Physics/Vehicle/VehicleController.cpp',
  'Jolt/Physics/Vehicle/VehicleDifferential.cpp',
  'Jolt/Physics/Vehicle/VehicleEngine.cpp',
  'Jolt/Physics/Vehicle/VehicleTrack.cpp',
  'Jolt/Physics/Vehicle/VehicleTransmission.cpp',
  'Jolt/Physics/Vehicle/Wheel.cpp',
  'Jolt/Physics/Vehicle/WheeledVehicleController.cpp',
  'Jolt/RegisterTypes.cpp',
  'Jolt/Renderer/DebugRenderer.cpp',
  'Jolt/Renderer/DebugRendererPlayback.cpp',
  'Jolt/Renderer/DebugRendererRecorder.cpp',
  'Jolt/Renderer/DebugRendererSimple.cpp',
  'Jolt/Skeleton/SkeletalAnimation.cpp',
  'Jolt/Skeleton/Skeleton.cpp',
  'Jolt/Skeleton/SkeletonMapper.cpp',
  'Jolt/Skeleton/SkeletonPose.cpp',
  'Jolt/TriangleSplitter/TriangleSplitter.cpp',
  'Jolt/TriangleSplitter/TriangleSplitterBinning.cpp',
  'Jolt/TriangleSplitter/TriangleSplitterMean.cpp',
)

object_stream = get_option('object_stream')

if object_stream
  sources += files(
    'Jolt/ObjectStream/ObjectStream.cpp',
    'Jolt/ObjectStream/ObjectStreamBinaryIn.cpp',
    'Jolt/ObjectStream/ObjectStreamBinaryOut.cpp',
    'Jolt/ObjectStream/ObjectStreamIn.cpp',
    'Jolt/ObjectStream/ObjectStreamOut.cpp',
    'Jolt/ObjectStream/ObjectStreamTextIn.cpp',
    'Jolt/ObjectStream/ObjectStreamTextOut.cpp',
    'Jolt/ObjectStream/SerializableObject.cpp',
    'Jolt/ObjectStream/TypeDeclarations.cpp',
  )
endif

args = []
fp_args = cpp.get_supported_arguments(['-mfpmath=sse'])
build_args = []

if get_option('default_library') == 'shared'
  args += ['-DJPH_SHARED_LIBRARY']
  build_args += ['-DJPH_BUILD_SHARED_LIBRARY']
endif

build_debug = get_option('debug')
sanitize = get_option('b_sanitize')

broadphase_stats = get_option('broadphase_stats').disable_auto_if(
  not build_debug,
)
narrowphase_stats = get_option('narrowphase_stats').disable_auto_if(
  not build_debug,
)
debug_render = get_option('debug_render').disable_auto_if(not build_debug)
profile = get_option('profile').disable_auto_if(not build_debug)
asserts_opt = get_option('asserts').disable_auto_if(not build_debug)

disable_custom_allocator = get_option('disable_custom_allocator')
cross_platform_determinism = get_option('cross_platform_determinism')
tests_opt = get_option('tests').disable_auto_if(meson.is_subproject())

if sanitize.contains('address')
  disable_custom_allocator = true
endif

if object_stream
  args += ['-DJPH_OBJECT_STREAM']
endif

if get_option('fpu_exceptions')
  args += ['-DJPH_FLOATING_POINT_EXCEPTIONS_ENABLED']
endif

if disable_custom_allocator
  args += ['-DJPH_DISABLE_TEMP_ALLOCATOR']
endif

if get_option('double_precision')
  args += ['-DJPH_DOUBLE_PRECISION']
endif

if cross_platform_determinism
  args += ['-DJPH_CROSS_PLATFORM_DETERMINISM']
  fp_args += cpp.get_supported_arguments(['-ffp-contract=off'])
endif

if get_option('cpp_eh') == 'none'
  build_args += ['-D_HAS_EXCEPTIONS=0']
endif

args += ['-DJPH_OBJECT_LAYER_BITS=@0@'.format(get_option('object_layer_bits'))]

if broadphase_stats.allowed()
  args += ['-DJPH_TRACK_BROADPHASE_STATS']
endif

if narrowphase_stats.allowed()
  args += ['-DJPH_TRACK_NARROWPHASE_STATS']
endif

if debug_render.allowed()
  args += ['-DJPH_DEBUG_RENDERER']
endif

if profile.allowed()
  args += ['-DJPH_PROFILE_ENABLED']
endif

if asserts_opt.allowed()
  args += ['-DJPH_ENABLE_ASSERTS']
endif

jolt = library(
  'Jolt',
  sources,
  cpp_args: args + build_args + fp_args,
  override_options: ['cpp_std=c++17'],
  install: true,
)

jolt_dep = declare_dependency(
  include_directories: '.',
  link_with: jolt,
  compile_args: args + fp_args,
)

meson.override_dependency('Jolt', jolt_dep)

# riscv fails to run tests due to alignment issues
platform_supports_tests = true
if host_machine.cpu_family() == 'riscv64'
  platform_supports_tests = false
endif

if platform_supports_tests
  doctest = dependency(
    'doctest',
    required: tests_opt,
  )
  if doctest.found()
    test_src = files(
      'UnitTests/Core/ArrayTest.cpp',
      'UnitTests/Core/BinaryHeapTest.cpp',
      'UnitTests/Core/FPFlushDenormalsTest.cpp',
      'UnitTests/Core/HashCombineTest.cpp',
      'UnitTests/Core/InsertionSortTest.cpp',
      'UnitTests/Core/JobSystemTest.cpp',
      'UnitTests/Core/LinearCurveTest.cpp',
      'UnitTests/Core/PreciseMathTest.cpp',
      'UnitTests/Core/QuickSortTest.cpp',
      'UnitTests/Core/STLLocalAllocatorTest.cpp',
      'UnitTests/Core/ScopeExitTest.cpp',
      'UnitTests/Core/StringToolsTest.cpp',
      'UnitTests/Core/UnorderedMapTest.cpp',
      'UnitTests/Core/UnorderedSetTest.cpp',
      'UnitTests/Geometry/ClosestPointTests.cpp',
      'UnitTests/Geometry/ConvexHullBuilderTest.cpp',
      'UnitTests/Geometry/EPATests.cpp',
      'UnitTests/Geometry/EllipseTest.cpp',
      'UnitTests/Geometry/GJKTests.cpp',
      'UnitTests/Geometry/PlaneTests.cpp',
      'UnitTests/Geometry/RayAABoxTests.cpp',
      'UnitTests/Math/BVec16Tests.cpp',
      'UnitTests/Math/DMat44Tests.cpp',
      'UnitTests/Math/DVec3Tests.cpp',
      'UnitTests/Math/EigenValueSymmetricTests.cpp',
      'UnitTests/Math/HalfFloatTests.cpp',
      'UnitTests/Math/Mat44Tests.cpp',
      'UnitTests/Math/MathTests.cpp',
      'UnitTests/Math/MatrixTests.cpp',
      'UnitTests/Math/QuatTests.cpp',
      'UnitTests/Math/TrigonometryTests.cpp',
      'UnitTests/Math/UVec4Tests.cpp',
      'UnitTests/Math/Vec3Tests.cpp',
      'UnitTests/Math/Vec4Tests.cpp',
      'UnitTests/Math/VectorTests.cpp',
      'UnitTests/Physics/ActiveEdgesTests.cpp',
      'UnitTests/Physics/BroadPhaseTests.cpp',
      'UnitTests/Physics/CastShapeTests.cpp',
      'UnitTests/Physics/CharacterVirtualTests.cpp',
      'UnitTests/Physics/CollidePointTests.cpp',
      'UnitTests/Physics/CollideShapeTests.cpp',
      'UnitTests/Physics/CollisionGroupTests.cpp',
      'UnitTests/Physics/ContactListenerTests.cpp',
      'UnitTests/Physics/ConvexVsTrianglesTest.cpp',
      'UnitTests/Physics/DistanceConstraintTests.cpp',
      'UnitTests/Physics/EstimateCollisionResponseTest.cpp',
      'UnitTests/Physics/HeightFieldShapeTests.cpp',
      'UnitTests/Physics/HingeConstraintTests.cpp',
      'UnitTests/Physics/MotionQualityLinearCastTests.cpp',
      'UnitTests/Physics/MutableCompoundShapeTests.cpp',
      'UnitTests/Physics/ObjectLayerPairFilterMaskTests.cpp',
      'UnitTests/Physics/ObjectLayerPairFilterTableTests.cpp',
      'UnitTests/Physics/OffsetCenterOfMassShapeTests.cpp',
      'UnitTests/Physics/PathConstraintTests.cpp',
      'UnitTests/Physics/PhysicsDeterminismTests.cpp',
      'UnitTests/Physics/PhysicsStepListenerTests.cpp',
      'UnitTests/Physics/PhysicsTests.cpp',
      'UnitTests/Physics/RayShapeTests.cpp',
      'UnitTests/Physics/SensorTests.cpp',
      'UnitTests/Physics/ShapeFilterTests.cpp',
      'UnitTests/Physics/ShapeTests.cpp',
      'UnitTests/Physics/SixDOFConstraintTests.cpp',
      'UnitTests/Physics/SliderConstraintTests.cpp',
      'UnitTests/Physics/SoftBodyTests.cpp',
      'UnitTests/Physics/SubShapeIDTest.cpp',
      'UnitTests/Physics/TaperedCylinderShapeTests.cpp',
      'UnitTests/Physics/TransformedShapeTests.cpp',
      'UnitTests/Physics/WheeledVehicleTests.cpp',
      'UnitTests/PhysicsTestContext.cpp',
      'UnitTests/UnitTestFramework.cpp',
    )
    if object_stream
      test_src += files('UnitTests/ObjectStream/ObjectStreamTest.cpp')
    endif
    test_exe = executable(
      'UnitTests',
      test_src,
      cpp_args: [
        '-D_HAS_EXCEPTIONS=0',
      ],
      include_directories: ['UnitTests'],
      dependencies: [jolt_dep, doctest],
      override_options: ['cpp_std=c++17'],
      build_by_default: false,
    )
    test(
      'UnitTests',
      test_exe,
      timeout: 360,
    )
  endif
endif
