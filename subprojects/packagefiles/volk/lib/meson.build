lib_incs = [volk_incs, include_directories('.')]
lib_args = volk_args + ['-Dvolk_EXPORTS']
tmpl_dir = meson.project_source_root() / 'tmpl'

volk_machines_h = custom_target(
  input: tmpl_dir / 'volk_machines.tmpl.h',
  output: 'volk_machines.h',
  command: tmpl_command,
  depend_files: tmpl_depends,
)

volk_sources = [volk_machines_h, volk_gen_headers]
foreach name : ['volk', 'volk_cpu', 'volk_machines']
  volk_sources += custom_target(
    input: tmpl_dir / (name + '.tmpl.c'),
    output: name + '.' + src_ext,
    command: tmpl_command,
    depend_files: tmpl_depends,
  )
endforeach

foreach name : ['volk_prefs', 'volk_rank_archs', 'volk_malloc']
  if is_msvc
    volk_sources += configure_file(
      input: name + '.c',
      output: name + '.cc',
      copy: true,
    )
  else
    volk_sources += files(name + '.c')
  endif
endforeach

# Each machine is compiled with the flags of its archs
volk_link_whole = []
machine_defs = []
compiler_info = []
foreach machine : available_machines
  flags = machine_flags[machine]
  machine_src = custom_target(
    input: tmpl_dir / 'volk_machine_xxx.tmpl.c',
    output: 'volk_machine_@0@.@1@'.format(machine, src_ext),
    command: tmpl_command + [machine],
    depend_files: tmpl_depends,
  )
  volk_link_whole += static_library(
    'volk_machine_' + machine,
    machine_src,
    volk_machines_h,
    volk_gen_headers,
    c_args: lib_args + flags,
    cpp_args: lib_args + flags,
    include_directories: lib_incs,
    gnu_symbol_visibility: 'hidden',
  )
  machine_defs += '-DLV_MACHINE_' + machine.to_upper()
  compiler_info += ':::'.join(machine, compiler_name, ' '.join(flags))
endforeach

if 'neonv7' in available_archs
  neon_asm = []
  foreach name : run_command(
    glob_command,
    meson.project_source_root() / 'kernels' / 'volk' / 'asm' / 'neon',
    '*.s',
    check: true,
  ).stdout().strip().split(';')
    neon_asm += files('..' / 'kernels' / 'volk' / 'asm' / 'neon' / name)
  endforeach
  volk_link_whole += static_library(
    'volk_neon_asm',
    neon_asm,
    c_args: arch_flags['neonv7'],
  )
endif

if cpu_family == 'riscv64'
  foreach name : run_command(
    glob_command,
    meson.project_source_root() / 'kernels' / 'volk' / 'asm' / 'riscv',
    '*.s',
    check: true,
  ).stdout().strip().split(';')
    volk_sources += files('..' / 'kernels' / 'volk' / 'asm' / 'riscv' / name)
  endforeach
endif

if have_orc
  foreach name : run_command(
    glob_command,
    meson.project_source_root() / 'kernels' / 'volk' / 'asm' / 'orc',
    '*.orc',
    check: true,
  ).stdout().strip().split(';')
    volk_sources += custom_target(
      input: '..' / 'kernels' / 'volk' / 'asm' / 'orc' / name,
      output: '@BASENAME@.' + src_ext,
      command: [
        orcc,
        '--include',
        'math.h',
        '--implementation',
        '--include',
        'volk/volk_complex.h',
        '-o',
        '@OUTPUT@',
        '@INPUT@',
      ],
    )
  endforeach
endif

constants_conf = configuration_data()
constants_conf.set('prefix', get_option('prefix').replace('\\', '\\\\'))
constants_conf.set('VERSION', meson.project_version())
constants_conf.set(
  'cmake_c_compiler_version',
  '@0@ @1@'.format(cc.get_id(), cc.version()),
)
constants_conf.set('COMPILER_INFO', '\\n'.join(compiler_info))
constants_conf.set('available_machines', ';'.join(available_machines))
volk_sources += configure_file(
  input: 'constants.c.in',
  output: 'constants.' + src_ext,
  configuration: constants_conf,
)

if use_cpu_features
  volk_link_whole += cpu_features_lib
endif

volk_lib = library(
  'volk',
  volk_sources,
  c_args: lib_args + machine_defs,
  cpp_args: lib_args + machine_defs,
  include_directories: lib_incs,
  link_whole: volk_link_whole,
  dependencies: [
    cc.find_library(
      'm',
      required: false,
    ),
    cpu_features_deps,
    orc_dep,
  ],
  gnu_symbol_visibility: 'hidden',
  version: meson.project_version(),
  soversion: soversion,
  install: true,
)

# Otherwise VOLK_API is __declspec(dllimport), which a static library can't satisfy
volk_dep_args = []
if is_msvc and get_option('default_library') == 'static'
  volk_dep_args += '-Dvolk_EXPORTS'
endif

volk_dep = declare_dependency(
  compile_args: volk_dep_args,
  link_with: volk_lib,
  include_directories: volk_public_incs,
  sources: volk_gen_headers,
)
meson.override_dependency('volk', volk_dep)

fmt_dep = dependency(
  'fmt',
  required: get_option('tests'),
)
if fmt_dep.found()
  test_incs = lib_incs
  if is_msvc
    # Shadows cmake/msvc/sys/time.h, which clang-cl rejects
    test_incs = [include_directories('msvc'), test_incs]
  endif
  volk_test_all = executable(
    'volk_test_all',
    'testqa.cc',
    'qa_utils.cc',
    cpp_args: volk_args,
    include_directories: test_incs,
    dependencies: [volk_dep, fmt_dep],
  )
  foreach kernel : kernel_names
    # Its tolerance is at the accuracy limit of the non-FMA SIMD kernels, which
    # makes it flaky; fixed upstream after 3.3.0 (gnuradio/volk@58ef9ce)
    if kernel == 'volk_32f_log2_32f'
      continue
    endif
    test(
      kernel,
      volk_test_all,
      args: kernel,
    )
  endforeach
endif
