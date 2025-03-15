swar_benchmark = executable(
    'swar',
    files(
        'any.cpp',
        'delimited.cpp',
        'digits.cpp',
        'identifier.cpp',
        'literal.cpp',
        'main.cpp',
        'swar.hpp',
        'until.cpp',
    ),
    dependencies: benchmarks_deps,
)
benchmark('swar_benchmark', swar_benchmark)
