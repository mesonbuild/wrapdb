project(
  'glbinding',
  'cpp',
  version: '3.5.0',
  license: 'MIT',
  meson_version: '>=0.62.0',
  default_options: ['cpp_std=c++17', 'warning_level=0'],
)

cpp = meson.get_compiler('cpp')

if get_option('default_library') == 'both' and cc.get_argument_syntax() == 'msvc'
  error('default_library=both not supported when compiling with MSVC')
endif

system_name_arg = '-DSYSTEM_@0@'.format(host_machine.system().to_upper())

glbinding_args = [system_name_arg]
glbinding_aux_args = [system_name_arg]
glbinding_public_args = []
glbinding_aux_public_args = []

if host_machine.system() != 'windows'
  dl_dep = dependency('dl')
else
  dl_dep = declare_dependency()
endif

if cpp.has_function_attribute('visibility:default')
  glbinding_args += [
    '-DGLBINDING_API=__attribute__((visibility("default")))',
    '-DGLBINDING_TEMPLATE_API=__attribute__((visibility("default")))',
  ]
  glbinding_public_args += [
    '-DGLBINDING_API=__attribute__((visibility("default")))',
    '-DGLBINDING_TEMPLATE_API=__attribute__((visibility("default")))',
  ]
  glbinding_aux_args += [
    '-DGLBINDING_AUX_API=__attribute__((visibility("default")))',
    '-DGLBINDING_AUX_TEMPLATE_API=__attribute__((visibility("default")))',
  ]
  glbinding_aux_public_args += [
    '-DGLBINDING_AUX_API=__attribute__((visibility("default")))',
    '-DGLBINDING_AUX_TEMPLATE_API=__attribute__((visibility("default")))',
  ]
elif host_machine.system() == 'windows' and get_option('default_library') != 'static'
  glbinding_args += [
    '-DGLBINDING_API=__declspec(dllexport)',
    '-DGLBINDING_TEMPLATE_API=',
  ]
  glbinding_public_args += [
    '-DGLBINDING_API=__declspec(dllimport)',
    '-DGLBINDING_TEMPLATE_API=',
  ]
  glbinding_aux_args += [
    '-DGLBINDING_AUX_API=__declspec(dllexport)',
    '-DGLBINDING_AUX_TEMPLATE_API=',
  ]
  glbinding_aux_public_args += [
    '-DGLBINDING_AUX_API=__declspec(dllimport)',
    '-DGLBINDING_AUX_TEMPLATE_API=',
  ]
else
  glbinding_args += ['-DGLBINDING_API=', '-DGLBINDING_TEMPLATE_API=']
  glbinding_public_args += ['-DGLBINDING_API=', '-DGLBINDING_TEMPLATE_API=']
  glbinding_aux_args += [
    '-DGLBINDING_AUX_API=',
    '-DGLBINDING_AUX_TEMPLATE_API=',
  ]
  glbinding_aux_public_args += [
    '-DGLBINDING_AUX_API=',
    '-DGLBINDING_AUX_TEMPLATE_API=',
  ]
endif

subdir('source/glbinding/include/glbinding')
subdir('source/glbinding/include/glbinding-aux')
glbinding_includes = ['source/glbinding/include', 'bundled_headers']

use_system_khrplatform = cpp.has_header('KHR/khrplatform.h')
summary('Use system KHR/khrplatform.h', use_system_khrplatform)

if not use_system_khrplatform
  glbinding_includes += 'source/3rdparty/KHR/include'
endif

glbinding_sources = files(
  'source/glbinding/source/AbstractFunction.cpp',
  'source/glbinding/source/AbstractState.cpp',
  'source/glbinding/source/AbstractValue.cpp',
  'source/glbinding/source/Binding.cpp',
  'source/glbinding/source/Binding_list.cpp',
  'source/glbinding/source/Binding_objects_0.cpp',
  'source/glbinding/source/Binding_objects_a.cpp',
  'source/glbinding/source/Binding_objects_b.cpp',
  'source/glbinding/source/Binding_objects_c.cpp',
  'source/glbinding/source/Binding_objects_d.cpp',
  'source/glbinding/source/Binding_objects_e.cpp',
  'source/glbinding/source/Binding_objects_f.cpp',
  'source/glbinding/source/Binding_objects_g.cpp',
  'source/glbinding/source/Binding_objects_h.cpp',
  'source/glbinding/source/Binding_objects_i.cpp',
  'source/glbinding/source/Binding_objects_j.cpp',
  'source/glbinding/source/Binding_objects_k.cpp',
  'source/glbinding/source/Binding_objects_l.cpp',
  'source/glbinding/source/Binding_objects_m.cpp',
  'source/glbinding/source/Binding_objects_n.cpp',
  'source/glbinding/source/Binding_objects_o.cpp',
  'source/glbinding/source/Binding_objects_p.cpp',
  'source/glbinding/source/Binding_objects_q.cpp',
  'source/glbinding/source/Binding_objects_r.cpp',
  'source/glbinding/source/Binding_objects_s.cpp',
  'source/glbinding/source/Binding_objects_t.cpp',
  'source/glbinding/source/Binding_objects_u.cpp',
  'source/glbinding/source/Binding_objects_v.cpp',
  'source/glbinding/source/Binding_objects_w.cpp',
  'source/glbinding/source/Binding_objects_x.cpp',
  'source/glbinding/source/Binding_objects_y.cpp',
  'source/glbinding/source/Binding_objects_z.cpp',
  'source/glbinding/source/FunctionCall.cpp',
  'source/glbinding/source/State.cpp',
  'source/glbinding/source/getProcAddress.cpp',
  'source/glbinding/source/gl/functions-patches.cpp',
  'source/glbinding/source/gl/functions_0.cpp',
  'source/glbinding/source/gl/functions_a.cpp',
  'source/glbinding/source/gl/functions_b.cpp',
  'source/glbinding/source/gl/functions_c.cpp',
  'source/glbinding/source/gl/functions_d.cpp',
  'source/glbinding/source/gl/functions_e.cpp',
  'source/glbinding/source/gl/functions_f.cpp',
  'source/glbinding/source/gl/functions_g.cpp',
  'source/glbinding/source/gl/functions_h.cpp',
  'source/glbinding/source/gl/functions_i.cpp',
  'source/glbinding/source/gl/functions_j.cpp',
  'source/glbinding/source/gl/functions_k.cpp',
  'source/glbinding/source/gl/functions_l.cpp',
  'source/glbinding/source/gl/functions_m.cpp',
  'source/glbinding/source/gl/functions_n.cpp',
  'source/glbinding/source/gl/functions_o.cpp',
  'source/glbinding/source/gl/functions_p.cpp',
  'source/glbinding/source/gl/functions_q.cpp',
  'source/glbinding/source/gl/functions_r.cpp',
  'source/glbinding/source/gl/functions_s.cpp',
  'source/glbinding/source/gl/functions_t.cpp',
  'source/glbinding/source/gl/functions_u.cpp',
  'source/glbinding/source/gl/functions_v.cpp',
  'source/glbinding/source/gl/functions_w.cpp',
  'source/glbinding/source/gl/functions_x.cpp',
  'source/glbinding/source/gl/functions_y.cpp',
  'source/glbinding/source/gl/functions_z.cpp',
  'source/glbinding/source/glbinding.cpp',
)

glbinding_lib = library(
  'glbinding',
  glbinding_sources,
  cpp_args: glbinding_args,
  dependencies: [dl_dep],
  include_directories: glbinding_includes,
  gnu_symbol_visibility: 'hidden',
  cpp_pch: 'pch/pch.h',
)

glbinding_dep = declare_dependency(
  link_with: glbinding_lib,
  include_directories: glbinding_includes,
  compile_args: glbinding_public_args,
)

glbinding_aux_includes = ['source/glbinding-aux/include', 'bundled_headers']

glbinding_aux_sources = files(
  'source/glbinding-aux/source/ContextInfo.cpp',
  'source/glbinding-aux/source/Meta.cpp',
  'source/glbinding-aux/source/Meta_BitfieldsByString.cpp',
  'source/glbinding-aux/source/Meta_BooleansByString.cpp',
  'source/glbinding-aux/source/Meta_EnumsByString.cpp',
  'source/glbinding-aux/source/Meta_ExtensionsByFunctionString.cpp',
  'source/glbinding-aux/source/Meta_ExtensionsByString.cpp',
  'source/glbinding-aux/source/Meta_FunctionStringsByExtension.cpp',
  'source/glbinding-aux/source/Meta_FunctionStringsByVersion.cpp',
  'source/glbinding-aux/source/Meta_ReqVersionsByExtension.cpp',
  'source/glbinding-aux/source/Meta_StringsByBitfield.cpp',
  'source/glbinding-aux/source/Meta_StringsByBoolean.cpp',
  'source/glbinding-aux/source/Meta_StringsByEnum.cpp',
  'source/glbinding-aux/source/Meta_StringsByExtension.cpp',
  'source/glbinding-aux/source/Meta_getStringByBitfield.cpp',
  'source/glbinding-aux/source/ValidVersions.cpp',
  'source/glbinding-aux/source/ValidVersions_list.cpp',
  'source/glbinding-aux/source/debug.cpp',
  'source/glbinding-aux/source/logging.cpp',
  'source/glbinding-aux/source/types_to_string.cpp',
  'source/glbinding-aux/source/types_to_string_private.cpp',
)

glbinding_aux_lib = library(
  'glbinding-aux',
  glbinding_aux_sources,
  cpp_args: glbinding_aux_args,
  dependencies: [glbinding_dep, dependency('threads')],
  include_directories: glbinding_aux_includes,
  cpp_pch: 'pch/pch.h',
  gnu_symbol_visibility: 'hidden',
  build_by_default: false,
)

glbinding_aux_dep = declare_dependency(
  link_with: glbinding_aux_lib,
  dependencies: [glbinding_dep],
  include_directories: glbinding_aux_includes,
  compile_args: glbinding_aux_public_args,
)

subdir('source/tests')

if get_option('main_glbinding_includes_aux')
  glbinding_dep = declare_dependency(
    dependencies: [glbinding_dep, glbinding_aux_dep],
  )
endif

meson.override_dependency('glbinding', glbinding_dep)
meson.override_dependency('glbinding-aux', glbinding_aux_dep)
