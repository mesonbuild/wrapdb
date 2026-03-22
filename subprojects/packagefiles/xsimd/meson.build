project(
  'xsimd',
  'cpp',
  license: 'BSD-3-Clause',
  meson_version: '>=0.63.0',
  version: '14.1.0',
  default_options: ['cpp_std=c++14'],
)

xsimd_inc = include_directories('include')
xtl_dep = dependency(
  'xtl',
  version: '>=0.7.0',
  required: get_option('xtl_complex'),
)

if xtl_dep.found()
  complex_args = ['-DXSIMD_ENABLE_XTL_COMPLEX=1']
else
  complex_args = []
endif

xsimd_dep = declare_dependency(
  include_directories: xsimd_inc,
  dependencies: xtl_dep,
  compile_args: complex_args,
)

meson.override_dependency('xsimd', xsimd_dep)
