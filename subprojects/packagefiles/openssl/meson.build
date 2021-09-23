project(
  'openssl',
  'c',
  version: '3.0.2',
  license : 'Apache-2.0',
  meson_version: '>= 0.64.0',
  default_options: [
    'warning_level=1',
  ],
)

soversion = meson.project_version().split('.')[0]

cc = meson.get_compiler('c')

dependencies = [
  # TODO: Make this optionally added once we have threading configurable via options
  dependency('threads'),
]
c_args = [
  # Compile out hardware engines. Most are stubs that dynamically load
  # the real driver but that poses a security liability when an attacker
  # is able to create a malicious DLL in one of the default search paths.
  '-DOPENSSL_NO_HW',
]

is_bsd = host_machine.system() in ['dragonfly', 'freebsd', 'netbsd', 'openbsd']
is_darwin = host_machine.system() == 'darwin'
is_linux = host_machine.system() in ['linux', 'android']
is_sunos = host_machine.system() == 'sunos'
is_windows = host_machine.system() == 'windows'

is_x86 = host_machine.cpu_family() == 'x86'
is_x86_64 = host_machine.cpu_family() == 'x86_64'
is_aarch64 = host_machine.cpu_family() == 'aarch64'
is_mips64 = host_machine.cpu_family() == 'mips64'
is_s390x = host_machine.cpu_family() == 's390x'
is_arm = host_machine.cpu_family() == 'arm'
is_ppc = host_machine.cpu_family() == 'ppc'
is_ppc64 = host_machine.cpu_family() == 'ppc64'
is_riskv64 = host_machine.cpu_family() == 'riscv64'

asm_opt = get_option('asm')
asm = 'asm'
if is_bsd
  if is_x86
    arch_subdir = 'BSD-x86'
  elif is_x86_64
    arch_subdir = 'BSD-x86_64'
  else
    asm = 'no-asm'
  endif
elif is_darwin
  if is_aarch64
    arch_subdir = 'darwin64-arm64-cc'
  elif is_x86_64
    arch_subdir = 'darwin64-x86_64-cc'
  elif is_x86
    arch_subdir = 'darwin-i386-cc'
  else
    asm = 'no-asm'
  endif
elif is_linux
  if is_mips64
    arch_subdir = 'linux64-mips64'
  elif is_s390x
    arch_subdir = 'linux64-s390x'
  elif is_aarch64
    arch_subdir = 'linux-aarch64'
  elif is_arm
    arch_subdir = 'linux-armv4'
  elif is_ppc
    arch_subdir = 'linux-ppc'
  elif is_ppc64 and host_machine.endian() == 'big'
    arch_subdir = 'linux-ppc64'
  elif is_ppc64
    arch_subdir = 'linux-ppc64le'
  elif is_x86
    arch_subdir = 'linux-x32'
  elif is_x86_64
    arch_subdir = 'linux-x86_64'
  else
    asm = 'no-asm'
  endif
elif is_sunos
  if is_x86_64
    arch_subdir = 'solaris64-x86_64-gcc'
  elif is_x86
    arch_subdir = 'solaris-x86-gcc'
  else
    asm = 'no-asm'
  endif
elif is_windows
  if is_x86 or is_x86_64
    arch_subdir = is_x86_64 ? 'VC-WIN64A' : 'VC-WIN32'
    if not add_languages('nasm', native: false, required: asm_opt)
      asm = 'no-asm'
    endif
  else
    asm = 'no-asm'
  endif
else
  asm = 'no-asm'
endif

if asm_opt.disabled()
  asm = 'no-asm'
elif asm_opt.enabled() and asm == 'no-asm'
  error('Unsupported arch+OS combo: ' + host_machine.cpu_family() + ' + ' + host_machine.system())
endif

if asm == 'no-asm'
  c_args += ['-DOPENSSL_NO_ASM']
endif

# Make sure to generate configs in case they are not already
fs = import('fs')
if not fs.exists('generated-config/archs' / arch_subdir)
  message('Generating OpenSSL configs...')
  run_command('generator.py', meson.current_source_dir(), '--arch', arch_subdir, '--asm', asm, check: true)
endif

subdir('generated-config/archs' / arch_subdir / asm)

# Build options specific to OS, engines are disabled on purpose for the same reasons as `OPENSSL_NO_HW` above
if is_windows
  c_args += [
    ## default of Win. See INSTALL in openssl repo.
    '-DOPENSSLDIR="C:\\Program Files\\Common Files\\SSL"',
    '-DENGINESDIR="NUL"',
    '-DMODULESDIR="NUL"',
    '-DOPENSSL_SYS_WIN32', '-DWIN32_LEAN_AND_MEAN', '-DL_ENDIAN',
    '-D_CRT_SECURE_NO_DEPRECATE', '-DUNICODE', '-D_UNICODE',
  ]
  if cc.get_argument_syntax() == 'msvc'
    c_args += [
      '-wd4090', '-Gs0', '-GF', '-Gy', '-nologo',
    ]
  endif
elif is_darwin
  c_args += [
    '-DOPENSSLDIR="/System/Library/OpenSSL/"',
    '-DENGINESDIR="/dev/null"',
    '-DMODULESDIR="/dev/null"',
  ]
  c_args += [
    '-Wno-missing-field-initializers',
  ]
elif is_sunos
  c_args += [
   '-DOPENSSLDIR="/etc/ssl"',
   '-DENGINESDIR="/dev/null"',
   '-DMODULESDIR="/dev/null"',
   '-D__EXTENSIONS__'
 ]
else
  # Linux and others
  c_args += [
    '-DOPENSSLDIR="/etc/ssl"',
    '-DENGINESDIR="/dev/null"',
    '-DMODULESDIR="/dev/null"',
  ]
  c_args += [
    '-Wno-missing-field-initializers',
  ]
  if cc.get_id() != 'clang'
    c_args += [
      '-Wno-old-style-declaration',
    ]
  endif
endif

foreach library: openssl_libraries
  dependencies += [
    cc.find_library(library),
  ]
endforeach

# We may need to add some defines for static builds
if get_option('default_library') == 'static'
  c_args += [
    '-DOSSL_CRYPTO_DSO_CONF_H',
    '-DDSO_NONE',
    '-DDSO_EXTENSION=".so"',
    '-DOPENSSL_NO_DSO',
  ]
endif

libcrypto_kwargs = {}
libssl_kwargs = {}
if is_windows
  windows = import('windows')
  libcrypto_sources += windows.compile_resources(libcrypto_winres)
  libssl_sources += windows.compile_resources(libssl_winres)
  openssl_sources += windows.compile_resources(openssl_winres)
  libcrypto_kwargs += {'vs_module_defs': libcrypto_vs_module_defs}
  libssl_kwargs += {'vs_module_defs': libssl_vs_module_defs}
endif

libcrypto_lib = library(
  'crypto',
  dependencies: dependencies,
  sources: libcrypto_sources,
  include_directories: [libcrypto_includes],
  c_args: [c_args, libcrypto_c_args],
  link_args: libcrypto_link_args,
  kwargs: libcrypto_kwargs,
  soversion: soversion,
  name_prefix: 'lib',
  install: true,
)

libcrypto_dep = declare_dependency(
  include_directories: 'include',
  dependencies: dependencies,
  link_with: libcrypto_lib,
)

libssl_lib = library(
  'ssl',
  dependencies: dependencies + [libcrypto_dep],
  sources: libssl_sources,
  include_directories: [libssl_includes],
  c_args: [c_args, libssl_c_args],
  link_args: libssl_link_args,
  kwargs: libssl_kwargs,
  soversion: soversion,
  name_prefix: 'lib',
  install: true,
)

libssl_dep = declare_dependency(
  include_directories: 'include',
  dependencies: dependencies + [libcrypto_dep],
  link_with: libssl_lib,
)

openssl_dep = declare_dependency(
  dependencies: [libcrypto_dep, libssl_dep],
)

cli_opt = get_option('build_cli')

openssl_cli = executable(
  'openssl',
  build_by_default: cli_opt,
  dependencies: dependencies + [openssl_dep],
  sources: openssl_sources,
  include_directories: [openssl_includes],
  c_args: [c_args, openssl_c_args],
  install: cli_opt,
)
