inc = include_directories('include')

# The minimum set of files needed for lwIP.
core_src = files(
  'core/altcp.c',
  'core/altcp_alloc.c',
  'core/altcp_tcp.c',
  'core/def.c',
  'core/dns.c',
  'core/inet_chksum.c',
  'core/init.c',
  'core/ip.c',
  'core/mem.c',
  'core/memp.c',
  'core/netif.c',
  'core/pbuf.c',
  'core/raw.c',
  'core/stats.c',
  'core/sys.c',
  'core/tcp.c',
  'core/tcp_in.c',
  'core/tcp_out.c',
  'core/timeouts.c',
  'core/udp.c',
)
core4_src = files(
  'core/ipv4/acd.c',
  'core/ipv4/autoip.c',
  'core/ipv4/dhcp.c',
  'core/ipv4/etharp.c',
  'core/ipv4/icmp.c',
  'core/ipv4/igmp.c',
  'core/ipv4/ip4.c',
  'core/ipv4/ip4_addr.c',
  'core/ipv4/ip4_frag.c',
)
core6_src = files(
  'core/ipv6/dhcp6.c',
  'core/ipv6/ethip6.c',
  'core/ipv6/icmp6.c',
  'core/ipv6/inet6.c',
  'core/ipv6/ip6.c',
  'core/ipv6/ip6_addr.c',
  'core/ipv6/ip6_frag.c',
  'core/ipv6/mld6.c',
  'core/ipv6/nd6.c',
)
# APIFILES: The files which implement the sequential and socket APIs.
api_src = files(
  'api/api_lib.c',
  'api/api_msg.c',
  'api/err.c',
  'api/if_api.c',
  'api/netbuf.c',
  'api/netdb.c',
  'api/netifapi.c',
  'api/sockets.c',
  'api/tcpip.c',
)
# Files implementing various generic network interface functions
netif_src = files('netif/bridgeif.c', 'netif/bridgeif_fdb.c', 'netif/ethernet.c')
if not get_option('exclude_slipif')
  netif_src += 'netif/slipif.c'
endif
# 6LoWPAN
sixlowpan_src = files(
  'netif/lowpan6.c',
  'netif/lowpan6_ble.c',
  'netif/lowpan6_common.c',
  'netif/zepif.c',
)
# PPP
ppp_src = files(
  'netif/ppp/auth.c',
  'netif/ppp/ccp.c',
  'netif/ppp/chap-md5.c',
  'netif/ppp/chap-new.c',
  'netif/ppp/chap_ms.c',
  'netif/ppp/demand.c',
  'netif/ppp/eap.c',
  'netif/ppp/ecp.c',
  'netif/ppp/eui64.c',
  'netif/ppp/fsm.c',
  'netif/ppp/ipcp.c',
  'netif/ppp/ipv6cp.c',
  'netif/ppp/lcp.c',
  'netif/ppp/magic.c',
  'netif/ppp/mppe.c',
  'netif/ppp/multilink.c',
  'netif/ppp/polarssl/arc4.c',
  'netif/ppp/polarssl/des.c',
  'netif/ppp/polarssl/md4.c',
  'netif/ppp/polarssl/md5.c',
  'netif/ppp/polarssl/sha1.c',
  'netif/ppp/ppp.c',
  'netif/ppp/pppapi.c',
  'netif/ppp/pppcrypt.c',
  'netif/ppp/pppoe.c',
  'netif/ppp/pppol2tp.c',
  'netif/ppp/pppos.c',
  'netif/ppp/upap.c',
  'netif/ppp/utils.c',
  'netif/ppp/vj.c',
)
# All LWIP files without apps
lwipcore_lib = library(
  'lwipcore',
  core_src,
  core4_src,
  core6_src,
  api_src,
  netif_src,
  sixlowpan_src,
  ppp_src,
  include_directories: inc,
  dependencies: [lwipopts_dep, lwipport_dep],
)
lwipcore_dep = declare_dependency(
  link_with: lwipcore_lib,
  include_directories: inc,
  dependencies: [lwipopts_dep, lwipport_dep],
)
meson.override_dependency('lwip-core', lwipcore_dep)

# SNMPv3 agent
snmp_src = files(
  'apps/snmp/snmp_asn1.c',
  'apps/snmp/snmp_core.c',
  'apps/snmp/snmp_mib2.c',
  'apps/snmp/snmp_mib2_icmp.c',
  'apps/snmp/snmp_mib2_interfaces.c',
  'apps/snmp/snmp_mib2_ip.c',
  'apps/snmp/snmp_mib2_snmp.c',
  'apps/snmp/snmp_mib2_system.c',
  'apps/snmp/snmp_mib2_tcp.c',
  'apps/snmp/snmp_mib2_udp.c',
  'apps/snmp/snmp_msg.c',
  'apps/snmp/snmp_netconn.c',
  'apps/snmp/snmp_pbuf_stream.c',
  'apps/snmp/snmp_raw.c',
  'apps/snmp/snmp_scalar.c',
  'apps/snmp/snmp_snmpv2_framework.c',
  'apps/snmp/snmp_snmpv2_usm.c',
  'apps/snmp/snmp_table.c',
  'apps/snmp/snmp_threadsync.c',
  'apps/snmp/snmp_traps.c',
  'apps/snmp/snmpv3.c',
)
# HTTP server + client
http_src = files(
  'apps/http/altcp_proxyconnect.c',
  'apps/http/fs.c',
  'apps/http/http_client.c',
  'apps/http/httpd.c',
)
# MAKEFSDATA HTTP server host utility
makefsdata_src = files('apps/http/makefsdata/makefsdata.c')
# IPERF server
iperf_src = files('apps/lwiperf/lwiperf.c')
# SMTP client
smtp_src = files('apps/smtp/smtp.c')
# SNTP client
sntp_src = files('apps/sntp/sntp.c')
# MDNS responder
mdns_src = files(
  'apps/mdns/mdns.c',
  'apps/mdns/mdns_domain.c',
  'apps/mdns/mdns_out.c',
)
# NetBIOS name server
netbios_src = files('apps/netbiosns/netbiosns.c')
# TFTP server files
tftp_src = files('apps/tftp/tftp.c')
# MQTT client files
mqtt_src = files('apps/mqtt/mqtt.c')
# LWIPAPPFILES: All LWIP APPs
lwipallapps_lib = library(
  'lwipallapps',
  snmp_src,
  http_src,
  iperf_src,
  smtp_src,
  sntp_src,
  mdns_src,
  netbios_src,
  tftp_src,
  mqtt_src,
  include_directories: inc,
  dependencies: [lwipopts_dep, lwipport_dep, lwipcore_dep],
)
lwipallapps_dep = declare_dependency(
  link_with: lwipallapps_lib,
  include_directories: inc,
  dependencies: [lwipopts_dep, lwipport_dep, lwipcore_dep],
)
meson.override_dependency('lwip-apps', lwipallapps_dep)

# ARM MBEDTLS related files of lwIP rep
lwipmbedtls_lib = library(
  'libmbedtls',
  files(
    'apps/altcp_tls/altcp_tls_mbedtls.c',
    'apps/altcp_tls/altcp_tls_mbedtls_mem.c',
    'apps/snmp/snmpv3_mbedtls.c',
  ),
  include_directories: inc,
  dependencies: [lwipopts_dep, lwipport_dep, lwipcore_dep],
)
lwipmbedtls_dep = declare_dependency(
  link_with: lwipmbedtls_lib,
  include_directories: inc,
  dependencies: [lwipopts_dep, lwipport_dep, lwipcore_dep],
)
meson.override_dependency('lwip-mbedtls', lwipmbedtls_dep)
