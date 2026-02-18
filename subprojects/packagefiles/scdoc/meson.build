project(
  'scdoc',
  'c',
  version: '1.11.4',
  license: 'MIT',
  meson_version: '>=0.63.0',
  default_options: ['warning_level=3', 'c_std=c99'],
)
incdir = include_directories('include')



sources = files(
  'src/main.c',
  'src/string.c',
  'src/utf8_chsize.c',
  'src/utf8_decode.c',
  'src/utf8_encode.c',
  'src/utf8_fgetch.c',
  'src/utf8_fputch.c',
  'src/utf8_size.c',
  'src/util.c',
)

version_flag = '-DVERSION="' + meson.project_version() + '"'

scdoc_exe = executable(
  'scdoc',
  sources,
  include_directories: incdir,
  c_args: version_flag,
  install: true,
)

meson.override_find_program('scdoc', scdoc_exe)

# Install man with scdoc
# Example command : ./scdoc < scdoc.5.scd > scdoc.5

scdoc_man1 = custom_target(
  'man1',
  output: 'scdoc.1',
  input: 'scdoc.1.scd',
  command: [scdoc_exe],
  feed: true,
  capture: true,
  install: true,
  install_dir: get_option('mandir') / 'man1',
)

scdoc_man5 = custom_target(
  'man5',
  output: 'scdoc.5',
  input: 'scdoc.5.scd',
  command: [scdoc_exe],
  feed: true,
  capture: true,
  install: true,
  install_dir: get_option('mandir') / 'man5',
)
