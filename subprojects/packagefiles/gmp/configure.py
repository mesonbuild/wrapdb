import argparse
import copy
from collections import OrderedDict
from fnmatch import fnmatch
from typing import Dict, List, NamedTuple, Optional

CompilerAndABI = NamedTuple(
    "CompilerAndABI",
    [
        ("compiler", str),
        ("abi", str)
    ]
)

# default abi identifier, usually the 32-bit one,
# shortcut for "last one in the abilist"
STANDARD_ABI = "standard"

# common abi + compiler defintions
GCC = CompilerAndABI(compiler="gcc", abi=STANDARD_ABI)
GCC_32 = CompilerAndABI(compiler="gcc", abi="32")
GCC_64 = CompilerAndABI(compiler="gcc", abi="64")
CC = CompilerAndABI(compiler="cc", abi=STANDARD_ABI)
CC_32 = CompilerAndABI(compiler="cc", abi="32")
CC_64 = CompilerAndABI(compiler="cc", abi="64")

CompilerOptions = NamedTuple(
    "CompilerOptions",
    [
        ("flags", List[str]),
        ("cpp_flags", List[str]),
        ("flags_maybe", List[str]),  # single flags to use if they work
        ("optional_flags", OrderedDict[str, List[str]]), # the first working flag of each list is kept
        ("ld_flags", List[str]),  # -Wc,-foo flags for libtool linking with compiler xx
        ("testlist", List[str])
    ],
)

ABIOptions = NamedTuple(
    "ABIOptions",
    [
        ("ar_flags", List[str]),  # extra flags for $AR
        ("nm_flags", List[str]),  # extra flags for $NM
        ("limb", Optional[str]),  # limb size, can be "longlong"
        ("mpn_search_path", List[str]),
        ("mpn_extra_functions", List[str]),
        ("calling_conventions_objs", List[str]),
        ("speed_cyclecounter_obj", Optional[str]),
        ("cyclecounter_size", int),
        ("testlist", List[str]),  # tests for any compiler with that abi
    ]
)

Options = NamedTuple(
    "Options",
    [
        ("compilers", Dict[CompilerAndABI, CompilerOptions]),
        ("abis", Dict[str, ABIOptions]),  # ABI name -> objs
        ("gmp_asm_syntax_testing", bool),
        ("defines", Dict[str, Optional[str]]),
        ("testlist", List[str]),  # tests for any compiler
        ("gmp_include_mpn", List[str])
    ]
)

def empty_compiler_options() -> CompilerOptions:
    return CompilerOptions(
        flags=[],
        cpp_flags=[],
        flags_maybe=[],
        optional_flags=OrderedDict(),
        ld_flags=[],
        testlist=[]
    )

def default_gcc_flags() -> List[str]:
    return ["-O2", "-pedantic"]

def default_gcc_options() -> CompilerOptions:
    return CompilerOptions(
        flags=default_gcc_flags(),
        cpp_flags=[],
        flags_maybe=[],
        optional_flags=OrderedDict(),
        ld_flags=[],
        testlist=[]
    )    


def default_cc_flags() -> List[str]:
    return ["-O"]

def default_cc_options() -> CompilerOptions:
    return CompilerOptions(
        flags=default_cc_flags(),
        cpp_flags=[],
        flags_maybe=[],
        optional_flags=OrderedDict(),
        ld_flags=[],
        testlist=[]
    )

def default_abi_options() -> ABIOptions:
    return ABIOptions(
        ar_flags=[],
        nm_flags=[],
        limb=None,
        mpn_search_path=[],
        mpn_extra_functions=[],
        calling_conventions_objs=[],
        speed_cyclecounter_obj=None,
        cyclecounter_size=2,
        testlist=[],
    )

def default_options() -> Options:
    return Options(
        compilers={
            GCC: default_gcc_options(),
            CC: default_cc_options(),             
        },
        abis={
            STANDARD_ABI: default_abi_options()
        },
        gmp_asm_syntax_testing=True,
        defines={},
        testlist=[],
        gmp_include_mpn=[]
    )

def match(text: str, *patterns: str) -> bool:
    return any(fnmatch(text, pattern) for pattern in patterns)

def mpn_search_path_for_alpha(host_cpu: str) -> List[str]:
    if match(host_cpu, "alphaev5*", "alphapca5*"):
        return ["alpha/ev5", "alpha"]
    elif match(host_cpu, "alphaev67", "alphaev68", "alphaev7*"):
        return ["alpha/ev67", "alpha/ev6", "alpha"]
    elif match(host_cpu, "alphaev6"):
        return ["alpha/ev6", "alpha"]
    else:
        return ["alpha"]

def asm_flags_for_alpha_gcc(host_cpu: str) -> List[str]:
    # gcc version "2.9-gnupro-99r1" on alphaev68-dec-osf5.1 has been seen
    # accepting -mcpu=ev6, but not putting the assembler in the right mode
    # for what it produces.  We need to do this for it, and need to do it
    # before testing the -mcpu options.
    #
    # On old versions of gcc, which don't know -mcpu=, we believe an
    # explicit -Wa,-mev5 etc will be necessary to put the assembler in
    # the right mode for our .asm files and longlong.h asm blocks.
    #
    # On newer versions of gcc, when -mcpu= is known, we must give a -Wa
    # which is at least as high as the code gcc will generate.  gcc
    # establishes what it needs with a ".arch" directive, our command line
    # option seems to override that.
    #
    # gas prior to 2.14 doesn't accept -mev67, but -mev6 seems enough for
    # ctlz and cttz (in 2.10.0 at least).
    #
    # OSF `as' accepts ev68 but stupidly treats it as ev4.  -arch only seems
    # to affect insns like ldbu which are expanded as macros when necessary.
    # Insns like ctlz which were never available as macros are always
    # accepted and always generate their plain code.
    if match(host_cpu, "alpha"):
        return ["-Wa,-arch,ev4", "-Wa,-mev4"]
    elif match(host_cpu, "alphaev5"):
        return ["-Wa,-arch,ev5", "-Wa,-mev5"]
    elif match(host_cpu, "alphaev56"):
        return ["-Wa,-arch,ev56", "-Wa,-mev56"]
    elif match(host_cpu, "alphapca56", "alphapca57"):
        return ["-Wa,-arch,pca56", "-Wa,-mpca56"]
    elif match(host_cpu, "alphaev6"):
        return ["-Wa,-arch,ev6", "-Wa,-mev6"]
    elif match(host_cpu, "alphaev67", "alphaev68", "alphaev7*"):
        return ["-Wa,-arch,ev67", "-Wa,-mev67", "-Wa,-arch,ev6", "-Wa,-mev6"]
    else:
        return []

def cpu_flags_for_alpha_gcc(host_cpu: str) -> List[str]:
    # gcc 2.7.2.3 doesn't know any -mcpu= for alpha, apparently.
    # gcc 2.95 knows -mcpu= ev4, ev5, ev56, pca56, ev6.
    # gcc 3.0 adds nothing.
    # gcc 3.1 adds ev45, ev67 (but ev45 is the same as ev4).
    # gcc 3.2 adds nothing.
    #
    # gcc version "2.9-gnupro-99r1" under "-O2 -mcpu=ev6" strikes internal
    # compiler errors too easily and is rejected by GMP_PROG_CC_WORKS.  Each
    # -mcpu=ev6 below has a fallback to -mcpu=ev56 for this reason.
    if match(host_cpu, "alpha"):
        return ["-mcpu=ev4"]
    elif match(host_cpu, "alphaev5"):
        return ["-mcpu=ev5"]
    elif match(host_cpu, "alphaev56"):
        return ["-mcpu=ev56"]
    elif match(host_cpu, "alphapca56", "alphapca57"):
        return ["-mcpu=pca56"]
    elif match(host_cpu, "alphaev6"):
        return ["-mcpu=ev6", "-mcpu=ev56"]
    elif match(host_cpu, "alphaev67", "alphaev68", "alphaev7*"):
        return ["-mcpu=ev67", "-mcpu=ev6", "-mcpu=ev56"]
    else:
        return []

def cpu_flags_for_alpha_cc(host_cpu: str) -> List[str]:
    # DEC C V5.9-005 knows ev4, ev5, ev56, pca56, ev6.
    # Compaq C V6.3-029 adds ev67.
    if match(host_cpu, "alpha"):
        return ["-arch~ev4~-tune~ev4"]
    elif match(host_cpu, "alphaev5"):
        return ["-arch~ev5~-tune~ev5"]
    elif match(host_cpu, "alphaev56"):
        return ["-arch~ev56~-tune~ev56"]
    elif match(host_cpu, "alphapca56", "alphapca57"):
        return ["-arch~pca56~-tune~pca56"]
    elif match(host_cpu, "alphaev6"):
        return ["-arch~ev6~-tune~ev6"]
    elif match(host_cpu, "alphaev67", "alphaev68", "alphaev7*"):
        return ["-arch~ev67~-tune~ev67", "-arch~ev6~-tune~ev6"]
    else:
        return []

def options_for_alpha_cc(host: str, host_cpu: str) -> CompilerOptions:
    # It might be better to ask "cc" whether it's Cray C or DEC C,
    # instead of relying on the OS part of $host.  But it's hard to
    # imagine either of those compilers anywhere except their native
    # systems.
    options = default_cc_options()
    if match(host, "*-cray-unicos*"):
        # no -g, it silently disables all optimizations
        return options._replace(flags=["-O"])
    elif match(host, "*-*-osf*"):
        return options._replace(
            flags=[],
            optional_flags=OrderedDict([
                # not sure if -fast works on old versions, so make it optional
                ("opt", ["-fast", "-O2"]),
                ("cpu", cpu_flags_for_alpha_cc(host_cpu))
            ])
        )
    else:
        return options

def options_for_alpha(host: str, host_cpu: str, assembly: bool) -> Options:
    options = default_options()._replace(
        defines={"HAVE_HOST_CPU_FAMILY_alpha": None}
    )
    options.gmp_include_mpn.append("alpha/alpha-defs.m4")
    abi_options = default_abi_options()._replace(
        mpn_search_path=mpn_search_path_for_alpha(host_cpu)
    )
    if assembly:
        abi_options = abi_options._replace(mpn_extra_functions=["cntlz"])
    options.abis[STANDARD_ABI] = abi_options
    options.compilers[GCC] = options.compilers[GCC]._replace(flags_maybe=["-mieee"])
    # need asm ahead of cpu, see below
    options.compilers[GCC].optional_flags["asm"] = asm_flags_for_alpha_gcc(host_cpu)
    options.compilers[GCC].optional_flags["cpu"] = cpu_flags_for_alpha_gcc(host_cpu)
    options.compilers[GCC].optional_flags["oldas"] = ["-Wa,-oldas"] # see GMP_GCC_WA_OLDAS.
    options.compilers[CC] = options_for_alpha_cc(host, host_cpu)

    if match(host, "*-cray-unicos*"):
        # Don't perform any assembly syntax tests on this beast.
        options = options._replace(gmp_asm_syntax_testing=False)
        options.gmp_include_mpn.append("alpha/unicos.m4")
    else:
        options.gmp_include_mpn.append("alpha/default.m4")

    if not match(host, "*-*-unicos*"):
        # tune/alpha.asm assumes int==4bytes but unicos uses int==8bytes
        options.abis[STANDARD_ABI] = options.abis[STANDARD_ABI]._replace(
            speed_cyclecounter_obj="alpha.lo",
            cyclecounter_size=1
        )
    
    return options
    
def options_for_cray() -> Options:
    # Cray vector machines.
    # This must come after alpha* so that we can recognize present and future
    # vector processors with a wildcard.

    # We used to have -hscalar0 here as a workaround for miscompilation of
    # mpz/import.c, but let's hope Cray fixes their bugs instead, since
    # -hscalar0 causes disastrously poor code to be generated.
    cc_options = default_cc_options()._replace(
        flags=["-O3", "-hnofastmd", "-htask0", "-Wa,-B"]
    )
    abi_options = default_abi_options()._replace(
        mpn_search_path=["cray"]
    )
    return default_options()._replace(
        gmp_asm_syntax_testing=False,
        compilers={CC: cc_options},
        abis={STANDARD_ABI: abi_options}
    )

def mpn_search_path_for_arm(host_cpu: str) -> List[str]:
    if match(host_cpu, "armxscale", "arm7ej", "arm9te", "arm9e*", "arm10*", "armv5*"):
        return ["arm/v5", "arm"]
    elif match(host_cpu, "armsa1", "arm7t*", "arm9t*", "armv4t*"):
        return ["arm"]
    elif match(host_cpu, "arm1156", "armv6t2*"):
        return ["arm/v6t2", "arm/v6", "arm/v5", "arm"]
    elif match(host_cpu, "arm11*", "armv6*"):
        return ["arm/v6", "arm/v5", "arm"]
    elif match(host_cpu, "armcortexa5", "armv7*"):
        return ["arm/v7a/cora5", "arm/v6t2", "arm/v6", "arm/v5", "arm"]
    elif match(host_cpu, "armcortexa5neon"):
        return ["arm/neon", "arm/v7a/cora5", "arm/v6t2", "arm/v6", "arm/v5", "arm"]
    elif match(host_cpu, "armcortexa7"):
        return ["arm/v7a/cora7", "arm/v6t2", "arm/v6", "arm/v5", "arm"]
    elif match(host_cpu, "armcortexa7neon"):
        return ["arm/neon", "arm/v7a/cora7", "arm/v6t2", "arm/v6", "arm/v5", "arm"]
    elif match(host_cpu, "armcortexa8"):
        return ["arm/v7a/cora8", "arm/v6t2", "arm/v6", "arm/v5", "arm"]
    elif match(host_cpu, "armcortexa8neon"):
        return ["arm/neon", "arm/v7a/cora8", "arm/v6t2", "arm/v6", "arm/v5", "arm"]
    elif match(host_cpu, "armcortexa9"):
        return ["arm/v7a/cora9", "arm/v6t2", "arm/v6", "arm/v5", "arm"]
    elif match(host_cpu, "armcortexa9neon"):
        return ["arm/neon", "arm/v7a/cora9", "arm/v6t2", "arm/v6", "arm/v5", "arm"]
    elif match(host_cpu, "armcortexa15"):
        return ["arm/v7a/cora15", "arm/v6t2", "arm/v6", "arm/v5", "arm"]
    elif match(host_cpu, "armcortexa15neon"):
        return ["arm/v7a/cora15/neon", "arm/neon", "arm/v7a/cora15", "arm/v6t2", "arm/v6", "arm/v5", "arm"]
    elif match(host_cpu, "armcortexa12", "armcortexa17"):
        return ["arm/v7a/cora17", "arm/v7a/cora15", "arm/v6t2", "arm/v6", "arm/v5", "arm"]
    elif match(host_cpu, "armcortexa12neon", "armcortexa17neon"):
        return [
            "arm/v7a/cora17/neon",
            "arm/v7a/cora15/neon",
            "arm/neon",
            "arm/v7a/cora17",
            "arm/v7a/cora15",
            "arm/v6t2",
            "arm/v6",
            "arm/v5",
            "arm"
        ]
    elif match(host_cpu, "armcortexa53", "armcortexa53neon", "armcortexa55", "armcortexa55neon"):
        return ["arm/neon", "arm/v7a/cora9", "arm/v6t2", "arm/v6", "arm/v5", "arm"]
    elif match(
        host_cpu,
        "armcortexa57", "armcortexa57neon",
        "armcortexa7[2-9]", "armcortexa7[2-9]neon",
        "armexynosm1",
        "armthunderx",
        "armxgene1",
        "aarch64*"
    ):
        return ["arm/v7a/cora15/neon", "arm/neon", "arm/v7a/cora15", "arm/v6t2", "arm/v6", "arm/v5", "arm"]
    else:
        return ["arm"]

def mpn_search_path_for_arm_64(host_cpu: str) -> List[str]:
    if match(host_cpu, "armcortexa53", "armcortexa53neon", "armcortexa55", "armcortexa55neon"):
        return ["arm64/cora53", "arm64"]
    elif match(
        host_cpu,
        "armcortexa57", "armcortexa57neon",
        "armcortexa7[2-9]", "armcortexa7[2-9]neon"
    ):
        return ["arm64/cora57", "arm64"]
    elif match(host_cpu, "armexynosm1", "armthunderx", "aarch64*"):
        return ["arm64"]
    elif match(host_cpu, "armxgene1"):
        return ["arm64/xgene1", "arm64"]
    else:
        return []

def arch_flags_for_arm_gcc(host_cpu: str) -> List[str]:
    if match(host_cpu, "armxscale", "arm7ej", "arm9te", "arm9e*", "arm10*", "armv5*"):
        return ["-march=armv5"]
    elif match(host_cpu, "armsa1", "arm7t*", "arm9t*", "armv4t*"):
        return ["-march=armv4"]
    elif match(host_cpu, "arm1156", "armv6t2*"):
        return ["-march=armv6t2"]
    elif match(host_cpu, "arm11*", "armv6*"):
        return ["-march=armv6"]
    elif match(
        host_cpu,
        "armcortexa5", "armv7*",
        "armcortexa5neon",
        "armcortexa8", "armcortexa8neon",
        "armcortexa9",
        "armcortexa9neon"
    ):
        return ["-march=armv7-a"]
    elif match(host_cpu, "armcortexa7", "armcortexa7neon"):
        return ["-march=armv7ve", "-march=armv7-a"]
    elif match(
        host_cpu,
        "armcortexa15",
        "armcortexa15neon",
        "armcortexa12", "armcortexa17",
        "armcortexa12neon", "armcortexa17neon"
    ):
        return ["-march=armv7ve", "-march=armv7-a"]
    elif match(
        host_cpu,
        "armcortexa53", "armcortexa53neon", "armcortexa55", "armcortexa55neon",
        "armcortexa57", "armcortexa57neon",
        "armcortexa7[2-9]", "armcortexa7[2-9]neon",
        "armexynosm1",
        "armthunderx",
        "armxgene1",
        "aarch64*"
    ):
        return ["-march=armv8-a"]
    else:
        return ["-march=armv4"]

def tune_flags_for_arm_gcc(host_cpu: str) -> List[str]:
    if match(host_cpu, "armcortexa5", "armcortexa5neon", "armv7*",):
        return ["-mtune=cortex-a5"]
    elif match(host_cpu, "armcortexa7", "armcortexa7neon"):
        return ["-mtune=cortex-a7"]
    elif match(host_cpu, "armcortexa8", "armcortexa8neon"):
        return ["-mtune=cortex-a8"]
    elif match(host_cpu, "armcortexa9", "armcortexa9neon"):
        return ["-mtune=cortex-a9"]
    elif match(
        host_cpu,
        "armcortexa12", "armcortexa12neon",
        "armcortexa15", "armcortexa15neon",
        "armcortexa17", "armcortexa17neon",
    ):
        return ["-mtune=cortex-a15", "-mtune=cortex-a9"]
    elif match(
        host_cpu,
        "armcortexa53", "armcortexa53neon",
        "armcortexa55", "armcortexa55neon",
    ):
        return ["-mtune=cortex-a53"]
    elif match(host_cpu, "armcortexa57", "armcortexa57neon"):
        return ["-mtune=cortex-a57"]
    elif match(host_cpu, "armcortexa7[2-9]", "armcortexa7[2-9]neon"):
        return ["-mtune=cortex-a72", "-mtune=cortex-a57"]
    elif match(host_cpu, "armexynosm1"):
        return ["-mtune=exynosm1"]
    elif match(host_cpu, "armthunderx"):
        return ["-mtune=thunderx"]
    elif match(host_cpu, "armxgene1"):
        return ["-mtune=xgene1"]
    else:
        return []

def neon_flags_for_arm_gcc(host_cpu: str) -> List[str]:
    if match(
        host_cpu,
        "*neon", # 5, 7, 8, 9, 12, 15, 17, 53, 55, 57, 7[2-9]
        "armcortexa53",
        "armcortexa55",
        "armcortexa57",
        "armcortexa7[2-9]",
        "armexynosm1",
        "armthunderx",
        "armxgene1",
        "aarch64*"
    ):
        return ["-mfpu=neon"]
    else:
        return []

def fpmode_flags_from_arm_gcc(host: str) -> List[str]:
    # This is needed for clang, which is not content with flags like -mfpu=neon
    # alone.
    if match(host, "*-*-*eabi"):
        return ["-mfloat-abi=softfp"]
    elif match(host, "*-*-*eabihf"):
        return ["-mfloat-abi=hard"]
    else:
        return []

def arm_cpu_has_64_abi(host_cpu: str) -> bool:
    return match(
        host_cpu,
        "armcortexa53", "armcortexa53neon", "armcortexa55", "armcortexa55neon",
        "armcortexa57", "armcortexa57neon",
        "armcortexa7[2-9]", "armcortexa7[2-9]neon",
        "armexynosm1",
        "armthunderx",
        "armxgene1",
        "aarch64*",
    )

def omit_frame_pointer_if_needed(options: Options, profiling: str) -> Options:
    if profiling != "gprof":
        options.compilers[GCC].flags.append("-fomit-frame-pointer")
    
    return options

def options_for_arm(host: str, host_cpu: str, profiling: str) -> Options:
    options = default_options()
    options.abis[STANDARD_ABI] = default_abi_options()._replace(
        mpn_search_path=mpn_search_path_for_arm(host_cpu),
        calling_conventions_objs=["arm32call.lo", "arm32check.lo"],
        testlist=["sizeof-void*-4"]
    )
    options = omit_frame_pointer_if_needed(options, profiling)
    options.compilers[GCC] = options.compilers[GCC]._replace(
        optional_flags=OrderedDict([
            ("arch", arch_flags_for_arm_gcc(host_cpu)),
            ("fpmode", fpmode_flags_from_arm_gcc(host)),
            ("neon", neon_flags_for_arm_gcc(host_cpu)),
            ("tune", tune_flags_for_arm_gcc(host_cpu))
        ]),
        testlist=["gcc-arm-umodsi"]
    )

    if arm_cpu_has_64_abi(host_cpu):
        options.abis["64"] = default_abi_options()._replace(
            mpn_search_path=mpn_search_path_for_arm_64(host_cpu),
            calling_conventions_objs=[],
            testlist=["sizeof-void*-8"]
        )
        options.compilers[CC_64] = default_cc_options()
        options.compilers[GCC_64] = default_gcc_options()._replace(
            optional_flags=OrderedDict([
                ("arch", options.compilers[GCC].optional_flags["arch"]),
                ("tune", options.compilers[GCC].optional_flags["tune"])
            ]),
            testlist=[]
        )
        if match(host, "*-*-mingw*"):
            options.abis["64"] = options.abis["64"]._replace(limb="longlong")
    
    return options


def options_for_fujitsu() -> Options:
    VCC = CompilerAndABI(compiler="vcc", abi=STANDARD_ABI)
    # FIXME: flags for vcc?
    vcc_options = empty_compiler_options()._replace(flags=["-g"])
    abi_options = default_abi_options()._replace(
        mpn_search_path=["fujitsu"]
    )
    return default_options()._replace(
        compilers={
            GCC: default_gcc_options(),
            VCC: vcc_options
        },
        abis={STANDARD_ABI: abi_options},
        gmp_include_mpn=["ia64/ia64-defs.m4"]
    )

def mpn_search_path_for_hp(host_cpu: str) -> List[str]:
    # FIXME: For hppa2.0*, path should be "pa32/hppa2_0 pa32/hppa1_1 pa32".
    # (Can't remember why this isn't done already, have to check what .asm
    # files are available in each and how they run on a typical 2.0 cpu.)
    if match(host_cpu, "hppa1.0*"):
        return ["pa32"]
    elif match(host_cpu, "hppa7000*"):
        return ["pa32/hppa1_1", "pa32"]
    elif match(host_cpu, "hppa2.0*", "hppa64"):
        return ["pa32/hppa2_0", "pa32/hppa1_1/pa7100", "pa32/hppa1_1", "pa32"]
    else:  # default to 7100
        return ["pa32/hppa1_1/pa7100", "pa32/hppa1_1", "pa32"]

def arch_flags_for_hp_gcc(host_cpu: str) -> List[str]:
    # gcc 2.7.2.3 knows -mpa-risc-1-0 and -mpa-risc-1-1
    # gcc 2.95 adds -mpa-risc-2-0, plus synonyms -march=1.0, 1.1 and 2.0
    #
    # We don't use -mpa-risc-2-0 in ABI=1.0 because 64-bit registers may not
    # be saved by the kernel on an old system.  Actually gcc (as of 3.2)
    # only adds a few float instructions with -mpa-risc-2-0, so it would
    # probably be safe, but let's not take the chance.  In any case, a
    # configuration like --host=hppa2.0 ABI=1.0 is far from optimal.
    if match(host_cpu, "hppa1.0*"):
        return ["-mpa-risc-1-0"]
    else:  # default to 7100
        return ["-mpa-risc-1-1"]

def flags_for_hp_cc(host_cpu: str) -> List[str]:
    if match(host_cpu, "hppa1.0*"):
        return ["+O2"]
    else:  # default to 7100
        return ["+DA1.1", "+O2"]

def options_for_hp(host: str, host_cpu: str) -> Options:
    # HP cc (the one sold separately) is K&R by default, but AM_C_PROTOTYPES
    # will add "-Ae", or "-Aa -D_HPUX_SOURCE", to put it into ansi mode, if
    # possible.
    
    # gcc for hppa 2.0 can be built either for 2.0n (32-bit) or 2.0w
    # (64-bit), but not both, so there's no option to choose the desired
    # mode, we must instead detect which of the two it is.  This is done by
    # checking sizeof(long), either 4 or 8 bytes respectively.  Do this in
    # ABI=1.0 too, in case someone tries to build that with a 2.0w gcc.
    options = default_options()
    options.compilers[GCC] = default_gcc_options()._replace(
        optional_flags=OrderedDict([
            ("arch", arch_flags_for_hp_gcc(host_cpu)),
        ]),
        testlist=["sizeof-long-4"]
    )
    options.compilers[CC] = default_cc_options()._replace(
        flags=flags_for_hp_cc(host_cpu)
    )
    options.abis[STANDARD_ABI] = default_abi_options()._replace(
        mpn_search_path=mpn_search_path_for_hp(host_cpu),
        speed_cyclecounter_obj="hppa.lo",
        cyclecounter_size=1
    )

    if match(host, "hppa2.0*-*-*", "hppa64-*-*"):
        ABI_20N = "2.0n"
        options.abis[ABI_20N] = default_abi_options()._replace(
            mpn_search_path=["pa64"],
            limb="longlong",
            speed_cyclecounter_obj="hppa2.lo",
            cyclecounter_size=2,
            testlist=["sizeof-long-4"]
        )
        GCC_20N = CompilerAndABI(compiler="gcc", abi=ABI_20N)

        # -mpa-risc-2-0 is only an optional flag, in case an old gcc is
        # used.  Assembler support for 2.0 is essential though, for our asm
        # files.
        options.compilers[GCC_20N] = default_gcc_options()._replace(
            optional_flags=OrderedDict([
                ("arch", ["-mpa-risc-2-0", "-mpa-risc-1-1"]),
            ]),
            testlist=["sizeof-long-4", "hppa-level-2.0"],
        )
        CC_20N = CompilerAndABI(compiler="cc", abi=ABI_20N)
        options.compilers[CC_20N] = empty_compiler_options()._replace(
            flags=["+DA2.0", "+e", "+O2", "-Wl,+vnocompatwarnings"],
            testlist=["hpc-hppa-2-0"]
        )

        # ABI=2.0w is available for hppa2.0w and hppa2.0, but not for
        # hppa2.0n, on the assumption that that the latter indicates a
        # desire for ABI=2.0n.
        # HPUX 10 and earlier cannot run 2.0w.  Not sure about other
        # systems (GNU/Linux for instance), but lets assume they're ok.
        if (
            not match(host, "hppa2.0n-*-*")
            and not match(host, "*-*-hpux[1-9]", "*-*-hpux[1-9].*", "*-*-hpux10", "*-*-hpux10.*")
        ):
            ABI_20W = "2.0w"
            GCC_20W = CompilerAndABI(compiler="gcc", abi=ABI_20W)
            options.compilers[GCC_20W] = default_gcc_options()._replace(
                flags=default_gcc_flags() + ["-mpa-risc-2-0"]
            )
            CC_20W = CompilerAndABI(compiler="cc", abi=ABI_20W)
            options.compilers[CC_20W] = empty_compiler_options()._replace(
                flags=["+DD64", "+O2"],
                testlist=["hpc-hppa-2-0"]
            )
            options.abis[ABI_20W] = default_abi_options()._replace(
                mpn_search_path=["pa64"],
                speed_cyclecounter_obj="hppa2w.lo",
                cyclecounter_size=2,
                testlist=["sizeof-long-8"]
            )
    
    return options

def mpn_search_path_for_itanium(host_cpu: str) -> List[str]:
    if match(host_cpu, "itanium"):
        return ["ia64/itanium", "ia64"]
    elif match(host_cpu, "itanium2"):
        return ["ia64/itanium2", "ia64"]
    else:
        return ["ia64"]

def tune_flags_for_itanium_gcc(host_cpu: str) -> List[str]:
    # gcc pre-release 3.4 adds -mtune itanium and itanium2
    if match(host_cpu, "itanium"):
        return ["-mtune=itanium"]
    elif match(host_cpu, "itanium2"):
        return ["-mtune=itanium2"]
    else:
        return []    

def options_for_itanium(host: str, host_cpu: str) -> Options:
    options = default_options()
    options.abis[STANDARD_ABI] = default_abi_options()._replace(
        mpn_search_path=mpn_search_path_for_itanium(host_cpu),
        speed_cyclecounter_obj="ia64.lo",
    )
    options.compilers[GCC].optional_flags["tune"] = tune_flags_for_itanium_gcc(host_cpu)
    if match(host, "*-*-linux*"):
        ICC = CompilerAndABI(compiler="icc", abi=STANDARD_ABI)
        options.compilers[ICC] = empty_compiler_options()._replace(
            flags=["-no-gcc"],
            # Don't use -O3, it is for "large data sets" and also miscompiles GMP.
            # But icc miscompiles GMP at any optimization level, at higher levels
            # it miscompiles more files...
            optional_flags=OrderedDict([("opt", ["-O2", "-O1"])])
            # Stepland: the original script had this defintion
            # icc_cflags_opt_maybe="-fp-model~precise"
            # but it looks like it goes completely unused by the configure script ...
        )
    elif match(host, "*-*-hpux*"):
        # HP cc sometimes gets internal errors if the optimization level is
        # too high.  GMP_PROG_CC_WORKS detects this, the "_opt" fallbacks
        # let us use whatever seems to work.
        options.abis["32"] = default_abi_options()._replace(
            mpn_search_path=["ia64"],
            limb="longlong",
            speed_cyclecounter_obj="ia64.lo",
            cyclecounter_size=2,
            testlist=["sizeof-long-4"]
        )
        options.abis["64"] = default_abi_options()._replace(
            testlist=["sizeof-long-8"]
        )
        options.compilers[GCC_32] = copy.deepcopy(options.compilers[GCC])._replace(
            flags=default_gcc_flags() + ["-milp32"]
        )
        options.compilers[CC_32] = default_cc_options()._replace(
            flags=[],
            optional_flags=OrderedDict([("opt", ["+O2", "+O1"])])
        )

        # Must have +DD64 in CPPFLAGS to get the right __LP64__ for headers,
        # but also need it in CFLAGS for linking programs, since automake
        # only uses CFLAGS when linking, not CPPFLAGS.
        # FIXME: Maybe should use cc_64_ldflags for this, but that would
        # need GMP_LDFLAGS used consistently by all the programs.
        options.compilers[CC] = options.compilers[CC]._replace(
            flags=["+DD64"],
            cpp_flags=["+DD64"],
            optional_flags=OrderedDict([("opt", ["+O2", "+O1"])])
        )
        options.compilers[GCC] = options.compilers[GCC]._replace(
            flags=default_gcc_flags() + ["-mlp64"]
        )
    
    return options

def arch_flags_for_motorola_68k_gcc(host_cpu: str) -> List[str]:
    # gcc 2.7.2 knows -m68000, -m68020, -m68030, -m68040.
    # gcc 2.95 adds -mcpu32, -m68060.
    # FIXME: Maybe "-m68020 -mnobitfield" would suit cpu32 on 2.7.2.
    if match(host_cpu, "m68020"):
        return ["-m68020"]
    elif match(host_cpu, "m68030"):
        return ["-m68030"]
    elif match(host_cpu, "m68040"):
        return ["-m68040"]
    elif match(host_cpu, "m68060"):
        return ["-m68060", "-m68000"]
    elif match(host_cpu, "m68360"):
        return ["-mcpu32", "-m68000"]
    else:
        return ["-m68000"]

def mpn_search_path_for_motorola_68k(host_cpu: str) -> List[str]:
    # FIXME: m68k/mc68020 looks like it's ok for cpu32, but this wants to be
    # tested.  Will need to introduce an m68k/cpu32 if m68k/mc68020 ever uses
    # the bitfield instructions.
    if match(host_cpu, "m680[234]0", "m68360"):
        return ["m68k/mc68020", "m68k"]
    else:
        return ["m68k"]

def options_for_motorola_68k(host_cpu: str, profiling: str) -> Options:
    # Motorola 68k
    options = default_options()._replace(
        defines={"HAVE_HOST_CPU_FAMILY_m68k": None},
        gmp_include_mpn=["m68k/m68k-defs.m4"]
    )
    options = omit_frame_pointer_if_needed(options, profiling) 
    options.compilers[GCC].optional_flags["arch"] = arch_flags_for_motorola_68k_gcc(host_cpu)
    options.abis[STANDARD_ABI]._replace(
        mpn_search_path=mpn_search_path_for_motorola_68k(host_cpu)
    )
    return options

def options_for_motorola_88k() -> Options:
    options = default_options()
    options.abis[STANDARD_ABI] = options.abis[STANDARD_ABI]._replace(
        mpn_search_path=["m88k"]
    )
    return options

def options_for_motorola_88110() -> Options:
    options = default_options()
    options.compilers[GCC] = options.compilers[GCC]._replace(
        flags=default_gcc_flags() + ["-m88110"]
    )
    options.abis[STANDARD_ABI] = options.abis[STANDARD_ABI]._replace(
        mpn_search_path=["m88k/mc88110", "m88k"]
    )
    return options

def mpn_search_path_for_mips_64(host_cpu: str) -> List[str]:
    if match(host_cpu, "mips64r[6789]*", "mipsisa64r[6789]*"):
        return ["mips64/r6", "mips64"]
    else:
        return ["mips64/hilo", "mips64"]

def options_for_mips(host: str, host_cpu: str) -> Options:
    # IRIX 5 and earlier can only run 32-bit o32.
    #
    # IRIX 6 and up always has a 64-bit mips CPU can run n32 or 64.  n32 is
    # preferred over 64, but only because that's been the default in past
    # versions of GMP.  The two are equally efficient.
    #
    # Linux kernel 2.2.13 arch/mips/kernel/irixelf.c has a comment about not
    # supporting n32 or 64.
    #
    # For reference, libtool (eg. 1.5.6) recognises the n32 ABI and knows the
    # right options to use when linking (both cc and gcc), so no need for
    # anything special from us.
    options = default_options()
    options.gmp_include_mpn.append("mips32/mips-defs.m4")
    options.compilers[GCC].optional_flags["abi"] = ["-mabi=32", "-m32"]
    options.compilers[GCC] = options.compilers[GCC]._replace(
        testlist=["gcc-mips-o32"]
    )
    options.abis[STANDARD_ABI] = options.abis[STANDARD_ABI]._replace(
        mpn_search_path=["mips32"]
    )
    options.compilers[CC] = options.compilers[CC]._replace(
        flags=["-O2", "-o32"]  # no -g, it disables all optimizations
    )

    if match(host, "mips64*-*-*", "mipsisa64*-*-*", "mips*-*-irix[6789]*"):
        ABI_N32 = "n32"
        GCC_N32 = CompilerAndABI(compiler="gcc", abi=ABI_N32)
        options.compilers[GCC_N32] = default_gcc_options()
        options.compilers[GCC_N32].optional_flags["abi"] = ["-mabi=n32", "-mn32"]
        CC_N32 = CompilerAndABI(compiler="cc", abi=ABI_N32)
        options.compilers[CC_N32] = default_cc_options()._replace(
            flags=["-O2", "-n32"]  # no -g, it disables all optimizations
        )
        options.abis[ABI_N32] = default_abi_options()._replace(
            mpn_search_path=mpn_search_path_for_mips_64(host_cpu),
            limb="longlong"
        )

        options.compilers[GCC_64] = default_gcc_options()._replace(
            ld_flags=["-Wc,-mabi=64"]
        )
        options.compilers[GCC_64].optional_flags["abi"] = ["-mabi=64", "-m64"]
        options.compilers[CC_64] = default_cc_options()._replace(
            flags=["-O2", "-64"],  # no -g, it disables all optimizations
            ld_flags=["-Wc,-64"]
        )
        options.abis["64"] = default_abi_options()._replace(
            mpn_search_path=mpn_search_path_for_mips_64(host_cpu)
        )
    
    return options

def mpn_search_path_for_powerpc(host_cpu: str) -> List[str]:
    if match(host_cpu, "powerpc740", "powerpc750"):
        return ["powerpc32/750", "powerpc32"]
    elif match(host_cpu, "powerpc7400", "powerpc7410"):
        return ["powerpc32/vmx", "powerpc32/750", "powerpc32"]
    elif match(host_cpu, "powerpc74[45]?"):
        return ["powerpc32/vmx", "powerpc32"]
    else:
        return ["powerpc32"]

def cpu_flags_for_powerpc_gcc(host_cpu: str) -> List[str]:
    if match(host_cpu, "powerpc401"):
        return ["-mcpu=401"]
    elif match(host_cpu, "powerpc403"):
        return ["-mcpu=403"]
    elif match(host_cpu, "powerpc405"):
        return ["-mcpu=405"]
    elif match(host_cpu, "powerpc505"):
        return ["-mcpu=505"]
    elif match(host_cpu, "powerpc601"):
        return ["-mcpu=601"]
    elif match(host_cpu, "powerpc602"):
        return ["-mcpu=602"]
    elif match(host_cpu, "powerpc603"):
        return ["-mcpu=603"]
    elif match(host_cpu, "powerpc603e"):
        return ["-mcpu=603e", "-mcpu=603"]
    elif match(host_cpu, "powerpc604"):
        return ["-mcpu=604"]
    elif match(host_cpu, "powerpc604e"):
        return ["-mcpu=604e", "-mcpu=604"]
    elif match(host_cpu, "powerpc620"):
        return ["-mcpu=620"]
    elif match(host_cpu, "powerpc630"):
        return ["-mcpu=630"]
    elif match(host_cpu, "powerpc740"):
        return ["-mcpu=740"]
    elif match(host_cpu, "powerpc7400", "powerpc7410"):
        return ["-mcpu=7400", "-mcpu=750"]
    elif match(host_cpu, "powerpc74[45]?"):
        return ["-mcpu=7450"]
    elif match(host_cpu, "powerpc750"):
        return ["-mcpu=750"]
    elif match(host_cpu, "powerpc801"):
        return ["-mcpu=801"]
    elif match(host_cpu, "powerpc821"):
        return ["-mcpu=821"]
    elif match(host_cpu, "powerpc823"):
        return ["-mcpu=823"]
    elif match(host_cpu, "powerpc860"):
        return ["-mcpu=860"]
    elif match(host_cpu, "powerpc970"):
        return ["-mtune=970"]  # Stepland: not -mcpu ?
    elif match(host_cpu, "power4"):
        return ["-mtune=power4"]
    elif match(host_cpu, "power5"):
        return ["-mtune=power5", "-mtune=power4"]
    elif match(host_cpu, "power6"):
        return ["-mtune=power6"]
    elif match(host_cpu, "power7"):
        return ["-mtune=power7", "-mtune=power5"]
    elif match(host_cpu, "power8"):
        return ["-mtune=power8", "-mtune=power7", "-mtune=power5"]
    elif match(host_cpu, "power9"):
        return ["-mtune=power9", "-mtune=power8", "-mtune=power7", "-mtune=power5"]
    else:
        return []

def arch_flags_for_powerpc_xlc(host_cpu: str) -> List[str]:
    if match(host_cpu, "powerpc403"):
        return ["-qarch=403", "-qarch=ppc"]
    elif match(host_cpu, "powerpc601"):
        return ["-qarch=601", "-qarch=ppc"]
    elif match(host_cpu, "powerpc602"):
        return ["-qarch=602", "-qarch=ppc"]
    elif match(host_cpu, "powerpc603", "powerpc603e"):
        return ["-qarch=603", "-qarch=ppc"]
    elif match(host_cpu, "powerpc604", "powerpc604e"):
        return ["-qarch=604", "-qarch=ppc"]
    elif match(host_cpu, "powerpc630"):
        return ["-qarch=pwr3"]
    elif match(host_cpu, "powerpc970"):
        return ["-qarch=970", "-qarch=pwr3"]
    elif match(host_cpu, "power4"):
        return ["-qarch=pwr4"]
    elif match(host_cpu, "power5"):
        return ["-qarch=pwr5"]
    elif match(host_cpu, "power6"):
        return ["-qarch=pwr6"]
    elif match(host_cpu, "power7"):
        return ["-qarch=pwr7", "-qarch=pwr5"]
    elif match(host_cpu, "power8"):
        return ["-qarch=pwr8", "-qarch=pwr7", "-qarch=pwr5"]
    elif match(host_cpu, "power9"):
        return ["-qarch=pwr9", "-qarch=pwr8", "-qarch=pwr7", "-qarch=pwr5"]
    else:
        return []    

def cpu_path_for_powerpc(host_cpu: str) -> List[str]:
    if match(host_cpu, "powerpc630"):
        return ["p3", "p3-p7"]
    elif match(host_cpu, "powerpc970", "power4"):
        return ["p4", "p3-p7"]
    elif match(host_cpu, "power5"):
        return ["p5", "p4", "p3-p7"]
    elif match(host_cpu, "power6"):
        return ["p6", "p3-p7"]
    elif match(host_cpu, "power7"):
        return ["p7", "p5", "p4", "p3-p7"]
    elif match(host_cpu, "power8"):
        return ["p8", "p7", "p5", "p4", "p3-p7"]
    elif match(host_cpu, "power9"):
        return ["p9", "p8", "p7", "p5", "p4", "p3-p7"]
    else:
        return []     

def vmx_path_for_powerpc(host_cpu: str) -> List[str]:
    if match(host_cpu, "powerpc970"):
        return ["powerpc64/vmx"]
    else:
        return []   

def mpn_search_path_for_powerpc_with_abi(host_cpu: str, abi: str) -> List[str]:
    res = [
        base + cpu_path
        for cpu_path in cpu_path_for_powerpc(host_cpu)
        for base in (
            "powerpc64/{}/".format(abi),
            "powerpc64/")
    ]
    res.extend([
        "powerpc64/{}".format(abi),
        *vmx_path_for_powerpc(host_cpu),
        "powerpc64"
    ])
    return res

def extended_mpn_search_path_for_powerpc(host_cpu: str) -> List[str]:
    return [
        "powerpc32/" + cpu_path
        for cpu_path in cpu_path_for_powerpc(host_cpu)
    ]

def options_for_powerpc_aix_64(options: Options, host_cpu: str) -> Options:
    # On AIX a true 64-bit ABI is available.
    # Need -Wc to pass object type flags through to the linker.
    MODE64 = "mode64"
    GCC_MODE64 = CompilerAndABI(compiler="gcc", abi=MODE64)
    options.compilers[GCC_MODE64] = default_gcc_options()._replace(
        flags=default_gcc_flags() + ["-maix64", "-mpowerpc64"],
        ld_flags=["-Wc,-maix64"]
    )
    options.compilers[GCC_MODE64].optional_flags["cpu"] = cpu_flags_for_powerpc_gcc(host_cpu)
    XLC_MODE64 = CompilerAndABI(compiler="xlc", abi=MODE64)
    options.compilers[XLC_MODE64] = empty_compiler_options()._replace(
        flags=["-O2", "-q64", "-qmaxmem=20000"],
        ld_flags=["-Wc,-q64"]
    )
    options.compilers[XLC_MODE64].optional_flags["arch"] = arch_flags_for_powerpc_xlc(host_cpu)
    options.abis[MODE64] = default_abi_options()._replace(
        mpn_search_path=mpn_search_path_for_powerpc_with_abi(host_cpu, MODE64),
        ar_flags=["-X64"],
        nm_flags=["-X64"],
        # grab this object, though it's not a true cycle counter routine
        speed_cyclecounter_obj="powerpc64.lo",
        cyclecounter_size=0
    )
    options.abis[STANDARD_ABI] = options.abis[STANDARD_ABI]._replace(
        mpn_search_path=(
            extended_mpn_search_path_for_powerpc(host_cpu)
            + options.abis[STANDARD_ABI].mpn_search_path
        ),
    )
    return options  

def options_for_powerpc_darwin_64(options: Options, host_cpu: str) -> Options:
    # On Darwin we can use 64-bit instructions with a longlong limb,
    # but the chip still in 32-bit mode.
    # In theory this can be used on any OS which knows how to save
    # 64-bit registers in a context switch.

    # Note that we must use -mpowerpc64 with gcc, since the
    # longlong.h macros expect limb operands in a single 64-bit
    # register, not two 32-bit registers as would be given for a
    # long long without -mpowerpc64.  In theory we could detect and
    # accommodate both styles, but the proper 64-bit registers will
    # be fastest and are what we really want to use.

    # One would think -mpowerpc64 would set the assembler in the right
    # mode to handle 64-bit instructions.  But for that, also
    # -force_cpusubtype_ALL is needed.

    # Do not use -fast for Darwin, it actually adds options
    # incompatible with a shared library.
    options.compilers[GCC] = options.compilers[GCC]._replace(
        flags=["-O2", "-O1"]  # will this become used?
    )
    MODE32 = "mode32"
    GCC_MODE32 = CompilerAndABI(compiler="gcc", abi=MODE32)
    options.compilers[GCC_MODE32] = default_gcc_options()._replace(
        flags=["-mpowerpc64"],
        flags_maybe=["-m32"],
        optional_flags=OrderedDict([
            ("subtype", ["-force_cpusubtype_ALL"]),
            ("cpu", cpu_flags_for_powerpc_gcc(host_cpu)),
            ("opt", ["-O2", "-O1"]),
        ])
    )
    options.abis[MODE32] = default_abi_options()._replace(
        mpn_search_path=mpn_search_path_for_powerpc_with_abi(host_cpu, MODE32),
        limb="longlong"
    )
    MODE64 = "mode64"
    GCC_MODE64 = CompilerAndABI(compiler="gcc", abi=MODE64)
    options.compilers[GCC_MODE64] = default_gcc_options()._replace(
        flags=["-m64"],
        optional_flags=OrderedDict([
            ("cpu", cpu_flags_for_powerpc_gcc(host_cpu)),
            ("opt", ["-O2", "-O1"])
        ])
    )
    options.abis[MODE64] = default_abi_options()._replace(
        mpn_search_path=mpn_search_path_for_powerpc_with_abi(host_cpu, MODE64),
        speed_cyclecounter_obj="powerpc64.lo",
        cyclecounter_size=0,
        testlist=["sizeof-long-8"]
    )
    options.abis[STANDARD_ABI] = options.abis[STANDARD_ABI]._replace(
        mpn_search_path=(
            extended_mpn_search_path_for_powerpc(host_cpu)
            + options.abis[STANDARD_ABI].mpn_search_path
        ),
    )
    return options

def options_for_powerpc_linux_64(options: Options, host_cpu: str) -> Options:
    # On GNU/Linux, assume the processor is in 64-bit mode.  Some
    # environments have a gcc that is always in 64-bit mode, while
    # others require -m64, hence the use of cflags_maybe.  The
    # sizeof-long-8 test checks the mode is right (for the no option
    # case).

    # -mpowerpc64 is not used, since it should be the default in
    # 64-bit mode.  (We need its effect for the various longlong.h
    # asm macros to be right of course.)

    # gcc64 was an early port of gcc to 64-bit mode, but should be
    # obsolete before too long.  We prefer plain gcc when it knows
    # 64-bits.
    MODE32 = "mode32"
    GCC_MODE32 = CompilerAndABI(compiler="gcc", abi=MODE32)
    options.compilers[GCC_MODE32] = default_gcc_options()._replace(
        flags=["-mpowerpc64"],
        flags_maybe=["-m32"],
        optional_flags=OrderedDict([
            ("cpu", cpu_flags_for_powerpc_gcc(host_cpu)),
            ("opt", ["-O2", "-O1"]),
        ])
    )
    options.abis[MODE32] = default_abi_options()._replace(
        mpn_search_path=mpn_search_path_for_powerpc_with_abi(host_cpu, MODE32),
        limb="longlong"
    )
    MODE64 = "mode64"
    GCC_MODE64 = CompilerAndABI(compiler="gcc", abi=MODE64)
    options.compilers[GCC_MODE64] = default_gcc_options()._replace(
        flags=["-m64"],
        optional_flags=OrderedDict([
            ("cpu", cpu_flags_for_powerpc_gcc(host_cpu)),
            ("opt", ["-O2", "-O1"])
        ])
    )
    options.abis[MODE64] = default_abi_options()._replace(
        mpn_search_path=mpn_search_path_for_powerpc_with_abi(host_cpu, MODE64),
        speed_cyclecounter_obj="powerpc64.lo",
        cyclecounter_size=0,
        testlist=["sizeof-long-8"]
    )
    GCC64_MODE64 = CompilerAndABI(compiler="gcc64", abi=MODE64)
    # Stepland : I don't understand which defaults actually end up being
    # used for gcc64 ...
    options.compilers[GCC64_MODE64] = default_gcc_options()
    options.abis[STANDARD_ABI] = options.abis[STANDARD_ABI]._replace(
        mpn_search_path=(
            extended_mpn_search_path_for_powerpc(host_cpu)
            + options.abis[STANDARD_ABI].mpn_search_path
        ),
    )
    return options

def options_for_powerpc(host: str, host_cpu: str) -> Options:
    # Darwin (powerpc-apple-darwin1.3) has it's hacked gcc installed as cc.
    # Our usual "gcc in disguise" detection means gcc_cflags etc here gets
    # used.

    # The darwin pre-compiling preprocessor is disabled with -no-cpp-precomp
    # since it doesn't like "__attribute__ ((mode (SI)))" etc in gmp-impl.h,
    # and so always ends up running the plain preprocessor anyway.  This could
    # be done in CPPFLAGS rather than CFLAGS, but there's not many places
    # preprocessing is done separately, and this is only a speedup, the normal
    # preprocessor gets run if there's any problems.

    # We used to use -Wa,-mppc with gcc, but can't remember exactly why.
    # Presumably it was for old versions of gcc where -mpowerpc doesn't put
    # the assembler in the right mode.  In any case -Wa,-mppc is not good, for
    # instance -mcpu=604 makes recent gcc use -m604 to get access to the
    # "fsel" instruction, but a -Wa,-mppc overrides that, making code that
    # comes out with fsel fail.

    # (Note also that the darwin assembler doesn't accept "-mppc", so any
    # -Wa,-mppc was used only if it worked.  The right flag on darwin would be
    # "-arch ppc" or some such, but that's already the default.)
    options = default_options()._replace(
        defines={"HAVE_HOST_CPU_FAMILY_powerpc": None}
    )
    options.compilers[CC] = options.compilers[CC]._replace(flags=["-O2"])
    options.compilers[GCC] = options.compilers[GCC]._replace(
        flags_maybe=["-m32"],
        optional_flags=OrderedDict([
            ("precomp", ["-no-cpp-precomp"]),
            ("subtype", ["-force_cpusubtype_ALL"]),  # for vmx on darwin
            ("asm", []),
            ("cpu", cpu_flags_for_powerpc_gcc(host_cpu)),
        ])
    )
    options.abis[STANDARD_ABI] = options.abis[STANDARD_ABI]._replace(
        mpn_search_path=mpn_search_path_for_powerpc(host_cpu),
        # grab this object, though it's not a true cycle counter routine
        speed_cyclecounter_obj="powerpc.lo",
        cyclecounter_size=0
    )
    if match(host, "*-*-aix*"):
        options.compilers[GCC] = options.compilers[GCC]._replace(
            flags_maybe=["-maix32"],
        )
        options.abis[STANDARD_ABI] = options.abis[STANDARD_ABI]._replace(
            ar_flags=["-X32"],
            nm_flags=["-X32"]
        )
        XLC = CompilerAndABI(compiler="xlc", abi=STANDARD_ABI)
        options.compilers[XLC] = empty_compiler_options()._replace(
            flags=["-O2", "-qmaxmem=20000"],
            flags_maybe=["-q32"]
        )
        options.compilers[XLC].optional_flags["arch"] = arch_flags_for_powerpc_xlc(host_cpu)
    
    # POWERPC64_PATTERN
    if match(
        host,
        "powerpc64-*-*",
        "powerpc64le-*-*",
        "powerpc620-*-*",
        "powerpc630-*-*",
        "powerpc970-*-*",
        "power[3-9]-*-*"
    ):
        if match(host, "*-*-aix*"):
            return options_for_powerpc_aix_64(options, host_cpu)
        elif match(host, "*-*-darwin*"):
            return options_for_powerpc_darwin_64(options, host_cpu)
        elif match(host, "*-*-linux*", "*-*-*bsd*"):
            return options_for_powerpc_linux_64(options, host_cpu)
    
    return options

def cpu_flags_for_power32(host: str) -> List[str]:
    # gcc 2.7.2 knows rios1, rios2, rsc

    # -mcpu=rios2 can tickle an AIX assembler bug (see GMP_PROG_CC_WORKS) so
    # there needs to be a fallback to just -mpower.
    if match(host, "power-*-*"):
        return ["-mcpu=power", "-mpower"]
    elif match(host, "power1-*-*"):
        return ["-mcpu=rios1", "-mpower"]
    elif match(host, "power2-*-*"):
        return ["-mcpu=rios2", "-mpower"]
    elif match(host, "power2sc-*-*"):
        return ["-mcpu=rsc", "-mpower"]
    else:
        return []

def options_for_power32(host: str, assembly: bool) -> Options:
    # POWER 32-bit
    options = default_options()._replace(
        compilers={GCC: default_gcc_options()._replace(
            optional_flags=OrderedDict([
                ("cpu", cpu_flags_for_power32(host))
            ])
        )},
        defines={"HAVE_HOST_CPU_FAMILY_power": "1"}
    )

    if assembly:
        options.abis[STANDARD_ABI] = options.abis[STANDARD_ABI]._replace(
            mpn_search_path=["power"],
            mpn_extra_functions=["udiv_w_sdiv"]
        )
    
    if match(host, "*-*-aix*"):
        XLC = CompilerAndABI(compiler="xlc", abi=STANDARD_ABI)
        options.compilers[XLC] = empty_compiler_options()._replace(
            flags=["-O2", "-qarch=pwr", "-qmaxmem=20000"]
        )
    
    return options

def options_for_risc_v() -> Options:
    return default_options()._replace(
        compilers={GCC: default_gcc_options()},
        abis={STANDARD_ABI: default_abi_options()._replace(
            mpn_search_path=["riscv/64"]
        )}
    )

def cpu_id_for_ibm(host_cpu: str) -> Optional[str]:
    if match(host_cpu, "z900", "z900esa"):
        return "z900"
    elif match(host_cpu, "z990", "z990esa"):
        return "z990"
    elif match(host_cpu, "z9", "z9esa"):
        return "z9"
    elif match(host_cpu, "z10", "z10esa"):
        return "z10"
    elif match(host_cpu, "z196", "z196esa"):
        return "z196"
    else:
        return None

def gccarch_for_ibm(host_cpu: str) -> Optional[str]:
    if match(host_cpu, "z9", "z9esa"):
        return "z9-109"
    else:
        return cpu_id_for_ibm(host_cpu)


def arch_flags_for_ibm_gcc(host_cpu: str) -> List[str]:
    gccarch = gccarch_for_ibm(host_cpu)
    if gccarch is None:
        return []
    else:
        return ["-march=" + gccarch]

S390_PATTERN = ["s390-*-*", "z900esa-*-*", "z990esa-*-*", "z9esa-*-*", "z10esa-*-*", "z196esa-*-*"]
S390X_PATTERN = ["s390x-*-*", "z900-*-*", "z990-*-*", "z9-*-*", "z10-*-*", "z196-*-*"]

def options_for_ibm(host: str, host_cpu: str, assembly: bool, profiling: str) -> Options:
    options = default_options()
    options = omit_frame_pointer_if_needed(options, profiling)
    options.compilers[GCC].optional_flags["arch"] = arch_flags_for_ibm_gcc(host_cpu)
    options.abis[STANDARD_ABI] = options.abis[STANDARD_ABI]._replace(
        mpn_search_path=["s390_32"]
    )
    if assembly:
        options.abis[STANDARD_ABI] = options.abis[STANDARD_ABI]._replace(
            mpn_extra_functions=["udiv_w_sdiv"]
        )
    options.compilers[GCC] = options.compilers[GCC]._replace(
        flags_maybe=["-m31"]
    )
    cpu_id = cpu_id_for_ibm(host_cpu)
    if cpu_id is not None:
        options.defines["HAVE_HOST_CPU_s390_" + cpu_id] = None
        options.defines["HAVE_HOST_CPU_s390_zarch"] = None
        options.abis[STANDARD_ABI] = options.abis[STANDARD_ABI]._replace(
            mpn_extra_functions=[]
        )
    
    if match(host, *S390X_PATTERN):
        options.compilers[GCC_64] = default_gcc_options()._replace(
            flags=default_gcc_flags() + ["-m64"]
        )
        options.compilers[GCC_64].optional_flags["arch"] = arch_flags_for_ibm_gcc(host_cpu)
        options.abis[STANDARD_ABI] = options.abis[STANDARD_ABI]._replace(
            mpn_search_path=[
                "s390_64/" + host_cpu,
                "s390_64"
            ],
            mpn_extra_functions=[]
        )
    
    return options

def options_for_sh() -> Options:
    return default_options()._replace(
        abis={STANDARD_ABI: default_abi_options()._replace(
            mpn_search_path=["sh"]
        )}
    )

def options_for_sh2() -> Options:
    return default_options()._replace(
        abis={STANDARD_ABI: default_abi_options()._replace(
            mpn_search_path=["sh/sh2", "sh"]
        )}
    )

def mpn_search_path_for_sparc(host_cpu: str) -> List[str]:
    if match(host_cpu, "sparcv8", "microsparc", "turbosparc"):
        return ["sparc32/v8", "sparc32"]
    elif match(host_cpu, "supersparc"):
        return ["sparc32/v8/supersparc", "sparc32/v8", "sparc32"]
    elif match(host_cpu, "sparc64", "sparcv9*", "ultrasparc", "ultrasparc[234]*"):
        return ["sparc32/v9", "sparc32/v8", "sparc32"]
    elif match(host_cpu, "ultrasparct[12345]"):
        return ["sparc32/ultrasparct1", "sparc32/v8", "sparc32"]
    else:
        return ["sparc32"]

def cpu_flags_for_spark_gcc(host_cpu: str) -> List[str]:
    # gcc 2.7.2 knows -mcypress, -msupersparc, -mv8, -msparclite.
    # gcc 2.95 knows -mcpu= v7, hypersparc, sparclite86x, f930, f934,
    #   sparclet, tsc701, v9, ultrasparc.  A warning is given that the
    #   plain -m forms will disappear.
    # gcc 3.3 adds ultrasparc3.
    if match(host_cpu, "supersparc*"):
        return ["-mcpu=supersparc", "-msupersparc"]
    elif match(host_cpu, "sparcv8", "microsparc*", "turbosparc", "hypersparc*"):
        return ["-mcpu=v8", "-mv8"]
    elif match(host_cpu, "sparc64", "sparcv9*"):
        return ["-mcpu=v9"]
    elif match(host_cpu, "ultrasparc1", "ultrasparc2*"):
        return ["-mcpu=ultrasparc", "-mcpu=v9"]
    elif match(host_cpu, "ultrasparc[34]"):
        return ["-mcpu=ultrasparc3", "-mcpu=ultrasparc", "-mcpu=v9"]
    elif match(host_cpu, "ultrasparct[12]"):
        return ["-mcpu=niagara", "-mcpu=v9"]
    elif match(host_cpu, "ultrasparct3"):
        return ["-mcpu=niagara3", "-mcpu=niagara", "-mcpu=v9"]
    elif match(host_cpu, "ultrasparct[45]"):
        return ["-mcpu=niagara4", "-mcpu=niagara3", "-mcpu=niagara", "-mcpu=v9"]
    else:
        return ["-mcpu=v7", "-mcypress"]

def asm_flags_for_spark_gcc(host_cpu: str) -> List[str]:
    if match(host_cpu, "supersparc*", "sparcv8", "microsparc*", "turbosparc", "hypersparc*"):
        return ["-Wa,-Av8", "-Wa,-xarch=v8"]
    else:
        return []

def asm_flags_for_spark_gcc_32(host_cpu: str) -> List[str]:
    if match(host_cpu, "sparc64", "sparcv9*"):
        return ["-Wa,-Av8", "-Wa,-xarch=v8plus"]
    elif match(host_cpu, "ultrasparc1", "ultrasparc2*"):
        return ["-Wa,-Av8plusa", "-Wa,-xarch=v8plusa"]
    elif match(host_cpu, "ultrasparc[34]"):
        return ["-Wa,-Av8plusb", "-Wa,-xarch=v8plusb"]
    elif match(host_cpu, "ultrasparct[12]"):
        return ["-Wa,-Av8plusc", "-Wa,-xarch=v8plusc"]
    elif match(host_cpu, "ultrasparct[345]"):
        return ["-Wa,-Av8plusd", "-Wa,-xarch=v8plusd"]
    else:
        return []    

def asm_flags_for_spark_gcc_64(host_cpu: str) -> List[str]:
    if match(host_cpu, "sparc64", "sparcv9*"):
        return ["-Wa,-Av9", "-Wa,-xarch=v9"]
    elif match(host_cpu, "ultrasparc1", "ultrasparc2*"):
        return ["-Wa,-Av9a", "-Wa,-xarch=v9a"]
    elif match(host_cpu, "ultrasparc[34]"):
        return ["-Wa,-Av9b", "-Wa,-xarch=v9b"]
    elif match(host_cpu, "ultrasparct[12]"):
        return ["-Wa,-Av9c", "-Wa,-xarch=v9c"]
    elif match(host_cpu, "ultrasparct[345]"):
        return ["-Wa,-Av9d", "-Wa,-xarch=v9d"]
    else:
        return []     

def arch_flags_for_spark_sun_cc(host_cpu: str) -> List[str]:
    if match(host_cpu, "sparcv8", "microsparc*", "supersparc*", "turbosparc", "hypersparc*"):
        return ["-xarch=v8"]
    elif match(host_cpu, "ultrasparct[345]"):
        return ["-xarch=v8plusd"]
    elif match(host_cpu, "sparc64", "sparcv9*", "ultrasparc*"):
        return ["-xarch=v8plus"]
    else:
        return ["-xarch=v7"]

def cpu_flags_for_spark_sun_cc(host_cpu: str) -> List[str]:
    # SunOS cc doesn't know -xchip and doesn't seem to have an equivalent.
    # SunPRO cc 5 recognises -xchip=generic, old, super, super2, micro,
    #   micro2, hyper, hyper2, powerup, ultra, ultra2, ultra2i.
    # SunPRO cc 6 adds -xchip=ultra2e, ultra3cu.
    if match(host_cpu, "supersparc*"):
        return ["-xchip=super"]
    elif match(host_cpu, "microsparc*"):
        return ["-xchip=micro"]
    elif match(host_cpu, "turbosparc"):
        return ["-xchip=micro2"]
    elif match(host_cpu, "hypersparc*"):
        return ["-xchip=hyper"]
    elif match(host_cpu, "ultrasparc"):
        return ["-xchip=ultra"]
    elif match(host_cpu, "ultrasparc2"):
        return ["-xchip=ultra2", "-xchip=ultra"]
    elif match(host_cpu, "ultrasparc2i"):
        return ["-xchip=ultra2i", "-xchip=ultra2", "-xchip=ultra"]
    elif match(host_cpu, "ultrasparc3"):
        return ["-xchip=ultra3", "-xchip=ultra"]
    elif match(host_cpu, "ultrasparc4"):
        return ["-xchip=ultra4", "-xchip=ultra3", "-xchip=ultra"]
    elif match(host_cpu, "ultrasparct1"):
        return ["-xchip=ultraT1"]
    elif match(host_cpu, "ultrasparct2"):
        return ["-xchip=ultraT2", "-xchip=ultraT1"]
    elif match(host_cpu, "ultrasparct3"):
        return ["-xchip=ultraT3", "-xchip=ultraT2"]
    elif match(host_cpu, "ultrasparct4"):
        return ["-xchip=T4"]
    elif match(host_cpu, "ultrasparct5"):
        return ["-xchip=T5", "-xchip=T4"]
    else:
        return ["-xchip=generic"]

def gcc_32_options_for_spark(host_cpu: str) -> CompilerOptions:
    # Note it's GCC_32 and not GCC because the latter would be used in the
    # 64-bit ABI on systems like "*bsd" where abilist="64" only.
    options = default_gcc_options()._replace(
        flags_maybe=["-m32"]
    )
    options.optional_flags["cpu"] = cpu_flags_for_spark_gcc(host_cpu)
    options.optional_flags["asm"] = asm_flags_for_spark_gcc_32(host_cpu) 
    return options   

def gcc_64_options_for_spark(host_cpu: str) -> CompilerOptions:
    options = default_gcc_options()._replace(
        flags=default_gcc_flags()+["-m64", "-mptr64"],
        ld_flags=["-Wc,-m64"]
    )
    options.optional_flags["cpu"] = cpu_flags_for_spark_gcc(host_cpu)
    options.optional_flags["asm"] = asm_flags_for_spark_gcc_64(host_cpu)
    return options

def mpn_search_path_for_spark64(host_cpu: str) -> List[str]:
    if match(host_cpu, "ultrasparc", "ultrasparc2", "ultrasparc2i"):
        return ["sparc64/ultrasparc1234", "sparc64"]
    elif match(host_cpu, "ultrasparc[34]"):
        return ["sparc64/ultrasparc34", "sparc64/ultrasparc1234", "sparc64"]
    elif match(host_cpu, "ultrasparct[12]"):
        return ["sparc64/ultrasparct1", "sparc64"]
    elif match(host_cpu, "ultrasparct3"):
        return ["sparc64/ultrasparct3", "sparc64"]
    elif match(host_cpu, "ultrasparct[45]"):
        return ["sparc64/ultrasparct45", "sparc64/ultrasparct3", "sparc64"]
    else:
        return ["sparc64"]

def flags_for_sun_cc_64(host_cpu: str) -> List[str]:
    # Sun cc.

    # We used to have -fast and some fixup options here, but it
    # recurrently caused problems with miscompilation.  Of course,
    # -fast is documented as miscompiling things for the sake of speed.
    if match(host_cpu, "ultrasparct[345]"):
        return default_cc_flags() + ["-xO3", "-xarch=v9d"]
    else:
        return ["-xO3", "-xarch=v9"]

def sun_cc_64_for_spark(host_cpu: str) -> CompilerOptions:
    options = default_cc_options()._replace(
        flags=flags_for_sun_cc_64(host_cpu)
    )
    options.optional_flags["cpu"] = cpu_flags_for_spark_sun_cc(host_cpu)
    return options

def options_for_64_bits_spark(options: Options, host: str, host_cpu: str) -> Options:
    options.compilers[GCC_64] = gcc_64_options_for_spark(host_cpu)
    options.abis["64"] = default_abi_options()._replace(
        mpn_search_path=mpn_search_path_for_spark64(host_cpu),
        testlist=["sizeof-long-8"],
        speed_cyclecounter_obj="sparcv9.lo",
        cyclecounter_size=2
    )
    if match(host, "*-*-solaris*"):
        options.compilers[CC_64] = sun_cc_64_for_spark(host_cpu)
    
    return options

def options_for_sparc(host: str, host_cpu: str) -> Options:
    # sizeof(long)==4 or 8 is tested, to ensure we get the right ABI.  We've
    # had various bug reports where users have set CFLAGS for their desired
    # mode, but not set our ABI.  For some reason it's sparc where this
    # keeps coming up, presumably users there are accustomed to driving the
    # compiler mode that way.  The effect of our testlist setting is to
    # reject ABI=64 in favour of ABI=32 if the user has forced the flags to
    # 32-bit mode.
    options = default_options()._replace(
        testlist=["sizeof-long-4"],
        gmp_include_mpn=["sparc32/sparc-defs.m4"]
    )
    options.compilers[GCC].optional_flags["cpu"] = cpu_flags_for_spark_gcc(host_cpu)
    options.compilers[GCC].optional_flags["asm"] = asm_flags_for_spark_gcc(host_cpu)
    ACC = CompilerAndABI(compiler="acc", abi=STANDARD_ABI)
    options.compilers[ACC] = empty_compiler_options()
    options.abis[STANDARD_ABI] = options.abis[STANDARD_ABI]._replace(
        mpn_search_path=mpn_search_path_for_sparc(host_cpu)
    )
    
    # SunPRO cc and acc, and SunOS bundled cc
    if match(host, "*-*-solaris*", "*-*-sunos*"):
        # Note no -g, it disables all optimizations.
        options.compilers[CC] = empty_compiler_options()
        # SunOS <= 4 cc doesn't know -xO3, fallback to -O2.
        options.compilers[CC].optional_flags["opt"] = ["-xO3", "-O2"]
        # SunOS cc doesn't know -xarch, apparently always generating v7
        # code, so make this optional
        options.compilers[CC].optional_flags["arch"] = arch_flags_for_spark_sun_cc(host_cpu)
        options.compilers[CC].optional_flags["cpu"] = cpu_flags_for_spark_sun_cc(host_cpu)

    if match(host_cpu, "sparc64", "sparcv9*", "ultrasparc*"):
        if match(host, "*-*-solaris2.[0-6]", "*-*-solaris2.[0-6].*"):
            # Solaris 6 and earlier cannot run ABI=64 since it doesn't save
            # registers properly, so ABI=32 is left as the only choice.
            options.compilers[GCC_32] = gcc_32_options_for_spark(host_cpu)
            options.abis["32"] = default_abi_options()._replace(
                speed_cyclecounter_obj="sparcv9.lo",
                cyclecounter_size=2
            )
        elif match(host, "*-*-*bsd*"):
            # BSD sparc64 ports are 64-bit-only systems, so ABI=64 is the only
            # choice.  In fact they need no special compiler flags, gcc -m64
            # is the default, but it doesn't hurt to add it.  v9 CPUs always
            # use the sparc64 port, since the plain 32-bit sparc ports don't
            # run on a v9.
            options = options_for_64_bits_spark(options, host, host_cpu)
        else:
            # For all other systems, we try both 64 and 32.

            # GNU/Linux sparc64 has only recently gained a 64-bit user mode.
            # In the past sparc64 meant a v9 cpu, but there were no 64-bit
            # operations in user mode.  We assume that if "gcc -m64" works
            # then the system is suitable.  Hopefully even if someone attempts
            # to put a new gcc and/or glibc on an old system it won't run.
            options.compilers[GCC_32] = gcc_32_options_for_spark(host_cpu)
            options.abis["32"] = default_abi_options()._replace(
                speed_cyclecounter_obj="sparcv9.lo",
                cyclecounter_size=2
            )
            options = options_for_64_bits_spark(options, host, host_cpu)

    return options

def options_for_vax(assembly: bool, profiling: str) -> Options:
    options = default_options()
    options = omit_frame_pointer_if_needed(options, profiling)
    if assembly:
        options.abis[STANDARD_ABI] = options.abis[STANDARD_ABI]._replace(
            mpn_extra_functions=["udiv_w_sdiv"]
        )
    return options

def options_for_vax_elf(assembly: bool, profiling: str) -> Options:
    # Use elf conventions (i.e., '%' register prefix, no global prefix)
    return options_for_vax(assembly, profiling)._replace(
        gmp_include_mpn=["vax/elf.m4"]
    )

def cpu_has_mulx_x86(host_cpu: str) -> bool:
    return match(
        host_cpu,
        "excavator", "bd4", "excavatornoavx", "bd4noavx",
        "zen", "zennoavx",
        "zen2", "zen2noavx", "zen3", "zen3noavx",
        "coreihwl", "coreihwlnoavx", "haswell", "haswellnoavx",
        "coreibwl", "coreibwlnoavx", "broadwell", "broadwellnoavx",
        "skylake", "skylakenoavx", "kabylake", "kabylakenoavx"
    )

def cpu_flags_for_x86_gcc(host_cpu: str) -> List[str]:
    if match(host_cpu, "i386*"):
        return ["-mtune=i386", "-mcpu=i386", "-m386"]
    elif match(host_cpu, "i486*"):
        return ["-mtune=i486", "-mcpu=i486", "-m486"]
    elif match(host_cpu, "i586", "pentium"):
        return ["-mtune=pentium", "-mcpu=pentium", "-m486"]
    elif match(host_cpu, "pentiummmx"):
        return ["-mtune=pentium-mmx", "-mcpu=pentium-mmx", "-mcpu=pentium", "-m486"]
    elif match(host_cpu, "i686", "pentiumpro"):
        return ["-mtune=pentiumpro", "-mcpu=pentiumpro", "-mcpu=i486", "-m486"]
    elif match(host_cpu, "pentium2"):
        return ["-mtune=pentium2", "-mcpu=pentium2", "-mcpu=pentiumpro", "-mcpu=i486", "-m486"]
    elif match(host_cpu, "pentium3"):
        return ["-mtune=pentium3", "-mcpu=pentium3", "-mcpu=pentiumpro", "-mcpu=i486", "-m486"]
    elif match(host_cpu, "pentiumm"):
        return ["-mtune=pentium3", "-mcpu=pentium3", "-mcpu=pentiumpro", "-mcpu=i486", "-m486"]
    elif match(host_cpu, "k6"):
        return ["-mtune=k6", "-mcpu=k6", "-mcpu=i486", "-m486"]
    elif match(host_cpu, "k62"):
        return ["-mtune=k6-2", "-mcpu=k6-2", "-mcpu=k6", "-mcpu=i486", "-m486"]
    elif match(host_cpu, "k63"):
        return ["-mtune=k6-3", "-mcpu=k6-3", "-mcpu=k6", "-mcpu=i486", "-m486"]
    elif match(host_cpu, "geode"):
        return ["-mtune=k6-3", "-mcpu=k6-3", "-mcpu=k6", "-mcpu=i486", "-m486"]
    elif match(host_cpu, "athlon"):
        return ["-mtune=athlon", "-mcpu=athlon", "-mcpu=pentiumpro", "-mcpu=i486", "-m486"]
    elif match(host_cpu, "i786", "pentium4"):
        return ["-mtune=pentium4", "-mcpu=pentium4", "-mcpu=pentiumpro", "-mcpu=i486", "-m486"]
    elif match(host_cpu, "viac32"):
        return ["-mtune=c3-2", "-mcpu=c3-2", "-mcpu=i486", "-m486"]
    elif match(host_cpu, "viac3*"):
        return ["-mtune=c3", "-mcpu=c3", "-mcpu=i486", "-m486"]
    elif match(host_cpu, "athlon64", "k8", "x86_64"):
        return ["-mtune=k8", "-mcpu=athlon", "-mcpu=pentiumpro", "-mcpu=i486", "-m486"]
    elif match(host_cpu, "k10"):
        return ["-mtune=amdfam10", "-mtune=k8"]
    elif match(host_cpu, "bobcat"):
        return ["-mtune=btver1", "-mtune=amdfam10", "-mtune=k8"]
    elif match(host_cpu, "jaguar", "jaguarnoavx"):
        return ["-mtune=btver2", "-mtune=btver1", "-mtune=amdfam10", "-mtune=k8"]
    elif match(host_cpu, "bulldozer", "bd1", "bulldozernoavx", "bd1noavx"):
        return ["-mtune=bdver1", "-mtune=amdfam10", "-mtune=k8"]
    elif match(host_cpu, "piledriver", "bd2", "piledrivernoavx", "bd2noavx"):
        return ["-mtune=bdver2", "-mtune=bdver1", "-mtune=amdfam10", "-mtune=k8"]
    elif match(host_cpu, "steamroller", "bd3", "steamrollernoavx", "bd3noavx"):
        return ["-mtune=bdver3", "-mtune=bdver2", "-mtune=bdver1", "-mtune=amdfam10", "-mtune=k8"]
    elif match(host_cpu, "excavator", "bd4", "excavatornoavx", "bd4noavx"):
        return ["-mtune=bdver4", "-mtune=bdver3", "-mtune=bdver2", "-mtune=bdver1", "-mtune=amdfam10", "-mtune=k8"]
    elif match(host_cpu, "zen", "zennoavx"):
        return ["-mtune=znver1", "-mtune=amdfam10", "-mtune=k8"]
    elif match(host_cpu, "zen2", "zen2noavx", "zen3", "zen3noavx"):
        return ["-mtune=znver2", "-mtune=znver1", "-mtune=amdfam10", "-mtune=k8"]
    elif match(host_cpu, "core2"):
        return ["-mtune=core2", "-mtune=k8"]
    elif match(host_cpu, "corei", "coreinhm", "coreiwsm", "nehalem", "westmere"):
        return ["-mtune=nehalem", "-mtune=corei7", "-mtune=core2", "-mtune=k8"]
    elif match(host_cpu, "coreisbr", "coreisbrnoavx", "coreiibr", "coreiibrnoavx", "sandybridge", "sandybridgenoavx", "ivybridge", "ivybridgenoavx"):
        return ["-mtune=sandybridge", "-mtune=corei7", "-mtune=core2", "-mtune=k8"]
    elif match(host_cpu, "coreihwl", "coreihwlnoavx", "haswell", "haswellnoavx"):
        return ["-mtune=haswell", "-mtune=corei7", "-mtune=core2", "-mtune=k8"]
    elif match(host_cpu, "coreibwl", "coreibwlnoavx", "broadwell", "broadwellnoavx"):
        return ["-mtune=broadwell", "-mtune=corei7", "-mtune=core2", "-mtune=k8"]
    elif match(host_cpu, "skylake", "skylakenoavx", "kabylake", "kabylakenoavx"):
        return ["-mtune=skylake", "-mtune=broadwell", "-mtune=corei7", "-mtune=core2", "-mtune=k8"]
    elif match(host_cpu, "atom"):
        return ["-mtune=atom", "-mtune=pentium3"]
    elif match(host_cpu, "silvermont"):
        return ["-mtune=slm", "-mtune=atom", "-mtune=pentium3"]
    elif match(host_cpu, "goldmont"):
        return ["-mtune=slm", "-mtune=atom", "-mtune=pentium3"]
    elif match(host_cpu, "nano"):
        return ["-mtune=nano"]
    else:
        return ["-mtune=i486", "-mcpu=i486", "-m486"]

def arch_flags_for_x86_gcc(host_cpu: str) -> List[str]:
    if match(host_cpu, "i386*"):
        return ["-march=i386"]
    elif match(host_cpu, "i486*"):
        return ["-march=i486"]
    elif match(host_cpu, "i586", "pentium"):
        return ["-march=pentium"]
    elif match(host_cpu, "pentiummmx"):
        return ["-march=pentium-mmx", "-march=pentium"]
    elif match(host_cpu, "i686", "pentiumpro"):
        return ["-march=pentiumpro", "-march=pentium"]
    elif match(host_cpu, "pentium2"):
        return ["-march=pentium2", "-march=pentiumpro", "-march=pentium"]
    elif match(host_cpu, "pentium3"):
        return ["-march=pentium3", "-march=pentiumpro", "-march=pentium"]
    elif match(host_cpu, "pentiumm"):
        return ["-march=pentium3", "-march=pentiumpro", "-march=pentium"]
    elif match(host_cpu, "k6"):
        return ["-march=k6"]
    elif match(host_cpu, "k62"):
        return ["-march=k6-2", "-march=k6"]
    elif match(host_cpu, "k63"):
        return ["-march=k6-3", "-march=k6"]
    elif match(host_cpu, "geode"):
        return ["-march=k6-3", "-march=k6"]
    elif match(host_cpu, "athlon"):
        return ["-march=athlon", "-march=pentiumpro", "-march=pentium"]
    elif match(host_cpu, "i786", "pentium4"):
        return ["-march=pentium4", "-march=pentium4~-mno-sse2", "-march=pentiumpro", "-march=pentium"]
    elif match(host_cpu, "viac32"):
        return ["-march=c3-2", "-march=pentium3", "-march=pentiumpro", "-march=pentium"]
    elif match(host_cpu, "viac3*"):
        return ["-march=c3", "-march=pentium-mmx", "-march=pentium"]
    elif match(host_cpu, "athlon64", "k8", "x86_64"):
        return ["-march=k8", "-march=k8~-mno-sse2", "-march=athlon", "-march=pentiumpro", "-march=pentium"]
    elif match(host_cpu, "k10"):
        return ["-march=amdfam10", "-march=k8", "-march=k8~-mno-sse2"]
    elif match(host_cpu, "bobcat"):
        return ["-march=btver1", "-march=amdfam10", "-march=k8", "-march=k8~-mno-sse2"]
    elif match(host_cpu, "jaguar", "jaguarnoavx"):
        return ["-march=btver2", "-march=btver1", "-march=amdfam10", "-march=k8", "-march=k8~-mno-sse2"]
    elif match(host_cpu, "bulldozer", "bd1", "bulldozernoavx", "bd1noavx"):
        return ["-march=bdver1", "-march=amdfam10", "-march=k8", "-march=k8~-mno-sse2"]
    elif match(host_cpu, "piledriver", "bd2", "piledrivernoavx", "bd2noavx"):
        return ["-march=bdver2", "-march=bdver1", "-march=amdfam10", "-march=k8", "-march=k8~-mno-sse2"]
    elif match(host_cpu, "steamroller", "bd3", "steamrollernoavx", "bd3noavx"):
        return ["-march=bdver3", "-march=bdver2", "-march=bdver1", "-march=amdfam10", "-march=k8", "-march=k8~-mno-sse2"]
    elif match(host_cpu, "excavator", "bd4", "excavatornoavx", "bd4noavx"):
        return ["-march=bdver4", "-march=bdver3", "-march=bdver2", "-march=bdver1", "-march=amdfam10", "-march=k8", "-march=k8~-mno-sse2"]
    elif match(host_cpu, "zen", "zennoavx"):
        return ["-march=znver1", "-march=amdfam10", "-march=k8"]
    elif match(host_cpu, "zen2", "zen2noavx", "zen3", "zen3noavx"):
        return ["-march=znver2", "-march=znver1", "-march=amdfam10", "-march=k8"]
    elif match(host_cpu, "core2"):
        return ["-march=core2", "-march=core2~-mno-sse2", "-march=k8", "-march=k8~-mno-sse2"]
    elif match(host_cpu, "corei", "coreinhm", "coreiwsm", "nehalem", "westmere"):
        return ["-march=nehalem", "-march=corei7", "-march=core2", "-march=core2~-mno-sse2", "-march=k8", "-march=k8~-mno-sse2"]
    elif match(host_cpu, "coreisbr", "coreisbrnoavx", "coreiibr", "coreiibrnoavx", "sandybridge", "sandybridgenoavx", "ivybridge", "ivybridgenoavx"):
        return ["-march=sandybridge", "-march=corei7", "-march=core2", "-march=core2~-mno-sse2", "-march=k8", "-march=k8~-mno-sse2"]
    elif match(host_cpu, "coreihwl", "coreihwlnoavx", "haswell", "haswellnoavx"):
        return ["-march=haswell", "-march=corei7", "-march=core2", "-march=core2~-mno-sse2", "-march=k8", "-march=k8~-mno-sse2"]
    elif match(host_cpu, "coreibwl", "coreibwlnoavx", "broadwell", "broadwellnoavx"):
        return ["-march=broadwell", "-march=corei7", "-march=core2", "-march=core2~-mno-sse2", "-march=k8", "-march=k8~-mno-sse2"]
    elif match(host_cpu, "skylake", "skylakenoavx", "kabylake", "kabylakenoavx"):
        return ["-march=broadwell", "-march=corei7", "-march=core2", "-march=core2~-mno-sse2", "-march=k8", "-march=k8~-mno-sse2"]
    elif match(host_cpu, "atom"):			
        return ["-march=atom", "-march=pentium3"]
    elif match(host_cpu, "silvermont"):		
        return ["-march=slm", "-march=atom", "-march=pentium3"]
    elif match(host_cpu, "goldmont"):			
        return ["-march=slm", "-march=atom", "-march=pentium3"]
    elif match(host_cpu, "nano"):
        return ["-march=nano"]
    else:
        return ["-march=i486"]

def noavx_flags_for_x86_gcc(host: str) -> List[str]:
    # Disable AVX if the CPU part tells us AVX is unavailable, but also
    # unconditionally for NetBSD where they don't work but OSXSAVE is set
    # to claim the contrary.
    if match(host, "*noavx-*-*", "*-*-netbsd*"):
        return ["-mno-avx"]
    else:
        return []

def mpn_search_path_for_x86(host_cpu: str) -> List[str]:
    if match(host_cpu, "i386*"):
        return ["x86"]
    elif match(host_cpu, "i486*"):
        return ["x86/i486", "x86"]
    elif match(host_cpu, "i586", "pentium"):
        return ["x86/pentium", "x86"]
    elif match(host_cpu, "pentiummmx"):
        return ["x86/pentium/mmx", "x86/pentium", "x86/mmx", "x86"]
    elif match(host_cpu, "i686", "pentiumpro"):
        return ["x86/p6", "x86"]
    elif match(host_cpu, "pentium2"):
        return ["x86/p6/mmx", "x86/p6", "x86/mmx", "x86"]
    elif match(host_cpu, "pentium3"):
        return ["x86/p6/p3mmx", "x86/p6/mmx", "x86/p6", "x86/mmx", "x86"]
    elif match(host_cpu, "pentiumm"):
        return ["x86/p6/sse2", "x86/p6/p3mmx", "x86/p6/mmx", "x86/p6", "x86/mmx", "x86"]
    elif match(host_cpu, "k6"):
        return ["x86/k6/mmx", "x86/k6", "x86/mmx", "x86"]
    elif match(host_cpu, "k62"):
        return ["x86/k6/k62mmx", "x86/k6/mmx", "x86/k6", "x86/mmx", "x86"]
    elif match(host_cpu, "k63"):
        return ["x86/k6/k62mmx", "x86/k6/mmx", "x86/k6", "x86/mmx", "x86"]
    elif match(host_cpu, "geode"):
        return ["x86/geode", "x86/k6/k62mmx", "x86/k6/mmx", "x86/k6", "x86/mmx", "x86"]
    elif match(host_cpu, "athlon"):
        return ["x86/k7/mmx", "x86/k7", "x86/mmx", "x86"]
    elif match(host_cpu, "i786", "pentium4"):
        return ["x86/pentium4/sse2", "x86/pentium4/mmx", "x86/pentium4", "x86/mmx", "x86"]
    elif match(host_cpu, "viac32"):
        return ["x86/p6/p3mmx", "x86/p6/mmx", "x86/p6", "x86/mmx", "x86"]
    elif match(host_cpu, "viac3*"):
        return ["x86/pentium/mmx", "x86/pentium", "x86/mmx", "x86"]
    elif match(host_cpu, "athlon64", "k8", "x86_64"):
        return ["x86/k8", "x86/k7/mmx", "x86/k7", "x86/mmx", "x86"]
    elif match(host_cpu, "k10"):
        return ["x86/k10", "x86/k8", "x86/k7/mmx", "x86/k7", "x86/mmx", "x86"]
    elif match(host_cpu, "bobcat"):
        return ["x86/bt1", "x86/k7/mmx", "x86/k7", "x86/mmx", "x86"]
    elif match(host_cpu, "jaguar", "jaguarnoavx"):
        return ["x86/bt2", "x86/bt1", "x86/k7/mmx", "x86/k7", "x86/mmx", "x86"]
    elif match(host_cpu, "bulldozer", "bd1", "bulldozernoavx", "bd1noavx"):
        return ["x86/bd1", "x86/k7/mmx", "x86/k7", "x86/mmx", "x86"]
    elif match(host_cpu, "piledriver", "bd2", "piledrivernoavx", "bd2noavx"):
        return ["x86/bd2", "x86/bd1", "x86/k7/mmx", "x86/k7", "x86/mmx", "x86"]
    elif match(host_cpu, "steamroller", "bd3", "steamrollernoavx", "bd3noavx"):
        return ["x86/bd3", "x86/bd2", "x86/bd1", "x86/k7/mmx", "x86/k7", "x86/mmx", "x86"]
    elif match(host_cpu, "excavator", "bd4", "excavatornoavx", "bd4noavx"):
        return ["x86/bd4", "x86/bd3", "x86/bd2", "x86/bd1", "x86/k7/mmx", "x86/k7", "x86/mmx", "x86"]
    elif match(host_cpu, "zen", "zennoavx"):
        return ["x86/k7/mmx", "x86/k7", "x86/mmx", "x86"]
    elif match(host_cpu, "zen2", "zen2noavx", "zen3", "zen3noavx"):
        return ["x86/k7/mmx", "x86/k7", "x86/mmx", "x86"]
    elif match(host_cpu, "core2"):
        return ["x86/core2", "x86/p6/sse2", "x86/p6/p3mmx", "x86/p6/mmx", "x86/p6", "x86/mmx", "x86"]
    elif match(host_cpu, "corei", "coreinhm", "coreiwsm", "nehalem", "westmere"):
        return ["x86/coreinhm", "x86/p6/sse2", "x86/p6/p3mmx", "x86/p6/mmx", "x86/p6", "x86/mmx", "x86"]
    elif match(host_cpu, "coreisbr", "coreisbrnoavx", "coreiibr", "coreiibrnoavx", "sandybridge", "sandybridgenoavx", "ivybridge", "ivybridgenoavx"):
        return ["x86/coreisbr", "x86/p6/sse2", "x86/p6/p3mmx", "x86/p6/mmx", "x86/p6", "x86/mmx", "x86"]
    elif match(host_cpu, "coreihwl", "coreihwlnoavx", "haswell", "haswellnoavx"):
        return ["x86/coreihwl", "x86/coreisbr", "x86/p6/sse2", "x86/p6/p3mmx", "x86/p6/mmx", "x86/p6", "x86/mmx", "x86"]
    elif match(host_cpu, "coreibwl", "coreibwlnoavx", "broadwell", "broadwellnoavx"):
        return ["x86/coreihwl", "x86/coreisbr", "x86/p6/sse2", "x86/p6/p3mmx", "x86/p6/mmx", "x86/p6", "x86/mmx", "x86"]
    elif match(host_cpu, "skylake", "skylakenoavx", "kabylake", "kabylakenoavx"):
        return ["x86/coreihwl", "x86/coreisbr", "x86/p6/sse2", "x86/p6/p3mmx", "x86/p6/mmx", "x86/p6", "x86/mmx", "x86"]
    elif match(host_cpu, "atom"):			
        return ["x86/atom/sse2", "x86/atom/mmx", "x86/atom", "x86/mmx", "x86"]
    elif match(host_cpu, "silvermont"):		
        return ["x86/silvermont", "x86/atom/sse2", "x86/atom/mmx", "x86/atom", "x86/mmx", "x86"]
    elif match(host_cpu, "goldmont"):			
        return ["x86/goldmont", "x86/atom/sse2", "x86/atom/mmx", "x86/atom", "x86/mmx", "x86"]
    elif match(host_cpu, "nano"):
        return ["x86/nano", "x86/mmx", "x86"]
    else:
        return ["x86"]

def cpu_flags_for_x86_gcc_64(host_cpu: str) -> List[str]:
    if match(host_cpu, "i786", "pentium4"):
        return ["-mtune=nocona"]
    else:
        return []

def mpn_search_path_for_x86_64(host_cpu: str) -> List[str]:
    if match(
        host_cpu,
        "i386*",
        "i486*", "i586",
        "pentium",
        "pentiummmx", "i686",
        "pentiumpro",
        "pentium2",
        "pentium3",
        "pentiumm",
        "k6",
        "k62",
        "k63",
        "geode",
        "athlon",
        "viac32",
        "viac3*"
    ):
        return []
    elif match(host_cpu, "i786", "pentium4"):
        return ["x86_64/pentium4", "x86_64"]
    elif match(host_cpu, "athlon64", "k8", "x86_64"):
        return ["x86_64/k8", "x86_64"]
    elif match(host_cpu, "k10"):
        return ["x86_64/k10", "x86_64/k8", "x86_64"]
    elif match(host_cpu, "bobcat"):
        return ["x86_64/bt1", "x86_64/k10", "x86_64/k8", "x86_64"]
    elif match(host_cpu, "jaguar", "jaguarnoavx"):
        return ["x86_64/bt2", "x86_64/bt1", "x86_64/k10", "x86_64/k8", "x86_64"]
    elif match(host_cpu, "bulldozer", "bd1", "bulldozernoavx", "bd1noavx"):
        return ["x86_64/bd1", "x86_64/k10", "x86_64/k8", "x86_64"]
    elif match(host_cpu, "piledriver", "bd2", "piledrivernoavx", "bd2noavx"):
        return ["x86_64/bd2", "x86_64/bd1", "x86_64/k10", "x86_64/k8", "x86_64"]
    elif match(host_cpu, "steamroller", "bd3", "steamrollernoavx", "bd3noavx"):
        return ["x86_64/bd3", "x86_64/bd2", "x86_64/bd1", "x86_64/k10", "x86_64/k8", "x86_64"]
    elif match(host_cpu, "excavator", "bd4", "excavatornoavx", "bd4noavx"):
        return ["x86_64/bd4", "x86_64/bd3", "x86_64/bd2", "x86_64/bd1", "x86_64/k10", "x86_64/k8", "x86_64"]
    elif match(host_cpu, "zen", "zennoavx"):
        return ["x86_64/zen", "x86_64"]
    elif match(host_cpu, "zen2", "zen2noavx", "zen3", "zen3noavx"):
        return ["x86_64/zen2", "x86_64/zen", "x86_64"]
    elif match(host_cpu, "core2"):
        return ["x86_64/core2", "x86_64"]
    elif match(host_cpu, "corei", "coreinhm", "coreiwsm", "nehalem", "westmere"):
        return ["x86_64/coreinhm", "x86_64/core2", "x86_64"]
    elif match(host_cpu, "coreisbr", "coreisbrnoavx", "coreiibr", "coreiibrnoavx", "sandybridge", "sandybridgenoavx", "ivybridge", "ivybridgenoavx"):
        return ["x86_64/coreisbr", "x86_64/coreinhm", "x86_64/core2", "x86_64"]
    elif match(host_cpu, "coreihwl", "coreihwlnoavx", "haswell", "haswellnoavx"):
        return ["x86_64/coreihwl", "x86_64/coreisbr", "x86_64/coreinhm", "x86_64/core2", "x86_64"]
    elif match(host_cpu, "coreibwl", "coreibwlnoavx", "broadwell", "broadwellnoavx"):
        return ["x86_64/coreibwl", "x86_64/coreihwl", "x86_64/coreisbr", "x86_64/coreinhm", "x86_64/core2", "x86_64"]
    elif match(host_cpu, "skylake", "skylakenoavx", "kabylake", "kabylakenoavx"):
        return ["x86_64/skylake", "x86_64/coreibwl", "x86_64/coreihwl", "x86_64/coreisbr", "x86_64/coreinhm", "x86_64/core2", "x86_64"]
    elif match(host_cpu, "atom"):			
        return ["x86_64/atom", "x86_64"]
    elif match(host_cpu, "silvermont"):		
        return ["x86_64/silvermont", "x86_64/atom", "x86_64"]
    elif match(host_cpu, "goldmont"):			
        return ["x86_64/goldmont", "x86_64/silvermont", "x86_64/atom", "x86_64"]
    elif match(host_cpu, "nano"):
        return ["x86_64/nano", "x86_64"]
    else:
        return ["x86_64"]

X86_PATTERN = [
    "i?86*-*-*",
    "k[5-8]*-*-*",
    "pentium*-*-*",
    "athlon-*-*",
    "viac3*-*-*",
    "geode*-*-*",
    "atom-*-*"
]

X86_64_PATTERN = [
    "athlon64-*-*",
    "k8-*-*",
    "k10-*-*",
    "bobcat-*-*",
    "jaguar*-*-*",
    "bulldozer*-*-*",
    "piledriver*-*-*",
    "steamroller*-*-*",
    "excavator*-*-*",
    "zen*-*-*",
    "pentium4-*-*",
    "atom-*-*",
    "silvermont-*-*",
    "goldmont-*-*",
    "core2-*-*",
    "corei*-*-*",
    "x86_64-*-*",
    "nano-*-*",
    "nehalem*-*-*",
    "westmere*-*-*",
    "sandybridge*-*-*",
    "ivybridge*-*-*",
    "haswell*-*-*",
    "broadwell*-*-*",
    "skylake*-*-*",
    "kabylake*-*-*"
]

def options_from_x86(host: str, host_cpu: str, assembly: bool, profiling: str) -> Options:
    # AMD and Intel x86 configurations, including AMD64

    # Rumour has it gcc -O2 used to give worse register allocation than just
    # -O, but lets assume that's no longer true.

    # -m32 forces 32-bit mode on a bi-arch 32/64 amd64 build of gcc.  -m64 is
    # the default in such a build (we think), so -m32 is essential for ABI=32.
    # This is, of course, done for any $host_cpu, not just x86_64, so we can
    # get such a gcc into the right mode to cross-compile to say i486-*-*.

    # -m32 is not available in gcc 2.95 and earlier, hence cflags_maybe to use
    # it when it works.  We check sizeof(long)==4 to ensure we get the right
    # mode, in case -m32 has failed not because it's an old gcc, but because
    # it's a dual 32/64-bit gcc without a 32-bit libc, or whatever.
    options = default_options()
    options = omit_frame_pointer_if_needed(options, profiling)
    options.abis[STANDARD_ABI] = options.abis[STANDARD_ABI]._replace(
        mpn_search_path=mpn_search_path_for_x86(host_cpu),
        calling_conventions_objs=["x86call.lo", "x86check$U.lo"],
        # Availability of rdtsc is checked at run-time.
        speed_cyclecounter_obj="pentium.lo"
    )
    options.compilers[GCC_32] = default_gcc_options()._replace(
        flags_maybe=["-m32"]
    )
    # like seen previously, the original configure script creates a variable
    # icc_cflags_opt_maybe="-fp-model~precise"
    # but it doesn't seem to be used anywhere ???
    options.abis["32"] = default_abi_options()._replace(
        testlist=["sizeof-long-4"]
    )
    x86_has_mulx = cpu_has_mulx_x86(host_cpu)
    options.compilers[GCC].optional_flags["cpu"] = cpu_flags_for_x86_gcc(host_cpu)
    options.compilers[GCC].optional_flags["arch"] = arch_flags_for_x86_gcc(host_cpu)
    options.compilers[GCC].optional_flags["noavx"] = noavx_flags_for_x86_gcc(host)

    if not match(host, *X86_64_PATTERN):
        ICC = CompilerAndABI(compiler="icc", abi=STANDARD_ABI)
        options.compilers[ICC] = empty_compiler_options()._replace(
            flags=["-no-gcc"]
        )
        options.compilers[ICC].optional_flags["opt"] = ["-O3", "-O2", "-O1"]
    if match(host, *X86_64_PATTERN):
        options.compilers[GCC_64] = default_gcc_options()._replace(
            flags=default_gcc_flags() + ["-m64"]
        )
        options.compilers[GCC_64].optional_flags["cpu"] = (
            cpu_flags_for_x86_gcc(host_cpu) + cpu_flags_for_x86_gcc_64(host_cpu)
        )
        options.compilers[GCC_64].optional_flags["arch"] = arch_flags_for_x86_gcc(host_cpu)
        options.compilers[GCC_64].optional_flags["noavx"] = noavx_flags_for_x86_gcc(host)
        options.abis["64"] = default_abi_options()._replace(
            mpn_search_path=mpn_search_path_for_x86_64(host_cpu),
            calling_conventions_objs=["amd64call.lo", "amd64check$U.lo"],
            speed_cyclecounter_obj="x86_64.lo",
            cyclecounter_size=2
        )

        X32_ABI = "x32"
        GCC_X32 = CompilerAndABI(compiler="gcc", abi=X32_ABI)
        options.compilers[GCC_X32] = default_gcc_options()._replace(
            flags=default_gcc_flags() + ["-mx32"]
        )
        options.compilers[GCC_X32].optional_flags["cpu"] = (
            cpu_flags_for_x86_gcc(host_cpu) + cpu_flags_for_x86_gcc_64(host_cpu)
        )
        options.compilers[GCC_X32].optional_flags["arch"] = arch_flags_for_x86_gcc(host_cpu)
        options.compilers[GCC_X32].optional_flags["noavx"] = noavx_flags_for_x86_gcc(host)
        options.abis[X32_ABI] = default_abi_options()._replace(
            mpn_search_path=mpn_search_path_for_x86_64(host_cpu),
            calling_conventions_objs=["amd64call.lo", "amd64check$U.lo"],
            speed_cyclecounter_obj="x86_64.lo",
            cyclecounter_size=2,
            limb="longlong",
            testlist=["sizeof-long-4"],
        )
        CC_X32 = CompilerAndABI(compiler="cc", abi=X32_ABI)
        options.compilers[CC_X32] = default_cc_options()

        if assembly:
            options.abis["64"].mpn_extra_functions.append("invert_limb_table")
            options.abis[X32_ABI] = options.abis[X32_ABI]._replace(
                mpn_extra_functions=options.abis["64"].mpn_extra_functions
            )
        
        if match(host, "*-*-solaris*"):
            options.compilers[CC_64] = options.compilers[CC_64]._replace(
                flags=["-xO3", "-m64"]
            )
        elif match(host, "*-*-mingw*", "*-*-msys", "*-*-cygwin"):
            options.abis["64"] = options.abis["64"]._replace(
                limb="longlong",
                calling_conventions_objs=[]
            )
            options.defines["HOST_DOS64"] = "1"
    
    return options

def options_for_host(
    host: str,
    host_cpu: str,
    assembly: bool,
    profiling: str
) -> Options:
    if match(host, "alpha*-*-*"):
        return options_for_alpha(host, host_cpu, assembly)
    elif match(host, "*-cray-unicos*"):
        return options_for_cray()
    elif match(host, "arm*-*-*", "aarch64*-*-*"):
        return options_for_arm(host, host_cpu, profiling)
    elif match(host, "f30[01]-fujitsu-sysv*"):
        return options_for_fujitsu()
    elif match(host, "hppa*-*-*"):
        return options_for_hp(host, host_cpu)
    elif match(host, "ia64*-*-*", "itanium-*-*", "itanium2-*-*"):
        return options_for_itanium(host, host_cpu)
    elif match(host, "m68k-*-*", "m68[0-9][0-9][0-9]-*-*"):
        return options_for_motorola_68k(host_cpu, profiling) 
    elif match(host, "m88k*-*-*"):
        return options_for_motorola_88k()
    elif match(host, "m88110*-*-*"):
        return options_for_motorola_88110()
    elif match(host, "mips*-*-*"):
        return options_for_mips(host, host_cpu)
    elif match(host, "powerpc*-*-*", "power[3-9]-*-*"):
        return options_for_powerpc(host, host_cpu)
    elif match(host, "power-*-*", "power[12]-*-*", "power2sc-*-*"):
        return options_for_power32(host, assembly)
    elif match(host, "riscv64-*-*"):
        return options_for_risc_v()
    elif match(host, *S390_PATTERN, *S390X_PATTERN):
        return options_for_ibm(host, host_cpu, assembly, profiling)
    elif match(host, "sh-*-*"):
        return options_for_sh()
    elif match(host, "sh[2-4]-*-*"):
        return options_for_sh2()
    elif match(host, "*sparc*-*-*"):
        return options_for_sparc(host, host_cpu)
    elif match(host, "vax*-*-*elf*"):
        return options_for_vax_elf(assembly, profiling)
    elif match(host, "vax*-*-*"):
        return options_for_vax(assembly, profiling)
    elif match(host, *X86_PATTERN, *X86_64_PATTERN):
        return options_from_x86(host, host_cpu, assembly, profiling)
    else:
        return default_options()

def options_for(
    host: str,
    host_cpu: str,
    assembly: bool,
    profiling: str
) -> Options:
    options = options_for_host(host, host_cpu, assembly, profiling)
    # mingw can be built by the cygwin gcc if -mno-cygwin is added.  For
    # convenience add this automatically if it works.  Actual mingw gcc accepts
    # -mno-cygwin too, but of course is the default.  mingw only runs on the
    # x86s, but allow any CPU here so as to catch "none" too.
    if match(host, "*-*-mingw*", "*-*-msys"):
        options.compilers[GCC].optional_flags["nocygwin"] = ["-mno-cygwin"]
    
    return options

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True)
    parser.add_argument("--host-cpu", required=True)
    parser.add_argument("--assembly", action="store_true")
    parser.add_argument("--profiling", required=True)
    args = parser.parse_args()
    options = options_for(
        args.host,
        args.host_cpu,
        args.assembly,
        args.profiling
    )
    print(options)