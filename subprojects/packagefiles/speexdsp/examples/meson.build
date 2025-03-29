if get_option('examples')
  examples = ['denoise', 'echo', 'jitter', 'resample', 'resample2']

  foreach example : examples
    executable(
      example,
      '../libspeexdsp/test' + example + '.c',
      dependencies: speexdsp_dep,
    )
  endforeach
endif
