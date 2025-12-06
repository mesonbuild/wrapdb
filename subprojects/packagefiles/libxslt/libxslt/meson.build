headers = [
  'xslt.h',
  'xsltutils.h',
  'pattern.h',
  'templates.h',
  'variables.h',
  'keys.h',
  'numbersInternals.h',
  'extensions.h',
  'extra.h',
  'functions.h',
  'namespaces.h',
  'imports.h',
  'attributes.h',
  'documents.h',
  'preproc.h',
  'transform.h',
  'security.h',
  'xsltInternals.h',
  'xsltexports.h',
  'xsltlocale.h',
]
install_headers(headers)

sources = [
  'attrvt.c',
  'xslt.c',
  'xsltlocale.c',
  'xsltutils.c',
  'pattern.c',
  'templates.c',
  'variables.c',
  'keys.c',
  'numbers.c',
  'extensions.c',
  'extra.c',
  'functions.c',
  'namespaces.c',
  'imports.c',
  'attributes.c',
  'documents.c',
  'preproc.c',
  'transform.c',
  'security.c',
]

version_arr = meson.project_version().split('.')
version_int = [
  version_arr[0].to_int(),
  version_arr[1].to_int(),
  version_arr[2].to_int(),
]
version_number = version_int[0] * 10000 + version_int[1] * 100 + version_int[2]
version_extra = ''

xsltconfig = configuration_data()
xsltconfig.set('VERSION', meson.project_version())
xsltconfig.set('LIBXSLT_VERSION_NUMBER', version_number)
xsltconfig.set('LIBXSLT_VERSION_EXTRA', version_extra)
xsltconfig.set(
  'LIBXSLT_DEFAULT_PLUGINS_PATH',
  get_option('prefix') / get_option('libdir') / 'libxslt-plugins',
)
xsltconfig.set10('WITH_DEBUGGER', get_option('debugger'))
xsltconfig.set10('WITH_MODULES', with_modules)
xsltconfig.set10('WITH_PROFILER', get_option('profiler'))
xsltconfig.set10('WITH_TRIO', with_trio)
xsltconfig.set10('WITH_XSLT_DEBUG', get_option('xslt_debug'))

configure_file(
  input: 'xsltconfig.h.in',
  output: 'xsltconfig.h',
  configuration: xsltconfig,
)

libxslt = library(
  'xslt',
  sources,
  include_directories: incdir,
  dependencies: [libxml2_dep, libm, librt],
  version: meson.project_version(),
  install: true,
)

pkg.generate(libxslt)

libxslt_dep = declare_dependency(
  compile_args: get_option('default_library') == 'static' ? '-DLIBXSLT_STATIC' : [],
  link_with: libxslt,
  include_directories: incdir,
  dependencies: libxml2_dep,
)

meson.override_dependency('libxslt', libxslt_dep)
