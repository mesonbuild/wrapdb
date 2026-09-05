#!/bin/sh

WORKDIR=$1

shift

cd "$WORKDIR"

exec "$@"
