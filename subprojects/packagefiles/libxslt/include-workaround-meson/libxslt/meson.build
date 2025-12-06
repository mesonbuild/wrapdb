# https://github.com/mesonbuild/meson/issues/2546
foreach h : libxslt_headers
  configure_file(
    copy: true,
    input: h,
    output: '@PLAINNAME@',
  )
endforeach
