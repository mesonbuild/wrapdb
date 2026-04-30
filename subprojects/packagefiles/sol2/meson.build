# upstream project does, in fact, provides meson.build. However, it uses
# different lua.wrap as dependency and it is incompatible with wrap file
# already in WrapDB. So we provide some simple header-only meson.build
# dependency. It is user responsibility to link everything with appropriate
# Lua

# Developer note: intstruction on how to update this wrap
# 1. Get new tag from upstream github and add it to sol2.wrap with correct
#    sha256 hash and so on.
# 2. Upstream meson.build is unlikely to be compatible. Go to ci_config.json,
#    find section for "sol2" and update "ignore_upstream_meson"
# 3. Go to releases.json and add new version to "versions"
# 4. Open sol2.wrap and update source_filename. Remember - source_filename
#    is how you want to name downloaded archive. It doesn't have to match
#    default name at all.
project(
  'sol2',
  'cpp',
  license: 'MIT',
  meson_version: '>=0.58',
)

# Expose standard dependency.
sol2 = declare_dependency(
  include_directories: include_directories('./include'),
)
