libexslt_headers = files('exslt.h', 'exsltexports.h')

sources = files(
  'common.c',
  'crypto.c',
  'date.c',
  'dynamic.c',
  'exslt.c',
  'functions.c',
  'math.c',
  'saxon.c',
  'sets.c',
  'strings.c',
)

version_arr = exslt_version.split('.')
version_int = [
  version_arr[0].to_int(),
  version_arr[1].to_int(),
  version_arr[2].to_int(),
]
version_number = version_int[0] * 10000 + version_int[1] * 100 + version_int[2]
version_extra = ''

exsltconfig = configuration_data()
exsltconfig.set('LIBEXSLT_VERSION', exslt_version)
exsltconfig.set('LIBEXSLT_VERSION_NUMBER', version_number)
exsltconfig.set('LIBEXSLT_VERSION_EXTRA', version_extra)
exsltconfig.set10('WITH_CRYPTO', libgcrypt_dep.found())

libexslt_headers += configure_file(
  input: 'exsltconfig.h.in',
  output: 'exsltconfig.h',
  configuration: exsltconfig,
)

install_headers(
  libexslt_headers,
  subdir: 'libexslt',
)

libexslt = library(
  'exslt',
  sources,
  include_directories: incdir,
  dependencies: [libxml2_dep, libxslt_dep, libm, librt, libgcrypt_dep],
  version: exslt_version,
  install: true,
)

pkg.generate(libexslt)

libexslt_dep = declare_dependency(
  compile_args: get_option('default_library') == 'static' ? '-DLIBEXSLT_STATIC' : [],
  link_with: libexslt,
  include_directories: depincdir,
  dependencies: libxslt_dep,
)

meson.override_dependency('libexslt', libexslt_dep)
