project(
    'nanobind',
    'cpp',
    version: '2.1.0',
    meson_version: '>=0.53.0',
    license: 'BSD-3-Clause',
)

py_mod = import('python')
py = py_mod.find_installation()
py_dep = py.dependency()

robin_map_dep = dependency('robin-map')

incdir = include_directories('include')

# Arguments are derived from nanobind_build_library function in CMake configuration
dep_compile_args = []
dep_link_args = []

if get_option('buildtype') == 'shared'
  if host_machine.system() == 'darwin'
    is_pypy = py_dep.get_variable('implementation_lower') == 'pypy'
    if is_pypy
      resp_file = meson.project_source_root() / 'cmake/darwin-ld-pypy.sym'
    else
      resp_file = meson.project_source_root() / 'cmake/darwin-ld-cpython.sym'
    endif
    add_project_link_arguments('-Wl,-dead_strip', '-Wl,x', '-Wl,-S', '-Wl,@' + resp_file)
    dep_link_args += ['-Wl,-dead_strip', '-Wl,x', '-Wl,-S', '-Wl,@' + resp_file]
  elif host_machine.system() != 'windows'
    add_project_link_arguments('-Wl,-s', language: 'cpp')
    dep_link_args += ['-Wl,-s']
  endif

  add_project_arguments('-DNB_BUILD', language: 'cpp')
  dep_compile_args += ['-DNB_SHARED']
elif host_machine.system() != 'windows' and host_machine.system() != 'darwin'
  dep_compile_args += ['-ffunction-sections', '-fdata-sections']
  dep_link_args += ['-Wl,--gc-sections']
endif

compiler = meson.get_compiler('cpp')
if compiler.get_id() == 'msvc'
  dep_compile_args += ['-D_CRT_SECURE_NO_WARNINGS']
else
  # Discussion in WrapDB PR #1556 as to whether or not this is necessary
  # add_project_arguments('-fno-strict-aliasing', language: 'cpp')
endif

if get_option('buildtype') == 'release'
  add_project_arguments('-DNB_COMPACT_ASSERTIONS', language: 'cpp')
endif

nanobind_lib = static_library(
    'nanobind',
    sources: [
        'src/nb_internals.cpp',
        'src/nb_func.cpp',
        'src/nb_type.cpp',
        'src/nb_enum.cpp',
        'src/nb_ndarray.cpp',
        'src/nb_static_property.cpp',
        'src/common.cpp',
        'src/error.cpp',
        'src/trampoline.cpp',
        'src/implicit.cpp',
    ],
    include_directories: [incdir],
    dependencies: [py_dep, robin_map_dep],
    gnu_symbol_visibility: 'hidden',
)


nanobind_dep = declare_dependency(
    include_directories: [incdir],
    link_with: [nanobind_lib],
    dependencies: [py_dep, robin_map_dep],
    compile_args: dep_compile_args,
    link_args: dep_link_args,
)
