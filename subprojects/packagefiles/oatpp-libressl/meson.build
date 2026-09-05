
project(
    'oatpp-libressl',
    'cpp',
    default_options: ['default_library=static', 'cpp_std=c++11'],
    version: '1.3.0',
    license: 'Apache-2.0',
)

oatpp_module_version = meson.project_version()
oatpp_module_so_version = (
    oatpp_module_version.split('.').get(0) + '.' + oatpp_module_version.split(
        '.',
    ).get(1)
)

install = get_option('install')

override_options = []
if get_option('shared_libs')
    override_options += 'default_library=shared'
else
    override_options += 'default_library=static'
endif

deps = []
src_files = []
inc_dirs = []


deps += dependency(
    'oatpp',
    version: '1.3.0',
    default_options: ['tests=disabled'],
)
# libressl, isn't available as wrap file, so prevent the usage of libcrypto or libssl from the openssl wrap file!
deps += dependency('libtls', allow_fallback: false)
deps += dependency('libcrypto', allow_fallback: false)
deps += dependency('libssl', allow_fallback: false)


subdir('src')


lib_oatpp_libressl = library(
    'oatpp-libressl',
    src_files,
    dependencies: deps,
    include_directories: inc_dirs,
    install: install,
    override_options: override_options,
    soversion: oatpp_module_so_version,
    version: oatpp_module_version,
)


oatpp_libressl_dep = declare_dependency(
    include_directories: inc_dirs,
    link_with: lib_oatpp_libressl,
    version: oatpp_module_version,
)


if get_option('tests')
    subdir('test')
endif

