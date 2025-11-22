examples_lib = static_library(
  'examples',
  'example_util.c',
  build_by_default: false,
  dependencies: common_deps,
  gnu_symbol_visibility: 'hidden',
)

foreach _spec : [
  ['cwebp', webpdemux_dep, [imageio_dec_lib, imageio_util_lib]],
  ['dwebp', webpdemux_dep, [imageio_dec_lib, imageio_enc_lib, imageio_util_lib]],
  ['webpinfo', webp_dep, imageio_util_lib],
  ['webpmux', webpmux_dep, imageio_util_lib],
]
  _name = _spec[0]
  _deps = _spec[1]
  _libs = _spec[2]
  _exe = executable(
    _name,
    _name + '.c',
    c_args: '-DWEBP_EXTERN=extern',
    dependencies: [get_variable('build_' + _name), common_deps, _deps],
    install: true,
    link_with: [examples_lib, _libs],
  )
  meson.override_find_program(_name, _exe)
endforeach
