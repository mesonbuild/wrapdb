project(
  'OpenCLHeaders',
  'c',
  license: 'Apache-2.0',
  version: '2024.10.24',
)

install_headers(
  'CL/cl_d3d10.h',
  'CL/cl_d3d11.h',
  'CL/cl_dx9_media_sharing.h',
  'CL/cl_dx9_media_sharing_intel.h',
  'CL/cl_egl.h',
  'CL/cl_ext.h',
  'CL/cl_ext_intel.h',
  'CL/cl_gl_ext.h',
  'CL/cl_gl.h',
  'CL/cl.h',
  'CL/cl_half.h',
  'CL/cl_icd.h',
  'CL/cl_layer.h',
  'CL/cl_platform.h',
  'CL/cl_va_api_media_sharing_intel.h',
  'CL/cl_version.h',
  'CL/opencl.h',
  subdir: 'CL',
)

pkgc = import('pkgconfig')
pkgc.generate(
  name: 'OpenCL-Headers',
  description: 'C language headers for the OpenCL API',
  version: '3.0',
)

depinc = include_directories('.')
opencl_headers_dep = declare_dependency(
  include_directories: depinc,
  version: '3.0',
)

if get_option('tests')
  subdir('tests')
endif
