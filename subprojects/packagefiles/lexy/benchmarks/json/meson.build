


fetch_targets = []

data = [
    ['canada.json', 'https://github.com/miloyip/nativejson-benchmark/raw/master/data/canada.json'],
    [
        'citm_catalog.json',
        'https://github.com/miloyip/nativejson-benchmark/raw/master/data/citm_catalog.json',
    ],
    [
        'twitter.json',
        'https://raw.githubusercontent.com/miloyip/nativejson-benchmark/master/data/twitter.json',
    ],
]

foreach d : data

    name = d[0]
    url = d[1]

    curl = find_program('curl', required: false)

    if curl.found()

        fetch_targets += custom_target(
            'fetch_' + name,
            output: name,
            command: [curl, url, '-o', '@OUTPUT@'],
        )

    else
        wget = find_program('wget')

        fetch_targets += custom_target(
            'fetch_' + name,
            output: name,
            command: [wget, url, '-O', '@OUTPUT@'],
        )

    endif


endforeach



benchmark_files = files('baseline.cpp', 'lexy.cpp', 'main.cpp')

pegtl_dep = dependency('PEGTL', required: false)
if pegtl_dep.found()
    benchmark_files += files('pegtl.cpp')
endif

json_dep = dependency('nlohmann_json', required: false)
if json_dep.found()
    benchmark_files += files('nlohmann.cpp')
endif

rapidjson_dep = dependency('rapidjson', required: false)
if rapidjson_dep.found()
    benchmark_files += files('rapidjson.cpp')
endif

# in the original also Boost.JSON is downloaded an used to compare it, that isn't done here 

json_benchmark = executable(
    'json',
    benchmark_files,
    dependencies: [benchmarks_deps, fetch_targets],
    cpp_args: ['-DLEXY_BENCHMARK_DATA=' + meson.current_build_dir()],
)
benchmark('json_benchmark', json_benchmark)
