cl_versions = ['100', '110', '120', '200', '210', '220', '300']

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
  foreach v : cl_versions
    test(
      'test_@0@_@1@'.format(t, v),
      executable(
        'test_@0@_@1@'.format(t, v),
        'test_@0@.h.c'.format(t),
        c_args: '-DCL_TARGET_OPENCL_VERSION=@0@'.format(v),
        dependencies: opencl_headers_dep,
      ),
    )
  endforeach
endforeach

test(
  'test_headers',
  executable(
    'headers',
    'test_headers.c',
    dependencies: opencl_headers_dep,
  ),
)
