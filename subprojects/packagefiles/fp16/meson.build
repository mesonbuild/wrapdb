project('FP16', 'c')


if not meson.is_subproject()
  cc = meson.get_compiler('c')
endif

inc = include_directories ('include')

fp16_dep = declare_dependency(
  include_directories : [inc])
