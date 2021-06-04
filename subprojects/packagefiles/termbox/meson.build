project('termbox', 'c', version: '1.1.2')

src = ['src/utf8.c', 'src/termbox.c']
c_args = ['-D_XOPEN_SOURCE']
lib = library('termbox', src, c_args: c_args)

configure_file(copy: true, input: 'src/termbox.h', output: 'termbox.h')
inc = include_directories('.')

termbox_dep = declare_dependency(link_with: lib, include_directories: inc)
meson.override_dependency('termbox', termbox_dep)
