project(
  'xsimd',
  'cpp',
  license: 'BSD-3-Clause',
  meson_version: '>=0.56.0',
  version: '14.1.0',
)

xsimd_inc = include_directories('include')

deps = []
if get_option('xtl_complex')
  deps += dependency(
    'xtl',
    version: '^0.7.0',
  )
  add_project_arguments(
    '-DXSIMD_ENABLE_XTL_COMPLEX=1',
    language: 'cpp',
  )
endif

xsimd_dep = declare_dependency(
  include_directories: xsimd_inc,
  dependencies: deps,
)

meson.override_dependency('xsimd', xsimd_dep)
