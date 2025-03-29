header_files = files(
  'AsyncController.hpp',
  'Controller.hpp',
  'Generator.hpp',
  'Model.hpp',
  'Resources.hpp',
  'Types.hpp',
  'oas3/Model.hpp',
)

src_files += header_files

src_files += files('Generator.cpp', 'Resources.cpp', 'Types.cpp')


install_headers(
  header_files,
  subdir: 'oatpp-swagger',
)
