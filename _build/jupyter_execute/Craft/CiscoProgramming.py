#!/usr/bin/env python
# coding: utf-8

# # Cisco Programming
# 
# ## S220 (Custom?)
# 
# Default speed 115200
# 
# ### Helpful commands - Show
# 
# show vlan
# - List the vLAN and show allocations
# 
# show management-vlan
# - show the current server's management vLAN
# 
# show ip
# - show the current switch virtual IP (for management)
# 
# ### Helpful commands - Configure
# 
# configure terminal
# - enter config mode
# 
# interface GigabitEthernet 15
# - set to use port 15
# 
# <hr>
SHOW: S220

aaa                 Show AAA values
access-lists        Display not empty access control lists (ACLs)
                    configured on the switch
arp                 Show the IP ARP translation table
backup-config       Contents of backup configuration
banner              Show the configuration of banners
bonjour             Shows bonjour advertisement status
boot                Shows the status of IP DHCP auto update or auto config
                    process
bootvar             Show boot attributes
bridge              Global bridge table configuration
ca-certificate      CA Certificate information
cable-diagnostics   Copper ports diagnostics
cbd                 CBD host configuration
cdp                 CDP information
class-map           Display QoS class maps, which
                    define the match criteria to classify traffic
clock               Display the time and date from the system clock
cpu                 Displays information about the system CPU utilization
debugging           debugging information
dot1x               802.1x configuration
env                 Environmental facilities
errdisable          Show errdisable state
etherchannel        EtherChannel information
fiber-ports         Fiber ports diagnostics
gvrp                GVRP information
hardware-resource   Display all access control entries(ACEs)
                    configured on this ACL
history             list the last several history commands
hosts               To display the default domain name, a list of name
                    server hosts, the static of host names and addresses
interfaces          Interface status and configuration
ip                  Global IP configuration commands
ipv6                IPV6 configuration
lacp                IEEE 802.3 link aggregation information
line                Show CLI services information
lldp                LLDP information
logging             Show the contents of logging buffers
loopback-detection  loopback-detection
mac                 MAC configuration
management          Management restrictions configuration
management-vlan     Management VLAN configuration
memory              Memory statistics
monitor             Monitor configuration
passwords           Passwords configuration
pnp                 Show PnP status
policy-map          Display QoS policy maps, which
                    define classification criteria for incoming traffic
port                Interface status and configuration
port-security       Show secure port information
privilege           Show current privilege level
qos                 Display quality of service (QoS) mode for the entire device
radius-server       Radius server's configuration
rate-limit          Use the rate-limit interface configuration command to limit 
                    the rate of the incoming traffic. Use the no form of this 
                    command to disable rate limit
rmon                Remote Monitoring (RMON) configuration subcommand
running-config      Current operating configuration
security-suite      Security protections
services            show the open TCP/UDP sessions
snmp-server         show snmp status
sntp                Show Simple Network Time Protocol (SNTP) information
spanning-tree       Spanning tree topology
startup-config      Contents of startup configuration
storm-control       Storm control settings
system              Show system information
tacacs              To display configuration and statistics for TACACS
                    servers
tech-support        Show tech-support information
time-range          Display time-range configured on the switch
username            Display information about local users
users               Display information about users
version             System hardware and software status
vlan                Display VLAN information
voice               Display Voice VLAN informationConfigure: S220

aaa                 Authentication, Authorization and Accounting is used to
                    manage user access to the system
banner              Set banner display message
bonjour             Enables globally MDNS advertisement and responding to
                    MDNS queries
boot                Boot Commands
bridge              Global bridge table configuration
ca-certificate      CA Certificate command
cbd                 CBD host configuration
cdp                 Global CDP configuration subcommands
class-map           This command create class map and enter class map configur
                    ation mode. Use no form in order to delete the class
clock               Manage the system clock
crypto              Global cryptographic features configuration subcommands
default             Set a command to its defaults
dot1x               802.1x configuration
do                  To run exec commands in current mode
eee                 EEE configuration
enable              Modify enable password parameters
encrypted           Encrypted commands for security sensitive data (SSD)
end                 End current mode and change to enable mode
errdisable          Error-Disable shutdown commands
exit                Exit current mode and down to previous mode
gvrp                Global GVRP configuration commands
hostname            Set system's network name
interface           Select an interface to configure
ip                  Global IP configuration commands
ipv6                IPV6 configuration
jumbo-frame         Jumbo Frame configuration
lacp                LACP Configuration
line                To identify a specific line for configuration
lldp                Global LLDP configuration subcommands
logging             Configure message logging facilities
loopback-detection  loopback-detection
mac                 MAC configuration
management          IP management
management-vlan     Management VLAN configuration
monitor             Monitor configuration
no                  Negate a command or set its defaults
passwords           Passwords configuration
pnp                 Configure PnP
policy-map          This command create policy map and enter policy map config
                    uration mode. Use no form to delete the policy map
port                Interface status and configuration
port-channel        EtherChannel configuration
priority-queue      Set priority queue parameters
qos                 Enable/Disable QoS on the device and enter the QoS mode (a
                    dvance/basic)
radius-server       Modify RADIUS parameters
rate-limit          Use the rate-limit interface configuration command to limit 
                    the rate of the incoming traffic. Use the no form of this 
                    command to disable rate limit
rmon                Remote Monitoring (RMON) configuration subcommand
security-suite      Security protections
service             Service options
snmp-server         Modify SNMP engine parameters
sntp                Configure sntp
spanning-tree       Spanning Tree Subsystem
storm-control       Storm control settings
tacacs-server       TACACS server command
time-range          Enters time-range configuration mode and defines time ranges 
                    for functions
traffic-shape       Shaper configuration
username            Establish User Name Authentication
vlan                VLAN commands
voice               Voice management
wrr-queue           Configure queue drop mechanism on egress portS220 : Interface Config

back-pressure       Enable back-pressure
cdp                 CDP interface subcommands
channel-group       Etherchannel/port bundling configuration
description         Interface specific description
dot1x               802.1x configuration
do                  To run exec commands in current mode
duplex              Configure duplex operation
eee                 EEE configuration
end                 End current mode and change to enable mode
exit                Exit from current mode
flowcontrol         Configure flow-control mode
gvrp                GVRP interface commands
ip                  Global IP configuration commands
ipv6                IPV6 configuration
lacp                LACP Configuration
lldp                LLDP interface subcommands
loopback-detection  loopback-detection
mac                 MAC configuration
no                  Negate a command or set its defaults
operation           Port operation time command
qos                 Enable/Disable QoS on the device and enter the QoS mode (advance/basic)
rate-limit          Use the rate-limit interface configuration command to limit the rate of the incoming traffic.                       Use the no form of this command to disable rate limit
security-suite      Security protections
service-policy      Apply a policy map to particular interface.Only one policy map per interface per direction is                       supported
shutdown            Shutdown the selected interface
spanning-tree       Spanning Tree Subsystem
speed               Configure speed operation
storm-control       Storm control settings
switchport          Configure switch port definition in VLAN
traffic-shape       Shaper configuration
voice               Voice management

# ## SG350 (IOS)
# 
# Modes of operation
# 
# ### User
# You will have "[name]>" in your console<br>
# "Exit" will disconnect your session (drops your level instead if you're higher)
# - ping
# - show
# - etc
# 
# Enable moves you to Privileged
# 
# ### Privileged
# You will have "[name]#" in your console<br>
# Disable drops you back to user mode
# - User +
# - debug
# - reload (reboot)
# 
# "configure terminal" moves you to global config<br>
# 
# ### Global Commands
# You will have a "[name] (config)#" in your console<br>
# 
# hostname, enable secret (sets the password), ip route<br>
# 
# "Interface enternet/serial/dsl/vlan/etc" moves you to interface configuration<br>
# "line " moves you to line configuration
# 
# #### Interface Configuration
# You will have a "[name] (config-if)#" in your console<br>
# "end" will drop you to "priveleged" mode (2 levels). CTRL+Z also does this
# 
# #### Line Configuration
# You will have a "[name] (config-line)#" in your console
# 
# 

# ## Useful commands
# 
# CTRL+A - move to the start of the line
# 
# show running-config<br>
# show startup-config<br>
# show backup-config<br>
# - all config
# 
# show version
# - uptime
# - restart reason
# - OS version, etc
# - features, etc
# 
# show interface
# 
# From Privileged mode:<br>
# enable password : Sets the pasword for EXEC mode<br>
# enable secret : Same as password, but encrypts the password. This is the only one that does it<br>
# From Config-line mode:<br>
# console password : Sets the console password<br>
# VTY password : Sets the telnet password<br>
# 
# service password-encryption : dont store the passwords in the config<br>
# 
# from config<br>
# banner motd # [messaage in here] #<br>
# 
# from Privileged mode
# copy running-config startup-config<br>
# erase startup-config <br>
# on switch : delete vlan.dat ... why? <br>
# 
# 
# Port is physical, interface is virtual<br>
# All ports are interfaces, not all interfaces are ports<br>
# 
# configure virtual interface 1
# interface vlan 1<br> 
# ip address IP SUB<br>
# no shutdown<br>

# In[ ]:




