cunit_dep = dependency('cunit', required : false)

if not cunit_dep.found()
  message('CUnit not found, skipping scpi-parser tests')
  subdir_done()
endif

cc = meson.get_compiler('c')

libscpi_test_options = []
libscpi_wanted_test_options = [
  # lots of visual noise during test compile, can only fix in upstream
  '-Wno-unused-but-set-variable',
  '-Wno-unused',
]

foreach opt : libscpi_wanted_test_options
  if cc.has_argument(opt)
    libscpi_test_options += opt
  endif
endforeach

test_names = [
  'test_fifo',
  'test_lexer_parser',
  'test_parser',
  'test_scpi_utils',
]

foreach t : test_names
  test_exe = executable(t, t+'.c',
    c_args : libscpi_test_options,
    dependencies : [ cunit_dep ],
    include_directories : libscpi_inc,

    # make sure "hidden" symbols from a static lib are defined
    objects : libscpi_lib.extract_all_objects(recursive : true),
  )
  test(t, test_exe)
endforeach
