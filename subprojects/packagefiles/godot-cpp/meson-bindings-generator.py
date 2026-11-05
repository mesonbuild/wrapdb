#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path
from binding_generator import generate_bindings


def parse_arguments():
    parser = ArgumentParser(
        description="Generate godot-cpp classes for a specific godot version and floating point precision."
    )
    parser.add_argument("api_version", type=str)
    return parser.parse_args()


def main():
    arguments = parse_arguments()

    json_directory = Path("gdextension")
    api_json_filepath = (
        json_directory / f"extension_api-{arguments.api_version.replace('.', '-')}.json"
    )
    interface_json_filepath = json_directory / "gdextension_interface.json"

    generate_bindings(
        str(api_json_filepath),
        str(interface_json_filepath),
        use_template_get_node=True,
        bits="64",
        precision="single",
        output_dir=arguments.api_version,
    )


if __name__ == "__main__":
    main()
