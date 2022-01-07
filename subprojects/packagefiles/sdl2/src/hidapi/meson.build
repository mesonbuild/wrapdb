all_sources += files(
  'SDL_hidapi.c',
)

core_inc += include_directories('hidapi')

if host_machine.system() == 'windows'
  core_deps += [cc.find_library('setupapi')]
endif
