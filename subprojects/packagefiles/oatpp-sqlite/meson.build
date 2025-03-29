
project(
  'oatpp-sqlite',
  'cpp',
  'c',  # for eventual SQLite amalgamation
  default_options: ['default_library=static', 'cpp_std=c++11'],
  version: '1.3.0',
  license: 'Apache-2.0',
)

oatpp_module_version = meson.project_version()
oatpp_module_so_version = (oatpp_module_version.split('.').get(0) + '.' + oatpp_module_version.split(
  '.',
).get(
  1,
)
)

flags = []

deps = []
src_files = []
inc_dirs = []

install = get_option('install')

override_options = []
if get_option('shared_libs')
  override_options += 'default_library=shared'
else
  override_options += 'default_library=static'
endif

deps += dependency(
  'oatpp',
  version: '1.3.0',
  default_options: ['tests=disabled'],
)

# three possible states are represented here, if sqlite_amalgamation is auto, it's used as fallback, if' its enabled, it is enforced, if it's disabled it is forbidden
if get_option('sqlite_amalgamation').enabled()
  subdir('src/sqlite')
  deps += sqlite_amalgamation_dep
else

  sqlite3_wrap_required = get_option('sqlite_amalgamation').disabled()
  sqlite3_dep = dependency(
    'sqlite3',
    required: sqlite3_wrap_required,
  )
  if sqlite3_dep.found()
    deps += sqlite3_dep
  else
    subdir('src/sqlite')
    deps += sqlite_amalgamation_dep
  endif
endif


subdir('src')

lib_oatpp_sqlite = library(
  'oatpp-sqlite',
  src_files,
  dependencies: deps,
  include_directories: inc_dirs,
  cpp_args: flags,
  install: install,
  override_options: override_options,
  soversion: oatpp_module_so_version,
  version: oatpp_module_version,
)


oatpp_sqlite_dep = declare_dependency(
  include_directories: inc_dirs,
  link_with: lib_oatpp_sqlite,
  version: oatpp_module_version,
)

# tests is a feature, so has three states: auto => run tests, if possible, enabled / disabled, run them always or never
run_tests = get_option('tests').enabled()
if get_option('tests').auto()
  tests_are_fixed_on_windows = oatpp_module_version.version_compare('>=1.4.0')

  if host_machine.system() == 'windows' and not tests_are_fixed_on_windows
    run_tests = false
  else
    run_tests = true
  endif
endif


if run_tests
  subdir('test')
endif

