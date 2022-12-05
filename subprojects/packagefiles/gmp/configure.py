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
# generic abi identifier that usually defaults to the 32-bit one
STANDARD_ABI = "standard"

# common abi + compiler defintions
ANY_32 = CompilerAndABI(compiler="any", abi="32")
ANY_64 = CompilerAndABI(compiler="any", abi="64")
GCC = CompilerAndABI(compiler="gcc", abi=STANDARD_ABI)
GCC_32 = CompilerAndABI(compiler="gcc", abi="32")
GCC_64 = CompilerAndABI(compiler="gcc", abi="64")
CC = CompilerAndABI(compiler="cc", abi=STANDARD_ABI)
CC_64 = CompilerAndABI(compiler="cc", abi="64")

CompilerOptions = NamedTuple(
    "CompilerOptions"
    [
        ("flags", List[str]),
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
    ]
)

Options = NamedTuple(
    "Options",
    [
        ("compilers", Dict[CompilerAndABI, CompilerOptions]),
        ("abis", Dict[str, ABIOptions]),  # ABI name -> objs
        ("gmp_asm_syntax_testing", bool),
        ("speed_cyclecounter_obj", Optional[str])
        ("cyclecounter_size", int)
    ]
)

def default_gcc_flags() -> List[str]:
    return ["-O2", "-pedantic"]

def default_gcc_options() -> CompilerOptions:
    return CompilerOptions(
        flags=default_gcc_flags(),
        flags_maybe=[],
        optional_flags=OrderedDict(),
        testlist=[]
    )    


def default_cc_options() -> CompilerOptions:
    return CompilerOptions(
        flags=["-O"],
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
        speed_cyclecounter_obj=None,
        cyclecounter_size=2,
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
        options = options._replace(
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
        calling_conventions_objs=["arm32call.lo", "arm32check.lo"]
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

    options.compilers[ANY_32] = empty_compiler_options()._replace(
        testlist=["sizeof-void*-4"]
    )

    if arm_cpu_has_64_abi(host_cpu):
        options.abis["64"] = default_abi_options()._replace(
            mpn_search_path=mpn_search_path_for_arm_64(host_cpu),
            calling_conventions_objs=[]
        )
        options.compilers[CC_64] = default_cc_options()
        options.compilers[GCC_64] = default_gcc_options()._replace(
            optional_flags=OrderedDict([
                ("arch", options.compilers[GCC].optional_flags["arch"]),
                ("tune", options.compilers[GCC].optional_flags["tune"])
            ]),
            testlist=[]
        )
        options.compilers[ANY_64] = empty_compiler_options()._replace(
            testlist=["sizeof-void*-8"]
        )
        if match(host, "*-*-mingw*"):
            options.abis["64"] = options.abis["64"]._replace(limb="longlong")


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