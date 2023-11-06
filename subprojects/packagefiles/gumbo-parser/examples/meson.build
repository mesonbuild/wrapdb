examples_opt = get_option('examples').require(
  cpp_available,
  error_message: 'missing C++ compiler',
)

if examples_opt.disabled()
  subdir_done()
endif

foreach _src : [
  'clean_text.cc',
  'find_links.cc',
  'get_title.c',
  'positions_of_class.cc',
  'prettyprint.cc',
  'serialize.cc',
]
  executable(
    _src.split('.')[0],
    _src,
    dependencies: gumbo_dep,
    c_args: '-D_POSIX_C_SOURCE=200112L',
  )
endforeach
