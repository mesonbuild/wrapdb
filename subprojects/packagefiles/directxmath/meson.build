project(
  'directxmath',
  'cpp',
  version: '3.1.9',
)

incdirs = include_directories('Inc')

directxmath_headers = files(
  'Inc/DirectXCollision.h',
  'Inc/DirectXCollision.inl',
  'Inc/DirectXColors.h',
  'Inc/DirectXMath.h',
  'Inc/DirectXMathConvert.inl',
  'Inc/DirectXMathMatrix.inl',
  'Inc/DirectXMathMisc.inl',
  'Inc/DirectXMathVector.inl',
  'Inc/DirectXPackedVector.h',
  'Inc/DirectXPackedVector.inl',
)

directxmath_dep = declare_dependency(
  include_directories: incdirs,
)

install_headers(
  directxmath_headers,
  subdir: 'directxmath',
)

pkgconfig = import('pkgconfig')
pkgconfig.generate(
  name: 'directxmath',
  version: meson.project_version(),
  subdirs: 'directxmath',
  description: 'DirectXMath SIMD C++ math library',
)

