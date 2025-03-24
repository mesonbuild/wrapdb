project('kafel', 'c',
  version: '2023.10.04',
  default_options: [
    'c_std=gnu11',
  ])

if host_machine.system() != 'linux'
  error('This platform is not supported. Only Linux is supported.')
endif

if not meson.get_compiler('c').has_header('sys/queue.h')
  error('sys/queue.h is required and cannot be found')
endif

flex = find_program('flex')
bison = find_program('bison')
pkgconf = import('pkgconfig')
sed = find_program('sed')


# The upstream source files (lexer.l and parser.y) have hardcoded output filenames
# using directives like '%option outfile="lexer.c"' and '%output "parser.c"'.
# These directives override any command-line arguments passed to flex/bison,
# causing the generated files to be placed in the wrong location when building with Meson.
#
# As a temporary workaround, we use sed to remove these directives before passing the files
# to flex/bison.

fix_parser = custom_target('fix_parser',
  command: [sed, '-e', '/%output "parser.c"/d', '-e', '/%defines "parser.h"/d', '@INPUT@'],
  capture: true,
  input: 'src/parser.y',
  output: 'parser.y.fixed',
)

fix_lexer = custom_target('fix_lexer',
  command: [sed, '-e', '/%option outfile="lexer.c" header-file="lexer.h"/d', '@INPUT@'],
  capture: true,
  input: 'src/lexer.l',
  output: 'lexer.l.fixed',
)

lexer = custom_target('lexer',
  command: [flex, '-o', '@OUTPUT0@', '--header-file=@OUTPUT1@', '@INPUT@'],
  input: fix_lexer,
  output: ['lexer.c', 'lexer.h'],
  build_by_default: true,
)

parser = custom_target('parser',
  command: [bison, '-o', '@OUTPUT0@', '--defines=@OUTPUT1@', '@INPUT@'],
  input: fix_parser,
  output: ['parser.c', 'parser.h'],
  build_by_default: true,
)

kafel_sources = [
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
  lexer,
  parser
]

kafel_inc = include_directories('include', 'src')

kafel_lib = library('kafel',
  sources: kafel_sources,
  include_directories: kafel_inc,
  install: true,
  gnu_symbol_visibility: 'hidden',
  soversion : 1
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
  kafel_lib,
  description : 'Kafel - seccomp filter generator',
  subdirs : 'kafel'
)
