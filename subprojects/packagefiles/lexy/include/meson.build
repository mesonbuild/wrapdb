inc_dirs += include_directories('.')


header_files = []
subdir('lexy')

ext_header_files = []
subdir('lexy_ext')

if install
    install_headers(
        header_files,
        subdir: 'lexy',
        preserve_path: true,
    )
    install_headers(
        ext_header_files,
        subdir: 'lexy_ext',
        preserve_path: true,
    )
endif
