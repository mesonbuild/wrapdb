project(
  'xtl',
  'cpp',
  version: '0.8.0',
  meson_version: '>=0.49.0',
  license: 'BSD-3-Clause',
  default_options: ['warning_level=3'],
)

json_dep = dependency(
  'nlohmann_json',
  version: '>=3.1.1',
)

xtl_dep = declare_dependency(
  include_directories: include_directories(
    'include',
    is_system: true,
  ),
  dependencies: [json_dep],
)

extra_cflags = []

# Workaround from issue: https://github.com/mesonbuild/meson/issues/2550
if meson.is_subproject()
  install_dir = get_option('subproj_includedir')
  extra_cflags += '-I' + get_option('prefix') / install_dir
else
  install_dir = get_option('includedir')
endif

install_subdir(
  'include/xtl',
  install_dir: install_dir,
)

pkgconfig = import('pkgconfig')
pkgconfig.generate(
  name: meson.project_name(),
  version: meson.project_version(),
  description: 'Basic tools (containers, algorithms) used by other quantstack packages.',
  extra_cflags: extra_cflags,
)
