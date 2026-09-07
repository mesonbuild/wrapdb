project(
  'glm',
  'cpp',
  version: '1.0.3',
  license: 'MIT',
  meson_version: '>= 0.56.0',
)

glm_dep = declare_dependency(
  include_directories: include_directories('.'),
)

meson.override_dependency('glm', glm_dep)
