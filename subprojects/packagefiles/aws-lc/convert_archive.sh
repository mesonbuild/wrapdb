#!/bin/sh

INPUT=$1
OUTPUT=$2

ar -t "$INPUT" | xargs ar rvs "$OUTPUT" > /dev/null
