project('kafel', 'c',
  version: '2023.10.10',
  default_options: [
    'c_std=gnu11',
  ])

flex = find_program('flex', required: true)
bison = find_program('bison', required: true)

lexer_gen = custom_target(
  'lexer',
  input: 'src/lexer.l',
  output: ['lexer.c', 'lexer.h'],
  command: [flex, '@INPUT@'],
)

parser_gen = custom_target(
  'parser',
  input: 'src/parser.y',
  output: ['parser.c', 'parser.h'],
  command: [bison, '-o', 'parser.c', '@INPUT@'],
)

generated_sources = [lexer_gen, parser_gen]

kafel_inc = include_directories('include', 'src')

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
) + generated_sources

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
