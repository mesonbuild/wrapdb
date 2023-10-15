project(
  'openssl',
  'c',
  version: '3.0.8',
  license : 'Apache-2.0',
  meson_version: '>= 0.55',
  default_options: [
    'warning_level=1',
  ],
)

# Make sure to generate configs in case they are not already
fs = import('fs')
if not fs.exists('generated-config')
  message('Generating OpenSSL configs...')

  if host_machine.system() != 'linux'
    error('Generator only works on Linux, other platforms are not supported')
  endif

  bash = find_program('bash')
  run_command(
    bash,
    'generator.sh',
    check: true,
    env: ['OPENSSL_VERSION=' + meson.project_version()],
  )
endif

include_directories = [
  'include',
  'crypto',
  'crypto/modes',
  'crypto/ec/curve448',
  'crypto/ec/curve448/arch_32',
  'providers/common/include',
  'providers/implementations/include',
]

compiler = meson.get_compiler('c')

dependencies = [
  # TODO: Make this optionally added once we have threading configurable via options
  dependency('threads'),
]
defines = [
  # Compile out hardware engines. Most are stubs that dynamically load
  # the real driver but that poses a security liability when an attacker
  # is able to create a malicious DLL in one of the default search paths.
  'OPENSSL_NO_HW',
]
c_args = []

asm_opt = get_option('asm')

if asm_opt.disabled()
  gas_or_nasm = false
else
  gas_or_nasm = (
    find_program('as', required: false).found() or
    find_program('nasm', required: false).found()
  )
endif

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
is_ppc64 = host_machine.cpu_family() == 'ppc64'
is_riskv64 = host_machine.cpu_family() == 'riscv64'

if gas_or_nasm
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
    elif is_ppc64
      arch_subdir = 'linux-ppc64le'
    elif is_x86
      arch_subdir = 'linux-elf'
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
    if is_x86
      warning('x86 + windows combo does not support ASM yet, please contribute')
      asm = 'no-asm'
      # TODO: Port this for Windows and uncomment
      # arch_subdir = 'VC-WIN32'
      # asm = 'asm'
      #'rules': [
      #  {
      #    'rule_name': 'Assemble',
      #    'extension': 'asm',
      #    'inputs': [],
      #    'outputs': [
      #      '<(INTERMEDIATE_DIR)/<(RULE_INPUT_ROOT).obj',
      #    ],
      #    'action': [
      #      'nasm.exe',
      #      '-f win32',
      #      '-o', '<(INTERMEDIATE_DIR)/<(RULE_INPUT_ROOT).obj',
      #      '<(RULE_INPUT_PATH)',
      #    ],
      #  }
      #],
    elif is_x86_64
      warning('x86_64 + windows combo does not support ASM yet, please contribute')
      asm = 'no-asm'
      # TODO: Port this for Windows and uncomment
      # arch_subdir = 'VC-WIN64A'
      # asm = 'asm'
      #'rules': [
      #  {
      #    'rule_name': 'Assemble',
      #    'extension': 'asm',
      #    'inputs': [],
      #    'outputs': [
      #      '<(INTERMEDIATE_DIR)/<(RULE_INPUT_ROOT).obj',
      #    ],
      #    'action': [
      #      'nasm.exe',
      #      '-f win64',
      #      '-DNEAR',
      #      '-Ox',
      #      '-g',
      #      '-o', '<(INTERMEDIATE_DIR)/<(RULE_INPUT_ROOT).obj',
      #      '<(RULE_INPUT_PATH)',
      #    ],
      #  }
      #],
    else
      asm = 'no-asm'
    endif
  else
    asm = 'no-asm'
  endif
elif asm_opt.enabled()
  error('Neither GNU Assembler nor Netwide Assembler were found, cannot use use "asm=enabled" option')
else
  asm = 'no-asm'
endif

if asm == 'no-asm'
  defines += ['OPENSSL_NO_ASM']
  error_message = 'Unsupported arch+OS combo: ' + host_machine.cpu_family() + ' + ' + host_machine.system()

  if is_bsd
    if is_x86
      arch_subdir = 'BSD-x86'
    elif is_x86_64
      arch_subdir = 'BSD-x86_64'
    else
      error(error_message)
    endif
  elif is_darwin
    if is_aarch64
      arch_subdir = 'darwin64-arm64-cc'
    elif is_x86_64
      arch_subdir = 'darwin64-x86_64-cc'
    elif is_x86
      arch_subdir = 'darwin-i386-cc'
    else
      error(error_message)
    endif
  elif is_linux
    if is_mips64
      arch_subdir = 'linux64-mips64'
    elif is_riskv64
      arch_subdir = 'linux64-riscv64'
    elif is_s390x
      arch_subdir = 'linux64-s390x'
    elif is_aarch64
      arch_subdir = 'linux-aarch64'
    elif is_arm
      arch_subdir = 'linux-armv4'
    elif is_ppc64
      arch_subdir = 'linux-ppc64le'
    elif is_x86
      arch_subdir = 'linux-elf'
    elif is_x86_64
      arch_subdir = 'linux-x86_64'
    else
      error(error_message)
    endif
  elif is_sunos
    if is_x86_64
      arch_subdir = 'solaris64-x86_64-gcc'
    elif is_x86
      arch_subdir = 'solaris-x86-gcc'
    else
      error(error_message)
    endif
  elif is_windows
    if is_x86
      arch_subdir = 'VC-WIN32'
    elif is_aarch64
      arch_subdir = 'VC-WIN64-ARM'
    elif is_x86_64
      arch_subdir = 'VC-WIN64A'
    else
      error(error_message)
    endif
  else
    error(error_message)
  endif

  message('OpenSSL is configured without ASM support')
else
  message('OpenSSL is configured with ASM support')
endif

subdir('generated-config/archs' / arch_subdir / asm)

# Build options specific to OS, engines are disabled on purpose for the same reasons as `OPENSSL_NO_HW` above
if is_windows
  defines += [
    ## default of Win. See INSTALL in openssl repo.
    'OPENSSLDIR="C:\\Program Files\\Common Files\\SSL"',
    'ENGINESDIR="NUL"',
    'MODULESDIR="NUL"',
    'OPENSSL_SYS_WIN32', 'WIN32_LEAN_AND_MEAN', 'L_ENDIAN',
    '_CRT_SECURE_NO_DEPRECATE', 'UNICODE', '_UNICODE',
  ]
  if compiler.get_id() == 'msvc'
    c_args += [
      '-wd4090', '-Gs0', '-GF', '-Gy', '-nologo',
    ]
  endif
elif is_darwin
  defines += [
    'OPENSSLDIR="/System/Library/OpenSSL/"',
    'ENGINESDIR="/dev/null"',
    'MODULESDIR="/dev/null"',
  ]
  c_args += [
    '-Wno-missing-field-initializers',
  ]
elif is_sunos
  defines += [
   'OPENSSLDIR="/etc/ssl"',
   'ENGINESDIR="/dev/null"',
   'MODULESDIR="/dev/null"',
   '__EXTENSIONS__'
 ]
else
  # Linux and others
  defines += [
    'OPENSSLDIR="/etc/ssl"',
    'ENGINESDIR="/dev/null"',
    'MODULESDIR="/dev/null"',
  ]
  c_args += [
    '-Wno-missing-field-initializers',
  ]
  if compiler.get_id() != 'clang'
    c_args += [
      '-Wno-old-style-declaration',
    ]
  endif
endif

foreach library: openssl_libraries
  # MSVC fails with "ERROR: C static library 'ws2_32' not found" when `static` is specified at all
  if compiler.get_id() == 'msvc'
    dependencies += [
      compiler.find_library(library),
    ]
  else
    dependencies += [
      compiler.find_library(
        library,
        static: get_option('default_library') == 'static',
      ),
    ]
  endif
endforeach

# We may need to add some defines for static builds
if get_option('default_library') == 'static'
  defines += [
    'OSSL_CRYPTO_DSO_CONF_H',
    'DSO_NONE',
    'DSO_EXTENSION=".so"',
    'OPENSSL_NO_DSO',
  ]
endif

foreach define : defines + openssl_defines
  c_args += ['-D' + define]
endforeach

c_args += openssl_cflags

include_directories += openssl_include_directories

libcrypto_lib = library(
  'crypto',
  dependencies: dependencies,
  sources: libcrypto_sources,
  include_directories: include_directories,
  c_args: c_args,
  vs_module_defs: 'crypto.def',
  install: true,
)

libcrypto_dep = declare_dependency(
  include_directories: include_directories,
  dependencies: dependencies,
  link_with: libcrypto_lib,
)

libssl_lib = library(
  'ssl',
  dependencies: dependencies + [libcrypto_dep],
  sources: libssl_sources,
  include_directories: include_directories,
  c_args: c_args,
  vs_module_defs: 'ssl.def',
  install: true,
)

libssl_dep = declare_dependency(
  include_directories: include_directories,
  dependencies: dependencies + [libcrypto_dep],
  link_with: libssl_lib,
)

openssl_dep = declare_dependency(
  dependencies: [libcrypto_dep, libssl_dep],
)

openssl_cli_directories = include_directories + [
  'apps/include'
]

cli_opt = get_option('build_cli')

openssl_cli = executable(
  'openssl',
  build_by_default: cli_opt,
  dependencies: dependencies + [openssl_dep],
  sources: openssl_cli_sources,
  include_directories: openssl_cli_directories,
  c_args: c_args,
  install: cli_opt,
)
