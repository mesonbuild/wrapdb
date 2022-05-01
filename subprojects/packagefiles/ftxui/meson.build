project('ftxui', 'cpp',
    version: '2.0.0',
    default_options: ['cpp_std=c++17'],
)

if host_machine.system() == 'windows'
  add_project_arguments('/utf-8', '-DUNICODE', language: 'cpp')
endif

thread_dep = dependency('threads')

# Upstream CMake supports only static linking,
# so we do the same.

screen_lib = static_library('screen',
    'src/ftxui/screen/box.cpp',
    'src/ftxui/screen/color.cpp',
    'src/ftxui/screen/color_info.cpp',
    'src/ftxui/screen/screen.cpp',
    'src/ftxui/screen/string.cpp',
    'src/ftxui/screen/terminal.cpp',
    include_directories: 'include',
    dependencies: thread_dep,
)

dom_lib = static_library('dom',
    'src/ftxui/dom/blink.cpp',
    'src/ftxui/dom/bold.cpp',
    'src/ftxui/dom/border.cpp',
    'src/ftxui/dom/box_helper.cpp',
    'src/ftxui/dom/canvas.cpp',
    'src/ftxui/dom/clear_under.cpp',
    'src/ftxui/dom/color.cpp',
    'src/ftxui/dom/composite_decorator.cpp',
    'src/ftxui/dom/dbox.cpp',
    'src/ftxui/dom/dim.cpp',
    'src/ftxui/dom/flex.cpp',
    'src/ftxui/dom/flexbox.cpp',
    'src/ftxui/dom/flexbox_config.cpp',
    'src/ftxui/dom/flexbox_helper.cpp',
    'src/ftxui/dom/focus.cpp',
    'src/ftxui/dom/frame.cpp',
    'src/ftxui/dom/gauge.cpp',
    'src/ftxui/dom/graph.cpp',
    'src/ftxui/dom/gridbox.cpp',
    'src/ftxui/dom/hbox.cpp',
    'src/ftxui/dom/inverted.cpp',
    'src/ftxui/dom/node.cpp',
    'src/ftxui/dom/node_decorator.cpp',
    'src/ftxui/dom/paragraph.cpp',
    'src/ftxui/dom/reflect.cpp',
    'src/ftxui/dom/scroll_indicator.cpp',
    'src/ftxui/dom/separator.cpp',
    'src/ftxui/dom/size.cpp',
    'src/ftxui/dom/spinner.cpp',
    'src/ftxui/dom/table.cpp',
    'src/ftxui/dom/text.cpp',
    'src/ftxui/dom/underlined.cpp',
    'src/ftxui/dom/util.cpp',
    'src/ftxui/dom/vbox.cpp',
    include_directories: ['include', 'src'],
    link_with: screen_lib,
    dependencies: thread_dep,
)

component_lib = static_library('component',
    'src/ftxui/component/button.cpp',
    'src/ftxui/component/catch_event.cpp',
    'src/ftxui/component/checkbox.cpp',
    'src/ftxui/component/collapsible.cpp',
    'src/ftxui/component/component.cpp',
    'src/ftxui/component/container.cpp',
    'src/ftxui/component/dropdown.cpp',
    'src/ftxui/component/event.cpp',
    'src/ftxui/component/input.cpp',
    'src/ftxui/component/maybe.cpp',
    'src/ftxui/component/menu.cpp',
    'src/ftxui/component/radiobox.cpp',
    'src/ftxui/component/radiobox.cpp',
    'src/ftxui/component/renderer.cpp',
    'src/ftxui/component/resizable_split.cpp',
    'src/ftxui/component/screen_interactive.cpp',
    'src/ftxui/component/slider.cpp',
    'src/ftxui/component/terminal_input_parser.cpp',
    'src/ftxui/component/toggle.cpp',
    include_directories: ['include', 'src'],
    link_with: [dom_lib, screen_lib],
    dependencies: thread_dep,
)

screen_dep = declare_dependency(link_with: screen_lib,
    include_directories: 'include')

dom_dep = declare_dependency(link_with: dom_lib,
    include_directories: 'include')

component_dep = declare_dependency(link_with: component_lib,
    include_directories: 'include')

subdir('examples')
