project('asio',
    'cpp',
    version : '1.22.1',
    license : 'Boost'
)

asio_deps = []

# For windows builds, ASIO depends on ws2_32
if target_machine.system() == 'windows'
    compiler = meson.get_compiler('cpp')
    ws2_32_dep = compiler.find_library('ws2_32', required: true)
    asio_deps += ws2_32_dep
endif

add_project_arguments('-DASIO_STANDALONE', language : 'cpp')

asio_dep = declare_dependency(
    include_directories : include_directories('include'),
    dependencies: asio_deps,
)
