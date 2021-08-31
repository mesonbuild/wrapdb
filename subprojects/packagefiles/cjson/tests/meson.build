tests = [
    'cjson_add',
    'compare_tests',
    'json_patch_tests',
    'minify_tests',
    'misc_tests',
    'misc_utils_tests',
    'old_utils_tests',
    'parse_array',
    'parse_examples',
    'parse_hex4',
    'parse_number',
    'parse_object',
    'parse_string',
    'parse_value',
    'parse_with_opts',
    'print_array',
    'print_number',
    'print_object',
    'print_string',
    'print_value',
    'readme_examples',
]

unity = library('unity', 'unity/src/unity.c')
unity_dep = declare_dependency(link_with: unity, include_directories: 'unity/src')

foreach t : tests
    e = executable(
        t,
        '@0@.c'.format(t),
        dependencies: [
            libcjson_dep,
            unity_dep,
        ]
    )

    test(t, e, workdir: meson.current_source_dir())
endforeach
