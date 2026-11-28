subdir('4.3')
subdir('4.4')
subdir('4.5')
subdir('4.6')
subdir('4.7')

generated_sources_map = {
  '4.3': sources_4_3,
  '4.4': sources_4_4,
  '4.5': sources_4_5,
  '4.6': sources_4_6,
  '4.7': sources_4_7,
}

# List of common sources. These are version-independent.
common_sources = files(
  '../src/classes/editor_plugin_registration.cpp',
  '../src/classes/low_level.cpp',
  '../src/classes/wrapped.cpp',
  '../src/core/class_db.cpp',
  '../src/core/error_macros.cpp',
  '../src/core/memory.cpp',
  '../src/core/method_bind.cpp',
  '../src/core/object.cpp',
  '../src/core/print_string.cpp',
  '../src/variant/aabb.cpp',
  '../src/variant/basis.cpp',
  '../src/variant/callable_custom.cpp',
  '../src/variant/callable_method_pointer.cpp',
  '../src/variant/char_string.cpp',
  '../src/variant/color.cpp',
  '../src/variant/packed_arrays.cpp',
  '../src/variant/plane.cpp',
  '../src/variant/projection.cpp',
  '../src/variant/quaternion.cpp',
  '../src/variant/rect2.cpp',
  '../src/variant/rect2i.cpp',
  '../src/variant/transform2d.cpp',
  '../src/variant/transform3d.cpp',
  '../src/variant/variant.cpp',
  '../src/variant/variant_internal.cpp',
  '../src/variant/vector2.cpp',
  '../src/variant/vector2i.cpp',
  '../src/variant/vector3.cpp',
  '../src/variant/vector3i.cpp',
  '../src/variant/vector4.cpp',
  '../src/variant/vector4i.cpp',
  '../src/godot.cpp',
)
version_specific_sources = files(generated_sources_map[godot_api_version])
