project('fft2d', 'c', default_options : ['default_library=shared'])

if not meson.is_subproject() 
  cc = meson.get_compiler('c')
endif

include = include_directories('.')

fft2d_sources = files(
  'fftsg.c',
  'fftsg2d.c'
)

fft2d = library('fft2d',
  fft2d_sources,
  include_directories : [include],
  install : true,
  link_args : ['-lm'],
)

fft2d_dep = declare_dependency(
  link_with : fft2d,
  include_directories : [include]
)
