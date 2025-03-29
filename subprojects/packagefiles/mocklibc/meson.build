project(
  'mocklibc',
  'c',
  version: '1.0',
  license: 'Apache',
  default_options: 'c_std=none',
  meson_version: '>= 0.36.0',
)

soversion = 0
current = 0
revision = 0
libversion = '@0@.@1@.@2@'.format(soversion, current, revision)

example_dir = join_paths(meson.current_source_dir(), 'example')

subdir('src')
subdir('bin')
