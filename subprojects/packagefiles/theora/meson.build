project(
  'theora',
  'c',
  'cpp',
  version: '1.2.0',
  meson_version: '>= 0.49.0',
  license: 'BSD-3-Clause',
  default_options: ['c_std=c11'],
)

theora_libversion = '0.3.10'
theora_darwin_version = ['4.0.0', '4.10.0']
theoradec_libversion = '1.1.4'
theoradec_darwin_version = ['3.0.0', '3.4.0']
theoraenc_libversion = '1.1.2'
theoraenc_darwin_version = ['3.0.0', '3.2.0']

conf = configuration_data()

valgrind_testing = get_option('valgrind-testing')

valgrind_exe = find_program(
  'valgrind',
  required: valgrind_testing,
)

if valgrind_exe.found()
  add_test_setup(
    'valgrind',
    exe_wrapper: [
      valgrind_exe,
      '-q',
      '--leak-check=yes',
      '--show-reachable=yes',
      '--num-callers=100',
    ],
  )
endif

cc = meson.get_compiler('c')

compile_args = cc.get_supported_arguments(
  '-Wno-parentheses',
  '-Wno-shift-op-parentheses',
  '-Wno-shift-negative-value',
)

m_dep = cc.find_library(
  'm',
  required: false,
)

if get_option('collect-metrics')
  add_project_arguments(
    '-DOC_COLLECT_METRICS',
    language: 'c',
  )
endif

ogg_dep = dependency(
  'ogg',
  version: '>= 1.1',
)

vorbis_dep = dependency(
  'vorbis',
  version: '>= 1.0.1',
  required: false,
  disabler: true,
)

vorbisenc_dep = dependency(
  'vorbisenc',
  version: '>= 1.0.1',
  required: false,
  disabler: true,
)

sdl_dep = dependency(
  'sdl',
  required: false,
  disabler: true,
)
if not sdl_dep.found()
  message('*** Unable to find SDL -- Not compiling example players ***')
endif

if (cc.has_header('sys/soundcard.h')
or cc.has_header('soundcard.h')
or cc.has_header('machine/soundcard.h')
)
  if host_machine.system() == 'openbsd'
    oss_dep = dependency(
      'ossaudio',
      required: false,
      disabler: true,
    )
  else
    oss_dep = declare_dependency()
  endif
else
  oss_dep = disabler()
endif

if not oss_dep.found()
  message('OSS audio support not found -- not compiling player_example')
endif

libpng_dep = dependency(
  'libpng',
  required: false,
)

if cc.has_header('unistd.h')
  unistd_dep = declare_dependency()
else
  unistd_dep = disabler()
endif

cairo_dep = dependency(
  'cairo',
  required: get_option('telemetry'),
)
if cairo_dep.found()
  conf.set('HAVE_CAIRO', true)
endif

mem_constraint = get_option('mem-constraint')

if mem_constraint.enabled()
  conf.set(
    'HAVE_MEMORY_CONSTRAINT',
    language: 'c',
  )
endif

asm = not get_option('asm').disabled()
if asm
  if host_machine.cpu_family() == 'x86_64'
    conf.set('CPU_x86_64', true)
    if cc.get_argument_syntax() != 'msvc'
      conf.set('OC_X86_ASM', true)
      conf.set('OC_X86_64_ASM', true)
    endif
  elif host_machine.cpu_family() == 'x86'
    conf.set('CPU_x86_32', true)
    conf.set('OC_X86_ASM', true)
  endif
endif

config_h = configure_file(
  configuration: conf,
  output: 'config.h',
)

config_dep = declare_dependency(
  sources: config_h,
)

add_project_arguments(
  '-DHAVE_CONFIG_H',
  language: 'c',
)

pkg = import('pkgconfig')
windows = import('windows')

subdir('include')

subdir('lib')

examples = get_option('examples')

if examples.auto() or examples.enabled()
  subdir('examples')
endif

subdir('tests')

doc = get_option('doc')

doc_root_dir = meson.current_source_dir()

doxygen_exe = find_program(
  'doxygen',
  required: doc,
  disabler: true,
)

subdir('doc')

spec = get_option('spec')

if spec.auto() or spec.enabled()
  # Note: unlike the original autotools script, here we use
  # latexmk to do the dependency management for us.
  # This implicates that we've got to copy spec.{tex,bib}
  # to the build folder in /doc/spec/ to make all files
  # live in the same folder.
  latexmk_exe = find_program(
    'latexmk',
    required: spec,
  )
  transfig_exe = find_program(
    'fig2dev',
    required: spec,
  )
  # used indirectly by latexmk
  pdflatex = find_program(
    'pdflatex',
    required: spec,
  )
  bibtex = find_program(
    'bibtex',
    required: spec,
  )

  if (latexmk_exe.found()
and pdflatex.found()
and bibtex.found()
and transfig_exe.found()
)
    check_needed_tex_packages = find_program(
      'doc/spec/check-needed-tex-packages.py',
      required: true,
    )
    test_tex_packages = find_program(
      'doc/spec/test-tex-packages.py',
      required: true,
    )

    message(
      'Checking for packages in @0@...'.format(
        meson.current_source_dir() / 'doc/spec/spec.tex',
      ),
    )

    packages = run_command(
      check_needed_tex_packages,
      capture: true,
      check: true,
    ).stdout().split()

    tex_pkg_ok = true

    foreach pkg : packages
      message('for Tex package @0@'.format(pkg))

      pkg_test = run_command(test_tex_packages, '--pdflatex', pdflatex, pkg)
      if pkg_test.returncode() != 0
        message = 'The \'@0@\' TeX package is missing or broken'.format(pkg)

        if spec.enabled()
          error(message)
        else
          warning(message)
          tex_pkg_ok = false
        endif
        break
      endif
    endforeach
  else
    tex_pkg_ok = false
  endif

  if tex_pkg_ok and meson.project_version() > '1.2.0alpha1'
    # libtheora <= 1.2.0alpha1 has a tex file which is incompatible
    # with TeX distributions < 2015 at the least.
    # See commit fbb275803696085225c310773474ef4dcf8a4528.
    subdir('doc/spec')
  else
    message('*** Format Specification will not be built.')
  endif
endif
