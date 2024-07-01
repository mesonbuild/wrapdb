
project(
    'oatpp',
    'cpp',
    default_options: ['default_library=static', 'cpp_std=c++11'],
    version: '1.3.0', # upstream it's called 1.3.0-latest
    license: 'Apache-2.0',
)

oatpp_version = meson.project_version()
oatpp_so_version = (
    oatpp_version.split('.').get(0) + '.' + oatpp_version.split('.').get(1)
)

flags = []


if get_option('disable_env_object_counters')
    flags += '-DOATPP_DISABLE_ENV_OBJECT_COUNTERS'
endif

if get_option('disable_pool_allocations')
    flags += '-DOATPP_DISABLE_POOL_ALLOCATIONS'
    warning(
        'disable_pool_allocations option is deprecated and has no effect.',
    )
endif

if not get_option('thread_hardware_concurrency').auto()
    flags += (
        '-DOATPP_THREAD_HARDWARE_CONCURRENCY=' + get_option(
            'thread_hardware_concurrency',
        ).enabled().to_string().to_upper()
    )
endif

if get_option('thread_distributed_mem_pool_shards_count')
    flags += (
        '-DOATPP_THREAD_DISTRIBUTED_MEM_POOL_SHARDS_COUNT=' + get_option(
            'thread_hardware_concurrency',
        ).enabled().to_string().to_upper()
    )

    warning(
        'OATPP_THREAD_DISTRIBUTED_MEM_POOL_SHARDS_COUNT option is deprecated and has no effect.',
    )
endif

if get_option('compat_build_no_thread_local')
    flags += '-DOATPP_COMPAT_BUILD_NO_THREAD_LOCAL'
endif


if get_option('compat_build_no_set_affinity')
    flags += '-DOATPP_COMPAT_BUILD_NO_SET_AFFINITY'
endif

if get_option('disable_logv')
    flags += '-DOATPP_DISABLE_LOGV'
endif

if get_option('disable_logd')
    flags += '-DOATPP_DISABLE_LOGD'
endif

if get_option('disable_logi')
    flags += '-DOATPP_DISABLE_LOGI'
endif

if get_option('disable_logv')
    flags += '-DOATPP_DISABLE_LOGV'
endif

if get_option('disable_logw')
    flags += '-DOATPP_DISABLE_LOGW'
endif

if get_option('disable_loge')
    flags += '-DOATPP_DISABLE_LOGE'
endif


cpp = meson.get_compiler('cpp')
if cpp.get_id() == 'gcc' and cpp.version().version_compare('<5.0.0') == false
    flags += '-DOATPP_DISABLE_STD_PUT_TIME'
endif

is_msvc_or_similar = cpp.get_id() == 'msvc' or cpp.get_id() == 'clang-cl'
if is_msvc_or_similar
    add_project_arguments('/permissive-', language: 'cpp')
endif


deps = []
src_files = []
inc_dirs = []

test_module_deps = []
test_module_src_files = []
test_module_inc_dirs = []

install = get_option('install')

override_options = []
if get_option('shared_libs')
    override_options += 'default_library=shared'
else
    override_options += 'default_library=static'
endif

if is_msvc_or_similar
    if get_option('msvc_link_static_runtime')
        override_options += 'b_vscrt=static_from_buildtype'
    else
        override_options += 'b_vscrt=from_buildtype'
    endif
endif

subdir('src')

lib_oatpp = library(
    'oatpp',
    src_files,
    dependencies: deps,
    include_directories: inc_dirs,
    cpp_args: flags,
    install: install,
    override_options: override_options,
    soversion: oatpp_so_version,
    version: oatpp_version,
)


oatpp_dep = declare_dependency(
    include_directories: inc_dirs,
    link_with: lib_oatpp,
    version: oatpp_version,
)


# test module of oatpp (not the tests, but the module that is the test suite like e.g gtest)
lib_test_oatpp = library(
    'oatpp-test',
    test_module_src_files,
    dependencies: test_module_deps,
    include_directories: test_module_inc_dirs,
    cpp_args: flags,
    install: install,
    override_options: override_options,
    soversion: oatpp_so_version,
    version: oatpp_version,
)


oatpp_test_dep = declare_dependency(
    dependencies: oatpp_dep,
    include_directories: test_module_inc_dirs,
    link_with: lib_test_oatpp,
    version: oatpp_version,
)


# tests is a feature, so has three states: auto => run tests, if possible, enabled / disabled, run them always or never
run_tests = get_option('tests').enabled()
if get_option('tests').auto()
    tests_are_fixed_on_windows = oatpp_version.version_compare('>=1.4.0')

    if host_machine.system() == 'windows' and not tests_are_fixed_on_windows
        run_tests = false
    else
        run_tests = true
    endif
endif


if run_tests
    subdir('test')
endif
