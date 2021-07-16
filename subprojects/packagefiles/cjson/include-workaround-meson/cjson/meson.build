# This is a workaround for creating a cjson/ folder with the headers in it in
# the builddir space.
#
# See https://github.com/mesonbuild/meson/issues/2546 for where the technique comes from
foreach h: headers
  configure_file(copy: true,
                 input: h,
                 output: '@PLAINNAME@')
endforeach
