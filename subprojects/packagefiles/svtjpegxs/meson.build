project(
  'svtjpegxs',
  'c',
  version: '0.9.0',
  meson_version: '>= 0.64.0',
)

cc = meson.get_compiler('c')
if host_machine.cpu_family() == 'x86_64'
  add_project_arguments(
    '-DARCH_X86_64=1',
    language: 'c',
  )
else
  error('unsupported architecture: SVT-JPEG-XS requires x86_64')
endif

add_languages(
  'nasm',
  native: false,
)

build_shared = get_option('default_library') in ['shared', 'both']
if build_shared
  add_project_arguments(
    '-DDEF_DLL',
    '-DDEF_BUILDING_SHARED_LIBS',
    language: 'c',
  )
endif

subdir('third_party/cpuinfo')
subdir('Source/Lib')
