#!/usr/bin/env python3
"""Build the libtommath PDF manual from LaTeX sources

This script is called by meson with the following environment variables set:
LATEX, PDFLATEX, MAKEINDEX

Only requires standard Python library - no external tools beyond LaTeX itself.
"""

import os
import sys
import shutil
import subprocess
import re
from datetime import datetime, timezone


def main():
    if len(sys.argv) != 4:
        print("Usage: build-manual.py INPUT OUTDIR OUTPUT", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    outdir = sys.argv[2]
    output_file = sys.argv[3]

    # Get tools from environment
    latex = os.environ.get('LATEX', 'latex')
    pdflatex = os.environ.get('PDFLATEX', 'pdflatex')
    makeindex = os.environ.get('MAKEINDEX', 'makeindex')

    # Convert paths to absolute before changing directories
    input_file = os.path.abspath(input_file)
    output_file = os.path.abspath(output_file)

    # Change to output directory
    os.chdir(outdir)

    # Copy input to bn.tex
    shutil.copy2(input_file, 'bn.tex')

    # Create backup with same timestamp
    shutil.copy2('bn.tex', 'bn.bak')

    # Get modification time of bn.tex and format for PDF
    mtime = os.stat('bn.tex').st_mtime
    dt = datetime.fromtimestamp(mtime, tz=timezone.utc)

    # Format as PDF date string: D:YYYYMMDDHHmmSS+HH'mm'
    # For UTC, timezone offset is +00'00'
    date_str = dt.strftime("D:%Y%m%d%H%M%S+00'00'")

    # Write deterministic PDF header
    with open('bn-deterministic.tex', 'w') as f:
        f.write(f"\\def\\fixedpdfdate{{{date_str}}}\n")
        f.write("\\pdfinfo{\n")
        f.write("  /CreationDate (\\fixedpdfdate)\n")
        f.write("  /ModDate (\\fixedpdfdate)\n")
        f.write("}\n")

        # Append original content
        with open('bn.tex', 'r') as orig:
            f.write(orig.read())

    # Replace bn.tex with deterministic version
    shutil.move('bn-deterministic.tex', 'bn.tex')

    # Restore original timestamp
    shutil.copystat('bn.bak', 'bn.tex')

    # Build the manual
    with open('bn.ind', 'w') as f:
        f.write('hello\n')

    subprocess.run([latex, 'bn'], stdout=subprocess.DEVNULL, check=True)
    subprocess.run([latex, 'bn'], stdout=subprocess.DEVNULL, check=True)
    subprocess.run([makeindex, 'bn'], check=True)
    subprocess.run([latex, 'bn'], stdout=subprocess.DEVNULL, check=True)
    subprocess.run([pdflatex, 'bn'], stdout=subprocess.DEVNULL, check=True)

    # Make PDF ID deterministic using Python
    with open('bn.pdf', 'rb') as f:
        pdf_data = f.read()

    # Replace /ID [<...> <...>] with /ID [<0> <0>]
    pdf_data = re.sub(rb'^/ID \[.*\]$', rb'/ID [<0> <0>]', pdf_data, flags=re.MULTILINE)

    with open('bn.pdf', 'wb') as f:
        f.write(pdf_data)

    # Rename to desired output name
    shutil.move('bn.pdf', output_file)

    # Cleanup
    shutil.move('bn.bak', 'bn.tex')

    cleanup_files = [
        'bn.aux', 'bn.dvi', 'bn.log', 'bn.idx',
        'bn.lof', 'bn.out', 'bn.toc', 'bn.ilg',
        'bn.ind', 'bn.tex'
    ]
    for f in cleanup_files:
        try:
            os.remove(f)
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    main()
