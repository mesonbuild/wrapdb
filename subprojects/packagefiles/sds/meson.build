project('sds', 'c', version : '2.0.0', license: 'BSD-2-Clause')

sds_inc = include_directories('.')

sds_lib = library('sds',
    sources: ['sds.c'],
    include_directories: sds_inc,
)

sds_dep = declare_dependency(
    link_with: [sds_lib],
    include_directories: sds_inc,
)

if get_option('tests')
    sds_test_exe = executable('hts_endian',
        sources: ['sds.c'],
        c_args: ['-DSDS_TEST_MAIN'],
        include_directories: sds_inc,
    )

    test('sds_test', sds_test_exe)
endif
