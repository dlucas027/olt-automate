# Configuração na íntegra

```bash

---

ZXAN#show ru
ZXAN#show running-config 
Building configuration...
olleh
timestamp_write: 02:25:44 02/02/2025
config-version 2.1
!
crtv disable
!
load-balance enable
!
operator-mode NORMAL
!
system-forwarding-mode normal-mode
!
!
!
set-pnp enable
add-rack rackno 1 racktype C320Rack
add-shelf rackno 1 shelfno 1 shelftype C320_SHELF
add-card rackno 1 shelfno 1 slotno 1 GTGH
add-card rackno 1 shelfno 1 slotno 3 PRAM
add-subcard rackno 1 shelfno 1 slotno 4 subcardno 1 UCDC/3
!
ip tcp finwait-time 600 
ip tcp queuemax 5 
ip tcp synwait-time 30 
ip tcp window-size 2144 
!
urpf log off 
!
!
!
!
!
mac aging-time 300
mac monitor-period 10
mac usage-threshold 70
!
eth-switch max-frame-length  1600
port diaglog status-info disable
!
sdisk disable
!
auto-update backup disable
auto-update activate disable
!
!
!
!
!
gpon
  profile tcont 1G-UP type 5 fixed 64 assured 64 maximum 1048064
  profile traffic 1G-DOWN sir 1048064 pir 1048064
!
!
gpon
  onu profile vlan 100 tag-mode tag cvlan 100
  onu profile vlan 11 tag-mode tag cvlan 11
  onu profile vlan 13 tag-mode tag cvlan 13
  onu profile vlan 12 tag-mode tag cvlan 12
  onu profile vlan 14 tag-mode tag cvlan 14
!
!
epon
!
!
pon
  onu-type ZTE-F660 gpon
  onu-type ZTE-F660 gpon max-tcont 8
  onu-type ZTE-F660 gpon max-gemport 32
  onu-type ZTE-F660 gpon max-switch-perslot 8
  onu-type ZTE-F660 gpon max-flow-perswitch 8
  onu-type ZTE-F660 gpon max-iphost 5
  onu-type DLINK-MODELOX gpon
  onu-type DLINK-MODELOX gpon max-tcont 8
  onu-type DLINK-MODELOX gpon max-gemport 32
  onu-type DLINK-MODELOX gpon max-switch-perslot 8
  onu-type DLINK-MODELOX gpon max-flow-perswitch 8
  onu-type DLINK-MODELOX gpon max-iphost 5
  onu-type NOKIA_G1425GB gpon
  onu-type NOKIA_G1425GB gpon max-tcont 8
  onu-type NOKIA_G1425GB gpon max-gemport 32
  onu-type NOKIA_G1425GB gpon max-switch-perslot 8
  onu-type NOKIA_G1425GB gpon max-flow-perswitch 8
  onu-type NOKIA_G1425GB gpon max-iphost 5
  onu-type NOKIA_G1426GA gpon description 4xETH_2xWIFI
  onu-type NOKIA_G1426GA gpon max-tcont 8
  onu-type NOKIA_G1426GA gpon max-gemport 32
  onu-type VSOL-BRIDGE-1P gpon
  onu-type VSOL-BRIDGE-1P gpon max-tcont 8
  onu-type VSOL-BRIDGE-1P gpon max-gemport 32
  onu-type VSOL-BRIDGE-1P gpon max-switch-perslot 8
  onu-type VSOL-BRIDGE-1P gpon max-flow-perswitch 8
  onu-type VSOL-BRIDGE-1P gpon max-iphost 5
  onu-type-if ZTE-F660 eth_0/1
  onu-type-if DLINK-MODELOX eth_0/1
  onu-type-if NOKIA_G1425GB eth_0/1
  onu-type-if VSOL-BRIDGE-1P eth_0/1
  uncfg-onu-display-info model sn pw 
!
!
onu-pnp
!
no vlan-reserve 4091 out-voip
no vlan-reserve 4092 in-voip
no vlan-reserve 4094 gpon
!
vlan database
  vlan 1,11-19,50,100
!
vlan 12
  description VLAN para uplink
!
vlan 100
  description VLAN_de_QINQ
!
!
!
his-performance sample enable
his-performance alarm enable
his-performance auto-upload disable
!        
!
clock
!
!

!
clock
!
!

!
ptp
!
!
ip dhcp snooping control-port enable
port-identification access-node-id-type inband-mac
port-identification rackno 1 frameno 1
!
igmp enable
mld disable
  mib-compatibility iftable v1
!
ip-source-guard disable
ipv6 nd snooping disable
!

security port-protect enable
!
!
!
virtual-mac flexible-syntax-profile MT
add Ctrl-Byte 0 width 6 index 6
exit
virtual-mac access-node-id 0
!
epm
 mode passthrough


         


!
!
!
interface mng1
  ip address 136.1.1.100 255.255.0.0
  config-filename startrun.dat
  negotiation auto
  tag-mode untag
!
interface vlan 11
!
interface vlan 12
!
interface vlan 50
  ip address 10.200.50.2 255.255.255.252
!
interface vlan 100
!
interface null1
!
interface gpon-olt_1/1/1
  no shutdown
  linktrap disable
!
interface gpon-olt_1/1/2
  no shutdown
  linktrap disable
!
interface gpon-olt_1/1/3
  shutdown
  linktrap disable
  description F601
!
interface gpon-olt_1/1/4
  no shutdown
  linktrap disable
  name testpopjt
  onu 1 type ZTE-F601 sn ZTEGCCE7B888
!
interface gpon-onu_1/1/4:1
  name "testenoc1gb"
  description "testenoc1gb"
  sn-bind enable sn
  tcont 1 profile default
  gemport 1 tcont 1
  service-port 1 vport 1 user-vlan 14 vlan 14 
!
interface gpon-olt_1/1/5
  no shutdown
  linktrap disable
!
interface gpon-olt_1/1/6
  no shutdown
  linktrap disable
!
interface gpon-olt_1/1/7
  no shutdown
  linktrap disable
!
interface gpon-olt_1/1/8
  shutdown
  linktrap disable
!
interface gpon-olt_1/1/9
  no shutdown
  linktrap disable
!
interface gpon-olt_1/1/10
  no shutdown
  linktrap disable
!
interface gpon-olt_1/1/11
  no shutdown
  linktrap disable
!
interface gpon-olt_1/1/12
  no shutdown
  linktrap disable
!
interface gpon-olt_1/1/13
  no shutdown
  linktrap disable
!
interface gpon-olt_1/1/14
  no shutdown
  linktrap disable
!
interface gpon-olt_1/1/15
  no shutdown
  linktrap disable
!
interface gpon-olt_1/1/16
  no shutdown
  linktrap disable
!
interface gei_1/4/1
  no shutdown
  hybrid-attribute fiber
  negotiation auto
  flowcontrol disable
  linktrap enable
  switchport mode trunk
  switchport vlan 1,11-19,50,100 tag
  port-protect disable
  uplink-isolate disable
!
interface xgei_1/4/2
  phy-attribute lan
  shutdown
  hybrid-attribute fiber
  no negotiation auto
  speed 10000
  duplex full
  flowcontrol disable
  linktrap enable
  switchport mode trunk
  switchport vlan 1 tag
  port-protect disable
  uplink-isolate disable
!
interface gei_1/4/3
  no shutdown
  hybrid-attribute copper
  negotiation auto
  flowcontrol disable
  linktrap enable
  switchport mode trunk
  switchport vlan 1,13-14 tag
  port-protect disable
  uplink-isolate disable
!
!
mpls ldp dynamic-capability
!
!
!
!
!
!
!
ip route 0.0.0.0 0.0.0.0 10.200.50.1
!
ipoa inatmarp-interval 10
ipoa gateway-arp-interval 10
!
mpnat trans-table aging-time 60
mpnat onu-telnet idle-time 3
mpnat onu-ftp aging-time 5
mpnat onu-snmp aging-time 30
mpnat onu-ftp-data aging-time 5
mpnat onu-mng-port auto-alloc disable
mpnat modem-telnet idle-time 3
!
pon
!
!
pon-onu-mng gpon-onu_1/1/4:1
  service 1 gemport 1 vlan 14
  vlan port eth_0/1 mode tag vlan 14
!
!
pon
!
!
mac vpn 4cac.0adb.aa4e
!
!
!
auto-write disable
!
inband-management enable
!
username user-suspend mode none 
!
username high-level-security disable
username inactivity-day 120
username pwd-expire-day 90
!
version V4.8.35
!
hostname ZXAN
!
enable secret level 15 5 RcMLuUKvnFZX9kNAV6A/UA==
!
service password-encryption
!
!
username oltcloud password  7 5U3sresLuvB2I+t5+C7zXA== privilege 15 first-login true
username oltcloud password  7 5U3sresLuvB2I+t5+C7zXA== max-sessions 16
username oltcloud enable
username login-range name oltcloud login-begin 00:00:00  login-end 23:59:59
username expire-date name oltcloud datetime 12-31-2099 23:59:59
username password-changed name oltcloud is-changed false

!
!
!
user-authentication-type local
user-authorization-type local
!
help message full
!
banner incoming @
*************************************************************************
Welcome to ZXAN product C320 of ZTE Corporation
*************************************************************************
@
!
message-of-day @
@
!
!
service timestamps log datetime localtime
service timestamps debug datetime localtime
!
!
!
!
snmp-server location No.889 BiBo Rd.PuDong District, Shanghai, China
snmp-server contact +86-21-68895000
snmp-server packetsize 8192
snmp-server engine-id mode mac
snmp-server group GroupPriv15 v3 priv read AllView write AllView
snmp-server group GroupPriv10 v3 priv read AllView write ViewPriv10
snmp-server group GroupPriv5 v3 priv read AllView write ViewPriv5
snmp-server group GroupPriv0 v3 priv read AllView
snmp-server community oltcloud view AllView rw
snmp-server view AllView 1.2 included 
snmp-server view AllView 1.3 included 
snmp-server view ViewPriv5 1.2 included 
snmp-server view ViewPriv5 1.3 included 
snmp-server view ViewPriv5 1.3.6.1.4.1.3902.1082.10.1 excluded 
snmp-server view ViewPriv5 1.3.6.1.4.1.3902.1082.10.10 excluded 
snmp-server view ViewPriv5 1.3.6.1.4.1.3902.1082.20.1 excluded 
snmp-server view ViewPriv5 1.3.6.1.4.1.3902.1082.20.10 excluded 
snmp-server view ViewPriv10 1.2 included 
snmp-server view ViewPriv10 1.3 included 
snmp-server view ViewPriv10 1.3.6.1.4.1.3902.1082.20.10 excluded 
!
!
no ftp-server enable listen 21 
ftp-server top-directory  /flash/ 
!
logging alarmlog enable
logging exc-event auto-write enable
logging level notification
logging cmdlog enable
logging snmplog disable
logging igmplog disable
syslog facility local0
syslog severity 6
syslog hostname-field hostname
line console idle-timeout 15 
line console absolute-timeout 1440 
line telnet idle-timeout 15 
line telnet absolute-timeout 1440 
line telnet users 16 
line cli detail-info-show disable

no hotkey ctrl_g 
no hotkey ctrl_l 
no hotkey ctrl_o 
no hotkey ctrl_r 
no hotkey ctrl_s 
no hotkey ctrl_t 
!
ssh server enable
ssh server authentication mode local
ssh server authentication type pap
no ssh server only
ssh server version 2
!
!
radius attribute vendor-specific vendor-id 3902
!
!
!
radius server-port-check on
!
!
tacacs disable 
tacacs-server timeout 5
tacacs-server deadtime 5
tacacs-server packet 1024
!
!
alarm enable
alarm confirm
alarm trap-confirm retry 3 timeout 20 
nms-hello-trap disable
alarm report-speed 0
alarm anti-jitter 0 
!
end
ZXAN#  
---
