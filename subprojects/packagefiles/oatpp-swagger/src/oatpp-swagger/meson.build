header_files = files(
    'oas3/Model.hpp',
    'AsyncController.hpp',
    'Controller.hpp',
    'Generator.hpp',
    'Model.hpp',
    'Resources.hpp',
    'Types.hpp',
)

src_files += header_files

src_files += files('Generator.cpp', 'Resources.cpp', 'Types.cpp')


install_headers(header_files, subdir: 'oatpp-swagger')
