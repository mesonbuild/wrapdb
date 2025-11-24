# We build those executables here and not in the parent
# directory to workaround this meson bug on Windows:
# https://github.com/mesonbuild/meson/issues/7413

mujs = executable(
  'mujs',
  '../main.c',
  c_args: readline_dep.found() ? '-DHAVE_READLINE' : [],
  dependencies: [mujs_dep, readline_dep],
  override_options: override_opts,
  install: true,
)
meson.override_find_program('mujs', mujs)

mujs_pp = executable(
  'mujs-pp',
  '../pp.c',
  dependencies: mujs_dep,
  override_options: override_opts,
  install: true,
)
meson.override_find_program('mujs-pp', mujs_pp)
