# upstream project does, in fact, provides meson.build. However, it uses
# different lua.wrap as dependency and it is incompatible with wrap file
# already in WrapDB. So we provide some simple header-only meson.build
# dependency. It is user responsibility to link everything with appropriate
# Lua
project(
  'sol2',
  'cpp',
  license: 'MIT',
  meson_version: '>=0.58',
)

includes = include_directories('include')

# Expose standard dependency.
sol2 = declare_dependency(
	include_directories: include_directories('./include'),
)
