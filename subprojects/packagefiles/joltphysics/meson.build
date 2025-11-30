project(
  'jolt',
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

if host_machine.cpu_family() == 'ppc64'
  error(
    'unsupported architecture: Jolt 5.3.0 cannot be built on ppc64, 5.4.0+ is required',
  )
endif

# Source files
all = [
  'Jolt/ConfigurationString.h',
  'Jolt/RegisterTypes.h',
  'Jolt/RegisterTypes.cpp',
  'Jolt/Jolt.h',
  'Jolt/Physics/PhysicsScene.cpp',
  'Jolt/Physics/PhysicsScene.h',
  'Jolt/Physics/IslandBuilder.cpp',
  'Jolt/Physics/DeterminismLog.cpp',
  'Jolt/Physics/PhysicsUpdateContext.cpp',
  'Jolt/Physics/PhysicsSettings.h',
  'Jolt/Physics/StateRecorderImpl.cpp',
  'Jolt/Physics/LargeIslandSplitter.h',
  'Jolt/Physics/IslandBuilder.h',
  'Jolt/Physics/PhysicsLock.h',
  'Jolt/Physics/PhysicsSystem.cpp',
  'Jolt/Physics/PhysicsStepListener.h',
  'Jolt/Physics/PhysicsSystem.h',
  'Jolt/Physics/StateRecorderImpl.h',
  'Jolt/Physics/StateRecorder.h',
  'Jolt/Physics/EPhysicsUpdateError.h',
  'Jolt/Physics/LargeIslandSplitter.cpp',
  'Jolt/Physics/EActivation.h',
  'Jolt/Physics/DeterminismLog.h',
  'Jolt/Physics/PhysicsUpdateContext.h',
  'Jolt/Physics/Character/CharacterVirtual.cpp',
  'Jolt/Physics/Character/CharacterBase.h',
  'Jolt/Physics/Character/CharacterBase.cpp',
  'Jolt/Physics/Character/Character.cpp',
  'Jolt/Physics/Character/CharacterID.h',
  'Jolt/Physics/Character/CharacterVirtual.h',
  'Jolt/Physics/Character/Character.h',
  'Jolt/Physics/Collision/PhysicsMaterialSimple.h',
  'Jolt/Physics/Collision/EstimateCollisionResponse.h',
  'Jolt/Physics/Collision/CollisionCollectorImpl.h',
  'Jolt/Physics/Collision/BackFaceMode.h',
  'Jolt/Physics/Collision/RayCast.h',
  'Jolt/Physics/Collision/CollisionDispatch.h',
  'Jolt/Physics/Collision/CollideConvexVsTriangles.h',
  'Jolt/Physics/Collision/CollectFacesMode.h',
  'Jolt/Physics/Collision/SimShapeFilter.h',
  'Jolt/Physics/Collision/ObjectLayerPairFilterMask.h',
  'Jolt/Physics/Collision/CollidePointResult.h',
  'Jolt/Physics/Collision/CollideShapeVsShapePerLeaf.h',
  'Jolt/Physics/Collision/ManifoldBetweenTwoFaces.h',
  'Jolt/Physics/Collision/NarrowPhaseStats.cpp',
  'Jolt/Physics/Collision/ManifoldBetweenTwoFaces.cpp',
  'Jolt/Physics/Collision/NarrowPhaseQuery.h',
  'Jolt/Physics/Collision/SimShapeFilterWrapper.h',
  'Jolt/Physics/Collision/NarrowPhaseQuery.cpp',
  'Jolt/Physics/Collision/ActiveEdgeMode.h',
  'Jolt/Physics/Collision/CollideSphereVsTriangles.cpp',
  'Jolt/Physics/Collision/PhysicsMaterialSimple.cpp',
  'Jolt/Physics/Collision/CollideSoftBodyVertexIterator.h',
  'Jolt/Physics/Collision/GroupFilterTable.cpp',
  'Jolt/Physics/Collision/CastConvexVsTriangles.cpp',
  'Jolt/Physics/Collision/CastSphereVsTriangles.cpp',
  'Jolt/Physics/Collision/GroupFilterTable.h',
  'Jolt/Physics/Collision/CollisionDispatch.cpp',
  'Jolt/Physics/Collision/CollisionCollector.h',
  'Jolt/Physics/Collision/CollideShape.h',
  'Jolt/Physics/Collision/ShapeCast.h',
  'Jolt/Physics/Collision/PhysicsMaterial.cpp',
  'Jolt/Physics/Collision/ActiveEdges.h',
  'Jolt/Physics/Collision/ObjectLayerPairFilterTable.h',
  'Jolt/Physics/Collision/CollideSphereVsTriangles.h',
  'Jolt/Physics/Collision/ContactListener.h',
  'Jolt/Physics/Collision/CollideConvexVsTriangles.cpp',
  'Jolt/Physics/Collision/ObjectLayer.h',
  'Jolt/Physics/Collision/CastResult.h',
  'Jolt/Physics/Collision/GroupFilter.cpp',
  'Jolt/Physics/Collision/TransformedShape.h',
  'Jolt/Physics/Collision/CollisionGroup.cpp',
  'Jolt/Physics/Collision/ShapeFilter.h',
  'Jolt/Physics/Collision/GroupFilter.h',
  'Jolt/Physics/Collision/EstimateCollisionResponse.cpp',
  'Jolt/Physics/Collision/TransformedShape.cpp',
  'Jolt/Physics/Collision/InternalEdgeRemovingCollector.h',
  'Jolt/Physics/Collision/CastConvexVsTriangles.h',
  'Jolt/Physics/Collision/CastSphereVsTriangles.h',
  'Jolt/Physics/Collision/SortReverseAndStore.h',
  'Jolt/Physics/Collision/PhysicsMaterial.h',
  'Jolt/Physics/Collision/CollideSoftBodyVerticesVsTriangles.h',
  'Jolt/Physics/Collision/CollisionGroup.h',
  'Jolt/Physics/Collision/AABoxCast.h',
  'Jolt/Physics/Collision/NarrowPhaseStats.h',
  'Jolt/Physics/Collision/Shape/SphereShape.h',
  'Jolt/Physics/Collision/Shape/ScaledShape.h',
  'Jolt/Physics/Collision/Shape/StaticCompoundShape.h',
  'Jolt/Physics/Collision/Shape/CompoundShape.cpp',
  'Jolt/Physics/Collision/Shape/TaperedCapsuleShape.cpp',
  'Jolt/Physics/Collision/Shape/PlaneShape.cpp',
  'Jolt/Physics/Collision/Shape/TaperedCylinderShape.h',
  'Jolt/Physics/Collision/Shape/EmptyShape.h',
  'Jolt/Physics/Collision/Shape/MutableCompoundShape.cpp',
  'Jolt/Physics/Collision/Shape/StaticCompoundShape.cpp',
  'Jolt/Physics/Collision/Shape/ScaledShape.cpp',
  'Jolt/Physics/Collision/Shape/SphereShape.cpp',
  'Jolt/Physics/Collision/Shape/CapsuleShape.h',
  'Jolt/Physics/Collision/Shape/GetTrianglesContext.h',
  'Jolt/Physics/Collision/Shape/TaperedCapsuleShape.h',
  'Jolt/Physics/Collision/Shape/ConvexShape.cpp',
  'Jolt/Physics/Collision/Shape/CapsuleShape.cpp',
  'Jolt/Physics/Collision/Shape/HeightFieldShape.h',
  'Jolt/Physics/Collision/Shape/CompoundShape.h',
  'Jolt/Physics/Collision/Shape/CompoundShapeVisitors.h',
  'Jolt/Physics/Collision/Shape/PlaneShape.h',
  'Jolt/Physics/Collision/Shape/DecoratedShape.h',
  'Jolt/Physics/Collision/Shape/DecoratedShape.cpp',
  'Jolt/Physics/Collision/Shape/EmptyShape.cpp',
  'Jolt/Physics/Collision/Shape/TaperedCapsuleShape.gliffy',
  'Jolt/Physics/Collision/Shape/Shape.h',
  'Jolt/Physics/Collision/Shape/OffsetCenterOfMassShape.h',
  'Jolt/Physics/Collision/Shape/PolyhedronSubmergedVolumeCalculator.h',
  'Jolt/Physics/Collision/Shape/Shape.cpp',
  'Jolt/Physics/Collision/Shape/RotatedTranslatedShape.cpp',
  'Jolt/Physics/Collision/Shape/ConvexHullShape.cpp',
  'Jolt/Physics/Collision/Shape/CylinderShape.h',
  'Jolt/Physics/Collision/Shape/SubShapeID.h',
  'Jolt/Physics/Collision/Shape/TriangleShape.h',
  'Jolt/Physics/Collision/Shape/MutableCompoundShape.h',
  'Jolt/Physics/Collision/Shape/MeshShape.cpp',
  'Jolt/Physics/Collision/Shape/OffsetCenterOfMassShape.cpp',
  'Jolt/Physics/Collision/Shape/BoxShape.h',
  'Jolt/Physics/Collision/Shape/ScaleHelpers.h',
  'Jolt/Physics/Collision/Shape/ConvexHullShape.h',
  'Jolt/Physics/Collision/Shape/TriangleShape.cpp',
  'Jolt/Physics/Collision/Shape/MeshShape.h',
  'Jolt/Physics/Collision/Shape/ConvexShape.h',
  'Jolt/Physics/Collision/Shape/CylinderShape.cpp',
  'Jolt/Physics/Collision/Shape/SubShapeIDPair.h',
  'Jolt/Physics/Collision/Shape/HeightFieldShape.cpp',
  'Jolt/Physics/Collision/Shape/TaperedCylinderShape.cpp',
  'Jolt/Physics/Collision/Shape/RotatedTranslatedShape.h',
  'Jolt/Physics/Collision/Shape/BoxShape.cpp',
  'Jolt/Physics/Collision/BroadPhase/BroadPhaseQuadTree.cpp',
  'Jolt/Physics/Collision/BroadPhase/BroadPhaseQuadTree.h',
  'Jolt/Physics/Collision/BroadPhase/ObjectVsBroadPhaseLayerFilterMask.h',
  'Jolt/Physics/Collision/BroadPhase/ObjectVsBroadPhaseLayerFilterTable.h',
  'Jolt/Physics/Collision/BroadPhase/QuadTree.h',
  'Jolt/Physics/Collision/BroadPhase/BroadPhaseBruteForce.cpp',
  'Jolt/Physics/Collision/BroadPhase/BroadPhaseQuery.h',
  'Jolt/Physics/Collision/BroadPhase/BroadPhaseBruteForce.h',
  'Jolt/Physics/Collision/BroadPhase/QuadTree.cpp',
  'Jolt/Physics/Collision/BroadPhase/BroadPhaseLayerInterfaceTable.h',
  'Jolt/Physics/Collision/BroadPhase/BroadPhaseLayer.h',
  'Jolt/Physics/Collision/BroadPhase/BroadPhase.h',
  'Jolt/Physics/Collision/BroadPhase/BroadPhase.cpp',
  'Jolt/Physics/Collision/BroadPhase/BroadPhaseLayerInterfaceMask.h',
  'Jolt/Physics/Ragdoll/Ragdoll.cpp',
  'Jolt/Physics/Ragdoll/Ragdoll.h',
  'Jolt/Physics/Body/MotionQuality.h',
  'Jolt/Physics/Body/BodyInterface.h',
  'Jolt/Physics/Body/BodyPair.h',
  'Jolt/Physics/Body/MotionProperties.h',
  'Jolt/Physics/Body/BodyManager.h',
  'Jolt/Physics/Body/BodyLockMulti.h',
  'Jolt/Physics/Body/MassProperties.cpp',
  'Jolt/Physics/Body/BodyID.h',
  'Jolt/Physics/Body/BodyLockInterface.h',
  'Jolt/Physics/Body/BodyCreationSettings.h',
  'Jolt/Physics/Body/Body.h',
  'Jolt/Physics/Body/BodyFilter.h',
  'Jolt/Physics/Body/Body.cpp',
  'Jolt/Physics/Body/BodyActivationListener.h',
  'Jolt/Physics/Body/BodyCreationSettings.cpp',
  'Jolt/Physics/Body/BodyType.h',
  'Jolt/Physics/Body/MotionType.h',
  'Jolt/Physics/Body/BodyInterface.cpp',
  'Jolt/Physics/Body/MotionProperties.inl',
  'Jolt/Physics/Body/BodyManager.cpp',
  'Jolt/Physics/Body/MotionProperties.cpp',
  'Jolt/Physics/Body/AllowedDOFs.h',
  'Jolt/Physics/Body/BodyLock.h',
  'Jolt/Physics/Body/Body.inl',
  'Jolt/Physics/Body/MassProperties.h',
  'Jolt/Physics/Body/BodyAccess.h',
  'Jolt/Physics/SoftBody/SoftBodyMotionProperties.h',
  'Jolt/Physics/SoftBody/SoftBodyContactListener.h',
  'Jolt/Physics/SoftBody/SoftBodyShape.h',
  'Jolt/Physics/SoftBody/SoftBodyMotionProperties.cpp',
  'Jolt/Physics/SoftBody/SoftBodySharedSettings.h',
  'Jolt/Physics/SoftBody/SoftBodyShape.cpp',
  'Jolt/Physics/SoftBody/SoftBodyCreationSettings.h',
  'Jolt/Physics/SoftBody/SoftBodyVertex.h',
  'Jolt/Physics/SoftBody/SoftBodyManifold.h',
  'Jolt/Physics/SoftBody/SoftBodySharedSettings.cpp',
  'Jolt/Physics/SoftBody/SoftBodyCreationSettings.cpp',
  'Jolt/Physics/SoftBody/SoftBodyUpdateContext.h',
  'Jolt/Physics/Vehicle/VehicleAntiRollBar.h',
  'Jolt/Physics/Vehicle/VehicleController.h',
  'Jolt/Physics/Vehicle/MotorcycleController.h',
  'Jolt/Physics/Vehicle/VehicleTransmission.h',
  'Jolt/Physics/Vehicle/VehicleEngine.h',
  'Jolt/Physics/Vehicle/VehicleController.cpp',
  'Jolt/Physics/Vehicle/Wheel.cpp',
  'Jolt/Physics/Vehicle/VehicleEngine.cpp',
  'Jolt/Physics/Vehicle/VehicleTrack.cpp',
  'Jolt/Physics/Vehicle/VehicleCollisionTester.cpp',
  'Jolt/Physics/Vehicle/TrackedVehicleController.h',
  'Jolt/Physics/Vehicle/VehicleDifferential.h',
  'Jolt/Physics/Vehicle/WheeledVehicleController.h',
  'Jolt/Physics/Vehicle/WheeledVehicleController.cpp',
  'Jolt/Physics/Vehicle/VehicleDifferential.cpp',
  'Jolt/Physics/Vehicle/TrackedVehicleController.cpp',
  'Jolt/Physics/Vehicle/VehicleTrack.h',
  'Jolt/Physics/Vehicle/VehicleConstraint.h',
  'Jolt/Physics/Vehicle/VehicleTransmission.cpp',
  'Jolt/Physics/Vehicle/VehicleCollisionTester.h',
  'Jolt/Physics/Vehicle/VehicleAntiRollBar.cpp',
  'Jolt/Physics/Vehicle/MotorcycleController.cpp',
  'Jolt/Physics/Vehicle/VehicleConstraint.cpp',
  'Jolt/Physics/Vehicle/Wheel.h',
  'Jolt/Physics/Constraints/PointConstraint.h',
  'Jolt/Physics/Constraints/DistanceConstraint.h',
  'Jolt/Physics/Constraints/ContactConstraintManager.cpp',
  'Jolt/Physics/Constraints/Constraint.cpp',
  'Jolt/Physics/Constraints/TwoBodyConstraint.h',
  'Jolt/Physics/Constraints/ContactConstraintManager.h',
  'Jolt/Physics/Constraints/DistanceConstraint.cpp',
  'Jolt/Physics/Constraints/SwingTwistConstraint.h',
  'Jolt/Physics/Constraints/RackAndPinionConstraint.h',
  'Jolt/Physics/Constraints/GearConstraint.h',
  'Jolt/Physics/Constraints/SixDOFConstraint.h',
  'Jolt/Physics/Constraints/RackAndPinionConstraint.cpp',
  'Jolt/Physics/Constraints/PathConstraintPath.h',
  'Jolt/Physics/Constraints/SixDOFConstraint.cpp',
  'Jolt/Physics/Constraints/PathConstraint.cpp',
  'Jolt/Physics/Constraints/PathConstraintPathHermite.h',
  'Jolt/Physics/Constraints/CalculateSolverSteps.h',
  'Jolt/Physics/Constraints/PathConstraintPath.cpp',
  'Jolt/Physics/Constraints/ConeConstraint.cpp',
  'Jolt/Physics/Constraints/PulleyConstraint.h',
  'Jolt/Physics/Constraints/PulleyConstraint.cpp',
  'Jolt/Physics/Constraints/MotorSettings.h',
  'Jolt/Physics/Constraints/FixedConstraint.h',
  'Jolt/Physics/Constraints/TwoBodyConstraint.cpp',
  'Jolt/Physics/Constraints/HingeConstraint.cpp',
  'Jolt/Physics/Constraints/SliderConstraint.cpp',
  'Jolt/Physics/Constraints/PathConstraint.h',
  'Jolt/Physics/Constraints/PathConstraintPathHermite.cpp',
  'Jolt/Physics/Constraints/FixedConstraint.cpp',
  'Jolt/Physics/Constraints/SpringSettings.cpp',
  'Jolt/Physics/Constraints/ConstraintManager.h',
  'Jolt/Physics/Constraints/ConeConstraint.h',
  'Jolt/Physics/Constraints/GearConstraint.cpp',
  'Jolt/Physics/Constraints/ConstraintManager.cpp',
  'Jolt/Physics/Constraints/HingeConstraint.h',
  'Jolt/Physics/Constraints/SpringSettings.h',
  'Jolt/Physics/Constraints/SwingTwistConstraint.cpp',
  'Jolt/Physics/Constraints/MotorSettings.cpp',
  'Jolt/Physics/Constraints/Constraint.h',
  'Jolt/Physics/Constraints/PointConstraint.cpp',
  'Jolt/Physics/Constraints/SliderConstraint.h',
  'Jolt/Physics/Constraints/ConstraintPart/AxisConstraintPart.h',
  'Jolt/Physics/Constraints/ConstraintPart/RotationQuatConstraintPart.h',
  'Jolt/Physics/Constraints/ConstraintPart/HingeRotationConstraintPart.h',
  'Jolt/Physics/Constraints/ConstraintPart/PointConstraintPart.h',
  'Jolt/Physics/Constraints/ConstraintPart/SpringPart.h',
  'Jolt/Physics/Constraints/ConstraintPart/GearConstraintPart.h',
  'Jolt/Physics/Constraints/ConstraintPart/RotationEulerConstraintPart.h',
  'Jolt/Physics/Constraints/ConstraintPart/RackAndPinionConstraintPart.h',
  'Jolt/Physics/Constraints/ConstraintPart/IndependentAxisConstraintPart.h',
  'Jolt/Physics/Constraints/ConstraintPart/AngleConstraintPart.h',
  'Jolt/Physics/Constraints/ConstraintPart/DualAxisConstraintPart.h',
  'Jolt/Physics/Constraints/ConstraintPart/SwingTwistConstraintPart.h',
  'Jolt/Skeleton/SkeletonPose.cpp',
  'Jolt/Skeleton/Skeleton.h',
  'Jolt/Skeleton/SkeletalAnimation.h',
  'Jolt/Skeleton/SkeletonMapper.h',
  'Jolt/Skeleton/SkeletonPose.h',
  'Jolt/Skeleton/Skeleton.cpp',
  'Jolt/Skeleton/SkeletonMapper.cpp',
  'Jolt/Skeleton/SkeletalAnimation.cpp',
  'Jolt/AABBTree/AABBTreeToBuffer.h',
  'Jolt/AABBTree/AABBTreeBuilder.h',
  'Jolt/AABBTree/AABBTreeBuilder.cpp',
  'Jolt/AABBTree/NodeCodec/NodeCodecQuadTreeHalfFloat.h',
  'Jolt/AABBTree/TriangleCodec/TriangleCodecIndexed8BitPackSOA4Flags.h',
  'Jolt/Geometry/RayCapsule.h',
  'Jolt/Geometry/Indexify.cpp',
  'Jolt/Geometry/RayCylinder.h',
  'Jolt/Geometry/ClosestPoint.h',
  'Jolt/Geometry/IndexedTriangle.h',
  'Jolt/Geometry/ConvexSupport.h',
  'Jolt/Geometry/RaySphere.h',
  'Jolt/Geometry/ConvexHullBuilder2D.cpp',
  'Jolt/Geometry/Ellipse.h',
  'Jolt/Geometry/AABox.h',
  'Jolt/Geometry/Indexify.h',
  'Jolt/Geometry/RayAABox.h',
  'Jolt/Geometry/AABox4.h',
  'Jolt/Geometry/Triangle.h',
  'Jolt/Geometry/ConvexHullBuilder.cpp',
  'Jolt/Geometry/GJKClosestPoint.h',
  'Jolt/Geometry/EPAConvexHullBuilder.h',
  'Jolt/Geometry/Plane.h',
  'Jolt/Geometry/OrientedBox.h',
  'Jolt/Geometry/OrientedBox.cpp',
  'Jolt/Geometry/ConvexHullBuilder2D.h',
  'Jolt/Geometry/ClipPoly.h',
  'Jolt/Geometry/RayTriangle.h',
  'Jolt/Geometry/ConvexHullBuilder.h',
  'Jolt/Geometry/MortonCode.h',
  'Jolt/Geometry/EPAPenetrationDepth.h',
  'Jolt/Geometry/Sphere.h',
  'Jolt/Renderer/DebugRendererSimple.h',
  'Jolt/Renderer/DebugRendererPlayback.cpp',
  'Jolt/Renderer/DebugRenderer.h',
  'Jolt/Renderer/DebugRendererPlayback.h',
  'Jolt/Renderer/DebugRenderer.cpp',
  'Jolt/Renderer/DebugRendererSimple.cpp',
  'Jolt/Renderer/DebugRendererRecorder.h',
  'Jolt/Renderer/DebugRendererRecorder.cpp',
  'Jolt/Core/JobSystemThreadPool.h',
  'Jolt/Core/StridedPtr.h',
  'Jolt/Core/FixedSizeFreeList.h',
  'Jolt/Core/TickCounter.h',
  'Jolt/Core/FixedSizeFreeList.inl',
  'Jolt/Core/TickCounter.cpp',
  'Jolt/Core/Factory.h',
  'Jolt/Core/RTTI.h',
  'Jolt/Core/JobSystemWithBarrier.cpp',
  'Jolt/Core/HashTable.h',
  'Jolt/Core/Semaphore.h',
  'Jolt/Core/LinearCurve.cpp',
  'Jolt/Core/Profiler.h',
  'Jolt/Core/JobSystemSingleThreaded.cpp',
  'Jolt/Core/RTTI.cpp',
  'Jolt/Core/JobSystem.h',
  'Jolt/Core/MutexArray.h',
  'Jolt/Core/TempAllocator.h',
  'Jolt/Core/IssueReporting.cpp',
  'Jolt/Core/Color.h',
  'Jolt/Core/JobSystemWithBarrier.h',
  'Jolt/Core/StreamOut.h',
  'Jolt/Core/Semaphore.cpp',
  'Jolt/Core/Profiler.cpp',
  'Jolt/Core/JobSystem.inl',
  'Jolt/Core/UnorderedSet.h',
  'Jolt/Core/StringTools.h',
  'Jolt/Core/HashCombine.h',
  'Jolt/Core/FPException.h',
  'Jolt/Core/Reference.h',
  'Jolt/Core/ScopeExit.h',
  'Jolt/Core/LockFreeHashMap.h',
  'Jolt/Core/StaticArray.h',
  'Jolt/Core/Array.h',
  'Jolt/Core/Memory.cpp',
  'Jolt/Core/Mutex.h',
  'Jolt/Core/LinearCurve.h',
  'Jolt/Core/FPFlushDenormals.h',
  'Jolt/Core/STLLocalAllocator.h',
  'Jolt/Core/FPControlWord.h',
  'Jolt/Core/StreamIn.h',
  'Jolt/Core/Core.h',
  'Jolt/Core/InsertionSort.h',
  'Jolt/Core/StreamWrapper.h',
  'Jolt/Core/Factory.cpp',
  'Jolt/Core/StringTools.cpp',
  'Jolt/Core/Memory.h',
  'Jolt/Core/JobSystemSingleThreaded.h',
  'Jolt/Core/Profiler.inl',
  'Jolt/Core/BinaryHeap.h',
  'Jolt/Core/IssueReporting.h',
  'Jolt/Core/STLAlignedAllocator.h',
  'Jolt/Core/UnorderedMap.h',
  'Jolt/Core/ARMNeon.h',
  'Jolt/Core/Result.h',
  'Jolt/Core/ByteBuffer.h',
  'Jolt/Core/StreamUtils.h',
  'Jolt/Core/Atomics.h',
  'Jolt/Core/LockFreeHashMap.inl',
  'Jolt/Core/Color.cpp',
  'Jolt/Core/STLAllocator.h',
  'Jolt/Core/STLTempAllocator.h',
  'Jolt/Core/JobSystemThreadPool.cpp',
  'Jolt/Core/QuickSort.h',
  'Jolt/Core/NonCopyable.h',
  'Jolt/Math/Mat44.inl',
  'Jolt/Math/DMat44.inl',
  'Jolt/Math/DMat44.h',
  'Jolt/Math/MathTypes.h',
  'Jolt/Math/Double3.h',
  'Jolt/Math/FindRoot.h',
  'Jolt/Math/Mat44.h',
  'Jolt/Math/Trigonometry.h',
  'Jolt/Math/Swizzle.h',
  'Jolt/Math/EigenValueSymmetric.h',
  'Jolt/Math/Float3.h',
  'Jolt/Math/BVec16.h',
  'Jolt/Math/Float2.h',
  'Jolt/Math/Vector.h',
  'Jolt/Math/UVec4.h',
  'Jolt/Math/Vec3.cpp',
  'Jolt/Math/Vec3.inl',
  'Jolt/Math/Quat.inl',
  'Jolt/Math/Quat.h',
  'Jolt/Math/Real.h',
  'Jolt/Math/Vec3.h',
  'Jolt/Math/Vec4.h',
  'Jolt/Math/HalfFloat.h',
  'Jolt/Math/GaussianElimination.h',
  'Jolt/Math/Math.h',
  'Jolt/Math/DVec3.inl',
  'Jolt/Math/BVec16.inl',
  'Jolt/Math/Vec4.inl',
  'Jolt/Math/UVec4.inl',
  'Jolt/Math/Float4.h',
  'Jolt/Math/Matrix.h',
  'Jolt/Math/DVec3.h',
  'Jolt/Math/DynMatrix.h',
  'Jolt/TriangleSplitter/TriangleSplitterMean.cpp',
  'Jolt/TriangleSplitter/TriangleSplitter.h',
  'Jolt/TriangleSplitter/TriangleSplitterBinning.cpp',
  'Jolt/TriangleSplitter/TriangleSplitterBinning.h',
  'Jolt/TriangleSplitter/TriangleSplitter.cpp',
  'Jolt/TriangleSplitter/TriangleSplitterMean.h',
]

object_stream = get_option('object_stream')

if object_stream
  all += [
    'Jolt/ObjectStream/ObjectStreamBinaryIn.h',
    'Jolt/ObjectStream/ObjectStreamTextIn.cpp',
    'Jolt/ObjectStream/SerializableAttribute.h',
    'Jolt/ObjectStream/SerializableObject.h',
    'Jolt/ObjectStream/ObjectStreamTextIn.h',
    'Jolt/ObjectStream/TypeDeclarations.cpp',
    'Jolt/ObjectStream/ObjectStream.h',
    'Jolt/ObjectStream/ObjectStreamIn.cpp',
    'Jolt/ObjectStream/ObjectStreamTextOut.cpp',
    'Jolt/ObjectStream/ObjectStreamBinaryOut.cpp',
    'Jolt/ObjectStream/ObjectStreamIn.h',
    'Jolt/ObjectStream/GetPrimitiveTypeOfType.h',
    'Jolt/ObjectStream/ObjectStreamBinaryIn.cpp',
    'Jolt/ObjectStream/SerializableObject.cpp',
    'Jolt/ObjectStream/ObjectStreamBinaryOut.h',
    'Jolt/ObjectStream/ObjectStream.cpp',
    'Jolt/ObjectStream/ObjectStreamOut.cpp',
    'Jolt/ObjectStream/SerializableAttributeTyped.h',
    'Jolt/ObjectStream/SerializableAttributeEnum.h',
    'Jolt/ObjectStream/TypeDeclarations.h',
    'Jolt/ObjectStream/ObjectStreamOut.h',
    'Jolt/ObjectStream/ObjectStreamTextOut.h',
    'Jolt/ObjectStream/ObjectStreamTypes.h',
  ]
endif

headers = []
sources = []

foreach item : all
  if item.endswith('.h') or item.endswith('.inl')
    headers += item
  elif item.endswith('.cpp')
    sources += item
  endif
endforeach

args = []
build_args = []

if get_option('default_library') == 'shared'
  args += ['-DJPH_SHARED_LIBRARY']
  build_args += ['-DJPH_BUILD_SHARED_LIBRARY']
endif

buildtype = get_option('buildtype')
build_debug = buildtype.contains('debug')
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
  args += cpp.get_supported_arguments(['-ffp-contract=off'])
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

args += cpp.get_supported_arguments(['-mfpmath=sse'])

jolt = library(
  'Jolt',
  sources,
  include_directories: '.',
  extra_files: headers,
  cpp_pch: 'Jolt/Jolt.h',
  cpp_args: args + build_args,
  override_options: ['cpp_std=c++17'],
  install: true,
)

jolt_dep = declare_dependency(
  include_directories: '.',
  link_with: jolt,
  compile_args: args,
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
    test_src = [
      'UnitTests/UnitTestFramework.cpp',
      'UnitTests/PhysicsTestContext.cpp',
      'UnitTests/Physics/PhysicsDeterminismTests.cpp',
      'UnitTests/Physics/CollideShapeTests.cpp',
      'UnitTests/Physics/BroadPhaseTests.cpp',
      'UnitTests/Physics/HeightFieldShapeTests.cpp',
      'UnitTests/Physics/ContactListenerTests.cpp',
      'UnitTests/Physics/HingeConstraintTests.cpp',
      'UnitTests/Physics/ShapeFilterTests.cpp',
      'UnitTests/Physics/TaperedCylinderShapeTests.cpp',
      'UnitTests/Physics/PathConstraintTests.cpp',
      'UnitTests/Physics/CollidePointTests.cpp',
      'UnitTests/Physics/SensorTests.cpp',
      'UnitTests/Physics/EstimateCollisionResponseTest.cpp',
      'UnitTests/Physics/OffsetCenterOfMassShapeTests.cpp',
      'UnitTests/Physics/SoftBodyTests.cpp',
      'UnitTests/Physics/ConvexVsTrianglesTest.cpp',
      'UnitTests/Physics/SliderConstraintTests.cpp',
      'UnitTests/Physics/ActiveEdgesTests.cpp',
      'UnitTests/Physics/ShapeTests.cpp',
      'UnitTests/Physics/SixDOFConstraintTests.cpp',
      'UnitTests/Physics/MutableCompoundShapeTests.cpp',
      'UnitTests/Physics/ObjectLayerPairFilterMaskTests.cpp',
      'UnitTests/Physics/WheeledVehicleTests.cpp',
      'UnitTests/Physics/CastShapeTests.cpp',
      'UnitTests/Physics/MotionQualityLinearCastTests.cpp',
      'UnitTests/Physics/ObjectLayerPairFilterTableTests.cpp',
      'UnitTests/Physics/CollisionGroupTests.cpp',
      'UnitTests/Physics/TransformedShapeTests.cpp',
      'UnitTests/Physics/RayShapeTests.cpp',
      'UnitTests/Physics/PhysicsStepListenerTests.cpp',
      'UnitTests/Physics/SubShapeIDTest.cpp',
      'UnitTests/Physics/DistanceConstraintTests.cpp',
      'UnitTests/Physics/CharacterVirtualTests.cpp',
      'UnitTests/Physics/PhysicsTests.cpp',
      'UnitTests/Geometry/EllipseTest.cpp',
      'UnitTests/Geometry/ConvexHullBuilderTest.cpp',
      'UnitTests/Geometry/RayAABoxTests.cpp',
      'UnitTests/Geometry/ClosestPointTests.cpp',
      'UnitTests/Geometry/EPATests.cpp',
      'UnitTests/Geometry/PlaneTests.cpp',
      'UnitTests/Geometry/GJKTests.cpp',
      'UnitTests/Core/FPFlushDenormalsTest.cpp',
      'UnitTests/Core/QuickSortTest.cpp',
      'UnitTests/Core/BinaryHeapTest.cpp',
      'UnitTests/Core/HashCombineTest.cpp',
      'UnitTests/Core/UnorderedMapTest.cpp',
      'UnitTests/Core/UnorderedSetTest.cpp',
      'UnitTests/Core/StringToolsTest.cpp',
      'UnitTests/Core/PreciseMathTest.cpp',
      'UnitTests/Core/InsertionSortTest.cpp',
      'UnitTests/Core/STLLocalAllocatorTest.cpp',
      'UnitTests/Core/ScopeExitTest.cpp',
      'UnitTests/Core/JobSystemTest.cpp',
      'UnitTests/Core/ArrayTest.cpp',
      'UnitTests/Core/LinearCurveTest.cpp',
      'UnitTests/Math/QuatTests.cpp',
      'UnitTests/Math/Vec4Tests.cpp',
      'UnitTests/Math/BVec16Tests.cpp',
      'UnitTests/Math/DVec3Tests.cpp',
      'UnitTests/Math/Mat44Tests.cpp',
      'UnitTests/Math/Vec3Tests.cpp',
      'UnitTests/Math/DMat44Tests.cpp',
      'UnitTests/Math/EigenValueSymmetricTests.cpp',
      'UnitTests/Math/MatrixTests.cpp',
      'UnitTests/Math/UVec4Tests.cpp',
      'UnitTests/Math/MathTests.cpp',
      'UnitTests/Math/TrigonometryTests.cpp',
      'UnitTests/Math/HalfFloatTests.cpp',
      'UnitTests/Math/VectorTests.cpp',
    ]
    if object_stream
      test_src += ['UnitTests/ObjectStream/ObjectStreamTest.cpp']
    endif
    test_exe = executable(
      'UnitTests',
      test_src,
      include_directories: ['.', 'UnitTests'],
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
