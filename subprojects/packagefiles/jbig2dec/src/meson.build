# Because of the presence of `getopt.h` alongside the standard source files,
# and the mix of private and public headers in the same directory, we copy
# only the files needed to the build directory.
foreach _listname, _needed : {
  'lib_inc'  : true,
  'lib_src'  : true,
  'progs_src': progs_opt.allowed(),
  'tests_src': progs_opt.allowed(),
}
  if not _needed
    continue
  endif
  _srclist = get_variable(_listname)
  _dstlist = []
  foreach _file : _srclist
    _filecopy = fs.copyfile('..' / _file, _file)
    set_variable(_file.underscorify(), _filecopy)
    _dstlist += _filecopy
  endforeach
  set_variable(_listname, _dstlist)
endforeach

config_h = configure_file(
  configuration: cdata,
  input: 'config.h.meson',
  output: 'config.h',
)

config_types_h = configure_file(
  configuration: cdata,
  input: 'config_types.h.meson',
  output: 'config_types.h',
)

lib_inc += [config_h, config_types_h, jbig2_h]

jbig2dec_lib = library(
  'jbig2dec',
  [lib_inc, lib_src],
  dependencies: m_dep,
  install: true,
  version: '0.0.0',
  vs_module_defs: 'jbig2dec.def',
)

jbig2dec_dep = declare_dependency(
  include_directories: public_include,
  link_with: jbig2dec_lib,
  sources: jbig2_h,
)
meson.override_dependency('jbig2dec', jbig2dec_dep)

pkg = import('pkgconfig')
pkg.generate(
  jbig2dec_lib,
  description: 'JBIG2 decoder library.',
  filebase: 'jbig2dec',
  name: 'libjbig2dec',
)

if progs_opt.allowed()
  executable(
    'jbig2dec',
    [lib_inc, progs_src],
    dependencies: [jbig2dec_dep, png_dep],
    install: true,
  )
endif

if tests_opt.allowed()
  # Tests need access to all symbols, including on Windows.
  jbig2dec_priv_lib = static_library(
    'jbig2dec_priv',
    objects: jbig2dec_lib.extract_all_objects(
      recursive: true,
    ),
  )
  foreach _name, _src : {
    'arith'  : jbig2_arith_c,
    'huffman': jbig2_huffman_c,
    'sha1'   : sha1_c,
  }
    test(
      _name,
      executable(
        _name,
        [lib_inc, _src],
        c_args: '-DTEST',
        include_directories: public_include,
        link_with: jbig2dec_priv_lib,
      ),
    )
  endforeach
endif
