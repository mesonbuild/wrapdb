#!/bin/sh

WORKDIR=$1
INPUT=$2
CMD=$3

cd "$WORKDIR"

go run $CMD -in-executable "$INPUT"
