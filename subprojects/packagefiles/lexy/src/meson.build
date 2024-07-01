

if get_option('user_config_header') != ''
    compile_args += ('-DLEXY_USER_CONFIG_HEADER=' + get_option('user_config_header'))
endif


# Link to have FILE I/O. this is only designed to be a static library, since it's  very small by design!
lexy_file_lib = static_library(
    'lexy_file',
    files('input' / 'file.cpp'),
    include_directories: inc_dirs,
)

compile_args += '-DLEXY_HAS_UNICODE_DATABASE=1'

lexy_lib = library(
    'lexy',
    header_files,
    ext_header_files,
    install: install,
    cpp_args: compile_args,
    link_with: [lexy_file_lib],
    override_options: override_options,
)
