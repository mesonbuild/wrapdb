# We build those executables here and not in the parent
# directory to workaround this meson bug on Windows:
# https://github.com/mesonbuild/meson/issues/7413

executable(
  'mujs',
  '../main.c',
  c_args: readline_dep.found() ? '-DHAVE_READLINE' : [],
  dependencies: [mujs_dep, readline_dep],
  install: true,
)
executable(
  'mujs-pp',
  '../pp.c',
  dependencies: mujs_dep,
  install: true,
)
