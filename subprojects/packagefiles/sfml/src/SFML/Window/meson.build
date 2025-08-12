window_sources = files(
  'Clipboard.cpp',
  'Context.cpp',
  'Cursor.cpp',
  'GlContext.cpp',
  'GlResource.cpp',
  'Joystick.cpp',
  'JoystickManager.cpp',
  'Keyboard.cpp',
  'Mouse.cpp',
  'Sensor.cpp',
  'SensorManager.cpp',
  'Touch.cpp',
  'VideoMode.cpp',
  'Vulkan.cpp',
  'Window.cpp',
  'WindowBase.cpp',
  'WindowImpl.cpp',
)

if host_machine.system() == 'windows'
  window_sources += files(
    'Win32/ClipboardImpl.cpp',
    'Win32/CursorImpl.cpp',
    'Win32/InputImpl.cpp',
    'Win32/JoystickImpl.cpp',
    'Win32/SensorImpl.cpp',
    'Win32/VideoModeImpl.cpp',
    'Win32/VulkanImplWin32.cpp',
    'Win32/WglContext.cpp',
    'Win32/WindowImplWin32.cpp',
  )
  window_deps = []
elif host_machine.system() == 'linux'
  window_sources += files(
    'Unix/ClipboardImpl.cpp',
    'Unix/CursorImpl.cpp',
    'Unix/Display.cpp',
    'Unix/GlxContext.cpp',
    'Unix/InputImpl.cpp',
    'Unix/JoystickImpl.cpp',
    'Unix/KeySymToKeyMapping.cpp',
    'Unix/KeySymToUnicodeMapping.cpp',
    'Unix/KeyboardImpl.cpp',
    'Unix/SensorImpl.cpp',
    'Unix/VideoModeImpl.cpp',
    'Unix/VulkanImplX11.cpp',
    'Unix/WindowImplX11.cpp',
  )
  window_deps = [
    dependency('xcursor'),
    dependency('xrandr'),
    dependency('x11'),
    dependency('xi'),
    dependency('libudev'),
  ]
elif host_machine.system() == 'darwin'
  add_languages(
    'objc',
    native: false,
  )
  add_languages(
    'objcpp',
    native: false,
  )
  window_sources += files(
    'macOS/AutoreleasePoolWrapper.mm',
    'macOS/ClipboardImpl.mm',
    'macOS/CursorImpl.mm',
    'macOS/HIDInputManager.mm',
    'macOS/HIDJoystickManager.cpp',
    'macOS/InputImpl.mm',
    'macOS/JoystickImpl.cpp',
    'macOS/NSImage+raw.mm',
    'macOS/SFApplication.m',
    'macOS/SFApplicationDelegate.m',
    'macOS/SFContext.mm',
    'macOS/SFKeyboardModifiersHelper.mm',
    'macOS/SFOpenGLView+keyboard.mm',
    'macOS/SFOpenGLView+mouse.mm',
    'macOS/SFOpenGLView.mm',
    'macOS/SFSilentResponder.m',
    'macOS/SFViewController.mm',
    'macOS/SFWindow.m',
    'macOS/SFWindowController.mm',
    'macOS/SensorImpl.cpp',
    'macOS/VideoModeImpl.cpp',
    'macOS/WindowImplCocoa.mm',
    'macOS/cg_sf_conversion.mm',
  )
  window_deps = dependency(
    'appleframeworks',
    modules: ['Foundation', 'AppKit', 'IOKit', 'Carbon'],
  )
else
  error('Not yet implemented.')
endif

window_lib = library(
  'sfml-window',
  window_sources,
  cpp_args: [
    get_option('default_library') != 'static' ? '-DSFML_WINDOW_EXPORTS' : '-DSFML_STATIC',
    '-DUNICODE',
  ],
  link_with: system_lib,
  include_directories: [glad_inc, pub_inc, priv_inc, vulkan_inc],
  dependencies: [gl_dep, winmm_dep, window_deps],
)
