project(
  'leptonica',
  'c',
  version: '1.84.1',
  meson_version: '>=0.59.0',
)

cc = meson.get_compiler('c')

dependencies = [
  cc.find_library(
    'm',
    required: false,
  ),
]

cdata = configuration_data()

foreach _feat, _spec : {
  'libjp2k': ['libopenjp2', '>=2.1.0'],
  'libjpeg': ['libjpeg'],
  'libpng' : ['libpng'],
  'libtiff': ['libtiff-4'],
  'libwebp': ['libwebp'],
  'libz'   : ['zlib'],
}
  _dep = dependency(
    _spec[0],
    required: get_option(_feat),
    version: _spec.get(1, []),
  )
  set_variable('has_' + _feat.underscorify(), _dep.found())
  if _dep.found()
    cdata.set('HAVE_' + _feat.underscorify().to_upper(), 1)
  endif
  dependencies += [_dep]
endforeach

has_libgif = get_option('libgif').allowed()
if has_libgif
  gif_dep = dependency(
    'giflib',
    required: false,
  )
  if not gif_dep.found()
    gif_dep = cc.find_library(
      'gif',
      has_headers: 'gif_lib.h',
      required: false,
    )
  endif
  has_libgif = get_option('libgif').require(
    gif_dep.found(),
    error_message: 'giflib not found',
  ).allowed()
  dependencies += gif_dep
endif
if has_libgif
  cdata.set('HAVE_LIBGIF', 1)
endif

if has_libjp2k
  cdata.set_quoted('LIBJP2K_HEADER', 'openjpeg.h')
endif

dependencies += dependency(
  'libwebpmux',
  required: get_option('libwebp-anim').require(
    has_libwebp,
    error_message: 'libwebp feature needed',
  ),
  version: '>=0.5.0',
)
has_libwebp_anim = dependencies[-1].found()
if has_libwebp_anim
  cdata.set('HAVE_LIBWEBP_ANIM', 1)
endif

if cc.has_header_symbol('dirent.h', 'dirfd')
  cdata.set('HAVE_DIRFD', 1)
endif

if cc.has_header_symbol('stdio.h', 'fmemopen')
  cdata.set('HAVE_FMEMOPEN', 1)
endif

if cc.has_header_symbol('sys/stat.h', 'fstatat')
  cdata.set('HAVE_FSTATAT', 1)
endif

config_h = configure_file(
  output: 'config_auto.h',
  configuration: cdata,
)

subdir('src')
subdir('prog')
