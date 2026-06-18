basiclu_sources = files([
  'src/basiclu_factorize.c',
  'src/basiclu_solve_dense.c',
  'src/lu_build_factors.c',
  'src/lu_factorize_bump.c',
  'src/lu_initialize.c',
  'src/lu_markowitz.c',
  'src/lu_setup_bump.c',
  'src/lu_solve_sparse.c',
  'src/basiclu_get_factors.c',
  'src/basiclu_solve_for_update.c',
  'src/lu_condest.c',
  'src/lu_file.c',
  'src/lu_internal.c',
  'src/lu_matrix_norm.c',
  'src/lu_singletons.c',
  'src/lu_solve_symbolic.c',
  'src/lu_update.c',
  'src/basiclu_initialize.c',
  'src/basiclu_solve_sparse.c',
  'src/lu_pivot.c',
  'src/lu_solve_dense.c',
  'src/lu_solve_triangular.c',
  'src/basiclu_object.c',
  'src/basiclu_update.c',
  'src/lu_dfs.c',
  'src/lu_garbage_perm.c',
  'src/lu_residual_test.c',
  'src/lu_solve_for_update.c',
])

basiclu_include_directories = [include_directories('include'), hconfig_include_dir]

c_compiler = meson.get_compiler('c')
m_dep = c_compiler.find_library('m', required : false)

libbasiclu = library('basiclu', basiclu_sources,
  dependencies : m_dep,
  include_directories : basiclu_include_directories )



basiclu_dep = declare_dependency(
  link_with : libbasiclu,
  include_directories : basiclu_include_directories
)
