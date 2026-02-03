project(
  'jitterentropy',
  'c',
  version: '3.6.3',
  meson_version: '>=0.63.0',
  license: 'BSD-3-Clause OR GPL-2.0-only',
)

pkg = import('pkgconfig')

tests_opt = get_option('tests').disable_auto_if(meson.is_subproject())
enable_internal_timer_opt = get_option('enable_internal_timer').disable_auto_if(
  host_machine.system() == 'windows',
)
environments_opt = get_option('environments')

env_defines = {
  'aws-lc': 'AWSLC',
  'libgcrypt': 'LIBGCRYPT',
  'openssl': 'OPENSSL',
}

src = files(
  'src/jitterentropy-gcd.c',
  'src/jitterentropy-health.c',
  'src/jitterentropy-noise.c',
  'src/jitterentropy-sha3.c',
  'src/jitterentropy-timer.c',
)

inc = include_directories('.')
private_inc = include_directories('src')

# jitterentropy doesn't have a configuration header, so these defines also need
# to be passed to consumers.
c_args = []
deps = []
private_deps = []

foreach env : environments_opt
  c_args += '-D@0@=1'.format(env_defines[env])
endforeach

if environments_opt.contains('aws-lc')
  deps += [dependency('aws-lc')]
endif

if environments_opt.contains('libgcrypt')
  deps += [dependency('libgcrypt')]
endif

if environments_opt.contains('openssl')
  deps += [dependency('openssl')]
endif

if enable_internal_timer_opt.allowed()
  c_args += '-DJENT_CONF_ENABLE_INTERNAL_TIMER=1'
  private_deps += [dependency('threads')]
endif

libjitterentropy_base = static_library(
  'jitterentropy-base',
  'src/jitterentropy-base.c',
  include_directories: [inc, private_inc],
  dependencies: [deps, private_deps],
  c_args: c_args,
  install: false,
  gnu_symbol_visibility: 'hidden',
  # CPU jitter should not be optimized, it reduces the entropy quality.
  override_options: ['optimization=0'],
)

libjitterentropy = library(
  'jitterentropy',
  src,
  include_directories: [inc, private_inc],
  dependencies: [deps, private_deps],
  link_whole: [libjitterentropy_base],
  c_args: c_args,
  install: true,
  version: meson.project_version(),
  gnu_symbol_visibility: 'hidden',
)

jitterentropy_dep = declare_dependency(
  dependencies: deps,
  link_with: libjitterentropy,
  include_directories: inc,
  compile_args: c_args,
)

install_headers(
  'jitterentropy.h',
  'jitterentropy-base-user.h',
  'arch/jitterentropy-base-power.h',
  'arch/jitterentropy-base-s390.h',
  'arch/jitterentropy-base-windows.h',
  'arch/jitterentropy-base-x86.h',
  preserve_path: true,
)

install_man(
  'doc/jitterentropy.3',
)

meson.override_dependency(
  'jitterentropy',
  jitterentropy_dep,
)

pkg.generate(
  libjitterentropy,
  url: 'https://www.chronox.de/jent/',
  extra_cflags: c_args,
)

if tests_opt.allowed()
  testcases = {
    'gcd': {
      'sources': files('src/jitterentropy-gcd.c', 'tests/gcd/gcd.c'),
    },
  }

  foreach name, kwargs : testcases
    test_exe = executable(
      'test-@0@'.format(name),
      kwargs: kwargs,
      include_directories: [inc, private_inc],
      dependencies: [jitterentropy_dep],
    )

    test(
      'test-@0@'.format(name),
      test_exe,
      suite: 'jitterentropy',
    )
  endforeach
endif
