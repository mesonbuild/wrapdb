import sys

EXTRA_CRYPTO = """\
WPACKET_allocate_bytes
WPACKET_cleanup
WPACKET_close
WPACKET_fill_lengths
WPACKET_finish
WPACKET_get_curr
WPACKET_get_length
WPACKET_get_total_written
WPACKET_init
WPACKET_init_static_len
WPACKET_memcpy
WPACKET_memset
WPACKET_put_bytes__
WPACKET_reserve_bytes
WPACKET_set_flags
WPACKET_start_sub_packet
WPACKET_start_sub_packet_len__
WPACKET_sub_allocate_bytes__
WPACKET_sub_memcpy__
WPACKET_sub_reserve_bytes__
ssl3_cbc_digest_record
ssl3_cbc_remove_padding_and_mac
tls1_cbc_remove_padding_and_mac
""".splitlines()

def main():
    import argparse
    p = argparse.ArgumentParser(description="Convert OpenSSL .num files into .def files")
    p.add_argument("--fixup-crypto", action="store_true", help="crypto.dll-specific fixups")
    args = p.parse_args()

    input = sys.stdin.read()
    lines = [line.split() for line in input.splitlines()]
    data = [tuple([name, ordinal] + tags.split(":")) for name, ordinal, _, tags in lines]

    print("EXPORTS")
    for name, ordinal, exists, system, _, tags, *_ in data:
        if exists != "EXIST":
            continue
        if system and not system.startswith("!"):
            continue
        if any(tag in "COMP CRYPTO_MDEBUG DGRAM EC_NISTP_64_GCC_128 EGD MD2 RC5 SSL3_METHOD UNIT_TEST".split() for tag in tags.split(",")):
            continue
        print("    {} @{}".format(name, ordinal))
    if args.fixup_crypto:
        for name in EXTRA_CRYPTO:
            print("    {}".format(name))

if __name__ == "__main__":
    sys.exit(main())
