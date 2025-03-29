sources = [
  'Biquad.cpp',
  'Butterworth.cpp',
  'Cascade.cpp',
  'ChebyshevI.cpp',
  'ChebyshevII.cpp',
  'Custom.cpp',
  'PoleFilter.cpp',
  'RBJ.cpp',
]

headers = [
  'Biquad.h',
  'Butterworth.h',
  'Cascade.h',
  'ChebyshevI.h',
  'ChebyshevII.h',
  'Common.h',
  'Custom.h',
  'Layout.h',
  'MathSupplement.h',
  'PoleFilter.h',
  'RBJ.h',
  'State.h',
  'Types.h',
]

install_headers(
  headers,
  subdir: 'iir',
)

# Maybe disable exceptions
if not get_option('exceptions')
  add_project_arguments(
    '-DIIR1_NO_EXCEPTIONS',
    language: 'cpp',
  )
endif

lib = library(
  'iir',
  sources,
  include_directories: incdirs,
  install: true,
  version: meson.project_version(),
)

libiir_dep = declare_dependency(
  include_directories: incdirs,
  link_with: lib,
)

pkgconfig = import('pkgconfig')
pkgconfig.generate(
  lib,
  description: 'IIR is an an infinite impulse response (IIR) filter library',
  version: meson.project_version(),
)
