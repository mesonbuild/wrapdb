# bgfx examples
# cmake: examples.cmake — each example links example-common (imgui_dep)
# Disabled: 21-deferred, 37-gpudrivenrendering, 41-tess (same as cmake)

example_args = [
  '-DENTRY_CONFIG_IMPLEMENT_MAIN=1',
  '-D__STDC_FORMAT_MACROS',
  '-D_CRT_SECURE_NO_WARNINGS',
]

if opt_with_wayland
  example_args += '-DENTRY_CONFIG_USE_WAYLAND=1'
endif

# Most examples are single .cpp files linking imgui_dep (example-common)
examples = {
  'example-00-helloworld':       ['00-helloworld/helloworld.cpp'],
  'example-01-cubes':            ['01-cubes/cubes.cpp'],
  'example-02-metaballs':        ['02-metaballs/metaballs.cpp'],
  'example-03-raymarch':         ['03-raymarch/raymarch.cpp'],
  'example-04-mesh':             ['04-mesh/mesh.cpp'],
  'example-05-instancing':       ['05-instancing/instancing.cpp'],
  'example-06-bump':             ['06-bump/bump.cpp'],
  'example-07-callback':         ['07-callback/callback.cpp'],
  'example-08-update':           ['08-update/update.cpp'],
  'example-09-hdr':              ['09-hdr/hdr.cpp'],
  'example-10-font':             ['10-font/font.cpp'],
  'example-11-fontsdf':          ['11-fontsdf/fontsdf.cpp'],
  'example-12-lod':              ['12-lod/lod.cpp'],
  'example-13-stencil':          ['13-stencil/stencil.cpp'],
  'example-14-shadowvolumes':    ['14-shadowvolumes/shadowvolumes.cpp'],
  'example-15-shadowmaps-simple':['15-shadowmaps-simple/shadowmaps_simple.cpp'],
  'example-16-shadowmaps':       ['16-shadowmaps/shadowmaps.cpp'],
  'example-17-drawstress':       ['17-drawstress/drawstress.cpp'],
  'example-18-ibl':              ['18-ibl/ibl.cpp'],
  'example-19-oit':              ['19-oit/oit.cpp'],
  'example-20-nanovg':           ['20-nanovg/nanovg.cpp'],
  # 21-deferred: DISABLED in cmake
  'example-22-windows':          ['22-windows/windows.cpp'],
  'example-23-vectordisplay':    ['23-vectordisplay/vectordisplay.cpp', '23-vectordisplay/main.cpp'],
  'example-24-nbody':            ['24-nbody/nbody.cpp'],
  'example-26-occlusion':        ['26-occlusion/occlusion.cpp'],
  'example-27-terrain':          ['27-terrain/terrain.cpp'],
  'example-28-wireframe':        ['28-wireframe/wireframe.cpp'],
  'example-29-debugdraw':        ['29-debugdraw/debugdraw.cpp'],
  'example-30-picking':          ['30-picking/picking.cpp'],
  'example-31-rsm':              ['31-rsm/reflectiveshadowmap.cpp'],
  'example-32-particles':        ['32-particles/particles.cpp'],
  'example-33-pom':              ['33-pom/pom.cpp'],
  'example-34-mvs':              ['34-mvs/mvs.cpp'],
  'example-35-dynamic':          ['35-dynamic/dynamic.cpp'],
  'example-36-sky':              ['36-sky/sky.cpp'],
  # 37-gpudrivenrendering: DISABLED in cmake
  'example-38-bloom':            ['38-bloom/bloom.cpp'],
  'example-39-assao':            ['39-assao/assao.cpp'],
  'example-40-svt':              ['40-svt/svt.cpp', '40-svt/vt.cpp'],
  # 41-tess: DISABLED in cmake
  'example-43-denoise':          ['43-denoise/denoise.cpp'],
  'example-44-sss':              ['44-sss/screen_space_shadows.cpp'],
  'example-45-bokeh':            ['45-bokeh/bokeh.cpp'],
  'example-46-fsr':              ['46-fsr/fsr.cpp', '46-fsr/app.cpp'],
  'example-47-pixelformats':     ['47-pixelformats/pixelformats.cpp'],
  'example-48-drawindirect':     ['48-drawindirect/drawindirect.cpp'],
  'example-49-hextile':          ['49-hextile/hextile.cpp'],
  'example-50-headless':         ['50-headless/headless.cpp'],
  'example-51-gpufont':          ['51-gpufont/gpufont.cpp'],
}

foreach name, srcs : examples
  executable(name, files(srcs),
    dependencies: imgui_dep,
    cpp_args: example_args,
  )
endforeach

# 25-c99: C example — still uses example-common entry system
executable('example-25-c99', files('25-c99/helloworld.c'),
  dependencies: imgui_dep,
  c_args: example_args,
)

# 42-bunnylod: Mixed C/C++ (progmesh.c + bunnylod.cpp)
executable('example-42-bunnylod',
  files('42-bunnylod/bunnylod.cpp', '42-bunnylod/progmesh.c'),
  dependencies: imgui_dep,
  cpp_args: example_args,
)
