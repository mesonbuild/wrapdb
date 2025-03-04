sdl_dep = disabler()
if device_io.enabled()
  if host_system == 'emscripten'
    sdl_dep = declare_dependency(compile_args: '--use-port=sdl2', link_args: '--use-port=sdl2')
  else
    sdl_dep = dependency('sdl2', required: false)
  endif
  if sdl_dep.found()
    executable(
      'custom_backend',
      'custom_backend.c',
      name_suffix: host_system == 'emscripten' ? 'html' : [],
      dependencies: ma_sys_deps + ma_backend_deps + sdl_dep,
      install: false,
      implicit_include_directories: false,
      include_directories: ma_inc,
    )
  endif
endif

if decoding and device_io.enabled() and (
  opus_dep.found()
  and opusfile_dep.found()
  and vorbis_dep.found()
  and vorbisfile_dep.found()
)
  executable(
    'custom_decoder',
    'custom_decoder.c',
    dependencies: ma_sys_deps
    + ma_backend_deps
    + [opus_dep, opusfile_dep, vorbis_dep, vorbisfile_dep],
    install: false,
    implicit_include_directories: false,
    include_directories: ma_inc,
  )

  if engine and resource_manager.enabled()
    executable(
      'custom_decoder_engine',
      'custom_decoder_engine.c',
      dependencies: ma_sys_deps
      + ma_backend_deps
      + [opus_dep, opusfile_dep, vorbis_dep, vorbisfile_dep],
      install: false,
      implicit_include_directories: false,
      include_directories: ma_inc,
    )
  endif
endif

if decoding and device_io.enabled()
  executable(
    'data_source_chaining',
    'data_source_chaining.c',
    dependencies: ma_sys_deps + ma_backend_deps,
    install: false,
    implicit_include_directories: false,
    include_directories: ma_inc,
  )
endif

if node_graph.enabled() and device_io.enabled()
  executable(
    'duplex_effect',
    'duplex_effect.c',
    dependencies: ma_sys_deps + ma_backend_deps,
    install: false,
    implicit_include_directories: false,
    include_directories: ma_inc,
  )
endif

if engine and device_io.enabled() and resource_manager.enabled()
  executable(
    'engine_hello_world',
    'engine_hello_world.c',
    dependencies: ma_sys_deps + ma_backend_deps,
    install: false,
    implicit_include_directories: false,
    include_directories: ma_inc,
  )
  executable(
    'engine_advanced',
    'engine_advanced.c',
    dependencies: ma_sys_deps + ma_backend_deps,
    install: false,
    implicit_include_directories: false,
    include_directories: ma_inc,
  )
  if sdl_dep.found() and host_system != 'emscripten'
    executable(
      'engine_sdl',
      'engine_sdl.c',
      dependencies: ma_sys_deps + ma_backend_deps + sdl_dep,
      install: false,
      implicit_include_directories: false,
      include_directories: ma_inc,
    )
  endif
endif

if engine and node_graph.enabled()
  executable(
    'engine_effects',
    'engine_effects.c',
    dependencies: ma_sys_deps + ma_backend_deps,
    install: false,
    implicit_include_directories: false,
    include_directories: ma_inc,
  )
endif

if engine
  phonon_dep = dependency('phonon', required: false)
  if phonon_dep.found()
    executable(
      'engine_steamaudio',
      'engine_steamaudio.c',
      dependencies: ma_sys_deps + ma_backend_deps + phonon_dep,
      install: false,
      implicit_include_directories: false,
      include_directories: ma_inc,
    )
  endif
endif

if device_io.enabled() and engine
  executable(
    'hilo_interop',
    'hilo_interop.c',
    dependencies: ma_sys_deps + ma_backend_deps,
    install: false,
    implicit_include_directories: false,
    include_directories: ma_inc,
  )
endif

if node_graph.enabled() and decoding and device_io.enabled()
  executable(
    'node_graph',
    'node_graph.c',
    dependencies: ma_sys_deps + ma_backend_deps,
    install: false,
    implicit_include_directories: false,
    include_directories: ma_inc,
  )
endif

if resource_manager.enabled() and device_io.enabled()
  executable(
    'resource_manager',
    'resource_manager.c',
    name_suffix: host_system == 'emscripten' ? 'html' : [],
    dependencies: ma_sys_deps + ma_backend_deps,
    install: false,
    implicit_include_directories: false,
    include_directories: ma_inc,
  )
  executable(
    'resource_manager_advanced',
    'resource_manager_advanced.c',
    dependencies: ma_sys_deps + ma_backend_deps,
    install: false,
    implicit_include_directories: false,
    include_directories: ma_inc,
  )
endif

if device_io.enabled() and encoding
  executable(
    'simple_capture',
    'simple_capture.c',
    dependencies: ma_sys_deps + ma_backend_deps,
    install: false,
    implicit_include_directories: false,
    include_directories: ma_inc,
  )
endif
if device_io.enabled()
  executable(
    'simple_duplex',
    'simple_duplex.c',
    name_suffix: host_system == 'emscripten' ? 'html' : [],
    dependencies: ma_sys_deps + ma_backend_deps,
    install: false,
    implicit_include_directories: false,
    include_directories: ma_inc,
  )
  executable(
    'simple_enumeration',
    'simple_enumeration.c',
    dependencies: ma_sys_deps + ma_backend_deps,
    install: false,
    implicit_include_directories: false,
    include_directories: ma_inc,
  )
endif

if device_io.enabled() and (
  'wasapi' in backends
  or (backends == ['_miniaudio_default'] and host_system == 'windows')
)
  executable(
    'simple_loopback',
    'simple_loopback.c',
    dependencies: ma_sys_deps + ma_backend_deps,
    install: false,
    implicit_include_directories: false,
    include_directories: ma_inc,
  )
endif

if device_io.enabled() and decoding
  executable(
    'simple_looping',
    'simple_looping.c',
    dependencies: ma_sys_deps + ma_backend_deps,
    install: false,
    implicit_include_directories: false,
    include_directories: ma_inc,
  )
  executable(
    'simple_mixing',
    'simple_mixing.c',
    dependencies: ma_sys_deps + ma_backend_deps,
    install: false,
    implicit_include_directories: false,
    include_directories: ma_inc,
  )
  executable(
    'simple_playback',
    'simple_playback.c',
    dependencies: ma_sys_deps + ma_backend_deps,
    install: false,
    implicit_include_directories: false,
    include_directories: ma_inc,
  )
endif

if device_io.enabled() and generation
  executable(
    'simple_playback_sine',
    'simple_playback_sine.c',
    name_suffix: host_system == 'emscripten' ? 'html' : [],
    dependencies: ma_sys_deps + ma_backend_deps,
    install: false,
    implicit_include_directories: false,
    include_directories: ma_inc,
  )
endif
