project(
  'libwebp',
  'c',
  version: '1.6.0',
  license: 'BSD-3-Clause',
  meson_version: '>=0.59.0',
)

# Build libraries. {{{

build_libsharpyuv = (get_option('libsharpyuv').allowed()
  ? declare_dependency() : disabler()
)

build_libwebp = (get_option('libwebp').require(
    build_libsharpyuv.found(),
  error_message: 'depends on libsharpyuv',
  ).allowed() ? declare_dependency() : disabler()
)

build_libwebpdecoder = (get_option('libwebpdecoder').allowed()
  ? declare_dependency() : disabler()
)

build_libwebpdemux = (get_option('libwebpdemux').require(
    build_libwebp.found() or build_libwebpdecoder.found(),
  error_message: 'depends on libwebp or libwebpdecoder',
  ).allowed() ? declare_dependency() : disabler()
)

build_libwebpmux = (get_option('libwebpmux').require(
    build_libwebp.found(),
  error_message: 'depends on libwebp',
  ).allowed() ? declare_dependency() : disabler()
)

# }}}

# Build programs. {{{

# Note: can't build with `libwebpdecoder`.
build_cwebp = (get_option('cwebp').require(
    build_libwebp.found() and build_libwebpdemux.found(),
  error_message: 'depends on libwebp and libwebpdemux',
  ).allowed() ? declare_dependency() : disabler()
)

# Note: same as above.
build_dwebp = (get_option('dwebp').require(
    build_libwebp.found() and build_libwebpdemux.found(),
  error_message: 'depends on libwebp and libwebpdemux',
  ).allowed() ? declare_dependency() : disabler()
)

build_webpinfo = (get_option('webpinfo').require(
    build_libwebp.found(),
  error_message: 'depends on libwebp',
  ).allowed() ? declare_dependency() : disabler()
)

build_webpmux = (get_option('webpmux').require(
    build_libwebpmux.found(),
  error_message: 'depends on libwebpmux',
  ).allowed() ? declare_dependency() : disabler()
)

# }}}

cc = meson.get_compiler('c')

pkg = import('pkgconfig')

m_dep = cc.find_library(
  'm',
  required: false,
)

add_project_arguments(
  '-DHAVE_CONFIG_H',
  language: 'c',
)

if get_option('default_library') != 'static'
  add_project_arguments(
    '-DWEBP_DLL',
    language: 'c',
  )
endif

if host_machine.endian() == 'big'
  add_project_arguments(
    '-DWORDS_BIGENDIAN',
    language: 'c',
  )
endif

top_includes = include_directories('.', 'src')

cdata = configuration_data()

# Advanced.
cdata.set('WEBP_NEAR_LOSSLESS', get_option('near-lossless') ? 1 : false)
# Note: the following flags are passed as argument because
# not all of the impacted code will have included `config.h`.
if get_option('disable-stats')
  add_project_arguments(
    '-DWEBP_DISABLE_STATS=1',
    language: 'c',
  )
endif
if get_option('reduce-csp')
  add_project_arguments(
    '-DWEBP_REDUCE_CSP=1',
    language: 'c',
  )
endif
if get_option('reduce-size')
  add_project_arguments(
    '-DWEBP_REDUCE_SIZE=1',
    language: 'c',
  )
endif

# Threading.
threads_dep = dependency(
  'threads',
  required: get_option('threads'),
)
cdata.set('WEBP_USE_THREAD', threads_dep.found() ? 1 : false)

# Headers.
foreach _hdr : ['cpu-features.h']
  cdata.set(
    'HAVE_' + _hdr.underscorify().to_upper(),
    cc.has_header(_hdr) ? 1 : false,
  )
endforeach

# Builtins.
foreach _builtin, _arg : {
  'bswap16': '1u << 15',
  'bswap32': '1u << 31',
  'bswap64': '1ull << 63',
}
  _fn = '__builtin_' + _builtin
  cdata.set(
    'HAVE_BUILTIN_' + _builtin.to_upper(),
    cc.links(
      '''
    int main(void) {
      (void)@0@(@1@);
      return 0;
    }
    '''.format(_fn, _arg),
      name: _fn,
    ) ? 1 : false,
  )
endforeach

# SIMD. {{{.

has_simd = false
simd_cflags = {}
simd_support = {}
simd_variants = [
  {
    'name'               : 'Neon',
    'id'                 : 'neon',
    'emscripten_on_args' : ['-msimd128', '-mfpu=neon'],
    'emscripten_off_args': [],
    'gcc_on_args'        : host_machine.cpu_family() == 'aarch64' ? [] : [
      '-mfpu=neon',
    ],
    'gcc_off_args'       : [],
  },
  {
    'name'               : 'SSE2',
    'id'                 : 'sse2',
    'emscripten_off_args': [],
    'emscripten_on_args' : ['-msimd128', '-msse2'],
    'gcc_off_args'       : ['-mno-sse2'],
    'gcc_on_args'        : ['-msse2'],
  },
  {
    'name'               : 'SSE4.1',
    'id'                 : 'sse41',
    'emscripten_off_args': [],
    'emscripten_on_args' : ['-msimd128', '-msse4.1'],
    'gcc_off_args'       : ['-mno-sse4.1'],
    'gcc_on_args'        : ['-msse4.1'],
  },
  {
    'name'               : 'AVX2',
    'id'                 : 'avx2',
    'emscripten_off_args': [],
    'emscripten_on_args' : ['-msimd128', '-mavx2'],
    'gcc_off_args'       : ['-mno-avx2'],
    'gcc_on_args'        : ['-mavx2'],
  },
]

foreach _variant : simd_variants
  # NOTE: we can't use `cc.get_supported_arguments()` for "on arguments",
  # has it calls `has_argument` individually for each argument, and the
  # combination of arguments is actually important (e.g. for Emscripten).
  _args = {
    'on': [],
    'off': [],
  }
  foreach _mode : _args.keys()
    foreach _syntax : [
      # We give the compiler id syntax priority.
      cc.get_id(),
      cc.get_argument_syntax(),
    ]
      _key = '@0@_@1@_args'.format(_syntax, _mode)
      if _variant.has_key(_key)
        _args += {
          _mode: _variant[_key],
        }
        break
      endif
    endforeach
  endforeach
  _flag = _variant['id'].to_upper()
  _supported = (get_option('simd').allowed()
  and cc.compiles(
      '''
      #include "src/dsp/cpu.h"
      int main(void) {
        #if !defined(WEBP_USE_@0@)
        # error flag is not enabled
        #endif
        return 0;
      }
      '''.format(_flag),
    args: _args['on'],
    include_directories: top_includes,
    name: 'SIMD (@0@) using @1@'.format(_variant['name'], _args['on']),
    )
)
  if _supported
    _args = _args['on']
  else
    # NOTE: we assume "off arguments" don't need to be combined.
    _args = cc.get_supported_arguments(_args['off'])
  endif
  cdata.set('WEBP_HAVE_@0@'.format(_flag), _supported ? 1 : false)
  simd_support += {
    _variant['name']: _supported,
  }
  simd_cflags += {
    _variant['id']: _args,
  }
  has_simd = has_simd or _supported
endforeach

get_option('simd').require(
  has_simd,
  error_message: 'no support',
)

has_neon_rtd = simd_support['Neon'] and host_machine.system() == 'linux'
cdata.set('WEBP_HAVE_NEON_RTCD', has_neon_rtd ? 1 : false)
if has_neon_rtd
  simd_support += {
    'Neon': 'Runtime detection',
  }
endif

# }}}

# Need to be first for `config.h` generation.
subdir('src/webp')

common_deps = [
  declare_dependency(
    include_directories: top_includes,
    sources: config_h,
  ),
  m_dep,
  threads_dep,
]

# Libraries:
# - libsharpyuv
subdir('sharpyuv')
# - libwebp/libwebpdecoder
subdir('src/dec')
subdir('src/dsp')
subdir('src/enc')
subdir('src/utils')
subdir('src')
# - libwebpdemux
subdir('src/demux')
# - libwebpmux
subdir('src/mux')

# Programs.
subdir('imageio')
subdir('examples')

summary(
  {
    'SIMD'   : has_simd,
    'Threads': threads_dep.found(),
  },
  bool_yn: true,
  section: 'Features',
)

summary(
  simd_support,
  bool_yn: true,
  section: 'SIMD',
)
