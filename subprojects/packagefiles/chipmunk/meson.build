project(
  'chipmunk',
  'c',
  version: '7.0.3',
  license: 'MIT',
)

cc = meson.get_compiler('c')
m_dep = cc.find_library(
  'm',
  required: false,
)

inc = include_directories('include')
lib = library(
  'chipmunk',
  'src/chipmunk.c',
  'src/cpArbiter.c',
  'src/cpArray.c',
  'src/cpBBTree.c',
  'src/cpBody.c',
  'src/cpCollision.c',
  'src/cpHashSet.c',
  'src/cpPolyShape.c',
  'src/cpRobust.c',
  'src/cpShape.c',
  'src/cpSpace.c',
  'src/cpSpaceComponent.c',
  'src/cpSpaceHash.c',
  'src/cpSpaceQuery.c',
  'src/cpSpaceStep.c',
  'src/cpSpatialIndex.c',
  'src/cpSweep1D.c',
  include_directories: inc,
  dependencies: m_dep,
)

chipmunk_dep = declare_dependency(
  include_directories: inc,
  link_with: lib,
)
