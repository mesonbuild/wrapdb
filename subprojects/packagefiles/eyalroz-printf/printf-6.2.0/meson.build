cc = meson.get_compiler('c')
## Checks related to the 'j', 'z' and 't' size modifiers
sizeof_long = cc.sizeof('long')
sizeof_long_long = cc.sizeof('long long')
acceptable_jzt_type_sizes = [sizeof_long, sizeof_long_long]
types = ['intmax_t', 'size_t', 'ptrdiff_t']
foreach type : types
  type_size = cc.sizeof(
    type,
    prefix: ['#include <stdint.h>'],
  )
  if type_size not in acceptable_jzt_type_sizes
    error(
      f'sizeof(@type@) is @type_size@, which is neither sizeof(long) (@sizeof_long@) nor sizeof(long long) (@sizeof_long_long@). Please contact the library maintainers with your platform details.',
    )
  endif
endforeach

private_c_args = []
public_c_args = []
lib_config = {}
if cc.get_argument_syntax() == 'gcc'
  private_c_args += ['-Wall', '-Wextra', '-pedantic', '-Wconversion']
elif cc.get_argument_syntax() == 'msvc'
  private_c_args += '/W4'
endif
if get_option('alias_standard_function_names') != 'none'
  option_val_upper = get_option('alias_standard_function_names').to_upper()
  public_c_args += f'-DPRINTF_ALIAS_STANDARD_FUNCTION_NAMES_@option_val_upper@=1'
  if cc.get_argument_syntax() == 'gcc'
    public_c_args += '-fno-builtin-printf'
  endif

  if get_option('alias_standard_function_names') == 'hard'
    lib_config += {
      'PRINTF_ALIAS_STANDARD_FUNCTION_NAMES_SOFT': 0,
      'PRINTF_ALIAS_STANDARD_FUNCTION_NAMES_HARD': 1,
    }
  else
    lib_config += {
      'PRINTF_ALIAS_STANDARD_FUNCTION_NAMES_SOFT': 1,
      'PRINTF_ALIAS_STANDARD_FUNCTION_NAMES_HARD': 0,
    }
  endif
else
  lib_config += {
    'PRINTF_ALIAS_STANDARD_FUNCTION_NAMES_SOFT': 0,
    'PRINTF_ALIAS_STANDARD_FUNCTION_NAMES_HARD': 0,
  }
endif
private_c_args += '-DPRINTF_INCLUDE_CONFIG_H'

bool_option_names = [
  'support_decimal_specifiers',
  'support_exponential_specifiers',
  'support_msvc_style_integer_specifiers',
  'support_writeback_specifier',
  'support_long_long',
  'use_double_internally',
  'check_for_nul_in_format_specifier',
]
foreach option_name : bool_option_names
  lib_config += {
    'PRINTF_' + option_name.to_upper(): get_option(option_name).to_int(),
  }
endforeach
int_option_names = ['integer_buffer_size', 'decimal_buffer_size']
foreach option_name : int_option_names
  lib_config += {
    'PRINTF_' + option_name.to_upper(): get_option(option_name),
  }
endforeach
int_option_names_wo_prefix = [
  'default_float_precision',
  'max_integral_digits_for_decimal',
  'log10_taylor_terms',
]
foreach option_name : int_option_names_wo_prefix
  lib_config += {
    option_name.to_upper(): get_option(option_name),
  }
endforeach

cfg_header_file = configure_file(
  input: 'printf_config.h.in',
  configuration: lib_config,
  format: 'cmake@',
  output: 'printf_config.h',
)
eyalroz_printf_lib = library(
  'eyalroz-printf',
  'src/printf/printf.c',
  cfg_header_file,
  include_directories: 'src',
  c_args: [private_c_args, public_c_args],
)
eyalroz_printf_dep = declare_dependency(
  include_directories: 'src',
  link_with: eyalroz_printf_lib,
  compile_args: [public_c_args],
)
meson.override_dependency('eyalroz-printf', eyalroz_printf_dep)

if get_option('tests')
  subdir('test')
endif

# Prints the sizes of the different sections of the ELF file: text, dat, vss etc.
size_prog = find_program('size')
if size_prog.found()
  custom_target(
    'printf-sizes',
    command: [size_prog, '-A', '-t', eyalroz_printf_lib],
    capture: true,
    output: 'printf_sizes.txt',
  )
endif

# Produces lists of the symbols, and C++demangled symbols, inside the library
nm_prog = find_program('nm')
if nm_prog.found()
  lib_path = eyalroz_printf_lib.full_path()
  sh_cmd = 'nm --numeric-sort --print-size ' + lib_path + ' > @OUTDIR@/printf_symbols.txt'
  filt_prog = find_program('c++filt')
  if filt_prog.found()
    sh_cmd += ' && nm --numeric-sort ' + lib_path + ' | c++filt > @OUTDIR@/printf_cpp_symbols.txt'
  endif
  custom_target(
    'printf-symbols',
    command: ['sh', '-c', sh_cmd],
    depends: eyalroz_printf_lib,
    output: ['printf_symbols.txt', 'printf_cpp_symbols.txt'],
  )
endif

# Dissassembles the compiled library into an .list file
objdump_prog = find_program('objdump')
if objdump_prog.found()
  custom_target(
    'printf-lst',
    command: [
      objdump_prog,
      '--disassemble',
      '--line-numbers',
      '-S',
      eyalroz_printf_lib,
    ],
    capture: true,
    output: 'printf.list',
  )
endif
