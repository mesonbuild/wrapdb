project(
  'indicators',
  'cpp',
  version: '2.3',
  license: 'MIT',
)

includes = include_directories(['single_include', 'include'])

indicators_dep = declare_dependency(
  include_directories: includes,
)

install_headers(
  [
    'include/indicators/block_progress_bar.hpp',
    'include/indicators/color.hpp',
    'include/indicators/cursor_control.hpp',
    'include/indicators/cursor_movement.hpp',
    'include/indicators/details/stream_helper.hpp',
    'include/indicators/display_width.hpp',
    'include/indicators/dynamic_progress.hpp',
    'include/indicators/font_style.hpp',
    'include/indicators/indeterminate_progress_bar.hpp',
    'include/indicators/multi_progress.hpp',
    'include/indicators/progress_bar.hpp',
    'include/indicators/progress_spinner.hpp',
    'include/indicators/progress_type.hpp',
    'include/indicators/setting.hpp',
    'include/indicators/termcolor.hpp',
    'include/indicators/terminal_size.hpp',
    'single_include/indicators/indicators.hpp',
  ],
  subdir: 'indicators',
)
