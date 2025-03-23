
project(
  'oatpp-swagger',
  'cpp',
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

install = get_option('install')

override_options = []
if get_option('shared_libs')
  override_options += 'default_library=shared'
else
  override_options += 'default_library=static'
endif

cpp = meson.get_compiler('cpp')
is_msvc_or_similar = cpp.get_id() == 'msvc' or cpp.get_id() == 'clang-cl'

if is_msvc_or_similar
  if get_option('msvc_link_static_runtime')
    override_options += 'b_vscrt=static_from_buildtype'
  else
    override_options += 'b_vscrt=from_buildtype'
  endif
endif

flags = []
compile_args = []

if install
  # this has to be different, depending on the folder, if it's installed, set the path to the installed dir, otherwise to the current source dir!
  res_install_dir = (get_option('datadir') / ('oatpp-swagger-' + oatpp_module_version)
)
  compile_args += ('-DOATPP_SWAGGER_RES_PATH="' + (res_install_dir / 'res') + '"'
)

  install_subdir(
    'res',
    install_dir: res_install_dir,
  )

else
  compile_args += ('-DOATPP_SWAGGER_RES_PATH="' + (meson.project_source_root() / 'res') + '"'
)

endif

flags += compile_args

deps = []
src_files = []
inc_dirs = []


deps += dependency(
  'oatpp',
  version: '1.3.0',
  default_options: ['tests=disabled'],
)
subdir('src')

lib_oatpp_swagger = library(
  'oatpp-swagger',
  src_files,
  dependencies: deps,
  include_directories: inc_dirs,
  cpp_args: flags,
  install: install,
  override_options: override_options,
  soversion: oatpp_module_so_version,
  version: oatpp_module_version,
)


oatpp_swagger_dep = declare_dependency(
  include_directories: inc_dirs,
  link_with: lib_oatpp_swagger,
  version: oatpp_module_version,
  compile_args: compile_args,
)


if get_option('tests')
  subdir('test')
endif
