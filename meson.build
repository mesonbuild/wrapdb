project('wrapdb',
  meson_version: '>=0.55.0'
)

wraps = get_option('wraps')

foreach w : wraps
  subproject(w)
endforeach

run_target('update',
  command: ['meson', 'subprojects', 'update', '--sourcedir', meson.current_source_dir(), '--reset'] + wraps,
)
