project(
  'wrapdb',
  meson_version: '>=0.58.0',
  default_options: ['cpp_std=c++17'],
)

wraps = get_option('wraps')

foreach w : wraps
  sub = subproject(w)
endforeach

foreach name : get_option('depnames')
  dep = dependency(name)
  assert(dep.type_name() == 'internal')
endforeach

foreach name : get_option('prognames')
  prog = find_program(name)
  assert(
    prog.full_path().startswith(meson.global_build_root()) or prog.full_path().startswith(
      meson.global_source_root(),
    ),
  )
endforeach

run_target(
  'update',
  command: [
    'meson',
    'subprojects',
    'update',
    '--sourcedir',
    meson.current_source_dir(),
    '--reset',
  ] + wraps,
)
