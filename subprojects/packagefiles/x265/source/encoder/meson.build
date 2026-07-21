if cc.get_id() in ['gcc', 'clang']
  c_args += ['-Wno-uninitialized']
endif

if cc.get_argument_syntax() == 'msvc'
  # potentially uninitialized local variable 'foo' used
  c_args += ['/wd4701']
endif

encoder_srcs = files(
  '../x265.h',
  'analysis.cpp',
  'analysis.h',
  'api.cpp',
  'bitcost.cpp',
  'bitcost.h',
  'dpb.cpp',
  'dpb.h',
  'encoder.cpp',
  'encoder.h',
  'entropy.cpp',
  'entropy.h',
  'frameencoder.cpp',
  'frameencoder.h',
  'framefilter.cpp',
  'framefilter.h',
  'level.cpp',
  'level.h',
  'motion.cpp',
  'motion.h',
  'nal.cpp',
  'nal.h',
  'ratecontrol.cpp',
  'ratecontrol.h',
  'rdcost.h',
  'reference.cpp',
  'reference.h',
  'sao.cpp',
  'sao.h',
  'search.cpp',
  'search.h',
  'sei.cpp',
  'sei.h',
  'slicetype.cpp',
  'slicetype.h',
  'svt.h',
  'weightPrediction.cpp',
)

encoders = []

foreach bit, depth : bit_depths
  encoder_args = c_args + get_variable(f'@depth@_args')
  encoders += static_library(
    f'encoder-@depth@',
    encoder_srcs,
    c_args: encoder_args,
    cpp_args: encoder_args,
    include_directories: include_dirs,
    build_by_default: false,
      # gnu_symbol_visibility: 'inlineshidden',
  )
endforeach
