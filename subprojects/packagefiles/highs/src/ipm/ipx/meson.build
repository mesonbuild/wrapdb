ipx_sources = files([
  'src/basiclu_kernel.cc',
  'src/basiclu_wrapper.cc',
  'src/basis.cc',
  'src/conjugate_residuals.cc',
  'src/control.cc',
  'src/crossover.cc',
  'src/diagonal_precond.cc',
  'src/forrest_tomlin.cc',
  'src/guess_basis.cc',
  'src/indexed_vector.cc',
  'src/info.cc',
  'src/ipm.cc',
  'src/ipx_c.cc',
  'src/iterate.cc',
  'src/kkt_solver.cc',
  'src/kkt_solver_basis.cc',
  'src/kkt_solver_diag.cc',
  'src/linear_operator.cc',
  'src/lp_solver.cc',
  'src/lu_factorization.cc',
  'src/lu_update.cc',
  'src/maxvolume.cc',
  'src/model.cc',
  'src/normal_matrix.cc',
  'src/sparse_matrix.cc',
  'src/sparse_utils.cc',
  'src/splitted_normal_matrix.cc',
  'src/starting_basis.cc',
  'src/symbolic_invert.cc',
  'src/timer.cc',
  'src/utils.cc',
])

ipx_include_directories = [include_directories(['include', '../../', '../../../extern']), hconfig_include_dir]

libipx = library('ipx', ipx_sources,
  dependencies : basiclu_dep,
  include_directories : ipx_include_directories )

ipx_dep = declare_dependency(
  link_with : libipx,
  dependencies : basiclu_dep,
  include_directories : ipx_include_directories,
)
