test(
  'example',
  executable(
    'example',
    'example.c',
    c_args: compile_args + ['-DZLIBNG_ENABLE_TESTS'],
    link_args: link_args,
    dependencies: zlib_ng_dep,
  ),
)
