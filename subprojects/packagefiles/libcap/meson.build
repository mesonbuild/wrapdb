project('libcap', 'c',
  version: '2.75',
  license: 'BSD',
  default_options: [
    'c_std=gnu11',
  ])

incdir = include_directories('libcap/include')

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

pam_cap = get_option('pam_cap')
if pam_cap != 'no'
  pam_sources = files(
    'pam_cap/pam_cap.c',
  )
  pam = library('pam_cap',
    sources: pam_sources,
    include_directories: incdir,
    dependencies: [dependency('pam')],
    install: true)
endif

if get_option('tests')
  test_sources = files(
    'tests/test_cap.c',
    'tests/test_libcap.c',
  )
  test_exe = executable('test_libcap',
    sources: test_sources,
    dependencies: [libcap_dep])

  test('libcap_tests', test_exe)
endif

if get_option('progs')
  progs_sources = files(
    'progs/capsh.c',
    'progs/getcap.c',
    'progs/getpcaps.c',
    'progs/setcap.c',
  )
  foreach prog : ['capsh', 'getcap', 'getpcaps', 'setcap']
    executable(prog,
      sources: 'progs/@0@.c'.format(prog),
      dependencies: [libcap_dep],
      install: true)
  endforeach
endif

if get_option('doc')
  install_man('doc/capsh.8', 'doc/getcap.8', 'doc/getpcaps.8', 'doc/setcap.8')
endif
