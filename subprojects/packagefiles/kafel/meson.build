project('kafel', 'c',
  version: '2023.10.10',
  default_options: [
    'c_std=gnu11',
  ])

flex = find_program('flex')
bison = find_program('bison')
pkgconf = import('pkgconfig')

run_command(flex, '--outfile=lexer.c', 'src/lexer.l', check: true)
run_command(bison, '-o=parser.c', 'src/parser.y', check: true)

kafel_sources = files(
  'src/kafel.c',
  'src/context.c',
  'src/codegen.c',
  'src/expression.c',
  'src/includes.c',
  'src/parser_types.c',
  'src/policy.c',
  'src/range_rules.c',
  'src/syscall.c',
  'src/syscalls/amd64_syscalls.c',
  'src/syscalls/i386_syscalls.c',
  'src/syscalls/aarch64_syscalls.c',
  'src/syscalls/mipso32_syscalls.c',
  'src/syscalls/mips64_syscalls.c',
  'src/syscalls/riscv64_syscalls.c',
  'src/syscalls/arm_syscalls.c',
  'lexer.c',
  'parser.c'
)

kafel_inc = include_directories('include', 'src')

kafel_lib = library('kafel',
  sources: kafel_sources,
  include_directories: kafel_inc,
  install: true
)

kafel_dep = declare_dependency(
  include_directories: kafel_inc,
  link_with: kafel_lib
)

dump_policy_bpf_sources = files(
  'tools/dump_policy_bpf/disasm.c',
  'tools/dump_policy_bpf/main.c',
  'tools/dump_policy_bpf/print.c',
)

dump_policy_bpf_exe = executable('dump_policy_bpf',
  sources: dump_policy_bpf_sources,
  dependencies: [kafel_dep],
  install: true
)

install_headers('include/kafel.h', subdir: 'kafel')

meson.override_find_program('dump_policy_bpf', dump_policy_bpf_exe)
meson.override_dependency('kafel', kafel_dep)

pkgconf.generate(
  name : 'kafel',
  description : 'Kafel - seccomp filter generator',
  version : meson.project_version(),
  filebase : 'kafel',
  subdirs : 'kafel',
  libraries : kafel_lib
)
