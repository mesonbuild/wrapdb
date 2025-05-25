project('libcap', 'c',
  version: '2.76',
  license: 'BSD-3-Clause',
  default_options: [
    'c_std=gnu11',
    'buildtype=release']
  )

incdir = include_directories('libcap/include')
gen_script = files('generate_cap_names.sh')

cap_names_h = custom_target('cap_names.h',
  output: 'cap_names.h',
  input: 'libcap/cap_names.header',
  command: [
    executable('_makenames',
      sources: custom_target('patched_makenames.c',
        input: 'libcap/_makenames.c',
        output: 'patched_makenames.c',
        command: [gen_script, 'patch', '@INPUT@', '@OUTPUT@'],
        install: false),
      include_directories: incdir,
      native: true),
    '@INPUT@'
  ],
  capture: true)

libcap = library('cap',
  sources: [
    'libcap/cap_alloc.c',
    'libcap/cap_extint.c',
    'libcap/cap_file.c',
    'libcap/cap_flag.c',
    'libcap/cap_proc.c',
    'libcap/cap_text.c',
    'libcap/cap_syscalls.c',
    cap_names_h
  ],
  include_directories: incdir,
  install: true)

libcap_dep = declare_dependency(
  include_directories: incdir,
  link_with: libcap)
