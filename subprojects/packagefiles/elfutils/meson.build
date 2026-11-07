project('elfutils', 'c', meson_version: '>=0.56.0')

# elfutils generates definition files using `m4`
# TODO: we could be smarter here and handle cases where the `m4`
# binary is setup as a subproject
m4 = find_program('m4', required: true)

mod = import('unstable-external_project')

proj = mod.add_project('configure',
  configure_options: [
    '--prefix=@PREFIX@',
    '--libdir=@PREFIX@/@LIBDIR@',
    '--includedir=@PREFIX@/@INCLUDEDIR@',
    '--disable-debuginfod',
  ],
)

asm = proj.dependency('asm')
dw = proj.dependency('dw')
elf = proj.dependency('elf')
