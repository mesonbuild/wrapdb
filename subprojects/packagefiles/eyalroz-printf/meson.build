project(
  'eyalroz-printf',
  'c',
  'cpp',
  license: 'MIT',
  meson_version: '>=1.0.0',
  version: '6.2.0',
  default_options: [
    'b_staticpic=false',
    'c_std=c99',
    'default_library=static',  # For shared support we need to somehow provide putchar_ implementation
  ],
)

subdir('printf-6.2.0')
