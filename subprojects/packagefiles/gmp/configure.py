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
    "CompilerOptions"
    [
        ("flags", List[str]),
        ("cpp_flags", List[str])
        ("flags_maybe", List[str]),
        ("optional_flags", OrderedDict[str, List[str]]),
        ("testlist", List[str])
    ],
)

ABIOptions = NamedTuple(
    "ABIOptions",
    [
        ("ar_flags", List[str]),
        ("nm_flags", List[str]),
        ("limb", Optional[str]),
        ("mpn_search_path", List[str]),
        ("mpn_extra_functions", List[str]),
        ("calling_conventions_objs", List[str]),
        ("speed_cyclecounter_obj", Optional[str]),
        ("cyclecounter_size", int),
        ("testlist", List[str]), # tests for any compiler with that abi
    ]
)

Options = NamedTuple(
    "Options",
    [
        ("compilers", Dict[CompilerAndABI, CompilerOptions]),
        ("abis", Dict[str, ABIOptions]),  # ABI name -> objs
        ("gmp_asm_syntax_testing", bool),
    ]
)

def default_gcc_flags() -> List[str]:
    return ["-O2", "-pedantic"]

def default_gcc_options() -> CompilerOptions:
    return CompilerOptions(
        flags=default_gcc_flags(),
        cpp_flags=[],
        flags_maybe=[],
        optional_flags=OrderedDict(),
        testlist=[]
    )    


def default_cc_options() -> CompilerOptions:
    return CompilerOptions(
        flags=["-O"],
        cpp_flags=[],
        flags_maybe=[],
        optional_flags=OrderedDict(),
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
    )

def empty_compiler_options() -> CompilerOptions:
    return CompilerOptions(
        flags=[],
        flags_maybe=[],
        optional_flags=OrderedDict(),
        testlist=[]
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
    elif match(host, "*-cray-unicos*"):
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
    options = default_options()
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
        return ()

def arm_cpu_has_64_abi(host_cpu: str) -> boolean:
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

def options_for_arm(host: str, host_cpu: str, profiling: str) -> Options:
    options = default_options()
    options.abis[STANDARD_ABI] = default_abi_options()._replace(
        mpn_search_path=mpn_search_path_for_arm(host_cpu),
        calling_conventions_objs=["arm32call.lo", "arm32check.lo"],
        testlist=["sizeof-void*-4"]
    )
    if profiling != "gprof":
        options.compilers[GCC] = options.compilers[GCC]._replace(
            flags=default_gcc_flags() + ["-fomit-frame-pointer"]
        )

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
    vcc_options = empty_compiler_options()._replace(flags="-g")
    abi_options = default_abi_options()._replace(
        mpn_search_path=["fujitsu"]
    )
    return default_options()._replace(
        compilers={
            GCC: default_gcc_options(),
            VCC: vcc_options
        },
        abis={STANDARD_ABI: abi_options}
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
        options.compiler[CC_20N] = empty_compiler_options()._replace(
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
            options.compiler[CC_20W] = empty_compiler_options()._replace(
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
        options.compiler[CC_32] = default_cc_options()._replace(
            flags=[],
            optional_flags=OrderedDict([("opt", ["+O2", "+O1"])])
        )

        # Must have +DD64 in CPPFLAGS to get the right __LP64__ for headers,
        # but also need it in CFLAGS for linking programs, since automake
        # only uses CFLAGS when linking, not CPPFLAGS.
        # FIXME: Maybe should use cc_64_ldflags for this, but that would
        # need GMP_LDFLAGS used consistently by all the programs.
        options.compiler[CC] = options.compiler[CC]._replace(
            flags=["+DD64"],
            cpp_flags=["+DD64"],
            optional_flags=OrderedDict([("opt", ["+O2", "+O1"])])
        )
        options.compiler[GCC] = options.compiler[GCC]._replace(
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
    options = default_options()
    if profiling != "gprof":
        options.compilers[GCC] = options.compilers[GCC]._replace(
            flags=default_gcc_flags() + ["-fomit-frame-pointer"]
        )
    
    options.compilers[GCC].optional_flags["arch"] = arch_flags_for_motorola_68k_gcc(host_cpu)
    options.abis[STANDARD_ABI]._replace(
        mpn_search_path=mpn_search_path_for_motorola_68k(host_cpu)
    )
    return options

def options_for_motorola_88k() -> Options:
    options = default_options()
    options.abi[STANDARD_ABI] = options.abi[STANDARD_ABI]._replace(
        mpn_search_path=["m88k"]
    )
    return options

def options_for_motorola_88110() -> Options:
    options = default_options()
    options.compilers[GCC] = options.compilers[GCC]._replace(
        flags=default_gcc_flags() + ["-m88110"]
    )
    options.abi[STANDARD_ABI] = options.abi[STANDARD_ABI]._replace(
        mpn_search_path=["m88k/mc88110", "m88k"]
    )
    return options

def options_for(
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
        return options_for_motorola_68k(host_cpu) 
    elif match(host, "m88k*-*-*"):
        return options_for_motorola_88k()
    elif match(host, "m88110*-*-*"):
        return options_for_motorola_88110()

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