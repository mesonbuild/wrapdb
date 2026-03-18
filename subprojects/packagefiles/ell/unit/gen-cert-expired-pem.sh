#!/bin/sh -e

echo -n > cert-ca-index.txt
OUTDIR=`mktemp -d`
openssl ca -batch \
	-config "$4" -name example \
	-cert "$2" \
	-keyfile "$3" \
	-outdir $OUTDIR \
	-rand_serial -extensions cert_ext \
	-extfile "$5" -md sha256 \
	-startdate 000101120000Z -enddate 010101120000Z \
	-preserveDN -notext -in "$1" -out "$6"
rm -rf $OUTDIR cert-ca-index.txt*
