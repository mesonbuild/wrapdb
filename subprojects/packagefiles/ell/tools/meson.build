tools = [
  'certchain-verify',
  'genl-discover',
  'genl-watch',
  'genl-request',
  'gpio',
]

if get_option('tools')
  foreach tool : tools
    exe = executable(
      tool,
      '@0@.c'.format(tool),
      include_directories: include_directories('..'),
      dependencies: libell_private_dep,
      install: false,
    )
  endforeach
endif
