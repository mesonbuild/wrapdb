project(
  'vo-aacenc',
  'c',
  default_options: [
    'c_std=c11',  # c99 is not recognised by MSVC
    'b_lundef=true',
    'pkgconfig.relocatable=true',
  ],
  license: 'Apache-2.0',
  version: '0.1.3',
  # Need 1.2.0 for cc.compiles() with a file generated at setup time. This is only used on arm, so the CI will warn on x86_64.
  meson_version: '>= 1.2.0',
)

armv7neon = false
armv5e = false

cc = meson.get_compiler('c')
python3 = import('python').find_installation()
makedef = find_program(
  'meson/makedef.py',
  native: true,
)
system = host_machine.system()
cpu = host_machine.cpu()

if cpu == 'arm'
  asm_as_checks = [
    ['qadd r0, r0, r0', 'armv5te'],
    ['vadd.i16 q0, q0, q0', 'neon'],
  ]
  foreach check : asm_as_checks
    f = configure_file(
      command: [
        python3,
        '-c',
        'import sys; print(sys.argv[1])',
        '@0@'.format(check[0]),
      ],
      input: files('configure'),
      output: '@0@.S'.format(check[1]),
      capture: true,
    )
    set_variable(
      check[1],
      cc.compiles(
        f,
        name: check[1],
      ),
    )
  endforeach
endif

cflags = []

if armv7neon
  cflags += [
    '-DARMV5E',
    '-DARMV7Neon',
    '-DARM_INASM',
    '-DARMV5_INASM',
    '-DARMV6_INASM',
  ]
elif armv5e
  cflags += ['-DARMV5E', '-DARM_INASM', '-DARMV5_INASM']
endif

# Disable all warnings emitted by Clang
cflags += cc.get_supported_arguments(
  '-Wno-unused-but-set-variable',
  '-Wno-unused-function',
  '-Wno-unused-variable',
  '-Wno-parentheses-equality',
  '-Wno-misleading-indentation',
)

libvo_aacenc_includes = []

subdir('aacenc')
subdir('common')

makedef_args = [makedef, '--regex', '^(vo|cmn)']

if system in ['darwin', 'ios']
  makedef_args += ['--os', 'darwin']
elif system in ['windows', 'cygwin']
  makedef_args += ['--os', 'win']
else
  makedef_args += ['--os', 'linux']
endif

if cc.symbols_have_underscore_prefix()
  makedef_args += ['--prefix', '_']
else
  makedef_args += ['--prefix', '']
endif

libvo_def = configure_file(
  command: [makedef_args, '--list', '@INPUT@'],
  input: files('vo-aacenc.sym'),
  output: 'vo-aacenc.def',
  capture: true,
)

libvo_ver = configure_file(
  command: [makedef_args, '--list', '@INPUT@'],
  input: files('vo-aacenc.sym'),
  output: 'vo-aacenc.ver',
  capture: true,
)

version_script = meson.current_build_dir() / 'vo-aacenc.ver'

if host_machine.system() in ['darwin', 'ios']
  vflag = '-Wl,-exported_symbols_list,@0@'.format(version_script)
else
  vflag = '-Wl,--version-script,@0@'.format(version_script)
endif

libvo_aacenc = library(
  'vo-aacenc',
  libvo_aacenc_sources,
  c_args: cflags,
  link_args: cc.get_supported_link_arguments([vflag]),
  link_depends: libvo_ver,
  dependencies: cc.find_library(
    'm',
    required: false,
  ),
  include_directories: libvo_aacenc_includes,
  vs_module_defs: libvo_def,
  install: true,
  version: meson.project_version(),
)

libvo_aacenc_dep = declare_dependency(
  link_with: libvo_aacenc,
  include_directories: libvo_aacenc_includes,
)

meson.override_dependency('vo-aacenc', libvo_aacenc_dep)

if not get_option('example').disabled()
  example = executable(
    'aac-enc',
    files('aac-enc.c', 'wavreader.c'),
    include_directories: include_directories('.'),
    dependencies: libvo_aacenc_dep,
    install: false,
  )
endif

pkg = import('pkgconfig')

pkg.generate(
  libvo_aacenc,
  filebase: meson.project_name(),
  name: 'VisualOn AAC Encoder',
  description: 'AAC codec library',
)
