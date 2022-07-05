cl_tests = [
  'cl',
  'cl_d3d10',
  'cl_dx9_media_sharing',
  'cl_dx9_media_sharing_intel',
  'cl_egl',
  'cl_ext',
  'cl_ext_intel',
  'cl_gl',
  'cl_gl_ext',
  'cl_half',
  'cl_icd',
  'cl_layer',
  'cl_platform',
  'cl_version',
  'opencl',
]

foreach t : cl_tests
  test('test_@0@'.format(t), executable(t, 'test_@0@.h.c'.format(t), dependencies: opencl_headers_dep))
endforeach

test('test_headers', executable('headers', 'test_headers.c', dependencies: opencl_headers_dep))
