# https://github.com/mesonbuild/meson/issues/2546
foreach h : api
  configure_file(
    copy: true,
    input: h,
    output: '@PLAINNAME@',
  )
endforeach

vconf = configure_file(
  configuration: version,
  input: versionh,
  output: 'yajl_version.h',
  format: 'cmake',
)

install_headers(
  api,
  vconf,
  subdir: 'yajl',
)
