project('chipmunk', 'c', version : '6.2.2', license : 'MIT')

cc = meson.get_compiler('c')
m_dep = cc.find_library('m', required : false)

inc = include_directories('include/chipmunk')
lib = library('chipmunk', ['src/chipmunk.c', 'src/cpArbiter.c', 'src/cpArray.c', 'src/cpBB.c',
	'src/cpBBTree.c', 'src/cpBody.c', 'src/cpCollision.c', 'src/cpHashSet.c', 'src/cpPolyShape.c',
	'src/cpShape.c', 'src/cpSpace.c', 'src/cpSpaceComponent.c', 'src/cpSpaceHash.c',
	'src/cpSpaceQuery.c', 'src/cpSpaceStep.c', 'src/cpSpatialIndex.c', 'src/cpSweep1D.c',
	'src/cpVect.c', 'src/constraints/cpConstraint.c', 'src/constraints/cpDampedRotarySpring.c',
	'src/constraints/cpDampedSpring.c', 'src/constraints/cpGearJoint.c',
	'src/constraints/cpGrooveJoint.c', 'src/constraints/cpPinJoint.c',
	'src/constraints/cpPivotJoint.c', 'src/constraints/cpRatchetJoint.c',
	'src/constraints/cpRotaryLimitJoint.c', 'src/constraints/cpSimpleMotor.c',
	'src/constraints/cpSlideJoint.c',
], include_directories : inc, dependencies : m_dep)

chipmunk_dep = declare_dependency(include_directories : inc, link_with : lib)
