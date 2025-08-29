project(
  'wrapdb',
  meson_version: '>=0.58.0',
)

if (
  meson.version().version_compare('<1.9.1') and
  meson.version().version_compare('>=1.8.4')
)
  # ensure c_std= and cpp_std= are not ignored in subprojects
  # https://github.com/mesonbuild/meson/issues/14939
  add_languages(
    'c',
    'cpp',
    native: false,
  )
endif

wraps = get_option('wraps')

foreach w : wraps
  subproject(w)
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
