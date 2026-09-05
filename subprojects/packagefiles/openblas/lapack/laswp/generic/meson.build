ssmod = import('sourceset')

laswp_ss = ssmod.source_set()
zlaswp_ss = ssmod.source_set()

laswp_ss.add(
  when: ['ARCH_ALPHA'],
  if_true: files('laswp_k_1.c'),
)
zlaswp_ss.add(
  when: ['ARCH_ALPHA'],
  if_true: files('zlaswp_k_1.c'),
)

laswp_ss.add(
  when: ['ARCH_ARM', 'CORE2'],
  if_true: files('laswp_k_2.c'),
)
zlaswp_ss.add(
  when: ['ARCH_ARM', 'CORE2'],
  if_true: files('zlaswp_k_2.c'),
)

laswp_ss.add(
  when: ['ARCH_ARM', 'OPTERON'],
  if_true: files('laswp_k_1.c'),
)
zlaswp_ss.add(
  when: ['ARCH_ARM', 'OPTERON'],
  if_true: files('zlaswp_k_1.c'),
)

laswp_ss.add(
  when: ['ARCH_ARM', 'PRESCOTT'],
  if_true: files('laswp_k_1.c'),
)
zlaswp_ss.add(
  when: ['ARCH_ARM', 'PRESCOTT'],
  if_true: files('zlaswp_k_1.c'),
)

laswp_ss.add(
  when: ['ARCH_ARM64', 'CORE2'],
  if_true: files('laswp_k_2.c'),
)
zlaswp_ss.add(
  when: ['ARCH_ARM64', 'CORE2'],
  if_true: files('zlaswp_k_2.c'),
)

laswp_ss.add(
  when: ['ARCH_ARM64', 'OPTERON'],
  if_true: files('laswp_k_1.c'),
)
zlaswp_ss.add(
  when: ['ARCH_ARM64', 'OPTERON'],
  if_true: files('zlaswp_k_1.c'),
)

laswp_ss.add(
  when: ['ARCH_ARM64', 'PRESCOTT'],
  if_true: files('laswp_k_1.c'),
)
zlaswp_ss.add(
  when: ['ARCH_ARM64', 'PRESCOTT'],
  if_true: files('zlaswp_k_1.c'),
)

laswp_ss.add(
  when: ['ARCH_MIPS64'],
  if_true: files('laswp_k_1.c'),
)
zlaswp_ss.add(
  when: ['ARCH_MIPS64'],
  if_true: files('zlaswp_k_1.c'),
)

laswp_ss.add(
  when: ['ARCH_POWER'],
  if_true: files('laswp_k_1.c'),
)
zlaswp_ss.add(
  when: ['ARCH_POWER'],
  if_true: files('zlaswp_k_1.c'),
)

laswp_ss.add(
  when: ['ARCH_SPARC'],
  if_true: files('laswp_k_1.c'),
)
zlaswp_ss.add(
  when: ['ARCH_SPARC'],
  if_true: files('zlaswp_k_1.c'),
)

laswp_ss.add(
  when: ['ARCH_X86', 'CORE2'],
  if_true: files('laswp_k_2.c'),
)
zlaswp_ss.add(
  when: ['ARCH_X86', 'CORE2'],
  if_true: files('zlaswp_k_2.c'),
)

laswp_ss.add(
  when: ['ARCH_X86', 'OPTERON'],
  if_true: files('laswp_k_1.c'),
)
zlaswp_ss.add(
  when: ['ARCH_X86', 'OPTERON'],
  if_true: files('zlaswp_k_1.c'),
)

laswp_ss.add(
  when: ['ARCH_X86', 'PRESCOTT'],
  if_true: files('laswp_k_1.c'),
)
zlaswp_ss.add(
  when: ['ARCH_X86', 'PRESCOTT'],
  if_true: files('zlaswp_k_1.c'),
)

laswp_ss.add(
  when: ['ARCH_X86_64', 'CORE2'],
  if_true: files('laswp_k_2.c'),
)
zlaswp_ss.add(
  when: ['ARCH_X86_64', 'CORE2'],
  if_true: files('zlaswp_k_2.c'),
)

laswp_ss.add(
  when: ['ARCH_X86_64', 'OPTERON'],
  if_true: files('laswp_k_1.c'),
)
zlaswp_ss.add(
  when: ['ARCH_X86_64', 'OPTERON'],
  if_true: files('zlaswp_k_1.c'),
)

laswp_ss.add(
  when: ['ARCH_X86_64', 'PRESCOTT'],
  if_true: files('laswp_k_1.c'),
)
zlaswp_ss.add(
  when: ['ARCH_X86_64', 'PRESCOTT'],
  if_true: files('zlaswp_k_1.c'),
)

laswp_ss.add(
  when: ['DYNAMIC_ARCH'],
  if_true: files('laswp_k_4.c'),
)
zlaswp_ss.add(
  when: ['DYNAMIC_ARCH'],
  if_true: files('zlaswp_k_4.c'),
)

# So the targets don't have to be explicitly false
laswap_conf = laswp_ss.apply(
  conf_hdat,
  strict: false,
)
zlaswap_conf = zlaswp_ss.apply(
  conf_hdat,
  strict: false,
)

laswap_srcs = []
if laswap_conf.sources().length() == 1
  laswap_srcs = laswap_conf.sources()
else
  laswap_srcs = files('laswp_k.c')
endif

zlaswap_srcs = []
if zlaswap_conf.sources().length() == 1
  zlaswap_srcs = zlaswap_conf.sources()
else
  zlaswap_srcs = files('zlaswp_k.c')
endif

_lapack_roots += {
  'base': '?laswp_*',
  '_types': ['s', 'd'],
  '_meth': {
    'plus': ['-UMINUS'],
    'minus': ['-DMINUS'],
  },
  'ss': laswap_srcs,
}
_lapack_roots += {
  'base': '?laswp_*',
  '_types': ['c', 'z'],
  '_meth': {
    'plus': ['-UMINUS'],
    'minus': ['-DMINUS'],
  },
  'ss': zlaswap_srcs,
}
