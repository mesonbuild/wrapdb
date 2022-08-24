project('wrapdb',
  meson_version: '>=0.55.0',
  default_options: ['cpp_std=c++17'],
)

wraps = get_option('wraps')

foreach w : wraps
  sub = subproject(w)
  if wraps.length() == 1
    foreach d: get_option('depvars')
      v = sub.get_variable(d)
    endforeach
  endif
endforeach


run_target('update',
  command: ['meson', 'subprojects', 'update', '--sourcedir', meson.current_source_dir(), '--reset'] + wraps,
)
