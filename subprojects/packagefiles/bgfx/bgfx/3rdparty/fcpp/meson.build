# fcpp - Frexx C Preprocessor

fcpp_sources = files(
  'cpp1.c',
  'cpp2.c',
  'cpp3.c',
  'cpp4.c',
  'cpp5.c',
  'cpp6.c',
)

fcpp_c_args = [
  '-DNINCLUDE=64',
  '-DNWORK=65536',
  '-DNBUFF=65536',
  '-DOLD_PREPROCESSOR=0',
]

if meson.get_compiler('c').get_id() == 'msvc'
  fcpp_c_args += ['/wd4055', '/wd4244', '/wd4701', '/wd4706']
else
  fcpp_c_args += [
    '-Wno-implicit-fallthrough',
    '-Wno-parentheses-equality',
  ]
  if meson.get_compiler('c').has_argument('-Wno-incompatible-pointer-types')
    fcpp_c_args += '-Wno-incompatible-pointer-types'
  endif
endif

fcpp_lib = static_library('fcpp', fcpp_sources,
  c_args: fcpp_c_args,
  include_directories: include_directories('.'),
  override_options: ['c_std=c11'],
)

fcpp_dep = declare_dependency(
  link_with: fcpp_lib,
  include_directories: include_directories('.'),
)
