import argparse
from typing import NamedTuple, List, Optional

CompilerOptions = NamedTuple(
    "CompilerOptions",
    [
        ("c_flags", List[str]), # C flags for compiler
        ("c_flags_maybe", List[str]), # C flags for compiler, if they work
        ("cpp_flags"), # C++ flags for compiler
        ("optional_flag_sets", Dict[str, List[str]]),
        ("ld_flags", List[str]), # -Wc,-foo flags for libtool linking with compiler
    ],
)

MPNOptions = NamedTuple(
    "MPNOptions",
    [
        ("search_path", List[str]),
        ("extra_functions", List[str]),
    ],
)

ABIOptions = NamedTuple(
    "ABIOptions",
    [
        ("compiler", Dict[str, CompilerOptions]),
        ("ar_flags", List[str]), # extra flags for $AR
        ("nm_flags", List[str]), # extra flags for $NM
        ("limb", str), # limb size, can be "longlong"
        ("mpn", MPNOptions),
    ],
)

FatOptions = NamedTuple(
    "FatOptions",
    [
        ("mpn_search_path", List[str]), # fat binary mpn search path [if fat binary desired]
        ("function", List[str]),
        ("thresholds", List[str]),
    ],
)

Options = NamedTuple(
    "Options",
    [
        ("abi", Dict[str, ABIOptions]),
        ("fat", Optional[FatOptions]),
    ],
)

parser = argparse.ArgumentParser()
parser.add_argument("--cpu-family", type=str, required=True)
parser.add_argument("--cpu", type=str, required=True)
parser.add_argument("--assembly", type=str, required=True)
args = parser.parse_args()

