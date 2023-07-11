sqlite_amalgamation_version = '3.33.0'
sqlite_amalgamation_so_version = sqlite_amalgamation_version.split('.').get(0)

sqlite_amalgamation_header_files = files('sqlite3.h')
sqlite_amalgamation_src_files = files(
    'sqlite3.c',
)

inc_dirs += include_directories('.')

sqlite_amalgamation_src_files += sqlite_amalgamation_header_files

install_headers(sqlite_amalgamation_header_files)

lib_sqlite_amalgamation = library(
    'sqlite_amalgamation',
    sqlite_amalgamation_src_files,
    install: install,
    c_args: flags,
    override_options: override_options,
    soversion: sqlite_amalgamation_so_version,
    version: sqlite_amalgamation_version,
)


sqlite_amalgamation_dep = declare_dependency(
    include_directories: include_directories('.'),
    link_with: lib_sqlite_amalgamation,
    version: sqlite_amalgamation_version,
)
