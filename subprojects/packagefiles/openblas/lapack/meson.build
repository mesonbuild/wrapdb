# TODO: This is all specialized for Fortran LAPACK only for now
add_languages('fortran', native: false)
lapack_deps = [ fc.find_library('quadmath', required: true) ]

lapack_args = []
# Recall from the LAPACK Users Guide 1990 that:
# XYYZZZ
# X -> S (real) | D (double) | C (complex) | Z (double complex)
# YY -> Matrix type
# ZZZ -> computation
#
# We only need to build the following matrix types for OpenBLAS
# GE (general, unsymmetric)
# LA (auxiliary)
# PO (symmetric or Hermitian positive definite)
# TR (triangular or quasi-triangular in some cases)
#
# Along with the following computations:
# TRF (factorize)
# TRS (solve Ax=b by forward / backward substitution)
# SWP (swap rows)
# UUM (product L^HL or UU^H, unblocked)
# UU2 (product L^HL or UU^H, blocked)
# TF2 (Cholesky, unblocked)
# TI2 (triangular matrix inverse, unblocked)
# TRI (inverse)
#
# Note that 2 implies the unblocked version
#
# Specifically we have:
#
# getf2:  GEneral matrix Factorization (unblocked)
# getrf:  GEneral matrix Factorization (blocked)
# getrs:  GEneral matrix solve (using factored matrix)
# laswp:  LA auxiliary routine for swapping rows
# lauu2:  LA auxiliary routine for unblocked matrix factorization
# lauum:  LA auxiliary routine for blocked matrix factorization
# potf2:  POsitive definite matrix factorization (unblocked)
# potrf:  POsitive definite matrix factorization (blocked)
# trti2:  TRiangular matrix Inversion (unblocked)
# trtri:  TRiangular matrix Inversion (blocked)
# trtrs:  TRiangular matrix solve
_lapack_roots = [
    {
        'base': '?getf2_k',
        '_types': ['s', 'd', 'q'],
        'fdir': 'getf2',
        'fname': 'getf2_k.c',
    },
    {
        'base': '?getf2_k',
        '_types': ['c', 'z', 'x'],
        'fdir': 'getf2',
        'fname': 'zgetf2_k.c',
    },
    {
        'base': '?getrf_single',
        '_types': ['s', 'd', 'q', 'c', 'z', 'x'],
        'fdir': 'getrf',
        'fname': 'getrf_single.c',
        'def': ['UNIT'],
    },
    {
        'base': '?getrf_parallel',
        '_types': ['s', 'd', 'q', 'c', 'z', 'x'],
        'fdir': 'getrf',
        'fname': 'getrf_parallel.c',
        'def': ['UNIT'],
        'addl_srcs': ['../param.h'],
    },
    {
        'base': '?getrs_*_single',
        '_types': ['s', 'd', 'q'],
        '_meth': {'N': ['-UTRANS'], 'T': ['-DTRANS']},
        'fdir': 'getrs',
        'fname': 'getrs_single.c',
    },
    {
        'base': '?getrs_*_single',
        '_types': ['c', 'z', 'x'],
        '_meth': {
            'N': ['-DTRANS=1'],
            'T': ['-DTRANS=2'],
            'R': ['-DTRANS=3'],
            'C': ['-DTRANS=4'],
        },
        'fdir': 'getrs',
        'fname': 'zgetrs_single.c',
    },
    {
        'base': '?getrs_*_parallel',
        '_types': ['s', 'd', 'q'],
        '_meth': {'N': ['-UTRANS'], 'T': ['-DTRANS']},
        'fdir': 'getrs',
        'fname': 'getrs_parallel.c',
        # 'onlyif': ['SMP']
    },
    {
        'base': '?getrs_*_parallel',
        '_types': ['c', 'z', 'x'],
        '_meth': {
            'N': ['-DTRANS=1'],
            'T': ['-DTRANS=2'],
            'R': ['-DTRANS=3'],
            'C': ['-DTRANS=4'],
        },
        'fdir': 'getrs',
        'fname': 'zgetrs_parallel.c',
        # 'onlyif': ['SMP']
    },
    {
        'base': '?trti2_*',
        '_types': ['s', 'd', 'q'],
        '_meth': {'UU': ['-DUNIT'], 'UN': ['-UUNIT']},
        'fdir': 'trti2',
        'fname': 'trti2_U.c',
    },
    {
        'base': '?trti2_*',
        '_types': ['s', 'd', 'q'],
        '_meth': {'LU': ['-DUNIT'], 'LN': ['-UUNIT']},
        'fdir': 'trti2',
        'fname': 'trti2_L.c',
    },
    {
        'base': '?trti2_*',
        '_types': ['c', 'z', 'x'],
        '_meth': {'UU': ['-DUNIT'], 'UN': ['-UUNIT']},
        'fdir': 'trti2',
        'fname': 'ztrti2_U.c',
    },
    {
        'base': '?trti2_*',
        '_types': ['c', 'z', 'x'],
        '_meth': {'LU': ['-DUNIT'], 'LN': ['-UUNIT']},
        'fdir': 'trti2',
        'fname': 'ztrti2_L.c',
    },
    {
        'base': '?trtri_*_single',
        '_types': ['s', 'd', 'q', 'c', 'z', 'x'],
        '_meth': {'UU': ['-DUNIT'], 'UN': ['-UUNIT']},
        'fdir': 'trtri',
        'fname': 'trtri_U_single.c',
    },
    {
        'base': '?trtri_*_single',
        '_types': ['s', 'd', 'q', 'c', 'z', 'x'],
        '_meth': {'LU': ['-DUNIT'], 'LN': ['-UUNIT']},
        'fdir': 'trtri',
        'fname': 'trtri_L_single.c',
    },
    {
        'base': '?trtri_*_parallel',
        '_types': ['s', 'd', 'q', 'c', 'z', 'x'],
        '_meth': {'UU': ['-DUNIT'], 'UN': ['-UUNIT']},
        'fdir': 'trtri',
        'fname': 'trtri_U_parallel.c',
    },
    {
        'base': '?trtri_*_parallel',
        '_types': ['s', 'd', 'q', 'c', 'z', 'x'],
        '_meth': {'LU': ['-DUNIT'], 'LN': ['-UUNIT']},
        'fdir': 'trtri',
        'fname': 'trtri_L_parallel.c',
    },
    {
        'base': '?trtrs_*_single',
        '_types': ['s', 'd', 'q'],
        '_meth': {
            'UNU': ['-UUPLO', '-UTRANS', '-UDIAG'],
            'UNN': ['-UUPLO', '-UTRANS', '-DDIAG'],
            'UTU': ['-UUPLO', '-DTRANS', '-UDIAG'],
            'UTN': ['-UUPLO', '-DTRANS', '-DDIAG'],
            'LNU': ['-DUPLO', '-UTRANS', '-UDIAG'],
            'LNN': ['-DUPLO', '-UTRANS', '-DDIAG'],
            'LTU': ['-DUPLO', '-DTRANS', '-UDIAG'],
            'LTN': ['-DUPLO', '-DTRANS', '-DDIAG'],
        },
        'fdir': 'trtrs',
        'fname': 'trtrs_single.c',
    },
    {
        'base': '?trtrs_*_single',
        '_types': ['c', 'z', 'x'],
        '_meth': {
            'UNU': ['-UUPLO', '-DTRANS=1', '-UDIAG'],
            'UNN': ['-UUPLO', '-DTRANS=1', '-DDIAG'],
            'UTU': ['-UUPLO', '-DTRANS=2', '-UDIAG'],
            'UTN': ['-UUPLO', '-DTRANS=2', '-DDIAG'],
            'URU': ['-UUPLO', '-DTRANS=3', '-UDIAG'],
            'URN': ['-UUPLO', '-DTRANS=3', '-DDIAG'],
            'UCU': ['-UUPLO', '-DTRANS=4', '-UDIAG'],
            'UCN': ['-UUPLO', '-DTRANS=4', '-DDIAG'],
            'LNU': ['-DUPLO', '-DTRANS=1', '-UDIAG'],
            'LNN': ['-DUPLO', '-DTRANS=1', '-DDIAG'],
            'LTU': ['-DUPLO', '-DTRANS=2', '-UDIAG'],
            'LTN': ['-DUPLO', '-DTRANS=2', '-DDIAG'],
            'LRU': ['-DUPLO', '-DTRANS=3', '-UDIAG'],
            'LRN': ['-DUPLO', '-DTRANS=3', '-DDIAG'],
            'LCU': ['-DUPLO', '-DTRANS=4', '-UDIAG'],
            'LCN': ['-DUPLO', '-DTRANS=4', '-DDIAG'],
        },
        'fdir': 'trtrs',
        'fname': 'ztrtrs_single.c',
    },
    {
        'base': '?trtrs_*_parallel',
        '_types': ['s', 'd', 'q'],
        '_meth': {
            'UNU': ['-UUPLO', '-UTRANS', '-UDIAG'],
            'UNN': ['-UUPLO', '-UTRANS', '-DDIAG'],
            'UTU': ['-UUPLO', '-DTRANS', '-UDIAG'],
            'UTN': ['-UUPLO', '-DTRANS', '-DDIAG'],
            'LNU': ['-DUPLO', '-UTRANS', '-UDIAG'],
            'LNN': ['-DUPLO', '-UTRANS', '-DDIAG'],
            'LTU': ['-DUPLO', '-DTRANS', '-UDIAG'],
            'LTN': ['-DUPLO', '-DTRANS', '-DDIAG'],
        },
        'fdir': 'trtrs',
        'fname': 'trtrs_parallel.c',
    },
    {
        'base': '?trtrs_*_parallel',
        '_types': ['c', 'z', 'x'],
        '_meth': {
            'UNU': ['-UUPLO', '-DTRANS=1', '-UDIAG'],
            'UNN': ['-UUPLO', '-DTRANS=1', '-DDIAG'],
            'UTU': ['-UUPLO', '-DTRANS=2', '-UDIAG'],
            'UTN': ['-UUPLO', '-DTRANS=2', '-DDIAG'],
            'URU': ['-UUPLO', '-DTRANS=3', '-UDIAG'],
            'URN': ['-UUPLO', '-DTRANS=3', '-DDIAG'],
            'UCU': ['-UUPLO', '-DTRANS=4', '-UDIAG'],
            'UCN': ['-UUPLO', '-DTRANS=4', '-DDIAG'],
            'LNU': ['-DUPLO', '-DTRANS=1', '-UDIAG'],
            'LNN': ['-DUPLO', '-DTRANS=1', '-DDIAG'],
            'LTU': ['-DUPLO', '-DTRANS=2', '-UDIAG'],
            'LTN': ['-DUPLO', '-DTRANS=2', '-DDIAG'],
            'LRU': ['-DUPLO', '-DTRANS=3', '-UDIAG'],
            'LRN': ['-DUPLO', '-DTRANS=3', '-DDIAG'],
            'LCU': ['-DUPLO', '-DTRANS=4', '-UDIAG'],
            'LCN': ['-DUPLO', '-DTRANS=4', '-DDIAG'],
        },
        'fdir': 'trtrs',
        'fname': 'ztrtrs_parallel.c',
    },
]

foreach base_name : ['lauu2', 'potf2']
    foreach uplo : ['U', 'L']
        # Real types
        _lapack_roots += {
            'base': f'?@base_name@_@uplo@',
            '_types': ['s', 'd', 'q'],
            'fdir': base_name,
            'fname': f'@base_name@_@uplo@.c',
        }

        # Complex types
        _lapack_roots += {
            'base': f'?@base_name@_@uplo@',
            '_types': ['c', 'z', 'x'],
            'fdir': base_name,
            'fname': f'z@base_name@_@uplo@.c',
        }
    endforeach
endforeach

foreach base_name : ['lauum', 'potrf']
    foreach par : ['parallel', 'single']
        foreach uplo : ['U', 'L']
            _lapack_roots += {
                'base': f'?@base_name@_@uplo@_@par@',
                '_types': ['s', 'd', 'q', 'c', 'z', 'x'],
                'fdir': base_name,
                'fname': f'@base_name@_@uplo@_@par@.c',
            }
        endforeach
    endforeach
endforeach

# CPU dispatch in the folder
subdir('laswp/generic')

# Handle netlib fill-in, i.e. adding all the symbols without optimized variants

lapack_base_netlib = [
    # This is basically _install_aux
    {'base': 'ilaver', '_t': [''], 'froot': 'INSTALL'}, # needed here
    # {'base': 'lsame', '_t': [''], 'froot': 'INSTALL'}, # Part of openblas anyway
    {'base': '?lamch', '_t': ['s', 'd'], 'froot': 'INSTALL'},
    {'base': '?roundup_lwork', '_t': ['s', 'd'], 'froot': 'INSTALL'},
    {'base': '?secnd_INT_CPU_TIME', '_t': ['d'], 'froot': 'INSTALL'},
    # This is basically _auxlapack from lapack-netlib/SRC
    {'base': 'ilaenv2stage', '_t': [''], 'froot': 'SRC'},
    {'base': 'ieeeck', '_t': [''], 'froot': 'SRC'},
    {'base': 'lsamen', '_t': [''], 'froot': 'SRC'},
    {'base': 'iparmq', '_t': [''], 'froot': 'SRC'},
    {'base': 'iparam2stage', '_t': [''], 'froot': 'SRC', 'ext': '.F'},
    {'base': 'ilaprec', '_t': [''], 'froot': 'SRC'},
    {'base': 'ilatrans', '_t': [''], 'froot': 'SRC'},
    {'base': 'ilauplo', '_t': [''], 'froot': 'SRC'},
    {'base': 'iladiag', '_t': [''], 'froot': 'SRC'},
    {'base': 'chla_transtype', '_t': [''], 'froot': 'SRC'},
    {'base': 'la_xisnan', '_t': [''], 'froot': 'SRC', 'ext': '.F90'},
    {'base': 'la_constants', '_t': [''], 'froot': 'SRC', 'ext': '.f90'},
    {'base': 'xerbla_array', '_t': [''], 'froot': 'SRC'},
]

_allaux = []
foreach simple_def : lapack_base_netlib
  base_pattern = simple_def['base']
  _tlist = simple_def['_t']
  _fdir = '../lapack-netlib/' + simple_def['froot']

    if simple_def.has_key('ext')
      fname = sym_name + simple_def['ext']
    else
      fname = sym_name + '.f'
    endif

  foreach _type : _tlist
    # Construct the specific filename (e.g., sgebal.c, dgebal.c, etc.)
    sym_name = base_pattern.replace('?', _type)
    if simple_def.has_key('ext')
      fname = sym_name + simple_def['ext']
    else
      fname = sym_name + '.f'
    endif
    _allaux += f'@_fdir@/@fname@'
  endforeach

endforeach

# _auxlapack -- Auxiliary routines for lapack
_auxlapack = static_library('_auxlapack',
                     sources: _allaux,
                    )

lapack_netlib_roots = [
    {'base': '?combssq', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?bdsvdx', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?stevx', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?bdsdc', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?isnan', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?disna', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?labad', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lacpy', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ladiv', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lae2', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?laebz', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?laed0', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laed1', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?laed2', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?laed3', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?laed4', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?laed5', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?laed6', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?laed7', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laed8', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laed9', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?laeda', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?laev2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lagtf', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lagts', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lamrg', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lanst', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lapy2', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lapy3', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?larnv', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?larra', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?larrb', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?larrc', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?larrd', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?larre', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?larrf', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?larrj', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?larrk', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?larrr', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?laneg', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lartg', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC', 'ext': '.f90'},
    {'base': '?laruv', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?las2', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lascl', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lasd0', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lasd1', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lasd2', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lasd3', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lasd4', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lasd5', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lasd6', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lasd7', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lasd8', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lasda', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lasdq', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lasdt', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?laset', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lasq1', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lasq2', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lasq3', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lasq4', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lasq5', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lasq6', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lasr', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lasrt', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lassq', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC', 'ext': '.f90'},
    {'base': '?lasv2', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?pttrf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?stebz', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?stedc', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?steqr', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sterf', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?stein', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laisnan', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lartgp', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lartgs', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?larmm', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?gbbrd', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gbcon', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gbequ', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gbrfs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gbsv', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gbsvx', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gbtf2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gbtrf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gbtrs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gebak', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gebal', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gebd2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gebrd', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gecon', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?geequ', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gees', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?geesx', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?geev', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?geevx', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gehd2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gehrd', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gelq2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gelqf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gels', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gelsd', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gelss', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gelsy', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?geql2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?geqlf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?geqp3', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?geqp3rk', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?geqr2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?geqr2p', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?geqrf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?geqrfp', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gerfs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gerq2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gerqf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gesc2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gesdd', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gesvd', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gesvdx', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?getc2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?getrf2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?getri', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ggbak', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ggbal', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gges', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gges3', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ggesx', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ggev', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ggev3', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ggevx', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ggglm', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gghrd', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gghd3', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gglse', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ggqrf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ggrqf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ggsvd3', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ggsvp3', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gtcon', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gtrfs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gtsv', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gtsvx', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gttrf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gttrs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gtts2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?hgeqz', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqz0', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqz1', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqz2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqz3', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqz4', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?hsein', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?hseqr', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?labrd', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lacon', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lacn2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laein', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laexc', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lag2', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lags2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lagtm', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lagv2', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lahqr', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laic1', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laln2', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lals0', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lalsa', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lalsd', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?langb', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lange', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?langt', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lanhs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lansb', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lansp', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lansy', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lantb', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lantp', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lanv2', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lapll', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lapmt', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqgb', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqge', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqp2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqp2rk', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqp3rk', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqps', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqsb', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqsp', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqsy', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqr0', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqr1', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqr2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqr3', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqr4', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqr5', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laqtr', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lar1v', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lar2v', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?larfb_gett', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?larfgp', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?larft', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?larfx', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?larfy', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?largv', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?larrv', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lartv', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?larz', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?larzb', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?larzt', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lasy2', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?lasyf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lasyf_rook', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lasyf_rk', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lasyf_aa', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?latbs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?latdf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?latps', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?latrd', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?latrs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?latrz', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?opgtr', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?opmtr', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?org2l', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?org2r', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orgbr', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orghr', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orgl2', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orglq', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orgql', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orgqr', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orgr2', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orgrq', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orgtr', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orm2l', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orm2r', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orm22', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?ormbr', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?ormhr', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orml2', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?ormlq', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?ormql', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?ormqr', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?ormr2', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?ormr3', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?ormrq', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?ormrz', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?ormtr', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?pbcon', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?pbequ', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?pbrfs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?pbstf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?pbsv', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?pbsvx', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?pbtf2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?pbtrf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?pbtrs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?pocon', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?poequ', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?porfs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?posv', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?posvx', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?potrf2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?potrs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?potri', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?pstrf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?pstf2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ppcon', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ppequ', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?pprfs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ppsv', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ppsvx', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?pptrf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?pptri', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?pptrs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ptcon', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?pteqr', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ptrfs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ptsv', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ptsvx', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?pttrs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?ptts2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?rscl', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sbev', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?sbevd', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?sbevx', '_t': ['s', 'd'], 'froot': 'SRC'},

    {'base': '?sbgst', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?sbgv', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?sbgvd', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?sbgvx', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?sbtrd', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?spcon', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?spev', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?spevd', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?spevx', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?spgst', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?spgv', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?spgvd', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?spgvx', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?sprfs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?spsv', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?spsvx', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sptrd', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?sptrf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sptri', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sptrs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?stegr', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?stev', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?stevd', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?stevr', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?sycon', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?syev', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?syevd', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?syevr', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?syevx', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?sygs2', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?sygst', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?sygv', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?sygvd', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?sygvx', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?syrfs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sysv', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sysvx', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytd2', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?sytf2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytrd', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?sytrf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytri', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytri2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytri2x', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?syswapr', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytrs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytrs2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?syconv', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?syconvf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?syconvf_rook', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sysv_aa', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sysv_aa_2stage', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytrf_aa', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytrf_aa_2stage', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytrs_aa', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytrs_aa_2stage', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytf2_rook', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytrf_rook', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytrs_rook', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytri_rook', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sycon_rook', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sysv_rook', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytf2_rk', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytrf_rk', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytrs_3', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytri_3', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytri_3x', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sycon_3', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sysv_rk', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tbcon', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tbrfs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tbtrs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tgevc', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tgex2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tgexc', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tgsen', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tgsja', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tgsna', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tgsy2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tgsyl', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tpcon', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tprfs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tptri', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tptrs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?trcon', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?trevc', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?trevc3', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?trexc', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?trrfs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?trsen', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?trsna', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?trsyl', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    # {'base': '?trtrs', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?tzrzf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?stemr', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lansf', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?pftrf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?pftri', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?pftrs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sfrk', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?tfsm', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tftri', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tfttp', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tfttr', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tpttf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tpttr', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?trttf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?trttp', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gejsv', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gesvj', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gsvj0', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gsvj1', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?geequb', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?syequb', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?poequb', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gbequb', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?bbcsd', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lapmr', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?orbdb', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orbdb1', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orbdb2', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orbdb3', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orbdb4', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orbdb5', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orbdb6', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orcsd', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orcsd2by1', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?geqrt', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?geqrt2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?geqrt3', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gemqrt', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tpqrt', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tpqrt2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tpmqrt', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tprfb', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gelqt', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gelqt3', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gemlqt', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?getsls', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?getsqrhrt', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?geqr', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?latsqr', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lamtsqr', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gemqr', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gelq', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laswlq', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lamswlq', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gemlq', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tplqt', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tplqt2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?tpmlqt', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?sytrd_2stage', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?sytrd_sy2sb', '_t': ['s', 'd'], 'froot': 'SRC', 'ext': '.f'},
    {'base': '?sytrd_sb2st', '_t': ['s', 'd'], 'froot': 'SRC', 'ext': '.F'},
    {'base': '?sb2st_kernels', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?hb2st_kernels', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?syevd_2stage', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?syev_2stage', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?syevx_2stage', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?syevr_2stage', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?sbev_2stage', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?hbev_2stage', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?sbevx_2stage', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?hbevx_2stage', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?sbevd_2stage', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?hbevd_2stage', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?sygv_2stage', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?gesvdq', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?laorhr_col_getrfnp', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?laorhr_col_getrfnp2', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orgtsqr', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orgtsqr_row', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?orhr_col', '_t': ['s', 'd'], 'froot': 'SRC'},
    {'base': '?latrs3', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?trsyl3', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gelst', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gedmd', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC', 'ext': '.f90'},
    {'base': '?gedmdq', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC', 'ext': '.f90'},
    {'base': '?trtri', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    # {'base': '?gesvxx', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?gerfsx', '_t': ['s', 'd'], 'froot': 'SRC'},
    # # {'base': '?la_gerfsx_extended', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?la_geamv', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?la_gercond', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?la_gerpvgrw', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?sysvxx', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?syrfsx', '_t': ['s', 'd'], 'froot': 'SRC'},
    # # {'base': '?la_syrfsx_extended', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?la_syamv', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?la_syrcond', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?la_syrpvgrw', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?posvxx', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?porfsx', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?la_porfsx_extended', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?la_porcond', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?la_porpvgrw', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?gbsvxx', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?gbrfsx', '_t': ['s', 'd'], 'froot': 'SRC'},
    # # {'base': '?la_gbrfsx_extended', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?la_gbamv', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?la_gbrcond', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?la_gbrpvgrw', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?la_lin_berr', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?larscl2', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?lascl2', '_t': ['s', 'd'], 'froot': 'SRC'},
    # {'base': '?la_wwaddw', '_t': ['s', 'd'], 'froot': 'SRC'},

    {'base': '?bdsqr', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?gesvx', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lantr', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?lahr2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?larf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?larfb', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': '?larfg', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': 'ila?lc', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},
    {'base': 'ila?lr', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC'},

    {'base': '?srscl', '_t': ['c'], 'froot': 'SRC'},
    {'base': '?hpevx', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hbevd', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hbevx', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hbgst', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hbev', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hbgv', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hbgvd', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hbgvx', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hbtrd', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hpgv', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hptrs', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hptrf', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hpgvd', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hpgvx', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hprfs', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hpsv', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hpsvx', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hfrk', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hpcon', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hpev', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hpevd', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hpgst', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?heev', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?heevd', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?heevr', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?heevx', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?heequb', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hegv', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hegvd', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hegvx', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?herfs', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hegs2', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hegst', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hptrd', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetd2', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetrs', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetf2', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetrd', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetrf', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetri', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetri2', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetri2x', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?heswapr', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetrs2', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hecon', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hesv', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hesvx', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hptri', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?lanhe', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?laqhe', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?lanhf', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?laqhb', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?lanhp', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?larcm', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?lacrm', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?lacp2', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?laqhp', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?lahef', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?lahef_aa', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?lahef_rk', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?lahef_rook', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?lacrt', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?lacgv', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?laesy', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unmqr', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?ung2r', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unmrq', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unmhr', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unmrz', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unmbr', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?rot', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?lanhb', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?lanht', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unhr_col', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?ungtsqr_row', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?ungtsqr', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unglq', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unmlq', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unml2', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unm2r', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unmr2', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unmr3', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unm22', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unghr', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?ungqr', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?ungbr', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unmtr', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?ungtr', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?ungl2', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?ung2l', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?ungql', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unmql', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unm2l', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?uncsd', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unbdb', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unbdb1', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unbdb2', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unbdb3', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unbdb4', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unbdb5', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?unbdb6', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?uncsd2by1', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?ungrq', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?ungr2', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?upgtr', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?upmtr', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hecon_3', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hecon_rook', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?heev_2stage', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?heevd_2stage', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?heevr_2stage', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?heevx_2stage', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hegv_2stage', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hesv_aa', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hesv_aa_2stage', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hesv_rk', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hesv_rook', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetf2_rk', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetf2_rook', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetrd_2stage', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetrd_hb2st', '_t': ['c', 'z'], 'froot': 'SRC', 'ext': '.F'},
    {'base': '?hetrd_he2hb', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetrf_aa', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetrf_aa_2stage', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetrf_rk', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetrf_rook', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetri_3', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetri_3x', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetri_rook', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetrs_3', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetrs_aa', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetrs_aa_2stage', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?hetrs_rook', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?launhr_col_getrfnp', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?launhr_col_getrfnp2', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': 'i?max1', '_t': ['c', 'z'], 'froot': 'SRC'},
    {'base': '?drscl', '_t': ['z'], 'froot': 'SRC'},

    {'base': 'dsgesv', '_t': [''], 'froot': 'SRC'},
    {'base': 'zcgesv', '_t': [''], 'froot': 'SRC'},
    {'base': 'dsposv', '_t': [''], 'froot': 'SRC'},
    {'base': 'clag2z', '_t': [''], 'froot': 'SRC'},
    {'base': 'slag2d', '_t': [''], 'froot': 'SRC'},
    {'base': 'dlat2s', '_t': [''], 'froot': 'SRC'},
    {'base': 'dlag2s', '_t': [''], 'froot': 'SRC'},
    {'base': 'zlag2c', '_t': [''], 'froot': 'SRC'},
    {'base': 'zlat2c', '_t': [''], 'froot': 'SRC'},
    {'base': 'zcposv', '_t': [''], 'froot': 'SRC'},
    {'base': 'scsum1', '_t': [''], 'froot': 'SRC'},
    {'base': 'dzsum1', '_t': [''], 'froot': 'SRC'},
    {'base': 'ilaenv', '_t': [''], 'froot': 'SRC'},

    # Deprecated symbols (still built by Makefile:545, lapack.cmake:439)
    {'base': '?gegs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC/DEPRECATED'},
    {'base': '?gegv', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC/DEPRECATED'},
    {'base': '?gelsx', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC/DEPRECATED'},
    {'base': '?geqpf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC/DEPRECATED'},
    {'base': '?ggsvd', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC/DEPRECATED'},
    {'base': '?ggsvp', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC/DEPRECATED'},
    {'base': '?lahrd', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC/DEPRECATED'},
    {'base': '?latzm', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC/DEPRECATED'},
    {'base': '?tzrqf', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC/DEPRECATED'},
    {'base': '?gelqs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC/DEPRECATED'},
    {'base': '?geqrs', '_t': ['s', 'd', 'c', 'z'], 'froot': 'SRC/DEPRECATED'},

    # *CATGEN
    # TODO(HaoZeke): Only build on request..
    {'base': '?latm1', '_t': ['s', 'd', 'c', 'z'], 'froot': 'TESTING/MATGEN'},
    {'base': '?laran', '_t': ['s', 'd'], 'froot': 'TESTING/MATGEN'},
    {'base': '?larnd', '_t': ['s', 'd', 'c', 'z'], 'froot': 'TESTING/MATGEN'},
    # *MATGEN
    {'base': '?latms', '_t': ['s', 'd', 'c', 'z'], 'froot': 'TESTING/MATGEN'},
    {'base': '?latme', '_t': ['s', 'd', 'c', 'z'], 'froot': 'TESTING/MATGEN'},
    {'base': '?latmr', '_t': ['s', 'd', 'c', 'z'], 'froot': 'TESTING/MATGEN'},
    {'base': '?latmt', '_t': ['s', 'd', 'c', 'z'], 'froot': 'TESTING/MATGEN'},
    {'base': '?lagge', '_t': ['s', 'd', 'c', 'z'], 'froot': 'TESTING/MATGEN'},
    {'base': '?lagsy', '_t': ['s', 'd', 'c', 'z'], 'froot': 'TESTING/MATGEN'},
    {'base': '?lakf2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'TESTING/MATGEN'},
    {'base': '?large', '_t': ['s', 'd', 'c', 'z'], 'froot': 'TESTING/MATGEN'},
    {'base': '?laror', '_t': ['s', 'd', 'c', 'z'], 'froot': 'TESTING/MATGEN'},
    {'base': '?larot', '_t': ['s', 'd', 'c', 'z'], 'froot': 'TESTING/MATGEN'},
    {'base': '?latm2', '_t': ['s', 'd', 'c', 'z'], 'froot': 'TESTING/MATGEN'},
    {'base': '?latm3', '_t': ['s', 'd', 'c', 'z'], 'froot': 'TESTING/MATGEN'},
    {'base': '?latm5', '_t': ['s', 'd', 'c', 'z'], 'froot': 'TESTING/MATGEN'},
    {'base': '?latm6', '_t': ['s', 'd', 'c', 'z'], 'froot': 'TESTING/MATGEN'},
    {'base': '?latm7', '_t': ['s', 'd'], 'froot': 'TESTING/MATGEN'},
    {'base': '?lahilb', '_t': ['s', 'd', 'c', 'z'], 'froot': 'TESTING/MATGEN'},
    {'base': '?laghe', '_t': ['c', 'z'], 'froot': 'TESTING/MATGEN'},

    # {'base': 'dlaset', '_t': [''], 'froot': 'SRC'},
    # {'base': 'lapacke_ctrtri', '_t': [''], 'froot': 'LAPACKE/src'},
    # {'base': 'lapacke_nancheck', '_t': [''], 'froot': 'LAPACKE/src'},
    # {'base': 'lapacke_xerbla', '_t': [''], 'froot': 'LAPACKE/utils'},
]

foreach simple_def : lapack_netlib_roots
  base_pattern = simple_def['base']
  _tlist = simple_def['_t']
  _fdir = '../lapack-netlib/' + simple_def['froot']

  # Loop through each LAPACK type (s, d, c, z)
  foreach _type : _tlist
    # Construct the specific filename (e.g., sgebal.c, dgebal.c, etc.)
    sym_name = base_pattern.replace('?', _type)
    if simple_def.has_key('ext')
      fname = sym_name + simple_def['ext']
    else
      fname = sym_name + '.f'
    endif

    _lapack_roots += {
      'base': base_pattern,
      '_types': [_type],
      'fdir': _fdir,
      'fname': fname
    }
  endforeach
endforeach


_lapack_libs = []
foreach conf : _lapack_roots
    foreach type : conf['_types']
        if 'q' in type or 'x' in type
            # TODO: Figure out when to build these
            # These are the XDOUBLE symbols
            continue
        endif
        # Seed with common args
        compiler_args = _cargs + lapack_args
        # Generate the symbol flags
        base = conf['base']
        # Set the type arguments
        if precision_mappings.get(type).has_key('def')
            foreach d : precision_mappings[type]['def']
                compiler_args += ['-D' + d]
            endforeach
        endif
        if precision_mappings.get(type).has_key('undef')
            foreach u : precision_mappings[type]['undef']
                compiler_args += ['-U' + u]
            endforeach
        endif

        if conf.has_key('addl')
            compiler_args += conf['addl']
        endif

        # Construct conditionals
        # If specific to the symbol
        if conf.has_key('def')
            foreach d : conf['def']
                compiler_args += ['-D' + d]
            endforeach
        endif
        if conf.has_key('undef')
            foreach u : conf['undef']
                compiler_args += ['-U' + u]
            endforeach
        endif

        # Make mangled symbols
        # TODO: This might be conditional on other options

        all_srcs = []
        if conf.has_key('fdir') and conf.has_key('fname')
            all_srcs += [conf['fdir'] + '/' + conf['fname']]
            if conf.has_key('addl_srcs')
                all_srcs += conf['addl_srcs']
            endif
        endif
        if conf.has_key('ss')
            all_srcs += conf['ss']
        endif

        if conf.has_key('_meth')
            foreach ckey : conf['_meth'].keys()
                __cargs = conf['_meth'][ckey]
                sym_name = conf['base'].replace('?', type)
                sym_name = sym_name.replace('*', ckey)
                sym_underscored = f'@sym_name@_'
                lib = static_library(
                    sym_name,
                    sources: all_srcs,
                    link_whole: _auxlapack,
                    include_directories: _inc,
                    c_args: compiler_args + [
                        f'-DASMNAME=@asm_name_prefix@@sym_name@',
                        f'-DASMFNAME=@asm_name_prefix@@sym_underscored@',
                        f'-DNAME=@sym_underscored@',
                        f'-DCNAME=@sym_name@',
                        f'-DCHAR_NAME="@sym_underscored@"',
                        f'-DCHAR_CNAME="@sym_name@"',
                    ] + __cargs,
                )
                _lapack_libs += lib
            endforeach
        else
            sym_name = conf['base'].replace('?', type)
            sym_underscored = f'@sym_name@_'
            lib = static_library(
                sym_name,
                sources: all_srcs,
                link_whole: _auxlapack,
                include_directories: _inc,
                c_args: compiler_args + [
                    f'-DASMNAME=@asm_name_prefix@@sym_name@',
                    f'-DASMFNAME=@asm_name_prefix@@sym_underscored@',
                    f'-DNAME=@sym_underscored@',
                    f'-DCNAME=@sym_name@',
                    f'-DCHAR_NAME="@sym_underscored@"',
                    f'-DCHAR_CNAME="@sym_name@"',
                ],
            )
            _lapack_libs += lib
        endif
    endforeach
endforeach

_lapack = static_library('_lapack',
                         link_whole: _lapack_libs)
 # LD_LIBRARY_PATH=$HOME/Git/Github/Python/openblas_buildsys_snips/subrepos/openblas/bbdir/blah-inst/usr/local/lib python dev.py -n test -- -k linprog -x
 # meson install -C bbdir --destdir blah-inst
