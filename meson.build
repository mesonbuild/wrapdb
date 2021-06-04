project('wrapdb')

wraps = get_option('wraps')

foreach w : wraps
  subproject(w)
endforeach

run_target('update',
  command: ['meson', 'subprojects', 'update', '--sourcedir', meson.current_source_dir(), '--reset'] + wraps,
)
