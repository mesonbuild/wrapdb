# data

# Input: install_prefix, install_libdir, install_datadir, install_includedir,
#        install_pkgconfigdir, cairomm_pcname, cairomm_api_version,
#        cairomm_requires, msvc14x_toolset_ver, cairo_dep
# Output: -

pkg_conf_data = configuration_data()
pkg_conf_data.set('prefix', install_prefix)
pkg_conf_data.set('exec_prefix', '${prefix}')
pkg_conf_data.set('libdir', '${exec_prefix}' / install_libdir)
pkg_conf_data.set('datarootdir', '${prefix}' / install_datadir)
pkg_conf_data.set('datadir', '${datarootdir}')
pkg_conf_data.set('includedir', '${prefix}' / install_includedir)
pkg_conf_data.set('PACKAGE_VERSION', meson.project_version())
pkg_conf_data.set('CAIROMM_MODULE_NAME', cairomm_pcname)
pkg_conf_data.set('CAIROMM_API_VERSION', cairomm_api_version)
pkg_conf_data.set('CAIROMM_MODULES', cairomm_requires)
pkg_conf_data.set('CAIROMM_EXTRA_LIBS', cairomm_extra_libs)
pkg_conf_data.set('MSVC_TOOLSET_VER', msvc14x_toolset_ver)

configure_file(
  input: 'cairomm.pc.in',
  output: cairomm_pcname + '.pc',
  configuration: pkg_conf_data,
  install_dir: install_pkgconfigdir,
  install: true,
)

foreach cairomm_mod : [
  'ft',
  'pdf',
  'png',
  'ps',
  'quartz',
  'quartz-font',
  'quartz-image',
  'svg',
  'win32',
  'win32-font',
  'xlib',
  'xlib-xrender',
]

  # Install the module only if there is a corresponding cairo module.
  if cairo_dep.type_name() in ['pkgconfig', 'internal']
    do_install = dependency(
      'cairo-' + cairomm_mod,
      required: false,
    ).found()
  else
    if cairomm_mod == 'png'
      do_install = cpp_compiler.has_function(
        'cairo_surface_write_to_png',
        prefix: '#include <cairo.h>',
        dependencies: cairo_dep,
      )
    elif cairomm_mod == 'quartz-font'
      do_install = cpp_compiler.has_function(
        'cairo_quartz_font_face_create_for_cgfont',
        prefix: '#include <cairo-quartz.h>',
        dependencies: cairo_dep,
      )
    elif cairomm_mod == 'win32-font'
      do_install = cpp_compiler.has_function(
        'cairo_win32_font_face_create_for_hfont',
        prefix: '#include <cairo-win32.h>',
        dependencies: cairo_dep,
      )
    else
      do_install = cpp_compiler.has_header('cairo-@0@.h'.format(cairomm_mod))
    endif
  endif
  pc_file = 'cairomm-' + cairomm_mod
  configure_file(
    input: pc_file + '.pc.in',
    output: pc_file + '-' + cairomm_api_version + '.pc',
    configuration: pkg_conf_data,
    install_dir: install_pkgconfigdir,
    install: do_install,
  )
endforeach
