project(
  'eyalroz-printf',
  'c',
  'cpp',
  license: 'MIT',
  meson_version: '>=0.63.0',
  version: '6.2.0',
  default_options: [
    'b_staticpic=false',
    'c_std=c99',
    'default_library=static',  # For shared support we need to somehow provide putchar_ implementation
  ],
)


cc = meson.get_compiler('c')
## Checks related to the 'j', 'z' and 't' size modifiers
sizeof_long = cc.sizeof('long')
sizeof_long_long = cc.sizeof('long long')
acceptable_jzt_type_sizes = [sizeof_long, sizeof_long_long]
types = ['intmax_t', 'size_t', 'ptrdiff_t']
foreach type : types
  type_size = cc.sizeof(
    type,
    prefix: '#include <stdint.h>',
  )
  if type_size not in acceptable_jzt_type_sizes
    error(
      f'sizeof(@type@) is @type_size@, which is neither sizeof(long) (@sizeof_long@) nor sizeof(long long) (@sizeof_long_long@). Please contact the library maintainers with your platform details.',
    )
  endif
endforeach

lib_config = {}
private_c_args = cc.get_supported_arguments(
  '-Wall',
  '-Wextra',
  '-pedantic',
  '-Wconversion',
  '/W4',
)
private_c_args += '-DPRINTF_INCLUDE_CONFIG_H'
public_c_args = []
aliasing_defines = {
  'hard': {
    'PRINTF_ALIAS_STANDARD_FUNCTION_NAMES_SOFT': 0,
    'PRINTF_ALIAS_STANDARD_FUNCTION_NAMES_HARD': 1,
  },
  'soft': {
    'PRINTF_ALIAS_STANDARD_FUNCTION_NAMES_SOFT': 1,
    'PRINTF_ALIAS_STANDARD_FUNCTION_NAMES_HARD': 0,
  },
  'none': {
    'PRINTF_ALIAS_STANDARD_FUNCTION_NAMES_SOFT': 0,
    'PRINTF_ALIAS_STANDARD_FUNCTION_NAMES_HARD': 0,
  },
}
alias_standard_function_names = get_option('alias_standard_function_names')
if alias_standard_function_names != 'none'
  option_val_upper = alias_standard_function_names.to_upper()
  public_c_args += f'-DPRINTF_ALIAS_STANDARD_FUNCTION_NAMES_@option_val_upper@=1'
  public_c_args += cc.get_supported_arguments('-fno-builtin-printf')
endif
lib_config += aliasing_defines[alias_standard_function_names]

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
size_prog = find_program(
  'size',
  required: false,
)
if size_prog.found()
  custom_target(
    'printf-sizes',
    command: [size_prog, '-A', '-t', eyalroz_printf_lib],
    capture: true,
    output: 'printf_sizes.txt',
  )
endif

# Produces lists of the symbols, and C++demangled symbols, inside the library
nm_prog = find_program(
  'nm',
  required: false,
)
if nm_prog.found()
  custom_target(
    'printf-symbols',
    command: [nm_prog, '--numeric-sort', '--print-size', eyalroz_printf_lib],
    capture: true,
    output: 'printf_symbols.txt',
  )
endif

# Dissassembles the compiled library into an .list file
objdump_prog = find_program(
  'objdump',
  required: false,
)
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
