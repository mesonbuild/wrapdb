# api/ also holds internal headers, only expose the public one to dependents
configure_file(
  input: '..' / 'api' / 'fftw3.h',
  output: 'fftw3.h',
  copy: true,
)
fftw_inc = include_directories('.')
