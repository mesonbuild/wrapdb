project(
  'monocypher', 'c',
  version: '4.0.2',
  license: 'CC0-1.0'
)

monocypher_lib = library(
  'monocypher', [
    'src/monocypher.c',
    'src/optional/monocypher-ed25519.c',
  ],
  include_directories: ['src', 'src/optional'],
  install: true,
)

monocypher_dep = declare_dependency(
  include_directories: ['src', 'src/optional'],
  link_with: monocypher_lib,
)
