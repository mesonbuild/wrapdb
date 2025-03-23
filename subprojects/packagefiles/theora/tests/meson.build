theora_libs = [libtheora]
theoradec_libs = [libtheoradec]
theoraenc_libs = [libtheoraenc, libtheoradec]

tests = {}

# dummy call tests for the current api
noop = executable(
  'noop',
  files('noop.c'),
  c_args: compile_args,
  link_with: theoraenc_libs,
  dependencies: [m_dep, ogg_dep, config_dep],
  include_directories: incdir,
)

tests += {
  'noop': noop,
}

# dummy call tests for the pre-1.0 legacy api with current link line
noop_theoraenc = executable(
  'noop_theoraenc',
  files('noop_theora.c'),
  c_args: compile_args,
  link_with: theoraenc_libs,
  dependencies: [m_dep, ogg_dep, config_dep],
  include_directories: incdir,
)

tests += {
  'noop_theoraenc': noop_theoraenc,
}

# dummy call tests for the pre-1.0 legacy api with legacy link line
noop_theora = executable(
  'noop_theora',
  files('noop_theora.c'),
  c_args: compile_args,
  link_with: theora_libs,
  dependencies: [m_dep, ogg_dep, config_dep],
  include_directories: incdir,
)

tests += {
  'noop_theora': noop_theora,
}

# comment utilities for the current api
comment = executable(
  'comment',
  files('comment.c'),
  c_args: compile_args,
  link_with: theoradec_libs,
  dependencies: [m_dep, ogg_dep, config_dep],
  include_directories: incdir,
)

tests += {
  'comment': comment,
}

# comment utilities for the legacy api and current lib
comment_theoradec = executable(
  'comment_theoradec',
  files('comment.c'),
  c_args: compile_args,
  link_with: theoradec_libs,
  dependencies: [m_dep, ogg_dep, config_dep],
  include_directories: incdir,
)

tests += {
  'comment_theoradec': comment_theoradec,
}

# comment utilities for the legacy api and legacy lib
comment_theora = executable(
  'comment_theora',
  files('comment_theora.c'),
  c_args: compile_args,
  link_with: theora_libs,
  dependencies: [m_dep, ogg_dep, config_dep],
  include_directories: incdir,
)

tests += {
  'comment_theora': comment_theora,
}

granulepos = executable(
  'granulepos',
  files('granulepos.c'),
  c_args: compile_args,
  link_with: theoraenc_libs,
  dependencies: [m_dep, ogg_dep, config_dep],
  include_directories: incdir,
)

tests += {
  'granulepos': granulepos,
}

granulepos_theoraenc = executable(
  'granulepos_theoraenc',
  files('granulepos_theora.c'),
  c_args: compile_args,
  link_with: theoraenc_libs,
  dependencies: [m_dep, ogg_dep, config_dep],
  include_directories: incdir,
)

tests += {
  'granulepos_theoraenc': granulepos_theoraenc,
}

granulepos_theora = executable(
  'granulepos_theora',
  files('granulepos_theora.c'),
  c_args: compile_args,
  link_with: theora_libs,
  dependencies: [m_dep, ogg_dep, config_dep],
  include_directories: incdir,
)

tests += {
  'granulepos_theora': granulepos_theora,
}

foreach name, exe : tests
  test(name, exe)
endforeach
