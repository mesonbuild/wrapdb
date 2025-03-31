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

_lapack = static_library('_lapack', link_whole: _lapack_libs)
