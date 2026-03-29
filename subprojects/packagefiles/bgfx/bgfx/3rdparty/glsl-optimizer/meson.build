# glsl-optimizer

glsl_optimizer_sources = files(
  # src/glsl/glcpp/
  'src/glsl/glcpp/glcpp-lex.c',
  'src/glsl/glcpp/glcpp-parse.c',
  'src/glsl/glcpp/pp.c',
  # src/glsl/
  'src/glsl/ast_array_index.cpp',
  'src/glsl/ast_expr.cpp',
  'src/glsl/ast_function.cpp',
  'src/glsl/ast_to_hir.cpp',
  'src/glsl/ast_type.cpp',
  'src/glsl/builtin_functions.cpp',
  'src/glsl/builtin_types.cpp',
  'src/glsl/builtin_variables.cpp',
  'src/glsl/glsl_lexer.cpp',
  'src/glsl/glsl_optimizer.cpp',
  'src/glsl/glsl_parser.cpp',
  'src/glsl/glsl_parser_extras.cpp',
  'src/glsl/glsl_symbol_table.cpp',
  'src/glsl/glsl_types.cpp',
  'src/glsl/hir_field_selection.cpp',
  'src/glsl/ir.cpp',
  'src/glsl/ir_basic_block.cpp',
  'src/glsl/ir_builder.cpp',
  'src/glsl/ir_clone.cpp',
  'src/glsl/ir_constant_expression.cpp',
  'src/glsl/ir_equals.cpp',
  'src/glsl/ir_expression_flattening.cpp',
  'src/glsl/ir_function.cpp',
  'src/glsl/ir_function_can_inline.cpp',
  'src/glsl/ir_function_detect_recursion.cpp',
  'src/glsl/ir_hierarchical_visitor.cpp',
  'src/glsl/ir_hv_accept.cpp',
  'src/glsl/ir_import_prototypes.cpp',
  'src/glsl/ir_print_glsl_visitor.cpp',
  'src/glsl/ir_print_metal_visitor.cpp',
  'src/glsl/ir_print_visitor.cpp',
  'src/glsl/ir_rvalue_visitor.cpp',
  'src/glsl/ir_stats.cpp',
  'src/glsl/ir_unused_structs.cpp',
  'src/glsl/ir_validate.cpp',
  'src/glsl/ir_variable_refcount.cpp',
  'src/glsl/link_atomics.cpp',
  'src/glsl/link_functions.cpp',
  'src/glsl/link_interface_blocks.cpp',
  'src/glsl/link_uniform_block_active_visitor.cpp',
  'src/glsl/link_uniform_blocks.cpp',
  'src/glsl/link_uniform_initializers.cpp',
  'src/glsl/link_uniforms.cpp',
  'src/glsl/link_varyings.cpp',
  'src/glsl/linker.cpp',
  'src/glsl/loop_analysis.cpp',
  'src/glsl/loop_controls.cpp',
  'src/glsl/loop_unroll.cpp',
  'src/glsl/lower_clip_distance.cpp',
  'src/glsl/lower_discard.cpp',
  'src/glsl/lower_discard_flow.cpp',
  'src/glsl/lower_if_to_cond_assign.cpp',
  'src/glsl/lower_instructions.cpp',
  'src/glsl/lower_jumps.cpp',
  'src/glsl/lower_mat_op_to_vec.cpp',
  'src/glsl/lower_named_interface_blocks.cpp',
  'src/glsl/lower_noise.cpp',
  'src/glsl/lower_offset_array.cpp',
  'src/glsl/lower_output_reads.cpp',
  'src/glsl/lower_packed_varyings.cpp',
  'src/glsl/lower_packing_builtins.cpp',
  'src/glsl/lower_ubo_reference.cpp',
  'src/glsl/lower_variable_index_to_cond_assign.cpp',
  'src/glsl/lower_vec_index_to_cond_assign.cpp',
  'src/glsl/lower_vec_index_to_swizzle.cpp',
  'src/glsl/lower_vector.cpp',
  'src/glsl/lower_vector_insert.cpp',
  'src/glsl/lower_vertex_id.cpp',
  'src/glsl/opt_algebraic.cpp',
  'src/glsl/opt_array_splitting.cpp',
  'src/glsl/opt_constant_folding.cpp',
  'src/glsl/opt_constant_propagation.cpp',
  'src/glsl/opt_constant_variable.cpp',
  'src/glsl/opt_copy_propagation.cpp',
  'src/glsl/opt_copy_propagation_elements.cpp',
  'src/glsl/opt_cse.cpp',
  'src/glsl/opt_dead_builtin_variables.cpp',
  'src/glsl/opt_dead_builtin_varyings.cpp',
  'src/glsl/opt_dead_code.cpp',
  'src/glsl/opt_dead_code_local.cpp',
  'src/glsl/opt_dead_functions.cpp',
  'src/glsl/opt_flatten_nested_if_blocks.cpp',
  'src/glsl/opt_flip_matrices.cpp',
  'src/glsl/opt_function_inlining.cpp',
  'src/glsl/opt_if_simplification.cpp',
  'src/glsl/opt_minmax.cpp',
  'src/glsl/opt_noop_swizzle.cpp',
  'src/glsl/opt_rebalance_tree.cpp',
  'src/glsl/opt_redundant_jumps.cpp',
  'src/glsl/opt_structure_splitting.cpp',
  'src/glsl/opt_swizzle_swizzle.cpp',
  'src/glsl/opt_tree_grafting.cpp',
  'src/glsl/opt_vectorize.cpp',
  'src/glsl/s_expression.cpp',
  'src/glsl/standalone_scaffolding.cpp',
  'src/glsl/strtod.c',
  # src/mesa/
  'src/mesa/main/imports.c',
  'src/mesa/program/prog_hash_table.c',
  'src/mesa/program/symbol_table.c',
  # src/util/
  'src/util/hash_table.c',
  'src/util/ralloc.c',
)

glsl_optimizer_args = []
glsl_optimizer_c_args = []

_cpp = meson.get_compiler('cpp')
if _cpp.get_id() == 'msvc'
  glsl_optimizer_args += [
    '/wd4100', '/wd4127', '/wd4132', '/wd4189',
    '/wd4204', '/wd4244', '/wd4245', '/wd4389',
    '/wd4701', '/wd4702', '/wd4706', '/wd4996',
  ]
  glsl_optimizer_c_args += glsl_optimizer_args
else
  glsl_optimizer_args += [
    '-fno-strict-aliasing',
    '-Wno-implicit-fallthrough',
    '-Wno-parentheses',
    '-Wno-sign-compare',
    '-Wno-unused-function',
    '-Wno-unused-parameter',
  ]
  glsl_optimizer_c_args += [
    '-Wno-implicit-fallthrough',
    '-Wno-parentheses',
    '-Wno-sign-compare',
    '-Wno-unused-function',
    '-Wno-unused-parameter',
  ]
  if _cpp.has_argument('-Wno-deprecated-register')
    glsl_optimizer_args += '-Wno-deprecated-register'
  endif
  if _cpp.has_argument('-Wno-misleading-indentation')
    glsl_optimizer_args += '-Wno-misleading-indentation'
  endif
endif

glsl_optimizer_lib = static_library('glsl-optimizer', glsl_optimizer_sources,
  c_args: glsl_optimizer_c_args,
  cpp_args: glsl_optimizer_args,
  include_directories: [
    include_directories('include'),
    include_directories('src/glsl'),
    include_directories('src'),
    include_directories('src/mesa'),
  ],
  override_options: ['cpp_std=c++17'],
)

glsl_optimizer_dep = declare_dependency(
  link_with: glsl_optimizer_lib,
  include_directories: [
    include_directories('include'),
    include_directories('src/glsl'),
  ],
)
