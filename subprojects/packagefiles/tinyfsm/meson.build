project(
  'tinyfsm',
  'cpp',
  version: '0.3.3',
  meson_version: '>=0.50.0',
  license: 'MIT',
)

tinyfsm_dep = declare_dependency(
  include_directories: include_directories('include'),
)

# build examples as compile tests
build_examples = get_option('build_examples')

# elevator example
ex_elevator_exe = executable(
  'elevator',
  [
    'examples/elevator/elevator.cpp',
    'examples/elevator/main.cpp',
    'examples/elevator/motor.cpp',
  ],
  include_directories: 'examples/elevator',
  override_options: 'cpp_std=c++11',
  dependencies: tinyfsm_dep,
  build_by_default: build_examples,
)

# debugging_switch example
ex_debugging_switch_exe = executable(
  'debugging_switch',
  'examples/api/debugging_switch.cpp',
  include_directories: 'examples/api',
  override_options: 'cpp_std=c++11',
  dependencies: tinyfsm_dep,
  build_by_default: build_examples,
)

# mealy_machine example
ex_mealy_machine_exe = executable(
  'mealy_machine',
  'examples/api/mealy_machine.cpp',
  include_directories: 'examples/api',
  override_options: 'cpp_std=c++11',
  dependencies: tinyfsm_dep,
  build_by_default: build_examples,
)

# moore_machine example
ex_moore_machine_exe = executable(
  'moore_machine',
  'examples/api/moore_machine.cpp',
  include_directories: 'examples/api',
  override_options: 'cpp_std=c++11',
  dependencies: tinyfsm_dep,
  build_by_default: build_examples,
)

# multiple_switch example
ex_multiple_switch_exe = executable(
  'multiple_switch',
  'examples/api/multiple_switch.cpp',
  include_directories: 'examples/api',
  override_options: 'cpp_std=c++11',
  dependencies: tinyfsm_dep,
  build_by_default: build_examples,
)

# resetting_switch example
ex_resetting_switch_exe = executable(
  'resetting_switch',
  'examples/api/resetting_switch.cpp',
  include_directories: 'examples/api',
  override_options: 'cpp_std=c++11',
  dependencies: tinyfsm_dep,
  build_by_default: build_examples,
)

# simple_switch example
ex_simple_switch_exe = executable(
  'simple_switch',
  'examples/api/simple_switch.cpp',
  include_directories: 'examples/api',
  override_options: 'cpp_std=c++11',
  dependencies: tinyfsm_dep,
  build_by_default: build_examples,
)
