project(
  'x-plane-sdk',
  'c',
  version: '4.0.1',
  license: 'MIT',
  default_options: 'warning_level=0',
  meson_version: '>= 0.60.0',
)

xplm_incdir = include_directories('SDK/CHeaders/XPLM')
widgets_incdir = include_directories('SDK/CHeaders/Widgets')
wrappers_incdir = include_directories('SDK/CHeaders/Wrappers')

cc = meson.get_compiler('c')

ca = []
xplm_level = get_option('xplm-level')

if xplm_level >= 200
  ca += '-DXPLM200'
endif

if xplm_level >= 210
  ca += '-DXPLM210'
endif

if xplm_level >= 300
  ca += '-DXPLM300'
endif

if xplm_level >= 301
  ca += '-DXPLM301'
endif

if xplm_level >= 303
  ca += '-DXPLM303'
endif

if xplm_level >= 400
  ca += '-DXPLM400'
endif

if target_machine.system() == 'windows'
  ca += ['-DAPL=0', '-DIBM=1', '-DLIN=0']
  xplm_dep = declare_dependency(
    compile_args: ca,
    include_directories: [xplm_incdir],
    dependencies: [
      cc.find_library(
        'XPLM_64',
        dirs: [meson.current_source_dir() / 'SDK' / 'Libraries' / 'Win'],
      ),
    ],
  )
  xpwidgets_dep = declare_dependency(
    compile_args: ca,
    include_directories: [widgets_incdir],
    dependencies: [
      xplm_dep,
      cc.find_library(
        'XPWidgets_64',
        dirs: [meson.current_source_dir() / 'SDK' / 'Libraries' / 'Win'],
      ),
    ],
  )
elif target_machine.system() == 'darwin'
  ca += ['-DAPL=1', '-DIBM=0', '-DLIN=0']
  xplm_dep = declare_dependency(
    compile_args: ca,
    link_args: [
      '-F' + meson.current_source_dir() / 'SDK' / 'Libraries' / 'Mac',
      '-framework',
      'XPLM',
    ],
    include_directories: [xplm_incdir],
  )
  xpwidgets_dep = declare_dependency(
    compile_args: ca,
    link_args: [
      '-F' + meson.current_source_dir() / 'SDK' / 'Libraries' / 'Mac',
      '-framework',
      'XPWidgets',
    ],
    include_directories: [widgets_incdir],
    dependencies: [xplm_dep],
  )
else
  ca += ['-DAPL=0', '-DIBM=0', '-DLIN=1']
  xplm_dep = declare_dependency(
    compile_args: ca,
    include_directories: [xplm_incdir],
  )
  xpwidgets_dep = declare_dependency(
    compile_args: ca,
    include_directories: [widgets_incdir],
    dependencies: [xplm_dep],
  )
endif

if add_languages(
  'cpp',
  native: false,
  required: get_option('cpp'),
)
  xpcpp_dir = 'SDK/CHeaders/Wrappers'
  # There is no reason to make this a dynamic library.
  # Static is the only sensible choice for this particular library.
  xpcpp = static_library(
    'xpcpp',
    cpp_args: ca,
    include_directories: [wrappers_incdir],
    pic: true,
    dependencies: [xplm_dep, xpwidgets_dep],
    sources: [
      xpcpp_dir / 'XPCBroadcaster.cpp',
      xpcpp_dir / 'XPCDisplay.cpp',
      xpcpp_dir / 'XPCListener.cpp',
      xpcpp_dir / 'XPCProcessing.cpp',
      xpcpp_dir / 'XPCWidgetAttachments.cpp',
      xpcpp_dir / 'XPCWidget.cpp',
    ],
  )

  xpcpp_dep = declare_dependency(
    compile_args: ca,
    dependencies: [xplm_dep, xpwidgets_dep],
    include_directories: [wrappers_incdir],
    link_with: [xpcpp],
  )
else
  xpcpp_dep = dependency(
    '',
    required: false,
  )
endif
