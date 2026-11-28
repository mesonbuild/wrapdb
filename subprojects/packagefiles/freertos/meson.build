project(
  'freertos',
  'c',
  'cpp',
  license: 'MIT',
  meson_version: '>=0.63.0',
  version: '11.2.0',
  default_options: ['b_staticpic=false', 'default_library=static'],
)

# FreeRTOSConfig.h must be specified as dependency like that:
#
# freertos_config_dep = declare_dependency(
#   sources: 'configs/FreeRTOSConfig.h',
#   include_directories: 'configs',
# )
# meson.override_dependency('freertos-config', freertos_config_dep)
#
# If not specified then we use config from examples as fallback.
freertos_config_dep = dependency(
  'freertos-config',
  required: false,
)
if not freertos_config_dep.found()
  freertos_config_dep = declare_dependency(
    sources: 'examples/template_configuration/FreeRTOSConfig.h',
    include_directories: 'examples/template_configuration',
  )
endif

inc = [include_directories('include')]
src = files(
  'croutine.c',
  'event_groups.c',
  'list.c',
  'queue.c',
  'stream_buffer.c',
  'tasks.c',
  'timers.c',
)

# Dependency with custom port on unknown arch
freertos_port_dep = dependency(
  'freertos-custom-port',
  required: false,
)
if not freertos_port_dep.found()
  subdir('portable')
endif

# Dependency with custom heap implementation
freertos_heap_dep = dependency(
  'freertos-custom-heap',
  required: false,
)
if not freertos_heap_dep.found()
  heap_number = get_option('heap_number')
  src += files(f'portable/MemMang/heap_@heap_number@.c')
endif

freertos_lib = library(
  'freertos_kernel',
  src,
  include_directories: inc,
  dependencies: [freertos_config_dep, freertos_port_dep, freertos_heap_dep],
)
freertos_dep = declare_dependency(
  include_directories: inc,
  link_with: freertos_lib,
  dependencies: [freertos_config_dep, freertos_port_dep],
)
meson.override_dependency('freertos', freertos_dep)
