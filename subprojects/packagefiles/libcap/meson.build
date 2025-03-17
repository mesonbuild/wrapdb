project('libcap', 'c',
  version: '2.75',
  license: 'BSD',
  default_options: [
    'c_std=gnu11',
  ])

incdir = include_directories('libcap', 'libcap/include')

libcap_sources = files(
  'libcap/cap_alloc.c',
  'libcap/cap_extint.c',
  'libcap/cap_file.c',
  'libcap/cap_flag.c',
  'libcap/cap_proc.c',
  'libcap/cap_text.c',
  'libcap/cap_syscalls.c'
)

libcap = library('cap',
  sources: libcap_sources,
  include_directories: incdir,
  install: true)

libcap_dep = declare_dependency(
  include_directories: incdir,
  link_with: libcap)
