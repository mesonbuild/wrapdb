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
    'Touch.cpp',
    'Sensor.cpp',
    'SensorManager.cpp',
    'VideoMode.cpp',
    'Window.cpp',
    'WindowImpl.cpp',
)

if host_machine.system() == 'windows'
    window_sources += files(
        'Win32/CursorImpl.cpp',
        'Win32/ClipboardImpl.cpp',
        'Win32/WglContext.cpp',
        'Win32/WglExtensions.cpp',
        'Win32/InputImpl.cpp',
        'Win32/JoystickImpl.cpp',
        'Win32/SensorImpl.cpp',
        'Win32/VideoModeImpl.cpp',
        'Win32/WindowImplWin32.cpp',
    )
    window_deps = []
elif host_machine.system() == 'linux'
    window_sources += files(
        'Unix/CursorImpl.cpp',
        'Unix/ClipboardImpl.cpp',
        'Unix/Display.cpp',
        'Unix/InputImpl.cpp',
        'Unix/SensorImpl.cpp',
        'Unix/VideoModeImpl.cpp',
        'Unix/WindowImplX11.cpp',
        'Unix/JoystickImpl.cpp',
        'Unix/GlxContext.cpp',
        'Unix/GlxExtensions.cpp',
    )
    window_deps = [dependency('xrandr'), dependency('x11'), dependency('libudev')]
else
    error('Not yet implemented.')
endif

symbol_args = get_option('default_library') == 'shared' ? ['-DSFML_WINDOW_EXPORTS'] : ['-DSFML_STATIC']

window_lib = library('sfml-window',
    window_sources,
    cpp_args: symbol_args + ['-DUNICODE'],
    link_with: [system_lib],
    include_directories: [pub_inc, priv_inc],
    dependencies: [gl_dep, winmm_dep] + window_deps,
)
